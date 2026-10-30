---
name: coolify-deployment-operations
description: Use when automating or verifying Coolify deployments.
version: 1.0.0
author: Hermes Agent
license: Proprietary
metadata:
  hermes:
    tags: [coolify, deployment, github, webhooks, ci-cd]
    related_skills: [coolify-github-repo-transfer, galatea-archon]
---

# Coolify Deployment Operations

Automate and verify Coolify deployments without confusing a configured source, an accepted trigger, a successful build, and the revision actually serving traffic.

## When to Use

Use when configuring merge-to-deploy automation, choosing between Git-provider webhooks and the Coolify API, diagnosing stale deployments, integrating an orchestrator such as Archon or CI, or proving which revision is live. Use the repository-transfer recovery skill for source ownership and deploy-key repairs.

## Procedure

1. **Identify the deployment policy before changing anything.** Record the application UUID, environment, canonical repository, deploy branch, current branch head, and currently running revision. Use push-triggered deployment for staging; use an explicit approval gate before production promotion unless the user has chosen continuous production deployment.
2. **Inspect the source and auto-deploy state independently.** Read the application repository/branch and `application_settings.is_auto_deploy_enabled` through the supported UI/API. On a self-hosted instance where those are unavailable, use read-only PostgreSQL queries scoped to the application UUID; never print webhook secrets, private keys, environment values, or tokens.
3. **Verify the upstream event path.** For a manually connected GitHub repository, inspect repository hooks with `gh api repos/OWNER/REPO/hooks` and report only safe metadata such as hook ID, active state, events, content type, and update time. For a GitHub App source, verify that the app installation includes the repository and receives push events. A stored webhook secret or `Auto Deploy=true` does not prove GitHub has a live hook; all three pieces—source, switch, and event delivery—must exist.
4. **Choose one deployment trigger.** Prefer a Git-provider push webhook for automatic staging deployment after merges to the configured branch. Prefer the Coolify API or deploy webhook when a workflow must hold an approval gate or select an exact revision. Never let both GitHub and an orchestration workflow trigger the same merge, because duplicate events create competing builds and ambiguous status.
5. **Keep orchestration responsibilities explicit.** If GitHub triggers Coolify, Archon or CI should observe the merge, wait for Coolify, verify health and revision, and notify; it should not deploy again. If Archon or CI triggers Coolify, store the credential in the platform secret store, invoke the authenticated endpoint only after the merge/approval gate, and make that workflow the sole trigger.
6. **Verify deployment as a state transition.** Capture the expected full commit SHA, wait for a terminal Coolify deployment state, then verify application health and the revision reported by the running service. Prefer a build-identity endpoint such as `/api/build-id`; otherwise compare the immutable running image tag or label with the remote branch head. A successful webhook response or build exit code alone is not deployment proof.
7. **Report layer-specific results.** State separately: merge SHA, trigger delivery, Coolify deployment status, health result, observed running SHA, and whether observed equals expected. Never collapse these into “deployed” when one layer is unknown.

## Safe read-only probes

```bash
# Canonical branch head
git ls-remote https://github.com/OWNER/REPO.git refs/heads/main

# Safe GitHub hook metadata; do not print hook URLs or secrets
gh api repos/OWNER/REPO/hooks \
  --jq '[.[] | {id,active,events,content_type:.config.content_type,updated_at}]'

# Self-hosted Coolify fallback: source and branch
docker exec coolify-db psql -U coolify -d coolify -P pager=off -c \
  "select uuid,name,git_repository,git_branch,git_commit_sha from applications where uuid='<APP_UUID>';"

# Self-hosted Coolify fallback: auto-deploy switch
docker exec coolify-db psql -U coolify -d coolify -P pager=off -c \
  "select a.uuid,s.is_auto_deploy_enabled from applications a join application_settings s on s.application_id=a.id where a.uuid='<APP_UUID>';"
```

## Safety and failure recovery

- Ask before adding or changing repository hooks, GitHub App grants, Coolify deployment settings, production gates, or external secrets; these are state-changing external operations.
- Keep existing healthy containers serving while a new deployment builds. A failed candidate must not be described as an outage unless traffic actually moved or health degraded.
- If GitHub shows no repository hook for a manual source, do not infer automatic deployment from a recent matching container; it may have been deployed manually.
- If the running revision differs from the expected branch head, inspect trigger delivery and deployment history before changing application code or databases; stale deployment frequently masquerades as a product regression.
- Do not store deploy URLs, webhook secrets, API tokens, or credentials in repository workflow YAML, Archon inputs, logs, chat, or skills. Reference secret names only.
