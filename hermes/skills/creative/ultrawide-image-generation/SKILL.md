---
name: ultrawide-image-generation
description: Use when generating exact 21:9 image batches.
version: 0.1.0
author: Somex Studios, Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Image Generation, 21:9, QA]
---

# Ultrawide Image Generation

## When to Use

Use with `reference-driven-image-generation` when a user asks for an exact 21:9 image or a batch of independent panoramas.

1. Assign each original reference a bounded role; for a legless worm design, do not import legs or turrets from armored-mech references. Pre-assign different chassis topologies and poses for each independent image, not merely recolors. Prompt for a native 21:9 ultra-wide single composition, full subject head-to-tail, no multi-panel layout, and enough safe margin to correct the ratio.
2. The image tool's coarse `landscape` argument does not guarantee its *returned file* has that ratio. Inspect actual dimensions; output may be approximately 1916x821 or 1860x845 even when requested dimensions differ. Preserve the generator's original files.
3. If only slightly off, crop a copy to the largest exact 7:3 rectangle: `k=min(width//7,height//3)`, destination `7*k` by `3*k`, centered. **Before cropping**, visually confirm no head, tail, limbs, horizon-critical element, or text lies in the removed margin; otherwise regenerate or outpaint rather than cut. Never stretch to claim an exact ratio.
4. Verify `final.width*3 == final.height*7`, count requested standalone outputs, check unique hashes and inspect each final image plus a contact sheet for completeness, anatomy, palette, framing and meaningful silhouette variety. The contact sheet is QA only; deliver each requested image separately.
5. For this user's image-generation requests, use ChatGPT/OpenAI only; do not invoke Claude or Higgsfield unless the user explicitly changes that rule.
