---
name: youtube-shorts-title-desc
description: Use when writing Quantum 13 YouTube Shorts metadata.
version: 1.0.0
author: Somex Studios, Hermes Agent
metadata:
  status: approved
  hermes:
    tags: [marketing, youtube, shorts, somex-studios]
    related_skills: [somex-content-calendar, quantum-13-canon, youtube-algorithm-advisor]
---

# Somex Studios - Quantum 13 YouTube Shorts metadata

Write and review Shorts titles and descriptions for Quantum 13. Optimize for both new-viewer discovery and a useful path to the full episode. Draft only; do not upload, edit, schedule, or publish. Keep this separate from the content-calendar skill, which owns placement, and the Community-post skill, which owns Community copy.

## When to Use

Use for requests to optimize, draft, compare, or revise Quantum 13 YouTube Shorts titles and descriptions. Do not use for scheduling, editing the video, or drafting unrelated Community posts. Treat every output as a proposal until the user approves it.

## Inputs and evidence

- Get the episode number and, when available, the actual Short clip or its complete transcript/shot list. When the user does not send video, accept exact start/end lines, duration, and scene summary as a bounded alternative. Check the episode's produced summary in the project database and cross-check the supplied cut boundary against governing subtitles. Use the lightweight review below to minimize image/context tokens; a single opening frame or line does not establish the rest of the cut. The World Bible checks continuity but does not authorize an unreleased reveal.
- Read `references/channel-examples-and-evidence.md` before claiming that a title pattern or description element worked on this channel. Treat title/description examples, public view counts, and aggregated Shorts totals as different types of evidence. Correlation is not causal proof. Do not promise reach, SEO rank, or episode clicks from a metadata change.

## Lightweight clip review

When the user uploads a Short, inspect its duration and available captions first. If the user prefers not to send the video, accept the exact start and end lines, length, and a scene summary; cross-check against the produced episode subtitles, write only what that span supports, and disclose that the edit itself was not visually checked. Read only the matching produced-episode scene summary and subtitle span, not the whole canon library. Sample roughly 6-10 frames spread across the entire clip, ideally as one timestamped contact sheet, and read a concise dialogue transcript where available. Do not dump raw full-resolution frames, large transcripts, or an exhaustive video report into context. If edits are rapid or a sampled moment contradicts the summary, inspect only the uncertain interval with a few extra frames. Do not send audio to a transcription service without the user's approval; if words cannot be verified locally, avoid quoting them or ask for a transcript. Sampling supports a scoped on-screen claim, not a claim to have watched every frame. If the footage remains ambiguous, say what cannot be verified rather than inventing a scene. Return only the requested metadata, not the analysis log.

## Write the package

1. Lead with the clip's own concrete moment, character, or tension. Give the viewer a reason to watch without implying a scene, outcome, or emotion not shown. Avoid spoilers **beyond the clip**, including from later parts of the same released episode. Do not use development-only events, unresolved theory as fact, or 'upcoming' and 'out now' without checking current release state.
2. Use Title Case for a hook matching the clip's visible action: an actual line of dialogue, core conflict, or emotional beat. Put it first, followed by the **fixed, exact suffix** ` | QUANTUM 13, A Sci-Fi Action Series with Undead Cyborgs vs Superhumans`. The suffix occupies 72 characters; enforce the user's stricter **27-character maximum for the hook**, and count the complete title to ensure it is no more than 100 characters before finalizing. Do not shorten or change the suffix. The hook should still convey the point when mobile truncates the title around 40-50 characters. Provide one title by default, or usually 5-10 genuinely distinct options if the user asks for choices.
3. Follow `references/description-format.md` for the user's preferred **layered description**: a clip-specific opening about the named characters; a divider; the supplied, fixed Quantum 13 series-premise paragraph; another divider; a developed, clip-specific context paragraph and closing beat; then a spoiler-safe call to action, verified matching episode and playlist links, and the exact hashtag line `#quantum13 #quantumxiii #scifi #action #cyberpunk #somexstudios`. Keep prose flowing and the clip-specific material within the verified cut. The series name in new copy is `QUANTUM 13`; the legacy-form hashtag is expressly requested. If links are missing, leave clear draft placeholders and never call the result publish-ready.
4. Verify episode summary against the actual edit when available, or against the user-provided exact clip boundaries and subtitle span when the video is unavailable. Check names, dialogue if quoted, hook length, and spoiler boundary. Do not imply an event beyond the verified clip span, a future release promise, or an unverified production claim. If even the boundaries cannot substantiate the claim, ask for the missing detail rather than describing unseen footage as fact.

## Learning from channel results

- Compare like with like: Shorts only, same channel, comparable clip topic and age since publication. Track each clip's URL/ID, title, description, publication date, duration, views and engaged views where supplied, viewed-vs-swiped-away, average view duration or percentage viewed, traffic source, and measured full-episode click behavior if available. The title alone cannot explain a view-count difference when clip, publication age, promotion, and audience differ.
- Separate observed results from hypotheses for next titles. Treat the supplied screenshot and CSV as a directional baseline, not a controlled test or proof that long titles/long descriptions caused performance. When more results arrive, update the evidence reference rather than silently changing the creative rules.

## Output

In chat by default: one `Title:` and one `Description:` following the layered reference format, without prefatory analysis. If asked for choices, usually give 5-10 genuinely different options in the requested scope. If asked for only a title or description, return only that component. If a summary or screenshot cannot substantiate the cut, ask for exact start/end lines or the clip; never claim to have seen an uninspected edit. Do not create an external document unless requested.

## Resources

- `references/channel-examples-and-evidence.md` - Read for the supplied title/description examples, the Shorts-only aggregate, the screenshot's visible ranking, and evidence limits.
- `references/description-format.md` - Read before producing Shorts copy for the user's preferred layered description format, approved wording, and lightweight review requirement.
