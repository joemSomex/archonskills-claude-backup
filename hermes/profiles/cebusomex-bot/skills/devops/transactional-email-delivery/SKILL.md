---
name: transactional-email-delivery
description: Use when selecting or integrating transactional email.
---

# Transactional email delivery

## Procedure

1. **Map the email streams before choosing a provider.** Separate authentication mail, application-triggered transactional mail, billing lifecycle mail, inbound mail, and marketing campaigns. Record which system owns each event; the delivery provider is never the source of truth for membership or payment state.
2. **Inspect the existing integration before recommending a migration.** Search code, environment names, SMTP configuration, webhook handlers, templates, retry/idempotency behavior, and provider-specific endpoints. Prefer consolidating an already-working provider over adding a third path.
3. **Choose by required capabilities, not brand familiarity.** Fetch current official pricing and limits at decision time because plans change. Use `references/provider-selection.md` for the reusable decision table. When self-hosted useSend + SES is selected, load `usesend-aws-ses` for the detailed branch.
4. **Authenticate a dedicated sending subdomain.** Configure provider-issued DKIM and SPF records, add DMARC in monitoring mode first, and use a custom MAIL FROM/bounce domain when supported. Do not overwrite unrelated MX/SPF records on the root domain; merge SPF deliberately because a domain must not publish multiple SPF policies.
5. **Provision least-privilege credentials.** Use separate test/staging and production keys where supported. Store API keys and SMTP passwords only in masked server-side secrets. Never put them in `NEXT_PUBLIC_*`, screenshots, chat, client bundles, or committed `.env` files.
6. **Integrate through one application adapter.** Keep templates and event composition provider-neutral; isolate provider HTTP/SMTP calls behind one send function. Carry an idempotency key derived from the business event so webhook retries do not duplicate membership messages.
7. **Keep billing resilient.** Persist the Stripe/Supabase membership state before attempting email. Treat delivery failure as observable follow-up work, not a reason to fail or replay a successful payment webhook.
8. **Cut over by message type.** Verify domain status, send to controlled inboxes, confirm webhook signatures and suppression behavior, then test auth confirmation/reset and every billing lifecycle event. Prevent duplicate provider emails before enabling the new path. Keep the previous path available for a rollback window and remove it only after production evidence is clean.

## Provider default

For a Next.js/TypeScript application needing account, membership, receipt, failed-payment, cancellation, and product notifications, prefer Resend unless requirements demand Mailgun's deeper inbound routing, subaccounts, regional operations, validation, or enterprise deliverability controls. Prefer self-hosted useSend + SES only when owning the mail control plane is intentional and its database, Redis, IAM, SNS, upgrades, monitoring, and backups have an assigned operator.

## Guided setup style

- Guide Joshua one verified screen at a time; give the exact menu path or direct regional console URL, then wait for the result before advancing.
- When a secret must be generated, use one atomic command that generates and copies it, display only its length, and explain that the number shown is the length—not the secret. Never ask for a screenshot after the value may be visible.
- Distinguish AWS API credentials, SES SMTP credentials, and provider API keys; they are not interchangeable.
- In the AWS console, IAM is global. Lock icons in IAM's region selector are not evidence of a region restriction; open the regional service directly and diagnose permissions only from the service's actual `AccessDenied` response.

## Verification

A provider setup is complete only when:

- DKIM/SPF/DMARC status is verified from DNS and the provider dashboard.
- Production/sandbox restrictions and sending quotas are known.
- A real inbox receives both HTML and plain-text content.
- Auth confirmation and password reset succeed.
- Each membership lifecycle event sends once despite a duplicate webhook delivery.
- Bounce, complaint, and suppression events are accepted and observable.
- No secret or raw provider error reaches logs, UI, chat, screenshots, or source control.
- The rollback path has been tested.
