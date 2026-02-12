---
name: youtube-transcriber
description: Transcribe a YouTube video using the Claude Chrome extension and prepare it for synthesis into a source note. This is the first step in the content pipeline — transcribe, then synthesize.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
argument-hint: "<youtube-url>"
---

# YouTube Transcriber

Capture and prepare a YouTube video transcript for synthesis into a structured source note.

## Overview

This skill documents the transcript capture workflow using the Claude Chrome extension. It's the upstream step before `/synthesize-source` — you capture the raw transcript here, then synthesize it into a structured note.

## Workflow

### Step 1: Capture the transcript

The user captures the transcript using one of these methods:

**Method A: Claude Chrome Extension (preferred)**
1. Open the YouTube video in Chrome
2. Activate the Claude Chrome extension
3. Play the video (or use the transcript panel)
4. The extension captures the transcript text
5. Copy the transcript and paste it into the Claude Code conversation

**Method B: YouTube's built-in transcript**
1. Open the YouTube video
2. Click "..." → "Show transcript"
3. Select all transcript text and copy
4. Paste into the Claude Code conversation

**Method C: Third-party transcript tools**
- [youtubetranscript.com](https://youtubetranscript.com)
- [kome.ai](https://kome.ai/tools/youtube-transcript-generator)
- yt-dlp: `yt-dlp --write-auto-sub --sub-lang en --skip-download <url>`

### Step 2: Gather video metadata

Use the noembed API to get basic metadata:
```bash
curl -sL "https://noembed.com/embed?url=<youtube-url>" | python3 -m json.tool
```

This returns: title, author_name, author_url, thumbnail_url.

For additional metadata (date, duration, view count), use WebSearch:
```
"<video title>" "<channel name>" youtube published duration
```

### Step 3: Save the raw transcript

Save the raw transcript to a temporary file for reference:
```
sources/_drafts/NNN-raw-transcript.md
```

Include metadata header:
```markdown
# Raw Transcript: Video Title

- **URL**: https://youtube.com/watch?v=...
- **Creator**: Channel Name
- **Captured**: YYYY-MM-DD
- **Method**: Chrome extension / YouTube transcript / yt-dlp

---

[transcript text here]
```

### Step 4: Hand off to synthesis

The raw transcript is now ready for `/synthesize-source`. The user can either:
- Run `/synthesize-source <url>` and paste the transcript when prompted
- Or provide both the URL and transcript in a single message

## Notes

- Raw transcripts are saved in `sources/_drafts/` — this directory is for working files and can be cleaned up periodically
- The transcript capture step is manual (requires a browser) — the synthesis step is automated
- For batch processing, capture multiple transcripts first, then run `/synthesize-source` for each one
- YouTube auto-generated transcripts may have errors — the synthesis step should interpret intent rather than relying on exact wording
