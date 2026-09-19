"""Validate the audit before anything is published, and render it for review.

Shape, unique keys, declared severity and status, real file evidence, and the
bound are checked here deterministically. Whether a finding is worth building is
the auditor's judgment and the reader's; this script only refuses an audit no
publisher should act on -- above all one that claims a gap without pointing at
the code it read.
"""

import json
import os
import re
import sys
from pathlib import Path

STATUS = ("missing", "partial", "broken", "unverified")
SEVERITY = ("blocking", "major", "minor")
SIZES = ("small_bounded", "risky", "large")
KEY = re.compile(r"^[a-z0-9][a-z0-9-]{1,60}$")
# "src/lib/cms/schema.ts", "src/app/page.tsx:42", "harness/END-TO-END.md:12-30".
EVIDENCE = re.compile(r"^(?P<path>[A-Za-z0-9._/-]+?)(?::\d+(?:-\d+)?)?$")


def fail(message: str) -> None:
    print(f"check-gaps: {message}", file=sys.stderr)
    sys.exit(1)


def evidence_paths(root: Path, key: str, items: object) -> list[str]:
    if not isinstance(items, list) or not items:
        fail(f"finding '{key}' needs at least one evidence reference")
    paths = []
    for item in items:
        if not isinstance(item, str) or not item.strip():
            fail(f"finding '{key}' has a non-string evidence reference")
        match = EVIDENCE.match(item.strip())
        if not match:
            fail(f"finding '{key}' evidence '{item}' is not a path or path:line reference")
        path = match.group("path")
        resolved = (root / path).resolve()
        if not resolved.is_relative_to(root):
            fail(f"finding '{key}' evidence '{item}' escapes the checkout")
        # A gap may be "this file does not exist", so absence is legal for a
        # missing status only; anything else must point at code that was read.
        paths.append(path)
    return paths


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    root = Path.cwd().resolve()
    artifacts = Path(os.environ["ARTIFACTS_DIR"])
    bound = int(os.environ["INPUTS_MAX_GAPS"])
    commit = os.environ.get("INPUTS_COMMIT", "").strip()
    path = artifacts / "gaps.json"
    if not path.is_file():
        fail("the auditor wrote no gaps.json")
    try:
        findings = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"gaps.json is not valid JSON: {error}")
    if not isinstance(findings, list):
        fail("gaps.json must be an array")
    if not findings:
        # A portal that implements its mission is the point of running this.
        # Nothing to check, nothing to publish, and that is a pass.
        (artifacts / "gaps.md").write_text(
            f"# Implementation audit\n\nNo gaps found at `{commit}`.\n", encoding="utf-8")
        print(json.dumps({"count": 0, "blocking": 0, "keys": []}))
        return 0
    if len(findings) > bound:
        fail(f"{len(findings)} findings exceed the bound of {bound}")

    seen: list[str] = []
    blocking = 0
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            fail(f"finding {index} is not an object")
        for field in ("key", "title", "area", "body"):
            value = finding.get(field)
            if not isinstance(value, str) or not value.strip():
                fail(f"finding {index} needs a non-empty string '{field}'")
        key = finding["key"]
        if not KEY.match(key):
            fail(f"finding {index} key '{key}' must be a lowercase slug")
        if key in seen:
            fail(f"duplicate key '{key}'")
        if finding.get("status") not in STATUS:
            fail(f"finding '{key}' status must be one of {', '.join(STATUS)}")
        if finding.get("severity") not in SEVERITY:
            fail(f"finding '{key}' severity must be one of {', '.join(SEVERITY)}")
        if finding.get("size") not in SIZES:
            fail(f"finding '{key}' size must be one of {', '.join(SIZES)}")
        paths = evidence_paths(root, key, finding.get("evidence"))
        if finding["status"] != "missing":
            # Present-but-wrong is a claim about code; it must name code that is
            # there. Only an absent capability may cite a path that does not exist.
            absent = [p for p in paths if not (root / p).exists()]
            if absent:
                fail(f"finding '{key}' is '{finding['status']}' but its evidence "
                     f"does not exist: {', '.join(absent)}")
        invariants = finding.get("invariants", [])
        if not isinstance(invariants, list) or any(not isinstance(i, str) for i in invariants):
            fail(f"finding '{key}' invariants must be an array of strings")
        if len(finding["body"]) < 150:
            fail(f"finding '{key}' body is too short to be a ticket contract")
        if finding["severity"] == "blocking":
            blocking += 1
        seen.append(key)

    order = {name: rank for rank, name in enumerate(SEVERITY)}
    ranked = sorted(findings, key=lambda f: order[f["severity"]])
    lines = ["# Implementation audit", "",
             f"{len(findings)} findings at `{commit}` -- {blocking} blocking.", ""]
    for index, finding in enumerate(ranked, 1):
        invariants = ", ".join(finding.get("invariants", [])) or "none"
        lines += [f"## {index}. {finding['title']}", "",
                  f"- key: `{finding['key']}`  area: {finding['area']}  "
                  f"status: {finding['status']}  severity: {finding['severity']}  "
                  f"size: {finding['size']}",
                  f"- evidence: {', '.join(finding['evidence'])}",
                  f"- mission invariants touched: {invariants}",
                  "", finding["body"].strip(), ""]
    (artifacts / "gaps.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"count": len(findings), "blocking": blocking, "keys": seen}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
