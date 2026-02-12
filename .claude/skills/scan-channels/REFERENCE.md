# Scan Channels — Reference Material

## RSS Feed Format

YouTube channel RSS feeds are available at:
```
https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID
```

### Feed Structure (Atom XML)
```xml
<feed>
  <title>Channel Name</title>
  <link rel="alternate" href="https://www.youtube.com/channel/CHANNEL_ID"/>
  <entry>
    <id>yt:video:VIDEO_ID</id>
    <yt:videoId>VIDEO_ID</yt:videoId>
    <yt:channelId>CHANNEL_ID</yt:channelId>
    <title>Video Title</title>
    <link rel="alternate" href="https://www.youtube.com/watch?v=VIDEO_ID"/>
    <published>2026-02-11T12:00:00+00:00</published>
    <updated>2026-02-11T12:00:00+00:00</updated>
    <media:group>
      <media:title>Video Title</media:title>
      <media:description>Video description text...</media:description>
      <media:thumbnail url="https://i.ytimg.com/vi/VIDEO_ID/hqdefault.jpg"/>
    </media:group>
  </entry>
  <!-- Up to 15 entries -->
</feed>
```

### Limitations
- **15 most recent uploads only** — older videos are not included
- **No duration data** — RSS doesn't include video length
- **No view count** — use WebSearch or noembed for engagement metrics
- **Shorts included** — RSS feeds include Shorts alongside regular videos; filter by title/description if needed
- **Delay**: New uploads may take 15-30 minutes to appear in the RSS feed

### WebFetch Parsing
When using `WebFetch` on an RSS URL, ask the AI to extract:
- All `<entry>` elements
- For each: title, video URL (from `<link>` href), published date, description
- The video ID (from `<yt:videoId>` or extracted from URL)

## Search Strategies (Supplementary)

### When RSS Isn't Enough
Use WebSearch to supplement RSS when:
- Looking for videos older than the 15-item window
- Searching for specific topics across multiple channels
- Verifying whether a channel has covered a topic recently

### Effective WebSearch Queries
```
# Recent videos from a specific channel
site:youtube.com "@BartSlodyczka" claude code 2026
site:youtube.com "IndyDevDan" agentic 2026

# Broader topic search
claude code tutorial 2026 -site:reddit.com
AI agent orchestration new 2026
```

## Relevance Assessment

When evaluating whether a video is worth indexing, consider:

### High Relevance (definitely index)
- Directly about Claude Code, Cursor, or other AI coding tools
- Covers agentic patterns, multi-agent orchestration, skills/hooks
- Analyzes AI industry economics or infrastructure constraints
- Provides critical/skeptical perspective on AI hype
- Demonstrates practical workflows that engineering teams can adopt

### Medium Relevance (probably index)
- General AI tool comparison or review
- AI strategy and adoption advice
- Security analysis of AI agent ecosystems
- Model capability analysis (benchmarks, limitations)

### Low Relevance (skip unless exceptional)
- Product announcements without analysis
- Pure marketing content
- Tutorials for non-development AI tools (art, music, etc.)
- Content that duplicates an existing source without new perspective

## Keyword Matching Rules

A video is considered keyword-relevant if its **title or description** contains any of the channel's configured keywords (case-insensitive). The matching is intentionally permissive — it's better to surface a video for human review than to miss it.

## Channel IDs

All channel IDs are stored in `watchlist/channels.yaml` with pre-computed RSS URLs. If a new channel needs to be added:

1. Visit the channel page (e.g., `https://www.youtube.com/@handle`)
2. Use browser DevTools or Playwright to extract the channel ID:
   ```javascript
   document.documentElement.innerHTML.match(/"externalId":"(UC[^"]+)"/)[1]
   ```
3. Add to channels.yaml with the computed RSS URL
