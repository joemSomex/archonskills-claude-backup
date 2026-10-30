---
name: kara-project
description: "Use when working on PROJECT KARA. Preserve locked decisions."
version: 0.1.0
---

# PROJECT KARA

## Locked direction

- Build KARA as an original, story-driven, third-person Windows PC action-adventure in Unreal Engine, with Steam distribution considered after the vertical slice.
- Present it as a **canon-adjacent Galatea Terminal mission simulation**, not irreversible Galatea/Quantum XIII canon.
- Make exploration and environmental puzzles the dominant experience; traversal, story discovery, tension, and limited readable combat support them.
- Set the first mission in a buried complex beneath a remote Galatea research outpost.
- Kara is a field systems engineer and recovery specialist, not a treasure-hunter analogue.
- Her signature contextual tool is an engineering resonance scanner for tracing systems, diagnosing structures and machinery, reconstructing failures, revealing evidence, and detecting contamination. It must not automatically solve puzzles.
- The first deliverable is a polished 10–15 minute vertical slice, provisionally titled **KARA: Echoes of the Spire / The Sealed Descent**.

## Technical direction

- Use a separate Unreal Engine project and repository for a native Windows PC build. Do not embed the Unreal runtime in the Next.js portal and do not promise browser execution; current Unreal versions do not provide an official HTML5 export path.
- Use a Blueprint/C++ hybrid: Blueprints for rapid mission, interaction, cinematic, and content iteration; C++ for stable gameplay foundations, save/versioning, performance-sensitive systems, and reusable interfaces.
- Use Blender as the mandatory production gate for modeling, retopology, UVs, rigging, collision, LODs, animation cleanup, and FBX/glTF interchange. Tripo AI output is provisional source material, never a production asset without Blender cleanup and Unreal validation.
- Use Higgsfield for approved concept frames, mood, shot design, and cinematic previs. Preserve character identity and require exact prompt/model/output/cost approval before every paid generation.
- Use Claude for narrative/system design, Unreal architecture review, documentation, and Blueprint/C++ planning; use Codex for implementation, automation, tests, build scripts, and code review. Neither agent may publish, spend, apply destructive changes, or override canon without approval.
- Keep the existing Next.js Galatea Terminal as the web launcher, lore/dossier, community, account, and future Steam-link layer. Native game integration should use versioned backend contracts rather than sharing runtime code.
- Target Windows PC first. Treat Steam packaging, achievements, cloud saves, and store compliance as a later release phase after the vertical slice is proven.
- Preserve original IP and never combine multiple game engines in the production runtime.

## Production rules

- Work phase-by-phase; keep a verified playable build at every gate.
- Separate input, movement, physics, camera, animation, traversal, combat, interaction, audio, and cinematic systems. Never create a monolithic controller.
- Use placeholders until mechanics are stable. Generated assets are concepts or preliminary inputs until optimized, retopologized, UV-checked, rigged, collision-prepared, LODed, and exported through Blender.
- Preserve original characters, locations, story, enemies, puzzles, dialogue, visual identity, music, animations, UI, and assets; do not copy Tomb Raider or Lara Croft.
- Confirm the exact prompt, model, output count, and known/unknown cost before any paid Higgsfield or other media generation. Never retry a paid failure automatically.
- Do not make irreversible canon decisions, deploy, change production data, or perform destructive operations without approval.

## Build playbook

The existing `/root/KARA_BUILD_PROCESS.md` predates the Unreal Engine decision and must not be executed as-is. Revise it for the locked Windows PC / Unreal / Blender pipeline before starting. The first executable work remains **Phase 0 only**: architecture, repository/source-control choice, controller/camera/animation spike, Tripo-to-Blender-to-Unreal asset proof, AI-tool operating boundaries, and Windows packaged-build verification. Stop for review before vertical-slice production.
