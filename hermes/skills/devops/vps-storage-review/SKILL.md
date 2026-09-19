---
name: vps-storage-review
description: "Use when auditing VPS storage, cleanup, or backups."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [storage, disk, VPS, cleanup, Docker]
    related_skills: []
---

# VPS Storage Review

Audit live disk use, explain growth, and rank safe cleanup opportunities without deleting anything unless the user explicitly approves a defined scope.

## When to Use

- The user asks how much VPS storage remains.
- The user asks for a disk-usage breakdown or cleanup plan.
- Disk use has grown and the user wants to know why.
- The user asks what must be backed up, how large an archive will be, or what can safely be delivered through chat.

Do not use for RAM, model context, or account-token usage; label those separately so “memory” is not confused with disk storage.

## Procedure

1. **Measure the filesystem first.** Use `terminal(command="df -h /")` and report total, used, available, and percentage from that fresh result. Never reuse an earlier number because build and agent workspaces can grow quickly.
2. **Attribute usage hierarchically.** Use bounded, same-filesystem `du` scans at `/`, then only the largest first-level directories, then the dominant children. Prefer `du -x -h --max-depth=1 <path>` and sort the returned rows programmatically or with `sort`; stop once the major consumers explain the used space.
3. **Inspect managed storage with its owner.** For Docker, run `docker system df` and `docker system df -v` instead of inferring reclaimable bytes from `/var/lib/containerd`. For journals, use `journalctl --disk-usage`. Do not manually delete files from containerd, Docker, package-manager, or journal internals because their metadata owns those files.
4. **Protect active work.** Before recommending deletion of run directories, worktrees, build outputs, or agent caches, inspect live processes and the relevant workflow manager. Keep active runs and their associated workspaces. Require committed or pushed work and preserved artifacts before retiring completed workspaces.
5. **Separate persistent data from cache.** Classify repositories, databases, knowledge archives, credentials, and project outputs as persistent. Classify provider downloads, package caches, build layers, browser binaries, generated-image caches, and stale worktrees as potentially reclaimable. An item being a cache does not make it disposable when current conversations or tools still reference it.
6. **Rank cleanup by reclaimable size and risk.** Lead with exact or provider-reported reclaimable space. Prefer managed cleanup commands such as Docker builder/image pruning over manual deletion. State the consequence: slower rebuilds, loss of rollback images, re-download cost, or loss of conversation-linked media.
7. **Classify backup scope before sizing or delivery.** Distinguish a credential-free portable profile export from a full disaster-recovery backup and from external data such as GBrain, Obsidian, application databases, and project repositories. Read `references/backup-scope.md` when the user asks for backup contents, size, restore coverage, scheduled rotation, or chat delivery.
8. **Build portable exports through a verification gate.** Run `hermes profile export <profile>` into a private temporary path, inspect the actual members, then repackage only the requested profile-owned classes. Follow the inspect → whitelist → credential scan → full decompression check → checksum → atomic publish → retention sequence in `references/backup-scope.md`; profile-export contents and installed-skill symlinks can vary by version and installation.
9. **Measure archives rather than estimating compression.** Create the exact requested archive at a private temporary path, read its byte size, then remove the temporary copy unless the user asked to retain it. Images, generated dependencies, and database pages compress unpredictably, so directory size is not an archive-size measurement.
10. **Re-measure after any approved cleanup.** Run `df -h /` again and read back the target directory or subsystem. Report actual space recovered, not the projected sum.

## Always-On Rules

- Report live numbers, not estimates from prior turns.
- Distinguish decimal `GB` from binary `GiB` when precision matters; do not imply differently rounded tools disagree.
- Never add directory sizes as if they were independent when one path contains another.
- Never claim all Docker “reclaimable” space is consequence-free; unused images may provide deployment rollback and build cache speeds future builds.
- Never delete active workspaces or database/container data based only on age or size.
- Archive important generated media before clearing messaging or Hermes caches.
- Never send a full Hermes backup through chat: it contains credentials and authentication state. Offer a verified, scoped profile export for chat and keep full backups encrypted in private storage.
- Never assume `hermes profile export` exactly matches a requested scope: inspect and whitelist members because profile data classes and absolute installed-skill links can be included.
- Never rotate older backups until the new archive has opened successfully, every member has decompressed, the required members are present, and the checksum has been computed; verification failure must leave prior backups untouched.
- Treat host snapshots and logical backups as complementary: filesystem recovery does not replace application-consistent database or live PGLite snapshots.
- Never bypass a live PGLite lock for backup. Coordinate with the owning GBrain process, because copying an actively written datastore can produce an inconsistent restore.
- Keep the user-facing summary concise: current capacity, largest consumers, safest first action, projected reclaim, and risks.

## Verification

- `df` was run in the current turn.
- The listed largest consumers are based on a current hierarchical scan.
- Managed subsystems were queried through their own tooling.
- Active processes were considered before workspace cleanup advice.
- No data was deleted without explicit approval.
- Any completed cleanup was followed by a fresh filesystem measurement.
- Backup advice distinguishes portable profile, full Hermes, and external-data coverage.
- A portable archive was inspected for forbidden members and credential-bearing filenames, fully decompressed, checked for required content, and hashed before publication or rotation.
- Any reported archive size and checksum came from the final retained archive.

## References

- `references/backup-scope.md` — backup scope, safe delivery, sizing, and restore decision table.
