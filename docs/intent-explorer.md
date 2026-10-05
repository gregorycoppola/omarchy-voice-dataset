# Python intent explorer

Version 2 now defines structured schemas for all 227 intents. See
[the current model and workflow](structured-intents.md). Historical counts and
example lists below describe the original audit; use `data/catalog.json` and
the browser explorer for current definitions.

Run from the repository root with Python 3.10 or newer. The library loads all
JSON files in `data/` and links the 227 outcome objects to their ten utterances.
It does not execute desktop commands.

```python
from intent_explorer import IntentExplorer

explorer = IntentExplorer.load()
for intent in explorer.iter_intents():
    print(intent.id, intent.status, intent.slots)
    for utterance in explorer.iter_utterances(intent.id):
        print(utterance.variant, utterance.text, utterance.arguments)

# Or stream all labeled examples directly:
for intent, utterance in explorer.iter_pairs(prefix="browser."):
    print(intent.id, utterance.text)

# Other source data is available by JSON file stem:
projects = explorer.raw("projects")
surfaces = explorer.raw("source-surfaces")
```

`Intent` exposes `id`, `status`, `slots`, `mapped_projects`, `support`, and an
ordered tuple of `utterances`. `Utterance` exposes `intent`, `variant`, `text`,
`arguments`, `origin`, `base_variant`, and `frame`. `arguments=None` means the
row has not received argument labels. `get_intent(id)` raises `KeyError` for
unknown IDs. Pass a repository path to `IntentExplorer.load(path)` to read
another checkout.

From a shell:

```bash
python -m intent_explorer stats
python -m intent_explorer list --prefix browser.
python -m intent_explorer show app.launch
python -m intent_explorer show app.launch --json
python -m intent_explorer walk --prefix audio.
python -m intent_explorer walk --prefix audio. --no-prompt
python -m intent_explorer segment "open the browser and tile" --json
python -m intent_explorer sequences
python -m intent_explorer compose browser.open:1 window.tile:1 --join and
```

`walk` pauses after each intent on an interactive terminal. Enter advances;
`q` quits. With `--no-prompt` or redirected input, it prints all matches.
`show --json` returns one machine-readable object. For bulk processing, use
the Python API or [utterances.json](../data/utterances.json).

`segment_utterance(text)` returns raw clause spans with character offsets.
Curated [segmentation examples](../data/segmentation-examples.json) also
include intent labels, Skipper source rule IDs, and context bindings. Unknown
phrases get `intent=None` for a future classifier. See the
[segmentation design](segmentation.md).

`iter_sequences()`, `get_sequence(id)`, and `compose_sequence(step_refs,
connector)` expose ordered command sequences. A step reference is an
`(intent_id, variant_number)` tuple. See [command sequences](command-sequences.md)
for the data format and source macro distinction.

The ten variants comprise two authored illustrations and eight synthetic
request frames. `origin`, `base_variant`, and `frame` let experiments separate
them. A parser comparison must split by base phrase or use independently
written holdout phrases; random row splits leak almost identical wording
between training and test sets. See [parsing strategies](parsing-strategies.md).
