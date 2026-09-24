# Structured intent catalog and Skipper integration

The active source of truth is `data/catalog.json`: 223 named intents with closed
JSON argument schemas, ten labeled examples each, and grammar templates binding
spoken slots into those arguments. These are authored shared contracts. A schema
being defined does not establish that every upstream project implements it.
Source mappings retain their audit evidence and provider adapters establish the
argument combinations that can actually execute.

```json
{
  "intent": "window.focus",
  "arguments": {"target": {"kind": "named", "value": "GitHub"}}
}
```

A target reference has a `kind`: `current`, `named`, `id`, `application`, `all`,
`context`, or `result`. All except `current` also carry a `value`. `named` and
`context` values need resolution; they are not invented window addresses.
An `id` must be supplied by the captured environment. A `result` such as
`open_browser.window` names an earlier step's output. Missing email bodies,
ambiguous routine times, and other incomplete requests need clarification before
an executor can act. `null` in an individual optional field records missing or
unspecified information; the complete arguments object is never null.

## Files to edit

- `data/catalog.json`: shared intent schemas, descriptions, examples, and illustrative
  grammar templates. A template's `slots` records argument paths and example values;
  its nested `arguments` binds `$slot` leaves. These templates describe the examples
  and are not automatically enabled executable grammar.
- `data/providers/skipper.json`: Skipper's active grammar patterns, fixed vocabulary,
  dynamic vocabulary providers, executor argument bindings, and exact alias references.
  Every expansion is translated to canonical arguments and validated at compilation.
- `data/command-sequences.json`: ordered intent instances with explicit arguments
  and step IDs. A macro's contextual arguments can differ from standalone examples.

`intents.json`, `outcomes.json`, `utterances.json`, and `llm-intents.schema.json`
are generated views. Regenerate them with `python scripts/export_catalog.py`.
The Python API and browser explorer read the authored catalog directly.

## Python and LLM API

```python
from intent_explorer import IntentExplorer

explorer = IntentExplorer.load()
for intent in explorer.iter_intents():
    print(intent.id, intent.arguments_schema)
    for phrase in intent.utterances:
        instance = {"intent": intent.id, "arguments": phrase.arguments}
        explorer.validate_instance(instance)
        print(phrase.text, instance)
    for rule in intent.grammar:
        print(rule["pattern"], rule["slots"], rule["arguments"])

payload = explorer.llm_context(
    ["browser.open", "window.focus"],
    context={"windows": [{"id": "window-1", "title": "GitHub"}]},
)
# payload contains definitions, grammar, examples, context, and output_schema.
# Send this to your chosen model; this API itself makes no model calls.
explorer.validate_instance({
    "intent": "browser.open",
    "arguments": {"browser": "default", "presentation": "fullscreen"},
})
```

`python -m intent_explorer schema browser.open window.focus` exports JSON Schema
2020-12. Model APIs may require a provider-specific wrapper around that schema.
The stdlib validator implements the subset of JSON Schema used in this catalog.
The catalog API also exposes `validate_plan` and `canonical_plan` for provider
bindings. Plan validation checks that result references point backward.

## Application boundary

Skipper's `dataset-reference.json` names this checkout. `OMARCHY_INTENT_DATASET`
can point to another checkout. There is no copy/import step and no bundled fallback.
A missing or invalid dataset produces an actionable startup error. Restart Skipper
and its native Explorer after edits to load a consistent revision; the browser
explorer reads the current catalog on refresh.

The application still owns audio, grammar compilation, confidence thresholds,
window discovery/resolution, confirmation, and execution handlers. Its old
execution IDs remain an adapter interface for saved corrections and existing
runtime code. `ParseResult.canonical_plan` exposes the shared intent instances,
and diagnostics record the catalog revision and this plan.

`IntentMatcher.parse_instance(instance, extra_expansions=...)` accepts validated
structured input and finds an existing executor binding. Unknown argument
combinations return an unrecognized result. A valid schema alone does not enable a
command. Live window expansions can be supplied so captured IDs can resolve.
The native Explorer's **Shared intents** tab displays all contracts; **Try a
command** displays the canonical parse. No LLM service has been connected yet.

## Historical audit and corrections

The original 55 typed seed intents, 168 schema gaps, and old example labels are
preserved under `data/history/2026-09-24/`. The source snapshot and crosswalk remain
the dated audit. `scripts/check.py` validates the current catalog;
`scripts/check_source_snapshot.py` separately checks whether current source
checkouts still equal the old frozen audit. Development changes are expected to
make the latter fail; do not rewrite the historical hashes to hide this.

During schema work, source inspection corrected three earlier example mistakes:
Genesis `system.idle_set` selects stay-awake/allow-idle rather than a timeout;
Omause `speech.route` starts the voice router rather than selecting headphones;
Herdr `coding.notification.show` displays a title/message rather than listing
notifications. The historical examples remain available for comparison.

## Verification and release

Run `python scripts/check.py` and `python -m unittest discover -s tests` here,
then the relevant parser and resolver tests in Skipper. The migration also compared
all 293 existing static Skipper expansions against their previous wording,
execution IDs, and executor arguments. Those values were unchanged.

This dataset is maintained separately from Skipper. Public releases are clean
snapshots at https://github.com/gregorycoppola/omarchy-voice-dataset, without private
development history. Skipper installers pin a matching public commit; development
can still reference a local working checkout. Personal overrides never belong here.
