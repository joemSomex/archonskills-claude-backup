---
name: generative-media-production-benchmarking
description: "Use when benchmarking generative-media production costs."
version: 1.0.0
author: Nous Research
license: MIT
metadata:
  hermes:
    tags: [generative-media, production, benchmarking, credits, costing, forecasting]
    category: research
---

# Generative Media Production Benchmarking

Benchmark image/video generation workflows using retained usable output rather than advertised clip prices. Keep operational efficiency, cash valuation, and production speed separate so changing packages, exchange rates, or model labels do not corrupt the comparison.

## When to Use

- Compare an existing generative-media workflow with a new model, provider, or production method.
- Convert credit consumption into actual USD, SGD, or another currency.
- Update cumulative footage checkpoints and project episode-length budgets.
- Compare production speed, retry burden, or retained usable output across productions.

## Always-on rules

- Treat the user's actual paid package or invoice as the authoritative credit valuation. Do not substitute a public top-up, promotional, subscription, or auto-refill rate unless the user asks for that scenario.
- Separate credits obtained, credits spent, and credits remaining. A phrase like "24,000 bought" may exclude plan-included credits; reconcile every source before computing the spent-per-minute baseline. If the balance is unknown, mark efficiency projections conditional rather than treating purchases as spend.
- Separate standardized credit valuation from actual cash outlay when plan-included credits are mixed with paid top-ups. State the top-up spend and the unknown plan payment separately; do not assign the top-up unit price to bundled credits as if it were their actual purchase price.
- Preserve provider and model labels exactly as the source records state them. If a record says only a model family, include it in a broad family benchmark but exclude it from a strict version-specific benchmark.
- Distinguish finished runtime, newly generated usable footage, repeated footage, alternative takes, and footage retained in the final edit. Never compare these as if they were the same denominator.
- Report both the cumulative rate and the incremental rate since the previous checkpoint. The cumulative rate is the planning baseline; the incremental rate reveals drift.
- Keep measured results separate from assumptions. Label contingencies, retention rates, exchange rates, and future scene-difficulty adjustments explicitly.
- Use straight ASCII punctuation in user-facing reports. When asked for a simple estimate, lead with only the requested duration -> credits -> USD -> SGD lines and one compact assumptions line; omit process narration, purchase accounting, and extra scenarios unless asked. Resolve "previous baseline" from context: if contrasting the current method with the most recent prior production, use that single production, not a pooled historical cohort. Name the selected baseline explicitly and switch only when the user asks for a pooled average.

## Procedure

1. **Establish the source record.** Extract each production's provider/model, finished runtime, newly generated usable duration, repeated duration, credits, generations, and calendar or working days. Verify totals programmatically rather than trusting a stated grand total.
2. **Normalize durations.** Convert every duration to seconds before calculating. Retain the original `MM:SS` representation for reporting.
3. **Choose comparable cohorts.** Build at least:
   - a broad workflow cohort for all records that genuinely belong to the same provider/model family;
   - a strict cohort containing only records explicitly labeled with the exact model version;
   - an all-history cohort only when the user wants a blended headline.
4. **Calculate weighted rates.** Sum credits and usable seconds across the cohort, then divide totals. Never average episode-level rates, because episodes have different durations.
5. **Process checkpoints.** For a new cumulative checkpoint, calculate credits per usable second/minute and usable seconds per 1,000 credits. Subtract the prior cumulative checkpoint to calculate the incremental segment.
6. **Value credits and new clip prices separately.** Ask for or retrieve the actual amount paid and credits received. Calculate `paid amount / credits received`; convert currencies using a quoted FX rate and state its date or that it is an earlier reference, never silently call an old quote current. Do not substitute provider storefront pricing for a user-supplied paid rate. A new raw clip price gives credits per *generated* minute, not per *usable* minute: divide by a measured usable-output yield only if raw generated duration and distinct usable duration are both known. Otherwise retain the last measured usable baseline as historical and show clearly labeled yield scenarios, not a fabricated new measured rate. Classify each discount by its actual mechanism before calculating: a price discount changes cash per credit but not credits burned; a generation/consumption discount multiplies pre-discount workload credits by `(1 - discount)` while leaving purchased credits and their cash price unchanged. If both exist, apply them to their separate dimensions and do not stack a withdrawn offer. When comparing price discounts, show full-price and discounted cash side by side for the same credit total; state the savings explicitly.
7. **Forecast targets and subscriptions.** Multiply the measured cumulative credits-per-minute rate by target usable minutes; when only raw clip pricing is new, calculate scenario credits as `raw credits/minute * target usable minutes / assumed usable yield`. Show total credits, credits already spent, additional credits required, and optional contingency separately. For an offer that discounts consumption, first establish whether the episode estimate is *before or after* that discount; calculate monthly burn from the undiscounted workload once, then subtract from the monthly credit allotment. Resolve the payment schedule before building a running balance: when monthly credits reset, label each remainder unused or expired monthly capacity and never plot a growing balance; for quarterly or annual prepayment, track the actual upfront pool within its paid period, but do not infer post-period validity without terms. A sum of monthly remainders is not an end-of-year balance. Separate usage-valued cost from a monthly minimum or annual contract obligation; do not imply unused credits are cash savings or automatically bankable. For annual episode plans, distinguish cadence from episode count: one episode/month over eight months produces eight, extending months nine through twelve produces twelve, while two episodes/month over eight months produces sixteen. Label low/high usage bands or yield cases as planning assumptions rather than measured confidence ranges.
8. **Compare workflows and platforms.** For one workflow across time, report percentage reduction in credits per usable minute and the output-efficiency multiple, then value both at the relevant paid rates. For different platforms, calculate each platform's `credits per identical generated clip * its own USD per credit` before comparing cash costs; raw credit counts are different denominations. When a screenshot gives an actual pack price in local currency, read the credit quantity and price directly, recompute USD per credit from that pack using a quoted FX rate, and update every downstream clip comparison; an earlier inferred USD rate is stale. Report both the allocated credit value of a clip and the cash required to purchase the smallest sufficient pack when they differ, including leftover credits, because pack expenditure is not identical to credits consumed. For an episode comparison, state the target duration and assumed usable yield, derive the required number of identical clips, then multiply by EACH platform's own credits per clip and USD per credit; never transfer a numeric credit total across platforms. Under an explicit equal-usable-yield assumption, scale both clip costs by the same retry/retention factor, but do not infer quality or speed parity from a shared model name. Keep plan minimums, expiry, and consumption discounts outside the raw-clip comparison unless they actually apply; verify platform-specific features and account-tier rights from primary sources before listing operational pros and cons.
9. **Assess production speed separately.** Compare usable minutes per calendar day or working hour only when time data exists. Credit efficiency does not establish faster production.
10. **State limitations.** Call out sample size, retained-versus-alternative footage, scene difficulty, revisions, and pricing/FX changes without presenting a planning contingency as a statistical confidence interval.

## Verification checklist

- Source totals equal the sum of line items.
- Finished runtime is not used where usable generated duration is required.
- Broad and strict model cohorts are clearly labeled.
- The newest checkpoint is cumulative unless the user explicitly says otherwise.
- Cash values use the user's real purchase rate and a stated currency rate.
- Rounded displayed values still reconcile with calculations made from unrounded values.
- Every projection says whether existing usable footage is included.

For formulas and reporting fields, read `references/benchmark-metrics.md`.
