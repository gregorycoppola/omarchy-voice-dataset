# Projects identified by 2026-09-24

The existing Skipper research listed twelve Omarchy-related voice projects.
This repository pins source checkouts for all twelve and inventories their
primary controls. Some are dictation or speech output systems and must not be
treated as command parsers merely because they handle voice.

| Project | Role in this dataset | Source status |
| --- | --- | --- |
| [Skipper](../data/projects.json) | Local grammar and checked desktop actions | Current private checkout inventoried; uncommitted file hashes frozen. |
| [Genesis](https://github.com/ronald2wing/Omarchy-Genesis) | Local phrase rules, custom commands and routines | Clean pinned clone inventoried. |
| [Omarvis](https://github.com/eliasstravik/omarvis) | Conversational router with Omarchy, Herdr, and browser catalogs | Clean pinned clone inventoried. |
| [OMA / omarchy-voice](https://github.com/wombatoperator/omarchy-voice) | Conversational planner with desktop tools and optional durable tasks | Clean pinned clone inventoried. |
| [Voxtype](https://voxtype.io/) | Dictation backend; Genesis can call it | Pinned source; recording, transcription and meeting controls inventoried. |
| [Voice Input](https://github.com/Saco93/voice-input) | Dictation | Pinned source; recording and support CLI controls inventoried. |
| [omarchy-stt](https://github.com/sebkouba/omarchy-stt) | Dictation with optional user-defined tools | Pinned source; dictation modes and tool loader inventoried. |
| [OmaPilot](https://github.com/spencerbull/omarchy-omapilot) | Voice conversation and conditional tools | Pinned source; desktop and configured capability tools inventoried. |
| [omause](https://github.com/devfros/omause) | Voice command router | Pinned source; motor primitives, discovery sources and CLI controls inventoried. |
| [Omarchy Handy Plugin](https://github.com/Blizl/Omarchy-Handy-Plugin) | Dictation integration | Pinned source; toggle controls inventoried. README marks the plugin deprecated. |
| [omarchy-voxtype-enhance](https://github.com/Johnmeri0008/omarchy-voxtype-enhance) | Dictation settings UI | Pinned source; bar controls and Voxtype configuration bridge inventoried. |
| [OmaYap](https://github.com/Ray-4Ws/OmaYap) | Selected-text and screen-text speech output | Pinned source; service controls inventoried. |

These are targeted source reviews, not complete demonstrations of every
configuration and feature. `data/projects.json` gives each inspected commit.

The eleven clean external checkouts are under `../other-apps/`. Genesis,
Omarvis and OMA were first reviewed on 2026-09-20; the remaining eight were
added on 2026-09-24. Their pinned commits are in `data/snapshot.json`.
They were not installed as Omarchy plugins for this snapshot.
