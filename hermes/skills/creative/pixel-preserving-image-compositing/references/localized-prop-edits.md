---
author: Hermes Agent
license: MIT
---

# Localized Prop and Weapon Edits

## When to Use

Use this recipe when a prop must move, lengthen, pass behind the subject, or gain new hand contact while the face, pose, costume, lighting, background, and canvas remain locked. It is especially useful when a generator can synthesize the new contact geometry but cannot preserve unrelated pixels globally.

## 1. Generate alignment scaffolding

- Use the untouched target as the sole edit base for every requested variant.
- Ask the generator to change only the prop path and the named contact hand. Lock identity, crop, pose, front hand, clothing, lighting, and background explicitly.
- Generate one calibration candidate first. Compare it side by side with the base and continue only when the face, silhouette, torso, and camera remain closely aligned.
- Treat the candidate as a source of replacement pixels, not as the final file; global redraw outside the requested region is expected and must be discarded.

## 2. Build the edit mask as three unions

1. **Old-prop cleanup:** cover the entire old prop, including every tip, chain link, glow halo, reflection, and detached fragment. Extend to the background immediately behind it so no ghost remains. Inspect the full old path at native resolution, including faint curved edges in dark background: a narrow mask can remove the bright blade but leave a thin gray arc outside it. After applying face/hair/armor protection, inspect the prop path again: a hard protection polygon can restore an old blade tip or guard. Carve the smallest local cleanup aperture through that protection only over the remnant, fill it from the aligned candidate, and verify the rest of the protected region still has zero changed pixels.
2. **New prop path:** follow the complete new shaft, blade, string, or chain until it reaches a real occlusion boundary. For a chain routed behind a body, include every visible link up to the exact body edge, then start a second visible segment where it re-emerges; do not leave a dangling link in open space.
3. **Contact geometry:** cover the smallest region containing the edited hand, wrist transition, handle, connector, and contact shadow. Keep the face, hair, front hand, and unrelated armor outside this region.

Feather the union narrowly—typically a few pixels at source resolution. A broad feather silently changes nearby armor and lighting; a hard boundary creates a pasted seam. After feathering, multiply the mask by hard-zero protection masks for the face, hair, hands, core costume, and any locked connector/shaft: blur can otherwise leak a few changed pixels into a protected region even when the pre-blur mask excluded it.

For size-only prop edits, choose and verify a fixed anchor before generating or compositing—such as a weapon hub, shaft centerline, or hand grip. If the prop already touches a canvas edge, symmetric enlargement is geometrically impossible without cropping or moving the anchor; explicitly choose an allowed expansion direction, then reject candidates that silently move the hub or break the connector. For a two-hand grip, mark both contact points, the pommel, and the guard along one measured shaft axis. Distinguish shortening the exposed tail beyond a locked upper hand from shortening the distance between hands: the latter cannot change while both contact points remain fixed, so it requires moving an allowed grip/contact and reconstructing its arm/occlusion. When only the upper-hand gesture is locked, restore its original silhouette over any shaft edit and edit an adjacent ring through a separate tiny aperture. Verify that the new terminal remains visibly capped and joins the old shaft on the same axis, the deleted terminal has no ghost, and the specified handle segment—not merely some other part of the weapon—became shorter.

When the user supplies an immutable design reference for an enlarged weapon head, first write a component inventory and preserve it as geometry rather than vague style: dominant-side versus secondary-side blade size, outer silhouette, plate layering, edge material, light-slot count and placement, central hub, bearing ring, support arms, pistons, connector neck, shaft axis, and intentional negative spaces. Describe each asymmetric side as a connected assembly, not as a collection of visual accents; for example, a compact secondary blade may require one continuous path from upper armor ridge through the outer metal cap and internal light cavity to the lower pointed blade. Use the existing hub/shaft junction in the target as the fixed anchor. Permit the enlarged head to leave the canvas or pass behind the character when requested; cropping and occlusion are preferable to shrinking, translating the hub, or changing the design. Build a foreground protection mask from the untouched base and composite the original hair, head, hands, and armor back above the enlarged weapon so the layer order is `background → weapon head → original foreground subject`. Do not erase a reference component merely because it is partly hidden; verify its visible continuation on both sides of the occluder.

Shape the replacement mask around the complete component silhouette, including every lower tip, outer cap, support, and attachment path. Do not let a broad foreground-protection polygon cut through a weapon terminal before it reaches the real hair, armor, or canvas-edge occlusion; that produces an apparently clean pixel diff but an amputated weapon. Where the weapon passes behind the subject, extend the synthesized weapon beneath the subject first, then restore the untouched foreground pixels above it. Preserve intentional holes inside the reference assembly, but distinguish them from accidental missing material by tracing every solid rail and plate to its designed endpoint.

## Paired handheld energy props with an immutable subject

1. On the decoded original, trace the full old prop silhouette, every visible grip/handle and the new prop's footprint on each side. Before editing, classify the other image as either an exact design to transplant or a style-only reference. For an exact transplant, inventory and preserve each half's outline, top/bottom caps, side notches, coupling tabs and handedness; image-left and image-right halves stay in their corresponding hands. If the user explicitly changes the field's opacity, preserve that hardware geometry but treat the material override as authoritative: a smoky reference pane is not permission to obscure the backdrop or the connected arm beneath a requested clear field. For style-only inspiration, borrow materials without copying the reference silhouette. Check source dimensions and decoded-image similarity if a reuploaded target may match an earlier base.
2. Reserve the mating topology before rendering: each half has a distinct outer edge, a compatible inner coupling rail, and connection points that would line up when joined. Keep the halves in their original respective hands. A pair of similarly tinted panels without visible coupling geometry does not prove detachability.
3. Generate one aligned replacement candidate from the untouched target and the design reference. Scale it uniformly back to the original canvas and compare the hands and shield footprints side by side. Use its new shields and minimal grip-contact pixels as scaffolding, never its globally redrawn torso, face, legs or labels. Calibrate the pane against the requested backdrop: pale blue-white must read as visibly translucent, with one uninterrupted field when requested; use fine edge glow, not interior skeleton, segmentation, bolts or branching filaments unless the user asks for them. For a restrained blue-white field on a vehicle or device front, interpret a "square curved" shield as a rectangular surface gently bowed outward, with softly rounded corners, faint surface texture, slight glow and edges fading into air. Do not add a bright polygon outline, thick rim, solid support, dense lattice or arcs just because a reference contains a red annotation or a conspicuous border; those additions can make a transparent pane read as a wireframe sticker. Calibrate its placement against the device's actual forward direction and keep any connection subtle but physically plausible. For optical transparency in front of a holder, stage each pane across the existing arm and hand rather than only in empty background. Inspect the same continuous shoulder-to-elbow-to-wrist-to-grip silhouette through the field, with backdrop visible beside it; reject a separate gray arm-shaped imprint inside the pane because that is a duplicate ghost limb. On a white studio set, a pane seen only over white cannot demonstrate that it would reveal dark armor. A style-only reference supplies energy/material language, not its silhouette or labels.
4. For each variant, composite from the same untouched decoded base through the union of the entire old and new half-shield footprints and necessary hand-contact strips. Where the transparent pane crosses the arm, include that overlap in the local candidate mask so the arm/pane depth order survives, while preserving the original face, core torso, legs and background outside the mask. A broad hard hand/forearm protection mask can restore an old shield shoulder or grip on top of the new prop; protect only verified foreground pixels, and locally reopen the cleanup mask where the old prop crosses a hand. Feather inward by only a few pixels. Trace both old lower tips even if the replacement is shorter, and inspect the new caps where a mask narrows beside the calf; otherwise an old tip or a cut cap survives despite a clean central-body pixel diff. Compare decoded pixels outside both edit masks (especially the central body) against the source; require zero differences there. Inspect both full shield tips and enlarged grip crops for old dark fragments, narrow background-colored wedges and clipping. Do not mistake different hashes or glow intensity for different shield designs when the user requested distinct concepts; when the user requested two placements of the same exact reference, vary pose rather than redesigning it.
5. Preserve the source canvas dimensions unless expansion is expressly requested. If a very narrow source is padded to the image generator's portrait ratio, register the candidate back to the padded original by stable armor features, transfer only the two prop silhouettes, and crop back to the original canvas. Before acceptance, check that both outer caps and rails remain entirely inside that crop; if not, fit the candidate props inward around their fixed grip anchors or regenerate a narrower pair, rather than cropping away a shield. Keep the robot's central armor pixels unchanged outside the local prop masks. If the delivered PNG uses blue-white coloration to depict a translucent *in-scene* field but has no RGBA alpha, describe that accurately; do not call the file itself transparent.

## Standalone industrial component into a locked photo

Use this when the user wants several genuinely different mounted-device structures but full-scene generation would redraw the protected subject. Generate the *permissible component itself* as a standalone photoreal product, not a restated blocked scene; never use a standalone prompt to evade a provider refusal. If policy does not permit the component, stop and report the blocker.

1. Recover the exact unmarked scene first. If a red annotation was added to a prior PNG, compare decoded pixels outside a dilated red-stroke mask against candidate clean files; use a candidate only when the protected scene actually matches, not merely when thumbnails look alike. Inventory the entire old device and its shoulder bearing before editing.
2. Classify the requested object's function before generating a donor. Specify its function-appropriate visible front, square **outer cross-section** when requested, length, bearing count, bracket shape and load path; an optical aperture is appropriate only for an optical device, not every square tube. Reserve a distinct macro construction for each requested design (different housing, mount and joint topology rather than skins), generate each independently from the original brief, and inspect the standalone contact sheet *for functional readability* before transfer. Reject a sensor/camera-shaped donor for a differently specified function instead of changing its label, texture or count. If the requested design is disallowed, do not disguise it as another object or treat the substitute as fulfilled; stop and report the shortfall.
3. On a white sweep, derive a soft cutout from the product's dark foreground after finding the largest connected component, include its complete hinge foot, and keep soft shadow alpha. Crop with margin, scale **uniformly**, rotate to the scene's perspective, and anchor the foot to the measured original mount. Check the final tip margin and projected tip-to-hinge length before batching. A loose white rectangle or a foot several pixels above the shoulder makes an otherwise photoreal insert read as a sticker.
4. Remove the old device across its *entire* silhouette, including the far tip and rear stub, but retain any original lower bearing and shoulder shadow that the new foot must meet. On a white backdrop, sample replacement sweep color from verified empty pixels on the **same row**; sampling near the head or shoulder can fill the old prop with a dark stripe. Feather the cleanup mask narrowly and restrict it to the old footprint, rather than wiping a broad rectangle through the shoulder. Composite the isolated photo over this cleaned original, not over a prior variant.
5. At native-size crops, trace the new aperture through its box housing, hinge links, bolts, foot and shoulder contact. Reject residual old stubs, a second bearing floating behind the new mount, white wedges, clipped tips, doubled arms, or a detached foot. Verify exact decoded-pixel equality outside the union of old-prop cleanup and new-prop footprints, then count the independently different *geometry* in a contact sheet. Describe standalone generation plus compositing accurately; do not imply the entire locked scene was regenerated.

## 3. Composite from the untouched base

Resize the candidate uniformly to the exact base dimensions, then use the mask only once:

```python
from PIL import Image, ImageFilter

base = Image.open("base.png").convert("RGB")
edit = Image.open("candidate.png").convert("RGB").resize(
    base.size, Image.Resampling.LANCZOS
)
mask = Image.open("edit-mask.png").convert("L").filter(
    ImageFilter.GaussianBlur(4)
)
out = Image.composite(edit, base, mask)
out.save("localized-edit.png")
```

For several variants, repeat from the same untouched base with independently generated candidates; never use an earlier composite as the next base.

## 4. Prove preservation

- Require equal dimensions and canvas ratio.
- Compute a pixel diff against the decoded base and require `outside_changed_pixels=0` wherever the edit mask is exactly zero.
- Separately require zero changed pixels in protected face, hair, all locked hands, core costume, and any preserved shaft/hub region. Check these protected masks after feathering, not only the broad outside-mask count.
- Record unique hashes for the independent final files.

A useful Pillow check is:

```python
from PIL import ImageChops

diff = ImageChops.difference(base, out).convert("L").point(
    lambda p: 255 if p else 0
)
outside = ImageChops.multiply(
    diff, Image.eval(mask, lambda p: 255 if p == 0 else 0)
)
assert outside.histogram()[255] == 0
```

## 5. Run topology QA at full resolution

Inspect the whole image and tight crops of both connection points. For a two-ended chained weapon, trace:

`front handle → chain start → weighted sag → body-entry occlusion → body-exit occlusion → rear handle → rear gripping fingers`

Reject any of the following:

- an old blade tip or chain fragment outside the cleanup mask
- a chain that stops in open space instead of entering occlusion
- parallel, forked, duplicated, or disconnected chains
- chain links painted across foreground armor when the route should pass behind it
- a rear hand near the handle rather than visibly wrapped around it
- broken wrist continuity, merged fingers, extra blades, or changed weapon design
- a resized asymmetric head that becomes symmetric, swaps its dominant side, loses a reference light slot/support arm, or moves its hub away from the preserved shaft axis
- a dominant blade whose outer edge, inner frame, light rail, or staggered terminal tips stop in open background instead of reaching their designed endpoint
- a compact secondary blade that is misread as separate upper and lower wings, becomes a long spear-like fin, loses its thick outer cap, or disconnects from the hub
- incorrect depth order where a rear weapon paints over foreground hair, face, hands, or armor; also reject an occluded component that fails to reappear consistently beyond the subject
- seams, halos, or background patches that expose the mask boundary

For size-only edits, compare the final image against both sources: use the target for pixel preservation and the design reference for component topology. Passing only one comparison is insufficient. Inspect separate full-resolution crops for the dominant blade, secondary blade, central hub, connector neck, shaft, and every foreground-occlusion boundary; never approve topology from a reduced montage alone. If the user marks a suspected gap, compare the same location in the design reference and decide explicitly whether it is intentional negative space, legitimate canvas/subject occlusion, or an accidental open-space termination before repairing it.

Only after topology and preservation both pass should the files be delivered.