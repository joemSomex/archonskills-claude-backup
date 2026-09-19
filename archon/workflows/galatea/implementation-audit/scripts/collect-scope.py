"""Admit the mission before a large-tier auditor spends on it.

MISSION.md is the only thing that says what "everything" means here. A missing,
truncated or unparseable mission is a bad invocation: fail the node rather than
let an auditor invent a product scope and report gaps against it.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

MISSION = "MISSION.md"
# Guidance the auditor must read; every one of these is tracked in the repo.
GUIDANCE = ("AGENTS.md", "FACTORY_RULES.md", "FACTORY.md", "NOTES.md",
            "harness/END-TO-END.md", ".factory/holdout/HOLDOUT.md")
MODES = ("preview", "approve", "auto")
# The in-scope areas are the bold headings between these two mission sections.
OPEN = "## Core capabilities (in scope)"
CLOSE = "## Out of scope"


def areas(text: str) -> list[str]:
    start = text.find(OPEN)
    if start < 0:
        raise ValueError(f"{MISSION} has no '{OPEN}' section to audit against")
    end = text.find(CLOSE, start)
    section = text[start:end if end > 0 else len(text)]
    found = [match.strip() for match in re.findall(r"^\*\*(.+?)\*\*\s*$", section, re.M)]
    if not found:
        raise ValueError(f"{MISSION} declares no capability areas under '{OPEN}'")
    return found


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    root = Path.cwd().resolve()
    mission = root / MISSION
    if not mission.is_file():
        raise ValueError(f"{MISSION} not found; this workflow audits against it and nothing else")
    text = mission.read_text(encoding="utf-8", errors="replace")
    if len(text.strip()) < 500:
        raise ValueError(f"{MISSION} is too short to be the scope of record")
    declared = areas(text)

    wanted = os.environ.get("INPUTS_AREA", "").strip()
    if wanted:
        match = [name for name in declared if name.lower() == wanted.lower()]
        if not match:
            raise ValueError(f"area '{wanted}' is not declared in {MISSION}; "
                             f"choose one of: {', '.join(declared)}")
        wanted = match[0]

    publication = os.environ.get("INPUTS_PUBLICATION", "preview").strip() or "preview"
    if publication not in MODES:
        raise ValueError(f"publication must be one of {', '.join(MODES)}")

    bound = os.environ.get("INPUTS_MAX_GAPS", "15").strip()
    if not bound.isdigit() or not 1 <= int(bound) <= 50:
        raise ValueError("max_gaps must be an integer between 1 and 50")

    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True,
                            text=True, check=True).stdout.strip()

    print(json.dumps({
        "commit": commit,
        "area": wanted,
        "areas": declared,
        "publication": publication,
        "max_gaps": int(bound),
        # Only guidance that actually exists; a named file that is absent is a
        # fact the auditor should not be told to read.
        "guidance": [name for name in GUIDANCE if (root / name).is_file()],
    }))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"collect-scope: {error}", file=sys.stderr)
        sys.exit(1)
