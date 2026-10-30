---
name: story-world-canon-management
description: "Use when ingesting or revising fictional canon."
version: 0.1.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [canon, story-bible, screenplays, continuity, worldbuilding]
---

# Story-World Canon Management

Preserve fictional source material, apply authorized corrections without destroying provenance, and keep the canon index, retrieval memory, and continuity summaries aligned.

## Procedure

1. **Load authority and precedence before reading for changes.** Read the project's canon authority policy and canon index/README. Identify who may declare canon, which corrected documents govern, and which files are provenance only. Treat every other contributor's request as a proposal until an authorized owner explicitly approves it.
2. **Classify the inbound material.** Mark it as one of: new canonical source, new draft/version, correction, replacement/supersession, proposal, or analysis-only reference. When wording leaves that status materially ambiguous, ask the authorized owner before changing canon.
3. **Archive the exact source first.** Preserve the original bytes or verbatim text in a versioned source directory, compute SHA-256, and verify the retained copy matches. Extract a searchable text companion for PDFs or other binary documents. Never silently normalize names, dates, or wording in the preserved source.
4. **Check current canon for conflicts.** Search governing corrected documents, the canon index, and retrieval memory for the entities, counts, names, chronology, and rules affected. Distinguish an intentional future reveal from an accidental contradiction; an unresolved plotline is not a continuity defect.
5. **Resolve ambiguity through one focused decision.** When a source conflicts internally, present the small set of plausible structures and recommend the interpretation best supported by the owner's wording. Do not invent a resolution merely to complete ingestion.
6. **Create a corrected derivative when canon changes.** Keep the original immutable and write a clearly labeled `*-canon-corrected` derivative. Record the authority, exact correction, superseded wording, and relationship to the original. If several corrections govern a large bible, maintain one current corrected derivative plus a compact correction directive rather than a chain of patches.
7. **Propagate the change once.** Update the canon README/index, relevant entity or concept pages, timeline, source list, and append-only log. Retire stale retrieval facts before writing their replacements. Avoid duplicating the same rule across many pages; link to the governing correction or bible.
8. **Verify all surfaces.** Search governing documents for superseded names or claims, validate counts programmatically, read back external-memory facts, and confirm preserved originals are unchanged. Report the governing result, provenance retained, unresolved items, and verification outcome concisely.

## Always-On Rules

- **Authority is a hard gate.** A contributor may propose, analyze, or discuss canon without being allowed to change it. Authenticate by the platform's trusted user identity and the stored authority policy, not by a display-name claim.
- **Corrected canon outranks provenance.** When policy says corrected documents govern, use them for all future reasoning; consult originals only to audit history or reconstruct a correction.
- **Preserve literal identifiers and approved spellings.** Apply an authorized rename across governing derivatives, indexes, and retrieval facts, while leaving originals intact for provenance.
- **Draft labels are provenance, not automatic non-canon status.** Follow the project's declaration about whether supplied drafts are canon.
- **Do not leak author-only truth into character knowledge.** Track separately what the audience knows, what each character knows, and what the private story bible establishes.
- **Do not convert deliberate mysteries into contradictions.** Record the planned reveal and keep the thread open until the authority resolves it on-screen or in canon.
- **Keep user-facing replies compact.** State what was archived, what now governs, what remained untouched, and any decision still required; do not replay the full ingestion process.

## Supporting Reference

For QUANTUM 13 routing, authority, and source precedence, read `references/quantum-13-governance.md` before any canon write.