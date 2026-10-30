---
name: card-design
description: "Use when creating card visuals or 卡牌设计."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [card-design, image-generation, dark-fantasy, 卡牌设计]
    related_skills: [reference-driven-image-generation]
---

# Card Design / 卡牌设计

## When to Use

Use for requests such as:
- card design, dark-fantasy card visual, three vertical card images
- 卡牌设计、暗黑幻想卡牌、生成三张竖版卡牌图、写卡牌指令

Reply in the language used by the requester. Preserve supplied prompt wording, reference roles, names, filenames, and locked terminology exactly unless the user explicitly asks to revise them.

## Required Template

Before writing a reusable card prompt or generating images, read `templates/generic-card-prompt-zh.md`. Treat its body as the canonical Chinese prompt. Copy it verbatim unless the user explicitly requests a change; fill only the blank `人物动作：` line when an action is supplied.

## Reference Roles

Use four references with strict role boundaries:
1. Figure 1: identity, face, hair, skin tone, wardrobe construction, and materials only.
2. Figure 2: background, spatial structure, palette, and environmental texture only.
3. Figures 3–4: art style, particles, grain, printing texture, material highlights, and dramatic lighting only.

Inspect visible content before assigning roles because platform attachment order can change. Ignore and forbid typography, numbers, logos, symbols, UI marks, watermarks, and signatures visible in any style reference.

## Workflow

1. Determine whether the user wants only the written instruction or finished images.
2. For a written instruction, return the canonical template in chat and leave one blank line after `人物动作：` unless the user supplied an action.
3. For generation, use all four original references on every image call. Use Figure 1 as the identity/edit base and Figures 2–4 as additional references.
4. Generate exactly one standalone image per call. Make three separate calls; never request or accept a collage, contact sheet, triptych, multi-view sheet, or character board as a deliverable.
5. Keep identity and wardrobe consistent across all three outputs. Vary only particle placement, grain, background light traces, and other non-identity details unless the user requests different actions.
6. When the user identifies one variant as having the preferred lighting, treat that variant as the accepted lighting calibration for subsequent images in the same visual series. Match its facial exposure, highlight placement, color temperature, shadow depth, and light intensity without copying unrelated pose or composition details.
7. When the user identifies one variant as having the preferred background, treat that variant as the accepted background calibration for subsequent images in the same visual series. Match its palette, glow placement, light-trace density, particle depth, negative space, and background contrast without copying unrelated pose, anatomy, or identity drift.
8. When the user prefers different components from different variants, preserve those preferences independently and combine them in the next iteration—for example, copy lighting calibration from one image and pose/anatomical arrangement from another without importing unrelated details.
9. If a custom action contains count-sensitive limbs, props, or appendages, state the exact visible total and traceable image-space placement before the canonical prompt. Do not let extra parts leak from the references.
10. Use portrait generation, then make a minimal safe crop to an exact integer 11:20 canvas when needed. Prefer 924×1680 when source dimensions allow it without damaging the composition. Never independently scale width and height to force a crop into 11:20: it distorts body and face proportions. If a tighter anatomical crop would require stretching or clipped hands, regenerate the composition or disclose that criterion as unmet rather than padding/cropping then anisotropically resizing.
11. Deliver only the three accepted standalone files, not the internal contact sheet.

## Verification

Before delivery, verify:
- Exactly three files exist and their cryptographic hashes differ.
- Each file is PNG and has an exact 11:20 pixel ratio.
- Each image is standalone and contains one intended subject, not a collage.
- Identity, face, hair, skin tone, wardrobe structure, and materials match Figure 1.
- Background follows Figure 2; style and lighting follow Figures 3–4 without copying their typography or symbols.
- The face is readable and unobscured.
- The subject remains sharply focused from the face through the lower frame; lower clothing, arms, hands, props, and silhouette edges show no depth-of-field blur, motion blur, feathering, fog, glow wash, particle occlusion, or dissolving edge.
- No text, letters, numbers, punctuation, logos, watermarks, signatures, runes, UI elements, or other recognizable symbols appear.
- No card border, metal frame, decorative frame, frame line, card-slot structure, outer frame, or white margin appears unless the user explicitly asks for one.
- Any user-specified action, direction, count, and placement visibly pass inspection.

If one output fails, regenerate only that output from the original references. Do not use another generated image as its reference unless the user explicitly requests iterative editing.
