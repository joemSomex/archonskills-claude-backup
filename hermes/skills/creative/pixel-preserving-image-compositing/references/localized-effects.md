# Localized additive effects

Use this recipe when the user wants particles, glow, haze, sparks, grain, or another additive effect in one region while the source face, framing, crop, lighting, and existing design must remain unchanged.

## Decision rule

Use deterministic raster editing rather than image-to-image generation whenever unchanged content is a hard requirement. Generative editors can redraw identity, pose, crop, and lighting across the full frame even when prompted not to.

## Procedure

1. Decode the source once with Pillow and keep that decoded RGB/RGBA image as the comparison baseline.
2. Measure the permitted edit region in original pixel coordinates. Prefer a hard rectangle for negative-space additions; use a grayscale mask for irregular regions.
3. Create a same-size transparent RGBA overlay. Draw only the new effect on this overlay.
4. Match the nearby source effect rather than inventing a new style:
   - sample its dominant colors;
   - reproduce particle-size and opacity ranges;
   - follow its flow direction and density gradient;
   - taper alpha near path ends and mask boundaries;
   - use a faint blurred under-layer beneath crisp particles so the effect feels embedded.
5. Hard-mask the overlay to the allowed region before compositing. Keep particles clear of faces, eyes, product marks, and other locked elements.
6. Alpha-composite overlay over the decoded source and save as PNG at the original dimensions.
7. For a second reference used as a faint background texture, cover-resize and center-crop it to the target canvas, then use a low-opacity screen blend through a combined mask: `allowed spatial region × dark-source luminance`. This keeps luminous strands and bokeh visible in black negative space without repainting the subject.
8. For broad colored glow, render the radial or elliptical glow on its own RGBA layer, blur that layer, and then multiply its final alpha by the same combined background mask. Mask after blur because blur expands beyond the original bounds and can relight the face or hair.
9. Verify zero changed pixels outside the allowed region with `scripts/verify_region_preservation.py`. Also inspect the full diff bounding box when a subject-protection contour is stricter than the rectangular edit region.
10. Inspect a temporary contact sheet when producing variants. Compare density, balance, negative space, accidental rings/wings/symbols, texture visibility, glow spill, and whether every variation still satisfies the same locked framing. Never deliver the contact sheet.

## Particle-arc guidance

For a subtle half-enclosure, use one or more open cubic Bézier paths outside the subject contour. Scatter narrow particle lanes around each path normal, fade density at both ends, and leave the arc visibly open. Vary density emphasis by region rather than changing the base image: top-heavy, middle-weighted, bottom-heavy, or uniformly sparse.

## Pitfalls

- Do not call a full-frame image generator for a one-region additive effect — the model can silently alter identity and composition.
- Do not blur the final composite globally — blur only a duplicate of the overlay, or locked source pixels will change.
- Do not alpha-composite a blurred glow directly over the full frame — its feathered edge can cross the intended boundary; re-mask the blurred alpha against the protected background before compositing.
- Do not place a semi-transparent effect reference uniformly over the target — use screen blend plus spatial and luminance masks so dark background receives the effect while skin, hair, and existing bright particles remain locked.
- Do not verify against the compressed source file bytes — compare decoded pixel arrays in the same color mode.
- Do not let procedural particles form letters, numbers, logos, complete halos, wings, or other semantic shapes when the user asked for abstract effects.
