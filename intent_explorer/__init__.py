"""Read and iterate the local Omarchy voice intent dataset.

Example::

    from intent_explorer import IntentExplorer
    explorer = IntentExplorer.load()
    for intent in explorer.iter_intents():
        for utterance in explorer.iter_utterances(intent.id):
            print(intent.id, utterance.text)
"""

from dataclasses import dataclass, replace
import json
from pathlib import Path
from typing import Any, Iterator

from .segmenter import IntentSegment, Segmentation, Segmenter
from .sequences import CommandSequence, SequenceStep, join_steps
from .catalog import Catalog

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Utterance:
    intent: str
    variant: int
    text: str
    arguments: dict[str, Any] | None
    origin: str
    base_variant: int | None
    frame: str | None


@dataclass(frozen=True)
class Intent:
    id: str
    status: str
    slots: dict[str, Any]
    mapped_projects: tuple[str, ...]
    support: dict[str, Any] | None
    utterances: tuple[Utterance, ...]
    arguments_schema: dict[str, Any]
    grammar: tuple[dict[str, Any], ...]


class IntentExplorer:
    """Validated in-memory view of all JSON data and linked intent records."""

    def __init__(self, root: Path, raw_data: dict[str, Any]):
        self.root = root
        self._raw_data = raw_data
        self.catalog = Catalog(root)
        typed = {row["id"]: row for row in raw_data["intents"]["intents"]}
        utterances: dict[str, list[Utterance]] = {}
        for definition in self.catalog.intents.values():
            for row in definition['examples']:
                utterances.setdefault(row["intent"], []).append(Utterance(**row))
        self._intents: dict[str, Intent] = {}
        for row in self.catalog.intents.values():
            intent_id = row["id"]
            variants = tuple(sorted(utterances.pop(intent_id, []), key=lambda item: item.variant))
            if len(variants) != 10 or [item.variant for item in variants] != list(range(1, 11)):
                raise ValueError(f"{intent_id}: expected variants 1 through 10")
            source = typed.get(intent_id)
            self._intents[intent_id] = Intent(
                id=intent_id,
                status=row["status"],
                slots=row["arguments_schema"]['properties'],
                mapped_projects=tuple(row["mapped_projects"]),
                support=source["support"] if source else None,
                utterances=variants,
                arguments_schema=row['arguments_schema'],
                grammar=tuple(row['grammar']),
            )
        if utterances or set(typed) - self._intents.keys():
            raise ValueError("utterance or typed intent IDs do not match outcomes")
        self._segmenter = Segmenter(raw_data["segmentation-examples"]["examples"])
        self._sequences: dict[str, CommandSequence] = {}
        for row in raw_data["command-sequences"]["sequences"]:
            steps = tuple(replace(self._step(item["intent"], item["variant"]),
                                  arguments=item['arguments'], id=item.get('id')) for item in row["steps"])
            for step in steps:
                self.catalog.validate_instance({'intent': step.intent, 'arguments': step.arguments})
            self.catalog.validate_plan([{**({'id': s.id} if s.id else {}),
                                         'intent': s.intent, 'arguments': s.arguments} for s in steps])
            if row["composition"] == "joined_standalone_commands" and \
                    join_steps(steps, row["connector"]) != row["utterance"]:
                raise ValueError(f"sequence text differs from referenced commands: {row['id']}")
            if row["id"] in self._sequences:
                raise ValueError(f"duplicate sequence ID: {row['id']}")
            self._sequences[row["id"]] = CommandSequence(
                id=row["id"], utterance=row["utterance"], connector=row["connector"],
                composition=row["composition"], evidence=row["evidence"], steps=steps,
                source_command=row["source_command"], bindings=row["bindings"],
            )

    @classmethod
    def load(cls, root: str | Path | None = None) -> "IntentExplorer":
        """Load every JSON file in ``root/data``; default to this package's repo."""
        path = Path(root) if root is not None else DEFAULT_ROOT
        raw_data = {file.stem: json.loads(file.read_text()) for file in (path / "data").glob("*.json")}
        required = {"intents", "outcomes", "utterances", "segmentation-examples", "command-sequences"}
        if not required <= raw_data.keys():
            raise ValueError(f"missing data files: {sorted(required - raw_data.keys())}")
        return cls(path, raw_data)

    def raw(self, name: str) -> Any:
        """Return another parsed dataset by stem, e.g. ``raw('projects')``."""
        return self._raw_data[name]

    def get_intent(self, intent_id: str) -> Intent:
        """Return one intent; raise ``KeyError`` if the ID is absent."""
        return self._intents[intent_id]

    def validate_instance(self, instance):
        return self.catalog.validate_instance(instance)

    def llm_context(self, intent_ids=None, context=None):
        return self.catalog.llm_context(intent_ids, context)

    def iter_intents(self, prefix: str | None = None) -> Iterator[Intent]:
        """Yield intent objects in ID order, optionally restricted by prefix."""
        for intent_id in sorted(self._intents):
            if prefix is None or intent_id.startswith(prefix):
                yield self._intents[intent_id]

    def iter_utterances(self, intent_id: str) -> Iterator[Utterance]:
        """Yield the ten labeled variants for one intent in variant order."""
        yield from self.get_intent(intent_id).utterances

    def iter_pairs(self, prefix: str | None = None) -> Iterator[tuple[Intent, Utterance]]:
        """Yield every (intent, utterance) pair for streaming experiments."""
        for intent in self.iter_intents(prefix):
            for utterance in intent.utterances:
                yield intent, utterance

    def segment_utterance(self, text: str) -> Segmentation:
        """Split one utterance; known fixtures include intent labels and source IDs."""
        return self._segmenter.segment(text)

    def _step(self, intent_id: str, variant: int) -> SequenceStep:
        intent = self.get_intent(intent_id)
        if not 1 <= variant <= len(intent.utterances):
            raise ValueError(f"invalid variant {variant} for {intent_id}")
        utterance = intent.utterances[variant - 1]
        return SequenceStep(intent_id, variant, utterance.text, utterance.arguments)

    def iter_sequences(self) -> Iterator[CommandSequence]:
        """Yield stored source and proposed sequences in ID order."""
        for sequence_id in sorted(self._sequences):
            yield self._sequences[sequence_id]

    def get_sequence(self, sequence_id: str) -> CommandSequence:
        """Return a stored sequence; raise ``KeyError`` if unknown."""
        return self._sequences[sequence_id]

    def compose_sequence(self, step_refs: list[tuple[str, int]], connector: str = "and") -> CommandSequence:
        """Construct a proposed sequence from standalone utterance variants."""
        steps = tuple(self._step(intent_id, variant) for intent_id, variant in step_refs)
        return CommandSequence(None, join_steps(steps, connector), connector,
                               "joined_standalone_commands", "generated_example", steps, None, {})

    def __len__(self) -> int:
        return len(self._intents)


__all__ = ["Catalog", "CommandSequence", "Intent", "IntentExplorer", "IntentSegment", "Segmentation",
           "SequenceStep", "Utterance"]
