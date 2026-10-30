---
name: kara-game-project
description: Use when planning or building the KARA browser game.
---

# KARA Game Project

## Locked direction

- Build **KARA** as an original, story-driven, third-person 3D action-adventure for desktop browsers first.
- Present it as a **canon-adjacent Galatea Terminal mission simulation**, not confirmed core canon.
- Make exploration and environmental puzzles the dominant experience; traversal and story follow, with limited readable combat.
- Set the first mission in a buried complex beneath a remote Galatea research outpost.
- Kara is a field systems engineer and recovery specialist, not a treasure-hunter analogue.
- Her signature contextual tool is an engineering resonance scanner for tracing systems, diagnosing structures, revealing evidence, and identifying contamination without automatically solving puzzles.
- Keep every character, location, story, puzzle, dialogue, visual identity, animation, and asset original; never imitate Tomb Raider characters, levels, UI, music, or copyrighted content.

## Technical recommendation

- Prefer a repository-first **TypeScript + Babylon.js + Vite** runtime with WebGPU and WebGL fallback.
- Use Babylon Havok where physics is justified, GLB/glTF for runtime assets, KTX2/Basis textures, HTML/CSS for suitable UI, and GSAP only for DOM transitions.
- Keep the game as an independently deployable build, preferably `play.galatea.system`, connected to the Next.js Galatea Terminal through explicit auth/save/unlock contracts.
- Use Blender as the production gate for topology, UVs, rigging, skinning, animation cleanup, collisions, LODs, materials, and GLB export.
- Use Higgsfield only for approved concepts, references, preliminary assets, previs, audio, and promotion. Confirm model and cost before every paid generation; generated assets are never production-ready without Blender review.
- Treat Equinox (`equinox.space`) as a visual/performance reference: Three.js, Blender, Houdini, GLB/Draco, KTX2, baked lightmaps, navmesh, culling groups, and spatial audio. Do not copy its content.
- PlayCanvas is the strongest Babylon alternative when visual scene editing and collaboration outweigh cloud-editor/private-project cost and repository-control concerns. Never combine multiple game engines in the final runtime.

## Delivery workflow

- Build a polished 10–15 minute vertical slice before the full game.
- Advance through verified phases only: architecture spikes; browser foundation; controller/camera; animation; interaction/scanner; traversal; puzzle framework; AI/combat; cinematics; save/audio; slice assembly; optimization; Terminal integration; release candidate.
- Keep input, movement, physics, animation, traversal, combat, interaction, audio, and camera communication separate. Never create one giant player-controller script.
- Use placeholders until mechanics are stable, measure browser performance continuously, and keep the build running at every phase boundary.
- Ask before destructive operations, production deployment, cloud migrations, irreversible canon changes, or spending money.
- The detailed copy-ready build prompts are in `/root/KARA_BUILD_PROCESS.md`; read that file when available instead of recreating the process from memory.
