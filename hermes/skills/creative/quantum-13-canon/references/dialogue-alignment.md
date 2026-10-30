# Dialogue Alignment

Use this procedure to turn a released episode's SRT into a speaker-labelled record that can drive an adjusted screenplay.

## Evidence order

1. Parse the SRT as immutable cue evidence: index, start, end, and exact text/line breaks.
2. Walk the governing screenplay in scene order and assign obvious dialogue runs by sequence and wording.
3. Consult the produced-episode canon analysis and local transcript for adaptation changes, reordered scenes, and episode-only dialogue.
4. Draft the complete map before inspecting video.
5. List only residual ambiguities; inspect short MP4 excerpts around those timestamps and no others unless validation exposes a wider problem.
6. If a line is absent from both screenplay and the archived MP4 cut, retain a functional role label and `low` confidence rather than inventing an identity.

## Normalized cue schema

Every `dialogue-map.json` cue uses:

- `index`
- `start`
- `end`
- `original_text`
- `speaker`
- `speaker_spans`
- `confidence`
- `evidence`
- `notes`

Use `speaker_spans` for mixed-speaker cues in spoken order. Keep `original_text` byte-for-byte equivalent after UTF-8/BOM normalization; corrections belong in a separately designated governing SRT derivative, never silently inside the map.

## Required outputs

Write these before optional analysis:

1. `dialogue-map.json` — machine-readable source of truth.
2. `speaker-labeled.srt` — same indices/timestamps/text with additive labels.
3. `revised-dialogue-script.md` — produced-order dialogue for screenplay revision.
4. `alignment-report.md` — confidence, adaptation differences, and unresolved attribution.

## Mechanical gates

Programmatically verify:

- map count equals source cue count;
- indices are unique, contiguous, and in source order;
- every start/end timestamp exactly matches;
- every original dialogue string and line break exactly matches;
- every cue has a speaker or explicit unresolved functional role;
- mixed cues preserve ordered spans;
- all four deliverables are non-empty;
- the revised script represents every cue exactly once.

Report unresolved attribution separately from mechanical validity: a complete map may contain an explicitly unresolved role, but it may not hide uncertainty behind a confident name.

## Adjusted-screenplay reconstruction

Use the governing screenplay for scene headings, action, and authorial intent. Replace or add dialogue from the produced-order map, then annotate material changes as episode addition, screenplay-only event, reassignment, reorder, compression/expansion, or unresolved conflict. Do not erase written-only continuity merely because the produced cut omitted it.