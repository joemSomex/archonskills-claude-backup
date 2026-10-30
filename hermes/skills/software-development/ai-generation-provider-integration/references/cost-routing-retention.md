# Cost, Routing, and Retention

Load this reference when comparing provider access paths or designing delivery of generated media.

## Route accounting

Count every independently billed or quota-limited layer:

| Route | Model usage | Provider usage |
|---|---|---|
| Agent → official API | Agent/orchestrator model | API credits/tokens/request charge |
| Agent → provider MCP | MCP-hosting agent model | Provider account credits |
| Agent → intermediary agent → MCP | Orchestrator model + intermediary model | Provider account credits |
| Script/CLI → official API | No LLM unless the script invokes one | API credits/tokens/request charge |

MCP does not erase provider charges and does not make generation local. It changes authentication and tool transport. Tool definitions and results still consume the hosting model’s context.

## Price comparison procedure

1. Normalize duration, resolution, aspect ratio, audio, quality/bitrate, references, and discount status. Do not compare unlike outputs.
2. Keep units separate: provider account credits, generation/video tokens, and LLM tokens are not interchangeable.
3. Calculate account-credit value from the actual purchased pack: `purchase price / credits received`.
4. Calculate one generation: `credits charged × cost per credit`.
5. For token-priced APIs, apply the provider’s current formula and authenticated account discount. Prefer a numeric authenticated estimate; if the estimate returns only a formula, label the result “before account discount.”
6. Compare exact totals and state the absolute difference, percentage difference, and assumptions.
7. Verify the final charged amount in provider analytics when discounts or launch offers are dynamic.

Never infer a universal credit value from an illustrative documentation response. Keep consumer-app cloud credits and developer-API credits separate unless official documentation explicitly defines their conversion and shared balance; matching names or a public add-on price do not prove equivalence. If official docs publish credits-per-output but no USD-per-API-credit price, report the exact credit consumption and mark the dollar total **NOT VERIFIED** until the authenticated developer billing page or purchase pack supplies the conversion. Never call a route cheaper based on headline “per second” pricing when audio, resolution, bitrate, or account discounts differ.

## Credential gate

Validate the exact credential source used by the runtime without printing values. Prefer an official non-billable status, identity, model-list, or estimate endpoint. Recheck immediately before a paid submission; historical success is not current authentication.

When the operator bans a route, do not use its credential probe as a workaround. The chosen route applies to tests as well as production generation until the operator changes it.

## Retention model

Assume four distinct copies may exist:

1. **Provider copy** — generation output and account/request history under provider retention.
2. **Agent cache** — downloaded temporary media for delivery.
3. **Approved archive** — durable local or cloud copy selected by the user.
4. **Messaging-platform copy** — delivery copy governed by that platform.

On completion:

1. Persist the provider request ID and terminal state.
2. Download the output before the documented retention window expires.
3. Verify file type, size, duration/resolution, and non-empty content.
4. Deliver from a stable local path when the messaging adapter supports it.
5. Promote approved media from cache to durable storage with a metadata sidecar and checksum.
6. Apply cache cleanup only to unapproved media; never treat provider deletion as implied by local cleanup.

MCP may return only a URL. Generic MCP registration does not guarantee automatic download, persistence, delivery, or deletion; verify the live tool result and add explicit post-processing where needed.
