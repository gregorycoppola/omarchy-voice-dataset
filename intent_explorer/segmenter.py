"""Structural utterance segmentation with a small labeled Skipper fixture set.

This does not infer arbitrary intent IDs. It splits explicit separators and
attaches labels only to the curated examples in segmentation-examples.json.
"""

from dataclasses import dataclass
import re
from typing import Any

_ACTION_START = r"open|launch|tile|close|show|list|start|stop|set|turn|move|focus|switch|read|send|run|play|pause"
_SEPARATOR = re.compile(
    rf"\s*(?:\n+|;|\band\s+then\b|\bthen\b|\band\b(?=\s+(?:{_ACTION_START})\b))\s*",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class IntentSegment:
    text: str
    start: int
    end: int
    intent: str | None


@dataclass(frozen=True)
class Segmentation:
    utterance: str
    segments: tuple[IntentSegment, ...]
    evidence: str
    source_rule: str | None
    source_command: str | None
    bindings: dict[str, Any]


def _key(text: str) -> str:
    return " ".join(text.casefold().split())


def split_clauses(text: str) -> tuple[IntentSegment, ...]:
    """Split explicit line/sequence boundaries; leave intent labels unknown."""
    spans = []
    start = 0
    for match in _SEPARATOR.finditer(text):
        spans.append((start, match.start()))
        start = match.end()
    spans.append((start, len(text)))
    result = []
    for start, end in spans:
        raw = text[start:end]
        left = len(raw) - len(raw.lstrip())
        right = len(raw.rstrip())
        if right > left:
            result.append(IntentSegment(raw[left:right], start + left, start + right, None))
    return tuple(result)


class Segmenter:
    def __init__(self, examples: list[dict[str, Any]]):
        self._examples = {_key(row["utterance"]): row for row in examples}
        if len(self._examples) != len(examples):
            raise ValueError("duplicate segmentation example")

    def segment(self, utterance: str) -> Segmentation:
        """Return clauses and offsets; label only exact curated example wording."""
        segments = split_clauses(utterance)
        example = self._examples.get(_key(utterance))
        if example:
            expected = example["segments"]
            if [_key(s.text) for s in segments] != [_key(s["text"]) for s in expected]:
                raise ValueError(f"segmentation example does not match splitter: {utterance}")
            segments = tuple(IntentSegment(s.text, s.start, s.end, label["intent"])
                             for s, label in zip(segments, expected, strict=True))
        return Segmentation(
            utterance=utterance,
            segments=segments,
            evidence=example["evidence"] if example else "unlabeled_split",
            source_rule=example["source_rule"] if example else None,
            source_command=example["source_command"] if example else None,
            bindings=example["bindings"] if example else {},
        )
