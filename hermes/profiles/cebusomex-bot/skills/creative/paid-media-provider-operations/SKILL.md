---
name: paid-media-provider-operations
description: "Use when operating paid generative-media providers."
version: 1.0.0
metadata:
  hermes:
    tags: [image-generation, video-generation, 3d, audio, mcp, api, oauth, billing]
    category: creative
---

# Paid Generative-Media Provider Operations

Connect and operate image, video, 3D, or audio providers without leaking credentials, confusing billing surfaces, or spending before approval.

## Procedure

1. **Choose the integration before touching credentials.** Establish whether the user wants remote MCP/OAuth, a vendor CLI/account session, or a server-side API key/SDK. Treat them as separate integrations even when they reach the same brand: they may use different credentials, balances, models, and tools.
2. **Choose the Hermes scope explicitly.** Resolve `$HERMES_HOME` before configuring. Root/default (`/root/.hermes` on this VPS) and named profiles (`/root/.hermes/profiles/<name>`) are isolated; a server on the root gateway does not automatically appear in a named Telegram/Discord profile. State which agent will receive the tools before writing config.
3. **Configure through supported interfaces.** Use `hermes mcp add`, `hermes config set`, or the provider's authenticated CLI; never hand-edit `config.yaml`. Keep API credentials in the selected profile's `.env` or an enabled secret manager, never in config, prompts, skills, repositories, chat, or command output.
4. **Migrate secrets without revealing them.** Search only for credential *names* and locations. Never print values or scrape transcripts, shell history, or session logs for a key. When the user explicitly asks to reuse a local credential, copy it server-side into the intended secret scope atomically, keep mode `0600`, and print only boolean/format checks.
5. **Install provider dependencies in isolation.** Prefer an app/profile-owned `uv` environment or vendor CLI rather than mutating the agent runtime. Pin the installed version for reproducibility, but re-check the current vendor release before future upgrades.
6. **Verify in layers, cheapest first.** Confirm config → dependency import → credential detection → non-billable remote status/catalog call when one exists → bounded paid canary only after approval. A local credential detector proves presence and format, not remote validity or available balance.
7. **Present the billable request before sending.** Show the exact prompt, model, output count/duration/resolution, known cost estimate, and billing surface. If the provider does not expose current pricing, say `exact cost unknown` and require explicit acceptance of that uncertainty.
8. **Execute once and verify.** Submit one approved request, retain its job/request ID internally, poll rather than resubmit, verify terminal status and returned artifact, then deliver the asset using the current platform's native media convention. Never retry a timed-out or failed paid submission until the provider is checked for an already-created job.
9. **Preserve production boundaries.** Treat generated 3D assets, textures, character art, video, and audio as provisional until the relevant production pipeline accepts them. Do not publish, deploy, train an identity model, or expose a result publicly without separate approval.

## Standing user rules

- Confirm the exact prompt, model, output count, and cost or cost uncertainty before every paid generation.
- Never auto-retry a paid failure or timeout.
- Prefer concise setup instructions one verified step at a time, based on the latest terminal output or screenshot.
- Never claim Telegram/Discord generation works from credential detection alone; only an approved end-to-end canary verifies generation plus delivery.
- Preserve exact prompt wording when the user supplies it and do not add creative changes without permission.

## Provider references

- Higgsfield integration and billing distinctions: `references/higgsfield.md`
