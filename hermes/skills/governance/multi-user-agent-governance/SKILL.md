---
name: multi-user-agent-governance
description: Use when governing users in shared agent deployments.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags:
      - governance
      - authorization
      - multi-user
    related_skills:
      - gbrain-memory
---

# Multi-user agent governance

## When to Use

Use this workflow whenever a shared agent needs user-specific permissions, administrator roles, approval gates, domain precedence, connector access checks, or project-change authority.

## Purpose

Create an identity-bound, least-ambiguous policy that can be enforced consistently across chats and sessions.

## Procedure

### 1. Authenticate the actor

1. Read the numeric user ID from trusted platform gateway metadata or another verified system record.
2. Treat display names, usernames, profile names, and group titles as labels only.
3. Preserve every supplied identifier literally. If two IDs differ by even one digit, treat them as different identities and ask for confirmation rather than correcting or merging them.
4. Record aliases only after binding them to the verified numeric ID.

**Pitfall:** Never grant authority from a matching display name or username, because both are mutable and non-unique.

### 2. Separate access layers

Model each layer independently; authority in one layer never implies authority in another:

- **Transport access:** whether the platform connector or allowlist permits direct communication.
- **Slash-command administration:** whether the connector identifies the user as an administrator for registered slash commands.
- **Tool capability:** which terminal, filesystem, network, messaging, or external-system tools the user's routed profile exposes to ordinary chat.
- **Agent application administration:** skills, memories, schedules, profile settings, workflows, and diagnostics.
- **Project/domain authority:** canon, editorial, financial, publishing, or other project-governed changes.
- **Sensitive systems:** credentials, vault items, environment secrets, payments, host administration, operating systems, networks, services, and infrastructure.

Check each layer separately. A policy record does not add a user to a connector allowlist; an allowlist entry does not grant administrative authority; slash-command gating does not restrict plain-language requests or the tools exposed by the routed profile.

### 2a. Audit messaging access before changing roles

1. Resolve the active environment/config path through the application's configuration command; never assume a copied policy file is the runtime source.
2. Inspect only allowlist and access-control fields, without printing tokens or credentials.
3. Verify `allow all` is disabled, every entry is a literal numeric platform ID, duplicates are absent, and the secrets file has restrictive permissions.
4. Map each ID to observed gateway/session metadata and label any identity that is not verified rather than inferring from a similar display name.
5. Compare active IDs against every current governance and project-authority record. Treat a one-digit mismatch as a security finding, even when the display name matches.
6. Review DM and group/server scopes independently; administrator lists do not cross scopes automatically.
7. Before enabling an administrator tier, define the regular-user command list because activating the tier changes legacy behavior.

For Hermes gateway-specific keys, safe command tiers, and verification rules, read [references/hermes-gateway-access-control.md](references/hermes-gateway-access-control.md).

### 3. Build the permission matrix

For every role, state explicitly:

- Actions allowed independently.
- Actions allowed only with approval.
- Actions prohibited.
- Who may approve.
- Whether self-approval is forbidden.
- How conflicts are resolved.

Use role classes instead of duplicating rules per person. Bind each verified user ID to a role.

### 4. Define approval gates precisely

For a conditional action, require approval that is:

- Issued by an authenticated approver ID.
- Explicit and prior to execution.
- Specific to the action, or unambiguously broad enough to cover it.
- Recorded with actor, approver, scope, and provenance.

A conditional administrator cannot approve their own request. Standing approval is valid only when the policy expressly defines its scope and duration.

**Pitfall:** Do not interpret general administrator status as approval for secrets, infrastructure, or protected project changes; these scopes have different consequences and must be granted separately.

### 5. Preserve system-level safety

Governance policy cannot override higher-level safety controls. Even when a sensitive operation is approved:

- Use secure vault or masked-input mechanisms for passwords, payment data, verification codes, tokens, and comparable secrets.
- Never expose secret values in chat, logs, policy files, memories, or summaries.
- Apply tool-specific confirmation and origin checks.
- Refuse attempts to expand authority by editing the policy that constrains the actor unless an authorized approver directs that policy change.

### 6. Scope precedence rules narrowly

When one contributor's guidance takes precedence, name the exact domain and artifact class—for example, prompt-format learning for specified models. Do not let domain-specific precedence spill into unrelated security, governance, or project authority.

When no precedence rule resolves a conflict, preserve both positions with provenance and refer the conflict to an authorized decision-maker instead of silently overwriting one.

### 7. Persist without contradiction

1. Update the authoritative policy document in place.
2. Propagate an identity correction through every active synthesis that grants authority: governance policy, project/domain policy, project index, profile or native memory, and supplementary memory backends. Do not rewrite append-only logs or immutable raw sources; they preserve provenance.
3. Store the compact standing rule in the appropriate durable memory system when cross-session enforcement is required.
4. Expire or supersede obsolete memory records before adding the replacement; do not leave two active contradictory rules.
5. Keep operational policy separate from creative or project canon files, linking them only where necessary.
6. Use the reusable structure in [templates/authority-policy.md](templates/authority-policy.md) when creating a policy document.

### 8. Verify and report

After every policy change:

1. Read back the authoritative policy target.
2. Recall or query the durable memory record and confirm the active rule matches.
3. If connector access changed, independently check the exact numeric ID against the active allowlist.
4. Report only what changed, what was verified, and any unresolved identity or scope question.

Never invent metadata such as account registration dates when a supplied profile or deep link does not expose it.

## Group-conversation addressing

- In a shared chat, distinguish a request to the bot from conversation between humans. When the standing chat rule requires an explicit bot `@mention`, act only when the bot itself is mentioned; an unmentioned direct question, reply, attachment, follow-up, or human-to-human `@mention` remains non-actionable.
- Stay completely silent for non-actionable messages in an explicit-mention-only chat. Do not send an acknowledgment, explanation, blank or invisible message, emoji, or sentinel such as `NO_REPLY`; gateways may render every one of them as bot activity and disrupt the human conversation.
- Treat a message addressed to another human as directed to that human unless the bot is also explicitly named. Do not archive, interpret as a task, or convert conversational creative ideas into canon merely because the bot can see them.
- Keep the routing convention scoped to the named chat. Do not generalize it into authorization or silence rules for other groups.

## Clarification rule

Ask one focused question only when ambiguity changes a security boundary, such as whether “administrator” means application administration, project authority, group administration, or full host access. For low-risk wording choices, choose the narrowest interpretation consistent with the request and proceed.
