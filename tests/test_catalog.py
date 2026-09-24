import copy
import unittest
from intent_explorer import Catalog, IntentExplorer


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = Catalog()

    def test_every_intent_has_schema_examples_and_bindable_templates(self):
        self.assertEqual(len(self.catalog.intents), 223)
        for row in self.catalog.intents.values():
            self.assertEqual(row['arguments_schema']['type'], 'object')
            self.assertFalse(row['arguments_schema']['additionalProperties'])
            self.assertEqual(len(row['examples']), 10)
            self.assertEqual(len(row['grammar']), 10)
            for example in row['examples']:
                self.catalog.validate_instance({'intent': row['id'], 'arguments': example['arguments']})

    def test_invalid_llm_arguments_rejected(self):
        invalid = [
            {'intent': 'made.up', 'arguments': {}},
            {'intent': 'browser.open', 'arguments': {}},
            {'intent': 'browser.open', 'arguments': {'browser': 'default', 'presentation': 'huge'}},
            {'intent': 'system.lock', 'arguments': {'shell': 'anything'}},
            {'intent': 'audio.volume_set', 'arguments': {'percent': 101}},
            {'intent': 'workspace.switch', 'arguments': {'workspace': True}},
            {'intent': 'window.focus', 'arguments': {'target': {'kind': 'id'}}},
        ]
        for instance in invalid:
            with self.subTest(instance=instance), self.assertRaises(ValueError):
                self.catalog.validate_instance(instance)

    def test_context_names_are_preserved_without_inventing_ids(self):
        definition = self.catalog.intents['browser.download']
        args = definition['examples'][0]['arguments']
        self.assertEqual(args['target'], {'kind': 'context', 'value': 'this file'})
        self.assertEqual(args['destination']['kind'], 'context')

    def test_result_reference_requires_an_earlier_step(self):
        plan = self.catalog.canonical_plan('skipper', 'open_browser_and_tile',
                                          {'first': 'this window', 'second': 'the browser'})
        self.assertEqual(plan[1]['arguments']['second'], {'kind': 'result', 'value': 'open_browser.window'})
        with self.assertRaises(ValueError):
            self.catalog.validate_plan(list(reversed(plan)))

    def test_llm_schema_is_subset_and_does_not_mutate_catalog(self):
        before = copy.deepcopy(self.catalog.intents['browser.open']['arguments_schema'])
        context = self.catalog.llm_context(['browser.open'], {'browsers': ['default']})
        self.assertEqual(len(context['output_schema']['oneOf']), 1)
        self.assertTrue(context['intents'][0]['grammar'])
        context['output_schema']['oneOf'][0]['properties']['arguments']['properties'].clear()
        self.assertEqual(self.catalog.intents['browser.open']['arguments_schema'], before)

    def test_stored_sequences_keep_contextual_arguments(self):
        explorer = IntentExplorer.load()
        sequence = explorer.get_sequence('skipper.browser_open_tile_pair')
        self.assertEqual(sequence.steps[0].arguments['presentation'], 'normal')
        self.assertEqual(explorer.get_intent('browser.open').utterances[0].arguments['presentation'], 'fullscreen')


if __name__ == '__main__':
    unittest.main()
