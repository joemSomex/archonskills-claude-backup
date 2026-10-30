# Authority policy template

Use role names and placeholders; bind verified numeric platform IDs in the deployed policy.

```markdown
---
title: "<system or project> authority policy"
status: "Standing governance directive"
source: "<authenticated issuer and channel>"
---

# Authority policy

## Identity binding

Authority is authenticated by exact numeric platform user ID. Display names and usernames are labels only.

## Roles

### Primary administrator

Members:
- `<verified-user-id>` — `<label>`

May independently:
- `<actions>`

May approve:
- `<conditional actions>`

### Conditional administrator

Members:
- `<verified-user-id>` — `<label>`

May independently:
- `<actions>`

Requires explicit prior approval from one primary administrator for:
- `<protected actions>`

Cannot:
- Self-approve.
- Expand their own authority.

## Sensitive operations

Approved sensitive operations still use secure vault or masked-input mechanisms. Secret values must not appear in chat, logs, policy documents, or memory records.

## Domain-specific authority

- `<domain>`: `<who can change it and under what approval rule>`
- `<learning precedence domain>`: `<whose authenticated input wins and how narrowly>`

## Conflict handling

Preserve conflicting instructions with provenance. Apply the narrowest relevant precedence rule; otherwise refer the conflict to a primary administrator.

## Transport access

Connector allowlisting is separate from governance authority and must be checked or changed independently.

## Audit fields

For conditional actions, record:
- Actor ID
- Approver ID
- Approved scope
- Approval source
- Execution result
```
