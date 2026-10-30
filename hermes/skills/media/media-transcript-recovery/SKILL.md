---
name: media-transcript-recovery
description: "Use when public video transcripts are blocked."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [video, podcast, transcript, captions, youtube, recovery]
    related_skills: [youtube-content, watch, blocked-page-recovery]
---

# Media Transcript Recovery

Recover spoken content from a public video when direct captions, transcript APIs, or media downloads are blocked. Work from verified source audio, not snippets. Unless the user requests a file, return the finished summary directly in chat.

## Procedure

1. **Try the normal transcript route once.** Use the platform transcript helper with timestamps. If it returns a bot/IP block, stop repeating that endpoint; pivot to a syndicated copy.

2. **Identify the program precisely.** Record the exact video title, guest, show/channel, and displayed duration. Search the exact title plus guest/show for Apple Podcasts, Castbox, Listen Notes, Spotify, or the publisher's podcast page.

3. **Resolve the canonical podcast feed.** For an Apple Podcasts show ID, retrieve metadata through:

```bash
curl -sL "https://itunes.apple.com/lookup?id={SHOW_ID}"
```

Read `feedUrl`, fetch that RSS feed, and inspect its `<item>` entries.

4. **Verify the matching episode before downloading.** Require an exact title or an unmistakable guest/topic match, then compare the RSS duration and chapter/timecode description with the source video. Do not substitute a nearby episode merely because it discusses the same topic.

5. **Download the enclosure audio.** Use the matched `<enclosure url="…">` and verify duration with `ffprobe`.

6. **Transcribe locally with timestamps.** Prefer an already configured local transcriber. Otherwise use `uv run --with faster-whisper` with a small script built around:

```python
from faster_whisper import WhisperModel
model = WhisperModel("base.en", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio_path, beam_size=1, vad_filter=True)
```

Write `[start --> end] text` lines so claims can be tied back to the recording.

7. **Handle long audio deterministically.** If transcription exceeds the foreground timeout, split the audio into overlapping ranges with `ffmpeg -ss/-t`, transcribe each range, add the range offset to timestamps, and verify overlap continuity before merging. Never treat a partial transcript as complete merely because it ends cleanly.

8. **Cross-check completeness.** Confirm the final transcript reaches the enclosure duration and that its topic changes align with the publisher's episode chapters or description.

9. **Summarize for the user's purpose.** Lead with the central thesis, organize the speaker's claims into clear sections, separate claims from independently established facts, include timestamps for major points, and end with practical takeaways when the content is instructional.

## Pitfalls

- **Do not summarize from search snippets when the recording is recoverable** — snippets omit qualifications and frequently collapse distinct claims.
- **Do not use authenticated YouTube cookies merely to defeat a bot wall** — it risks the user's account and weakens provenance when a public syndicated copy exists.
- **Do not claim to have watched visuals when only audio was inspected** — say the summary is based on the verified episode audio/transcript.
- **Do not overfit to channel-wide benchmark numbers** — preserve the speaker's context and examples rather than turning illustrative figures into universal rules.
