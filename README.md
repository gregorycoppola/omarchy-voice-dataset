# Omarchy voice intent dataset

The active **version 2 catalog** defines all 227 intents as names plus structured
arguments, with 2,270 labeled examples and grammar templates. Skipper reads its
grammar and vocabulary directly from this repository. Start with
[the structured intent model and editing workflow](docs/structured-intents.md).

Author `data/catalog.json` and `data/providers/skipper.json`. Run
`python scripts/export_catalog.py`, `python scripts/check.py`, and
`python -m unittest discover -s tests`. Refresh the browser explorer and restart
Skipper to use an edited catalog.

The inventory below describes the preserved 2026-09-24 source audit.

Local research repository, snapshot **2026-09-24**. It records the command
surfaces of twelve voice-related projects at identified source versions,
then maps them to candidate outcome intents. It is separate from the Skipper
application. Public snapshots are published at
[omarchy-voice-dataset](https://github.com/gregorycoppola/omarchy-voice-dataset).

## What is here

| File | Meaning |
| --- | --- |
| [data/projects.json](data/projects.json) | Twelve known voice-related projects, pinned source commits, and their audit state. |
| [data/snapshot.json](data/snapshot.json) | Exact commits for eleven clean external clones, plus a content digest and file hashes for private Skipper source. No private commit ID is copied. |
| [data/source-surfaces.json](data/source-surfaces.json) | Declared rules, action handlers, routes, tools, dictation controls, and speech output controls from the twelve source trees. |
| [data/intents.json](data/intents.json) | Generated view of all 227 structured intent definitions. |
| [data/surface-crosswalk.json](data/surface-crosswalk.json) | A proposed mapping of each source surface to one outcome, component intents for a composite command, or an open-ended enabler. |
| [data/outcomes.json](data/outcomes.json) | One candidate outcome list spanning all twelve projects, with schema status and mapped projects. |
| [docs/intent-coverage.md](docs/intent-coverage.md) | Markdown coverage matrix for 55 reviewed intents and grouped list of 168 additional candidates. |
| [data/utterances.json](data/utterances.json) | 2,270 illustrative utterances, ten per candidate intent; origin and argument labels are explicit. |
| [data/segmentation-examples.json](data/segmentation-examples.json) | Skipper browser commands and proposed multi-intent utterances with clause labels. |
| [data/command-sequences.json](data/command-sequences.json) | Ordered references to individual intent examples, with connectors and source macro evidence. |
| [docs/utterance-variants.md](docs/utterance-variants.md) | Readable list of ten ways to say each intent. |
| [docs/intent-explorer.md](docs/intent-explorer.md) | Python API and CLI for iterating through intents and utterances. |
| [docs/segmentation.md](docs/segmentation.md) | Why Skipper compound commands need a separate segmentation and context stage. |
| [docs/command-sequences.md](docs/command-sequences.md) | Data model and Python API for composing individual commands into sequences. |
| [explorer.html](explorer.html) | Browser view of all 227 intents, their ten phrases, and command sequences. |
| [docs/parsing-strategies.md](docs/parsing-strategies.md) | Proposed parser approaches and a fair comparison method. |
| [data/local-omarchy-routes.json](data/local-omarchy-routes.json) | The 387 public Omarchy CLI routes exposed by this machine on the snapshot day. These are dynamic environment data for Omarvis/OMA, not voice test results. |
| [surfaces.html](surfaces.html) | Searchable view of every inventoried static source surface and its proposed outcome. |
| [outcomes.html](outcomes.html) | Searchable view of the unified candidate outcome list. |
| [docs/verification.md](docs/verification.md) | Tests actually run, failures, and limits of what “working” means here. |
| [index.html](index.html) | Searchable view of the 55 reviewed intents. Serve the parent workspace so source links work. |

The preserved source-audit crosswalk has **393 source surfaces** and **223 candidate outcomes**,
including **168 that originally lacked typed schemas**; all now have authored shared schemas. A source surface is a declared rule,
executor branch, allowed route, or tool; it is not necessarily a unique user
feature. Skipper grammar rules and execution IDs intentionally overlap. Its
browser opening and tiling macro has two component intents. Omarvis
Herdr routes depend on Herdr being installed, OMA and OmaPilot have conditional
tools, and several projects discover commands from the installed Omarchy CLI.
Therefore these counts
must not be presented as a count of working voice commands.

## Evidence levels

1. **Declared in source:** the command or tool appears in the pinned checkout.
2. **Unit tested:** a named upstream or Skipper test ran on this machine and
   passed. This checks only the cases in that test.
3. **Integrated on this machine:** the full spoken command, dependency, action,
   and observed result were exercised. No external app has this label yet.

The snapshot currently establishes level 1 for the inventoried surfaces and
limited level 2 for several projects. It does **not** establish that all features
of any external project worked end to end on 2026-09-24. See
[verification](docs/verification.md). The source checkouts were first reviewed
on 2026-09-20 for Genesis, Omarvis, and OMA; their exact commits are frozen here.
The remaining eight were checked out for this snapshot. Skipper has local edits;
its source digest and file hashes identify the inspected content without
recording private Git history.

## Rebuild and audit

For the browser view:

```bash
cd ~/Projects/omarchy-voice-manager
python -m http.server 8765 --bind 127.0.0.1
# Open http://127.0.0.1:8765/omarchy-voice-dataset/explorer.html
```

The snapshot scripts expect this layout under `omarchy-voice-manager/`:
`private/`, the eleven `other-apps/` clones, and this repository.
They read source and metadata; they do not run desktop actions.

```bash
cd ~/Projects/omarchy-voice-manager/omarchy-voice-dataset
python scripts/export_catalog.py
python scripts/check.py
python -m unittest discover -s tests
```

Explore the labels and phrases without running a desktop action:

```bash
python -m intent_explorer stats
python -m intent_explorer show app.launch
python -m intent_explorer walk --prefix browser.
python -m intent_explorer segment "open the browser and tile" --json
python -m intent_explorer compose browser.open:1 window.tile:1 --join and
```

Regenerating on changed checkouts creates a **new** snapshot; keep a dated copy
or commit first. Do not rewrite the 2026-09-24 claims after the source changes.
The crosswalk is a research proposal. A future evaluated dataset needs exact
phrases that each product actually accepted, context fixtures, expected target
state, and observed results. [Method](docs/method.md) defines those fields.

This repo contains no recordings, credentials, model files, copied upstream
implementation, or personal command history. Public snapshots have independent
history; private development history is never merged into them. The authored
catalog and code are GPL-3.0-only; linked projects retain their own licenses.

## Shared language policy

`data/providers/skipper.json` owns `language_policy`: browser spelling forms,
specific-rule priority, and spoken window-name forms. Runtime target identities
and personal aliases/corrections/history stay on each user’s machine.
