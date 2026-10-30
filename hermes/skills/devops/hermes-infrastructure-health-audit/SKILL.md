---
name: hermes-infrastructure-health-audit
description: "Use when auditing Hermes stack health. Verify each layer."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, diagnostics, gateway, gbrain, postgresql, mcp, cron]
---

# Hermes infrastructure health audit

## When to Use

Use for end-to-end health checks of a Hermes installation, especially when the request names several layers such as the launcher, updater, gateway, messaging adapters, scheduled jobs, GBrain, PostgreSQL, MCP discovery, or recall.

Audit the stack as independent layers. Never infer that “service running” means the launcher, updater, adapters, cron workers, MCP, database, and recall path are all healthy.

## Procedure

### 1. Establish scope and audit trail

1. Resolve the active profile and Hermes home rather than assuming `~/.hermes`.
2. For an administrator operating under a notification policy, send the required start alert and append a local audit entry before diagnostics.
3. Keep the audit read-only unless the user explicitly asks for repairs. Do not upgrade GBrain, change credentials, delete rollback stores, pair messaging accounts, or apply database migrations during a health check.

### 2. Verify the launcher and installation identity

Run:

```bash
hermes --version
hermes --help
command -v hermes
hermes doctor
```

If multiple launchers or installs exist, inspect each resolved launcher and compare its reported install directory and revision. Treat divergent install roots as a finding even when both commands start, because subprocesses and services may resolve a different runtime than the interactive shell.

### 3. Verify the updater without installing

Run both:

```bash
hermes update --check
hermes update --plan
```

Also compare the checkout directly when it is a Git install:

```bash
git rev-parse HEAD
git rev-parse origin/main
git status --short --branch
```

Report “up to date” only when the updater and revision comparison agree. A pending formatting-only commit is still an available update, but it is not evidence that an unrelated runtime defect is fixed.

### 4. Verify gateway process and every adapter

Run:

```bash
hermes gateway status
hermes status
systemctl status hermes-gateway.service --no-pager --full
journalctl -u hermes-gateway.service --since '15 minutes ago' --no-pager
```

Classify the gateway separately as:

- **healthy** — service active and all configured adapters serving;
- **degraded** — core process active while one or more configured adapters are parked, unpaired, rate-limited, or repeatedly failing;
- **down** — supervisor or gateway process inactive.

Do not collapse a degraded gateway into “working.” Name which platforms are operational and which require human pairing, upstream recovery, or configuration.

### 5. Verify cron across every served profile

For the default profile and every profile named by `hermes status`, run:

```bash
hermes cron status
hermes cron list
hermes cron doctor
hermes cron incidents
hermes cron runs --limit 10
hermes -p <profile> cron status
hermes -p <profile> cron list
```

**Pitfall:** Never accept `cron doctor` alone as proof of execution health; it can validate job definitions while restart-safe workers are failing. Inspect recent runs, unresolved incidents, and the last result of each active job in every served profile.

When a worker fails before ownership acknowledgement, inspect the captured traceback and distinguish:

- scheduler/ticker liveness;
- job-definition validity;
- external-worker runtime/import health;
- the job script or agent’s own failure.

These are separate failure domains and need separate conclusions.

### 6. Verify GBrain, PostgreSQL, and MCP independently

Run the engine and database checks:

```bash
<gbrain-launcher> engine status --json --probe
<gbrain-launcher> doctor --json
<gbrain-launcher> stats
```

For a local PostgreSQL proxy, verify all three:

1. container/process is running and restart count is stable;
2. TCP listener accepts a connection;
3. GBrain’s authenticated engine probe succeeds.

A listening TCP port alone does not prove that the database behind the proxy accepts GBrain queries.

Verify Hermes MCP discovery:

```bash
hermes mcp test gbrain
hermes mcp list
```

Then run a real bounded recall through **both** paths:

```bash
<gbrain-launcher> call recall '{"query":"<known indexed topic>","budget_tokens":600,"limit":5}'
```

and the native GBrain MCP `recall` tool with the same query. Require structured results or known facts, not merely successful tool discovery.

**Pitfall:** Do not equate a low GBrain doctor score with recall outage. Report core availability separately from optional quality features such as embeddings, graph coverage, maintenance cycles, or skill-pack currency. Conversely, a successful recall does not clear schema, provider, or maintenance warnings.

### 7. Recheck current state before reporting

Repeat the cheapest authoritative probes after diagnostics:

- gateway active/enabled state;
- updater check and Git revision;
- PostgreSQL engine probe;
- MCP test;
- real recall;
- recent gateway errors;
- latest active cron-job results.

This avoids reporting a transient earlier snapshot as current state.

### 8. Report by component

Use three sections:

1. **Working** — only independently verified components.
2. **Still broken or incomplete** — exact layer, evidence, and operational impact.
3. **Changes made** — state explicitly when the audit was read-only.

Avoid saying “everything is fixed” unless every named layer passed. Send the required completion alert and append the completion audit record with a concise component matrix.
