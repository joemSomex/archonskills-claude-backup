# Audit Galatea Portal against its mission

Commit under audit: $scope.output.commit
Area filter (empty means every in-scope area): $scope.output.area
Declared in-scope areas: $scope.output.areas
Finding bound: $scope.output.max_gaps
Project guidance present: $scope.output.guidance
Operator context (may be empty): $ARGUMENTS

You are answering one question: **is everything MISSION.md declares in scope
actually implemented in this checkout, and does it still hold the hard
invariants?** You are not improving the product. Do not edit a single file.

## What to read, in this order

1. `MISSION.md` in full. It is the scope of record: its in-scope capabilities,
   its "Out of scope" list, its hard invariants, its definition of done, and its
   open questions all govern this audit.
2. The project guidance listed above.
3. The code. Read it — do not infer a capability from a filename, a route that
   exists, or a heading in a report. `BUILD_REPORT.md` and any other status
   document in this repo are claims, not evidence; verify them or ignore them.

## How to decide whether something is implemented

Walk each in-scope capability area (or only the filtered area, when one is
given). For every bullet the mission lists under it, find the code that
implements it and the test or journey that covers it, then classify:

- **implemented** — the code does it and something asserts it. Report nothing.
- **`missing`** — no code implements it.
- **`partial`** — code exists for part of it, or for the happy path only.
- **`broken`** — code exists and is wrong: it contradicts the mission, breaks a
  hard invariant, or cannot work as written.
- **`unverified`** — code plausibly implements it, but nothing asserts it and
  you could not establish it by reading. Say what evidence would settle it.

Four things are gaps even when the feature works:

- A **hard invariant** (MISSION.md §"Hard invariants") that the code no longer
  holds. Check each of the eleven against the code, not against a document that
  says they hold. These are `blocking`.
- Anything in the mission's **"Out of scope"** list that the code actually does.
  A service-role client, a public draft policy, or a second reset clock is a
  `blocking` finding even though nobody asked for it.
- A **definition-of-done** gate the repository cannot currently pass.
- A capability with **no coverage at all** in `harness/END-TO-END.md` or the test
  suite, where the mission says its correctness is assertable.

Three things are **not** gaps. Do not report them:

- Anything on the "Out of scope" list that is correctly absent.
- The mission's open questions Q1–Q5. They are undecided, not missing. If work
  you found depends on one, say so in the finding's body rather than answering it.
- Anything under "What the factory does NOT own" — pacing, visual judgment,
  fiction, economy balance. Those are a person's call, not an implementation gap.

## What to write

Write `$ARTIFACTS_DIR/gaps.json`: a JSON array, most severe first. Each finding
is an object with:

- `key`: short stable lowercase slug, unique in this audit. Keep it stable across
  runs — it is the dedup marker, so the same gap must produce the same key.
- `title`: imperative and specific, the outcome as a person would say it.
- `area`: the MISSION.md capability area, verbatim.
- `status`: `missing`, `partial`, `broken`, or `unverified`.
- `severity`: `blocking` (a hard invariant, an out-of-scope behaviour that
  exists, or a definition-of-done gate that fails), `major` (a declared
  capability a member would notice missing), or `minor`.
- `size`: `small_bounded`, `risky`, or `large`.
- `evidence`: the paths you actually read, as `path` or `path:line` or
  `path:start-end`, relative to the checkout. At least one. For anything other
  than `missing` the paths must exist — this is what separates a finding from a
  guess, and a deterministic check enforces it.
- `invariants`: the mission hard invariants this touches, by number and name.
  Empty when it touches none.
- `body`: Markdown that stands on its own as a ticket, so `archon-ship` can take
  it without re-deriving the context: what is wrong, the MISSION.md section it
  comes from, what you read and what you found there, the desired outcome, the
  invariants that must survive, and acceptance criteria as a checklist with
  exact values a verifier can check — not adjectives.

Rules:

1. **Order by severity, then by what a member would miss first.**
2. **Stop at the bound.** When the portal has more gaps than the bound, keep the
   most severe and end the summary with what you left for a later audit.
3. **Nothing found is a valid audit.** If every in-scope bullet is implemented
   and every invariant holds, write an empty array, return `count` 0, and say in
   the summary what you checked and what established it. That is the point of
   the workflow, not a failure.
4. **Never propose out-of-scope work**, and never report a gap you cannot point
   at code for.

Return `count` (findings), `blocking` (how many are severity `blocking`),
`verdict` — exactly `complete`, `incomplete`, or `violated` (use `violated` when
any blocking finding exists) — and a `summary`: what you audited, what holds,
what is missing, and what you could not establish by reading.
