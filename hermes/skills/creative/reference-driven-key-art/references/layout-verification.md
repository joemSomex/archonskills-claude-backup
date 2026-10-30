# Exact layout and verification

## Pixel-exact geometry

Use Pillow after generation when a model gets the art right but misses exact placement:

1. Open the accepted generated image and the exact background reference.
2. Resize/crop the background to the requested canvas with `ImageOps.fit`.
3. Detect stable frame lines by color/count or inspect their coordinates once; crop each complete rounded card including its border. A reliable detector counts amber-like pixels per column/row and collapses consecutive coordinates into frame-line runs.
4. Compute final positions instead of eyeballing them: `row_width = panel_count * panel_width + (panel_count - 1) * gap`, `start_x = (canvas_width - row_width) // 2`, and `top_y = round(canvas_height * reserved_top_fraction)`.
5. Preserve anatomy when the requested panel ratio differs from the generated card. Crop the source card interior, scale it uniformly from one axis, then center-crop the excess on the other axis; never resize width and height independently. Intentional edge-cropping is preferable to squeezing bodies, hands, ears, mechanical limbs, robes, or props.
6. Paste final interiors onto the exact supplied background with rounded masks. Redraw borders and glows at final resolution so a requested 1px line stays 1px after scaling; render selected/active cards separately with their brighter color and glow rather than trusting a resampled source border.
7. For any reserved band, place the panel row at the computed `top_y` and confirm every bottom border remains inside the canvas. Keep the unoccupied top, bottom, and side regions from the exact background reference, not from the generated approximation.
8. Save PNG and verify dimensions and hash.

Do not generatively redraw a composition that already passes art-direction QA merely to fix measurable placement. Deterministic extraction and compositing preserve approved identities while enforcing exact geometry.

## Deterministic UI screenshots

For exact copy and spacing:

- Build a fixed-size HTML canvas with CSS variables for card width, height, gap, and top offset.
- Use supplied textures as local assets; do not regenerate them.
- Render with headless Chromium using `--window-size=<width>,<height> --force-device-scale-factor=1 --hide-scrollbars`.
- Screenshot each variant separately, then verify pixel dimensions with Pillow.

## QA checklist

- Requested file count exists.
- Every file is PNG at the exact requested dimensions.
- Files have unique hashes.
- Character count and left-to-right order are exact.
- Panels have equal dimensions and aligned edges when required.
- Reserved background-only area matches the requested percentage.
- Background references appear only in their assigned scope.
- No text, logos, watermarks, extra people, or cross-panel effects appear unless requested.
