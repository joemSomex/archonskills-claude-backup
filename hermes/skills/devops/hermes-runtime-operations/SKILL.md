---
name: hermes-runtime-operations
description: "Use when testing or repairing Hermes runtime services."
version: 1.0.0
---

# Hermes Runtime Operations

Use this skill for Hermes gateway/systemd status checks, package-environment repair, service recovery, and post-repair health tests. Load the bundled `hermes-agent` skill first because its current CLI and troubleshooting guidance remains authoritative.

## Operating workflow

1. Establish the real service state; do not rely on the condensed `hermes status` label alone.
   - Run `hermes status` or `hermes gateway status --system` for the product view.
   - Run `systemctl status hermes-gateway --no-pager --full` and inspect `ActiveState`, `SubState`, `Result`, `ExecMainStatus`, and `NRestarts` with `systemctl show`.
   - Treat `activating (auto-restart)` as a crash loop, not as a stopped or healthy service.

2. Read the service journal before changing anything.
   - Use `journalctl -u hermes-gateway --no-pager --since '<window>' -n <count>`.
   - Identify the first direct startup failure separately from secondary adapter warnings.
   - For a generic failed-reply notice, correlate the reported platform, local time, channel, and user with the exact `Agent error in session` entry in the gateway log. Read the originating traceback before changing permissions, models, or session state; a live gateway can still fail when constructing a fresh agent.
   - For alternating stdio-wrapper recursion, follow `references/stdio-wrapper-recursion.md` before restarting; a restart clears accumulated wrappers but does not prevent recurrence.

3. Check whether the installed service targets the active Hermes installation.
   - Compare `systemctl cat hermes-gateway` with `command -v hermes` and `readlink -f "$(command -v hermes)"`.
   - Never assume `hermes pm repair` rewrites systemd: it repairs the recorded dependency environment, while an existing unit may still reference an obsolete install path.

4. Repair only the broken layer.
   - Dependency environment: run `hermes pm repair`.
   - Stale system service target: reinstall with `hermes gateway install --force --system --run-as-user <existing-service-user> --start-now`.
   - Preserve the existing service scope and user unless the user explicitly requests a migration; changing user/system scope can change credential and profile access.

5. Verify recovery after a short stability window.
   - Confirm the unit is `active` and `enabled`, `ExecMainStatus=0`, and `Result=success`.
   - Record the PID and `NRestarts`, wait briefly, then confirm the PID remains present and `NRestarts` does not increase.
   - Run `hermes gateway status --system` as the product-level readback.

6. Test subsystem readiness, not just process liveness.
   - Inspect startup logs for each configured messaging adapter, MCP server, and cron worker.
   - For PM-managed installs, verify restart-safe cron workers use the committed dependency venv interpreter, not the bare store Python. A gateway can import `ruamel` while external workers still fail before acknowledgement with `ModuleNotFoundError`; reproduce with a real scheduled monitor run, not only an in-process cron command.
   - Classify the result as `HEALTHY`, `DEGRADED`, or `DOWN`: a running systemd unit is only `HEALTHY` when required subsystems also start; it is `DEGRADED` when the gateway serves some platforms while others are parked or failing.

## Reporting

Report three compact blocks:
- Core service: active/enabled, stable PID/restart count.
- Connected/working subsystems.
- Failed or degraded subsystems with the exact actionable cause.

Do not call the gateway fixed merely because systemd says `active`; Hermes can deliberately remain running while configured adapters or workers are unavailable. Report code-test success, adapter reconnection, and a real user-message round trip as separate verification levels; if the last is pending, say so explicitly. Compare post-restart errors only within the new process's startup window, and establish a new restart-count baseline after an intentional restart.

For a deeper command checklist and state interpretation, read `references/gateway-health.md`.
