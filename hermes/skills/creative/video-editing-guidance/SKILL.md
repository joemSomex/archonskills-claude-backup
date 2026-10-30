---
name: video-editing-guidance
description: Use when guiding video editing and compositing steps.
version: 1.0.0
metadata:
  hermes:
    tags: [video-editing, compositing, premiere-pro, beginner-guidance]
---

# Video editing guidance

Guide the user from their actual editor state to a working edit, especially when they supply screenshots or ask for Premiere Pro steps. Match their experience level as expressed now; being new to an editor does not mean they need instructions to find a timecode for every operation.

## Workflow

1. **Identify the intended composite.** Ask what remains fixed and what moves only if the supplied image and description leave it ambiguous. Distinguish footage revealed *inside* logo letterforms (track matte) from footage playing *behind* an untouched logo (ordinary layered composite). For a website hero, prefer exporting the motion background and keeping the original transparent logo as a separate page layer; a flattened screenshot does not provide a clean alpha logo.
2. **Read the current screen and track mapping before naming a control.** Inspect the latest screenshot and use the user's correction as authoritative for track contents. State the known V1/V2/V3 assignments; do not extrapolate whether an asset has transparency or enough timeline duration from its thumbnail alone. Do not send the user through generic sequence setup when the sequence and layers are already in place.
3. **Choose the least complex technique that produces the requested look.** If a transparent logo is above the montage, that alone preserves the logo; add an inverted opacity mask on the footage only when the original background must remain visible in a protected area around the logo. Place a darkened background montage below the fixed logo, and check contrast, cut rhythm, autoplay mute, and loop seams when intended for a website.
4. **Version-check the editing UI before giving click paths.** In Premiere Pro, opacity-mask shape controls may appear under Effect Controls in older versions, but newer masking interfaces move ellipse/rectangle/pen controls to the Tools toolbar and may create an unassigned mask that must be assigned to Opacity. Use the visible UI or current Adobe documentation to identify the correct path; do not insist a missing button is under Opacity. For an inverted mask, verify its target effect and preview the result before instructing feather or export.
5. **Give bounded, actionable steps.** For a novice, offer one operation at a time and ask what changed on screen. When they say to skip ahead or demonstrate familiarity, switch immediately to concise effect-specific instructions. Identify the selected clip, panel, tool, operation, and expected preview change; do not ask an unnecessary confirmation about an already stated decision.
6. **Verify output, not merely setup.** Preview several frames and the loop seam, ensure logo pixels/shape stay unchanged and background assets last for the full sequence, then inspect the exported file or site composite when available. Never claim the edit or website was made when only guidance was given.

## Pitfalls

- Do not recommend a track matte when the intended motion is behind the logo: it reveals footage through the logo and reverses the requested effect.
- Do not invent UI controls from an older Premiere layout: interface changes can make an otherwise correct masking method impossible to follow.
- Do not confuse a composited preview with proof that the logo asset is transparent or unchanged: inspect the actual source layer before promising pixel preservation.
