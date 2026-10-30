---
name: one-off-character-batch-runner
description: "Use when running overnight character-sheet batches."
version: 1.0.0
author: Hermes Agent
license: Proprietary
metadata:
  hermes:
    tags: [character-design, automation, overnight, image-generation]
    related_skills: [character-live-action-to-game-design, hermes-agent]
---

# One-off character batch runner

## When to Use

Use only with explicit user authorization for a bounded unattended batch. This skill does not create standing authority, a recurring schedule, or permission to select new sources.

1. Load `character-live-action-to-game-design`, its full generation brief, and `hermes-agent` plus its CLI reference. Recover the exact numbered source manifest, verify count/order and original checksums, and use the numeric destination from the current message origin. Never infer a chat ID from its display name.
2. Run one source at a time through a fresh, OpenAI-pinned child agent. Use the attached original to derive source-specific identity, covering, wardrobe and palette. The skill's default is ten independently generated three-view PNGs per source, not ten total for the entire queue. Never mix source sheets in one generation call.
3. Keep the complete generation brief in every image-generation request; a source-specific identity lock and variation suffix supplement it rather than replace it. Require OpenAI receipts and disallow inference/image fallback providers or Higgsfield. Do not spend banked resets without explicit authorization.
4. Persist per-source state, per-slot generation receipts, final paths/checksums and visual-QA findings. Require actual visual inspection of the original and output contact sheets, with final-size crops for ambiguous details. Distinct hashes prove different files, not meaningful variations or fidelity. Do not count an unfinished or visually failed set as completed.
5. Deliver accepted standalone files with both source and variation labels before starting the next source. Persist actual destination and message IDs from Telegram delivery receipts, reject warnings/partial sends, and preserve delivered-slot checkpoints to avoid duplicate posts after recovery. Telegram Bot API does not offer a general getMessage readback; do not describe receipt checks as independently reading a posted message back.
6. Use an explicitly bounded, one-off process that survives the initiating turn; do not use conversation-scoped subagents for an overnight lifetime. A transient systemd service with Restart=no and an agreed/disclosed overnight cutoff is appropriate. Verify active service, live child-agent events and actual delivery destination before saying the worker started. A script on disk is not a running job.
7. Keep source-retention rules separate from output generation. Do not extend the input archive's expiry or delete source files as part of queue processing. On completion or cutoff, send truthful counts for completed, partial, failed, pending and delivered outputs. Do not schedule another night automatically.

## Completing a partial pass

- Distinguish process completion from deliverable completion: an exited-success worker can still have partial source sets. Parse all per-source QA and delivery receipts, calculate missing slots programmatically, and do not say the requested run is complete until every required slot is accepted and posted.
- On explicit renewed authorization to complete a run, repair only rejected/undelivered slots, keeping accepted files and message IDs untouched. Do not restart an expired nightly service against its old cutoff or repost successful sets. Preserve rejected versions and original QA before replacement.
- Treat content refusals as blockers, not an invitation to repeatedly vary phrasing. If a legitimate wardrobe/coverage adaptation could resolve the issue, obtain explicit permission because it changes the source design; record that override and apply it only to the authorized slots. Never bypass provider safeguards.
- After a shared style failure, correct and visually inspect one source-specific slot before generating the remaining failed variations. Use the original source only, not a prior generated image, and retain the full authoritative brief.
- For an otherwise accepted sheet with a small unwanted signature, use tight localized inpainting, prove zero changed pixels outside the edit mask, and inspect the repaired region at native resolution instead of redrawing the whole character.
- Before closing the task, enumerate every source/slot, recompute final-file hashes and PNG dimensions, require unique successful message IDs to the exact target, and regenerate affected contact sheets/manifests. Preserve historical delivery summaries as historical records rather than rewriting them to imply the old pass was complete.

## Runtime pitfalls

- Discover the real launcher with `type -a hermes` and `shutil.which`; the first PATH entry may be an environment entry point, while `/root/.local/bin/hermes` may be a different launcher. Check live help before selecting private launcher flags.
- Use Hermes' `load_config()` rather than importing PyYAML directly in a helper. This packaged deployment can run Hermes without a standalone `yaml` module. Importing `hermes_bootstrap` does not itself make PyYAML available.
- Verify the generator helper's imports and its OpenAI dispatch path before launching the full queue. Never install host packages just to replace a working built-in config loader.
- Clear inherited session/RPC/kernel variables for fresh CLI workers and supply a stable PATH. Preserve the active profile rather than creating or modifying another profile.

## Existing implementation discovery

The default profile's reusable entry points are `/root/.hermes/scripts/overnight_character_dispatch.py` and `/root/.hermes/scripts/overnight_character_generate.py`. Read them before reuse: source manifest, output directory, target, model and cutoff are task-specific values, not defaults for a future run. Check the existing transient service and state before starting another worker. Do not overwrite an active run or duplicate its delivery.
