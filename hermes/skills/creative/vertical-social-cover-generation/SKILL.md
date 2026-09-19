---
name: vertical-social-cover-generation
description: Use when generating text-free vertical social cover art.
version: 1.0.0
author: Somex Studios
metadata:
  hermes:
    tags: [Cover Art, Social Media, Image Generation, Portrait, Poster]
---

# Vertical Social Cover Generation

Generate six independent vertical social-media cover images from identity and design references, with stable identity, meaningfully different layouts, and no text by default.

## Reference roles

1. Treat images 1–2 as two views of the same subject unless the user says otherwise. Use the frontal view for overall facial structure and the profile view for nose, brow, cheekbone, jaw, ear, and hair geometry.
2. Treat image 3 onward as design-only references. Extract composition, subject scale, negative space, lighting, color, depth, texture, and visual effects; never import their people, identity, wardrobe, props, text, symbols, logos, or narrative content.
3. Use every original reference in every generation. Never feed a generated cover back as a reference.

## Workflow

1. Analyze the identity views and write a single internal identity lock: facial proportions, eye color, nose, lips, jaw, hair, age impression, and distinguishing traits.
2. Analyze each design reference only for reusable visual language. Explicitly ignore all typography and symbolic graphics because poster references strongly bias image models toward recreating them.
3. Read `templates/dual-angle-no-text-cover.md` and retain its locked role separation and no-text rules.
4. Plan six layouts before generation. Each layout must differ in at least three structural dimensions: face angle, subject position, crop, scale, negative space, depth, lighting direction, foreground treatment, or effects. Color changes alone do not count.
5. Generate six times from a new slate, one PNG per call. Keep one clear subject only; do not create a front/profile pair, reflection double, duplicate face, or second person.
6. Default to no text or symbols unless the user explicitly requests them. Ban text and symbol-like content from clothing, props, background, particles, borders, and interface-style decoration—not only from title areas.
7. Verify each output individually for identity, duplicate faces, unintended characters, text, pseudo-text, logos, watermarks, symbols, and layout compliance. Then make an internal contact sheet to compare all six for real compositional diversity; never deliver the contact sheet.
8. Verify exact 3:4 dimensions programmatically. Prefer a native 3:4 result such as 1086×1448. If the provider returns another portrait ratio, keep the subject inside a centered 3:4 safe area, crop to an exact 3:4 integer size, and inspect again after cropping.
9. Deliver exactly six separate PNG files with short layout labels. Never deliver a collage, grid, contact sheet, or combined board.

## Visual rules

- Keep the subject's identity stable across frontal, profile, three-quarter, high-angle, and low-angle views by combining both identity references instead of copying only one view.
- Use abstract particles, smoke, light strands, glass blur, or geometric occlusion only when they remain non-semantic. Do not let effects form glyphs, emblems, UI marks, or pseudo-writing.
- Preserve a complete, natural face unless deliberate cropping is part of the approved layout; never create double eyes, fused profiles, or a second readable face in reflection or dissolution.
- Keep clothing plain and unbranded by default so design references cannot leak logos or typography into the output.

## Verification

Confirm before delivery:

- Exactly six independent PNG files exist.
- Every file is exactly 3:4 portrait.
- Images 1–2 resolve to one stable identity, not two people.
- Image 3 onward influences visual design only.
- The six compositions are structurally distinct, not recolors or minor crops.
- No text, letters, numbers, punctuation, logos, watermarks, pseudo-text, or symbol-like graphics appear unless explicitly requested.
- No output contains a duplicate face, second person, collage, or picture-in-picture.

## Resources

- `templates/dual-angle-no-text-cover.md` — reusable Chinese prompt scaffold for one subject supplied as frontal and profile references.
- `references/layout-recipes.md` — optional composition recipes for six genuinely different cover layouts.
