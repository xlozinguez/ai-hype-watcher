---
name: scan-channels
description: Scan YouTube watchlist channels for new relevant content using RSS feeds. Checks recent uploads against keyword filters and reports findings for potential source note creation.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
argument-hint: "[all | high | @handle | channel-name]"
---

# Scan Channels

Scan monitored YouTube channels for new content relevant to AI-assisted development using RSS feeds.

## Input

One of:
- No argument or `high` — scan only high-priority channels (default)
- `all` — scan all channels regardless of priority
- `@handle` or channel name — scan a specific channel

## Workflow

### Step 1: Load watchlist

Read `watchlist/channels.yaml` to get the channel list with channel IDs, keywords, and priorities.

### Step 2: Load existing sources

Read `sources/README.md` to get the list of already-indexed source URLs and titles. Extract all YouTube video IDs from existing entries to prevent recommending already-indexed content.

### Step 3: Filter channels

Based on the input argument, filter to the appropriate channel set.

### Step 4: Fetch RSS feeds

For each channel in the filtered set:

1. Use `WebFetch` on the channel's RSS feed URL:
   ```
   https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID
   ```
   The `rss_url` field in channels.yaml has this pre-computed.

2. Extract video entries from the RSS feed. Each entry contains:
   - `<title>` — video title
   - `<link>` — video URL (with `href` attribute)
   - `<published>` — publication date (ISO 8601)
   - `<media:description>` — video description
   - `<yt:videoId>` — YouTube video ID

3. **Note**: RSS feeds only contain the **15 most recent uploads**. For older content discovery, fall back to WebSearch (Step 5).

### Step 5: Keyword filter and dedup

For each video entry from RSS:

1. **Dedup check**: Skip if the video URL or video ID already appears in existing sources
2. **Keyword match**: Check if the video title or description contains any of the channel's configured `keywords` (case-insensitive)
3. **Relevance assessment**: Brief judgment on whether the content is worth indexing based on:
   - Direct relevance to AI-assisted development
   - Alignment with curriculum themes
   - Novelty (does it cover ground not already in existing sources?)

### Step 6: Supplementary WebSearch (optional)

If RSS yields few results for a high-priority channel, use WebSearch as a supplementary check:
```
site:youtube.com "@{handle}" {keyword} 2026
```
This catches videos that may have fallen off the 15-item RSS window.

### Step 7: Compile findings report

Create a report listing discovered content, organized by channel:

```markdown
## Scan Results — YYYY-MM-DD

### Channel Name (@handle) — priority
**Feed**: N videos checked, M new relevant found

- **[Video Title](url)** — Published: YYYY-MM-DD
  Keywords matched: keyword1, keyword2
  Relevance: Brief assessment
  Action: `/ingest <url>`

### Channel Name — No new relevant content
Last RSS entry: YYYY-MM-DD — no keyword matches in recent uploads

---

**Summary**: N channels scanned, M new relevant videos found
**Next steps**: Run `/ingest <url>` for each video above, or `/ingest scan` to process all
```

### Step 8: Output findings

Print the findings report. If new relevant content was found, suggest `/ingest` commands for processing.

## Notes

- RSS feeds are fast and reliable but limited to the 15 most recent uploads per channel
- The scan creates no files — it only reports findings for human review
- For comprehensive discovery beyond the RSS window, use WebSearch as a supplement
- Run scans regularly (daily or weekly) to catch new content before it falls off the RSS window
