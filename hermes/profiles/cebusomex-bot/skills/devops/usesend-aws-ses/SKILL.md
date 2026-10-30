---
name: usesend-aws-ses
description: Use when connecting self-hosted useSend to Amazon SES.
---

# Self-hosted useSend with Amazon SES

Use this specialist workflow only after the provider decision selects self-hosting. For provider comparison, event ownership, migration, and cutover rules, load `transactional-email-delivery` and its `references/provider-selection.md` first.

## Architecture

- Keep useSend self-hosted on Coolify/Hostinger.
- Use Amazon SES for sending and Amazon SNS for delivery-status events.
- Use an IAM user or role with delegated permissions; never require or create AWS root credentials.
- useSend needs AWS API credentials, not SES SMTP credentials, unless its optional SMTP path is deliberately selected.

## Guided setup order

Proceed one verified screen at a time:

1. Open the regional SES console and select the intended region.
2. Verify the sending domain with Easy DKIM.
3. Configure SPF, DMARC, and a custom MAIL FROM domain.
4. Request SES production access and confirm sending quotas.
5. Create dedicated least-privilege useSend API credentials for SES/SNS.
6. Store credentials only in Coolify masked runtime variables.
7. Connect the public SNS callback URL through useSend.
8. Send a controlled test and verify delivery/status events.

## Console pitfall

IAM is a global AWS service. If the console shows `Global` and lock icons beside all regions while the user is inside IAM, do not diagnose a region restriction from that alone. Open the regional SES console directly first. Treat an actual SES `AccessDenied` response as the evidence of missing permission.

## Safety

Never expose AWS access keys, secret keys, SMTP passwords, account IDs, or callback secrets in chat, screenshots, source control, or logs. Confirm cost before paid changes and obtain explicit approval before production activation or DNS changes.
