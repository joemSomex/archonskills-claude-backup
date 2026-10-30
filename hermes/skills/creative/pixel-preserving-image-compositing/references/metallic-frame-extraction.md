# Metallic outer-frame extraction

Use this recipe when the requester wants only a gold, silver, or other metallic border from a flattened artwork on transparency.

## Procedure

1. Measure the decoded source dimensions and preserve them unless resizing was requested.
2. Inspect the complete border and estimate its maximum inward extent on every side. Build an outer-ring spatial mask slightly wider than that extent; force the protected center to zero alpha.
3. Inside the ring, classify the metal by color ordering rather than brightness alone. For antique gold, a useful starting condition is `R > G > B` with minimum channel-difference and brightness floors. Reject red pixels whose green share is too small and neutral silver pixels whose green and blue are too similar. Tune against the actual source instead of hard-coding one universal threshold.
4. Convert the material score into alpha, retaining intermediate values for antialiasing and cracked/dusty edges. Apply only a sub-pixel blur (about 0.3–0.5 px) and reapply the strict spatial ring after the blur so alpha cannot spill into the center.
5. Remove detached non-frame remnants with 8-connected components. Keep components that touch the canvas edge or exceed a conservative ornament-area threshold; discard small isolated components even when their color resembles metal. This prevents nearby red highlights, armor, limbs, and dust from surviving as false frame fragments.
6. Preserve literal RGB by default. If the source is flattened against red/black artwork and the requester explicitly wants a clean single-metal layer, decontaminate retained pixels to the target metal hue while preserving per-pixel value variation; do not alter geometry or alpha.
7. For a metal-color conversion such as gold → silver, recolor only pixels whose existing alpha is nonzero. Derive a value or luminance from the retained RGB, map it to a neutral or slightly cool silver ramp, and copy the alpha channel byte-for-byte from the extracted border. This preserves cracks, antialiasing, dust, thickness, placement, and transparency while preventing hue conversion from expanding or eroding the mask. Verify `source_alpha == output_alpha` programmatically before visual QA.
8. Export PNG RGBA. Verify programmatically that dimensions are unchanged, alpha extrema include both `0` and a nonzero value, intermediate alpha exists for edge quality, and the central protected rectangle has exactly zero nonzero-alpha pixels.
9. Composite the output over a checkerboard for visual QA only. Reject missing frame segments, hard ring cutoffs, residual subject/background pieces, target-metal contamination (for example, residual yellow/orange in a silver-only request), and detached false fragments. Deliver the RGBA PNG—not the checkerboard preview.

## Pillow implementation notes

- Build the ring with four rectangles in an `L` mask.
- Use a per-pixel metal score such as the minimum of scaled channel differences and brightness, then clamp to 0–255.
- Run connected-component cleanup on a low alpha threshold so faint antialiased islands are classified with their parent ornament.
- Set fully transparent RGB pixels to `(0, 0, 0, 0)` to avoid hidden colored payloads in downstream compositors.
- For silver conversion, keep highlight/shadow variation but constrain chroma: use a slightly blue-biased neutral ramp rather than simple desaturation, then visually reject any residual gold/yellow/orange tint.
- Compare alpha bytes or hashes before and after recoloring; matching dimensions and alpha extrema alone do not prove geometry was preserved.
