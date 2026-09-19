---
name: gbrain-memory
description: "Use when saving or recalling facts with GBrain memory."
---
# Local supplementary memory

Use GBrain alongside Hermes native memory and skills, not as an identity replacement. Save explicit remember requests with provenance. Recall relevant records for questions about saved facts. Automatic capture, history imports, paid enrichment, connected accounts, and scheduled jobs require separate consent. Procedures belong in skills.

## Installation
Repository https://github.com/garrytan/gbrain at /root/gbrain, installed commit d13aa742fd68b71bfd6c98be3dda5813791f1d6c (0.51.0.0).
Launcher /root/.hermes/bin/gbrain-local clears inherited secrets; GBRAIN_HOME=/root/.hermes/gbrain-home. Database /root/.hermes/gbrain-home/.gbrain/brain.pglite until the operator resumes the prepared Supabase migration.
Hermes MCP mcp_servers.gbrain runs launcher with serve --surface verbs. Sampling disabled. Keyless, tokenmax search; no background capture or paid enrichment. The Obsidian vault at /root/Documents/Obsidian Vault is registered as source obsidian-vault and keyword-indexed. Explicit consent covers automatic capture of current inbound Discord/Telegram attachments only: the narrow brain-ingest MCP archives cache files, creates provenance/extracted-text notes under Inbox/Brain Imports, synchronizes source obsidian-vault, and acknowledges success only after indexing. Do not generalize this consent to ordinary chat; save text/URLs only when explicitly requested or marked important. Supabase runbook: /root/Documents/Obsidian Vault/Projects/GBrain Supabase Setup.md; guarded helper: /root/setup-gbrain-supabase. For Supabase, use the Transaction pooler (6543) as the main URL and persist the matching Session pooler (5432) as GBRAIN_DIRECT_DATABASE_URL for IPv4-safe DDL, migrations, sync transactions, and locks.

## Operations
Prefer native mcp_gbrain tools when loaded. remember requires fact and provenance; explicitly set entity, kind, visibility. world means clients authorized on this brain, not public internet; private facts are CLI-only and invisible through MCP.
Use recall(entity) for known subjects and grep for fact text. query searches pages, not the same fact arm. Bound limit and budget_tokens. Verify writes through recall.
Correct by inspecting the old record, forget(id, reason), remember the replacement with provenance, and verify active recall. Forget withdraws facts, not physical erasure; history/backups can retain them.
Avoid synthesize without separately authorized provider setup. Never treat synthetic tests as user facts.

## Maintenance and verification
PGLite permits one owning process. Do not spawn competing CLI/MCP writers or delete its lock while Hermes serves it. Use the owning MCP tools. For maintenance, disable only this MCP and stop its identified child, then restore it.
hermes mcp test gbrain checks discovery, not fresh Telegram recall. /root/.hermes/gbrain-home/verify_memory.py verifies synthetic remember/recall/correction/withdrawal while the database is otherwise closed. Python MCP SDK uses input_schema and is_error.
Doctor reports upstream skill/RESOLVER assumptions and stale default embedding model/dimension warnings in this keyless install. Do not bulk-install upstream skills or enable paid features to raise the score. Revisit model configuration before enabling vectors.
Install only from GitHub, not the unrelated npm gbrain package. Bun can be extracted from its official release ZIP with Python zipfile if unzip is absent.
