---
name: reference-image-prompting
description: Use when prompts depend on reference images.
---

# Reference Image Prompting

## Required behavior

- Proceed directly to the complete video prompt when the user asks for one; do not pause to obtain approval for reference mapping, an outline, or a draft. Recover relevant images from the active conversation where available and resolve ordinary visual choices from the brief. This permission is for prompt drafting, not for paid generation, changes to canon, attachment archiving, or durable memory writes.
- For every Seedance 2.0 or Seedance 2.5 prompt, first confirm that the required reference image or images are available. If none are attached or otherwise available in the active request or recoverable context, ask the user to provide them before finalizing the prompt.
- Before `Scene Overview`, always add a `REFERENCE IMAGE ASSIGNMENT` section that maps each supplied image token (for example, `@image1`) to its intended subject or function.
- State which visual properties each reference controls, such as identity, architecture, silhouette, materials, lighting, environment, or display content.
- Treat the assignment as the source-of-truth boundary and prevent unrelated visual traits from leaking between references.
- Do not claim to have inspected or assigned an absent reference.

## Example

```text
REFERENCE IMAGE ASSIGNMENT

@image1 is the tower reference. Treat @image1 as the sole source of truth for the tower’s architecture, silhouette, proportions, structural details, materials, and design language.

1.) Scene Overview
```
