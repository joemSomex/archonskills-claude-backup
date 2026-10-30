# Benchmark metrics

## Core conversions

Convert `MM:SS` to seconds:

`usable_seconds = minutes * 60 + seconds`

Convert seconds back to display duration using integer division and remainder.

## Efficiency metrics

- Credits per usable second: `credits / usable_seconds`
- Credits per usable minute: `credits / (usable_seconds / 60)`
- Usable seconds per 1,000 credits: `usable_seconds / credits * 1000`
- Generations per usable minute: `generations / (usable_seconds / 60)`
- Usable minutes per day: `(usable_seconds / 60) / production_days`

For a cohort, sum credits and usable seconds first:

`weighted_credits_per_minute = total_credits / (total_usable_seconds / 60)`

Do not average per-production ratios.

## Checkpoint metrics

For cumulative checkpoints A and B:

- Incremental credits: `B_credits - A_credits`
- Incremental usable seconds: `B_seconds - A_seconds`
- Incremental credits per usable minute: `incremental_credits / (incremental_seconds / 60)`

If either difference is negative, confirm whether the checkpoint was revised rather than treating it as new production.

## Workflow comparison

- Credit-cost reduction: `(1 - new_rate / old_rate) * 100%`
- Output-efficiency multiple: `old_rate / new_rate`
- Credits saved at target duration: `(old_rate - new_rate) * target_minutes`

Use credits per usable minute for both rates.

## Cash valuation

- Currency value per credit: `actual_amount_paid / credits_received`
- Production cash cost: `credits_used * value_per_credit`
- Converted value: `source_currency_amount * quoted_fx_rate`

State whether taxes and card/FX fees are included. Storefront list prices are scenarios, not the user's realized cost.

## Forecast fields

For each target duration, show:

1. Base total credits
2. Credits already spent
3. Additional credits required
4. Base cash value
5. Optional contingency total
6. Historical-comparison total and savings

A contingency is a planning allowance. Do not call it an uncertainty interval unless it comes from measured variance or a statistical model.
