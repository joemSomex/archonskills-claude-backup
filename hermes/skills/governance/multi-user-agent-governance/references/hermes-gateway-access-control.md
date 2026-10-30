# Hermes Gateway Access Control

Use this reference when reviewing or configuring user allowlists and slash-command administrator tiers for Telegram, Discord, or another Hermes gateway platform.

## Three independent controls

1. **Connector allowlist** decides who may talk to the bot.
2. **Slash-command tier** decides which registered `/commands` an allowed user may invoke.
3. **Profile/tool policy** decides what the agent can do in response to ordinary language.

Never present slash-command gating as a complete security boundary. Plain chat is not gated by `allow_admin_from`; restrict terminal, filesystem-write, process-control, credentials, and external-system tools through profile routing and tool configuration.

## Audit workflow

1. Resolve the active secrets file with `hermes config env-path`.
2. Read only these non-secret values where configured:
   - `GATEWAY_ALLOW_ALL_USERS`
   - `TELEGRAM_ALLOWED_USERS`
   - `TELEGRAM_GROUP_ALLOWED_USERS`
   - `TELEGRAM_GROUP_ALLOWED_CHATS`
   - `DISCORD_ALLOWED_USERS`
   - `DISCORD_ALLOW_ALL_USERS` and `DISCORD_REQUIRE_MENTION` when granting Discord access
   Also inspect `platforms.telegram.extra.allow_from` and `group_allow_from`: explicit adapter lists can control admission independently of environment fallbacks. Check admission before slash-command tiers; an administrator rejected at admission never reaches command authorization. For Discord, check the actual mention setting before telling a new user they must @mention the bot; mention-free channels and a global override change that behavior.
3. Report counts, duplicates, numeric-format failures, and file mode without printing any token or unrelated environment value.
4. Map numeric IDs to trusted gateway metadata or session records. Treat names as labels only.
5. Compare each elevated ID character-for-character against governance and project-authority records.
6. Inspect administrator settings with:

```bash
hermes config get platforms.telegram.extra.allow_admin_from
hermes config get platforms.telegram.extra.group_allow_admin_from
hermes config get platforms.discord.extra.allow_admin_from
hermes config get platforms.discord.extra.group_allow_admin_from
```

7. Review regular-user command lists in the matching DM and group scopes:

```bash
hermes config get platforms.telegram.extra.user_allowed_commands
hermes config get platforms.telegram.extra.group_user_allowed_commands
hermes config get platforms.discord.extra.user_allowed_commands
hermes config get platforms.discord.extra.group_user_allowed_commands
```

## Hermes slash-tier behavior

- No `allow_admin_from` for a scope means slash gating is disabled there for backward compatibility.
- Once an admin list is non-empty, non-admins retain `/help` and `/whoami` plus commands in `user_allowed_commands`.
- DM and group/server admin lists are separate. A DM administrator is not automatically a group administrator.
- Configure both scopes only when the operator intends the same role in both.
- Use canonical command names, not aliases, in command lists.

## Recommended balanced regular-user commands

This set allows users to manage their own active conversation without changing gateway, provider, automation, memory, or billing configuration:

```yaml
user_allowed_commands:
  - new
  - retry
  - undo
  - compress
  - stop
  - queue
  - steer
  - btw
  - status
  - commands
  - profile
  - version
```

`help` and `whoami` do not need to be listed because Hermes always retains them for gated users.

For a stricter deployment, allow only `status`, `commands`, `profile`, and `version` in addition to the automatic floor.

## Keep administrator-only by default

- Approval and bypass: `approve`, `deny`, `yolo`
- Gateway lifecycle and routing: `restart`, `sethome`, `platform`
- Updates and diagnostics upload: `update`, `debug`
- Cost/provider controls: `model`, `reasoning`, `fast`, `moa`, `topup`
- Background or historical state: `bg`, `branch`, `resume`, `sessions`
- Persistent knowledge and extensibility: `memory`, `skills`, `learn`, `bundles`, `curator`
- Automation and collaboration: `cron`, `blueprint`, `suggestions`, `kanban`
- Runtime reloads: `reload`, `reload-mcp`, `reload-skills`
- Every plugin-provided administration command unless explicitly reviewed

## Applying changes safely

1. Preserve existing verified administrators; append rather than overwrite unless revocation is explicit. For ordinary Discord admission, resolve the active `.env` with `hermes config env-path`, validate the supplied numeric ID and existing comma-separated IDs, append only if absent, and keep the file's ownership/mode. Do not print unrelated `.env` keys or tokens.
2. Set the regular-user command list before or atomically with the first non-empty administrator list so ordinary users are not unexpectedly reduced to only `/help` and `/whoami`.
3. Set DM and group/server lists explicitly rather than relying on fallback behavior.
4. Validate configuration with `hermes config check`.
5. Restart the gateway using its installation owner and verify the active service loaded the intended configuration. A graceful restart can wait for other active agent turns; if it outlasts a foreground command, run the restart as a tracked background process with completion notification instead of forcing it or claiming activation. Check the service's new start/PID and gateway logs after completion.
6. Test `/whoami` from one administrator account and one regular account, then test one allowed and one denied command from the regular account.
7. Re-read the active configuration and report the exact administrator IDs, regular command set, test results, and anything left unverified. Distinguish allowlist-on-disk, gateway-loaded, and live Discord-response verification.

## Telegram group non-response checks

1. Resolve the exact chat ID and transport profile from observed gateway/session metadata before making chat-specific changes. Search the supplied title literally first; a title alone is not a routing identifier.
2. Parse session registries defensively: skip non-dictionary metadata entries and normalize nullable labels with `value.get('display_name') or ''`. A failed parser is not evidence that a chat is absent.
3. Compare the affected numeric user ID against DM admission, group admission, DM administrator, and group administrator lists separately. Preserve existing members and repair only the authorized scope.
4. Inspect timestamped authorization logs for the exact user and chat. When asked who else is affected, distinguish users excluded by configuration from users with observed blocked events; absence of logged blocks does not prove universal access.
5. Read back each changed configuration/environment target. Treat a graceful-restart timeout as activation unconfirmed, not restart success; confirm a subsequent service startup before claiming the new configuration is active.
6. Separate configuration verification from end-to-end verification: an actual `/whoami` response in the affected group verifies the live command tier. No new blocked log lines alone does not prove message receipt.
7. If the new group is absent from session records, do not invent its ID or repeatedly broaden permissions. Ask once for a bot-addressed test and correlate its time with gateway logs. After the user confirms that test was sent, investigate delivery rather than repeating the same instruction. Label privacy mode, membership, and send permissions as hypotheses until observed.
8. Scope any claim of 'all chats' to the checked transport profile. Inspect other profiles read-only when relevant, and request explicit scope before altering their policy.

## Identity-correction workflow

When an operator corrects a numeric ID:

1. Preserve the corrected digits exactly; never normalize or infer.
2. Update active connector policy only after the operator confirms the identity.
3. Replace the stale ID in current governance policies, domain/project indexes, and durable memory.
4. Expire stale supplementary-memory facts before saving replacements.
5. Search active synthesis and memory locations for the obsolete ID; exclude immutable source material and append-only logs from the stale-value requirement.
6. Verify the corrected ID is on the intended allowlist and bound to the expected observed account.
