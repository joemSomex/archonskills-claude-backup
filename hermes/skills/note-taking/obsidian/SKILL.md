---
name: obsidian
description: Read, search, create, and edit notes in the Obsidian vault.
version: 1.0.0
author: Teknium (teknium1), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Obsidian, Notes, Markdown, Vault]
    related_skills: []
---

# Obsidian Vault

Use this skill for filesystem-first Obsidian vault work: reading notes, listing notes, searching note files, creating notes, appending content, and adding wikilinks.

## Vault path

Use a known or resolved vault path before calling file tools.

The documented vault-path convention is the `OBSIDIAN_VAULT_PATH` environment variable, for example from `${HERMES_HOME:-~/.hermes}/.env`. If it is unset, use `~/Documents/Obsidian Vault`.

File tools do not expand shell variables. Do not pass paths containing `$OBSIDIAN_VAULT_PATH` to `read_file`, `write_file`, `patch`, or `search_files`; resolve the vault path first and pass a concrete absolute path. Vault paths may contain spaces, which is another reason to prefer file tools over shell commands.

If the vault path is unknown, `terminal` is acceptable for resolving `OBSIDIAN_VAULT_PATH` or checking whether the fallback path exists. Once the path is known, switch back to file tools.

## Local VPS deployment

The default profile's vault is `/root/Documents/Obsidian Vault`, with `Home.md`, `Memory/`, `Projects/`, `Daily/`, and `Inbox/`. For requests to save or recall notes in the Obsidian memory folder, use this vault and the filesystem tools. This is a headless Markdown vault, not an installed desktop application or an automatically injected memory provider. Preserve native Hermes memory and GBrain; do not migrate or automatically capture their contents without permission. Record provenance for saved facts. No cloud sync or backup is configured.

The Telegram bot has multiple allowed users. This shared filesystem vault does not enforce per-Telegram-user isolation; do not expose one user's private notes to another or treat OS permissions as chat-user access control.

## Structured memory helper

For durable facts and decisions in `Memory/`, prefer `scripts/obsidian_memory.py`. It writes provenance-bearing Markdown atomically, never overwrites a same-title note, searches case-insensitively, and confines reads to the memory folder. Resolve the script from this skill's `skill_dir`, then run it through `terminal`:

- Save: `python3 <skill_dir>/scripts/obsidian_memory.py save "<title>" "<content>" --source "<provenance>"`
- Search: `python3 <skill_dir>/scripts/obsidian_memory.py search "<exact phrase>"`
- Smart recall: `python3 <skill_dir>/scripts/obsidian_memory.py recall "<natural-language query>" --limit 5`
- Recall exact note: `python3 <skill_dir>/scripts/obsidian_memory.py get "<Memory-relative path>"`
- Recent: `python3 <skill_dir>/scripts/obsidian_memory.py recent --limit 10`

Use smart recall proactively when a request depends on earlier choices, saved facts, project history, or wording such as "remember," "previously," "we decided," or "our setup." Read the highest-ranked relevant note with `get` before answering. Do not search the vault for unrelated requests, and do not claim a recalled result is current when the note may be stale.

The helper resolves the vault from `OBSIDIAN_VAULT_PATH`, falling back to `~/Documents/Obsidian Vault`, and emits JSON. Smart recall is local keyword ranking, not semantic embeddings. Use the filesystem procedures below for arbitrary vault notes outside `Memory/` or for targeted edits to an existing note.

## Read a note

Use `read_file` with the resolved absolute path to the note. Prefer this over `cat` because it provides line numbers and pagination.

## List notes

Use `search_files` with `target: "files"` and the resolved vault path. Prefer this over `find` or `ls`.

- To list all markdown notes, use `pattern: "*.md"` under the vault path.
- To list a subfolder, search under that subfolder's absolute path.

## Search

Use `search_files` for both filename and content searches. Prefer this over `grep`, `find`, or `ls`.

- For filenames, use `search_files` with `target: "files"` and a filename `pattern`.
- For note contents, use `search_files` with `target: "content"`, the content regex as `pattern`, and `file_glob: "*.md"` when you want to restrict matches to markdown notes.

## Create a note

Use `write_file` with the resolved absolute path and the full markdown content. Prefer this over shell heredocs or `echo` because it avoids shell quoting issues and returns structured results.

## Append to a note

Prefer a native file-tool workflow when it is not awkward:

- Read the target note with `read_file`.
- Use `patch` for an anchored append when there is stable context, such as adding a section after an existing heading or appending before a known trailing block.
- Use `write_file` when rewriting the whole note is clearer than constructing a fragile patch.

For an anchored append with `patch`, replace the anchor with the anchor plus the new content.

For a simple append with no stable context, `terminal` is acceptable if it is the clearest safe option.

## Targeted edits

Use `patch` for focused note changes when the current content gives you stable context. Prefer this over shell text rewriting.

## Wikilinks

Obsidian links notes with `[[Note Name]]` syntax. When creating notes, use these to link related content.
