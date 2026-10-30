---
name: badge-levels
description: Use when creating badge rank material variants.
version: 1.0.0
metadata:
  hermes:
    tags: [Badge, Material Variants, Image Editing]
    related_skills: [pixel-preserving-image-compositing]
---

# Badge Levels

## When to Use

Use for Quantum 13 badge levels, iron/bronze/silver/gold badge ranks, or an immutable emblem with material-only variants.

## Workflow

Create four standalone Quantum 13 badge images from a supplied master: Level I iron, Level II bronze, Level III silver, Level IV gold. The master is the sole authority for silhouette, geometry, proportions, central symbol, relief, structural details, composition, viewpoint, framing, and scale. Each rank reference contributes **surface material only**; never copy its object, shape, symbol, or broad lighting field.

1. Inspect the original master and every assigned material reference. Recover omitted attachments from the source message manifest when needed, including AVIF. Map roles by filenames and visible content rather than attachment order. Ask only if a required source cannot be recovered.
2. Preserve one common canvas, background, light direction, and readable emblem details. Prefer deterministic material translation of the same source raster: keep original alpha and luminance topology, apply reference-derived dark-to-highlight color ramps and restrained high-pass microtexture inside the existing metal. Never redraw or regenerate geometry to create the rank differences. Load `pixel-preserving-image-compositing` and read its material-only variants reference before rendering. If the master is opaque, define and verify a foreground mask instead of inventing transparency.
3. Render every level independently from the untouched master, not from another rank. Do not add text, numbers, borders, symbols, ornaments, glow, or other effects. If a genuinely generative step is necessary and the user permits it, use ChatGPT/OpenAI image generation only, never Claude or Higgsfield; label any unverified geometry preservation as approximate.
4. Verify four distinct standalone files: identical dimensions and alpha/shape, faithful central symbol and structural details, distinguishable materials, legibility at website-thumbnail size. Inspect each file at native size. A contact sheet may be used **internally for QA only**, never as a deliverable.
5. Deliver only the four newly rendered rank images, **separately**, labeled Level I - Iron, Level II - Bronze, Level III - Silver, Level IV - Gold. Do not send a composite showing all levels. Do not resend the unchanged master. In Discord, attach each final PNG on its own bare `MEDIA:/absolute/path.png` line. Report plainly if any fidelity gate could not be verified.

Gather the master and references fresh for each request; do not bind this workflow to the examples or temporary files from a past run.
