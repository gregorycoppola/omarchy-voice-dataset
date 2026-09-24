# Intent coverage — 2026-09-24 source snapshot

Version 2 now defines structured schemas for all 223 intents. See
[the current model and workflow](structured-intents.md). Historical counts and
example lists below describe the original audit; use `data/catalog.json` and
the browser explorer for current definitions.

This report answers which user outcomes the inspected source *appears* to support.
It does not claim that a spoken phrase or desktop action succeeded. See the
[verification record](verification.md) for the tests actually run and their limits.
Source versions and the full twelve-project inventory are in
[the snapshot](../data/snapshot.json) and [projects](projects.md).

## How to read coverage

- **Explicit:** a named command or route for this outcome is declared in source.
- **Tool:** a general tool can potentially perform it; phrase recognition and
  execution have not been demonstrated.
- **Extension:** an integration or configured extension may provide it.
- **Unknown:** this inventory found no specific evidence; it does not prove
  the project cannot do it.

The 55 typed intents below were reviewed across Skipper, Genesis, Omarvis,
and OMA. The other eight projects are included in the 223-outcome source
crosswalk, but they have not received the same four-status review.
A project's appearance in the candidate list means only that a declared
source surface was *provisionally mapped* to that outcome.

## Reviewed intent summary

| Project | Explicit | Tool | Extension | Unknown |
| --- | ---: | ---: | ---: | ---: |
| skipper | 23 | 1 | 0 | 31 |
| genesis | 23 | 0 | 3 | 29 |
| omarvis | 17 | 29 | 0 | 9 |
| oma | 18 | 35 | 0 | 2 |

## All 55 typed intents

Each status is source evidence for that project. Intent names and slot types
come from [the typed dataset](../data/intents.json); that file also gives
illustrative phrases and a source path for each supported entry.

| Intent | Slots | Skipper | Genesis | Omarvis | OMA |
| --- | --- | --- | --- | --- | --- |
| `app.launch` | `application`: string | explicit | explicit | tool | explicit |
| `app.focus` | `application`: string | explicit | unknown | tool | tool |
| `app.close` | `application`: string, `selection`: enum | explicit | unknown | tool | tool |
| `window.focus` | `target`: window | explicit | unknown | explicit | tool |
| `window.close` | `target`: window | explicit | unknown | explicit | tool |
| `window.move_monitor` | `target`: window, `monitor`: monitor | explicit | unknown | tool | tool |
| `window.maximize` | `target`: window | explicit | unknown | explicit | tool |
| `window.tile` | `scope`: enum | explicit | unknown | tool | explicit |
| `window.list` | `scope`: enum | explicit | unknown | tool | explicit |
| `window.fullscreen` | `target`: window, `state`: enum | tool | unknown | explicit | tool |
| `window.float` | `target`: window, `state`: enum | unknown | unknown | explicit | tool |
| `window.hide` | `target`: window | explicit | unknown | tool | tool |
| `workspace.switch` | `workspace`: integer | unknown | explicit | explicit | tool |
| `workspace.move_window` | `target`: window, `workspace`: integer | unknown | unknown | explicit | tool |
| `audio.volume_up` | `amount`: optional_number | explicit | explicit | tool | tool |
| `audio.volume_down` | `amount`: optional_number | explicit | explicit | tool | tool |
| `audio.mute` | `state`: true | explicit | explicit | tool | tool |
| `audio.unmute` | `state`: false | explicit | explicit | tool | tool |
| `display.brightness_up` | `amount`: optional_number | explicit | explicit | tool | tool |
| `display.brightness_down` | `amount`: optional_number | explicit | explicit | tool | tool |
| `media.play` | `state`: play | explicit | explicit | tool | tool |
| `media.pause` | `state`: pause | explicit | explicit | tool | tool |
| `media.next` | `direction`: next | explicit | explicit | tool | tool |
| `media.previous` | `direction`: previous | explicit | explicit | tool | tool |
| `system.lock` | — | unknown | explicit | tool | tool |
| `system.suspend` | — | unknown | explicit | tool | tool |
| `system.shutdown` | — | unknown | explicit | tool | tool |
| `system.reboot` | — | unknown | explicit | tool | tool |
| `system.screenshot` | `target`: enum | unknown | explicit | tool | tool |
| `system.theme_set` | `theme`: string | unknown | explicit | tool | tool |
| `system.power_profile_set` | `profile`: enum | unknown | explicit | tool | tool |
| `system.battery_query` | — | unknown | explicit | tool | explicit |
| `system.time_query` | — | unknown | explicit | tool | explicit |
| `browser.navigate` | `url_or_destination`: string | explicit | unknown | explicit | explicit |
| `browser.tab_new` | `url`: optional_string | explicit | unknown | explicit | tool |
| `browser.tab_close` | `target`: tab | explicit | unknown | explicit | tool |
| `browser.tab_switch` | `target`: tab | unknown | unknown | explicit | tool |
| `browser.page_back` | — | unknown | unknown | explicit | tool |
| `browser.page_scroll` | `direction`: enum, `amount`: optional_number | unknown | unknown | explicit | explicit |
| `browser.element_click` | `target`: element | unknown | unknown | explicit | explicit |
| `browser.form_fill` | `target`: element, `text`: string | unknown | unknown | explicit | tool |
| `browser.page_read` | `target`: optional_string | unknown | unknown | explicit | explicit |
| `reminder.create` | `message`: string, `delay`: optional_duration | unknown | explicit | tool | tool |
| `speech.say` | `text`: string | unknown | explicit | tool | tool |
| `smarthome.device_set` | `device`: string, `state`: enum | unknown | extension | unknown | unknown |
| `tv.power_set` | `state`: enum | unknown | extension | unknown | unknown |
| `terminal.read` | `target`: terminal | unknown | unknown | unknown | explicit |
| `terminal.run` | `target`: terminal, `command`: string | unknown | unknown | unknown | explicit |
| `terminal.watch` | `target`: terminal | unknown | unknown | unknown | explicit |
| `task.submit` | `goal`: string | unknown | extension | tool | explicit |
| `task.status` | `task_id`: string | unknown | unknown | explicit | explicit |
| `clipboard.read` | — | unknown | unknown | unknown | explicit |
| `clipboard.write` | `text`: string | unknown | unknown | unknown | explicit |
| `notes.remember` | `text`: string | unknown | unknown | unknown | explicit |
| `screen.read` | `target`: window | unknown | unknown | unknown | explicit |

## Additional candidate outcomes needing schemas

These 168 IDs come from the [source crosswalk](../data/surface-crosswalk.json).
They still need human review of meaning, arguments, and examples. Project
names in the table are proposed source mappings, not verified voice coverage.
An em dash means no project has been mapped to that candidate yet.

### agent (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `agent.request` | genesis, omause |

### app (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `app.list` | omapilot |

### audio (2)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `audio.mute_toggle` | genesis |
| `audio.volume_set` | omause |

### browser (15)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `browser.close` | omarvis |
| `browser.download` | omarvis |
| `browser.drag` | omarvis |
| `browser.element_focus` | omarvis |
| `browser.element_hover` | omarvis |
| `browser.form_check` | omarvis |
| `browser.form_select` | omarvis |
| `browser.handoff` | omapilot |
| `browser.open` | skipper |
| `browser.page_forward` | omarvis |
| `browser.page_reload` | omarvis |
| `browser.tab_list` | omarvis |
| `browser.tabs_clear` | skipper |
| `browser.upload` | omarvis |
| `browser.wait` | omarvis |

### calendar (4)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `calendar.events` | omapilot |
| `calendar.list` | omapilot |
| `calendar.todo_create` | omapilot |
| `calendar.todo_list` | omapilot |

### camera (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `camera.inspect` | oma |

### clipboard (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `clipboard.manage` | oma |

### coding (53)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `coding.agent.explain` | omarvis |
| `coding.agent.focus` | omarvis |
| `coding.agent.get` | omarvis |
| `coding.agent.list` | omarvis |
| `coding.agent.prompt` | omarvis |
| `coding.agent.read` | omarvis |
| `coding.agent.rename` | omarvis |
| `coding.agent.send_keys` | omarvis |
| `coding.agent.start` | omarvis |
| `coding.api.snapshot` | omarvis |
| `coding.notification.show` | omarvis |
| `coding.pane.close` | omarvis |
| `coding.pane.current` | omarvis |
| `coding.pane.edges` | omarvis |
| `coding.pane.focus` | omarvis |
| `coding.pane.get` | omarvis |
| `coding.pane.input` | omarvis |
| `coding.pane.layout` | omarvis |
| `coding.pane.list` | omarvis |
| `coding.pane.move` | omarvis |
| `coding.pane.neighbor` | omarvis |
| `coding.pane.process_info` | omarvis |
| `coding.pane.read` | omarvis |
| `coding.pane.rename` | omarvis |
| `coding.pane.resize` | omarvis |
| `coding.pane.run` | omarvis |
| `coding.pane.send_keys` | omarvis |
| `coding.pane.send_text` | omarvis |
| `coding.pane.split` | omarvis |
| `coding.pane.swap` | omarvis |
| `coding.pane.zoom` | omarvis |
| `coding.server.reload_config` | omarvis |
| `coding.server.stop` | omarvis |
| `coding.session.delete` | omarvis |
| `coding.session.list` | omarvis |
| `coding.session.stop` | omarvis |
| `coding.status` | omarvis |
| `coding.tab.close` | omarvis |
| `coding.tab.create` | omarvis |
| `coding.tab.focus` | omarvis |
| `coding.tab.get` | omarvis |
| `coding.tab.list` | omarvis |
| `coding.tab.rename` | omarvis |
| `coding.workspace.close` | omarvis |
| `coding.workspace.create` | omarvis |
| `coding.workspace.focus` | omarvis |
| `coding.workspace.get` | omarvis |
| `coding.workspace.list` | omarvis |
| `coding.workspace.rename` | omarvis |
| `coding.worktree.create` | omarvis |
| `coding.worktree.list` | omarvis |
| `coding.worktree.open` | omarvis |
| `coding.worktree.remove` | omarvis |

### dictation (13)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `dictation.cancel` | omarchy-stt, voice-input, voxtype |
| `dictation.capture` | omarchy-stt |
| `dictation.chat` | omarchy-stt |
| `dictation.history` | voice-input |
| `dictation.history_paste` | voice-input |
| `dictation.output_set` | voxtype-enhance |
| `dictation.paste_keys_set` | voxtype-enhance |
| `dictation.restart` | voice-input |
| `dictation.start` | voice-input, voxtype |
| `dictation.status` | voice-input, voxtype, voxtype-enhance |
| `dictation.stop` | handy, voice-input, voxtype |
| `dictation.submit` | omarchy-stt |
| `dictation.toggle` | handy, voice-input, voxtype |

### display (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `display.brightness_set` | omause |

### email (4)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `email.read` | omapilot |
| `email.reply` | omapilot |
| `email.search` | omapilot |
| `email.send` | omapilot |

### extension (3)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `extension.failure_report` | genesis |
| `extension.ipc_call` | genesis |
| `extension.script_run` | genesis |

### file (4)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `file.list` | omapilot |
| `file.open` | omapilot |
| `file.read` | omapilot |
| `file.search` | omapilot |

### input (2)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `input.keypress` | oma, omarvis |
| `input.type_text` | oma, omause |

### media (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `media.play_pause` | omause |

### meeting (12)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `meeting.delete` | voxtype |
| `meeting.export` | voxtype |
| `meeting.join` | omapilot |
| `meeting.label` | voxtype |
| `meeting.list` | voxtype |
| `meeting.pause` | voxtype |
| `meeting.resume` | voxtype |
| `meeting.show` | voxtype |
| `meeting.start` | voxtype |
| `meeting.status` | voxtype |
| `meeting.stop` | voxtype |
| `meeting.summarize` | voxtype |

### message (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `message.send` | omapilot |

### network (5)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `network.connect_open` | omause |
| `network.connect_saved` | omause |
| `network.disconnect` | omause |
| `network.wifi_disable` | omause |
| `network.wifi_enable` | omause |

### project (5)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `project.comment` | omapilot |
| `project.list` | omapilot |
| `project.search` | omapilot |
| `project.todo_create` | omapilot |
| `project.todo_list` | omapilot |

### routine (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `routine.schedule` | genesis |

### screen (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `screen.click_text` | oma |

### smarthome (2)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `smarthome.device_toggle` | genesis |
| `smarthome.scene_activate` | genesis |

### speech (14)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `speech.backend_set` | omayap |
| `speech.correction_save` | omause |
| `speech.engine_set` | voxtype-enhance |
| `speech.language_set` | voxtype-enhance |
| `speech.model_install` | voxtype-enhance |
| `speech.read_screen` | omayap |
| `speech.read_selection` | omayap |
| `speech.route` | omause |
| `speech.speed_set` | omayap |
| `speech.stop` | omayap |
| `speech.transcribe_file` | voice-input, voxtype |
| `speech.vocabulary_query` | omause |
| `speech.voice_install` | omayap |
| `speech.voice_select` | omayap |

### system (9)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `system.idle_set` | genesis |
| `system.idle_toggle` | omause |
| `system.logout` | genesis |
| `system.menu_open` | omause |
| `system.nightlight_toggle` | genesis, omause |
| `system.notifications_silence_toggle` | omause |
| `system.panel_open` | omause |
| `system.status_query` | genesis, oma, omause |
| `system.wait` | oma, omause |

### task (4)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `task.cancel` | oma |
| `task.list` | oma |
| `task.read` | oma |
| `task.resume` | oma |

### terminal (2)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `terminal.list` | oma |
| `terminal.open` | skipper |

### tv (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `tv.remote_action` | genesis |

### web (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `web.search` | oma |

### window (3)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `window.compose` | oma |
| `window.manage` | omapilot |
| `window.tile_pair` | skipper |

### workspace (1)

| Candidate intent | Proposed source mapping |
| --- | --- |
| `workspace.manage` | omapilot |

## Next evidence needed

To claim a feature worked on this date, record an exact phrase, environment,
expected result, observed result, and test artifact for the pinned source.
The [method](method.md) specifies those fields. The searchable
[intent matrix](../index.html) and [outcome browser](../outcomes.html)
show the same inventory with filters.
