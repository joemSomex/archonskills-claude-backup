---
name: galatea-archon
description: |
  Run Archon workflows on the Galatea portal (/root/galatea-system-stagin): audit whether
  everything in MISSION.md is actually implemented, take an issue or request to a reviewed
  PR, or triage whether work is ready to build. Use whenever the user asks about Galatea
  implementation status ("is everything implemented", "what is missing", "audit the portal"),
  asks to implement or fix something in Galatea, or asks about a running Archon run.
---

# Archon on the Galatea portal

Archon drives all engineering work on the Galatea portal at
`/root/galatea-system-stagin` (GitHub `SomexStudios/galatea-system-stagin`).
Everything runs through one command, `galatea-archon`, which is on `PATH`.
Never call `archon` directly and never edit the pinned engine under
`/root/.cache/factory/archon/<sha>/` — it is verified byte for byte and any
change there stops every run.

## Pick the command from what the user asked

| They asked | Run |
|---|---|
| "is everything implemented", "audit the portal", "what's missing", "did we skip anything in the mission" | `galatea-archon audit --detach` |
| the same, for one area only | `galatea-archon audit Forum --detach` |
| "implement this whole spec/feature", "build the leveling system", a design doc | `galatea-archon backlog <doc.md> --detach` |
| "implement issue #12", "fix the login bug", "build X" (ONE item) | `galatea-archon ship "<the request>" --detach` |
| "is this ready to build?", "should we do X?" | `galatea-archon triage "<the request>" --detach` |
| "how's the run going", "what happened" | `galatea-archon get <run-id>` |
| "show me the audit" | `galatea-archon report` |
| "is Archon healthy" | `galatea-archon doctor` |

Valid areas, exactly as MISSION.md spells them: `"Membership and identity"`,
`Forum`, `"Quantum XIII progression"`, `Broadcasts`, `"Terminal and content"`,
`"Engineering quality"`.

## Rules

1. **Always pass `--detach` when the request came from chat.** These runs take
   many minutes. `--detach` returns a run id immediately; report that id back and
   tell the user to ask for it later. Without it the turn blocks until the run
   ends. Run it in the foreground only when the user is at a terminal and asked
   to watch it.
2. **The audit publishes nothing by default.** `galatea-archon audit` only
   writes a report. To open GitHub issues from it, use
   `--publish approve`, which pauses at a gate the user must answer with
   `galatea-archon approve <run-id>`. Use `--publish auto` only when the user
   explicitly said to create the issues without being asked again.
3. **Never approve, reject, merge or deploy on the user's behalf.** `approve`,
   `reject` and `respond` relay a decision the user has actually made in this
   conversation. An Archon gate is the user's call, not yours.
4. **Report what the run says, not what you expect.** A run that failed, is
   still going, or returned `verdict: violated` is reported as such.
5. **`audit` is read-only.** It never edits the product. Fixing what it finds is
   `galatea-archon ship`, one finding at a time.
6. **One work item per `ship` run.** Triage refuses a target that implies a batch
   ("fix the forum", "implement Quantum XIII") with `route: no_action` rather than
   guessing which part to build. A whole spec or feature goes to `backlog` first,
   which slices it into ordered tickets; then `ship` them one at a time.
7. **`backlog` needs a text document in the repo.** A `.docx`/`.pdf` reaches the
   planner as replacement characters. The Quantum XIII spec's readable twin is
   `xp-rules/Quantum_XIII_Leveling_System_v1.md`, not the `.docx` beside it, and
   MISSION.md already names the Markdown as the spec of record. `backlog` refuses
   a binary path and tells you the one to use.
8. **`backlog` publishes nothing by default either.** Add `--publish approve` to
   open the issues behind a gate.
6. `galatea-archon halt` stops new launches; `unhalt` clears it. Cancel a live
   run with `galatea-archon cancel <run-id>`.

## The normal loop

```bash
galatea-archon audit --detach          # → run id
galatea-archon get <run-id>            # → verdict + findings
galatea-archon report                  # → the full gap report
galatea-archon ship "<finding title>" --detach   # fix one, with gates
```

Implementing a whole spec is the same shape, one step earlier:

```bash
galatea-archon backlog xp-rules/Quantum_XIII_Leveling_System_v1.md \
  --publish approve --detach        # → run id, pauses at a gate
galatea-archon approve <run-id>      # opens the tickets
galatea-archon ship "<ticket title>" --detach   # build them in order
```

The audit writes `gaps.md` and `gaps.json` into the run's artifacts directory
under `~/.archon/workspaces/SomexStudios/galatea-system-stagin/artifacts/runs/`.
Each finding is already shaped as a ticket, so its title and body can be handed
to `ship` unchanged.

## What the audit will not do

It will not report the mission's open questions Q1–Q5 as gaps (they are
undecided, not missing), will not propose anything on the "Out of scope" list,
and will not judge pacing, visuals, fiction or economy balance — MISSION.md
reserves all four for a human. If the user wants one of those, answer them
directly instead of starting a run.
