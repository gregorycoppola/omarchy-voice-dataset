# Commands and sequences

An **intent** names one requested action, such as `browser.open` or
`window.tile`. A **command sequence** is an ordered list of those actions.
The word `and`, `then`, or a line break is a way to *say* the sequence; it is
not part of either intent ID.

```text
Open the browser and tile open windows
  1. browser.open     → "Open the browser"
  2. window.tile      → "Tile open windows"
```

[command-sequences.json](../data/command-sequences.json) stores each sequence
with an ID, utterance, connector, ordered step references (`intent` plus
`variant`), context bindings, and evidence label. The Python API resolves
those references to the full standalone utterance objects. The same atomic
commands can be joined with different connectors without copying them.

```python
from intent_explorer import IntentExplorer

explorer = IntentExplorer.load()
for sequence in explorer.iter_sequences():
    print(sequence.id, sequence.utterance)
    for step in sequence.steps:
        print(step.intent, step.variant, step.text)

proposed = explorer.compose_sequence(
    [("browser.open", 1), ("window.tile", 1)], connector="and"
)
print(proposed.utterance)  # Open the browser and tile open windows
```

```bash
python -m intent_explorer sequences
python -m intent_explorer sequence skipper.browser_open_tile_pair --json
python -m intent_explorer compose browser.open:1 window.tile:1 --join and --json
```

`compose_sequence` produces a **proposed example**. It does not claim that
Skipper or another project recognizes or can execute the combined phrase.
It requires two or more standalone imperative variants and accepts `and`,
`then`, or `newline` as the connector.

Skipper's source rule for **“open the browser and tile”** is recorded as a
`source_macro`: it implements `browser.open` followed by `window.tile_pair`
with the originally focused window and browser as the pair. Its surface
utterance abbreviates the second command to “tile.” It is not equivalent to
**“open the browser and tile open windows,”** whose second step is
`window.tile` over the current workspace. See the
[segmentation examples](segmentation.md) for this distinction.

The planned parsing flow is: split a spoken utterance into clauses, classify
each clause as one intent, resolve references and arguments, then select an
executor or source macro for the resulting sequence. The current segmenter
labels only curated examples; arbitrary composed phrases are input for a
future parser, not a measured parser result.
