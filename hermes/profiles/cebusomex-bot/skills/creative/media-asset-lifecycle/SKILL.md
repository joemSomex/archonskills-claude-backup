---
name: media-asset-lifecycle
description: "Use when retaining or cleaning generated media assets."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [media, retention, cleanup, images, backup]
    related_skills: []
---

# Media Asset Lifecycle

Preserve approved generated media as durable project assets while allowing disposable generations to expire safely. Apply the workflow to images by default and extend it to audio or video only when the user asks.

## When to Use

- The user says to keep, save, approve, archive, or retain a generated image.
- The user requests age-based cleanup of generated media caches.
- A scheduled cleanup must distinguish generated outputs from uploaded references.

## Procedure

1. **Classify the asset before acting.** Establish whether the path came from a generation result, an inbound user attachment, or an unknown source. Use the generation tool result and filename together; never classify by age alone. Treat unknown provenance as keep.
2. **Archive an approved asset by copying it.** Copy rather than move so the current platform delivery and conversation references remain valid. Use a durable root chosen by the user; when none exists, use `$HOME/outputs/approved-images/YYYY-MM-DD/`.
3. **Make the archive self-describing.** Give the copy a descriptive collision-safe filename and create companion metadata recording the generation prompt when available, provider/model, source path, approval time, and SHA-256 checksum. Do not invent missing prompt or model details.
4. **Verify before acknowledging.** Confirm the durable copy exists, its size is nonzero, and its checksum matches the source. Return the permanent path and checksum.
5. **Preview cleanup first.** Enumerate only provider-generated cache files older than the requested retention period. Report file count, total bytes, oldest/newest timestamps, and sample paths before enabling deletion.
6. **Exclude protected classes explicitly.** Never delete inbound attachment names such as `img_*`, approved-asset directories, project assets, knowledge archives, or files of unknown provenance. Maintain an allowlist of observed provider-generated prefixes rather than a broad “everything except” rule, because new platform attachment formats may appear.
7. **Schedule deterministic cleanup without an LLM.** Use a script-only cron job for recurring cleanup. Keep preview mode as the initial state; enable permanent deletion only after the operator verifies the selection. On each destructive run, print the deleted count and reclaimed bytes; on uncertainty or script error, delete nothing and fail visibly.

## Always-On Rules

- “Keep this image” means preserve one verified durable copy plus metadata; it does not mean retain every intermediate generation.
- Retention cleanup applies to disposable generated outputs only. Uploaded references and user-provided media require separate explicit authorization.
- Never claim storage was reclaimed until the deletion completed and disk usage was measured again.
- Do not store passwords, tokens, or private authentication material in media metadata.

## Verification

- Approved assets survive removal of their cache originals.
- Source and archived-copy checksums match.
- Cleanup preview selects only known generated outputs older than the retention threshold.
- Protected and unknown files remain untouched.
- Scheduled cleanup is script-only, reports reclaimed space, and fails closed.
