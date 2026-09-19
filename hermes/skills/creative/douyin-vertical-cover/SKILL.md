---
name: douyin-vertical-cover
description: Use when generating text-free Douyin vertical covers.
version: 1.1.0
author: Somex Studios
metadata:
  hermes:
    tags: [Douyin, Cover, Poster, Image Generation]
---

# Douyin Vertical Cover

Generate six independent 3:4 text-free Douyin cover images from two identity references and one or more visual-design references.

## Required reference order

1. Frontal face and identity reference.
2. Side/profile reference of the same person.
3. All remaining images are design-only references.

Treat images 1–2 as one person. Use later references only for composition, layout, lighting, depth, materials, color atmosphere, and visual effects. Never import their identities, faces, text, symbols, logos, clothing graphics, or franchise-specific content.

## Required prompt

Before generation, read `templates/prompt.md` and use its Chinese instruction verbatim. Do not rewrite, shorten, correct, translate, or paraphrase it. Add only one distinct composition direction for each generation without weakening any locked requirement. Apply a subject or genre only when the user explicitly supplies one.

## Workflow

1. Analyze every reference and confirm its assigned role.
2. Use all original references in every generation. Never use a generated image as a reference for another.
3. Generate exactly six separate PNG files, each from a fresh generation slate.
4. Keep every output at an exact 3:4 portrait ratio.
5. Make all six compositions materially different through subject angle, placement, crop, spatial structure, depth, negative space, lighting, color relationships, or visual direction. Color, filter, background, or minor crop changes alone do not count.
6. Keep one stable character identity synthesized from images 1–2. Never duplicate, split, reflect, or repeat a recognizable face.
7. Inspect every output and regenerate failures.

## Verification

Confirm before delivery:

- Exactly six independent PNG files exist.
- Every file is exactly 3:4 portrait.
- The same single identity from images 1–2 appears in all six.
- Every image has a meaningfully different composition.
- No text, letter, number, punctuation, logo, watermark, signature, emblem, glyph, interface, icon, button, pseudo-text, or character-like pattern appears anywhere unless the user explicitly requests it.
- No duplicated face, second person, collage, grid, contact sheet, picture-in-picture, or combined layout appears.
- Clothing, props, accessories, and environmental details remain free of text, logos, numbers, and symbols unless explicitly requested.
