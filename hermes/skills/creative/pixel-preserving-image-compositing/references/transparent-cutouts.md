# Transparent character cutouts

Use this recipe when the user wants an existing character isolated on transparency while preserving identity, pose, clothing, lighting, glow, hair, and particles.

## Decision rule

- Use deterministic segmentation or masking when the source already contains the exact character. Do not use image-to-image generation: preservation wording does not stop a generator from redrawing the face, pose, clothing, or particle silhouette.
- Treat a separate “desired result” image as a composition/edge-quality reference only unless the user explicitly asks to copy its character design.
- When the user requests a **new pose or stylized avatar** from a character sheet, generate that new rendition first, then extract its background deterministically. Label it a generated likeness, not a pixel-preserving cutout of the sheet.

## Newly generated avatars on transparent backgrounds

1. Generate one subject per source sheet on a **uniform saturated chroma-key color absent from the clothing and hair** (for example, vivid green for dark armor and brown jackets). Forbid sheets, shadows, floor, gradient and glow on the key; a merely green-looking backdrop may have uneven RGB, so sample its corners before choosing thresholds.
2. Estimate soft alpha from key dominance rather than binary color deletion. For a green key, calculate `G - max(R, B)` and map background values to alpha zero, solid subject to alpha 255, retaining intermediate alpha on hair wisps. Calibrate the transition against the measured key RGB and the particular source; do not hard-code one threshold for every generator output.
3. Remove key contamination from partially transparent edge RGB by unmatting against the sampled key color, then locally despill green in the hair-edge region. Inspect before/after over dark **and** light mattes; a valid alpha channel can still leave vivid green hair strands or a colored halo, while over-aggressive despill can erase fine locks.
4. Verify `PNG` + `RGBA`, alpha extrema `0..255`, nonzero intermediate alpha for soft edges, and that the transparent field contains no opaque key remnants. If sending on Telegram, package the checked PNGs in a ZIP or explicitly send as documents, then verify each archived byte stream matches the PNG; a photo attachment can be delivered as flattened JPG.

## Preferred tool workflow

When a dedicated background-removal service is available, use it before attempting custom masks:

1. Upload the original source bytes with the media upload tool and PUT the file to its presigned URL.
2. Require the PUT to succeed before confirming the media. If the presigned upload fails, request one fresh upload URL and retry once; never confirm a failed upload.
3. Confirm the uploaded image, then run the background-removal tool on that confirmed media ID.
4. Download the completed PNG and inspect its alpha bounds and retained effects. Compare the cutout directly against the source at the same scale: every windblown lock, flyaway, detached wisp, backlit hair, and semi-transparent tip must remain. Reject the remover output if low-contrast hair was classified as haze or background. Do not substitute an image-generation edit: it can produce a convincing but different character and introduce colored edge artifacts.
5. If the automatic remover erodes hair, refine or rebuild the alpha mask from the original pixels with soft matting; do not reconstruct missing hair with a generator. Preserve mixed hair/background pixels with partial alpha, because aggressive decontamination and hard mask contraction delete fine strands.
6. Crop by the nonzero-alpha bounding box, scale uniformly onto the requested transparent canvas, center horizontally, and bottom-align only after removal. This keeps the original character pixels and prevents the model from inventing a new square composition.

## Procedure

1. Read the source dimensions and color mode before editing.
2. Remove text, UI, frames, gradients, haze, and the scene background through one alpha mask. Preserve the source RGB pixels for the character and retained effects.
3. Build soft alpha for fine hair, glow, and loose particles. Inventory the source hair silhouette before masking—main mass, windblown locks, flyaways, detached wisps, backlit strands, and translucent tips—and require every item to survive. Treat hair overlapping haze or similar-colored background as hair, not cleanup residue. Keep gaps between particles transparent; do not merge them into a continuous fiery outline or solid halo.
4. Keep the main face, hair mass, torso, and clothing near opaque. Only edge antialiasing, translucent glow, and originally translucent particles should carry intermediate alpha. Interpret “clean edges” as color decontamination without alpha erosion; never contract the mask merely to eliminate a fringe.
5. Compare the source and cutout side by side over both light and dark mattes before layout. Reject missing or shortened strands, colored edge contamination, globally translucent subjects, and any face, pose, clothing, or hair geometry change. A plausible silhouette is insufficient—the visible hair geometry must match the source.
6. Compute the nonzero-alpha bounds. Uniformly scale the cutout to the requested canvas, center it horizontally, align the torso to the bottom edge when requested, and add transparent padding for the head, hair, and particles. Never stretch or crop to force a fit.
7. Resize RGBA only after masking, using a high-quality uniform resampler. Save as PNG without flattening.
8. Verify the file programmatically:

```python
from PIL import Image

im = Image.open(output_path)
assert im.format == "PNG"
assert im.mode == "RGBA"
assert im.size == (2048, 2048)  # replace with requested size
alpha = im.getchannel("A")
lo, hi = alpha.getextrema()
assert lo == 0 and hi == 255
hist = alpha.histogram()
assert sum(hist[1:255]) > 0      # soft hair/glow/particles survived
assert hist[255] > 0             # solid subject pixels remain opaque
```

9. Inspect the PNG over light, dark, and checkerboard previews generated by alpha-compositing the RGBA file onto each matte. Never judge a cutout from a renderer that displays RGB while ignoring alpha: background removers can leave the original background, UI, and text in RGB beneath fully transparent pixels, making a valid mask look unedited. Verify unwanted regions are actually alpha 0, then reject dark/white/color halos, clipped particles, opaque background residue, a globally translucent subject, or any missing hair strand visible in the source. Do not use broad hue clamping as a substitute for a correct matte; it can recolor legitimate hair glow and particles while leaving the masking error unresolved.

## Delivery gate

Report the verified size, PNG/RGBA mode, and real alpha channel. Do not claim pixel preservation when a generative model redrew the character; either redo the extraction deterministically or state the limitation plainly.
