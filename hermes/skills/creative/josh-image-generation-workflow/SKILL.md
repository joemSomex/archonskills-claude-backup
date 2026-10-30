---
name: josh-image-generation-workflow
description: Applies Josh's workflow to strict reference-image tasks.
version: 1.1.0
author: Somex Studios
license: Proprietary
metadata:
  hermes:
    tags: [Image Generation, References, QA, Prompting]
    related_skills: [reference-driven-image-generation, pixel-preserving-image-compositing]
---

# Josh Image Generation Workflow

Apply Josh Makazo's fidelity-and-revision control layer to reference-image work. Use this overlay when a request emphasizes strict fidelity, exact reference roles, preserving accepted elements, revising only one part, or producing controlled variations. Trigger on phrases such as "use Josh's workflow," "keep the face and clothing exact," "fix only this part," "strictly follow each reference," and "make controlled variations."

## When to Use

Use for character portraits, wardrobe transfers, product or prop renders, cinematic key art, collectible-card imagery, pose-matched generations, and revisions where reference authority must remain explicit across iterations.

Load `reference-driven-image-generation` first and use it as the single source of truth for reference analysis, prompting, generation mechanics, visual geometry, and general QA. Apply this skill only for Josh's stricter fidelity and revision discipline. When the user requests image generation, do not describe a proposed image or prompt and wait for approval; proceed with generation when the required inputs are available.

If every pixel outside a named edit region must remain unchanged, load `pixel-preserving-image-compositing` and use deterministic compositing instead of generative revision.

## Josh Control Layer

### 1. Establish the reference contract

Before prompting, write a compact role contract for every source:

- **Authority:** the attributes the source controls.
- **Exclusions:** the attributes it must not contribute.
- **Priority:** which explicit user lock wins if sources conflict.

Treat the contract as stable across the task. Revise it only when the user replaces, adds, revokes, or reassigns a reference. Never infer roles from upload order alone.

### 2. Establish the acceptance state

Track each major category as `unresolved`, `accepted`, or `reopened`:

- identity
- wardrobe or product construction
- pose and anatomy
- composition and camera
- lighting and atmosphere
- background
- effects and props
- file properties

Once the user accepts a category, lock it. Do not reopen it merely to improve another category. Reopen only what the user explicitly changes or what must change to resolve a direct physical conflict.

### 3. Calibrate before multiplying

When several outputs share an uncertain property, generate and inspect one calibration image first. Resolve the shared identity, garment, product design, framing, scale, pose, or lighting issue before creating the remaining variations.

Do not repeat an unverified defect across a batch. After calibration passes, carry its measurable visual properties into later prompts without using the generated image as a reference unless iterative editing was explicitly requested. Calibration is an internal QA step, not a request for user approval unless the user asks to review a sample first.

### 4. Enforce a one-variable variation budget

Give each variation one declared difference, such as expression, head angle, gaze target, hand placement, or background accent. Keep accepted categories unchanged.

Reject a "variation" that silently changes identity, wardrobe construction, camera distance, palette, or another locked category. Generate every standalone output from the original governing references.

### 5. Revise surgically

Classify each failure before editing: identity drift, reference leakage, design drift, pose mismatch, anatomy or count error, composition error, lighting mismatch, unwanted text, or file-property failure.

Name the single failed category and preserve every accepted category in the revision instruction. Remove stale clauses that conflict with the correction. Use deterministic crop, padding, translation, or resizing for mechanical layout failures rather than generative redrawing.

### 6. Require evidence before acceptance

Before accepting or delivering any output, read `references/practical-qa-checklist.md` and apply every relevant gate. Treat the rendered pixels and verified file properties as the evidence; prompt wording alone never proves compliance.

When a required gate fails, reject or correct the image. Deliver only accepted standalone files and report briefly what was produced, what was verified, and what remains unresolved.

## Durable Learning Rule

Add a lesson to this skill only when it is distinctive to Josh's approval discipline. Add generally applicable prompting, geometry, generation, or QA lessons to `reference-driven-image-generation` instead. This boundary prevents duplicate rules and drift between the two skills.

## Provenance

This skill codifies practical control methods strengthened through image-generation work with Josh Makazo. It stores reusable craft rather than temporary conversations, transient attachments, or project-specific image files. Attribution does not override current user instructions or project-specific creative authority.

## Resources

- `references/practical-qa-checklist.md` — mandatory acceptance gates before any image is approved or delivered.
- `reference-driven-image-generation` — authoritative shared procedure for analysis, prompts, generation, visual geometry, and general QA.
- `pixel-preserving-image-compositing` — authoritative workflow when unchanged pixels are mandatory outside the edit region.
