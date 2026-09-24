#!/usr/bin/env python3
"""Render the dated, source-backed intent coverage report."""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs" / "intent-coverage.md"
PROJECTS = ("skipper", "genesis", "omarvis", "oma")


def read(name, key):
    return json.loads((ROOT / "data" / name).read_text())[key]


def render():
    intents = read("history/2026-09-24/intents.json", "intents")
    outcomes = read("history/2026-09-24/outcomes.json", "outcomes")
    counts = {project: Counter(row["support"][project]["status"] for row in intents)
              for project in PROJECTS}
    groups = defaultdict(list)
    for row in outcomes:
        if row["status"] == "needs_schema_review":
            groups[row["id"].split(".", 1)[0]].append(row)

    lines = [
        "# Intent coverage — 2026-09-24 source snapshot",
        "",
        "This report answers which user outcomes the inspected source *appears* to support.",
        "It does not claim that a spoken phrase or desktop action succeeded. See the",
        "[verification record](verification.md) for the tests actually run and their limits.",
        "Source versions and the full twelve-project inventory are in",
        "[the snapshot](../data/snapshot.json) and [projects](projects.md).",
        "",
        "## How to read coverage",
        "",
        "- **Explicit:** a named command or route for this outcome is declared in source.",
        "- **Tool:** a general tool can potentially perform it; phrase recognition and",
        "  execution have not been demonstrated.",
        "- **Extension:** an integration or configured extension may provide it.",
        "- **Unknown:** this inventory found no specific evidence; it does not prove",
        "  the project cannot do it.",
        "",
        "The 55 typed intents below were reviewed across Skipper, Genesis, Omarvis,",
        f"and OMA. The other eight projects are included in the {len(outcomes)}-outcome source",
        "crosswalk, but they have not received the same four-status review.",
        "A project's appearance in the candidate list means only that a declared",
        "source surface was *provisionally mapped* to that outcome.",
        "",
        "## Reviewed intent summary",
        "",
        "| Project | Explicit | Tool | Extension | Unknown |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for project in PROJECTS:
        c = counts[project]
        lines.append(f"| {project} | {c['explicit']} | {c['tool']} | "
                     f"{c['extension']} | {c['unknown']} |")
    lines += [
        "",
        "## All 55 typed intents",
        "",
        "Each status is source evidence for that project. Intent names and slot types",
        "come from [the typed dataset](../data/intents.json); that file also gives",
        "illustrative phrases and a source path for each supported entry.",
        "",
        "| Intent | Slots | Skipper | Genesis | Omarvis | OMA |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in intents:
        slots = ", ".join(f"`{name}`: {kind}" for name, kind in row["slots"].items()) or "—"
        statuses = [row["support"][p]["status"] for p in PROJECTS]
        lines.append(f"| `{row['id']}` | {slots} | " + " | ".join(statuses) + " |")
    lines += [
        "",
        "## Additional candidate outcomes needing schemas",
        "",
        f"These {sum(len(rows) for rows in groups.values())} IDs come from the "
        "[source crosswalk](../data/surface-crosswalk.json).",
        "They still need human review of meaning, arguments, and examples. Project",
        "names in the table are proposed source mappings, not verified voice coverage.",
        "An em dash means no project has been mapped to that candidate yet.",
        "",
    ]
    for category in sorted(groups):
        rows = sorted(groups[category], key=lambda row: row["id"])
        lines += [f"### {category} ({len(rows)})", "", "| Candidate intent | Proposed source mapping |",
                  "| --- | --- |"]
        for row in rows:
            mapped = ", ".join(row["mapped_projects"]) or "—"
            lines.append(f"| `{row['id']}` | {mapped} |")
        lines.append("")
    lines += [
        "## Next evidence needed",
        "",
        "To claim a feature worked on this date, record an exact phrase, environment,",
        "expected result, observed result, and test artifact for the pinned source.",
        "The [method](method.md) specifies those fields. The searchable",
        "[intent matrix](../index.html) and [outcome browser](../outcomes.html)",
        "show the same inventory with filters.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the report is stale")
    args = parser.parse_args()
    content = render()
    if args.check:
        if not REPORT.is_file() or REPORT.read_text() != content:
            parser.error(f"{REPORT} is missing or stale; regenerate it")
        print("OK: intent coverage Markdown matches dataset")
    else:
        REPORT.write_text(content)
        print(f"Wrote {REPORT}")
