# Next.js + Coolify + Supabase capacity notes

Load this reference only when the audited stack uses these components.

## Next.js self-hosting

Verify whether the deployment is one `next-server` process or multiple replicas. A large multi-core host does not make one JavaScript process use every core for request work.

For multiple instances, require all of the following before adding replicas:

- identical image/build output;
- stable `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` shared by instances;
- `deploymentId` or another version-skew strategy;
- shared cache/tag invalidation when cross-request Next caching is used;
- stateless sessions/uploads and shared object storage;
- health checks and graceful SIGTERM drain.

Dynamic authenticated HTML is private and should not be edge-cached. Cache hashed JS/CSS and public media aggressively; keep user-specific HTML/API bypassed.

## Coolify

`docker ps` labels identify the active application, domain, image tag, and project. Confirm the image tag against the intended Git commit before testing.

One application container behind Traefik is one failure and saturation domain. Coolify can deploy one image to multiple servers, but an external/cloud load balancer still owns public traffic distribution and health removal. Keep the Coolify control plane away from launch traffic when practical.

Inspect limits with:

```bash
docker inspect <container> --format '{{json .HostConfig}}'
docker exec <container> sh -c 'cat /proc/1/limits; cat /sys/fs/cgroup/cpu.max; cat /sys/fs/cgroup/memory.max; cat /sys/fs/cgroup/pids.max'
```

Set explicit CPU/memory reservations and limits only after measuring normal and peak usage. Limits protect the host; undersized limits manufacture outages.

## Supabase

Treat PostgREST/Auth edge latency and Postgres execution time as separate metrics. A fast function can still have high user latency from network, gateway, Auth, and queueing.

Read-only audit queries should cover:

```sql
select pg_database_size(current_database()),
       (select setting::int from pg_settings where name='max_connections');
select state,wait_event_type,wait_event,count(*)
from pg_stat_activity group by 1,2,3;
select relname,n_live_tup,n_dead_tup,seq_scan,idx_scan,
       pg_total_relation_size(relid)
from pg_stat_user_tables order by pg_total_relation_size(relid) desc;
```

Use `pg_stat_statements` for hot RPCs and Supabase unified edge logs for request count, status, and `response.origin_time`. Never print IPs, JWT fields, emails, user IDs, or URLs containing identifiers from raw logs; aggregate in SQL before returning results.

Before increasing compute, fix query and policy issues proven by plans/advisors:

- indexes on leading filter/join/FK columns;
- `(select auth.uid())` / `(select auth.jwt())` init plans when row-independent;
- bounded pagination and indexed ordering;
- avoid whole-table counts/aggregations on every feed request at large scale;
- cache shared, non-user-specific CMS/forum summaries where correctness permits.

A 60-connection database is Nano/Micro-class by current Supabase defaults. Do not declare a required upgrade tier from that fact alone: run the authenticated staging mix, watch CPU/IO/connection queues, then resize. Verify Auth token/IP rate limits separately for launch/login bursts.

## Media and CDN

Measure the actual request waterfall, not only `public/` directory size. Still flag very large first-view videos and images because 10,000 cold clients multiply origin egress immediately.

When a staging Basic Auth gate marks every response `private, no-store`, CDN bypass is expected and staging throughput understates a production CDN hit path. For production, prove cache status on media extensions and keep the gate away from public cacheable assets only if the assets are safe to expose.
