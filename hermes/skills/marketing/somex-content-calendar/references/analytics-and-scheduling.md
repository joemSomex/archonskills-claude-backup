# Platform analytics and scheduling constraints (user-provided, working)

## Supplied exports

- TikTok: `/root/.hermes/cache/documents/doc_f62d2c13a21a_Tiktok.zip`; daily `Overview.csv` (365 days, 2025-09-30 through 2026-09-29 with month/day labels requiring inferred year), per-video `Content.csv`, follower/activity data.
- Instagram: `/root/.hermes/cache/documents/doc_741a1df9db6b_Instagram.zip`; UTF-16 daily views/reach/interactions etc. (2026-01-01 through 2026-09-29), plus per-post lifetime table.
- YouTube: `/root/.hermes/cache/documents/doc_b033bc2681ae_Youtube.zip`; nested Studio export ZIPs. Daily `Totals.csv` inside `Content 2025-10-12_2026-10-12 Somex Studios.zip` spans 2025-10-12 through 2026-10-11, and older overlapping content export is also present. Do not sum overlapping periods.
- Read ZIPs safely in memory and inspect CSV encoding/headers. Do not assume TikTok's month/day data includes a year or daily exports include a confirmed timezone. Personal/audience demographic exports should not be reproduced in calendar replies.

## User's weekday interpretation (not a causal posting-time experiment)

- TikTok: Thursday, Wednesday, Friday, Monday, Tuesday, Sunday, Saturday.
- Instagram: Saturday, Wednesday, Thursday/Friday roughly tied, Sunday, Tuesday, Monday.
- YouTube: Sunday, Saturday, Monday, Tuesday, Friday, Wednesday, Thursday.
- The user reports YouTube day-to-day relative variation roughly -9% to +8%, versus TikTok -37% to +43% in their analysis, and correctly cautions that TikTok/Instagram day strength tracks when the studio posted. Do not silently present those percentage ranges as independently replicated from the raw ZIPs without matching the exact method/window/filter. A raw full-window weekday-mean calculation yielded qualitatively similar top weekdays and a much larger TikTok range driven by spikes; YouTube's middle-day order can change with small differences or analysis window. Avoid claiming the raw full-year data establish intrinsic best posting days.
- Treat weekday ranking as a planning *tie-breaker*, behind the Friday Community commitment, active assets, platform interaction formats, staffing, release timing, and the spacing constraints below. Test changes rather than optimizing against correlated historic posting days.

## Hard scheduling checks from user

0. Sunday is an off-day in GMT+8. Do not schedule or propose any platform activity, including videos, Stories, polls, Community posts, Reddit participation, or flexible slots, on Sunday. The historical YouTube Sunday ranking does not override this rule.
1. No platform publishes **videos** on consecutive calendar dates. A Saturday video and a Monday video on the same platform are allowed because Sunday is skipped. Check across week/month boundaries, including the previous week's last date and next week's first date when data is known. Stories and polls are exempt from this spacing rule.
2. TikTok and Instagram must never publish **videos** on the same calendar date, regardless of posting time. A TikTok video and Instagram Story or poll on the same date are allowed; likewise an Instagram video and a TikTok non-video activity. Check video-versus-video collisions only.
3. Maintain the Friday 23:00 GMT+8 YouTube Community post every week; extra Community posts may be proposed, never fewer. YouTube Shorts and Community posts may be on adjacent days; Community posts are not videos for the no-consecutive-video rule.
4. Interpret 00:00 GMT+8 as the start of the named date, not the end of the prior date; recheck day-level collision rules after assigning exact dates.
5. Draft-only concepts do not count as published, but every proposed calendar slot (including optional flexible slot once assigned) must satisfy the applicable constraints before presentation. Do not 'fix' a conflict by deleting the mandatory Friday Community slot.
