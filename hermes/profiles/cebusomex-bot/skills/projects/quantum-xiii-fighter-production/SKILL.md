---
name: quantum-xiii-fighter-production
description: Use when building the Quantum XIII Unreal fighting game.
version: 1.0.0
author: Somex Studios, Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [game-development, unreal-engine, blender, tripo, codex, quantum-xiii]
    related_skills: [browser-3d-game-architecture, media-asset-lifecycle]
---

# Quantum XIII fighter production

## When to Use

Use this skill for architecture, character pipelines, coding, asset generation, combat design, testing, or production planning for the Quantum XIII 2.5D Unreal fighting game.

## Approved working direction

Build an original 2.5D one-on-one fighting game in Unreal Engine. Street Fighter is a genre/quality reference only; never copy its characters, costumes, moves, animation, stages, UI, audio, or story.

Use this production stack:

- Tripo AI for approved concept meshes and blockouts only.
- Blender as the mandatory production gate for scale, topology, UVs, shared rig, weights, animations, LODs and FBX export.
- Unreal Engine 5 for the final runtime.
- C++ for fixed-frame combat truth; Blueprints for presentation and content assembly.
- Codex for text code, tests, build tooling and documentation; never binary `.uasset`, `.umap`, `.blend` or `.fbx` editing.
- Git + Git LFS for a small team; move to Perforce when binary locking becomes a daily collaboration need.

## Canon and product boundaries

- Preserve exact Quantum XIII character identities and owner-approved canon. Generated material is never canonical by default.
- Start with Sylvia Bloom and one explicitly owner-approved antagonist; do not invent the opponent from a faction name.
- Keep portal membership and forum XP out of competitive fighter statistics. They may unlock cosmetics, lore, badges or non-competitive poses only.
- Deliver an offline local two-fighter/one-arena vertical slice before online, campaign, economy, portal linking or a full roster.
- Paid Tripo work requires the exact prompt, model/mode, count and cost estimate or an explicit statement that cost is unknown, followed by approval.

## Technical rules

- Run authoritative combat on an integer 60 Hz clock.
- Use custom input history, command recognition, fighter state machine and deterministic hit/hurt/throw boxes.
- Keep gameplay truth out of Animation Notifies and nondeterministic physics.
- Keep ordinary fighter movement kinematic and on a 2.5D fight plane.
- Build deterministic input replay and state checksums before any rollback-netcode work.
- Profile standalone builds on the Apple M5 Pro; Editor performance is not release evidence.

## Required project references

Read these before planning or implementing:

- `/root/galatea-system-stagin/docs/quantum-xiii-fighter/README.md`
- `/root/galatea-system-stagin/docs/quantum-xiii-fighter/STACK_ARCHITECTURE.md`
- `/root/galatea-system-stagin/docs/quantum-xiii-fighter/MAC_SETUP.md`
- `/root/galatea-system-stagin/docs/quantum-xiii-fighter/CHARACTER_ASSET_PIPELINE.md`
- `/root/galatea-system-stagin/docs/quantum-xiii-fighter/VERTICAL_SLICE_PLAN.md`
- `/root/galatea-system-stagin/docs/quantum-xiii-fighter/CODEX_WORKFLOW.md`
- `/root/galatea-system-stagin/docs/quantum-xiii-fighter/FIGHTER_DESIGN_TEMPLATE.md`

## First decision gate

Before building, ask for three decisions together: target platform scope, visual direction, and Sylvia Bloom's exact first opponent. If unresolved, use neutral mannequins and do not spend on character generations.
