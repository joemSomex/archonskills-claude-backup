# Gateway Health Checklist

## Fast diagnosis

```bash
hermes status
systemctl status hermes-gateway --no-pager --full
systemctl show hermes-gateway \
  -p LoadState -p ActiveState -p SubState -p UnitFileState \
  -p Result -p ExecMainStatus -p MainPID -p NRestarts
journalctl -u hermes-gateway --no-pager --since '15 minutes ago' -n 200
```

Interpretation:

| Service evidence | Verdict | Next action |
|---|---|---|
| `inactive` and no restart policy activity | Stopped | Determine whether stopping was intentional, then start if requested. |
| `activating` + `auto-restart`, increasing `NRestarts` | Crash loop | Diagnose the first startup error from the journal. |
| `active (running)` + stable PID/restart count | Core process passes | Continue to adapter, MCP, and cron checks. |
| `active (running)` + parked/failed configured components | Degraded | Report the core as running and each failed subsystem separately. |

## Detect an obsolete unit target

```bash
systemctl cat hermes-gateway
command -v hermes
readlink -f "$(command -v hermes)"
```

If `ExecStart` belongs to a different or missing install tree, repairing the current dependency environment is insufficient. Reinstall the service using the same scope and account as the existing unit:

```bash
hermes gateway install --force --system --run-as-user <service-user> --start-now
```

Do not copy `root` blindly from an example. Preserve the current service account so `$HOME`, `HERMES_HOME`, credentials, profiles, and file permissions remain consistent.

## Dependency repair sequence

```bash
hermes pm repair
hermes gateway restart
```

After repair, re-check the unit target. If it still points to an obsolete install, reinstall the service rather than repeatedly restarting it.

## Stability verification

Capture these values twice with a short interval:

```bash
systemctl show hermes-gateway \
  -p ActiveState -p SubState -p Result -p ExecMainStatus \
  -p MainPID -p NRestarts
```

Pass conditions:
- `ActiveState=active`
- `SubState=running`
- `Result=success`
- `ExecMainStatus=0`
- `MainPID` is nonzero and stable
- `NRestarts` does not increase during the check

Then run:

```bash
hermes gateway status --system
journalctl -u hermes-gateway --no-pager --since '<restart time>' -n 200
```

Look for explicit connection/startup outcomes for configured messaging platforms, MCP servers, cron workers, and schedulers. Process liveness alone does not prove end-to-end gateway health.
