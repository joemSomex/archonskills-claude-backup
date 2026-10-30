---
name: hat-front-closeup
description: Use when making pose-matched close-up portraits with a referenced hat.
version: 1.0.0
author: Somex Studios
metadata:
  hermes:
    tags: [Hat, Portrait, Image Generation, Cinematic, Reference Images]
---

# Hat Pose-Matched Close-up

Generate four independent pose-matched close-up portraits from exactly five ordered reference images.

## Required reference order

Treat the five images as follows and never exchange their roles:

1. Character face and identity reference.
2. Hat design reference.
3. Background reference.
4. Pose-only reference.
5. Pose-only reference.

Never import identity, facial features, wardrobe, hats, backgrounds, lighting, or colors from images 4–5.

## Required prompt

Before generation, read `templates/prompt.md` and use its Chinese instruction verbatim. Do not rewrite, shorten, correct, translate, or paraphrase it. Add only a short per-generation pose variation when needed to make the four outputs distinct without changing the locked requirements.

## Workflow

1. Analyze all five references and confirm their ordered roles.
2. Use all five original references for every generation. Never feed a generated output back as a reference.
3. Generate exactly four separate PNG files, each on a new generation slate.
4. Keep every output in a 2:3 vertical composition. Never create a collage, grid, contact sheet, picture-in-picture, or combined layout.
5. For each output, choose either image 4 or image 5 as the independent pose reference. Preserve its head angle, facial orientation, gaze direction, shoulder-neck relationship, body orientation, and pose without mirroring, reversing, or forcibly turning the subject front-facing. Vary only the selected pose and subtle expression while preserving face identity, hat design, background, framing, camera treatment, and natural-light requirements.
6. Inspect every output. Regenerate any image that fails a locked criterion.

## Approved pose tendencies

For comparable three-quarter or side-facing hat portraits, prioritize these proven compositions when compatible with the supplied pose references:

- A restrained three-quarter side view with the head slightly lowered, gaze following the turn, shoulders relaxed, and both hands out of frame.
- A three-quarter side view with a slight lowered head tilt, one hand naturally touching the brim edge without covering the face or hat mark, and a calm, focused gaze from beneath the brim. This restrained expression is preferred for wind-swept portraits.

Avoid making every variation upright or visibly raising the chin; preserve the quieter downward head angle when the pose references support it.

## Verification

Confirm before delivery:

- Exactly four separate PNG files exist.
- Each file is 2:3 portrait.
- The face matches image 1 and the hat matches image 2.
- Image 3 remains the background.
- Images 4–5 influence pose only.
- The portrait is framed above the chest and its head angle, facial orientation, gaze direction, shoulder-neck relationship, and body orientation match either image 4 or image 5 without mirroring or blending the two poses.
- The complete hat is visible and uncropped.
- Lighting is natural-only, with no added artificial-light look.
- The requested restrained anamorphic characteristics are visibly present.
- No collage, watermark, or unintended text appears.
