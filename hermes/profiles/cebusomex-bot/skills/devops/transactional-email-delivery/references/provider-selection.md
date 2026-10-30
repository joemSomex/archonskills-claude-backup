# Provider selection

## Decision table

| Requirement | Prefer | Why |
|---|---|---|
| Next.js/TypeScript transactional mail with fast setup | Resend | Simple HTTP API, React/HTML support, webhooks, SMTP, and straightforward Supabase Auth integration |
| Complex inbound routing, subaccounts, validation, regional operations, or enterprise deliverability tooling | Mailgun | Deeper email-operations features and mature routing/reporting controls |
| Lowest raw sending cost with an AWS-skilled operator | Amazon SES directly | Low-level delivery service; the team owns IAM, DNS, sandbox exit, event handling, monitoring, and integration |
| Open-source sending dashboard on infrastructure the team operates | self-hosted useSend + SES | Adds a control plane over SES but also adds PostgreSQL, Redis, SNS, upgrades, backups, and availability work |

## Comparison procedure

1. Retrieve current plan pages and official integration documentation; never reuse remembered prices or quotas.
2. Compare at the expected monthly volume and peak daily rate, including overage, retention, domains, webhooks, dedicated IP prerequisites, validation, and support.
3. Confirm whether authentication mail can use the same provider through Supabase Custom SMTP or a supported email hook.
4. Confirm region/data-residency requirements, inbound-mail requirements, and whether marketing contacts are billed separately from transactional volume.
5. Price operational ownership as well as provider fees. A cheaper API is not cheaper if it requires an unowned mail control plane.
6. Choose one primary application path and one explicit rollback path; avoid permanently operating multiple providers for the same event class.

## Architecture boundaries

- Stripe owns subscriptions, invoices, trials, and payment state.
- Supabase owns application membership persistence and Auth state.
- The email provider transports messages and reports delivery events.
- Never infer membership access from an email-delivery event.
- Do not let an email failure roll back a valid payment or membership update.
