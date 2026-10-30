---
name: youtube-algorithm-advisor
description: "Diagnose YouTube algorithm, CTR, retention, and reach."
version: 0.1.0
author: Jason Gelchen, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [youtube, algorithm, analytics, creator-strategy]
    related_skills: [youtube-content, social-video-audience-analysis]
---

# YouTube Algorithm Advisor

Diagnose YouTube performance as an audience-matching problem rather than a creator-reward system. Turn available analytics into testable explanations and prioritized actions. Distinguish observed evidence, plausible interpretation, and uncertainty; never imply access to YouTube's private ranking systems.

## When to Use

Use for requests such as:

- “Why did this YouTube video flop?”
- “Why are my impressions low despite a good CTR?”
- “Should I change the title or thumbnail?”
- “Does YouTube suppress or shadowban videos?”
- “Do Shorts subscribers hurt long-form videos?”
- “How should I use Community posts?”
- “Analyze my retention, CTR, or viewer mix.”
- `/youtube-algorithm-advisor`

Do not use for extracting transcripts or collecting comments; load `youtube-content` or `social-video-audience-analysis` for those tasks, then apply this skill to the resulting evidence.

## Core Model

Before advising, read `references/algorithm-principles.md`. Apply its audience-matching model without implying access to YouTube's private ranking systems. Treat impressions, CTR, retention, and subscribers as conditional signals rather than rewards, punishments, or guarantees.

## Inputs

Gather the cheapest available evidence. Ask only for fields that could change the recommendation:

- Video age, length, publication time, and whether the topic is time-sensitive
- Impressions and impression CTR
- Views and watch time
- Average view duration and average percentage viewed
- First 30-second retention and major retention drops
- Traffic-source mix: Browse, Suggested, Search, Shorts, External, Notifications
- New, casual, regular, and returning viewer metrics when available, including each metric's scope and date range
- Title and thumbnail
- Topic, intended viewer, and promise made by the packaging
- Upload cadence and production cost
- One or more genuinely comparable videos from the same channel over the same elapsed period
- Creator objective: reach, subscribers, revenue, leads, or community depth

If screenshots are supplied, use `vision_analyze`. If a YouTube link must be inspected, load `youtube-content` or `watch`. Never invent missing metrics.

## Diagnostic Procedure

### 1. Establish the evaluation window

Avoid firm conclusions from the first 24–48 hours unless the video is news-driven or otherwise perishable. Real-time metrics are estimates and early audiences are often unusually loyal.

For older videos, compare equal lifecycle windows: first day to first day, first week to first week, or first 28 days to first 28 days.

### 2. Choose a valid benchmark

Compare like with like:

- Same channel before another channel
- Same content pillar before channel-wide average
- Similar video length, format, topic breadth, and traffic source
- Same elapsed time since publication
- Similar upload cadence and seasonality

Reject comparisons between a new upload and a competitor's year-old viral result unless explicitly analyzing long-tail potential.

### 3. Verify current-policy claims when required

For questions about present feature behavior, enforcement, monetization, or decisions carrying material cost, retrieve current evidence from official YouTube Help or Creator Insider sources. Record the publication or update date when available. Label official guidance, interview testimony, observed analytics, and inference separately.

### 4. Locate the constrained stage

Use the metrics as a funnel, not as isolated scores:

- **Low impressions + strong aggregate CTR/retention:** inspect viewer mix, topic breadth, and packaging accessibility. Do not call this “core-audience performance” unless cohort-specific data actually supports that claim.
- **High impressions + weak CTR:** inspect topic demand, title clarity, thumbnail comprehension, novelty, and audience fit.
- **Healthy CTR + sharp opening drop:** inspect promise-delivery mismatch, slow setup, confusing context, or an opening that delays the value.
- **Healthy clicks and retention + weak new-viewer evidence:** treat audience expansion as one hypothesis; do not diagnose a shadowban.
- **Search-heavy traffic:** inspect query fit, answer quality, freshness, and vulnerability to AI-generated answers.
- **Suggested/Browse weakness:** inspect whether the topic and packaging make sense to viewers who do not already know the creator.
- **Broad weakness across clicks, retention, and viewer expansion:** revisit the topic-package-content combination rather than changing only the thumbnail.

Label every metric as video-level, channel-level, cohort-level, or traffic-source-level. Do not combine channel-level new/casual/regular viewer classifications with video-level CTR or retention as if they measured the same cohort and window. Present multiple plausible explanations when the evidence cannot distinguish them.

### 5. Decide whether to intervene

Change packaging when there is enough exposure to interpret the signal and the title/thumbnail hypothesis is specific. Prefer controlled YouTube thumbnail testing where available.

For expensive, infrequent, high-stakes videos, earlier packaging intervention can be rational. For frequent, lower-stakes uploads with small samples, capture the lesson and prioritize the next upload rather than swapping packaging repeatedly.

Do not prescribe universal CTR, retention, or view-duration targets. Competitive baselines vary by audience, traffic source, format, length, and distribution breadth.

### 6. Extend distribution only when relevant

Apply this branch only when the user asks about Community strategy, repurposing, or distribution extension. Treat Community posts as standalone content: extract one useful idea, question, quiz, image, poll, or carousel with value even if the viewer never opens the video. Avoid posting only “new video—watch now.” Evaluate Community impressions, engagement, subscriptions, and downstream viewing without claiming guaranteed video views.

### 7. Recommend the next experiment

Prioritize no more than three actions. Each action must contain:

- Hypothesis
- Change to make
- Metric to watch
- Comparison window
- Success or failure criterion stated relative to the channel's own benchmark

Prefer learning loops over one-off hacks.

## Response Format

Return:

1. **Bottom line** — one concise diagnosis
2. **Evidence** — metrics and observations supporting it
3. **What remains uncertain** — missing or confounded evidence
4. **Priority actions** — up to three ordered experiments
5. **Do not conclude** — myths or overclaims unsupported by the data
6. **Next data to collect** — only fields that would materially change the diagnosis

When the user asks for strategy rather than diagnosis, adapt the headings but preserve evidence, uncertainty, and testability.

## Guardrails

- Never claim a shadowban without direct platform enforcement evidence.
- Never promise impressions, virality, revenue, or subscriber conversion.
- Never call inactive, Shorts-derived, or Community-derived subscribers inherently harmful.
- Never claim that adopting a new YouTube feature earns a ranking bonus.
- Never treat correlation in analytics as proof of causation.
- Never present one former employee's interview as current official YouTube policy.
- Separate spoken claims, official documentation, observed analytics, and inference.
- State when advice depends on a small sample or estimated real-time data.

## Verification

Before responding, confirm:

- Every metric cited was supplied or retrieved.
- Every comparison uses a matched lifecycle window.
- CTR and retention are interpreted alongside audience and traffic source without crossing metric scopes.
- Current-policy claims use dated official sources when required.
- Recommendations are prioritized, testable, and scoped to the creator's objective.
- Unsupported algorithm myths are labeled rather than repeated.

## Resources

- `references/algorithm-principles.md` — read before every diagnosis for detailed principles, caveats, and source timestamps.
