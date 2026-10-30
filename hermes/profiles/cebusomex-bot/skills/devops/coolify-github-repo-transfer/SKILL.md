---
name: coolify-github-repo-transfer
description: Use when a GitHub repo transfer breaks Coolify deploys.
---

# Coolify GitHub Repository Transfer Recovery

## When to use

Use after transferring a private GitHub repository when Coolify fails before build with `Repository not found` or still clones the old owner path.

## Safety boundaries

- Confirm the old deployment remains healthy before changing source authentication.
- Never print or copy private-key material. Public-key fingerprints are safe for comparison.
- Ask before deleting/re-registering a deploy key or editing Coolify state.
- Keep deploy keys read-only unless a verified workflow requires writes.
- Prefer supported UI/API changes. If the installed Coolify version exposes no source editor, update only the exact `applications.git_repository` row with a guarded predicate and immediate read-back.
- Do not alter unrelated build, environment, domain, or deployment settings.

## Diagnose

1. Read the failed clone command and capture the repository path, branch, and key identifier.
2. Verify the canonical repository exists and note the transferred owner/name.
3. Read Coolify's application row: `uuid`, `git_repository`, `git_branch`, and `private_key_id`.
4. Map `private_key_id` to the Coolify private-key UUID without printing key content.
5. Derive the public-key fingerprint with `ssh-keygen -y` piped to `ssh-keygen -lf -`.
6. Compare it with GitHub's registered deploy-key fingerprint.
7. Test the canonical SSH URL using the exact Coolify key and `git ls-remote ... refs/heads/<branch>`.

## New-organization deploy-key pitfall

New GitHub organizations disable deploy-key creation by default. A repair attempt then returns:

```text
422 — Deploy keys are disabled for this repository
```

Have an organization owner open:

```text
Organization Settings → Member privileges → Deploy keys
```

Select **Enabled** and save. This is an organization policy, not a paid branch-protection feature.

## Repair

1. If a transferred deploy key is listed but authenticates without repository read access, re-register the same public key to refresh the stale association:
   - remove the stale repository deploy key only after approval;
   - add the same public key back;
   - set `read_only=true`;
   - verify the returned key is `verified=true`.
2. Run `git ls-remote` against the canonical SSH URL. Do not continue until it returns the expected branch commit.
3. Update Coolify to the canonical `OWNER/REPO.git` value. Guard the update with both the application UUID and exact old repository value so the wrong row cannot change.
4. Read the row back and verify repository and branch.

## Redeploy and verify

1. Trigger a normal deployment; a cache bypass is unnecessary for clone failures.
2. Capture the deployment UUID.
3. Wait for terminal status (`finished` or failure); do not claim success while `queued` or `in_progress`.
4. Verify:
   - deployment status is `finished`;
   - deployed commit matches the expected branch head;
   - application status is `running:healthy`;
   - Coolify stores the canonical repository path;
   - GitHub lists the deploy key as verified and read-only;
   - the public endpoint responds as expected. A staging endpoint protected by Basic Auth may correctly return `401` with `WWW-Authenticate`.

## Failure recovery

- If deploy-key registration fails, stop before updating Coolify's repository path.
- If the path update succeeds but deployment fails, keep the previous healthy container running and inspect the new deployment log.
- If a guarded database update changes zero rows, re-read current state instead of broadening the predicate blindly.
- If the repository uses a GitHub App rather than a deploy key, grant the app access to the transferred repository and use Coolify's source-switch workflow instead.
