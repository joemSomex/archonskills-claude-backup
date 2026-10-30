---
name: seamless-loop-video-prompting
description: Use when prompting subtle seamless video loops from stills.
version: 1.0.0
metadata:
  hermes:
    tags: [Video, Seamless Loop, Image-to-Video, Timing, Lighting]
---

# Seamless Loop Video Prompting

Write production-ready image-to-video prompts for subtle, imperceptible loops whose first and last frames share the same visual state.

When asked for a loop prompt or revision, proceed directly to the finished prompt without requesting approval for a concept, motion plan, timing map, or internal QA checkpoint. Make ordinary creative choices from the supplied still and brief; ask only if an essential source cannot be recovered or the specified loop requirements are genuinely irreconcilable. Drafting permission does not authorize paid generation, changes to canon, attachment archiving, or durable memory writes.

## Procedure

1. **Inspect and map the still.** Identify the fixed camera composition, protected architecture and objects, every allowed moving region, local lights, reflections, and any element that must remain pixel-stable. Use screen-relative directions.
2. **Resolve loop physics before writing motion.** Separate cyclic state from instantaneous velocity. For one-way movement that must never reverse, specify a horizontally or vertically tileable procedural field: content exits one boundary and is replenished continuously at the opposite boundary while velocity keeps the same sign. Never solve a loop by ping-ponging, reversing, rewinding, or snapping back.
3. **Lock the camera and geometry.** Explicitly forbid dolly, pan, tilt, roll, zoom, lens breathing, handheld drift, reframing, parallax changes, structural deformation, texture drift, and reflection misalignment when the source composition is locked.
4. **Keep motion measurable and small.** State total displacement as a percentage of the visible region, define low-frequency local deformation separately, and forbid faster or larger interpretations. For nearly invisible cloud motion, use a few percent of the window width over the full runtime plus gentle edge billowing.
5. **Write a complete timeline.** Cover the entire runtime with no gaps or overlaps. Give each event an exact start, ramp, brief hold, recovery, and stable buffer. Use one-way state descriptions such as `100% → 97% → 100%` for dimming; do not use vague words like “flicker” without a curve.
6. **Desynchronize local light events deliberately.** Give each fixture its own pulse count and non-overlapping extrema. Keep the fixture on, use tiny changes, and restrict spill to physically nearby surfaces and reflections so local breathing does not become a global exposure change.
7. **Match start and end states.** Reserve stable buffers at both ends. Restore fixture brightness, reflection state, exposure, atmosphere density, and procedural texture phase by the final frame while preserving any required one-way velocity.
8. **For multi-shot sequences, cut instead of moving between locked cameras.** Assign one fixed camera per shot, place a `HARD CUT` at an exact timestamp, and carry object identity, material, lighting direction, animation direction, speed, and phase across the cut. A close-up must continue the same animation rather than restart it.
9. **Remove unwanted semantic graphics.** In hologram close-ups, ban text, letters, numbers, code, coordinates, logos, icons, buttons, reticles, and pseudo-text. Replace source interface marks with non-semantic rings, particles, light bands, or abstract geometry.
10. **Finish with a negative-motion gate.** Ban unrequested people, craft, weather, particles, UI, object morphing, edge melting, geometry wobble, material shimmer, and AI texture instability.

## Always-on Rules

- Preserve literal motion direction in image coordinates. If motion must remain rightward, repeat that it never moves left, never reverses, and never uses ping-pong playback.
- Treat “first frame equals last frame” and “always moves one way” as compatible only through periodic or tileable motion, because ordinary object translation cannot satisfy both without a reset.
- Use local light intensity changes of only a few percent for imperceptible loops; keep color temperature, fixture shape, and position fixed.
- Describe breathing dimming as a smooth decrease, short minimum hold, and smooth return. Never call it strobing, flashing, or fault flicker unless that is genuinely wanted.
- Keep every architectural element and static prop motionless when the user asks for a locked environment.
- On revisions, return the full revised prompt unless the user explicitly asks for only the replacement block.

## Verification

Confirm before delivery:

- Runtime and every interval sum exactly.
- Camera register and geometry locks are explicit for every shot.
- Every moving element has direction, magnitude, speed character, and forbidden counter-motion.
- One-way cyclic motion has a tileable/replenishing mechanism rather than reversal.
- Light pulses have exact counts, separate extrema, tiny amplitudes, and local-only spill.
- The final state matches the opening state without stopping, reversing, or visibly resetting required continuous motion.
- Multi-shot cuts preserve animation phase and object identity.
- Text and interface exclusions cover pseudo-text as well as readable copy.
