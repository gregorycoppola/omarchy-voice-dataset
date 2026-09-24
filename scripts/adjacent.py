"""Curated controls from pinned adjacent voice projects.

These include dictation and speech output controls; they are not necessarily
spoken desktop commands. Each entry points to the source that declares it.
"""

ITEMS = []


def add(project, kind, source, names, intents=None, availability="declared"):
    intents = intents or {}
    for name in names:
        ITEMS.append({"project": project, "kind": kind, "name": name,
                      "source": "../other-apps/" + source, "availability": availability,
                      "candidate_intent": intents.get(name), "evidence_level": "source_declared"})


add("omause", "motor_primitive", "omause/src/types.ts",
    ["command", "terminal_command", "desktop_app", "focus_window", "window_action",
     "focus_workspace", "move_window", "open_menu", "type_text", "wait"],
    {"desktop_app": "app.launch", "focus_window": "window.focus", "window_action": "window.close",
     "focus_workspace": "workspace.switch", "move_window": "workspace.move_window",
     "open_menu": "system.menu_open", "type_text": "input.type_text", "wait": "system.wait"})
add("omause", "discovery_source", "omause/src/types.ts",
    ["desktop_app", "terminal_executable", "omarchy_command", "system", "open_window",
     "window_action", "workspace", "menu"])
add("omause", "cli_control", "omause/src/cli.ts",
    ["run", "voice", "status", "setup", "doctor", "vocab", "teach", "help"],
    {"run": "agent.request", "voice": "speech.route", "status": "system.status_query",
     "vocab": "speech.vocabulary_query", "teach": "speech.correction_save"})
add("omause", "dynamic_catalog", "omause/README.md", ["omarchy commands --json"],
    availability="depends_on_installed_omarchy")
add("omause", "system_affordance", "omause/src/sources/audio.ts",
    ["audio:volume:<percent>", "audio:mute", "audio:unmute"],
    {"audio:volume:<percent>": "audio.volume_set", "audio:mute": "audio.mute",
     "audio:unmute": "audio.unmute"})
add("omause", "system_affordance", "omause/src/sources/display.ts",
    ["display:brighter", "display:dimmer", "display:brightness:<percent>"],
    {"display:brighter": "display.brightness_up", "display:dimmer": "display.brightness_down",
     "display:brightness:<percent>": "display.brightness_set"})
add("omause", "system_affordance", "omause/src/sources/media.ts",
    ["media:play-pause", "media:next", "media:previous"],
    {"media:play-pause": "media.play_pause", "media:next": "media.next",
     "media:previous": "media.previous"})
add("omause", "system_affordance", "omause/src/sources/power.ts",
    ["power:profile:<profile>", "power:battery-status"],
    {"power:profile:<profile>": "system.power_profile_set",
     "power:battery-status": "system.battery_query"})
add("omause", "system_affordance", "omause/src/sources/network.ts",
    ["network:wifi-on", "network:wifi-off", "network:down:<connection>",
     "network:up:<connection>", "network:open:<ssid>"],
    {"network:wifi-on": "network.wifi_enable", "network:wifi-off": "network.wifi_disable",
     "network:down:<connection>": "network.disconnect",
     "network:up:<connection>": "network.connect_saved",
     "network:open:<ssid>": "network.connect_open"})
add("omause", "system_affordance", "omause/src/sources/shell.ts",
    ["panel:bluetooth", "panel:network", "panel:power", "panel:display"],
    {name: "system.panel_open" for name in
     ("panel:bluetooth", "panel:network", "panel:power", "panel:display")})
add("omause", "authored_mode", "omause/src/registry.ts",
    ["notifications_silenced", "nightlight", "idle_lock"],
    {"notifications_silenced": "system.notifications_silence_toggle",
     "nightlight": "system.nightlight_toggle", "idle_lock": "system.idle_toggle"})

add("omapilot", "desktop_tool", "omapilot/runtime/src/tools/desktop.ts",
    ["app_catalog", "app_open", "desktop_state", "window_action", "workspace_action", "omarchy_commands"],
    {"app_catalog": "app.list", "app_open": "app.launch", "desktop_state": "window.list",
     "window_action": "window.manage", "workspace_action": "workspace.manage"})
add("omapilot", "web_tool", "omapilot/runtime/src/tools/web-handoff.ts", ["web_handoff"],
    {"web_handoff": "browser.handoff"}, availability="requires_configured_browser_handoff")
add("omapilot", "capability_discovery", "omapilot/runtime/src/capabilities/tools.ts",
    ["capabilities"])
add("omapilot", "optional_capability_tool", "omapilot/runtime/src/capabilities/tools.ts",
    ["email_search", "email_thread", "email_send", "email_reply",
     "calendar_list", "calendar_events", "calendar_todo_list", "calendar_todo_create",
     "files_list", "files_search", "files_read", "files_open", "project_list",
     "project_search", "project_todos", "project_todo_create", "project_comment",
     "signal_send", "meeting_join"],
    {"email_search": "email.search", "email_thread": "email.read", "email_send": "email.send",
     "email_reply": "email.reply", "calendar_list": "calendar.list",
     "calendar_events": "calendar.events", "calendar_todo_list": "calendar.todo_list",
     "calendar_todo_create": "calendar.todo_create", "files_list": "file.list",
     "files_search": "file.search", "files_read": "file.read", "files_open": "file.open",
     "project_list": "project.list", "project_search": "project.search",
     "project_todos": "project.todo_list", "project_todo_create": "project.todo_create",
     "project_comment": "project.comment", "signal_send": "message.send",
     "meeting_join": "meeting.join"}, availability="requires_configured_connector")

add("omarchy-stt", "dictation_mode", "omarchy-stt/README.md",
    ["push_to_talk", "chat_mode", "quick_submit", "cancel"],
    {"push_to_talk": "dictation.capture", "chat_mode": "dictation.chat",
     "quick_submit": "dictation.submit", "cancel": "dictation.cancel"})
add("omarchy-stt", "configurable_tool", "omarchy-stt/src/tools.rs", ["user_tools_json"],
    availability="requires_user_tool_definitions")

add("handy", "dictation_control", "handy-plugin/bin/handy-trigger",
    ["toggle", "stop", "press", "release"],
    {"toggle": "dictation.toggle", "stop": "dictation.stop",
     "press": "dictation.toggle", "release": "dictation.stop"})

add("voxtype", "dictation_control", "voxtype/src/cli/record.rs",
    ["start", "stop", "toggle", "cancel"],
    {"start": "dictation.start", "stop": "dictation.stop", "toggle": "dictation.toggle",
     "cancel": "dictation.cancel"})
add("voxtype", "cli_control", "voxtype/src/cli/commands.rs",
    ["daemon", "transcribe", "setup", "config", "info", "configure", "status", "record",
     "meeting", "check_update"],
    {"transcribe": "speech.transcribe_file", "status": "dictation.status"})
add("voxtype", "meeting_control", "voxtype/src/cli/meeting.rs",
    ["start", "stop", "pause", "resume", "status", "list", "export", "show", "delete", "label", "summarize"],
    {name: "meeting." + name for name in
     ("start", "stop", "pause", "resume", "status", "list", "export", "show", "delete", "label", "summarize")})

add("voice-input", "dictation_control", "voice-input/src/args.rs",
    ["start", "stop", "toggle", "cancel", "restart"],
    {name: "dictation." + name for name in ("start", "stop", "toggle", "cancel", "restart")})
add("voice-input", "cli_control", "voice-input/src/args.rs",
    ["history_show", "history_list", "history_paste", "status", "diagnostics",
     "asr_test", "asr_stream_test", "llm_test"],
    {"history_show": "dictation.history", "history_list": "dictation.history",
     "history_paste": "dictation.history_paste", "status": "dictation.status",
     "asr_test": "speech.transcribe_file", "asr_stream_test": "speech.transcribe_file"})
add("voice-input", "top_level_cli", "voice-input/src/args.rs",
    ["daemon", "record", "hud", "history", "status", "diagnostics", "config",
     "settings", "settings_backend", "setup", "asr", "llm", "help", "version"])

add("voxtype-enhance", "bar_control", "voxtype-enhance/bar/widget.qml",
    ["open_settings", "close_settings", "show_recording_state"],
    {"show_recording_state": "dictation.status"})
add("voxtype-enhance", "configuration", "voxtype-enhance/scripts/voxtype-config.py",
    ["model_download", "engine_select", "language_select", "output_mode", "paste_keys"],
    {"model_download": "speech.model_install", "language_select": "speech.language_set",
     "engine_select": "speech.engine_set", "output_mode": "dictation.output_set",
     "paste_keys": "dictation.paste_keys_set"})

add("omayap", "speech_output_control", "omayap/Service.qml",
    ["toggleSelection", "readOcr", "stop", "setSpeed", "setBackend",
     "installVoice", "selectVoice"],
    {"toggleSelection": "speech.read_selection", "readOcr": "speech.read_screen",
     "stop": "speech.stop", "setSpeed": "speech.speed_set",
     "setBackend": "speech.backend_set", "installVoice": "speech.voice_install",
     "selectVoice": "speech.voice_select"})
add("omayap", "announcement_event", "omayap/bin/yap",
    ["custom_stdin", "task-complete", "input-needed", "permission-needed", "error"],
    {name: "speech.say" for name in
     ("custom_stdin", "task-complete", "input-needed", "permission-needed", "error")})
