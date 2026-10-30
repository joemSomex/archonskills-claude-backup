---
name: item-live-action-to-game-design
description: "Use when 'Item: Live Action to Game Design.' appears."
version: 1.0.0
author: Somex Studios + Hermes Agent
license: Proprietary
metadata:
  hermes:
    tags: [item-design, image-generation, animated-asset]
    related_skills: [reference-driven-image-generation]
---

# 道具：真人影视改编游戏设计 (Item: Live Action to Game Design)

## When to Use

When the user says `Item: Live Action to Game Design.` with an attached image, treat that image as `@image1` and execute the ten-image generation workflow without asking for confirmation. Match capitalization-only differences. If no image accompanies a new invocation, ask for the item image rather than silently reusing an earlier one. A discussion or quotation of the phrase alone is not a generation request. Do not import attributes from a previous item.

**Before generating, read `references/generation-brief.md` in full.** It is the user's exact authoritative brief; preserve its requirements in every generation prompt. Inspect the original at useful resolution and record its shape, proportions, visible front/side/back evidence, structural connections, repeated features, materials, palette, emitters, and distinguishing details. For mechanical objects, also load `creative:reference-driven-image-generation` and its linked complex-prop-fidelity resource for topology and QA. The four views in each output depict one item, not four unrelated designs. Infer unseen surfaces conservatively and disclose that inference.

## Generate and verify

Use **ChatGPT/OpenAI image generation only** for this user's image work; never switch to Claude or Higgsfield. Generate ten independent images, each directly from the original `@image1`, never from a preceding variation. Lead every prompt with the full design/fidelity and four-view layout requirements, plus one controlled rendering-direction variation. Use a clean light-neutral studio and keep each image one standalone sheet. Do not substitute a photoreal filter, smooth CGI, different functional object, or a collage of all ten. When a shared style/layout problem appears, inspect one internally corrected generation before continuing the remaining slots, rather than repeating the same failed prompt ten times. For photo/CG source boards that repeatedly yield nearly identical glossy turnarounds, stop the batch at calibration: compare a design-only original reference plus style-only material evidence against a text-led painterly version. Reject a style change confined to paper/background, and reject text-led versions that visibly alter the item's connection graph or silhouette. Do not fill ten slots with near-duplicates merely to satisfy count; present the unresolved style-versus-topology tradeoff and request a concrete hand-painted prop style exemplar or another approved direction.

Honor the user's standing direct-delivery preference: do not make contact sheets, inspect generated images, or run correction loops unless the user explicitly asks for review. Still check file count, PNG format, exact ratio, and distinct hashes; do not claim visual acceptance. When review is requested, inspect four-view consistency, silhouette, topology, materials and painterly finish, replacing only failed slots.

Save each result as an individual PNG. Programmatically verify exactly ten files, PNG encoding, exact 16:9 aspect ratio, ten distinct hashes, and a source-linked manifest. If a generated canvas is nearly 16:9, minimally crop safe margins without distorting the object, then recheck the final file. Deliver the ten individual PNGs in chat, not the contact sheet as a substitute. These are 2D rendered design sheets, not editable 3D models.

## Resources

- `references/generation-brief.md` - mandatory verbatim user brief; read in full on every invocation.
