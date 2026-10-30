---
name: quantum-xiii-card-game
description: "Use when building the Quantum XIII browser card game."
version: 0.1.0
author: Somex Studios
license: Proprietary
metadata:
  hermes:
    tags: [game-development, quantum-xiii, babylonjs, card-game]
    related_skills: [browser-3d-game-architecture, kara-project]
---

# QUANTUM XIII: CONTINUITY PROTOCOL

## When to Use

Use for product, narrative, architecture, implementation, art-pipeline, QA, or deployment work on the browser card game and `card.galatea.systems`. Do not use it as the build guide for the separate native Unreal KARA game.

## Authority

- Read `/root/quantum-xiii-continuity-protocol-docs/README.md` first, then its bundled World Bible and numbered documents in the stated order.
- Treat `/root/quantum-xiii-continuity-protocol-docs/references/QUANTUM_XIII_WORLD_BIBLE_CANON_v9.md` as read-only canon. Its filename says v9 while its internal heading says v10; surface the mismatch rather than renaming or resolving it.
- Preserve ambiguity around Kara/Dione, the Thirteen, Necroids, and NIC continuity. Do not invent canon to unblock implementation.

## Locked product direction

- Premium browser-native game at `card.galatea.systems`, separate from the Unreal KARA project and the Galatea Next.js render loop.
- TypeScript + Vite + Babylon.js; prefer WebGPU and require WebGL fallback. React/DOM may own menus, settings, and semantic accessibility surfaces, not game authority.
- Single-player narrative tactical deckbuilder first. Initial scope: 24 cards, three encounters, one boss.
- Original signature systems: Classification (Person/Asset/Anomaly/Unresolved), Resonance, Institutional Pressure, and Network/Facility/Field sectors.
- No PvP, matchmaking, packs, gacha, trading, battle pass, live-service economy, Steam/native packaging, or broad campaign in the vertical slice.
- Use a deterministic headless TypeScript rules package with stable IDs, seeded RNG, versioned serialization, action/event logs, and replay hashes. Presentation never decides outcomes.
- Supabase may handle identity/profile/progression/content. Any future competitive mode requires a server-authoritative service; never trust the client for outcomes or rewards.

## Production boundaries

- Blender is the mandatory production gate. Tripo output is preliminary 3D source only. Higgsfield is for approved concepts, previs, and card-art exploration.
- Before paid media generation, show the exact prompt, provider/model/version, output count, and cost or state cost is unknown; require explicit approval and never auto-retry a paid failure.
- Preserve asset provenance, licenses, character identity, and original IP. Study genre conventions only; never copy Shadowverse characters, cards, text, classes, board/UI trade dress, evolution system, art, animation, audio, or economy.
- Stop for approval before canon/scope changes, repository creation, paid work, asset promotion to final, external services/telemetry, deployment/DNS/production changes, destructive actions, or phase progression.

## Execution

- Start with Phase 0 only from `docs/13-IMPLEMENTATION-ROADMAP.md`. Do not pretend a codebase, backend, deployment, assets, credentials, or tests exist.
- Use `docs/18-CODEX-START-PROMPT.md` for Codex and `docs/19-CLAUDE-START-PROMPT.md` for Claude.
- Keep rules independent of Babylon and test them headlessly. Every completed slice reports changed files, commands/tests and exit status, browser/build evidence, measurements, skipped checks, risks, and pending gates.
- The last direct probe of `https://card.galatea.systems/` returned Cloudflare HTTP 503. Treat the cause as unverified and follow the evidence-driven recovery checklist in `docs/12-DEVOPS-DEPLOYMENT.md` before making changes.
