---
name: vehicle-card-conversion
description: "Use when 'Vehicle: Card Conversion' is requested."
version: 1.0.0
author: Somex Studios + Hermes Agent
license: Proprietary
metadata:
  hermes:
    tags: [vehicle-card, image-generation, animated-art]
    related_skills: [reference-driven-image-generation]
---

# Vehicle: Card Conversion

## When to Use

When the user writes `Vehicle: Card Conversion` with vehicle and environment images, generate five individual cards without an approval pause. Capitalization-only differences count. If either image is absent, recover it only when its identity and role are unambiguously specified in preceding user messages; otherwise ask for the missing reference. Do not assume that the last used spacecraft, vehicle, or city is the intended reference merely because it was mentioned earlier. The user's full five-card vehicle brief also activates this skill when both sources are available.

Read `references/authoritative-brief.md` in full before generation. It overrides generic `card-design` defaults for reference roles, aspect ratio, number of outputs, and composition. Inspect the originals and map image 1 to **vehicle identity and topology** and image 2 to **environmental design language only**. Inventory the vehicle's silhouette, stance, engine/wheel/track configuration as applicable, body paneling, cockpit/windows/lights, materials, surface wear, visible repeated parts and connection graph. Never invent car-specific wheels or a driver for a spacecraft. Unseen geometry remains inferred and must not be called exact. Use `creative:reference-driven-image-generation` and its complex-prop-fidelity reference for mechanical QA.

Use only OpenAI/ChatGPT image generation for this user's images. Make five independent calls, each from **both original references** and never from another generated card. Reserve five different orientations, action/staging concepts and landscape layouts before generation; keep the same vehicle topology. Select believable motion for that particular craft, or stage it at rest with cinematic energy if movement would require a visible operator. No people, creatures, extra vehicles or competing objects. Put the vehicle and strongest action effects in the upper two-thirds; keep the bottom third naturally dark, calm and low-detail for future text without a visible panel. Render the whole scene in dimensional painterly animated-series style rather than a photoreal or generic CGI finish. Exclude lettering, symbols, logos, numbers, plates, UI, frames and watermarks everywhere.

For nose-origin scanning-light revisions, define the source-to-effect path explicitly: central wedge fuselage -> forward optical head -> diverging sensing rays, while rotor rings retain only their built-in lamps. Inspect the actual common ray origin before acceptance; side/rear views can silently attach a convincing fan to a rotor instead of the nose. Keep the scan short enough to end above the quiet lower third and verify frame-edge extent separately from craft clipping.

Inspect a labeled contact sheet and every native-size file for vehicle fidelity, credible action and support, perspective, style, meaningful variation, lower-third restraint and accidental text. Replace failed slots directly from the two originals. Export five standalone PNGs at an **exact 2:3 pixel ratio** with safe crop only; never stretch the craft or clip its identifying features. Verify count, format and distinct hashes; do not equate hash uniqueness with visually different cards. Send all five individual files in chat with candid caveats if necessary.

## Resources
- `references/authoritative-brief.md` - mandatory full user brief; read before generation.
