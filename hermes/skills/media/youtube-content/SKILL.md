---
name: youtube-content
description: "YouTube transcripts to summaries, threads, blogs."
version: 1.0.0
author: Teknium (teknium1), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [YouTube, Video, Transcripts, Media]
    related_skills: []
---

# YouTube Content Tool

## When to use

Use when the user shares a YouTube URL or video link, asks to summarize a video, requests a transcript, or wants to extract and reformat content from any YouTube video. Transforms transcripts into structured content (chapters, summaries, threads, blog posts).

Extract transcripts from YouTube videos and convert them into useful formats.

## Setup

Use `uv` so the dependency is installed into the same Hermes-managed environment
that runs the helper script:

```bash
uv pip install youtube-transcript-api
```

## Helper Script

`SKILL_DIR` is the directory containing this SKILL.md file. The script accepts any standard YouTube URL format, short links (youtu.be), shorts, embeds, live links, or a raw 11-character video ID.

```bash
# JSON output with metadata
uv run python SKILL_DIR/scripts/fetch_transcript.py "https://youtube.com/watch?v=VIDEO_ID"

# Plain text (good for piping into further processing)
uv run python SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only

# With timestamps
uv run python SKILL_DIR/scripts/fetch_transcript.py "URL" --timestamps

# Specific language with fallback chain
uv run python SKILL_DIR/scripts/fetch_transcript.py "URL" --language tr,en
```

## Output Formats

After fetching the transcript, format it based on what the user asks for:

- **Chapters**: Group by topic shifts, output timestamped chapter list
- **Summary**: Concise 5-10 sentence overview of the entire video
- **Chapter summaries**: Chapters with a short paragraph summary for each
- **Thread**: Twitter/X thread format — numbered posts, each under 280 chars
- **Blog post**: Full article with title, sections, and key takeaways
- **Quotes**: Notable quotes with timestamps

### Example — Chapters Output

```
00:00 Introduction — host opens with the problem statement
03:45 Background — prior work and why existing solutions fall short
12:20 Core method — walkthrough of the proposed approach
24:10 Results — benchmark comparisons and key takeaways
31:55 Q&A — audience questions on scalability and next steps
```

## Workflow

1. **Fetch** the transcript using the helper script with `--text-only --timestamps` via `uv run python`.
2. **Validate**: confirm the output is non-empty and in the expected language. If empty, retry without `--language` to get any available transcript. If still empty, tell the user the video likely has transcripts disabled.
3. **Chunk if needed**: if the transcript exceeds ~50K characters, split into overlapping chunks (~40K with 2K overlap) and summarize each chunk before merging.
4. **Transform** into the requested output format. If the user did not specify a format, default to a summary.
5. **Verify**: re-read the transformed output to check for coherence, correct timestamps, and completeness before presenting.

## Audience/comment analysis

- For comment requests, collect comments rather than substituting a transcript. Try `uvx --from yt-dlp yt-dlp --skip-download --write-comments --write-info-json --extractor-args 'youtube:comment_sort=new' URL`.
- If video playback/extraction is bot-blocked, public comments may still load in the browser after scrolling below the description; check before concluding access is blocked.
- In the browser, load top-level continuations under `ytd-comments`, excluding those inside `ytd-comment-replies-renderer`. Expand visible `#more-replies-sub-thread button` controls, then scroll each top-level thread into view to trigger lazy replies. Click visible continuation buttons for additional replies.
- Reply rendering can create nested and duplicate `ytd-comment-thread-renderer` elements. Filter top-level threads with `!e.closest('ytd-comment-replies-renderer')`; deduplicate extracted comments by the `lc` URL parameter, not DOM counts.
- Extract `ytd-comment-view-model` author, `#content-text`, likes, and `#published-time-text a` permalink. Preserve emoji by replacing cloned content's `img` elements with their alt text before taking textContent.
- Save each collection batch to JSON in `os.environ['BH_AGENT_WORKSPACE']` (the Python variable `workspace` may be undefined). Verify unique IDs against the displayed comment count and check for remaining continuations. Disclose any mismatch or coverage limit.
- Separate channel-owner posts/replies from audience feedback, distinguish messages from unique accounts, and avoid demographic or whole-audience sentiment claims based on self-selected commenters. Preserve quotes and comment links for evidence.

## Error Handling

- **Transcript disabled**: tell the user; suggest they check if subtitles are available on the video page.
- **Private/unavailable video**: relay the error and ask the user to verify the URL.
- **No matching language**: retry without `--language` to fetch any available transcript, then note the actual language to the user.
- **Dependency missing**: run `uv pip install youtube-transcript-api` and retry.
