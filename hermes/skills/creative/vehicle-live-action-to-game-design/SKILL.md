---
name: vehicle-live-action-to-game-design
description: "Use when 'Vehicle: Live Action to Game Design.' appears."
version: 1.0.0
author: Somex Studios + Hermes Agent
license: Proprietary
metadata:
  hermes:
    tags: [vehicle-design, image-generation, animation]
    related_skills: [reference-driven-image-generation]
---

# Vehicle: Live Action to Game Design

## When to Use

When the user writes `Vehicle: Live Action to Game Design.` with a source image, immediately generate the ten vehicle design sheets. Capitalization-only variants count. A full vehicle brief with `@image1` also triggers it. If a new invocation lacks an attachment but plainly repeats the last completed batch for the same vehicle, use that batch's **original** source photo, not its generated output, and create a fresh ten-file slate. If the vehicle/source is ambiguous, ask for the photo; do not silently substitute an unrelated image.

Read `references/authoritative-brief.md` before generation; it is the user's full specification. Inspect the actual source vehicle and write a morphology and connection inventory before prompting: body silhouette and proportions, repeated and exposed parts, windows, lights, panels, mechanical and material details, wear. Apply the brief's wheeled-vehicle details *only if they exist*: do not invent wheels, doors or grilles for a spacecraft, aircraft or boat. Treat unseen sides conservatively, disclose inferred geometry, and never certify exact turnaround fidelity from a single view. Also load `creative:reference-driven-image-generation` and the complex-prop-fidelity reference bundled with that skill.

Generate ten separate images using ChatGPT/OpenAI only, one call per file, always referencing the original source, never a generated variation. Each file is a clean four-view sheet of ONE consistent vehicle on a light neutral background: front/3/4 hero, side, rear and a close-up detail. Vary lighting, brushwork, texturing, shading and stylization but keep the geometry and parts locked. The primary style gate is dimensional painterly animated-series rendering: do not accept a merely photo-like/CGI turnaround with superficial brush marks as a finished style transfer. Inspect one style calibration if earlier attempts shared a style failure before repeating the batch; if it stays photographic, change the source role or approach while retaining OpenAI and original-source derivation.

Verify ten independent PNGs, ten distinct hashes, and each sheet's four-view legibility, source morphology, consistency and actually varied treatment. Use a labeled contact sheet plus native-size crops. Regenerate failed slots from the original if reasonable; otherwise report drafts and unmet gates honestly. Deliver all ten individual files in chat, not a combined contact sheet.

## Mechanical-source style and topology checks

- If a glossy spacecraft source anchors the first sheet to CGI, make a nonfigurative matte-gouache style swatch with OpenAI, use it as style-only `image_url`, and supply the ORIGINAL vehicle as the geometry-only reference in every fresh generation. Calibrate one sheet for actual painted surface transitions before continuing. Forbid swatch background stains and shape/color blobs; retain the source hull and pod construction rather than copying swatch geometry.
- Count outboard pods separately from central rear nozzles in every full view. In a true side view, explicitly retain the near-side pod overlapping the rear flank as well as any visible far-side pod; generation can silently omit the near pod to expose hull vents. Replace that failed sheet directly from original references. Distinguish side profile from top-down plan views; do not certify exact engineering turnarounds or pixel-exact part placement from generative images.

## Resources
- `references/authoritative-brief.md` - mandatory full user brief; read before image generation.
