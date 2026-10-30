---
name: canonical-document-sync
description: "Use when syncing canonical Office docs to text mirrors."
version: 0.1.0
metadata:
  hermes:
    tags: [documents, canonical-source, markdown, sync, docx]
    category: productivity
---

# Canonical Document Sync

Synchronize an approved Office document into a Markdown or text mirror without silently rewriting its decisions. The source document is authoritative; the mirror is a faithful, reviewable representation.

## Always-on rules

- Treat the user-designated canonical file as authoritative even when its filename, internal title, or version label conflicts. Preserve the source wording exactly and report the discrepancy; never “repair” it by inference.
- Update only the requested mirror. Do not propagate changes into duplicate worktrees, archived copies, imports, or generated run directories unless the user explicitly names them.
- Preserve document order, headings, tables, lists, emphasis, and literal values. Do not summarize, modernize, reconcile, or merge the old mirror with the canonical source unless requested.
- A successful write is not completion. Verify source-content coverage, structural counts, and repository diff cleanliness before reporting success.

## Procedure

1. **Resolve the canonical pair.** Search for every exact source and mirror filename. If duplicates exist, identify the intended repository root from the user's wording and inspect branch/status before writing. Compare source hashes when duplicate Office files exist; matching hashes establish identical inputs but do not authorize updating every copy.
2. **Inspect both sides.** Read the Office source and the complete existing mirror. Record the source's internal title/version, paragraph count, heading count, table count, and any metadata conflict. Use the existing mirror only to understand the replacement scope, not as authority.
3. **Convert in document-body order.** For DOCX→Markdown, use `scripts/docx_markdown_sync.py SOURCE.docx TARGET.md --write`. The script walks body paragraphs and tables in XML order, maps Word heading levels to Markdown beneath the document title, preserves run-level bold/italic text, emits list paragraphs as bullets, and renders tables as Markdown.
4. **Verify semantically and structurally.** The sync script verifies that every non-empty source paragraph and table cell survives normalized Markdown rendering, and that source/target heading and table counts match. Also run repository whitespace/diff checks such as `git diff --check -- TARGET` and review `git diff --stat -- TARGET`.
5. **Report material conflicts.** Explicitly mention internal-version versus filename conflicts and whether the change is committed. Do not describe the mirror as a newer version merely because its filename says so.
6. **Persist authority only when asked.** If the user explicitly asks to remember the canonical mapping, use the relevant memory skill after verification. Save the canonical path, mirror path, source hash, and internal-version discrepancy, then recall the record to verify persistence.

## Pitfalls

- **Do not rebuild Markdown from flattened extracted text.** Flat extraction loses table placement, heading styles, list semantics, and run emphasis; iterate DOCX body XML so blocks remain in source order.
- **Do not compare raw DOCX and Markdown strings.** Markdown markers interrupt source phrases; normalize emphasis, headings, list markers, escaped pipes, line breaks, and whitespace before asserting content coverage.
- **Do not infer authority from recency or branch names.** Generated worktrees and imports can contain matching filenames; the user-designated repository root controls the write target.
- **Do not equate a successful converter exit with fidelity.** Require zero missing source items plus matching heading/table counts, because a syntactically valid Markdown file may still omit whole blocks.

## Requirements

The helper requires Python 3.10+ and `python-docx`. Use the environment's isolated package runner when the base interpreter does not provide it; do not modify the project dependency set solely for document conversion.
