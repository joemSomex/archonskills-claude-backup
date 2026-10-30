---
name: messaging-activity-review
description: "Use when reviewing activity across messaging chats."
version: 1.0.0
metadata:
  hermes:
    tags: [messaging, activity, sessions, telegram, discord, weixin, whatsapp]
---

# Messaging Activity Review

Review the current Hermes profile's chat activity without posting into any channel.

## Workflow

1. **Fix the scope before reading.** Default “all chats” to every messaging chat recorded by the current active profile. Include other profiles only when the user explicitly asks for all profiles; Hermes profiles have isolated session stores.
2. **Browse recent sessions first.** Use `session_search` without a query, request newest-first results, and raise the limit to 10. This gives a quick activity map and human-readable session links.
3. **Make exhaustive requests exhaustive.** When the user says “all chats,” do not treat the ten-session browse result as complete. Resolve the active profile's `state.db` through `$HERMES_HOME` (fall back to `~/.hermes` only when unset) and query it read-only:
   - filter `sessions.source` to messaging platforms;
   - partition by `source` plus `COALESCE(chat_id, session_key, id)`;
   - keep the newest session for each chat;
   - inspect the latest substantive `user` and `assistant` messages from `messages`.
4. **Deduplicate by chat identity.** Count distinct platform/chat pairs, not sessions; long-running chats and restarted sessions otherwise inflate totals.
5. **Classify each chat from evidence.** Report completed work, active work, explicit interruptions, and genuine unanswered requests. A request is pending only when the latest substantive user message has no later substantive assistant response, or when the response explicitly says the operation was interrupted.
6. **Use the user's reporting timezone.** Convert activity timestamps to GMT+8 and label them. Keep exact times only when they help distinguish simultaneous work; otherwise use the date.
7. **Summarize, do not dump transcripts.** Lead with platform chat counts, then list recent notable activity and a short “needs attention” section. Name the chat and task outcome; quote private message text only when the wording itself is required to explain a correction.
8. **Separate history from connectivity.** Say “no recorded chat activity” when a platform has no sessions. Do not claim the platform is disconnected without a live platform-status check.
9. **Remain read-only.** Do not reply in other chats, restart work, or clear an interruption unless the user asks for that follow-up.

## Always-on Rules

- Prefer `display_name` plus platform over auto-generated session titles; titles often describe the first message rather than the current work.
- Treat empty assistant content as non-evidence because tool-call rows can have blank text while work is still progressing.
- Surface corrections and interrupted work before routine completed outputs; they are the items most likely to require action.
- Preserve chat privacy by reporting task-level summaries rather than copying full conversations.
- Distinguish “latest recorded activity” from real-time unread status; session history does not prove whether a human has read a message.

## Pitfalls

- **Do not call a bounded recent-session list “all chats”** — discovery tools intentionally cap results and can omit older but still relevant channels.
- **Do not count sessions as chats** — resumptions and per-thread sessions create duplicates for one channel.
- **Do not infer pending work from blank assistant rows** — tool invocations and streaming placeholders commonly persist with empty content.
- **Do not equate absence from `state.db` with a broken connector** — a connected platform may simply have no recorded conversation in this profile.
