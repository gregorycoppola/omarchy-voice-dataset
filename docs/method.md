# Inventory and intent method

Version 2 now defines structured schemas for all 227 intents. See
[the current model and workflow](structured-intents.md). Historical counts and
example lists below describe the original audit; use `data/catalog.json` and
the browser explorer for current definitions.

Snapshot date: 2026-09-24. The source files are local pinned checkouts; exact
commit IDs and Skipper file hashes are in `data/snapshot.json`.

## What counts as a command

- **Skipper:** authored grammar rule and resolved execution ID from
  `command_catalog.py`. Its recognized phrases are deterministic expansions,
  but a requested action still needs its target to exist and pass runtime checks.
- **Genesis:** top-level actions in `bin/execute`, plus configured commands,
  routines, and agent fallback. `bin/intent` maps phrases to these actions.
  Home Assistant and TV actions delegate to other plugins. The executor itself
  expects the caller to enforce confirmation.
- **Omarvis:** 31 fixed agent-browser routes and 53 Herdr policy routes from
  its source. The Herdr catalog also checks installed help output. Omarchy
  routes are discovered from `omarchy commands --json` at runtime; this
  machine's 387 public routes are a separate environment capture, not a
  promise that Omarvis understands a specific spoken phrase or will allow it.
- **OMA:** 24 core tool schemas, six conditional task tools, and one conditional
  camera tool. The `run_shell` core tool is off unless enabled. These are
  general executor tools behind a planner, not a finite phrase catalog.
- **Omause:** typed motor primitives and discovered affordances from Omarchy,
  apps, windows, workspaces, menus, and system sources. The dynamic set varies
  with the installed machine and configured TypeSafe Jev access.
- **OmaPilot:** six desktop tools, a web handoff tool, and twenty capability
  tools, most tied to configured accounts or services. Tool availability does
  not establish a spoken phrase or external account success.
- **omarchy-stt:** dictation modes and a configurable `tools.json` loader.
  No fixed desktop command list is implied by the tool-calling code.
- **Voxtype, Voice Input, Handy, Voxtype Enhance, OmaYap:** dictation or speech
  output controls, CLI operations, and configuration. These controls are
  inventoried to avoid treating their text output as desktop command intents.

`source-surfaces.json` preserves these distinct surface kinds and conditions.
The `surface-crosswalk.json` maps a declared surface to a proposed user
outcome. A Skipper browser-opening and tiling macro has `component_intents`
because its source command covers two requested outcomes. Some tools such as
`omarchy_cli`, `hypr_dispatch`, and `run_shell` are
marked `open_ended_enabler` because one tool can express many outcomes. A
candidate mapping is **not** evidence that a voice phrase succeeded.

The original 55 rows in `intents.json` have typed slots and illustrative
utterances. Its `explicit`, `tool`, `extension`, and `unknown` support labels
describe source evidence only. The 168 newer candidate outcome IDs in the
crosswalk still need human-reviewed argument schemas. Generated
`coding.*` candidates name Herdr operations precisely; they have not yet been
normalized into product-independent goals.

## What a working claim needs

For each project and concrete phrase, record:

```json
{
  "project": "genesis",
  "source_commit": "<full commit>",
  "observed_at": "<timestamp with timezone>",
  "environment": {"omarchy_version": "<version>", "dependencies": []},
  "utterance": "<exact text or private recording ID>",
  "context": {"focused_window": "<fixture>", "available_targets": []},
  "expected": {"intent": "<canonical ID>", "arguments": {}, "result": "<state>"},
  "observed": {"transcript": "<text>", "parsed_action": {}, "result": "<state>"},
  "evidence": "<test log or artifact ID>",
  "status": "pass"
}
```

Keep speech recognition, interpretation, authorization, dispatch, and observed
result separate. Use synthetic or consented data, and publish no private
recordings. Do not run shutdown, lock, arbitrary shell, home automation, or
remote-control commands merely to fill a matrix. Unit tests and mocked
executors can establish their logic; an end-to-end result requires a safe,
controlled environment and observable outcome.

An accurate historical statement is: “At commit X on date Y, test Z passed in
environment E.” “All functionality worked” requires coverage of every claimed
feature and its dependencies; this snapshot does not provide that evidence.
