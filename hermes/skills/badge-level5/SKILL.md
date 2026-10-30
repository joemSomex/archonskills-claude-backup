---
name: badge-level5
description: Use when applying the E5 antique-amber finish to badges.
version: 1.0.0
author: Somex Studios, Hermes Agent
license: Unspecified (user-provided visual assets)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Badge, Level V, Material Variants, Image Editing]
    related_skills: [pixel-preserving-image-compositing]
---

# Badge Level 5 - E5 Antique Amber

## When to Use

Use for "badge-level5", "E5 warm antique amber", or applying the approved olive-black/amber Level V material to a supplied Quantum 13 badge. This skill is independent of `badge-levels`, which remains the original Level I-IV workflow.

## Appearance Contract

- Treat each supplied badge as the **sole design authority**: exact silhouette, alpha, geometry, proportions, central symbol, panel seams, structural details, scale and framing. Never borrow the chevrons or arrow from `assets/approved-e5.png`.
- Treat `assets/approved-e5.png` as the **definitive E5 appearance target** and `assets/material-macro.jpeg` as texture context only. Reproduce warm antique amber/honey inclusions and narrow copper glints within dark moss/olive-black translucent mineral-glass. Preserve charcoal-olive structural recesses, legibility and restrained contrast. Avoid metallic bronze paint, uniform gray, orange flood, outer glow, flame, or copied rock shapes.
- These two assets are appearance-only. If the user supplies a newer explicit material reference or asks for a preview before changing this skill, honor the current request and wait for approval.

## Workflow

1. Inspect the new badge, measure its actual dimensions/alpha, and map its symbol and negative spaces. Load `pixel-preserving-image-compositing` and its material-only variants reference via `skill_view`. If alpha is missing, verify a foreground mask rather than inventing transparency.
2. Create ONE texture candidate per badge with `image_generate`: pass the new badge as `image_url` and `assets/approved-e5.png` as the appearance `reference_image_urls`. Ask for the E5 olive/amber material on the badge's existing planes, with the source's symbol and seam topology unchanged. Use OpenAI/ChatGPT image generation, not Claude or Higgsfield. Treat the result as untrusted texture only: reject candidates with a missing symbol, shifted orbit/arrow, duplicate rings or source-example shapes.
3. For a 1000 x 1000 RGBA source and centered, dark-background candidate, run `terminal(command="python <skill_dir>/scripts/composite.py --source <badge.png> --candidate <candidate.png> --output <review.png>")`. The script registers one isotropic scale, transfers E5 hue/refraction onto softened source relief, protects dark recesses, restores source alpha and transparent RGB byte-for-byte, and prints verification JSON. Do not use the candidate alpha or silhouette. If candidate background/registration is unsuitable, fix the candidate rather than forcing the composite.
4. Inspect the final PNG at native and thumbnail sizes against `assets/approved-e5.png`, and over both dark and light mattes. Compare central symbol, seams, contour and negative spaces to the supplied badge, not to the example. Source-alpha equality is necessary but does **not** prove every inner detail; reject or revise visibly changed constructions. Avoid hard mask seams, missing fine loops and excessive brightness.
5. Deliver only the requested standalone 1000 x 1000 transparent PNG(s). If the user requests review first, stop after the test and wait; do not batch remaining badges or update other skills until authorized. Never send a contact sheet or unchanged master unless explicitly requested.

## Verification

Require `size=[1000,1000]`, `mode=RGBA`, `alpha_equal=true`, and `transparent_rgb_equal=true` from the script for every output. Visually verify the E5 material, symbol and clean edges before claiming fidelity. If the input is not a 1000 x 1000 RGBA original or the candidate cannot be registered safely, report the limitation instead of silently resizing the badge.

## Resources

- `assets/approved-e5.png` - approved E5 badge appearance; material only, never geometry.
- `assets/material-macro.jpeg` - original olive/amber mineral texture context; do not copy rock silhouette.
- `scripts/composite.py` - deterministic source-alpha E5 texture transfer, tested on the arrow speech-bubble and atom badges.
