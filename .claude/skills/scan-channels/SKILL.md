---
name: scan-channels
description: Scan YouTube watchlist channels for new relevant content. Checks recent uploads against keyword filters and reports findings for potential source note creation.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
argument-hint: "[all | @handle | channel-name]"
---

# Scan Channels

Scan monitored YouTube channels for new content relevant to AI-assisted development.

## Input

One of:
- No argument or `high` — scan only high-priority channels (default)
- `all` — scan all channels regardless of priority
- `@handle` or channel name — scan a specific channel

## Workflow

### Step 1: Load watchlist

Read `watchlist/channels.yaml` to get the channel list, keywords, and priorities.

### Step 2: Load existing sources

Read `sources/README.md` to get the list of already-indexed source URLs and titles. This prevents recommending content that's already been synthesized.

### Step 3: Filter channels

Based on the input argument, filter to the appropriate channel set.

### Step 4: Scan each channel

For each channel in the filtered set:

1. Use WebSearch to find recent videos from the channel:
   - Query: `site:youtube.com "@{handle}" {keyword}` (try 2-3 keyword combinations)
   - Also try: `"{channel name}" youtube {keyword} 2026`
   - Focus on content from the last 14 days

2. For each video found, check:
   - Is the URL already in existing sources? (skip if yes)
   - Does the title match any of the channel's keywords? (skip if no match)
   - Is it relevant to AI-assisted development? (use judgment based on title/description)

3. Use WebFetch on promising video URLs to get more details (title, description, date, duration)

### Step 5: Compile findings report

Create a report listing discovered content, organized by channel:

```
## Scan Results — YYYY-MM-DD

### Channel Name (priority)
- **[Video Title](url)** — Published: date, Duration: MM:SS
  Keywords matched: keyword1, keyword2
  Relevance: Brief assessment of why this is worth indexing
  Action: `/synthesize-source URL`

### No New Content
- Channel Name — last checked: date, no new relevant uploads
```

### Step 6: Output findings

If the scan found new relevant content:
- Print the findings report to the console
- Suggest `/synthesize-source` commands for the most relevant items

If no new content was found:
- Report which channels were scanned and that no new relevant content was detected

## Notes

- YouTube doesn't have a public API for listing channel videos without an API key, so we rely on WebSearch to discover recent uploads. This means some videos may be missed if they don't appear in search results yet.
- For more comprehensive scanning, consider adding RSS feed support (YouTube channels have RSS feeds at `https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID`)
- The scan is designed to be fast and lightweight — it doesn't create any files, just reports findings for human review
