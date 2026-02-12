# Scan Channels — Reference Material

## Search Strategies

### YouTube Channel Search Patterns

Since YouTube's public search is the primary discovery mechanism, use these patterns for best results:

```
# Recent videos from a specific channel
site:youtube.com "@BartSlodyczka" claude code
site:youtube.com "IndyDevDan" agentic

# Channel + topic combinations
"Nate B Jones" youtube AI strategy 2026
"Confluent Developer" youtube AI agents kafka

# Broader topic search (when channel-specific search yields nothing)
claude code tutorial 2026 -site:reddit.com
AI agent orchestration new 2026
```

### RSS Feed URLs

YouTube channels expose RSS feeds that can be more reliable than search:

```
https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID
```

To find a channel's ID, visit their channel page and look for the canonical URL or use:
```
https://www.youtube.com/@handle → view page source → "channelId"
```

Known channel IDs (add as discovered):
```yaml
# Add channel IDs here as they're discovered
# BartSlodyczka: UC...
# indydevdan: UC...
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

## Output Format

Keep the findings report concise. For each relevant video:
- Title with link
- Publication date and duration (if available)
- Which keywords matched
- One-sentence relevance assessment
- Ready-to-run `/synthesize-source` command
