---
name: pixel-art-emoji-gif-production
description: Use when making a transparent looping pixel-art emoji GIF.
version: 1.0.0
author: Hermes Agent
license: UNLICENSED
metadata:
  hermes:
    tags: [Pixel Art, Emoji, GIF, Animation]
    related_skills: [reference-driven-image-generation, pixel-preserving-image-compositing]
---

# Pixel-art emoji GIF production

## When to Use

Use for requests such as "make a pixel art emoji GIF," "animate this chibi reaction," "split the sprite sheet into frames," or "slow down this transparent GIF." Produce a coherent chibi reaction loop with reviewable transparent PNG frames and a verified GIF. Honor the requested delivery gate: sheet, separate PNGs, or GIF. Never make a GIF before the user asks for one.

## 1. Lock references and motion

Inspect all originals. Give the character sheet authority over identity, corrected eye color, hair, outfit, accessories, and proportions; give emoji examples only their assigned style, pose, or expression role. Do not import style-only hearts, glyphs or props. Distinguish full-body from head-and-upper-body framing before generation. Load `reference-driven-image-generation` and its linked pixel-art emoji production reference for role separation, pixel rendering and alpha extraction.

Before restyling an existing GIF, inspect each decoded source frame at readable native scale, not only a downscaled montage. Explicitly record which anatomical arm moves and each hand, mouth, wink, and gaze change; a hoodie animation can look like stationary folded arms in thumbnails while actually containing an outward-thumb gesture and a hand-to-chest wink. Do not replace observed source performance with a summary inferred from its resting pose.

Map the requested frame count and reading order. For an eight-frame cheer, plan: idle; anticipation; fists rising; peak with both fists up; descent with hair inertia; arms lowering; settling; near-idle matching frame 1. Keep the camera, subject scale and costume consistent while varying shoulders, arms, torso, hair and facial expression. Make it joyful, not a punch. Verify both closed fists remain readable at the peak. For an upper-body version, omit legs and shoes intentionally while preserving the draped collar/scarf and hand motion.

## 2. Generate and prepare the frames

For this user's image work, use ChatGPT/OpenAI image generation only, never Claude or Higgsfield unless explicitly requested. A 4x2 sheet can improve identity continuity. Demand safe negative space per cell. When hair crosses nominal grid lines but sprites remain separate, isolate the eight largest connected silhouettes from the WHOLE generated sheet and sort them by row and horizontal centroid before extracting; do not cut through hair at nominal cell edges. If silhouettes merge, regenerate with more spacing.

When a user reports white filler or inconsistent eyes, regenerate the rejected frames rather than repeating a failed neutral-checker extraction. Use a flat key hue absent from the identity, explicitly include enclosed hair/arm gaps, and inspect those gaps on a dark matte. Lock iris hue, pupil scale and lid construction across frames; if a blink was not requested and makes consistency ambiguous, keep the eyes open and animate the head, hair and supporting hand instead.

The generator may output opaque RGB despite a transparency instruction. Use a flat key hue absent from the character, inspect source corners, remove it at native generated resolution, and check dark/light composites for fringes. Preserve intentional detached accents; remove only verified matte specks. Prefer source-resolution cells over upscaling a previously downsampled sheet. Center head axes, keep intended vertical bounce, and align first and last pose. Export and verify the user's exact count/dimensions, real PNG RGBA with transparent corners, safe silhouette bounds, distinct pixel hashes, correct eye color and outfit in every frame. Inspect the contact sheet and native-scale details; hashes alone do not prove motion. Deliver the PNGs without an animated file when the user asks to review frames only.

For navy-haired, cyan-piped characters on green matte, inspect dark hair-edge pixels after initial keying: low-brightness green contamination can survive a high `G` threshold. A tested stricter candidate gate was signed-channel `G>20`, `G-R>12`, `G-B>8`; apply only when the character has no green details and inspect hair, cyan piping and fingers afterward. Avoid matte dilation when it would shave fine strands.

When extracting a chroma-key sprite sheet, detect border-connected neutral grid lines separately from the green matte: white dividers can connect all eight poses into one foreground component. Remove only those background dividers, preserve disconnected eye highlights, and require the expected count of substantial silhouettes before extraction. Regenerate sheets whose neighboring silhouettes actually touch instead of cutting through their hair.

Do not stabilize a nod by copying Frame 1's torso beneath a fixed horizontal cutoff while retaining other frames' heads: the neck, collar, and long hair may separate at the join. Preserve complete poses and align stationary neck/collar landmarks using integer translations; redraw genuinely inconsistent poses rather than transplanting a torso or stacking incompatible face/arm patches. Validate continuity across the neck and both hair-to-shoulder edges in the delivered frames.

When unfolding an arm into a raised gesture, audit the lower torso for its leftover folded forearm: generators can retain the original crossed-arm layer beneath the legitimate supporting arm, producing a third limb. Remove only that obsolete segment and reconstruct the underlying torso, preserving the other arm and raised elbow. Use the clean original rather than an annotated screenshot, and propagate a registered local repair across all affected poses while leaving folded endpoints unchanged.

For expression-only revisions, do not bend or overlay a generic mouth curve: it can create pointed lips and does not provide supporting cheek/lid acting. Redraw expressions from source-resolution face crops, register candidates using unchanged outer facial/hair landmarks, then replace the complete old mouth region and only the required cheek/lower-lid details. Protect iris/pupil/highlight pixels, face silhouette, alpha, and every outside-mask pixel. Preserve the requested per-frame expression progression even when nod poses repeat; record original frame delays when delivering PNGs without rebuilding the GIF.

For crisp pixel-art loops, do not create extra frames with optical-flow blending or crossfades: they produce ghost outlines and uneven clusters. Redraw in-betweens together from the original identity, approved style and pose reference; inspect native-resolution edges before accepting them. Align the main torso silhouette's bottom separately from detached steam so effects do not determine the baseline.

For peeking loops, keep a visible hand continuously connected through wrist, sleeve, elbow and shoulder to the moving torso. Do not stabilize the grip by pasting a detached canonical hand across poses. If the user rejects early or lingering fingertips, make the hidden pose entirely character-free, show connected gripping arms during the peek, and redraw a released hand withdrawing toward the chest in the return frame. Stabilize only the stationary edge without overwriting moving anatomy; inspect the return pose separately because a generator may repeat the gripping hand despite a release instruction.

## 3. Build a GIF only after frame acceptance

Run `scripts/build_gif.py` on the accepted ordered PNGs. The script uses one shared palette, reserves palette index 0 for transparent pixels, quantizes opaque colors without dithering, then reopens the saved GIF and checks every decoded frame's size, transparency, duration, loop flag and color error. GIF has a 256-color palette and binary transparency; do not describe it as full RGBA. Inspect its dark/light QA preview before delivery. Default review timing for an eight-frame cheer is `150,150,150,250,150,150,150,250` milliseconds; accept a user-supplied timing override. For a timing-only revision, require the old and new decoded GIF frames to be pixel-identical.

Example:

```bash
python /root/.hermes/skills/creative/pixel-art-emoji-gif-production/scripts/build_gif.py \
  --input-dir /path/to/frames --pattern '*frame*.png' \
  --output /path/to/cheering.gif \
  --durations 150,150,150,250,150,150,150,250 \
  --qa-preview /path/to/qa.jpg
```

For small gold irises, do not trust a low whole-frame palette error: a shared GIF palette can map gold to skin-brown while passing the global check. Compare decoded iris crops against the source PNGs in every frame. Reserve a dedicated gold subpalette (for example 64 gold colors plus 191 general colors and one transparency index) sampled from verified iris regions, retain all timing and alpha, and verify both per-iris error and native-size visual color. Red-only accent oversampling does not protect gold eyes.

When constructing a custom amber subpalette, map opaque pixels directly to nearest colors among indices 1-255 using signed integer RGB distances. Do not quantize against a palette containing transparent index 0 then replace all zero indices with an arbitrary opaque entry: genuine dark pixels may choose index 0 and become pale contours. Reopen every encoded frame, verify alpha and delays, and reject dark source pixels mapped to bright colors; whole-frame average error and iris-only checks do not catch this reliably.

For a batch-wide half-body proportion correction, use the new reference only for head/body ratio and lower crop, never its pose, expression, armor, or lights. If a uniform zoom would cut low hand gestures, redraw each complete pose with a compact anatomically connected torso and visible hands rather than squashing the torso or pasting an enlarged head. Rebuild every playback frame, preserve the original per-variant delays and reversible pose order, and verify a common lower baseline and matching wraparound. When keeping the original palette is required, map the corrected opaque colors directly to its indices 1-255 and verify decoded pixels against those mapped PNGs.

When using Pillow palette images with transparency, inspect palette mode immediately before GIF encoding: converting a P image to RGBA for PNG QA can mutate its palette to RGBA in some Pillow versions. Reset the original RGB palette before saving the GIF, or encode from untouched copies, and verify decoded RGBA equality against the PNGs; otherwise encoding may fail with invalid palette size or write shifted colors.

For anchor-aligned waist-up batches, bound uniform nearest-neighbor scale by the largest left/right distance from the stationary chest anchor as well as source width/height. A high flex extends asymmetrically beyond the torso, so fitting by silhouette width alone can violate safe margins after chest registration. Avoid flooring the scale to an integer when that would halve otherwise comparable variants; preserve nearest-neighbor sampling and use integer whole-pose placement.

For batches of animated variants, distinguish output count from poses per animation: ten GIFs with four poses require ten distinct animations, not ten extracted frames or timing-only duplicates. Persist source and verification manifests per variant, then verify the final unique output count programmatically.

When preserving a four-key animation while adding generated inbetweens, keep the original keys pixel-identical as separate PNGs and generate one independent full-pose sheet per requested variation from all four original references. Insert the new drawings between the appropriate keys; a generated near-rest pose belongs before the folded endpoint, not after it if its hand is still raised. Use one uniform source-cell scale and integer whole-pose translation only; record collar matching scores and the bust baseline, and inspect low-score matches rather than treating baseline alignment as proof of collar stability. Save raw generated sheets, extracted poses, playback PNGs and reopened decoded frames alongside each verification manifest.

When detecting orange/gold iris colors automatically, constrain sampling to the eye apertures or a narrow neighborhood of verified sclera; copper hair and warm skin can contaminate a broad face ROI. Exclude deliberately closed-eye frames from iris-color metrics rather than treating tiny orange skin clusters as visible irises. Keep closed-eye frames encoded and verify their pixels normally.

When image restyling returns HTTP 400 Invalid image data with animated references, decode the relevant GIF reference frames to ordinary RGB PNGs and re-encode unusually large source sheets before retrying. Preserve the original animation metadata separately; a static style-reference conversion must not alter output playback order or delays.

For a gaze-following shoulder brush, audit pupils and nose direction separately from arm geometry: a generator can turn the head away from the fingertips despite correct hand motion. If it repeatedly looks the wrong way, request an explicit screen-left three-quarter face with nose pointing left and pupils down-left toward the hand, while keeping the approved rendering image primary and every original identity/style reference attached. Regenerate the whole sheet rather than patching eyes or mirroring the character.

For asymmetric lead-hand loops, define the lead in image-space as well as anatomy (for example, viewer-right = character-left), and inspect every action cell, especially the peak and release: a generator can use the correct arm during approach then switch arms mid-sheet. For crossbody shoulder brushing, explicitly lock the moving elbow on one side and wrist/hand on the opposite side through contact, outward sweep and lift-clear; normalized cell coordinates can reinforce this geometry. A correct full-pose sheet may be supplied as geometry-only guidance alongside the original identity and style references. Regenerate the full sheet from originals if the lead is wrong; do not mirror identity or armor as a shortcut. For cross-body shoulder brushes, state the geometry as upper-left wrist connected diagonally to lower-right elbow, with the screen-left unused arm down; audit approach, release and return individually because mixed-arm sheets can switch only those poses. If repeated original-reference generations switch sides, include a visually verified correct full-pose sheet as an additional geometry-only reference while retaining the original identity and style references on every independent variation.

Before reusing a batch exporter for a new character, remove identity-specific processing such as mole drawing, scar repair, hair recoloring, iris HEX overrides, and hard-coded anatomical anchors. Reuse only neutral extraction/encoding utilities; derive new masks and anchors from the current reference and generated frames so an old character cannot leak through procedural postprocessing.

Determine sheet layout from the actual substantial silhouettes and their top coordinates, not the requested grid or moving hand centroids. Generators may return a horizontal four-pose row despite a 2x2 prompt. Preserve actual reading order and inspect framing before extraction; a long torso in a horizontal layout may require a compact chest-up redraw rather than independent scaling.

For exit animations with a deliberately empty final frame, verify that its decoded alpha is zero everywhere and that no previous-frame pixels persist. If Pillow's high-level multi-frame writer emits an invalid empty-frame descriptor or unexpected frame count, encode a shared global palette with `GifImagePlugin.getheader`, then write each full-canvas frame through `GifImagePlugin.getdata` with explicit duration, transparency index 0 and disposal 2, followed by the GIF trailer. Reopen and seek every frame; do not disable decompression-bomb protection to accept a malformed file. Keep complete source poses separate from intentional screen-edge translations so only the specified exit frame is clipped.

## Character-specific visual corrections

- For Sylvia Bloom reactions, follow her portrait's flat, sleek, center-parted straight silver hair close to the scalp; do not inflate the crown or add wavy, fluffy, outward-curling ends. Keep the mole above the upper lip on the portrait's left side tiny and muted brown, not an enlarged black beauty mark. Inspect at emoji display size so it does not become a focal point. These are visual-reference locks, not new personality canon.

## Resources

- `scripts/build_gif.py` - run for two or more accepted ordered RGBA frames when a looping transparent GIF is requested; it encodes and verifies the result.
