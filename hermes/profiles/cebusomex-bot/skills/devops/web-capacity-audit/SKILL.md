---
name: web-capacity-audit
description: "Use when auditing whether a web stack handles target load."
version: 0.1.0
---

# Web Capacity Audit

Audit a deployed web system end to end, turn “N concurrent users” into a measurable workload, run only authorized load, and write a decision-ready Markdown report.

## Always-on rules

- Separate **connected/idle users**, **active users**, and **simultaneous requests**. Convert the target into request-rate scenarios before judging capacity; concurrency alone is not a load model.
- Never blast production because the user asked whether it can scale. Default to read-only production inspection plus a controlled local/staging ramp. Require an explicit production window, target rate, duration, abort thresholds, and rollback owner before production load.
- Audit edge/CDN, reverse proxy, application processes/replicas, host resources, database/pooler, Auth, storage, and third-party calls independently. One healthy layer does not prove the system.
- Report **measured**, **derived**, and **unknown** facts separately. A clean short test on unauthenticated pages does not prove authenticated forum capacity.
- Write the final artifact under `docs/` unless the user names another location. Lead with a plain verdict, evidence, limitations, then a numbered P0/P1/P2 plan and a repeatable load-test runbook.
- Do not mutate infrastructure, database settings, CDN rules, or production data during an audit without separate approval.

## Procedure

### 1. Lock the workload contract

Ask only what cannot be discovered: target environment, user journey, and whether live load is authorized. Define at least three scenarios:

```text
10,000 users × one request / 60 s = 167 RPS
10,000 users × one request / 30 s = 333 RPS
10,000 users × one request / 10 s = 1,000 RPS
```

Use a calculation tool, not mental arithmetic. Include write mix, login burst, media downloads, think time, test duration, geographic source, and SLOs such as error rate and p95 latency.

### 2. Inventory every serving layer

Capture live evidence before testing:

```bash
nproc; lscpu; free -h; df -h /; uptime
ulimit -n
sysctl fs.file-max net.core.somaxconn net.ipv4.ip_local_port_range
docker ps --format '{{json .}}'
docker stats --no-stream --format '{{json .}}'
docker inspect <app-container> --format '{{json .HostConfig}}'
```

Record replica count, app process count, CPU/memory/PID limits, restart policy, file-descriptor limits, health checks, proxy/CDN, and whether the control plane shares the application host. Inspect response headers and DNS to prove CDN/cache behavior rather than assuming it.

For Docker, treat `Memory=0`/`NanoCpus=0` as **unbounded**, not generously provisioned: one container can starve the host. See `references/nextjs-coolify-supabase.md` for this user’s common stack.

### 3. Trace the expensive user journey

Read route/layout/server-action/data-access code. Count external waves per page, including Auth, role/profile, progress, feed, media signing, and cache misses. Identify which calls run in parallel and which repeat per request.

Measure static payloads programmatically and list the largest first-load assets. A large media library is not itself the page payload, so distinguish total repository bytes from assets actually requested by one journey.

### 4. Inspect the data platform read-only

Use the provider’s own tools. For Postgres/Supabase collect:

- database size, `max_connections`, active/idle connections, deadlocks, temp bytes;
- `pg_stat_statements` calls, mean/p95-equivalent evidence, and total time for hot RPCs;
- top tables by size, live/dead tuples, sequential/index scans;
- indexes supporting forum ordering, pagination, foreign keys, and RLS filters;
- provider performance advisors and 24-hour API latency/error/peak-rate logs.

Do not call idle `ClientRead` waits “blocked connections.” Group `pg_stat_activity` by state and wait event first. Prefer provider edge-origin latency for user-facing evidence and database execution time for query-tuning evidence; they measure different layers.

### 5. Run a controlled ramp

Use `scripts/http-load.mjs` or k6 from a **separate generator host/container** when possible. The generator must not compete with the target for CPU or memory. If it runs inside the target container, label the result a smoke test/lower-confidence bound.

Start with one cheap route and one representative dynamic route:

```bash
node scripts/http-load.mjs https://staging.example.com / 10 5000
node scripts/http-load.mjs https://staging.example.com /forum 10 5000
# then 50, 100, 200 only while errors and latency remain inside abort thresholds
```

Use existing environment-injected Basic Auth without printing credentials. Ramp gradually, stop on elevated errors, health-check failure, DB saturation, or runaway latency, and sample CPU/memory/connections during each stage.

For the release gate, use k6 constant/ramping arrival rate with realistic authenticated accounts and a write-safe dataset. Set explicit thresholds, for example error rate `<1%` and route-specific p95/p99 budgets. Test login, forum feed, thread detail, publish, vote, and media as separate scenarios before a mixed journey.

### 6. Interpret honestly

- Throughput that plateaus while p95 rises is saturation even when errors remain zero.
- A 10-second smoke test proves only that tested range; it does not establish soak stability, autoscaling, or 10,000-user readiness.
- Compare required RPS with sustained measured RPS, not the single best sample.
- Include bandwidth math for simultaneous first loads. CDN cache hits and HTML/API requests are separate capacity problems.
- State the largest unknowns: authenticated fan-out, database plan/quotas, network uplink, cache-hit ratio, write contention, and geographic latency.

### 7. Recommend in dependency order

Typical order:

1. **P0 edge and safety:** CDN/object storage for media, cache verification, rate limits/WAF, resource limits, observability, and a representative staging test.
2. **P0 database:** fix measured hot queries/RLS/index warnings, size compute/pooler from tests, and verify Auth limits for launch bursts.
3. **P1 application scale:** multiple identical app instances, external load balancer, stable Server Action encryption key, deployment/version ID, shared cache/tag invalidation, and graceful draining.
4. **P1 resilience:** move app workloads off the Coolify control-plane host or add a second server; prove failover.
5. **P2 continuous performance:** retain k6 scripts, baselines, dashboards, alerts, and pre-event rehearsal.

Do not prescribe a final instance count from one smoke test. State a starting topology and require the staged test to confirm or revise it.

### 8. Produce and verify the report

Use citations for external platform behavior; local measurements need command/method attribution, not web citations. The report must include:

- verdict and confidence;
- current architecture and bottlenecks;
- measured server/database/load-test tables;
- target workload model;
- P0/P1/P2 enhancements with owner, acceptance test, and rollback;
- staged runbook from baseline to 10,000-user rehearsal;
- cost-sensitive options and unknowns;
- sources.

Verify cited URLs mechanically when using the grounded-citations ledger. Re-read the completed Markdown file and check that every claimed total matches the enumerated evidence.

## Verification checklist

- [ ] Target users were converted into RPS/write/media scenarios.
- [ ] Host and container state came from the live environment.
- [ ] Replica/process/resource-limit state was verified.
- [ ] App request fan-out and static payloads were inspected.
- [ ] Database/pooler/Auth evidence was collected read-only.
- [ ] Controlled load stayed within the authorized environment and ramp.
- [ ] Authenticated coverage and other limitations are explicit.
- [ ] Recommendations are ordered and testable.
- [ ] The Markdown report exists, was re-read, and citations verify.

## Supporting files

- `references/nextjs-coolify-supabase.md` — stack-specific probes and scaling decisions.
- `scripts/http-load.mjs` — deterministic HTTP concurrency smoke test that never prints credentials.
