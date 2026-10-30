---
name: galatea-ship-preferences
description: Use when shipping Galatea issues. Run detached and notify.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [galatea, archon, github, coolify, deployment]
    related_skills: [galatea-archon, github]
---

# Galatea ship preferences

## When to Use

Use for taking one Galatea issue from live-ticket preflight through an isolated, reviewed PR, and for verifying its post-merge staging deployment. Load the Coolify reference only when configuring or testing automatic deployment.

## Procedure

1. **Preflight the issue and existing work.** Read the live issue and comments, search all PRs for the issue and title keywords, and inspect any recorded Archon run and completion monitor before launching another run. Report `NO_ACTION` plainly when the requested fix already exists; never invent a PR merely to satisfy the expected workflow.
2. **Separate deployment layers for live regressions.** Verify repository/merge state, the commit and git source actually running in Coolify, hosted Supabase migration/object state, and signed-in browser behavior independently. A corrected deploy source or current container proves only that frontend code is present; keep the ticket open while its database contract or authenticated desktop/mobile verification remains incomplete.
3. **Protect pending PRs before a new launch.** Check prior Galatea ship runs and their PR states before invoking `galatea-archon ship`; launch-time worktree cleanup can reap completed runs. Run `galatea-archon status`, map every surviving worktree to its branch, and read any matching PR from GitHub. If any PR has not been explicitly approved for merge, stop and resolve that lifecycle first rather than allowing cleanup to decide it.
4. **Launch detached.** Run the Archon ship workflow with `--detach` and return the run ID immediately.
5. **Install or repoint one durable quiet monitor.** When the user wants notification, monitor for a pushed branch, a GitHub-confirmed PR, human gates, and the terminal run state. Reuse the existing issue monitor when superseding a run: update the run ID in both its deterministic monitor script and its complete cron prompt instead of creating a duplicate job. Run the monitor script once and read the persisted cron record to verify both updates.
6. **Verify milestones before notifying.** Read a PR back from GitHub before announcing it. At completion, verify the persisted Archon state, detached owner process, PR state, and checks; a dead worker can leave a run falsely marked `running`.
7. **Keep staging deployment event-driven and singular.** Let the GitHub push webhook trigger Coolify after Joshua merges to `main`; do not make Archon call the deployment API as a second trigger. The post-merge monitor observes and verifies the deployment instead. A successful webhook ping proves reachability only—the release is complete only when one deployment reaches healthy and `/api/build-id` equals the merge commit. Use the detailed setup and verification recipe in `references/coolify-auto-deploy.md`.

## Recovery and safety rules

- Recover an orphan using the supported abandon/adopt path, preserving its worktree and branch before repointing the monitor.
- When a run has terminally failed and cannot be adopted, inspect its triage artifact and search GitHub before restarting. If triage selected `no_action` because an existing PR already delivers the issue but a contract validator rejected that route, treat the run as `NO_ACTION`: verify the original run and PR instead of launching duplicate engineering work.
- Start one superseding detached run only when no existing branch or PR already delivers the issue; record which run it supersedes in the monitor and verify the new owner process is alive before reporting recovery.
- When a ship run is blocked only on a product-owner decision, record the decision in the issue or another repository-visible human-owned source and read it back before retrying; a decision embedded only in the launch target is not durable evidence and triage may reject it when protected governance says otherwise.
- Never approve, reject, merge, deploy, or apply a hosted Supabase migration without the user's explicit decision.
- Treat GitHub user `@joemSomex` as the sole intended merger of Galatea pull requests into `main`. Create and verify PRs, but leave them open for Joshua to merge unless he gives an explicit per-PR instruction to merge. The private repository is owned by the free-plan organization `SomexStudiosHQ`; because GitHub Free cannot enforce protected-branch merge restrictions there, collaborators such as `edsel-Somex` must remain `Triage` or `Read`, never `Write`, if this sole-merger policy is to hold.

### Pull-request conflict recovery

- Check whether any detached owner process for the PR branch is alive before editing; cancel that run first so it cannot overwrite the resolution.
- Fetch the exact PR head and current base. If no worktree owns the head branch, create an isolated tracking worktree rather than disturbing the shared checkout. Explicitly run the merge from that worktree: creating a worktree does not change the caller's working directory, so an unqualified next command may act on the shared checkout instead.
- Resolve per hunk by product intent. During `git merge origin/<base>`, stage 2 (`:2:path`) is the PR side and stage 3 (`:3:path`) is the base side. Preserve both features semantically; take an entire side only when history and consumers prove that blob is the required strict superset or generated output.
- Treat generated manifests as dependency maps, not ordinary prose conflicts. When the base renamed, content-hashed, or compressed assets, keep its current paths while preserving the feature's generator behavior, verify every referenced asset exists, and do not rebake unless generator inputs actually changed.
- When the merged base changes `package.json` or its lockfile, install from the merged lockfile inside the worktree with `npm ci`. Do not reuse or symlink another checkout's `node_modules`, because it may predate the base's dependencies and produce false missing-import failures.
- Scan migration prefixes after the merge. Renumber a migration introduced by the feature only when the merge makes its numeric prefix collide, and update every reference; report unrelated pre-existing duplicate prefixes instead of changing them as drive-by cleanup.
- Validate in this order: focused tests for the conflicted behavior, production build, standalone typecheck, full tests, lint, then the repository's post-build leak/chunk checks. In a fresh Next.js worktree, build before the final standalone typecheck so generated route types exist; a pre-build `PageProps`/`LayoutProps` failure is not final evidence.
- When a validation check fails, run the same check against isolated worktrees at the PR head and current base before editing assertions. Fix merge-only regressions; report parent failures as pre-existing, and separate a small required build repair rather than hiding it inside the conflict resolution.
- Re-fetch the base and head and re-read `state`, `headRefOid`, `mergedAt`, and `mergeCommit` immediately before pushing. If the head moved, reconcile it instead of force-pushing. If the PR merged while resolution was underway, stop pushing to the stale head, verify the merge commit is on the base, and open a narrowly scoped follow-up PR only for independently verified defects.
- Push the merge commit only when the PR is still open and unchanged, then read the PR back until GitHub reports a stable mergeability state (`CLEAN`/`MERGEABLE` or a real blocker). Report configured CI separately; an empty check list is not a green CI run.
