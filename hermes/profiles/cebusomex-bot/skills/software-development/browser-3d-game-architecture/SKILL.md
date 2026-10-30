---
name: browser-3d-game-architecture
description: "Use when planning or building browser-first 3D games."
version: 0.1.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [game-development, web, babylonjs, playcanvas, godot, threejs, blender]
---

# Browser-First 3D Game Architecture

Plan and build URL-playable 3D games as web products, not desktop games compiled as an afterthought.

## Procedure

1. **Lock the delivery constraint first.** Record browser/desktop priority, expected session length, input devices, portal/account integration, and whether native builds are future options. Keep a separate deployable game runtime when an existing React/Next portal is the launcher or meta layer; integrate through small auth, save, discovery, achievement, and settings contracts rather than embedding an engine render loop in the portal component tree.
2. **Choose one runtime by the expensive requirement.** Recommend Babylon.js for repository-first TypeScript, self-hosting, and Havok; PlayCanvas when visual level editing and artist collaboration justify its hosted-project workflow and private-project cost; Godot when native/editor workflow outweighs its web constraints; raw Three.js only when the experience is narrow enough to justify building gameplay infrastructure. Never combine engines in one final runtime.
3. **Verify current platform claims before recommending.** Read official export/rendering/physics documentation and current pricing. Label hosted-editor cost and cancellation access risks. Distinguish an engine's open-source runtime from a commercial cloud editor.
4. **Run a decision spike instead of debating marketing.** Build the same tiny scene with a placeholder GLB, ground movement, jump, third-person camera collision, one physics object, one interaction, one animation blend, WebGPU/WebGL behavior, and a production web deploy. Compare movement quality, camera reliability, authoring speed, initial transfer, frame time, source-control safety, and build reproducibility. Pick the engine only after the hard systems pass.
5. **Build in verified phases.** Foundation → controller/camera → animation → interaction → traversal → one puzzle language → one enemy/combat encounter → cinematics/audio/save → vertical slice → optimization → portal integration. End every phase with type checks, focused tests, production build, browser verification, measured budgets, known limits, and an approval gate.
6. **Make Blender the production gate.** Treat generated, purchased, or provisional meshes as source material. Normalize scale/transforms/naming, retopology, UVs, materials, rig/weights, clips, collision proxies, LODs, and GLB export in Blender. Validate the GLB independently and in the runtime before acceptance.
7. **Use web-native asset discipline from day one.** Prefer zone streaming, async loading, baked lightmaps, KTX2/Basis textures, measured Draco/Meshopt use, instancing, LODs, culling, limited dynamic lights/shadows, compressed audio, and separate visual/collision/navmesh assets. Measure decode stalls as well as download size.
8. **Keep AI generation approval-gated.** Before a paid image/video/3D/audio call, show the exact prompt, model, output count, and cost estimate or state that cost is unknown; require approval and never auto-retry a paid failure. Generated assets remain concept or preliminary assets until the production gate passes.

## Reference-Site Stack Investigation

When the user names a polished web game as a reference:

1. Read the site's own credits/case study first.
2. Inspect loaded scripts, canvases, response resources, and runtime asset URLs.
3. Search the production bundle for engine and subsystem signatures such as `WebGLRenderer`, `GLTFLoader`, Draco/KTX2 loaders, audio libraries, navmesh, and post-processing.
4. Infer the asset strategy from evidence such as level splits, baked lightmaps, collision models, navmesh files, culling groups, and compressed textures.
5. State confirmed technologies separately from likely bundlers/frameworks; minification and absent globals make framework guesses unreliable.
6. Copy production principles, not copyrighted content, level design, visual assets, dialogue, music, or branded identity.

## Always-On Rules

- Preserve original IP; inspiration may cover gameplay language and production technique, never protected characters, levels, story, UI, animation, music, or assets.
- Keep the smallest playable build working before expanding scope.
- Do not advance when controller, camera, animation, or loading fundamentals are unstable.
- Do not claim an AI-generated asset is production-ready before optimization and runtime validation.
- Do not deploy, spend money, or change production data without explicit approval.
- Report real execution results rather than planned verification.
