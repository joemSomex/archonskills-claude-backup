# Typography transfer recipes

## Red or orange luminous text on a dark background

Use Pillow to crop the complete lockup, build alpha from channel dominance, resize uniformly, and alpha-composite onto the base.

```python
from PIL import Image, ImageFilter, ImageChops

base = Image.open(BASE).convert("RGBA")
source = Image.open(SOURCE).convert("RGB")
crop = source.crop((left, top, right, bottom))

alpha_pixels = []
for r, g, b in crop.getdata():
    excess = r - max(g, b)
    brightness = max(r, g, b)
    a = max(0.0, min(255.0, (excess - 2.0) * 4.2))
    a *= max(0.0, min(1.0, (brightness - 7.0) / 42.0))
    alpha_pixels.append(round(a))

alpha = Image.new("L", crop.size)
alpha.putdata(alpha_pixels)
alpha = alpha.filter(ImageFilter.GaussianBlur(0.35))
layer = crop.convert("RGBA")
layer.putalpha(alpha)

scale = target_width / layer.width
layer = layer.resize(
    (target_width, round(layer.height * scale)),
    Image.Resampling.LANCZOS,
)

out = base.copy()
out.alpha_composite(layer, (x, y))
out.convert("RGB").save(OUTPUT, quality=100)
```

Tune thresholds only enough to remove the background. Raising them too far removes dim glow; lowering them too far carries a visible dark rectangle.

## Replace baked-in text with an exact reference lockup

Use this path when the user supplies another image that already contains the exact requested words in the desired effect:

1. Extract the entire lockup literally from the effect reference, including every subtitle, divider, bevel, highlight, shadow, and glow. Do not retype it; retyping changes both glyph design and material treatment.
2. Build a strict color-dominance matte for the solid glyphs. Recreate soft glow and black extrusion from that glyph matte instead of lowering the extraction threshold until the reference background leaks through; low thresholds create a pasted rectangular plate.
3. Remove the old baked-in target text through a tight glyph-shaped mask, not a broad title rectangle. Broad inpainting flattens the shoulder or background into a visible dark panel.
4. If a clean no-text reconstruction is needed, generate or obtain it separately, then blend it into the original only through the old glyph-shaped mask. Keep the rest of the target pixel-identical.
5. Crop the reference generously before scaling so the source glow is not clipped. Scale uniformly to the target cap height, leave safe right/bottom margins, and preserve the lockup’s internal line spacing.
6. Verify both gates: zero changed pixels outside the localized edit region, and visual QA confirming exact wording, complete strokes, no old text, no rectangular plate, no source-scene contamination between glyphs, and no clipping.

If the desired wording does not already exist in the reference and the original font or editable layer is unavailable, exact font/effect preservation is impossible. Ask for the font, PSD/PSB, transparent title asset, or a reference containing the exact wording; do not call a reconstructed approximation “unchanged.”

## Add a supplied inscription to an angled armor plate

Use this when the plate is blank and another reference already has the exact printed word. This is insertion, not old-text inpainting.

1. Crop the source print at native resolution with small margins. Threshold its light ink against the dark plate, then run `cv2.connectedComponentsWithStats` to retain each expected letter **and punctuation dot** while discarding neighboring scratches. Tune the threshold on this reference, not a fixed global constant; a too-high threshold can split a worn letter and lose its dot. Inspect the isolated six-component mask for a dotted three-letter abbreviation before transfer.
2. Inspect an enlarged target chest crop. Trace one uninterrupted plate face, its upper/lower seam slopes and nearby straps; choose four destination corners within that face. Match the whole word's perspective to both seam directions, not just a rotated baseline, and leave a margin before the strap, bevel and lower edge. Project source color and alpha with the **same** `cv2.getPerspectiveTransform`/`warpPerspective` mapping. Warp premultiplied color (`RGB * alpha`), then divide by the warped alpha where nonzero before compositing; this avoids dark background fringes around bright glyphs.
3. Start every variant from the untouched target. If several files are requested with no design differences specified, make explicit size/placement studies on the same plate rather than pretending they are different character designs. Change only the destination quadrilateral, not the font or underlying armor.
4. Require equal canvas dimensions and zero decoded pixel changes outside a tight allowed chest rectangle. Inspect the full card and a native-size enlarged crop for all letters/dots, readable contrast, uninterrupted plate placement, seam crossings and a physically plausible downward/upward slope. A valid outside-mask diff cannot catch text floating across a seam inside that rectangle.

## Find a complete vertical crop

When the bottom of a title or issue number is uncertain, profile source rows before rendering. Count pixels that match the element color in each row and inspect all contiguous groups. Extend the crop beyond the final strong group so antialiased edges and glow survive.

For red artwork, a useful pixel test is:

```python
r - max(g, b) > 25 and r > 40
```

Do not trust a bounding box estimated from a downscaled preview. Use coordinates from the original file.

## Replace one styled glyph or numeral

Treat replacement as deletion plus insertion, not as mutation of the old silhouette:

1. Measure the old glyph on the original-resolution source with color row/column profiles; preview coordinates are often scaled or approximate.
2. Remove the old glyph and its local glow completely inside a tight edit mask. Do not leave its stem, counter, or shadow as a scaffold—the residual geometry makes the replacement look patched.
3. Obtain the actual font or editable source whenever possible. Render the new glyph at the same cap height, baseline, slant, stroke weight, tracking, bevel, texture, and glow.
4. If the font is unavailable, create the replacement as a standalone asset on a transparent or removable dark background. Give the generator or designer only the isolated neighboring glyphs as style reference, not the full poster.
5. Run strict QA on the isolated asset before compositing: name the intended character, reject any reading as the old character, and compare height, baseline, slant, counter geometry, stroke weight, texture, and glow against adjacent glyphs.
6. Composite the accepted replacement into the untouched base, then verify zero changed pixels outside the edit region and run a second visual QA at delivery size.

Never satisfy a request such as `5 → 6` by adding a stroke to the 5. If no genuine replacement can be produced, ask for the font or editable source rather than delivering an improvised glyph.

## Replace a dark engraved name on textured metal

Use this for a single changed field on a photographed, already-engraved product; keep the attached finished image as the base rather than rebuilding an earlier layout.

1. Measure the old inscription's ink bounds inside its panel at native resolution. Make an ROI that excludes the dark frame and neighboring labels. Threshold dark ink against local metal, then use `cv2.connectedComponentsWithStats` to retain glyph-sized components and reject isolated grain. Dilate the accepted mask just enough to cover antialiasing and the old edge halo; inspect the mask before repair because metal scratches can also be dark.
2. Prefer a verified clean plate. Otherwise, restore only the dilated ink mask with a nearby unlettered metal-grain donor matched to local illumination; use `cv2.inpaint` with a small radius only when the donor is unsuitable. Inspect the entire donor crop at native size for lettering, frame strokes, and dark scratches **before every offset, row shift, or tile**: a donor clean at its original position may paste an old line across the replacement elsewhere. Keep donor grain within the glyph-shaped repair mask, then inspect both old rows for ghosts and repeated patches. Inpainting can create smooth gray islands around every letter even while the frame and outside pixels remain exact. Never fill the whole panel or paste a rectangular grain crop.
3. Inventory the replacement's required glyphs and digits before typesetting. If the user requires the **exact** font/effect, obtain the original font or editable engraving asset (or an exact-wording reference) before editing; literal transfers of available source glyphs plus hand-built missing glyphs are still an approximation, and must not be delivered as an unchanged font. Only with permission for approximation, measure cap height, stroke weight, tracking and panel margins, fit the replacement's width, and modulate its dark ink by the restored plate grain rather than filling new letters with flat black.
4. Composite inside the same bounded name ROI, then compare decoded source and final pixels for zero changes outside it. Inspect a native-size name crop for old-letter ghosts, metal smears, frame damage, mismatched stroke weight, and exact spelling; inspect the whole product for consistent hierarchy and legibility. Reject a revision with a visibly tiled donor, hard black bars, or broad flat patches even if the text is correct and the outside-mask pixel count is zero.

## Preservation check

```python
diff = ImageChops.difference(base.convert("RGB"), out.convert("RGB"))
outside = diff.copy()
outside.paste((0, 0, 0), (x, y, x + layer.width, y + layer.height))
changed_outside = sum(px != (0, 0, 0) for px in outside.getdata())
assert changed_outside == 0
assert out.size == base.size
```

This proves unrelated target pixels are unchanged. It does not prove the transferred lockup is complete, so follow it with visual QA that names every expected text element.
