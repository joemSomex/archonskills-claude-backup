# Next.js multi-instance requirements

Load this reference when the ECS service will run more than one Next.js task.

## Build once

Build one image and deploy its digest to every task in the service. Rebuilding per task can produce incompatible Server Action IDs, asset sets, or build identifiers.

## Shared Server Action encryption key

Set one stable `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` for every task in an environment. Generate it once, store it as a runtime/build secret according to the Next.js version's build contract, and rotate through a planned deployment. A different key per task causes cross-task Server Action failures.

## Deployment identity

Set a deployment/build identifier from the commit SHA so clients and servers can detect version skew during rolling deployments. Keep old hashed assets available long enough for clients still carrying the previous deployment.

## Cache coordination

Next.js filesystem and in-memory caches are per task by default. Before relying on cache tags or on-demand revalidation across replicas:

- disable per-instance memory caching where required;
- use a shared durable cache handler (commonly Redis or another approved store);
- coordinate tag/path invalidations across tasks;
- test that a mutation routed to task A is visible when the next read reaches task B.

Do not add Redis merely because there are multiple tasks. Add it when an actual cross-request cache is used and its invalidation semantics are defined.

## Static assets and media

Serve immutable framework assets and large public media through CloudFront/S3. Keep member-specific HTML and API responses uncached. Use content-hashed filenames for long TTLs; stable filenames require shorter TTLs and deliberate invalidation.

## Health and draining

Use a cheap process readiness endpoint for the ALB. It must not require Basic Auth or run every database/Auth dependency. During deployment, stop accepting new traffic before process exit and allow in-flight requests and `after()` work to finish.

## Verification

- Send sequential Server Actions while forcing requests across different tasks.
- Revalidate cached content through one task and read it through another.
- Terminate one task during traffic and require no failed user flow.
- Roll from one deployment ID to another while an old client remains open.
- Confirm CloudFront never caches authenticated HTML or action responses.
