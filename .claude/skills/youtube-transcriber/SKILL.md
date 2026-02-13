---
name: youtube-transcriber
description: Automatically extract a YouTube video transcript using Playwright browser automation and prepare it for synthesis into a source note. This is the first step in the content pipeline — transcribe, then synthesize.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_click, mcp__playwright__browser_evaluate, mcp__playwright__browser_wait_for, mcp__playwright__browser_close, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_press_key
argument-hint: "<youtube-url>"
---

# YouTube Transcriber

Automatically extract a YouTube video transcript using Playwright browser automation and prepare it for synthesis.

## Input

A YouTube video URL (e.g., `https://www.youtube.com/watch?v=...` or `https://youtu.be/...`).

## Workflow

### Step 1: Validate the URL

Confirm the input is a valid YouTube URL. Extract the video ID. Supported formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/watch?v=VIDEO_ID&t=...` (with timestamps)

### Step 2: Determine next source ID

Read `sources/README.md` to find the highest existing source ID. The draft will use the next sequential 3-digit zero-padded ID.

### Step 3: Gather video metadata

Use the noembed API to get basic metadata:
```bash
curl -sL "https://noembed.com/embed?url=<youtube-url>"
```

This returns: title, author_name, author_url, thumbnail_url.

For additional metadata (date, duration), use WebSearch:
```
"<video title>" "<channel name>" youtube published duration
```

### Step 4: Extract transcript via yt-dlp (preferred)

Download the auto-generated VTT subtitle file:
```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download -o "sources/_drafts/NNN-vtt" <youtube-url>
```

This creates `sources/_drafts/NNN-vtt.en.vtt`. Convert the VTT to raw transcript markdown:
- Strip VTT headers and metadata lines
- Merge consecutive duplicate lines (VTT repeats text across overlapping cue boundaries)
- Convert VTT timestamps (`HH:MM:SS.mmm`) to `[MM:SS]` format
- Insert a timestamp marker every ~30 seconds (not every line)
- Produce clean, readable paragraphs between timestamps

### Step 4b: Fallback — Extract transcript via Playwright

If yt-dlp fails (no auto-captions available), use Playwright browser automation:

**Navigate to the video page:**
1. `browser_navigate` → the YouTube video URL
2. `browser_wait_for` text "Subscribe" — confirms page load

**Handle consent dialog (if present):**
3. `browser_snapshot` — check for cookie/consent dialog
4. If consent dialog found → `browser_click` "Accept all" or "Reject all"

**Expand description and open transcript:**
5. `browser_snapshot` → find the "...more" button in the description area
6. `browser_click` → "...more" to expand the description
7. `browser_snapshot` → find "Show transcript" button
8. `browser_click` → "Show transcript"
9. `browser_wait_for` text "Search in video" — confirms transcript panel loaded

**Extract transcript segments:**
10. `browser_evaluate` with this JavaScript:
```javascript
() => {
  const segments = document.querySelectorAll('ytd-transcript-segment-renderer');
  if (segments.length === 0) return { error: 'No transcript segments found' };
  const result = [];
  segments.forEach(seg => {
    const timestamp = seg.querySelector('.segment-timestamp')?.textContent?.trim() || '';
    const text = seg.querySelector('.segment-text')?.textContent?.trim() || '';
    if (text) result.push({ timestamp, text });
  });
  return { segments: result, count: result.length };
}
```

**Clean up:**
11. `browser_close`

### Step 5: Save the raw transcript

Create `sources/_drafts/` directory if it doesn't exist.

Save to `sources/_drafts/NNN-raw-transcript.md` with this format:

```markdown
# Raw Transcript: Video Title

- **URL**: https://youtube.com/watch?v=...
- **Creator**: Channel Name
- **Date**: YYYY-MM-DD (publication date)
- **Duration**: MM:SS
- **Captured**: YYYY-MM-DD (today's date)
- **Method**: Playwright automated extraction
- **Segments**: N segments extracted

---

[timestamp] text
[timestamp] text
...
```

### Step 6: Report and hand off

Print a summary:
- Video title and creator
- Number of transcript segments extracted
- Draft file path
- Suggest next step: `/synthesize-source <url>`

## Fallback Handling

If yt-dlp returns no subtitles:
- Fall back to Playwright extraction (Step 4b above)

If Playwright "Show transcript" button is also NOT found:
- Report that the video may not have captions available
- Suggest manual alternatives:
  - Check if the video has community-contributed captions
  - Use [youtubetranscript.com](https://youtubetranscript.com)

If transcript segments return empty:
- Take a screenshot for debugging: `browser_take_screenshot`
- Report the issue and suggest manual extraction

## Notes

- Raw transcripts are saved in `sources/_drafts/` — this directory is for working files
- YouTube auto-generated transcripts may have errors — the synthesis step interprets intent, not exact wording
- The Playwright selectors (`ytd-transcript-segment-renderer`, `.segment-timestamp`, `.segment-text`) may change with YouTube frontend updates — see REFERENCE.md for troubleshooting
- For batch processing, run this skill for each video sequentially to avoid rate limiting
