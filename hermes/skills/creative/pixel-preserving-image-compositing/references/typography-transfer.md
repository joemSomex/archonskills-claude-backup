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

## Find a complete vertical crop

When the bottom of a title or issue number is uncertain, profile source rows before rendering. Count pixels that match the element color in each row and inspect all contiguous groups. Extend the crop beyond the final strong group so antialiased edges and glow survive.

For red artwork, a useful pixel test is:

```python
r - max(g, b) > 25 and r > 40
```

Do not trust a bounding box estimated from a downscaled preview. Use coordinates from the original file.

## Change one styled glyph without replacing the font

When one character or numeral must change but the original display font is unavailable, edit the extracted RGBA glyph structure instead of retyping the whole lockup:

1. Measure the glyph on the original-resolution source with color row/column profiles; preview coordinates are often scaled or approximate.
2. Decompose the old glyph into reusable strokes and counters. For an angular `5 → 6` change, retain the top, middle, lower-right, and bottom strokes; extend the existing upper-left stroke into the lower-left side to close the bowl while leaving a dark inner counter.
3. Copy texture from the same glyph or an adjacent matching glyph, reshape it only enough to fit, and alpha-composite it onto the new stroke. Reusing the original cracked material preserves color, marbling, bevels, and glow better than a substitute font.
4. Continue only a few existing fractures across the added stroke; avoid mirrored texture or repeated cracks because repetition exposes the patch.
5. Rebuild the final poster from the untouched target base, enlarge or reposition the complete lockup once, and visually verify that the new glyph reads unambiguously at delivery size.

Use this only for small structural edits. If the requested character cannot be built convincingly from existing strokes, obtain the actual font or ask for an editable source rather than silently approximating the typography.

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
