#!/usr/bin/env python3
"""Capture declared command surfaces from the pinned local reference checkouts.

This script reads source and imports only the parser/catalog modules named below.
It never calls an action executor or starts a voice service.
"""

import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / "data"


def source(relative):
    path = ROOT / relative
    return path.read_text(), path


def record(project, kind, name, relative, *, detail=None, availability="declared"):
    item = {"project": project, "kind": kind, "name": name,
            "source": "../" + relative, "availability": availability,
            "evidence_level": "source_declared"}
    if detail is not None:
        item["detail"] = detail
    return item


def git(path, *args):
    return subprocess.check_output(["git", "-C", str(path), *args], text=True).strip()


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def skipper_digest():
    tree = ROOT / "private"
    tracked = subprocess.check_output(["git", "-C", str(tree), "ls-files", "-z"]).split(b"\0")
    paths = {name.decode() for name in tracked if name}
    paths.update(dirty_paths)
    digest = hashlib.sha256()
    for name in sorted(paths):
        path = tree / name
        if path.is_file() and path.suffix in {".py", ".js", ".sh", ".qml", ".json", ".lua"}:
            digest.update(name.encode() + b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()


def python_named_dicts(relative):
    tree = ast.parse(source(relative)[0])
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key, value in zip(node.keys, node.values):
            if isinstance(key, ast.Constant) and key.value == "name" and isinstance(value, ast.Constant) and isinstance(value.value, str):
                yield value.value, node.lineno
                break


rows = []

# Skipper's authored grammar is expanded by its own pure parser module.
sys.path.insert(0, str(ROOT / "private"))
from command_catalog import RULES, STRUCTURED_INTENTS  # noqa: E402
from adjacent import ITEMS  # noqa: E402

for rule in RULES:
    rows.append(record("skipper", "grammar_rule", rule.id, "private/command_catalog.py",
                       detail={"intent_type": rule.intent_type, "patterns": list(rule.patterns),
                               "arguments": dict(rule.arguments), "command_template": rule.command}))
for name, intent in sorted(STRUCTURED_INTENTS.items()):
    rows.append(record("skipper", "execution_id", name, "private/command_catalog.py",
                       detail=intent.to_dict()))

# Genesis declares action handlers in a top-level shell case statement. The
# parser also has configured commands, routines and AI fallback, listed below.
relative = "other-apps/genesis/bin/execute"
body, _ = source(relative)
case = body.split('case "$action" in', 1)[1]
for match in re.finditer(r"^([a-z][a-z0-9-]*)\)\s*", case, re.MULTILINE):
    rows.append(record("genesis", "executor_action", match.group(1), relative,
                       detail={"line": body[:body.index('case "$action" in')].count("\n") + case[:match.start()].count("\n") + 2}))
for name, src in (("custom_plugin_command", "other-apps/genesis/bin/commands"),
                  ("custom_script_command", "other-apps/genesis/bin/commands"),
                  ("scheduled_routine", "other-apps/genesis/bin/routines"),
                  ("agent_fallback", "other-apps/genesis/bin/intent")):
    rows.append(record("genesis", "configurable_surface", name, src, availability="configured"))

# Omarvis has a fixed browser catalog, an allowlisted Herdr route set, and a
# catalog drawn from the installed Omarchy CLI at runtime.
sys.path.insert(0, str(ROOT / "other-apps/omarvis"))
from omarvis.catalog import browser_catalog  # noqa: E402
from omarvis.policy import HERDR_ALLOW  # noqa: E402

for route in sorted(browser_catalog().routes):
    rows.append(record("omarvis", "browser_route", " ".join(route),
                       "other-apps/omarvis/omarvis/catalog.py"))
for route in sorted(HERDR_ALLOW):
    rows.append(record("omarvis", "herdr_allowed_route", "herdr " + " ".join(route),
                       "other-apps/omarvis/omarvis/policy.py", availability="requires_herdr"))
rows.append(record("omarvis", "dynamic_catalog", "omarchy commands --json",
                   "other-apps/omarvis/omarvis/catalog.py", availability="depends_on_installed_omarchy"))

# OMA exposes general tools rather than a finite list of spoken commands.
for relative, availability in (
    ("other-apps/omarchy-voice/src/omarchy_voice/tools.py", "declared"),
    ("other-apps/omarchy-voice/src/omarchy_voice/tasks.py", "tasks_enabled"),
    ("other-apps/omarchy-voice/src/omarchy_voice/vision.py", "vision_enabled"),
):
    for name, line in python_named_dicts(relative):
        if name == "name":
            continue
        if relative.endswith("tools.py") and name == "run_shell":
            status = "allow_shell_enabled"
        else:
            status = availability
        rows.append(record("oma", "tool", name, relative,
                           detail={"line": line}, availability=status))
relative = "other-apps/omarchy-voice/src/omarchy_voice/tasks.py"
for node in ast.walk(ast.parse(source(relative)[0])):
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == "schema" and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and node.args[0].value.startswith("task_")):
        rows.append(record("oma", "tool", node.args[0].value, relative,
                           detail={"line": node.lineno}, availability="tasks_enabled"))

rows.extend(ITEMS)

# Freeze exact local source identity. The private Skipper checkout has work in
# progress, so record hashes of the imported files instead of implying HEAD
# contains them. External references are clean shallow clones.
snapshot = {"review_date": "2026-09-24", "claim": "source snapshot; no live end-to-end validation",
            "sources": []}
for project, directory in (("skipper", "private"), ("genesis", "other-apps/genesis"),
                           ("omarvis", "other-apps/omarvis"), ("oma", "other-apps/omarchy-voice"),
                           ("omause", "other-apps/omause"), ("omapilot", "other-apps/omapilot"),
                           ("omarchy-stt", "other-apps/omarchy-stt"),
                           ("handy", "other-apps/handy-plugin"),
                           ("voxtype", "other-apps/voxtype"),
                           ("voice-input", "other-apps/voice-input"),
                           ("voxtype-enhance", "other-apps/voxtype-enhance"),
                           ("omayap", "other-apps/omayap")):
    path = ROOT / directory
    snapshot["sources"].append({"project": project, "workspace_path": "../" + directory,
                                "git_commit": None if project == "skipper" else git(path, "rev-parse", "HEAD"),
                                "upstream_git": None if project == "skipper" else git(path, "remote", "get-url", "origin"),
                                "private_history_withheld": project == "skipper",
                                "clean": not bool(git(path, "status", "--porcelain"))})
snapshot["skipper_file_hashes"] = {
    name: sha256(ROOT / "private" / name)
    for name in ("command_catalog.py", "desktop_commands.py", "grammar_engine.py")
}
dirty_status = subprocess.check_output(
    ["git", "-C", str(ROOT / "private"), "status", "--porcelain", "-uall"], text=True)
dirty_paths = [line[3:] for line in dirty_status.splitlines()]
snapshot["skipper_dirty_file_hashes"] = {
    name: sha256(ROOT / "private" / name)
    for name in dirty_paths if (ROOT / "private" / name).is_file()
}
snapshot["skipper_source_digest"] = skipper_digest()
snapshot["counts"] = {entry["project"]: len([row for row in rows if row["project"] == entry["project"]])
                      for entry in snapshot["sources"]}

OUT.mkdir(exist_ok=True)
(OUT / "source-surfaces.json").write_text(json.dumps({"schema_version": 1, "surfaces": rows}, indent=2) + "\n")
(OUT / "snapshot.json").write_text(json.dumps(snapshot, indent=2) + "\n")
print(json.dumps(snapshot["counts"], indent=2))
