# Practical QA Checklist

Apply only the gates relevant to the active brief. A failed required gate rejects the output.

## Reference fidelity

- Confirm that every reference has an explicit role.
- Compare the face against the identity source: face shape, eye geometry and color, brows, nose, lips, skin tone, marks, hairline, part, color, and length.
- Compare wardrobe or product construction against its source: silhouette, panels, seams, closures, materials, colors, trim, wear, graphics, and hardware.
- Reject identity, wardrobe, pose, background, typography, or color leakage from references not assigned those roles.

## Composition and camera

- Check subject centerline separately from hair, capes, effects, and props.
- Check shot size, headroom, lowest visible anatomy, negative space, depth relationship, and intended crop edges.
- Verify camera height and angle through visible perspective, not the named camera or lens alone.
- Compare apparent object scale and apparent room width when the brief specifies a relative size.

## Pose and anatomy

- Trace shoulder to elbow to wrist for every visible arm.
- Verify head pitch, head yaw, and eye direction independently.
- Count people, human arms, hands, fingers, nonhuman appendages, props, blades, muzzles, tips, strings, and chains when constrained.
- Confirm hand-to-prop contact, wrist continuity, palm orientation, finger state, grip direction, and prop trajectory.
- Reject fused, duplicated, disconnected, hidden, or anatomically impossible structures.

## Lighting and atmosphere

- Verify key-light color, direction, angle, lit planes, shadow side, rim direction, fill level, contrast, and falloff.
- Distinguish background glow from light falling on the subject.
- Confirm that concealment, haze, bloom, grain, halation, and practical sources match the requested intensity rather than merely appearing somewhere.
- Reject unwanted competing colors and broad fill that reveals areas meant to remain dark.

## Image integrity

- Inspect the face, hands, props, distinctive marks, and lower 40 percent at full resolution.
- Reject unintended text, pseudo-text, logos, watermarks, UI, panel borders, collage layouts, and repeated subjects.
- Confirm sharpness or intentional blur in the specified regions.
- Confirm that approved regions remain visually stable after a targeted revision.

## File verification

- Confirm requested output count and one standalone image per file.
- Confirm file existence, encoding or format, pixel dimensions, and exact aspect ratio.
- Confirm cryptographic uniqueness when multiple unique files are required.
- Reinspect the final-size file after deterministic crop, padding, translation, or resize.

## Delivery gate

Deliver only outputs that pass every required visual and file-property check. State briefly what was produced, what was verified, and any requirement that remains unresolved.
