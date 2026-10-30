---
name: galatea-git-sync
description: Use when syncing the Galatea main Git checkout safely.
version: 1.0.0
author: Somex Studios
license: proprietary
metadata:
  hermes:
    tags:
      - git
      - galatea
      - synchronization
    related_skills:
      - github
---

# Galatea Git Sync

## When to Use

Use for requests such as `git status`, `git pull`, or checking a numbered PR in the Galatea repository.

Use `/root/galatea-system-stagin` for the Galatea portal checkout. If the user explicitly names `galatea-system-convergence`, use `/root/galatea-system-convergence` instead; verify its repository root and origin before pulling, so the two projects are never confused. Apply the same fast-forward-only and preservation rules to either checkout.

## Sync

1. Capture `git status --short --branch` before changing anything.
2. Run `git pull --ff-only`; never create a merge commit.
3. Capture `git status --short --branch` and `git log -1 --oneline --decorate` afterward.
4. Report whether the pull was already current or the exact old and new short SHAs, the latest commit subject, and whether local `main` matches `origin/main`.
5. Preserve every untracked path. Do not stage, delete, clean, or modify local artifacts.

## Optional pull-request check

When the user names a PR, query it directly:

```bash
gh pr view <number> --repo SomexStudiosHQ/galatea-system-stagin \
  --json number,title,state,isDraft,url,mergedAt,mergeCommit,headRefName,baseRefName,reviewDecision,statusCheckRollup
```

Report its state, title, source and target branches, merge commit when present, and whether the relevant commit is included in `origin/main`. Do not assume a merged PR targeted `main`.

## Safety

- Do not apply hosted Supabase migrations during a Git sync.
- If a pull is interrupted or its effect is uncertain, inspect `git status`, `git rev-parse HEAD`, and `git log -1` before retrying.
- Do not print credentials or inspect secret files.
