---
name: aws-container-deployment
description: "Use when deploying containerized web apps on AWS ECS."
version: 0.1.0
metadata:
  hermes:
    tags: [aws, ecs, fargate, alb, cloudfront, s3, deployment]
    category: devops
---

# AWS Container Deployment

Deploy a containerized web application to ECS Fargate behind an Application Load Balancer, with CloudFront/S3 for static content, least-privilege delivery, staged verification, and an explicit cost gate.

## Always-on rules

- Treat provisioning as a paid external write. Produce and review a cost estimate before creating NAT Gateways, ALBs, always-on tasks, WAF, ElastiCache, or paid DNS resources.
- Preserve the existing deployment as rollback until AWS has passed functional, load, failure, and observation-window gates. A successful ECS rollout is not authorization to delete the old platform.
- Never ask for or expose passwords, access keys, API secrets, webhook secrets, account recovery codes, or MFA codes. Use GitHub OIDC for CI and Secrets Manager/SSM references for runtime secrets.
- Build one immutable image per commit and deploy that exact image to every task. Never rely on mutable `latest` for rollback or evidence.
- Put public static/media bytes on S3 plus CloudFront; keep personalized HTML, Server Actions, and member-specific APIs uncached.
- Keep state outside the task filesystem. Sessions, uploads, queues, and shared caches must be reachable by every task before horizontal scaling.
- Do not migrate the database/Auth/storage platform in the same change unless the user explicitly approves a platform migration. First scale the web tier around the existing contracts.
- Report four states separately: repository readiness, AWS infrastructure, deployed revision, and live application verification.

## Procedure

### 1. Lock the deployment contract

Discover the Dockerfile, listening port, health behavior, build-time versus runtime variables, external database/Auth/storage, current DNS/CDN, target region, hostnames, rollback deployment, and expected load. Ask only for missing decisions.

Require explicit answers for:

- staging and production hostnames;
- primary DNS/CDN (CloudFront or another CDN, never an accidental double proxy);
- monthly budget and alert thresholds;
- region (normally close to the database, while the CDN serves users globally);
- deployment branch/environment and sole merger/approver policy.

### 2. Prepare the application before infrastructure

Add a lightweight unauthenticated `/api/health` or equivalent that proves process readiness without performing every downstream call. Do not use a Basic-Auth-protected landing page as the ALB health path.

Verify graceful SIGTERM handling, immutable build identity, runtime configuration, and stateless filesystem behavior. For multi-instance Next.js, follow `references/nextjs-multi-instance.md` before creating the service.

### 3. Design and approve cost

Estimate at least ALB, NAT/egress, minimum Fargate tasks, CloudFront, S3, WAF, logs/metrics, secret storage, and optional Redis. Use staging cost controls:

- two minimum tasks;
- one NAT only when reduced staging availability is accepted;
- short log retention;
- no Redis until shared-cache semantics require it;
- budget alerts before provisioning.

Never quote a final monthly amount from memory; use the live AWS Pricing Calculator for the chosen region and traffic model.

### 4. Build the network boundary

Create one VPC across at least two Availability Zones:

- public subnets for ALB and NAT;
- private subnets for Fargate tasks;
- Internet Gateway and explicit route tables;
- ALB security group accepting viewer HTTPS;
- task security group accepting the application port from the ALB security group only.

Use target type `ip` for Fargate. Disable public task IPs in the production design. Make outbound access explicit; use NAT or the required VPC endpoints, not accidental public exposure.

### 5. Create IAM and secret boundaries

Create separate least-privilege roles:

- task execution role for ECR pulls, CloudWatch logs, and named secret references;
- task role for only the AWS APIs the application calls;
- GitHub OIDC deployment role restricted to repository, branch/environment, ECR repository, ECS service, and deployment-status reads.

Store server secrets in Secrets Manager or SSM and reference ARNs from the task definition. Keep public build-time variables separate from runtime secrets. Never paste plaintext into task-definition JSON or CI logs.

### 6. Build immutable delivery

Create an ECR repository with image scanning and retention. CI must:

1. run repository gates;
2. authenticate with OIDC;
3. build once with approved build-time public values;
4. tag with the commit SHA;
5. push to ECR;
6. register a task-definition revision;
7. update ECS;
8. wait for service stability;
9. verify health and one real user path.

Database migrations remain a separately approved operation unless the deployment contract explicitly says otherwise.

### 7. Create ALB and ECS service

Create an IP target group on the application port with the dedicated health path. Create an internet-facing ALB across public subnets and redirect HTTP to HTTPS.

Create the Fargate service across private subnets in at least two zones. Start staging with two tasks. Enable deployment circuit breaker and rollback. Set CPU/memory explicitly and configure a drain period long enough for in-flight requests.

Do not enable aggressive autoscaling before setting database/pool budgets; web replicas can amplify downstream overload.

### 8. Separate media with CloudFront/S3

Create a private, encrypted, versioned S3 bucket. Grant CloudFront access through Origin Access Control rather than public bucket permissions.

Use path behaviors:

- versioned images/video/static media → S3 with long TTL;
- immutable framework assets → S3 or ALB with immutable caching;
- default dynamic/private behavior → ALB with caching disabled and only required cookies/headers/query strings forwarded.

Warm and verify cache hits. Verify personalized responses never become shared hits. Move only public media; keep private uploads in their existing protected store until separately migrated.

### 9. Add protection and observability

Attach WAF in count mode first, then enforce after false-positive review. Add alarms for unhealthy targets, task count, deployment failure, ALB 5xx/latency, task CPU/memory, restarts, and cost anomalies. Add application metrics for event-loop delay, queue depth, p95/p99, and downstream latency.

Configure target-tracking autoscaling only after a controlled load test establishes requests-per-task and downstream headroom. Keep minimum capacity high enough to avoid cold-start failure during launch events.

### 10. Verify before cutover

Require all of:

- tasks healthy across zones;
- one-task termination causes no outage;
- Server Actions work across tasks;
- static cache hits and private cache misses are correct;
- Auth callbacks and webhooks reach the intended host;
- rollback triggers on a deliberately unhealthy revision;
- external arrival-rate load meets correctness, latency, resource, and pool thresholds;
- secrets absent from logs and API responses.

Lower DNS TTL in advance, cut over gradually, and retain the old deployment through the observation window. Read back the running task-definition/image digest and DNS/CDN state before claiming completion.

## Common pitfalls

- **Do not lift-and-shift to one EC2 instance and call it scaling.** It preserves the single-host/process failure domain and adds AWS operations without horizontal capacity.
- **Do not put Fargate tasks in public subnets with public IPs for convenience.** The ALB should be the inbound boundary; private tasks reduce exposure.
- **Do not use the landing page as a health check when it needs Auth or external APIs.** A transient dependency or credential issue will churn every target.
- **Do not combine Cloudflare proxying and CloudFront accidentally.** Double CDNs complicate client IP forwarding, cache keys, invalidation, TLS, and incident diagnosis.
- **Do not autoscale the app independently of database limits.** More tasks can turn a slow downstream into connection-pool exhaustion.
- **Do not regenerate multi-instance framework keys per task.** Requests can land on another task and fail to decrypt actions or find the expected deployment.

## Verification checklist

- [ ] Cost and budget approved before paid resources.
- [ ] Health endpoint exists and is independent of member credentials.
- [ ] Tasks are private; ALB is the inbound boundary.
- [ ] Image is immutable and traceable to a commit.
- [ ] CI uses OIDC, not long-lived AWS keys.
- [ ] Runtime secrets are ARN references, not plaintext.
- [ ] At least two tasks and two zones are healthy.
- [ ] Circuit-breaker rollback was exercised.
- [ ] Static media is edge-cached; personalized content is not.
- [ ] Load test proves the target rate with downstream headroom.
- [ ] Old deployment remains available until cutover is verified.
