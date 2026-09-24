#!/usr/bin/env python3
"""Check dataset references, coverage, and frozen source identity."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys

from coverage_markdown import render as render_coverage

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT))
from intent_explorer import IntentExplorer


def read(name):
    return json.loads((DATA / name).read_text())


projects = read("projects.json")
snapshot = read("snapshot.json")
surfaces = read("source-surfaces.json")["surfaces"]
crosswalk = read("surface-crosswalk.json")["crosswalk"]
intents = read("history/2026-09-24/intents.json")["intents"]
outcomes = read("history/2026-09-24/outcomes.json")["outcomes"]
routes = read("local-omarchy-routes.json")

assert len({p["id"] for p in projects}) == len(projects)
assert len({i["id"] for i in intents}) == len(intents)
assert len({i["id"] for i in outcomes}) == len(outcomes)
assert len(crosswalk) == len(surfaces)
assert routes["route_count"] == len(routes["routes"])
assert len({r["route"] for r in routes["routes"]}) == len(routes["routes"])

project_ids = {p["id"] for p in projects}
source_entries = {entry["project"]: entry for entry in snapshot["sources"]}
assert project_ids == set(source_entries)
for project in projects:
    entry = source_entries[project["id"]]
    assert project["source_commit"] == entry["git_commit"]
    assert project["source_path"] == entry["workspace_path"]
    assert project["source_repository"] == entry["upstream_git"]
typed_ids = {i["id"] for i in intents}
candidate_ids = set(read("surface-crosswalk.json")["additional_candidates_needing_schema"])
assert {i["id"] for i in outcomes} == typed_ids | candidate_ids
for row, mapped in zip(surfaces, crosswalk, strict=True):
    assert row["project"] in project_ids
    assert row["evidence_level"] == "source_declared"
    assert (ROOT / row["source"]).is_file(), row["source"]
    assert (row["project"], row["kind"], row["name"]) == (
        mapped["project"], mapped["source_kind"], mapped["source_name"])
    assert mapped["candidate_intent"] in typed_ids | candidate_ids | {None}
    assert set(mapped.get("component_intents", [])) <= typed_ids | candidate_ids
    assert bool(mapped["candidate_intent"]) == (mapped["relationship"] == "proposed_outcome")
    assert bool(mapped.get("component_intents")) == (mapped["relationship"] == "proposed_composite")
    assert mapped["relationship"] in {"proposed_outcome", "proposed_composite", "open_ended_enabler", "non_intent_control"}

for intent in intents:
    for project, support in intent["support"].items():
        assert project in project_ids
        if evidence := support.get("evidence"):
            assert (ROOT / evidence).is_file(), (intent["id"], project, evidence)
    for example in intent["examples"]:
        assert example["parsed"]["intent"] == intent["id"]

for entry in snapshot["sources"]:
    path = ROOT / entry["workspace_path"]
    assert path.is_dir(), path
    if entry["git_commit"] is not None:
        actual = subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
        assert actual == entry["git_commit"], (entry["project"], "commit changed")
skipper_root = WORKSPACE / "private"
tracked = subprocess.check_output(["git", "-C", str(skipper_root), "ls-files", "-z"]).split(b"\0")
names = {name.decode() for name in tracked if name}
dirty_status = subprocess.check_output(
    ["git", "-C", str(skipper_root), "status", "--porcelain", "-uall"], text=True)
names.update(line[3:] for line in dirty_status.splitlines())
digest = hashlib.sha256()
for name in sorted(names):
    path = skipper_root / name
    if path.is_file() and path.suffix in {".py", ".js", ".sh", ".qml", ".json", ".lua"}:
        digest.update(name.encode() + b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
assert digest.hexdigest() == snapshot["skipper_source_digest"]
for name, expected in snapshot["skipper_file_hashes"].items():
    actual = hashlib.sha256((WORKSPACE / "private" / name).read_bytes()).hexdigest()
    assert actual == expected, (name, "working source changed; create a new dated snapshot")
for name, expected in snapshot["skipper_dirty_file_hashes"].items():
    actual = hashlib.sha256((WORKSPACE / "private" / name).read_bytes()).hexdigest()
    assert actual == expected, (name, "Skipper working file changed; create a new dated snapshot")

print('Historical source checkout matches the frozen 2026-09-24 audit')
