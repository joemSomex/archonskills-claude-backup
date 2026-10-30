---
name: map-creation
description: "Use when 'Map Creation.' requests five overhead maps."
version: 1.0.0
author: Somex Studios + Hermes Agent
license: Proprietary
metadata:
  hermes:
    tags: [map-design, environment, image-generation]
    related_skills: [reference-driven-image-generation]
---

# Map Creation

## When to Use

When the user says `Map Creation.` with three images, execute the five-map workflow without asking for confirmation. Load `references/authoritative-brief.md` **in full before generating**; it preserves the user's original prompt verbatim. Treat `@image1`, `@image2`, `@image3` as environment-design references only, resolving earlier attachments explicitly named by the user rather than assuming only the latest message's images exist. Inspect and classify all three originals. If they cannot be recovered, ask for the missing reference instead of substituting unrelated imagery. Do not import their exact layouts or landmarks. The interchangeable additional-description module is optional; apply a user-supplied module only if it does not conflict with the locked camera, center, edges, style, aspect ratio, or count.

## Execute

Create **exactly five separate, independently generated PNG maps**, each directly conditioned on all three ORIGINAL references and the full brief, never on a prior generated map. Use ChatGPT/OpenAI image generation only for this user's images; never Claude, and never Higgsfield without explicit instruction. Reserve a meaningfully different geography, central-ground shape, perimeter topology, routes, elevation, destruction, and light distribution for each of the five; keep a coherent broader world. No composite/contact sheet as a deliverable.

Before accepting each image, inspect it at useful scale. The optical axis must read as **90-degree direct overhead**, with roof planes and ground visible and no horizon, facades, oblique/isometric geometry, or tilted aerial camera. The central 40-55% must remain a contiguous, traversable, visually open battlefield; put complex architecture and storytelling on the asymmetric perimeter and keep flanking routes legible. The result must have dimensional painterly animated surface treatment, not photography, satellite imagery, generic CGI, or a diagram. If a shared camera/style error appears, correct and inspect one generation before completing the remaining slots.

Verify five PNG files, exact 16:9 geometry, distinct hashes **and visually distinct layouts**. If a near-16:9 canvas needs normalization, crop only safe margins without distortion and re-inspect. Save a source-linked manifest recording each generation, QA and any failed replacements. Deliver all five standalone files in chat, candidly labeling any remaining camera/style limitations rather than claiming compliance from hashes alone. If the image provider refuses a request, do not work around that refusal or switch providers.

## Resources

- `references/authoritative-brief.md` - mandatory verbatim user prompt and every acceptance criterion; read it in full for each invocation.
