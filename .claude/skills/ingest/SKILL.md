---
name: ingest
description: "Full pipeline orchestrator — transcribe, synthesize, and index a source in one step. Accepts YouTube URLs, article URLs, or 'scan' to discover new content."
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_click, mcp__playwright__browser_evaluate, mcp__playwright__browser_wait_for, mcp__playwright__browser_close, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_press_key
argument-hint: "<youtube-url | article-url | scan | url1 url2 ...>"
---

# Ingest

Full pipeline orchestrator that combines transcript extraction, synthesis, and indexing into a single workflow.

## Input

One of:
- **YouTube URL** → Mode A: transcribe + synthesize
- **Article/blog URL** → Mode B: fetch + synthesize
- **`scan`** → Mode C: discover new content, then process confirmed items

## Mode A: YouTube Video (`/ingest <youtube-url>`)

### Step 1: Transcribe

Run the `/youtube-transcriber` workflow:
1. Validate the YouTube URL and extract video ID
2. Determine the next source ID from `sources/README.md`
3. Gather metadata via `curl -sL "https://noembed.com/embed?url=URL"` + WebSearch for date/duration
4. Extract transcript via Playwright browser automation:
   - Navigate to video URL
   - Expand description ("...more")
   - Click "Show transcript"
   - Wait for transcript panel to load
   - Extract segments via JS: `document.querySelectorAll('ytd-transcript-segment-renderer')`
   - Close browser
5. Save raw transcript to `sources/_drafts/NNN-raw-transcript.md`

### Step 2: Synthesize

Run the `/synthesize-source` workflow using the draft transcript:
1. Read the template from `sources/_template.md`
2. Read reference material from `.claude/skills/synthesize-source/REFERENCE.md`
3. Read the raw transcript from `sources/_drafts/NNN-raw-transcript.md`
4. Synthesize into a structured source note (NOT a reformatted transcript):
   - Summary, Key Concepts, Practical Takeaways, Notable Quotes
   - Assign tags from the established taxonomy
   - Map to curriculum modules
   - Cross-reference related sources
5. Write the source file to `sources/NNN-creator-topic.md`
6. Update `sources/README.md` index

### Step 3: Report

Print:
- Created source file path
- Source ID, title, creator
- Tags and curriculum modules assigned
- Number of transcript segments used

## Mode B: Article/Post (`/ingest <article-url>`)

### Step 1: Fetch content

1. Determine the next source ID from `sources/README.md`
2. Use `WebFetch` on the article URL to extract content
3. Use WebSearch to find: author, publication date, any supplementary context

### Step 2: Synthesize

Same as Mode A Step 2, but using fetched article content instead of a transcript.

### Step 3: Report

Same as Mode A Step 3.

## Mode C: Scan (`/ingest scan`)

### Step 1: Discover

Run the `/scan-channels` workflow:
1. Load `watchlist/channels.yaml` for channel list and RSS URLs
2. Load `sources/README.md` for existing URLs
3. Fetch RSS feeds for high-priority channels (default) or all channels
4. Filter by keywords and dedup against existing sources
5. Compile findings report

### Step 2: Present findings

Show the scan results to the user with relevance assessments. Ask which videos to process:
- "Process all N videos"
- "Process selected videos" (user picks)
- "Skip" (just review the report)

### Step 3: Process confirmed items

For each confirmed URL, run Mode A (YouTube) or Mode B (article) sequentially.

## Error Handling

- **Transcript extraction fails**: Report the failure, suggest manual transcript methods, continue with remaining items if in batch mode
- **WebFetch fails for article**: Report the error, skip the item
- **Source ID conflict**: Re-check `sources/README.md` before each write to avoid overwrites

## Mode D: Batch/Playlist (`/ingest <url1> <url2> ...` or `/ingest <playlist-url>`)

### Step 1: Download all VTT files

For playlists or multiple URLs, use yt-dlp to download VTT files in bulk:
```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download -o "sources/_drafts/NNN-vtt" <url>
```

Assign sequential source IDs starting from the next available in `sources/README.md`.

### Step 2: Convert VTTs to raw transcripts

Can be parallelized — one Task agent per VTT file. Each agent reads the VTT and writes a clean `sources/_drafts/NNN-raw-transcript.md`.

### Step 3: Synthesize all sources

Parallelizable — one Task agent per source. Each reads its raw transcript, the template, and REFERENCE.md, then writes the source note and updates `sources/README.md`.

**Watch for conflicts**: Multiple agents writing to `sources/README.md` simultaneously can cause edit failures. If this happens, re-read and retry after other agents complete.

### Step 4: Post-ingest updates

After all sources are synthesized:
1. **Curriculum**: Update relevant modules (01-06) with new source content
2. **Synthesis**: Create a cross-source synthesis doc if 4+ sources share a theme
3. **Briefing**: Create or update the daily briefing for today's date
4. **Indexes**: Verify all README indexes are current

These can run as 3 parallel Task agents (curriculum, synthesis, briefing).

## Notes

- **yt-dlp is the preferred transcript method** — faster and more reliable than Playwright. Use Playwright only as fallback.
- Process YouTube videos **sequentially** for Playwright extraction to avoid rate limiting
- Articles can be processed without Playwright — they use WebFetch directly
- For batch processing, download all VTTs first, then parallelize synthesis
- The `/ingest` skill combines `/youtube-transcriber` + `/synthesize-source` into one flow — you can still run them separately if needed
