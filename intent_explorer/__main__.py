"""Command-line explorer for the intent dataset."""

import argparse
from dataclasses import asdict
import json
import sys

from . import IntentExplorer


def show(intent, as_json=False):
    if as_json:
        print(json.dumps(asdict(intent), indent=2, ensure_ascii=False))
        return
    print(f"{intent.id}  [{intent.status}]  {len(intent.utterances)} utterances")
    if intent.slots:
        print("Slots: " + ", ".join(f"{key}: {value}" for key, value in intent.slots.items()))
    for utterance in intent.utterances:
        print(f"  {utterance.variant:>2}. {utterance.text}  [{utterance.origin}]")


def show_sequence(sequence, as_json=False):
    if as_json:
        print(json.dumps(asdict(sequence), indent=2, ensure_ascii=False))
        return
    print(f"{sequence.id or '(generated)'}  [{sequence.evidence}]  {sequence.utterance!r}")
    for number, step in enumerate(sequence.steps, start=1):
        print(f"  {number}. {step.intent}:{step.variant} — {step.text}")
    if sequence.source_command:
        print(f"  Source command: {sequence.source_command}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    list_cmd = sub.add_parser("list", help="list all intent IDs")
    list_cmd.add_argument("--prefix", help="restrict intent IDs")
    show_cmd = sub.add_parser("show", help="show one intent and its ten variants")
    show_cmd.add_argument("intent_id")
    show_cmd.add_argument("--json", action="store_true", help="emit one machine-readable object")
    walk_cmd = sub.add_parser("walk", help="step through intents and utterances")
    walk_cmd.add_argument("--prefix", help="restrict intent IDs")
    walk_cmd.add_argument("--no-prompt", action="store_true", help="print all matches without pausing")
    segment_cmd = sub.add_parser("segment", help="split a phrase into intent clauses")
    segment_cmd.add_argument("text", nargs="*", help="phrase to split")
    segment_cmd.add_argument("--stdin", action="store_true", help="read the phrase from standard input")
    segment_cmd.add_argument("--json", action="store_true", help="emit a machine-readable result")
    sub.add_parser("sequences", help="list stored command sequences")
    sequence_cmd = sub.add_parser("sequence", help="show a stored command sequence")
    sequence_cmd.add_argument("sequence_id")
    sequence_cmd.add_argument("--json", action="store_true")
    compose_cmd = sub.add_parser("compose", help="join atomic command examples")
    compose_cmd.add_argument("steps", nargs="+", metavar="INTENT:VARIANT")
    compose_cmd.add_argument("--join", choices=("and", "then", "newline"), default="and")
    compose_cmd.add_argument("--json", action="store_true")
    sub.add_parser("stats", help="show dataset counts")
    schema_cmd = sub.add_parser('schema', help='export an LLM output schema')
    schema_cmd.add_argument('intents', nargs='*', help='intent IDs; defaults to all')
    args = parser.parse_args(argv)
    explorer = IntentExplorer.load()
    if args.command == 'schema':
        print(json.dumps(explorer.catalog.llm_schema(args.intents or None), indent=2))
    elif args.command == "list":
        for intent in explorer.iter_intents(args.prefix):
            print(f"{intent.id}\t{intent.status}\t{len(intent.utterances)}")
    elif args.command == "show":
        try:
            show(explorer.get_intent(args.intent_id), args.json)
        except KeyError:
            parser.error(f"unknown intent: {args.intent_id}")
    elif args.command == "walk":
        for intent in explorer.iter_intents(args.prefix):
            show(intent)
            if not args.no_prompt and sys.stdin.isatty():
                answer = input("Enter for next intent, q to quit: ").strip().lower()
                if answer == "q":
                    break
    elif args.command == "segment":
        phrase = sys.stdin.read() if args.stdin else " ".join(args.text)
        if not phrase.strip():
            parser.error("provide text or use --stdin")
        result = explorer.segment_utterance(phrase)
        if args.json:
            print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
        else:
            print(f"Evidence: {result.evidence}")
            if result.source_command:
                print(f"Skipper command: {result.source_command}")
            for index, segment in enumerate(result.segments, start=1):
                print(f"{index}. {segment.text} → {segment.intent or 'unlabeled'}")
    elif args.command == "sequences":
        for sequence in explorer.iter_sequences():
            print(f"{sequence.id}\t{sequence.evidence}\t{sequence.utterance.replace(chr(10), ' / ')}")
    elif args.command == "sequence":
        try:
            show_sequence(explorer.get_sequence(args.sequence_id), args.json)
        except KeyError:
            parser.error(f"unknown sequence: {args.sequence_id}")
    elif args.command == "compose":
        try:
            refs = [(intent_id, int(variant)) for intent_id, variant in
                    (text.rsplit(":", 1) for text in args.steps)]
            show_sequence(explorer.compose_sequence(refs, args.join), args.json)
        except (ValueError, KeyError) as exc:
            parser.error(str(exc))
    elif args.command == "stats":
        total = sum(len(intent.utterances) for intent in explorer.iter_intents())
        print(f"{len(explorer)} intents, {total} utterances, "
              f"{sum(i.status == 'schema_defined' for i in explorer.iter_intents())} typed intents, "
              f"{sum(1 for _ in explorer.iter_sequences())} stored sequences")


if __name__ == "__main__":
    main()
