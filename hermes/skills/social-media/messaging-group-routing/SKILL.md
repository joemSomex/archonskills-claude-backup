---
name: messaging-group-routing
description: Use when routing queued media between messaging groups.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [messaging, telegram, group-routing, media, queue]
---

# Messaging Group Routing

## When to Use

Use for ordered batches of media or prompts sent across chats, especially when the next item must wait for processing of the prior item. Also use to resolve a renamed destination group before sending.

## Procedure

1. **Inventory the source and order.** Enumerate attachments from actual inbound messages or session records in message order, deduplicate by source identity, check that every file exists, and count them programmatically. Preserve exact caption text and the user's sequence. For an all-items request, keep a durable queue cursor so interrupted work does not duplicate posts.
2. **Resolve the destination live.** Use the current profile's known-chat list or session database to find candidate chat IDs, then verify a candidate against the platform's live chat title before sending. A stored `display_name` can be stale after a group rename; an invitation preview confirms a name but does not itself provide a sendable chat ID. Do not infer non-membership from a missing or outdated local name.
3. **Check the sender-to-processor route before committing a batch.** Identify which account posts the media and which account handles the task. A bot's outbound group post is not necessarily an inbound user request to that same bot. Test the first item and require an observed task-start event rather than assuming that delivery starts generation. If no input route is confirmed, stop instead of posting the remaining queue.
4. **Send and verify one item.** Use the configured platform sender with the exact caption and one media path. For multi-file sets, send each file separately at a paced rate and atomically checkpoint its returned target and message ID before sending the next; a batch header is not proof its attachments landed. Read back the target's mirrored message or platform state where supported. On a timeout or ambiguous failure, pause that slot rather than blindly retrying and risking a duplicate. Treat a successful send as evidence of delivery only, not of downstream processing.
5. **Gate the next item on completion.** Match a completion event to the particular preceding input and verify the expected output count or status. Completion text alone is insufficient if multiple tasks could be active. Advance the persisted cursor only after both delivery and processing are verified; on timeout, failure, ambiguity, or an interrupted run, pause and report the exact last completed and in-flight items.

## Always-on rules

- Never use a fixed delay as a substitute for the target workflow's completion signal; generation times vary.
- Keep a group post, a task-start event, and a completed generation as three separate states in reports.
- When the requested queue depends on messages being sent as a human user, use an authorized user-account route rather than assuming the bot's own posts will invoke itself. Do not solicit authentication secrets in chat.
- Report concise counts: total items, processed, in flight, unsent, and the reason for any pause. Do not imply all items were processed because one post succeeded.
