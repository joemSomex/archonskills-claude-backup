---
name: digital-card-game-design
description: "Use when designing original digital card games."
version: 1.0.0
author: Somex Studios
license: Proprietary
metadata:
  hermes:
    tags: [game-design, card-game, deckbuilder, unreal-engine, prototyping]
    category: software-development
---

# Digital Card Game Design

Design an original, buildable digital card game from genre references without copying protected expression or committing prematurely to live-service scope.

## When to Use

Use for reference-game analysis, original card-system design, narrative deckbuilders, tactical card games, vertical-slice scoping, and Unreal card-game architecture. Use the paid-media provider skill alongside this one before any billable asset generation.

## Procedure

1. **Identify the reference before evaluating it.** Resolve the exact title, publisher, video purpose, and underlying game. When a YouTube stream cannot be downloaded, use YouTube oEmbed (`https://www.youtube.com/oembed?format=json&url=<encoded-url>`) to verify title/channel, inspect the public thumbnail, then research official rules pages. Distinguish an event promotion, trailer, or tournament broadcast from the actual game mode.
2. **Separate verified rules from visual inference.** Derive deck size, card types, resources, victory condition, classes, and signature mechanics from official game documentation. Use frames or thumbnails only for visible presentation claims. Label unavailable footage rather than implying it was watched.
3. **Assess both design quality and product model.** Evaluate readability, strategic depth, audiovisual feedback, onboarding, collection economy, monetization, balance burden, and current player reception separately. A polished battle system can still be a poor business-model reference. Query current storefront review totals when making reception claims and calculate ratios programmatically.
4. **Create an inspiration boundary.** List reusable genre conventions—turns, decks, resource costs, units, actions, targeting, and animated feedback—separately from elements that must remain original: names, card text, characters, art, factions, board/UI layout, icons, sounds, branded mechanics, animations, economy, and visual identity.
5. **Choose scope before designing content.** Default a small team to a single-player narrative deckbuilder or tactical card campaign. Require a specific justification before recommending a collectible PvP live service, because matchmaking, authoritative networking, anti-cheat, balance, economy, customer support, seasonal content, and population health multiply the project scope.
6. **Derive the signature mechanic from the IP's central conflict.** Write the setting's core dramatic question, then turn it into a repeated player verb and measurable state change. Do not merely rename another game's evolution, mana, or faction system. Define why the mechanic could exist only in this universe.
7. **Specify the minimum rules contract.** Lock the turn phases, zones, resources, legal actions, card types, targeting rules, state transitions, victory/mission conditions, randomness policy, and save/replay requirements before producing card art or effects. Include non-combat objectives when the narrative calls for investigation, containment, rescue, negotiation, or survival.
8. **Build the deterministic core before presentation.** Keep battle state and card resolution independent of animation, UI, camera, and audio. Every legal action must be serializable and replayable from an initial seed so tests, AI, undo/debug tools, replays, and possible future networking share one source of truth.
9. **Make content data-driven.** Store card definitions in validated Data Assets, tables, or versioned JSON rather than bespoke visual scripts. Use stable IDs and tags for traits, factions, target filters, statuses, and narrative flags. Automate checks for duplicate IDs, invalid costs, missing assets, illegal targets, and unresolved references.
10. **Prototype with a bounded set.** Begin with roughly 24–30 cards, one player deck, three encounter decks, one signature mechanic, three teaching encounters, one boss or capstone, local saves, and a packaged build. Expand only after playtests show that decisions remain interesting without final art.
11. **Use Unreal as presentation, not the rulebook.** Put deterministic battle logic, serialization, and validation in C++ or a testable engine-neutral module; use Blueprints for board choreography, mission scripting, cameras, Niagara, audio, and rapid content iteration. A card must resolve correctly when all presentation is disabled.
12. **Gate generated media through production.** Use AI output for concepts and preliminary assets only. Preserve prompts, model/version, generation date, commercial-use entitlement, source output, edits, and final asset mapping. Route 3D outputs through Blender cleanup and engine validation. Confirm exact prompt, model, output count, and known or unknown cost before every paid generation.
13. **Verify the vertical slice.** Test deterministic replay, save/load across turns, every card and target rule, keyboard/mouse and controller flow, readable card text at target resolution, packaged Windows execution, and performance with effects enabled. Do not propose Steam, PvP, packs, or live economy until this slice is fun and stable.

## Output format

Present recommendations in this order:

1. Exact reference identification and what it demonstrates
2. Good patterns to study and poor patterns to avoid
3. Fit with the user's story/IP
4. Original game pitch and signature mechanic
5. Core loop, card types, resources, zones, and victory conditions
6. First playable scope
7. Engine/content architecture
8. Production-tool responsibilities
9. Legal, provenance, monetization, and scope boundaries
10. Clear next build gate
