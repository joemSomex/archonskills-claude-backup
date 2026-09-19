---
name: cinematic-character-generation
description: "Generate ten unique cinematic character blends."
version: 0.7.0
author: Somex Studios, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Character, Image Generation, Cinematic, Portrait]
    related_skills: []
---

# Cinematic Character Generation

Generate ten separate character images by blending the user’s reference images.

## Required Prompt

Add this text to the image-generation prompt word for word:

```text
Create separate 10 unique PNG files. Create 10 different generations. Restart and do a new generation. New slate; start new. Each generation should be individually unique and different from the others. 9:16; ensure a realistic camera, photorealistic shot/image. Shot on ARRI Alexa Mini LF (or Alexa 35), anamorphic feel. Kowa Cine Prominar 2x Anamorphic Lens. True anamorphic traits: slight edge distortion, oval bokeh, gentle film grain, realistic halation on tiny highlights, natural bloom, controlled contrast, cool dark tone, minimal dark lighting. Create 10 individual file generations.
```

Do not rewrite, shorten, correct, or paraphrase this text.

## Camera Treatment Enforcement

The required camera and lens treatment overrides the references’ lighting, color grade, and background brightness whenever they conflict.

Translate the camera wording into visible image characteristics in every generation:

- Cool, dark, low-key grade with minimal motivated lighting.
- Controlled contrast with readable skin and shadow detail; do not crush the face into black.
- Slight optical softness and restrained distortion toward the frame edges.
- Clearly oval out-of-focus highlights.
- Fine organic film grain rather than digital noise.
- Subtle halation on small bright points and natural optical bloom.
- Smooth highlight roll-off without clipped digital whites.
- A few small background practical lights so oval bokeh, halation, and bloom are visible.
- No bright beauty lighting, plastic skin, excessive sharpness, generic CGI finish, heavy flare, or default orange-and-teal grading.

Camera and lens names alone do not satisfy the requirement. The treatment must be visibly present in the generated image.

## Procedure

1. Analyze every reference image with `vision_analyze`.
2. Identify the visible facial, physical, clothing, material, and design traits in each reference.
3. Determine the references’ shared baseline: apparent age range, shot framing and crop, camera angle, pose style, and wardrobe language. Treat these shared qualities as locked unless the user explicitly requests a change. Preserve shared background structure when compatible, but the required cool-dark camera treatment overrides reference lighting, color grade, and background brightness.
4. Create ten different facial-identity blend directions using traits from all references while preserving the shared baseline.
5. Each blend must produce a new character rather than copy one reference. Create uniqueness through facial synthesis and fine character details—not by inventing a different age, ethnicity, shot size, pose, wardrobe category, or environment.
6. Do not assign an age outside the range visibly supported by the references. If the references appear to share the same age range, preserve it in all ten generations.
7. Match the source framing. If the references are all head-and-shoulders portraits, all ten outputs must remain head-and-shoulders portraits with comparable camera distance, crop, and subject scale.
8. Run `image_generate` ten separate times with `aspect_ratio: portrait`.
9. Start every generation from a new slate.
10. Use the original reference images in every generation. Never use a generated image as a reference for another generation.
11. Add the user’s character description after the required prompt.
12. Reinforce the visible camera treatment in each generation direction: low-key motivated light, oval bokeh, edge softness/distortion, fine grain, restrained halation, natural bloom, controlled contrast, cool-dark grade, and smooth highlight roll-off. Include small background practical lights so the optical traits can be evaluated.
13. After generation, inspect every output with `vision_analyze`. Reject and regenerate any image that merely names the camera treatment in its prompt but does not visibly show it.
14. Deliver ten individual PNG files, labeled Generation 1 through Generation 10.

## Verification

Before delivery, confirm:

- Exactly ten separate PNG files were generated.
- Every image uses a 9:16 portrait format.
- Every image is photorealistic.
- Every image blends traits from the supplied references.
- The ten generations have distinct newly synthesized facial identities without copying one source.
- Apparent age remains within the range supported by the references.
- Shared source framing, crop, camera angle, pose style, and wardrobe language are preserved unless the user requested changes.
- Required camera treatment overrides conflicting reference lighting, grade, and background brightness.
- Every image visibly demonstrates cool-dark low-key lighting, controlled contrast, oval bokeh, fine grain, restrained halation, natural bloom, and smooth highlight roll-off.
- No image uses bright beauty lighting, plastic skin, excessive digital sharpness, heavy flare, generic CGI rendering, or default orange-and-teal grading.
- No output is a collage, contact sheet, or reused crop.
