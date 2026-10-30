# Static HTML extraction and implementation-claim verification

Use this recipe for HTML attachments, interactive guides, exported dashboards, or other executable-capable web documents.

## Safe structural inventory

Record before synthesis:

- byte size, MIME, encoding, SHA-256, and byte-identical durable copy
- document title and whether a version, date, or commit is actually stated
- heading hierarchy and stable section IDs with original source line ranges
- visible-text length after excluding script/style content
- tables, lists, comments, malformed sections, and unreadable text
- inline and external scripts/styles plus every remote resource URL

Parse source text or the DOM without browser execution. Do not fetch fonts, scripts, images, trackers, frames, audio, or video. Preserve the original HTML; derived Markdown is an extraction, not a replacement.

## Citations

HTML has no stable pagination. Cite factual claims as `document title, #anchor, lines N–M`; cite inline-script behavior separately by its source line range. Preserve exact formulas, thresholds, labels, reward values, and UI wording.

## Interactive calculations

1. Read the JavaScript formula statically.
2. Implement the arithmetic independently in a deterministic probe.
3. Test normal cases, caps/floors, state transitions, loss/draw behavior, and rounding boundaries.
4. If a hosted pure function exists, invoke it read-only with the same cases and compare outputs.
5. Record mismatches among visible prose, static JavaScript, repository code, hosted functions, and client documentation. Never execute the attachment merely to test it.

## Implementation claims

When the document names source files, migrations, tables, or deployed services, keep four states separate:

1. **Repository:** fetch current refs, identify the correct product checkout, verify each path, inspect current content, and note the exact commit.
2. **Tests:** run focused tests through the repository's declared package manager. A missing local install is a coverage gap, not evidence that the implementation is broken.
3. **Hosted database:** identify the exact project, query object/column/function definitions and migration history read-only, and run focused pure-function probes when safe.
4. **Deployed runtime:** inspect deployed function/version metadata and bundled constants or logic read-only when the provider exposes them.

A repository file can be stale while production is newer; a live object can exist without a recorded migration row; and a deployed bundle can identify a source module whose revision is absent from current history. Preserve these as provenance gaps rather than guessing how deployment occurred.

## Wiki shape

Keep the raw provenance/extraction note separate from synthesis. For a substantial guide, prefer focused pages for overview, formulas/mechanics, rewards or user-facing behavior, and implementation parity. Mark synthesis `contested: true` when repository, hosted database, runtime, or another authoritative source disagrees.
