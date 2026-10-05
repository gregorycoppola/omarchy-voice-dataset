import unittest

from intent_explorer import IntentExplorer


class IntentExplorerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.explorer = IntentExplorer.load()

    def test_complete_iteration(self):
        intents = list(self.explorer.iter_intents())
        pairs = list(self.explorer.iter_pairs())
        self.assertEqual(len(intents), 227)
        self.assertEqual(len(pairs), 2270)
        self.assertTrue(all(len(intent.utterances) == 10 for intent in intents))
        self.assertEqual(len(list(self.explorer.iter_intents("audio."))), 6)

    def test_typed_arguments_follow_source_variant(self):
        intent = self.explorer.get_intent("app.launch")
        self.assertEqual(intent.utterances[0].arguments, {"application": "firefox"})
        self.assertEqual(intent.utterances[2].arguments, {"application": "firefox"})
        self.assertEqual(intent.utterances[6].arguments, {"application": "browser"})
        self.assertEqual(intent.utterances[2].base_variant, 1)
        self.assertEqual(intent.utterances[6].base_variant, 2)

    def test_candidate_arguments_are_structured(self):
        intent = self.explorer.get_intent("coding.pane.split")
        self.assertEqual(intent.status, "schema_defined")
        self.assertTrue(all(isinstance(utterance.arguments, dict) for utterance in intent.utterances))
        self.assertEqual(intent.utterances[0].arguments["orientation"], "vertical")
        self.assertTrue(self.explorer.raw("projects"))

    def test_skipper_compound_keeps_pair_layout(self):
        result = self.explorer.segment_utterance("open the browser and tile")
        self.assertEqual([s.intent for s in result.segments], ["browser.open", "window.tile_pair"])
        self.assertEqual(result.source_command, "browser:open_tile")
        self.assertEqual(result.bindings["first_window"], "original_focused")

    def test_and_inside_target_does_not_split(self):
        result = self.explorer.segment_utterance("tile this window and the browser")
        self.assertEqual(len(result.segments), 1)
        self.assertEqual(result.segments[0].intent, "window.tile_pair")

    def test_unknown_phrase_splits_without_guessing_intent(self):
        result = self.explorer.segment_utterance("open the browser\nwrite a poem")
        self.assertEqual([s.text for s in result.segments], ["open the browser", "write a poem"])
        self.assertEqual([s.intent for s in result.segments], [None, None])

    def test_all_windows_phrase_is_only_proposed(self):
        result = self.explorer.segment_utterance("open the browser and tile the windows")
        self.assertEqual([s.intent for s in result.segments], ["browser.open", "window.tile"])
        self.assertEqual(result.evidence, "proposed_combination")
        self.assertIsNone(result.source_command)

    def test_source_macro_sequence_keeps_two_atomic_steps(self):
        sequence = self.explorer.get_sequence("skipper.browser_open_tile_pair")
        self.assertEqual([step.intent for step in sequence.steps],
                         ["browser.open", "window.tile_pair"])
        self.assertEqual(sequence.source_command, "browser:open_tile")
        self.assertEqual(sequence.composition, "source_macro")

    def test_composition_reuses_standalone_variants(self):
        sequence = self.explorer.compose_sequence(
            [("browser.open", 1), ("window.tile", 1)], connector="and")
        self.assertEqual(sequence.utterance, "Open the browser and tile open windows")
        self.assertEqual(sequence.evidence, "generated_example")
        self.assertIsNone(sequence.source_command)
        lines = self.explorer.compose_sequence(
            [("browser.open", 1), ("window.tile", 1)], connector="newline")
        self.assertEqual(lines.utterance, "Open the browser\nTile open windows")

    def test_composition_requires_two_imperatives(self):
        with self.assertRaises(ValueError):
            self.explorer.compose_sequence([("browser.open", 1)])
        with self.assertRaises(ValueError):
            self.explorer.compose_sequence([("system.time_query", 1), ("browser.open", 1)])


if __name__ == "__main__":
    unittest.main()
