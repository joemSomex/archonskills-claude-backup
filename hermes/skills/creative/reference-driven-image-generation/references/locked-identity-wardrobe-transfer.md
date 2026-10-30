---
author: Hermes Agent
license: MIT
---

# Locked Identity + Wardrobe Transfer

## When to Use

Use this checklist when one source controls the face/identity and a different source controls clothing or armor, especially when the user requires strict reference fidelity.

## 1. Build the role map

- Put the identity reference in `image_url`.
- Put the wardrobe reference first in `reference_image_urls`; follow it with background, lighting, style, and prop references in semantic order.
- State both exclusions: the identity source does not contribute clothing, pose, or background; the wardrobe source does not contribute face, hair, body identity, pose, or contact-sheet layout.
- If the wardrobe source is a turnaround or collage, extract the recurring garment design while rejecting its white background, dividers, repeated people, alternate poses, and framing.

## 2. Extract immutable identity traits

When the user assigns a portrait only to a partial facial feature or concealment boundary and asks for a NEW face, do not apply the strict identity lock below. Inventory what is actually visible, then crop the ORIGINAL to the permitted feature region if distinctive makeup, lip marks, or script tattoos keep leaking; specify a different nose, lips, jaw, skin tone, and hair positively, and inspect a native-size lower-face crop before batching. A negative instruction alone can preserve a high-contrast forbidden mark from a full-face source.

Inspect the original at useful resolution and lock visible geometry rather than broad labels:

- age and presentation
- face outline, jaw taper, cheekbone width, and chin
- eye shape, iris color, spacing, and lid geometry
- brow shape and density
- nose bridge, width, and tip
- philtrum, lip shape, and thickness
- skin tone, freckles, moles, scars, wrinkles, and other stable marks
- hair color, hairline, part, bang direction, layer lengths, side locks, and nape length
- facial hair, glasses, piercings, or the explicit absence of each

Forbid likely drift explicitly, such as a wider jaw, different eye color, missing freckles, darkened hair, mechanical facial pieces, or style-reference makeup.

## 3. Extract immutable wardrobe topology

Describe construction before surface style:

- collar or neck guard and how it sits on the neck
- chest layers, plate count/shape, overlap order, closures, and centerline
- shoulder silhouette and attachment
- upper-arm pieces, flexible joints, elbow transition, forearm guards, cuffs, and gloves
- waist, belt, fasteners, lower layers, and any visible hem
- material assignment per part: fabric, leather, rubber, matte metal, gloss metal, mesh
- seam, piping, trim, wear, print, emblem, and luminous-accent placement

Do not translate generic style words into new construction. Apply metal wear only to existing metal; do not turn fabric into armor or a fitted suit into a coat, robe, hood, cape, or fantasy plate set.

When a user replaces the suit palette with a national or organizational flag, preserve garment topology but assign each new color to named panels and flexible layers; do not leave the original dark suit dominant merely because the source is dark. Treat the flag patch as a separate acceptance gate: specify its geometry, stripe/order, emblem elements and placement, then inspect a native-resolution crop in every final file. A vaguely colored badge or unique file hash does not prove a correct emblem; if tiny details remain unreadable, label the patch approximate rather than claiming fidelity.

## 4. Front-load the lock before pose and style

Start the generation prompt with two compact blocks:

1. `Identity absolute lock — source A only:` immutable facial and hair traits plus forbidden drift.
2. `Wardrobe absolute lock — source B only:` garment topology, materials, accents, and forbidden redesign.

Then add pose/anatomy, background, lighting, style texture, and negatives. State that style references may affect only grain, halftone, chromatic aberration, material highlights, contrast, and lighting—not face, hair, clothing silhouette, armor language, or props.

## 5. Calibrate before batching

Generate one standalone calibration image from all original references. Do not use a generated variant as the next variant's source.

Review at least two tight crops:

- face and hair against the original identity image
- neck, chest, shoulder, arms, gloves, waist, and accent placement against the original wardrobe image

Identity and wardrobe must pass before evaluating stylistic preference. If either fails, strengthen only the failed lock and regenerate the calibration image from the originals.

## 6. Live-action conversion from illustrated sources

When the face and wardrobe references are illustrations but the user asks for a real-person portrait, inspect a prior render's face at useful size before repeating a batch. A highly detailed face can still retain anime proportions or smooth CGI skin.

Make one fresh calibration photograph from the original role-limited references, not an image edit of the stylized output. Use the face source for visible facial geometry and haircut, the wardrobe source for garment construction, and specify any user-overridden iris color separately; placing an illustrated output in `image_url` can reassert its rendered facial planes. Front-load a real adult actor, natural facial asymmetry, skin pores, individually resolved hair strands, tangible clothing and armor construction, and physically plausible white-studio light. Judge the face crop for photographic human anatomy and texture before proceeding with independent variants; valid pixel dimensions and file hashes do not establish the requested medium.

## 7. Acceptance gates

Reject the image when any of these change materially:

- face outline, eye geometry/color, nose, lips, skin tone/marks, or hair construction
- collar/neck geometry, chest topology, shoulder silhouette, arm segmentation, glove design, waist structure, material assignment, or distinctive accent placement
- identity leakage from the wardrobe model
- wardrobe leakage from the identity portrait
- costume or facial design imported from style references

After a calibration image passes, generate the remaining variants independently and vary only approved non-identity details such as particle placement, background traces, or negative-space distribution. Repeat face and wardrobe crop checks on every final output and again after deterministic cropping.
