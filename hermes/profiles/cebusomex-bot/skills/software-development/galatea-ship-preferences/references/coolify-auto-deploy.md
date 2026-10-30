# Coolify automatic deployment for Galatea staging

## Choose the trigger

Use the GitHub push webhook for staging: a merge into `main` emits a push, Coolify filters to its configured deploy branch, and one deployment starts. Do not also call the Coolify deployment API from Archon, because two independent triggers can build the same revision twice.

Reserve an authenticated API-triggered deployment for an explicitly gated production promotion or a requested manual redeploy. Archon owns PR preparation and post-merge verification; Joshua remains the merger.

## Preflight without exposing secrets

1. Read the Coolify application branch and auto-deploy flag. Confirm the branch is `main` and Auto Deploy is enabled.
2. Identify the source connection. A manual/private Git source needs a repository webhook even when Coolify already stores manual webhook secrets.
3. Check GitHub repository hooks. Auto Deploy enabled in Coolify does not prove GitHub has a hook configured.
4. Inspect secret presence only as a boolean. Never print the secret, full token, API key, or private-key material.
5. Capture the current `origin/main` SHA and running image/build SHA separately; equality proves only the current deployment, not that future pushes are automated.

## Guided UI setup

When guiding Joshua through screenshots, give one action per message and wait for the next screenshot. Do not bundle later secret steps into the current step.

1. Open the Coolify application—not global Settings—then **Configuration → Webhooks**.
2. Under **Manual Git webhooks → GitHub**, copy the GitHub event URL. Do not reveal the secret or click its eye icon in a shared screenshot.
3. Open GitHub repository **Settings → Webhooks → Add webhook**.
4. Paste the Coolify GitHub event URL as the Payload URL. Reject usernames or repository URLs in this field.
5. Select `application/json`.
6. Add the Coolify-provided secret privately.
7. Keep SSL verification enabled, select **Just the push event**, keep the hook active, and submit once.

Verify the saved hook by reading it back from GitHub: it must be active, subscribe to `push`, use JSON, and show a successful initial `ping` delivery. Treat the ping as endpoint/authentication validation only, not as deployment proof.

## End-to-end merge test

Use a narrowly scoped, approved documentation-only PR when a harmless test event is needed. The PR should not touch runtime behavior, environment variables, hosted data, migrations, or secrets.

After Joshua merges:

1. Record the full merge commit SHA from GitHub.
2. Read the hook deliveries and require one successful `push` delivery with a 2xx response.
3. Read Coolify deployments and require exactly one deployment for that SHA.
4. Wait for terminal status; require **Running / Healthy**, not merely queued, building, or a successful webhook response.
5. Read `/api/build-id` from the deployed site and require exact equality with the merge SHA.
6. Record evidence on the issue without copying webhook secrets, authenticated URLs, environment values, or build credentials.

If the push delivery succeeded but no deployment began, re-check Coolify Auto Deploy and branch filtering. If no push delivery exists, inspect the GitHub hook configuration and recent delivery error before touching Coolify. If deployment fails, keep the previous healthy container and inspect the failed build rather than retrying blindly.