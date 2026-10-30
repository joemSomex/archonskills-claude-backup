# Audiovisual Canon Reconciliation

Use this workflow when a produced episode, film, animatic, or other video adaptation must be reconciled against written canon.

## 1. Intake, verify, and identify the source

Preserve the video outside disposable messaging caches. For files too large for the chat transport, move them directly from the source machine with resumable progress instead of repeatedly retrying the attachment:

```bash
rsync -avhP "<local-video-or-folder>" "<user>@<host>:<durable-source-dir>/"
```

Run the transfer from the machine that holds the file, not from an interactive shell already logged into the destination. If bandwidth is the constraint and the task is narrative/dialogue review rather than pixel-level cinematography, keep the original untouched and create a 720p analysis proxy:

```bash
ffmpeg -i "<original.mp4>" -vf 'scale=1280:-2:force_original_aspect_ratio=decrease' \
  -c:v libx264 -preset medium -b:v 3M -maxrate 4M -bufsize 8M \
  -c:a aac -b:a 128k -map_metadata 0 -movflags +faststart "<proxy-720p.mp4>"
```

Record title, platform identity, local source path, duration, resolution, streams, byte size, and SHA-256. Run a complete decode before analysis; container metadata alone does not prove the upload is complete.

```bash
sha256sum "<video>"
ffprobe -v error -show_format -show_streams -of json "<video>"
ffmpeg -v error -i "<video>" -map 0:v:0 -map 0:a:0? -f null -
```

For a batch, write one machine-readable manifest containing every requested installment, path, checksum, size, duration, stream metadata, and decode result; verify its enumerated count against the request before dispatching parallel work. Keep source binaries immutable. Store analysis artifacts beside a source record, not inside the authored transcript or screenplay.

## 2. Establish the author's precedence rule

Write the rule directionally and at scene scope: which depicted actions, dialogue, chronology, or designs override which written passages. Do not assume a video omission deletes written continuity. Classify an unshown written event as `written-only / not depicted` unless the author explicitly states that omission itself is deletion.

If literal application would erase a load-bearing event needed by later continuity, surface the boundary before changing canon. Never silently reconcile it.

## 3. Cover the full runtime visually

For videos longer than ten minutes, do not rely on scene-change extraction alone: fast title animation can consume the frame budget and leave the later runtime uninspected. Extract uniform samples across the complete duration, then add dense keyframes around dialogue, reveals, fights, title cards, dates, UI, and transitions.

A useful narrative baseline is one frame every five seconds:

```bash
mkdir -p "<work>/uniform_frames_5s"
ffmpeg -hide_banner -loglevel error -i "<video>" \
  -vf 'fps=1/5,scale=640:-2' -q:v 2 \
  "<work>/uniform_frames_5s/frame_%04d.jpg"
```

Create contact sheets with timestamp labels so every extracted frame can be inspected without one tool call per image. Use individual full-resolution frames to verify small text, character identity, injuries, props, and ambiguous actions. A claim is visually verified only when its supporting frame or interval was inspected.

## 4. Establish governing dialogue before transcription

Search the project archive, attachment imports, and source bundle for author-supplied SRT/VTT files, dialogue exports, subtitle spreadsheets, and burned-caption masters before invoking speech-to-text. Preserve and checksum those files as authored sources. For exact dialogue, an author-supplied subtitle governs Whisper even when the video edit, music, or effects make the spoken line difficult to hear.

Before copying subtitle timestamps into the canon ledger, align at least three distinctive dialogue anchors across the beginning, middle, and end of the MP4. A subtitle may come from a longer assembly, earlier edit, or platform cut: when its timebase differs, keep MP4 visual timestamps and SRT cue/timestamps as separate coordinate systems. The SRT can prove released wording in its source assembly, but it cannot prove that subtitle-only scenes or visuals occur in the supplied MP4.

Use machine transcription only when governing dialogue text is absent, or as a timestamped search aid. Keep machine transcripts as evidence, not unquestioned canon: music, combat noise, title cards, and repeated hooks can become hallucinated speech. If authoritative subtitles arrive later, compare them against the cleaned ledger, replace guessed or machine-unclear wording, remove resolved dialogue questions, update affected index and durable-memory facts, and retain the raw machine transcript under an explicit fallback label.

When the full model or full-runtime transcription exceeds a worker timeout or memory cgroup, split mono 16 kHz audio into bounded chunks and transcribe each independently. Four-minute chunks are a reliable starting point:

```bash
mkdir -p "<work>/audio_chunks"
ffmpeg -hide_banner -loglevel error -i "<video>" -vn -ac 1 -ar 16000 \
  -c:a pcm_s16le -f segment -segment_time 240 -reset_timestamps 1 \
  "<work>/audio_chunks/chunk_%02d.wav"
```

Use an efficient local model such as `distil-large-v3` with int8 CPU inference and no VAD for effects-heavy drama; VAD can discard quiet dialogue. Add each chunk's absolute offset when merging timestamps. Cross-check uncertain lines with a second model or a shorter focused pass. Never present unclear tactical words, names, or song lyrics as exact dialogue.

Retain:
- raw transcript JSON with word timestamps and confidence;
- SRT for playback alignment;
- readable Markdown transcript;
- a cleaned canon record containing only evidence-checked dialogue.

## 5. Build the timestamped ledger

For each scene or beat, record:

- interval;
- setting and chronology;
- visible characters and state;
- actions and causal transitions;
- exact dialogue only where sufficiently supported;
- on-screen text and UI;
- category: `aligned`, `adaptation-only`, `written-only / not depicted`, `conflict`, or `uncertain`;
- governing canon result under the author's hierarchy.

Separate symbolic title imagery, soundtrack lyrics, and production branding from literal diegetic events.

## 6. Reconcile against the written source

Compare corresponding beats rather than whole documents. Explicitly identify replacements such as changed locations, routes, character presentation, responder behavior, chronology, or dialogue. Preserve unshown written events as supplementary continuity unless the author's rule makes omission deletion. A produced episode can govern depicted scenes while a written source still supplies offscreen connective events.

## 7. Archive and retrieve

Store:

- source metadata and checksum;
- timestamped canon analysis;
- raw transcript artifacts;
- adaptation ledger;
- governing precedence note.

Update the project index with a concise source pointer and decisive episode anchors. Save only compact, source-cited retrieval facts in durable memory; expire older facts that conflate written-only and onscreen events. Verify recall after writing.

## 8. Completion gate

Do not say the episode was watched or internalized until:

- the full binary decodes;
- the full runtime has visual coverage;
- every retained visual sample was inspected;
- dialogue evidence covers the full runtime or gaps are declared;
- authoritative subtitles, when available, have been reconciled against any machine transcript;
- the written comparison is complete;
- unresolved boundaries are explicit;
- archive, index, and durable recall point to the verified source.

For a batch, complete this gate independently for each installment and notify the user per episode only after its archive and recall verification pass. Finish with a programmatic batch count and stale-value search across current synthesis pages; do not count preprocessing completion as watching.
