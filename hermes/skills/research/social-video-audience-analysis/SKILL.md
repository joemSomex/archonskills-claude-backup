---
name: social-video-audience-analysis
description: "Use when analyzing comments on social videos."
version: 1.0.0
metadata:
  hermes:
    tags: [youtube, comments, audience, sentiment, engagement]
---

# Social Video Audience Analysis

Analyze public comments, creator activity, sentiment, and recurring feedback on serialized or standalone social videos.

## Procedure

1. **Define the population.** Identify the video IDs, requested date window, whether replies count, and whether the channel owner must be included or excluded. Use GMT+8 (UTC+08:00) for this user’s daily reporting boundaries unless they explicitly specify another timezone. For “repeat commenter” requests, distinguish total messages from distinct videos: if the wording does not resolve which threshold is intended, report both counts or state the chosen interpretation before listing results. When the rest of the request is obvious, proceed without asking.
2. **Collect before interpreting.** Obtain every accessible top-level comment and reply. For YouTube, follow `references/youtube-comment-collection.md`.
3. **Normalize and verify.** Deduplicate by platform comment ID/permalink, preserve author, video/episode, exact text, permalink, and reply status, and compare the unique count against the platform’s displayed total. Group people conservatively by exact author handle; never merge similar display names. Disclose any mismatch instead of describing a partial set as complete.
4. **Apply the requested filter.** Separate channel-owner activity from audience activity before analysis. Count messages, distinct videos, and unique accounts independently. Aggregate date and episode totals programmatically, then verify every declared total against the enumerated records.
5. **Resolve exact dates from an authoritative source.** Do not convert labels such as “1 day ago” into hard calendar-day totals when exact API timestamps, YouTube Studio, or a Google My Activity export are available; relative thresholds and account timezone can move large batches between dates. For an activity export, use `references/activity-export-audits.md`: count semantic activity records rather than renderer headings, reconcile the unfiltered total before applying an exact title/ID allowlist, and state the export cutoff and timezone. If only relative labels exist, mark day totals approximate.
6. **Identify recurring commenters programmatically.** Exclude the exact channel-owner handle, aggregate every retained message by exact author handle, compute total messages and distinct videos, filter with the requested threshold, and sort by message count then handle. Preserve each comment verbatim with its episode and reply label. If the list is long, give the verified match count and split the in-chat output into readable batches rather than silently narrowing or summarizing the population.
7. **Classify conservatively.** Keep positive, negative, mixed/actionable, neutral/question, ambiguous, and off-topic/promotional reactions distinct. Never infer a production flaw from an unexplained insult or classify ambiguity as negativity.
8. **Synthesize themes.** Report recurring praise, recurring criticism, representative exact quotes, and practical implications. Distinguish widespread themes from isolated comments.
9. **Deliver in chat by default.** Do not create CSV, Excel, PDF, or other documents unless the user explicitly asks for a file. For recurring episode reports, use: coverage, positive feedback, negative/constructive feedback, priorities, bottom line.

## Standing Rules

- Channel commenters are a self-selected group; do not claim they represent all viewers or audience demographics.
- A request for more episodes is positive demand with a possible release-communication implication, not automatically negative sentiment.
- One unexplained hostile comment counts as negative sentiment but provides no actionable diagnosis.
- Preserve exact identifiers and comment wording. Label translations of non-English comments.
- State whether totals include top-level comments, replies, or both.
- Treat owner-side activity exports or exact API timestamps as authoritative for date allocation; use public relative labels only as an explicitly approximate fallback.
- When cross-check sources disagree, correct the result from the more precise timestamp source and explain the discrepancy instead of averaging or preserving an earlier total.
- When asked to list commenters and comments, preserve the full qualifying set and exact wording; do not replace requested records with thematic summaries.
