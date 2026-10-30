---
name: supabase-production-operations
description: "Use when applying or verifying hosted Supabase SQL."
version: 1.0.0
---

# Supabase production operations

Use this workflow for hosted Supabase schema changes, corrective SQL, and questions about whether a database-backed fix is actually live.

## Procedure

1. **Separate the five states before acting.** Check repository code, automated tests, GitHub issue/PR state, the hosted Supabase database, and the deployed Edge Function/runtime independently. Never infer that a merged migration changed an already-provisioned database or that current `main` matches the deployed bundle.
2. **Connect through the official Supabase MCP when available.** Install it from the Hermes MCP catalog when absent, then have the user complete OAuth from an interactive terminal or Desktop session. Never request an OAuth redirect URL, authorization code, access token, or client secret in chat. Run `hermes mcp test supabase` and require a successful connection plus discovered tools before proceeding. MCPs added mid-session are not injected into the frozen tool catalog: start a fresh Hermes session (or a scoped `hermes chat -q` process) for the first tool call rather than claiming the connection is unusable.
3. **Identify the exact project before any write.** List accessible organizations/projects and read the selected project's reference, name, and current schema objects. If two projects could match, stop and ask. Distinguish projects by querying the expected domain tables and functions, not by name alone.
4. **Inspect live prerequisites.** Read the affected columns, functions, views, grants, and migration history. Do not rely on a general table-list call to prove that private views exist; query `to_regclass`, `to_regprocedure`, `information_schema`, `pg_get_functiondef`, and `pg_get_viewdef` directly. When behavior also lives in an Edge Function, read its deployed version/hash and inspect the retrieved bundle without exposing secrets. A live object without a migration-history row is a provenance gap, not proof that a named migration ran; a duplicate-object error likewise does not justify rerunning the historical file.
5. **Prepare the smallest forward-only patch.** Replace only the affected view/function or add a new migration step. Preserve column order and types for `CREATE OR REPLACE VIEW`, authorization boundaries, grants, and security-definer settings.
6. **Verify locally before production.** Reproduce the relevant schema with PGlite or the repository's database verifier, apply the patch twice, and assert the user-visible behavior—not only successful parsing.
7. **Gate the production write.** Treat a direct request to apply the named patch as approval for that patch only. Ask again if the project, SQL, scope, destructive effect, or data rewrite differs from what was approved.
8. **Apply through MCP and read back.** Execute the exact verified SQL, then re-read the changed object definition and run a focused behavioral query. A successful execute response alone is not completion.
9. **Report concisely.** State project, object changed, verification performed, and anything still local-only or blocked. Never claim the live site is fixed from repository tests alone.
10. **Provision shared application/Vault secrets as a synchronized pair.** First search the application for the expected environment-variable and Vault names; an unused secret is preparation, not a working integration. Generate one cryptographically random value without printing it, store it as a masked runtime-only application secret and as one uniquely named Vault row, verify metadata rather than decrypted plaintext, exercise one focused authenticated call, then clear clipboard and shell variables. Follow `references/vault-shared-secrets.md` for creation, rotation, and recovery.

## Standing safeguards

- Never rerun a historical migration merely because its file now contains a fix; migration files are not synchronization mechanisms after deployment.
- Never apply local migrations to hosted Supabase without explicit user authorization.
- Never expose `.env`, database URLs, OAuth tokens, service-role keys, or client secrets.
- Prefer reversible, idempotent DDL. Do not use `DROP`, destructive rewrites, or broad grants when a targeted replacement works.
- Preserve issue boundaries: a patch for one verified defect must not silently include another unresolved fix.

For forward-only patch patterns and verification recipes, read `references/forward-only-sql.md`.
