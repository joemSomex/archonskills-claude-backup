---
name: clothing-tryon-render
description: Use for 服装上身效果图 and clothing-on-model renders.
version: 1.0.0
author: Somex Studios
metadata:
  hermes:
    tags: [Clothing, Portrait, Image Generation, Fashion, Reference Images]
---

# Clothing Try-On Render

Generate three independent clothing-on-model images from exactly five ordered reference images. Trigger on requests such as “服装上身效果图”, “服装试穿效果图”, “调用服装上身效果图技能”, and “clothing try-on render”.

## Required reference order

Treat the five images as follows and never exchange their roles:

1. Character face and identity reference.
2. Clothing design reference.
3. Background reference.
4. Pose-only reference.
5. Pose-only reference.

Never import identity, facial features, hairstyle, skin tone, clothing, background, lighting, or colors from images 4–5.

## Required prompt

Before generation, read `templates/prompt.md` and use its Chinese instruction verbatim. Do not rewrite, shorten, correct, translate, or paraphrase it. Add only a short per-generation pose variation when needed to make the three outputs distinct without changing the locked requirements.

## Workflow

1. Analyze all five references and confirm their ordered roles.
2. Use all five original references for every generation. Never feed a generated output back as a reference.
3. Generate exactly three separate PNG files, each on a new generation slate.
4. Keep every output in a 2:3 vertical composition. Never create a collage, grid, contact sheet, picture-in-picture, or combined layout.
5. Preserve image 1 identity, image 2 clothing design, image 3 background and natural light, and use images 4–5 for pose only.
6. Frame the subject from the hips upward. Keep clothing construction, fit, materials, graphics, trims, and proportions faithful to image 2.
7. Inspect every output. Regenerate any image that fails a locked criterion.

## Verification

Confirm before delivery:

- Exactly three separate PNG files exist.
- Each file is 2:3 portrait.
- The face and identity match image 1.
- The clothing matches image 2 without redesign, simplification, or structural errors.
- Image 3 remains the background with its natural-light logic.
- Images 4–5 influence pose only.
- Every portrait is framed from the hips upward.
- Fabric thickness, drape, folds, tension, compression, and reflections look physically plausible.
- Lighting is natural-only, with no strobe, flash, flicker, flashlight, studio fill, rim light, or reflector effect.
- The requested restrained anamorphic characteristics are visibly present.
- No collage, watermark, or unintended text appears.

## Resources

- `templates/prompt.md` — mandatory exact Chinese generation prompt; read before every generation.
