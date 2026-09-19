# Publish the implementation audit as GitHub issues

Mode: $INPUTS.mode
Native approval: $INPUTS.approval

Read `$ARTIFACTS_DIR/gaps.json` (validated) and `$ARTIFACTS_DIR/gaps.md`.
Only `auto`, explicitly selected by the caller, or `approve` with a native
decision of `approve` authorizes writes. Otherwise return `published=false` with
empty `created` and `existing` and write nothing.

Use `gh` scoped to the origin repository's exact `owner/repo`. Work in the order
`gaps.md` renders (most severe first), one finding at a time:

1. The finding's marker is the line `<!-- galatea-implementation-audit: <key> -->`.
   Search open and closed issues for that exact marker before every write. If it
   exists, record the issue URL under `existing` and move on: an audit that runs
   weekly must never post the same gap twice.
2. Otherwise create the issue with `gh issue create` from a body file: the
   finding's body, then a blank line, then a line naming the audited commit and
   the evidence paths, then the marker as the last line. Use the repository's
   issue template if one exists. Read the created issue back and record its URL
   under `created`.
3. After an uncertain write, read before retrying. Never retry a create blindly.

Do not apply labels unless the caller supplied a mapping — the project's
`archon-*` state labels belong to triage, and guessing one here would route work
that triage has not seen. Do not assign, milestone, close, or comment on any
existing issue.

Write `$ARTIFACTS_DIR/gaps-publication.md` with every finding, its outcome and
URL. Return `published=true` only when every finding was created or already
present, plus the `created` and `existing` URL lists and a one-paragraph
`summary`. Partial failure is reported truthfully as `published=false` with what
did land.
