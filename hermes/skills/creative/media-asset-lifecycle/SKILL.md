---
name: media-asset-lifecycle
description: "Use when retaining, archiving, or cleaning media assets."
version: 0.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [media, retention, cleanup, images, backup]
    related_skills: []
---

# Media Asset Lifecycle

Preserve approved generated media as durable project assets while allowing disposable generations and explicitly authorized archived references to expire safely. Apply the workflow to images by default and extend it to audio or video only when the user asks.

## When to Use

- The user says to keep, save, approve, archive, or retain a generated image.
- The user requests age-based cleanup of generated media caches.
- The user explicitly requests review or deletion of archived inbound image references.
- A scheduled cleanup must distinguish generated outputs from uploaded references.

## Procedure

For large inbound media, first inspect prior session history and the project archive for a verified ingestion route before recommending a new cloud-sharing service. When the source is on the user's Mac and the archive is on a remote host, prefer the established direct SSH transfer when available: `rsync -avhP "SOURCE WITH SPACES" USER@HOST:DEST/`. Confirm the current host and destination before reusing them. Give a single copy-pasteable command on ONE physical line when the exact filename and extension are known; a newline after the command prefix executes an argumentless `rsync`, then the shell tries to execute the dragged media path and reports `zsh: permission denied`. For hidden extensions, have the user drag the Finder file into Terminal before pressing Return and then append the remote destination on that same command line. On a transfer error, inspect the complete stderr before changing SSH or folder permissions: shell `zsh: permission denied: /local/video` means a command-line break, while SSH authentication and remote write errors name different failing boundaries. A screenshot or a rejected messaging attachment is not a transferred video. Keep original and analysis proxy distinct; verify destination size, server-side checksum, and full media decode before claiming the received file is complete, but do not claim source-to-destination checksum equality without the source hash.

1. **Classify the asset before acting.** Establish whether the path came from a generation result, an inbound user attachment, or an unknown source. Use the generation tool result and filename together; never classify by age alone. Treat unknown provenance as keep.
2. **Archive an approved asset by copying it.** Copy rather than move so the current platform delivery and conversation references remain valid. Use a durable root chosen by the user; when none exists, use `$HOME/outputs/approved-images/YYYY-MM-DD/`.
3. **Make the archive self-describing.** Give the copy a descriptive collision-safe filename and create companion metadata recording the generation prompt when available, provider/model, source path, approval time, and SHA-256 checksum. Do not invent missing prompt or model details. For explicitly time-limited reference libraries, use a dedicated non-Git retention directory, a numbered manifest, and a memory index with the same absolute expiry. Preserve each user-confirmed numbered slot even if two uploaded files have identical bytes; deduplicate storage only if the slot-to-source mapping remains intact, because processing may still be requested per slot. Verify slot count and source-copy hashes before scheduling a script-only deletion. Check the script in preview mode and exercise before-expiry, checksum-change, expiry, unrelated-file protection, and repeat-run cases using synthetic fixtures, never live user assets. Limit deletion to enumerated matching files, and state that platform-hosted originals and independent backups are not erased by local retention.
4. **Verify before acknowledging.** Confirm the durable copy exists, its size is nonzero, and its checksum matches the source. Return the permanent path and checksum.
5. **Preview generated-cache cleanup first.** Enumerate only provider-generated cache files strictly older than the requested retention period. Report file count, total bytes, oldest/newest timestamps, and sample paths before enabling deletion. When the user explicitly requests a full temporary Hermes-cache clear, resolve `${HERMES_HOME:-~/.hermes}/cache`, assert that exact path before deletion, remove only its children, preserve the cache root, and immediately recreate the runtime directories used by the shell and tools (at minimum `terminal/`, `terminal-output/`, `exec/`, `images/`, `documents/`, `videos/`, and `browser-use/workspace/`). The terminal snapshot hook writes after each command, so deleting `terminal/` without recreating it produces a misleading post-command error even when cleanup succeeded. Measure bytes before and after, and keep project outputs plus the Obsidian/GBrain archive out of scope.
6. **Preview archived-reference cleanup from provenance metadata.** Only after explicit authorization to review uploaded references, select records whose declared media type matches the request and whose archive `created` timestamp is strictly earlier than the UTC cutoff. Use the archive timestamp rather than filesystem mtime because copying, synchronization, and reindexing can change mtime without changing age. Pair every metadata note with its referenced binary, report the cutoff, candidate count, total bytes, oldest/newest candidate, and the exact candidate list.
7. **Honor preview gates literally.** When the user says to show the list first, stop after the preview and await a new confirmation even if the same message also says “delete.” The requested review boundary is an explicit destructive-action gate.
8. **Exclude protected classes explicitly.** For generated-cache cleanup, never delete inbound attachment names such as `img_*`, approved-asset directories, project assets, knowledge archives, or files of unknown provenance. Maintain an allowlist of observed provider-generated prefixes rather than a broad “everything except” rule, because new platform attachment formats may appear. For separately authorized reference cleanup, exclude videos, documents, and audio when the request names images only.
9. **Delete archived pairs coherently.** Remove an archived reference only when both its metadata record and referenced binary have been identified and the owning knowledge index can be synchronized afterward; otherwise fail closed rather than leaving an orphaned binary, broken note, or stale searchable record.
10. **Schedule deterministic cleanup without an LLM.** Use a script-only cron job for recurring cleanup. Keep preview mode as the initial state; enable permanent deletion only after the operator verifies the selection. On each destructive run, print the deleted count and reclaimed bytes; on uncertainty or script error, delete nothing and fail visibly.

## Always-On Rules

- “Keep this image” means preserve one verified durable copy plus metadata; it does not mean retain every intermediate generation.
- Retention cleanup applies to disposable generated outputs by default. Uploaded references and user-provided media require separate explicit authorization and a metadata-driven preview.
- Use a strict UTC cutoff for “older than N days”; items exactly on the boundary are not older.
- Never claim storage was reclaimed until the deletion completed and disk usage was measured again.
- Clearing the temporary Hermes cache must not delete durable project deliverables or archived references; report those stores separately so the user knows what remains retrievable.
- Do not store passwords, tokens, or private authentication material in media metadata.

## Verification

- Approved assets survive removal of their cache originals.
- Source and archived-copy checksums match.
- Generated-cache preview selects only known generated outputs older than the retention threshold.
- Archived-reference preview uses declared media type and archive creation time, lists paired note and binary records, and pauses at any requested review gate.
- Protected, out-of-scope, and unknown files remain untouched.
- Completed archived-reference deletion leaves no orphaned binary, broken metadata note, or stale knowledge-index entry.
- Scheduled cleanup is script-only, reports reclaimed space, and fails closed.
