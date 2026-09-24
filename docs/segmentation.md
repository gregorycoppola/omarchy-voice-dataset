# Separate requested intents from Skipper commands

Skipper has a source rule for **“open the browser”** and another for
**“open the browser and tile.”** The previous one-label crosswalk described
the second rule only as `window.tile`. That lost the browser-opening request
and the two-window layout. The revised [crosswalk](../data/surface-crosswalk.json)
records it as a `proposed_composite` with two component intents:

| Spoken request | Requested intent clauses | Skipper source command |
| --- | --- | --- |
| Open the browser | `browser.open` | `browser:open_fullscreen` |
| Open the browser and tile | `browser.open` → `window.tile_pair` | `browser:open_tile` |
| Tile this window and the browser | `window.tile_pair` | `windows:tile_current_browser` |
| Tile open windows | `window.tile` | `windows:tile` |

The reusable [command-sequence dataset](command-sequences.md) stores ordered
references to these atomic intents. This segmentation page explains how to
recognize them in one spoken phrase.

**“Open the browser and tile the windows”** is included as a *proposed*
combination of `browser.open` and `window.tile`. The inspected Skipper grammar
does not declare that exact combined phrase. It also has a different target
set from Skipper's **“open the browser and tile”** macro.

The same source command can implement several requested intents. Conversely,
one requested intent may have source-specific presentation defaults. Skipper's
plain **“open the browser”** selects or launches a browser and presents it in
fullscreen. Its **“open the browser and tile”** command keeps the window that
was focused before the browser opens, places it left of the browser, and hides
other windows on that workspace. Therefore `window.tile_pair` is distinct from
`window.tile` over all open windows. These are descriptions of the pinned
Skipper source, not new live execution results.

## Proposed pipeline

1. **Segment the utterance** into requested clauses. A newline, semicolon,
   `then`, or an `and` followed by another action can mark a boundary.
2. **Identify each clause** as one intent and extract its arguments. This
   parser stage is still to be developed for arbitrary phrases.
3. **Resolve context and plan execution.** For `and tile`, `it` refers to the
   browser and the pair includes the originally focused window. A Skipper
   macro may execute both requested intents as one command.

Do not split every `and`: **“tile this window and the browser”** is one
`window.tile_pair` request with two target nouns. Also, splitting is separate
from intent recognition. The current Python segmenter labels only the
curated [examples](../data/segmentation-examples.json); unfamiliar phrases
return clause text with `intent=None` for a later parser to classify.

```python
from intent_explorer import IntentExplorer

explorer = IntentExplorer.load()
result = explorer.segment_utterance("open the browser and tile")
for segment in result.segments:
    print(segment.text, segment.intent)
# open the browser browser.open
# tile window.tile_pair
print(result.source_command)  # browser:open_tile
```

Or use the CLI:

```bash
python -m intent_explorer segment "open the browser and tile" --json
printf 'open the browser\ntile open windows' | python -m intent_explorer segment --stdin
```

The [source catalog](../../private/command_catalog.py) and
[Skipper's browser layout explanation](../../private/README.md) define the
source behavior. The segmentation fixtures record which rows are
`source_declared` and which are only `proposed_combination` examples.
