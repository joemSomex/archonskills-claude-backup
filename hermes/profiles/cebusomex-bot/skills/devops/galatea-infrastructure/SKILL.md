---
name: galatea-infrastructure
description: Use when planning Galatea hosting, AWS, CDN, or media.
---

# Galatea infrastructure decisions

## Approved architecture

- Keep the Next.js application, Traefik, and deployment workflow on Coolify on the Hostinger VPS.
- Use AWS only for public file and video delivery through a private S3 bucket and CloudFront.
- Do not provision ECS, Fargate, ALB, ECR, or NAT Gateway unless Joshua explicitly changes the architecture.
- Keep Supabase Auth, PostgreSQL, private Storage, RLS, and signed member media unchanged.
- Prefer `assets.galatea.systems` as the dedicated CloudFront hostname so authenticated HTML, cookies, Server Actions, and forum responses never enter the asset cache.

## Implementation rules

1. Read `/root/galatea-system-stagin/docs/AWS_S3_CLOUDFRONT_MEDIA_DELIVERY.md` before advising or implementing the media migration.
2. Start on staging, confirm AWS budget/cost approval, then create a private versioned S3 bucket with Block Public Access and CloudFront Origin Access Control.
3. Preserve the repository's cache semantics: stable asset names cache for one day with stale-while-revalidate; content-hashed `/media/` names cache immutable for one year.
4. Use GitHub Actions OIDC for automated uploads; never store long-lived AWS keys in GitHub, the repository, chat, or screenshots.
5. Keep original `public/` assets during the first rollback window. Do not use `aws s3 sync --delete` in the initial migration.
6. Verify content types, CORS, video range requests, CloudFront cache hits, direct-S3 denial, browser behavior, and reduced VPS media bandwidth before claiming success.
7. Do not claim this media offload raises dynamic forum or database capacity without a controlled post-change load test.

## Safety boundary

AWS provisioning and paid-resource changes require cost approval. DNS cutover, production activation, or deletion of AWS objects/distributions requires explicit confirmation. Hosted Supabase changes remain separately approval-gated.
