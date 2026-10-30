---
name: cinematic-video-prompt-workflow
description: Use for cinematic prompts, shot conversion, and revisions.
version: 1.0.0
author: Somex Studios + Hermes Agent
license: Proprietary
metadata:
  hermes:
    tags: [cinematic, video, prompt-writing, continuity, performance]
    related_skills: [quantum-13-canon, fiction-canon-management]
---

# Cinematic Video Prompt Workflow

Turn story material into visually executable, model-ready video prompts while preserving approved creative decisions. Apply when asked to write a video prompt, turn a scene into a shot, revise only part of a prompt, keep exact wording, or invoke `/cinematic-video-prompt-workflow`. Keep general filmmaking method separate from project-specific canon, character bibles, and authenticated author decisions.

## When to Use

Use for story-to-video prompting, screenplay-to-shot translation, character-performance direction, continuity-sensitive shot design, model-ready dialogue and timing, surgical prompt revisions, and management of multiple creative alternatives. Load the relevant canon skill alongside this one whenever the prompt belongs to an established story world.

## Scope and source precedence

Gather the active sources before drafting. Apply this field-specific precedence order:

1. Treat the current user instruction as the active task scope and highest authority for fields it explicitly changes.
2. Preserve explicit locks and current supplied assets for the wording, identity, composition, voice, or other fields they directly define unless the user reopens them.
3. Apply authenticated project canon and produced continuity to established story facts and shot-to-shot state.
4. Apply durable preferences to formatting, presentation, and recurring choices not fixed above.
5. Use this skill's craft defaults only where higher sources are silent.

Load any matching project canon or continuity skill. Keep screenplay text, produced audiovisual continuity, development alternatives, and interpretation source-labelled when they differ. Resolve conflicts within the field each source authoritatively defines; a newer formatting preference cannot override locked dialogue, canon, or a current reference asset.

## Execution without draft approval

An authenticated request to write or revise a video prompt authorizes drafting and delivery in the same turn. Do not stop at a concept, outline, reference interpretation, sample, or proposed split to request approval first. Resolve ordinary creative choices with the active brief and established references, then deliver the completed prompt. If runtime requires multiple clips, produce the appropriately labeled continuous parts unless the user asked for only one part. Ask only when a genuinely missing required input cannot be recovered or a consequential ambiguity would change the intended scene. This does not authorize generation spending, changing canonical source material, archiving attachments, or writing durable memory without the authority those actions require.

## Workflow

### 1. Establish the shot contract

Identify the generation target, model or platform when known, clip duration, aspect ratio, source scene, starting frame, ending state, dialogue or audio reference, required continuity, and forbidden changes. Assign every supplied reference one explicit role - identity, wardrobe, composition, material treatment, starting frame, or another named field - and never invent a missing reference or silently reassign one. Before declaring a reference missing, audit attachments across the relevant recent turns, including images attached to turns whose prior assistant response failed or was interrupted; those attachment paths may still be readable. Enumerate each named slot and its verified asset path, inspect unresolved candidates, then state a gap only after this check. A failed response does not mean the user's image was never delivered. When a scene reference defines the opening image, begin from that frame and describe the intended delta rather than rebuilding the scene from scratch. When a platform is named, consult supplied or current authoritative documentation for supported syntax, duration, aspect ratio, reference-media behavior, audio, negative prompting, and camera controls. Adapt to supported controls and omit unsupported syntax rather than guessing. Use sensible defaults only when they do not change the creative outcome. Ask a question only when missing information would materially alter the shot.

Name the active version or option before writing. If several alternatives exist, select the one named by the user and exclude sibling-only material.

### 2. Extract the dramatic beat

Reduce the source to what changes during the clip:

- the subject's immediate objective;
- the visible obstacle or pressure;
- the emotional turn;
- the physical action that expresses that turn;
- the final image or state that hands off to the next shot.

Preserve internal thoughts only when they can be translated into visible or audible evidence. Do not paste screenplay prose that a video model cannot render.

### 3. Build the visible shot

Specify only production-relevant information: subjects and identity anchors, environment, spatial relationships, blocking, action order, camera framing and movement, lighting, atmosphere, performance, dialogue, sound, and timing. Keep cause before effect and preserve screen direction, eyelines, object possession, injuries, wardrobe, weather, and beginning/end states. For dialogue scenes, make speaker orientation, gaze, turns, and reaction beats support the dramatic exchange instead of competing with it. For holographic, crystallized, archival, or memory imagery, keep the depicted world visibly alive through restrained motion and apply the chosen treatment coherently to characters, clothing, architecture, props, and atmosphere unless the user specifies a narrower effect.

Use concrete observable verbs. Replace abstractions such as "she realizes the truth" with visible behavior such as a held breath, a gaze shift toward the evidence, a restrained recoil, or a changed delivery. Avoid stacking unnecessary micro-actions that make performance robotic.

For detailed craft choices, read `references/craft-guide.md`.

### 4. Direct performance without over-directing

Anchor performance in objective, emotional pressure, restraint level, and a small number of legible signals. Before directing acted speech, read the performance and dialogue sections of `references/craft-guide.md`.

Keep approved dialogue exact. Do not paraphrase, polish, translate, or reassign a locked line. Treat supplied audio as authority for the vocal fields it demonstrates unless the user says otherwise.

### 5. Protect continuity and canon

Run a preflight against the active sources:

- identity, age, appearance, eye colour, wardrobe, injuries, and carried objects;
- abilities, limitations, technology, and transformation state;
- location, time, weather, lighting, and spatial geography;
- chronology, character knowledge, reveal order, and unresolved mysteries;
- starting pose and state inherited from the prior shot;
- final state required by the following shot.

Separate explicit fact, strong implication, and creative interpretation. Do not invent lore, motives, relationships, memories, powers, or connective events merely to make a prompt feel complete.

### 6. Write for generation reliability

Use a clear instruction hierarchy and one coherent action timeline. Keep character labels stable. Attribute every spoken line. Eliminate contradictory camera, lighting, movement, emotion, and timing instructions. Use negative constraints only for likely failure modes; do not bury the desired shot under a long prohibition list. If a model rejects or repeatedly misreads a prompt, simplify it: retain the core reference mapping, action, performance, camera, timing, and essential constraints while removing repetition and decorative detail.

Use copy-safe ASCII punctuation when required by the destination: straight quotation marks and apostrophes, three periods instead of a Unicode ellipsis, and plain hyphens instead of typographic dashes. Preserve an explicitly locked non-ASCII character when exact source fidelity takes precedence.

Fit the requested action to the available duration. Prioritize the dramatic beat over ornamental camera movement. If the scene cannot plausibly fit, state the constraint briefly and deliver a usable split into continuous clips; do not pause for approval of the split unless the user fixed an incompatible single-clip requirement.

### 7. Apply revisions surgically

Interpret "change only," "keep everything else," "use this exact wording," and similar language literally. Freeze unaffected content before editing. Modify only the named fields or bounded passage, then compare the result against the prior version. When content is removed, remove every operative occurrence from dialogue, timing, summaries, locks, examples, and negative constraints so stale wording cannot leak into generation.

Do not use cleanup as permission to alter story logic, performance, dialogue, timing, camera, formatting, or sibling versions. Repair only mechanical contradictions introduced by the requested change. If a requested correction supersedes an older approval, update the stale summary rather than treating the new instruction as a conflict.

### 8. Isolate alternatives

Give every durable alternative a stable label. Maintain a small version ledger in the working context: shared facts, option-specific facts, exact locks, and unresolved decisions. Never silently merge alternatives.

When one option is revised, edit only that option unless synchronization is explicitly requested. If shared continuity must change across several options, apply it deliberately to each and retain legitimate ending, staging, dialogue, or runtime differences.

### 9. Validate before delivery

Check the final prompt against these gates:

- **Executability:** every important instruction can be seen, heard, or timed.
- **Causality:** actions occur in a coherent order and produce the stated result.
- **Continuity:** identities, state, geography, knowledge, and handoffs match the sources.
- **Performance:** direction is playable, character-specific, and not mechanically overloaded.
- **Dialogue:** wording, speaker, delivery, and audio authority are correct.
- **Camera:** framing and movement support the beat without contradiction.
- **Timing:** the action fits the clip or is explicitly split.
- **Reliability:** punctuation, labels, and constraints are model-safe.
- **Scope:** no unrequested changes or cross-version leakage were introduced.

For revisions, compare the changed version with the previous one and confirm that only intended differences remain. Deliver the substantive prompt in chat unless the user explicitly requests a file.

## Collaboration and durable learning

Treat corrections as evidence, not as isolated patches. Classify a repeated or broadly reusable correction and propose the appropriate durable destination:

- general procedure and craft rules belong in this skill;
- project-specific continuity belongs in the matching canon skill;
- authenticated person-specific decisions or preferences belong in GBrain with provenance;
- exact source material and locked passages belong in the project archive.

Require explicit user instruction or approval before writing any correction to durable state. Without approval, present the proposed rule and destination only. Do not turn one subjective note into a universal rule without repeated evidence or explicit instruction. Preserve attribution when a collaborator's decision governs future work, and verify every approved durable write before claiming that later chats can use it.

## Resources

- `references/craft-guide.md` — read when choosing camera, blocking, performance, dialogue, timing, negative constraints, or scene-to-shot translations.
