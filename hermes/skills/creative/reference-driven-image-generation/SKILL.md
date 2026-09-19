---
name: reference-driven-image-generation
description: Use when generating images from multiple references.
version: 1.0.0
metadata:
  hermes:
    tags: [Image Generation, Reference Images, QA, Portrait]
---

# Reference-Driven Image Generation

Produce independent, role-faithful images from several references without allowing attachment ordering, identity leakage, or batch-layout errors to corrupt the result.

## Procedure

1. **Recover the complete active brief.** When resuming an interrupted task, read the latest relevant session and continue only the request the user has now explicitly reactivated. Reuse the original reference files and successful outputs; do not repeat completed generations or attachment-ingest side effects.
2. **Classify references by visible content before prompting.** Analyze every original image and assign its semantic role: identity, product/design, background, pose, wardrobe, or style. If filenames, platform attachment notes, and visible content disagree, trust the visible content and build a canonical ordered list for the generator. Discord can present attachment paths in an order different from the visual upload sequence, so never map roles from list position alone.
3. **Keep role boundaries explicit.** State which attributes each reference may contribute and which it must not contribute. Pose-only references must not leak identity, clothing, lighting, background, or color; product references must control the product design rather than the face or pose.
4. **Preserve locked prompt text exactly.** Load any required prompt template and include it word for word. Add only a short generation-specific suffix for the requested pose, expression, motion, or variation; do not paraphrase the locked body.
5. **Choose generation versus deterministic editing before calling the model.** Use `image_generate` when the user wants a new rendition and some global variation is acceptable. If the user requires the original face, crop, framing, lighting, or unrelated pixels to remain identical while changing only one region, route to `pixel-preserving-image-compositing`; image-to-image generation can redraw the full frame despite preservation language.
6. **Use all original references on every generation.** Put the identity reference in `image_url` when a generative edit base is appropriate and pass the remaining originals in `reference_image_urls` in canonical semantic order. Never feed a generated output into a later generation unless the user explicitly requests iterative editing.
7. **Generate one file per call.** Even when the locked prompt says to create several images, append a concise instruction such as “generate only image 1 as one standalone PNG in this call,” then make a fresh `image_generate` call for each output. This prevents collages, contact sheets, and repeated crops while preserving the required prompt verbatim.
8. **Make variations traceable.** Tie each output to exactly one pose reference and one small variation. Do not blend two pose references in a single image, mirror the pose, or change gaze direction merely to increase variety.
9. **Run visual QA on every output.** Inspect identity, product geometry and marks, background, pose direction, framing, motion direction, lighting, anatomy, crop, unwanted text, and collage artifacts. Regenerate only failed outputs from the original references.
10. **Verify file properties programmatically.** Confirm the requested count, file existence, PNG format, pixel dimensions, and exact aspect ratio before delivery. Visual inspection alone cannot prove encoding or dimensions.
11. **Deliver only the accepted standalone files.** Keep the report short: what was completed, what was verified, and the individual media attachments.

## Always-on Rules

- Never infer reference roles solely from attachment order; classify by visible content because messaging platforms may reverse or reorder attachments.
- Never let pose-only references influence identity, wardrobe, product design, background, lighting, or color.
- Never satisfy a multi-image request with a collage or grid; use independent generation calls and independent files.
- Never use generated images as references for subsequent variants unless iterative editing is explicitly requested.
- Preserve user-specified motion direction in image coordinates, such as “hair toward image-right,” and verify the visible result rather than trusting prompt wording.
- Treat names of cameras, lenses, and lighting styles as requirements for visible characteristics, not as proof that the output complies.
- Do not claim completion until both visual criteria and deterministic file properties pass.
- Do not use generative editing when the acceptance criterion is zero change outside a local region; use pixel-preserving compositing and prove the unchanged area with a diff.
