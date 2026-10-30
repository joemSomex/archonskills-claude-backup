# Higgsfield integration

## Pick one route

### Remote MCP / account OAuth

- Endpoint: `https://mcp.higgsfield.ai/mcp`
- Authentication: OAuth against the user's Higgsfield account.
- Billing: uses that account/plan's credits.
- An API key does not authenticate this remote MCP.

Configure in the exact Hermes scope that should receive the tools:

```bash
HERMES_HOME=/path/to/hermes-home hermes config set mcp_servers.higgsfield.url https://mcp.higgsfield.ai/mcp
HERMES_HOME=/path/to/hermes-home hermes config set mcp_servers.higgsfield.auth oauth
HERMES_HOME=/path/to/hermes-home hermes config set mcp_servers.higgsfield.enabled true
HERMES_HOME=/path/to/hermes-home hermes config set mcp_servers.higgsfield.connect_timeout 60
HERMES_HOME=/path/to/hermes-home hermes mcp login higgsfield
HERMES_HOME=/path/to/hermes-home hermes mcp test higgsfield
```

Run login interactively. If the browser returns a localhost redirect on another device, paste it back into the waiting terminal, never into chat. Inspect the discovered schemas before relying on generation tools; remote schemas and OAuth metadata can change independently of Hermes.

### Server-side API key / SDK

- Billing: separate Higgsfield API balance, not the consumer account's plan credits.
- Official SDK credential forms:

```env
HF_KEY=key-id:key-secret
```

or:

```env
HF_API_KEY=key-id
HF_API_SECRET=key-secret
```

Use a profile-owned isolated environment:

```bash
uv venv "$HERMES_HOME/tools/higgsfield-api/.venv"
uv pip install --python "$HERMES_HOME/tools/higgsfield-api/.venv/bin/python" higgsfield-client python-dotenv
```

A safe local detector loads the selected profile `.env`, calls `higgsfield_client.auth.get_credential_key()`, and reports only presence, combined-format validity, and optionally length. It must never print the credential. This does not prove remote validity or balance.

Do not install the account/CLI skill and assume it uses the API key: the official Higgsfield CLI normally authenticates an account session, while the Python SDK consumes `HF_KEY` or the key/secret pair. Keep the route and billing source explicit.

## Paid-call gate

Before image/video/3D/audio generation report:

- model or endpoint
- complete prompt/inputs
- output count, duration, resolution, aspect ratio
- price or `exact cost unknown`
- which balance will be charged

After approval submit once. On timeout, inspect request state by ID before any retry. For 3D/game production, route outputs through Blender optimization and runtime validation before calling them production-ready.
