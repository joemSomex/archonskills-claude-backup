---
name: reference-driven-key-art
description: Use when generating reference-driven cinematic key art.
---

# Reference-Driven Key Art

## Workflow

1. **Map every reference before generating.** Assign each supplied image a single role—page background, panel background, design language, layout, or named character—and inspect enough to verify that the path matches the claimed content. Trust visual content over attachment ordering when the two disagree.
2. **Put `REFERENCE IMAGE ASSIGNMENT` first.** State what each image controls and what must not leak from it. If a required reference is absent, ask for it before finalizing or running the prompt. Never claim to have inspected a missing reference.
3. **Separate structural constraints from art direction.** Restate exact canvas size, aspect ratio, panel count, panel order, equal sizing/alignment, reserved negative space, and forbidden content in a compact geometry block. Then state character fidelity, lighting, atmosphere, and camera treatment.
4. **Generate the requested count as real independent files.** Use the original references in every direct generation; never use one generated image as the identity source for another. When repeated multi-reference calls are rejected externally, diagnose once, then use a compliant successful generation as an edit base for additional variants while explicitly locking character order, identity, panel geometry, and prohibitions.
5. **QA every output visually.** Check exact character/panel count and order, equal geometry, reserved negative space, correct background isolation, identity/costume fidelity, prohibited text/logos/extra people, and any signature pose or motif. For a multi-card character batch, inspect a numbered contact sheet plus native-size visor/face, held-prop and reserved-space crops: an action pose can shrink the identity focal point, a foot or shield can intrude into the text-safe region, and different hashes can still hide duplicate compositions. Replace failed slots from the original references rather than accepting a darkened/cropped defect.
6. **Use deterministic post-processing for deterministic requirements.** Image models are unreliable at exact percentages, source-background fidelity, pixel-perfect card geometry, 1px borders, and selected-card states. Composite accepted panel interiors onto the exact supplied background with Pillow, uniformly scale then center-crop when panel ratios differ, and redraw final-resolution borders/glows—including active-state styling—after placement. Never squeeze character anatomy to hit a card ratio. Render strict copy-bearing UI with HTML/CSS and headless Chromium. See `references/layout-verification.md`.
7. **Verify before delivery.** Programmatically confirm output count, PNG format, dimensions, and unique hashes. Deliver descriptive absolute paths with a short verification note; do not replay the generation process.

## Always-on rules

- Preserve reference assignments and content boundaries exactly; a layout reference must not leak its characters, text, or logos into the result.
- Treat “exactly N,” ordering, empty navigation space, and equal panel dimensions as acceptance gates, not aesthetic suggestions.
- Keep reference images local and reusable, but never archive them unless the user explicitly asks to remember, save, archive, or add them to the brain.
- For strict website text and card layouts, prefer deterministic HTML/CSS rendering over image generation because generative models misspell and drift.
- When a safety filter falsely flags an adult character prompt, clarify that all subjects are adults, fully clothed, and non-sexual; preserve the requested design rather than omitting the character.
- Do not invent labels, file codes, metadata, UI controls, or copy that the user did not supply.
