---
name: ai-generation-provider-integration
description: "Use when integrating AI image/video provider APIs."
---

# AI Generation Provider Integration

Use this workflow when building an application, bot, or automation layer around image, video, audio, or multimodal generation providers.

## Procedure

### 0. Classify discovery versus implementation

Treat “How does this API work?” and “Can this connect to Hermes?” as **read-only discovery** unless the user explicitly asks to install, configure, authenticate, or build the integration. During discovery, inspect official public documentation and current local capability only; do not create files, add credentials, enable tools, scaffold a plugin, change configuration, or make authenticated test calls. An explicit “do not configure anything” is a hard boundary, not a prelude to setup.

End a discovery-only answer with the integration verdict, exact implementation gates, and a plain statement that no configuration changed. Move into implementation only after the user separately authorizes it.

### 1. Freeze implementation until discovery is complete

Do not scaffold provider clients, environment variables, model enums, or command options yet. First produce a provider-by-provider discovery report from official sources.

For each provider, classify every usable surface as exactly one of:

- **OFFICIAL MCP**
- **OFFICIAL API**
- **CUSTOM MCP WRAPPER AROUND OFFICIAL API**

Record official CLI/SDK options separately; a CLI is not an API and an MCP connector is not a server-to-server REST credential.

### 2. Establish a source hierarchy

Use sources in this order:

1. Official developer/API/MCP documentation
2. Official model catalog and per-model schema pages
3. Official provider help center and product announcements
4. Official organization repositories and CLI documentation

Treat search snippets, third-party wrappers, unofficial repositories, and marketing summaries as discovery leads only. Never derive endpoints, tool names, or schemas from them.

Use the grounded-citations workflow for the report. Cite operational claims sentence-by-sentence and attach a mechanically rendered Sources block.

### 3. Verify the integration surface

For every provider, capture:

- Official endpoint or package
- Authentication method and credential lifecycle
- Intended product use: interactive user account, agent connector, or embedded server application
- Exact tool/operation names when publicly documented
- Transport and runtime requirements; compare package engine constraints against the live host before declaring compatibility
- Capability coverage per surface, especially image versus video; an official MCP may expose only a subset of the provider's REST API
- Image, video, edit, upscale, reference, and cross-media workflows
- Current models and how model discovery works
- Per-model parameters rather than provider-wide guesses
- Single- and multiple-reference behavior
- Supported file types and documented byte limits
- Async submission, request identifiers, states, status lookup, and output retrieval
- Cancellation boundary
- Webhooks and delivery retry/deduplication semantics
- Account/model concurrency and rate-limit behavior
- Idempotency support
- Output retention and durable-download requirements

Use `references/discovery-matrix.md` as the report checklist. Load `references/cost-routing-retention.md` when comparing API, MCP, CLI, or intermediary-agent paths, or when deciding where generated media will persist.

### 4. Separate documented availability from account verification

A public catalog proves that a provider documents a capability; it does not prove the user's account can call it. Label every unresolved item as one of:

- **REQUIRES CONFIGURATION** — credentials, account access, plan choice, or an owner decision is needed.
- **NOT VERIFIED** — no official source or authenticated response establishes it.

After authentication, capture the live MCP `tools/list`, API model catalog, CLI JSON, or per-model forms before mapping commands. Never invent a convenient tool name or parameter from a natural-language feature label.

### 5. Choose the production surface by credential model

Prefer a documented server-side API for multi-user applications: it provides explicit credentials, schemas, lifecycle semantics, and operational controls.

Treat an OAuth MCP connector as an agent/account integration, not automatically as a multi-user backend. Before using it behind a bot, decide whose account owns generations, how tokens refresh and revoke, how credits are isolated, and whether centralized automation is allowed.

Never run `hermes mcp add` against a guessed endpoint. A marketing-page “MCP” label, navigation item, or third-party example is not proof of an official MCP server; require official endpoint documentation plus an authenticated discovery result before registration. When a documented server-side API exists, keep API integration and MCP discovery separate instead of trying an unverified OAuth MCP route.

If a provider has no public API, do not create an `*_API_KEY` variable or reverse-engineer private endpoints. Use the official MCP or official CLI only after authenticating a dedicated account and verifying live schemas and terms.

Treat the operator’s chosen surface as a hard architecture gate. “Use MCP, not the direct API,” “route through Claude Code,” or the inverse forbids silent fallback to another surface for tests, estimates, or generation. Do not keep a supposedly harmless direct credential probe alive after the operator has rejected that route; ask before changing the route again.

### 5.1 Account for every execution layer

Before recommending a path, enumerate its independent usage meters:

- the conversational/orchestrator model that interprets the request;
- any intermediary agent model used to call the provider;
- the generation provider’s credits, video tokens, or per-request charge.

MCP itself is a protocol and does not bill model tokens, but MCP tool schemas, arguments, and results consume the context/usage of whichever model hosts the MCP call. A direct Hermes→MCP path therefore avoids an intermediary model’s usage; a Hermes→Claude Code→MCP path can consume both Hermes-model usage and Claude usage, plus provider credits. State this before calling one route “cheaper.”

### 6. Design commands from capabilities, not wishes

Expose only parameters declared by the selected model's current schema. Route through a normalized internal request, but strip unsupported fields before submission.

For dynamic catalogs:

- Prefer a verified model-discovery endpoint/tool.
- Otherwise maintain a versioned registry sourced from official per-model documentation.
- Store source URL and refresh timestamp with each registry entry.
- Never present marketing examples as a complete permanent model list.

### 7. Design async reliability before generation code

Persist the local request before provider submission. Deduplicate platform retries using the incoming interaction/message ID before making any generation POST.

Store provider request IDs immediately. Distinguish:

- queued
- processing
- completed
- failed
- safety/moderation rejection
- canceled

Do not retry an ambiguous submission unless the provider supports idempotency. Poll with bounded backoff and jitter, and use webhooks when documented; keep polling as a recovery path. Deduplicate terminal webhook deliveries by provider request ID and terminal state.

Cancellation copy must match the provider boundary. If cancellation is only possible while queued, never imply that an in-progress remote job was stopped.

Revalidate credentials immediately before a paid submission using an official non-billable endpoint when one exists. A successful generation from an earlier turn does not prove the credential is still valid; keys can be revoked or rotated between calls. Stop on `401`/`403` instead of attempting a paid generation.

Treat provider storage and local storage as separate copies. MCP or API generation happens on the provider’s infrastructure first; a returned URL does not mean the asset lives on the agent host. Download completed media before provider retention expires, keep unapproved files in a cache, and copy approved files into a durable output directory with prompt, model, request ID, settings, cost, provenance, and checksum. Never promise provider-side deletion unless a documented delete operation returns success.

### 8. Gate implementation

Do not begin provider implementation until the report answers:

- Which official surface will be used?
- How will the bot authenticate unattended?
- How are models and schemas discovered?
- How are references uploaded?
- How are jobs tracked, canceled, and recovered?
- What limits must the local queue enforce?
- What remains REQUIRES CONFIGURATION or NOT VERIFIED?

The final discovery report should end with an implementation verdict per provider: **ready**, **conditionally ready**, or **blocked**, with the exact gate that changes the verdict.

### 9. Install and verify credentials without exposing them

On Debian/Ubuntu systems governed by PEP 668, install provider SDKs in a project virtual environment instead of overriding the system package manager:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install <provider-sdk> python-dotenv
```

If `venv` support is absent, install the distribution's `python3-venv` package first. Do not recommend `--break-system-packages`; it bypasses the ownership boundary and can damage OS-managed Python dependencies.

Create the credential file at the path the application actually loads, restrict it to the owning user with `chmod 600`, and use only variable names documented by the installed SDK. A `.env.local` file is not loaded by `python-dotenv`'s default search merely because it exists; call `load_dotenv("/exact/path/.env.local")` or configure the application explicitly.

Before making an authenticated call, parse the exact credential file and report only:

- file path
- recognized variable names
- whether required values are non-empty
- SDK/package version

Never print credential values, prefixes, or response content that may echo them. Do not treat the user's statement that a key was saved as verification; confirm that the process performing the test can read a non-empty recognized variable from the same host, user, and path.

Only after that local preflight passes, use an official non-billable identity, account, model-list, or status endpoint to test authentication. Distinguish outcomes explicitly: accepted, rejected (`401`/`403`), unreachable, or inconclusive. Do not submit a generation merely to test a key because it may consume credits. If the provider has no documented read-only authentication probe, say that authentication cannot be verified without a potentially billable operation and ask before submitting one.
