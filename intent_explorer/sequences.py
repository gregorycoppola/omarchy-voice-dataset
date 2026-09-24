"""Machine-readable ordered command sequences built from atomic intent examples."""

from dataclasses import dataclass
from typing import Any, Iterable

CONNECTORS = {"and": " and ", "then": ", then ", "newline": "\n"}


@dataclass(frozen=True)
class SequenceStep:
    intent: str
    variant: int
    text: str
    arguments: dict[str, Any] | None
    id: str | None = None


@dataclass(frozen=True)
class CommandSequence:
    id: str | None
    utterance: str
    connector: str
    composition: str
    evidence: str
    steps: tuple[SequenceStep, ...]
    source_command: str | None
    bindings: dict[str, Any]


def join_steps(steps: Iterable[SequenceStep], connector: str) -> str:
    """Join standalone imperative examples; reject question-shaped examples."""
    if connector not in CONNECTORS:
        raise ValueError(f"unknown connector: {connector}")
    steps = tuple(steps)
    if len(steps) < 2:
        raise ValueError("a sequence needs at least two commands")
    clauses = []
    for index, step in enumerate(steps):
        phrase = step.text.strip()
        if not phrase or phrase.endswith("?"):
            raise ValueError(f"choose an imperative variant for {step.intent}")
        phrase = phrase.rstrip(".! ")
        if index and connector != "newline":
            phrase = phrase[0].lower() + phrase[1:]
        clauses.append(phrase)
    return CONNECTORS[connector].join(clauses)
