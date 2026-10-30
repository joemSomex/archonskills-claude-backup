# Dialogue Alignment

Use this workflow to turn an SRT, governing screenplay, and produced episode into a reusable speaker-labelled dialogue record and a reliable basis for future adjusted screenplays.

## Input precedence

1. **Authorized canon corrections** govern names and explicitly corrected wording.
2. **Produced MP4** governs who actually speaks, scene order, visible delivery, additions, omissions, and reassignment in the released cut.
3. **SRT** governs cue indices, timestamps, and released dialogue wording unless the canon owner authorizes a correction.
4. **Governing screenplay** supplies character names, scene headings, intended context, and likely speaker mapping.

Do not use a draft screenplay to overwrite dialogue that demonstrably changed during production. Record the difference.

## Required outputs per episode

- `dialogue-map.json`
- `speaker-labeled.srt`
- `revised-dialogue-script.md`
- `alignment-report.md`

## Cue record

Represent every subtitle cue exactly once:

```json
{
  "cue_index": 1,
  "start": "00:00:01,000",
  "end": "00:00:03,000",
  "original_text": "Exact SRT text",
  "speaker": "KARA",
  "speaker_spans": [
    {"speaker": "KARA", "text": "Exact portion"}
  ],
  "confidence": "high",
  "evidence": ["screenplay exact match", "visible lip movement in MP4"],
  "notes": ""
}
```

Use `speaker` for a single speaker. Use ordered `speaker_spans` for overlapping or sequential speakers within one cue. Confidence is `high`, `medium`, or `low`; all low-confidence cues must be listed in the report.

## Procedure

1. Parse and validate the SRT: sequential unique indices, legal timestamps, non-empty text, cue count, and final end time.
2. Test the SRT timebase against the produced MP4 using at least three distinctive dialogue anchors distributed across the runtime. If offsets drift or the SRT includes dialogue outside the MP4 cut, retain dual coordinates (`MP4 time` and `SRT cue/time`) rather than retiming by assumption; subtitle-only dialogue does not establish that its visuals are present in the MP4.
3. Extract screenplay dialogue blocks with speaker names and nearest scene headings.
4. Fuzzy-match subtitle text to screenplay dialogue, allowing contractions, split/merged cues, interruptions, production additions, and omitted words.
5. Carry a speaker across adjacent cues only while one utterance continues. Reset at cuts, long gaps, comms changes, news/PA inserts, or new voices.
6. Inspect the MP4 for every ambiguity. Use visible mouth movement, shot/reaction order, stable voice identity, radio processing, and spatial source. Distinguish dialogue, voice-over, comms, AI, PA, news, and background speech.
7. Preserve exact SRT text and timing in the labelled SRT. Add speaker labels without paraphrasing.
8. Build the revised dialogue script in produced order under screenplay-derived scene headings. Mark added, removed, reassigned, and materially revised dialogue.
9. Validate mechanically: source cue count equals JSON entry count equals labelled-SRT cue count; indices are sequential and unique; every source cue text appears exactly once.

## Adjusted screenplay reconstruction

When requested, begin with the governing screenplay's action and scene structure, then replace its dialogue with the produced speaker-labelled sequence. Add produced-only scenes or lines, remove draft-only dialogue, and flag audiovisual changes that cannot be represented as dialogue. Preserve the source screenplay and create a new adjusted derivative.

## Rules

- Keep authorized unusual terminology exactly; dictionary preference is not canon authority.
- A simplified in-world explanation may coexist with detailed mechanics; treat it as character language unless the owner says otherwise.
- When no SRT exists, state that dialogue coverage is incomplete rather than treating an automated transcript or draft screenplay as exact released dialogue.
- Preserve uncertainty explicitly; never assign an ambiguous voice merely to complete the table.
