---
name: pixel-preserving-image-compositing
description: Use when editing one image without changing other pixels.
version: 1.0.0
metadata:
  hermes:
    tags: [Image Editing, Compositing, Typography, Pixel Preservation, QA]
---

# Pixel-preserving image compositing

Transfer or add text, logos, particles, lighting accents, and other graphic elements without regenerating the artwork or altering unrelated target pixels.

## Procedure

1. **Classify the references by visible content.** Inspect every attachment and identify the element source and the target canvas. Trust visible content over attachment order because messaging platforms can reorder files.
2. **Choose deterministic raster editing when preservation is locked.** If the user says to keep the face, framing, crop, pose, lighting, or existing artwork unchanged and modify only one region, do not use image-to-image generation: it can redraw the entire frame despite preservation language. Use an alpha overlay or literal pixel transfer confined to a measured mask. For additive particles or glow, read `references/localized-effects.md`.
3. **Choose literal compositing when source styling is locked.** If the user requires the same font, texture, color, glow, cracks, particles, or effects, extract or procedurally match the original pixels. Do not retype typography or regenerate the image, because either route changes locked styling and unrelated pixels.
4. **Measure all originals.** Read actual pixel dimensions programmatically; visual-analysis dimensions may be approximate. Locate the complete source element and allowed edit region in those coordinates.
5. **Crop generously, then isolate the element.** Include the complete glow and decorative effects. Remove only the source background with an alpha mask suited to the artwork. For luminous red typography on black, use red-channel excess plus a brightness floor; see `references/typography-transfer.md`.
6. **Composite only inside the allowed region.** Scale transferred elements uniformly and keep their internal layout intact. For generated particles or accents, draw on a transparent overlay, hard-mask it to the permitted region, then alpha-composite it over the decoded source. For broad glow or a semi-transparent background texture, combine the spatial edit mask with a luminance-derived dark-background mask and apply that mask after every blur; otherwise soft alpha can spill onto the face or hair and silently change the locked lighting. Preserve canvas dimensions and aspect ratio.
7. **Verify preservation deterministically.** Compare output against the decoded base and require zero changed pixels outside the edit rectangle or mask. Run `python scripts/verify_region_preservation.py SOURCE OUTPUT --rect X1,Y1,X2,Y2`; confirm `outside_changed_pixels=0` and equal dimensions.
8. **Run visual QA on the final file.** Check requested content, edge taper, density, material match, negative space, and subject clearance. Reject clipping, hard mask boundaries, pasted-on glow, unintended halos, semantic shapes, and subject overlap. For typography, also check every expected character, numeral, subtitle, divider, and glow.
9. **Deliver only accepted independent files.** State briefly which region changed, what remained pixel-identical, the verified dimensions, and attach each requested file separately.

## Always-on rules

- Route any “change only this region; keep everything else identical” request to deterministic compositing rather than generative editing, because generative edits can change identity, crop, and lighting globally.
- Preserve exact source styling by transferring pixels or procedurally matching local visual statistics rather than approximating the effect through full-frame regeneration.
- Do not alter the target image outside the requested overlay area; prove this with a pixel-difference check. When the user locks the face, framing, crop, and lighting, require the pixel-difference bounding box to begin outside the protected subject boundary, not merely outside a broad half-frame rectangle.
- Keep the target canvas size and aspect ratio unchanged unless the user explicitly requests resizing.
- Inspect references by content, not filenames or upload order.
- Treat every visible part of a text lockup as required, including issue numbers, subtitles, divider lines, glow, and nearby energy effects.
- For multiple requested variants, render every file independently from the same untouched base and vary only explicit placement/scale parameters; never composite a later variant from an earlier output, and verify the final standalone-file count programmatically.
- Never claim success after a single render; deterministic preservation and visual completeness are separate gates.

## Resources

- `references/typography-transfer.md` — isolate and transfer styled typography.
- `references/localized-effects.md` — add particles, glow, and similar effects while preserving all pixels outside a region.
- `scripts/verify_region_preservation.py` — verify dimensions and zero changed pixels outside an allowed rectangle.
