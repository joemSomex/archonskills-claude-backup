# Provider discovery matrix

Complete one matrix per provider before writing integration code.

## Identity

- Provider:
- Official product surface:
- Classification: OFFICIAL MCP / OFFICIAL API / CUSTOM MCP WRAPPER AROUND OFFICIAL API
- Official endpoint/package:
- Intended use: agent account / server application / both

## Authentication

- Method:
- Credential format:
- Interactive step required:
- Refresh/revocation behavior:
- Server-side unattended use documented:
- Account/credit owner:

## Operations

For each operation, record **verified**, **not available**, or **not verified**, plus the official source:

- Text-to-image
- Image-to-image/edit
- Upscale
- Text-to-video
- Image-to-video
- Video edit/extend
- Reference/character consistency
- Cross-provider input/output compatibility

## Models and schemas

- Dynamic discovery mechanism:
- Featured/current models:
- Per-model schema source:
- Parameters verified:
- Parameters intentionally not generalized:

## References and uploads

- Accepted URL types:
- Upload flow:
- File formats:
- Maximum bytes:
- Single-reference behavior:
- Multiple-reference behavior and limits:
- Retention:

## Job lifecycle

- Submission response:
- Provider request ID:
- States:
- Status API/tool:
- Polling guidance:
- Webhook support:
- Webhook retry/deduplication:
- Cancellation boundary:
- Result schema and download:

## Operations and cost control

- Rate/concurrency limits:
- Runtime limit source:
- Retry headers:
- Idempotency key support:
- Cost estimate support:
- Failed/moderated/canceled billing behavior:

## Gaps

- REQUIRES CONFIGURATION:
- NOT VERIFIED:
- Questions for provider support:

## Verdict

- Ready / conditionally ready / blocked:
- Exact implementation gate:
