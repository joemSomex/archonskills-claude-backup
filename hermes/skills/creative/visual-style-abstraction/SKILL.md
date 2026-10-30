---
name: visual-style-abstraction
description: "Use when abstracting visual style into original prompts."
version: 0.1.0
author: Somex Studios, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Visual Analysis, Style, Prompting, Originality, Chinese]
    related_skills: [watch, humanizer]
---

# Visual Style Abstraction / 视觉风格抽象

Analyze a visual reference and convert its transferable design logic into an original prompt without reproducing recognizable intellectual property. Use evidence across the whole work, separate design systems from signature assets, and make the resulting prompt usable with a different subject, brand, palette, and medium.

## When to Use

- “Break down this video’s design into a prompt I can reuse.”
- “I like the aesthetic, but do not copy its iconic traits.”
- “Extract the visual grammar from these images.”
- “把这个视频的视觉风格提炼成原创提示词。”
- “保留审美逻辑，但不要复制标志性元素。”

Do not use for requests to reproduce logos, characters, exact interfaces, or other protected identifiers.

## Language Handling

Answer in the requester’s language. Keep filenames, timestamps, IDs, and source titles unchanged. Present the skill name bilingually when listing it.

## Default Delivery

Return the result in chat unless the user asks for a file, using this order:

1. **Transferable design language** — evidence-grounded bullets covering composition, geometry, typography, palette, texture, subject treatment, depth, and motion.
2. **Reusable master prompt** — one fenced prompt with clear placeholders such as `[SUBJECT]`, `[MESSAGE]`, and palette roles so it can be applied to unrelated designs.
3. **Originality guardrail** — a separate tailored block naming the recognizable source traits that must not transfer.
4. **Compact prompt** — include only when it materially helps copy/paste use; it must preserve the same originality boundary rather than weakening it.

## Procedure

1. **Define the abstraction target.** Record the source, target deliverable, intended subject, practical format, and the user’s originality boundary. Distinguish “inspired by broad design principles” from “recreate this exact look.”

2. **Acquire verified visual evidence.** Use the `watch` workflow for public videos. Try the normal public download once. If a platform blocks it, stop repeating the same endpoint and look for an official or reputable syndicated copy of the exact title. In a browser, inspect embedded `<video>` sources when permitted, verify title and duration, download the public media, then run the local file through `watch`. Never use private cookies or login workarounds merely to defeat a bot wall.

3. **Sample the complete work.** Inspect scene-change frames, evenly spaced frames across the full runtime, and a dense half-second opening pass when the hook matters. Create labeled contact sheets for efficient inspection. Inspect every frame used as evidence; do not claim to have watched uninspected material.

4. **Decompose the design system.** Analyze composition, negative space, information density, palette logic, typography hierarchy, geometric vocabulary, subject treatment, image/3D integration, texture, lighting/materials, depth, transition grammar, motion rhythm, and audio only when verified. Cite timestamps for representative moments.

5. **Separate transferable from iconic.** Use `references/originality-boundary.md`. Signature logos, named characters, exact symbols, proprietary wording, distinctive silhouettes, exact UI arrangements, unique transition sequences, and signature palette combinations are excluded. Structural principles such as asymmetric information islands, source-bound color roles, data-to-object continuity, controlled distortion, and pacing contrast are candidates for transfer.

6. **Rebuild around the user’s subject.** Derive diagrams, labels, measurements, and motifs from the new subject’s actual function, anatomy, construction, behavior, or meaning. Choose a new palette and typographic system. For character prompts with several references, assign each one a bounded role (such as facial mood versus armor material), then specify the new person's anatomy, visible skin, and the intended cloth-to-armor balance; otherwise a mech-material reference can swallow a human costume. For a requested batch of independent designs, plan distinct silhouette families, body builds, and facial identities before separate generations; changing archetype labels alone leaves near-duplicate armor geometry. For hard-surface product batches, assign each concept a different functional chassis topology, propulsion placement, and sensor arrangement before separate generations, not just a different panel pattern or color. Render one design first to calibrate framing and palette, then review a labeled contact sheet midway and at completion; replace lookalike silhouettes or designs that accidentally copy the references. When a concept is insufficiently futuristic, redesign its primary shell masses and component connections before recoloring: vary outer-shell masses, rear supports and front enclosures across the batch. If a futuristic product batch is corrected as too heavy or mechanically busy, rebuild each silhouette with a thin low-profile continuous shell, flush optics and concealed propulsion; reserve only a few functional seams and short accent-light dashes. Do not merely remove surface details from the same bulky chassis, because the thickness and exposed attachments carry the unwanted visual weight. Distinguish variants by overall planform, wing topology, propulsion placement and sensor arrangement while keeping the shared restrained material language. Carry later user exclusions of chassis families as hard silhouette vetoes across the entire new batch: translate each prohibited name into visible thumbnail geometry and reject lookalikes even when their mechanisms or labels differ (for example, a U-bridge can still read as two parallel pods). If the user then permits richer futuristic industrial detail, restore it locally at wing roots, optics and propulsion interfaces with shallow layers and fine seams, not by reviving a forbidden topology or thickening the whole chassis. Treat the latest reference's negative spaces as optional, not mandatory. If the user permits openings only around the trigger and handgrip, specify one continuous opaque fore-end, receiver and stock in positive geometry; prohibit split prongs, vent slots and see-through rear frames, then inspect every white opening inside the silhouette at full size. Bind a two-tone matte palette to named physical layers and relative visible area: put the dominant color on every broad plane, including wing webbing, membranes, infill and underside shells, and confine the secondary color to narrow joints, vents or connectors. Inspect broad surfaces at thumbnail scale before batching, because a dark membrane can dominate the silhouette even when the fuselage is white. When the requested accent is only a trace, specify its tiny footprint and exact physical locations (such as short status-light dashes), and exclude competing colored glows; otherwise image generation expands it into broad trim or swaps in a source-reference light color. For unarmed sensing products, give projecting optics a broad blunt camera housing with visibly distinct glass apertures instead of a long narrow tube, which reads as a gun barrel even when described as a sensor. Inspect one calibration image at thumbnail size before scaling the batch; panel-line changes or a color grade on an old silhouette do not constitute a new design. When generation cannot produce a fresh design, offer a clearly labeled material-only edit only with the user's agreement and never deliver that edit as a redesign. If a full-body reference keeps overpowering the silhouettes, use a verified crop of its material/joints for some variants while retaining its assigned reference role, then compare the batch together when visual review or correction is requested. Replace recognizable props, makeup patterns, and silhouettes with new functional motifs instead of naming them only in a negative prompt. Do not leave the source title, brand, or fictional terminology inside the generated prompt.

7. **Write one universal master prompt.** Use `templates/style-abstraction-prompt.md`. Include the new deliverable, subject, composition, subject treatment, graphic system, palette, typography, texture, lighting/material, depth, and output requirements. Add an originality lock that explicitly forbids recognizable source assets while preserving only high-level design principles.

8. **Add medium-specific guidance only when needed.** For motion, add a progression and transition clause. For static design, omit motion language. For UI, prioritize hierarchy and interaction states. For packaging, bind every graphic element to material, print process, and physical placement.

9. **Verify the result.** Ensure the prompt works without naming the source, uses project-specific content, changes the signature palette and motif set, contains no copied wording or symbols, and still expresses the extracted high-level grammar.

10. **Complete the evidence report.** When using `watch`, fill every pending report marker and preserve the work directory for follow-up unless cleanup is requested.

## Always-On Rules

- Analyze the whole reference, not a thumbnail or one hero frame.
- State what is visible separately from what is spoken; never infer a transcript from visuals.
- Describe systems and relationships rather than “in the style of” a named property.
- Use glitch, grain, typography, or color only when they perform a defined role; generic decoration weakens the abstraction.
- Include a concise “do not copy” list tailored to the source’s recognizable features.
- Preserve timestamps in the breakdown so the user can verify the evidence.
- Prefer one adaptable prompt over several near-duplicate variants unless the user asks for alternatives.

## Pitfalls

- **Do not substitute a nearby mirror without verifying title and duration** — visually similar uploads may be different edits.
- **Do not call generic neon HUD decoration a design system** — identify hierarchy, density, geometry, and state logic.
- **Do not preserve the exact palette while claiming originality** — signature color relationships can be as recognizable as logos.
- **Do not overuse glitch** — controlled corruption works as transition/state punctuation; constant noise erases hierarchy.
- **Do not copy technical labels or fake codes** — generate project-specific terminology from the new subject.
- **Do not let a negative prompt carry the design** — specify what the new system positively does first.

## Verification

- Full-runtime, scene-change, and opening-hook evidence was inspected as applicable.
- Representative claims carry timestamps.
- Transferable and iconic traits are explicitly separated.
- The prompt names no source property, creator, character, or logo.
- Palette, typography, motifs, wording, and sequence are original.
- Every diagnostic/graphic element derives from the new subject.
- A tailored originality lock and exclusion list are present.
- The final prompt is usable for the requested medium without additional explanation.
