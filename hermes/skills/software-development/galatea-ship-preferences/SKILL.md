---
name: galatea-ship-preferences
description: Use when shipping Galatea issues. Run detached and notify.
---

# Galatea ship preferences

For Galatea issue shipping from chat:

- Run the Archon ship workflow detached and return the run ID immediately.
- When the user asks to be notified, install a durable quiet monitor; notify only after the branch is pushed and the pull request is confirmed by reading it back from GitHub.
- For status updates, verify both the persisted run state and the detached owner process. A dead worker can leave a run falsely marked `running`.
- Recover an orphan using the supported abandon/adopt path, preserve the worktree/branch, and update any completion monitor to the recovery run ID.
- Report `NO_ACTION` plainly when the requested fix already exists; do not invent a PR merely to satisfy the expected workflow.
