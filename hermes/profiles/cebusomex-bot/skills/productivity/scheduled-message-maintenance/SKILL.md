---
name: scheduled-message-maintenance
description: "Use when editing existing scheduled messages or reminders."
version: 1.0.0
metadata:
  hermes:
    tags: [cron, reminders, scheduled-messages, maintenance]
---

# Scheduled Message Maintenance

Update an existing Hermes cron message without duplicating the job, disturbing its schedule, or silently changing its wording.

## Workflow

1. Load the `hermes-agent` skill and its background-systems reference before changing Hermes cron state.
2. List jobs with the cron-management tool. Match the requested job by name, purpose, and delivery target; never infer or guess its ID.
3. Recover the **complete current prompt** before editing. Cron listings may expose only a preview. Resolve the active profile through `$HERMES_HOME` (falling back to `~/.hermes` only when unset), then read the matching entry from `cron/jobs.json` if the management interface does not return the full prompt.
4. Make the smallest requested edit. Preserve schedule, delivery, failure delivery, model settings, skills, continuity, and unrelated prompt wording unless the user explicitly asks to change them.
5. When changing a date or threshold, update every dependent occurrence in one edit:
   - the human-readable target date;
   - the machine-readable date used in calculations;
   - cutoff or post-event wording;
   - singular, tomorrow, today, and expired branches when their semantics depend on the date.
6. Update the existing job through the cron-management tool; do not create a near-duplicate.
7. Verify by reading back the exact persisted prompt and checking every dependent value. A successful update response with a truncated preview is not sufficient verification.
8. Do not trigger a test run unless the user asks: recurring message jobs can deliver immediately to a shared channel.

## Standing Rules

- Preserve the user's exact prompt wording and formatting outside the requested change; do not add optional improvements.
- Treat declared dates as literal requirements even when an older prompt contains a conflicting value. Apply the requested final value consistently rather than “correcting” it from context.
- Report only what changed, what was verified, and when it will take effect.

## Pitfalls

- **Read the full prompt before replacing it** — the update operation replaces the prompt wholesale, while list output may truncate it.
- **Search for semantic duplicates of the changed value** — countdown prompts often repeat one date in prose, ISO arithmetic, and expiration branches.
- **Verify persisted state, not the mutation response** — a success flag proves the write was accepted, not that every dependent occurrence is correct.
