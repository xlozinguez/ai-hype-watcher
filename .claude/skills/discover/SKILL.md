---
name: discover
description: Browse YouTube to find relevant AI-assisted development content beyond the watchlist. Supports topic search, trending scan, and channel scouting. Produces a curated list for human review — no auto-ingestion.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_click, mcp__playwright__browser_type, mcp__playwright__browser_press_key, mcp__playwright__browser_evaluate, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_close
argument-hint: "<topic> | trending | channels"
---

# Discover — YouTube Content Scout

Find relevant AI-assisted development content beyond the 8-channel watchlist. Produces a curated list for human review — no auto-ingestion.

## Input

One of:
- `<topic>` — search YouTube for a specific topic (e.g., `claude code hooks`, `ai agent security`)
- `trending` — scan for trending topics derived from the tag taxonomy
- `channels` — scout for new channels to recommend for the watchlist

## Workflow

### Mode 1: Topic Search (`/discover <topic>`)

#### Step 1: Load context for dedup

1. Read `sources/README.md` to get all existing source URLs, titles, and tags
2. Read `watchlist/channels.yaml` to know which channels are already tracked

#### Step 2: Search YouTube via Playwright

1. Navigate to `https://www.youtube.com/results?search_query=<url-encoded-topic>&sp=CAISBAgCEAE` (filter: this month, relevance)
2. Take a snapshot of the search results page
3. Extract up to 15 results:
   - Video title
   - Channel name
   - Video URL (construct from video ID: `https://www.youtube.com/watch?v=VIDEO_ID`)
   - Upload date (relative text like "2 days ago")
   - View count (if visible)
4. If results look thin, also try a WebSearch query:
   ```
   site:youtube.com "<topic>" AI 2026
   ```

#### Step 3: Supplement with WebSearch

Run a WebSearch for the topic to catch content YouTube's algorithm might deprioritize:
```
site:youtube.com <topic> 2026
```

#### Step 4: Score and filter

For each result:

1. **Dedup check**: Skip if video URL or title already appears in `sources/README.md`
2. **Watchlist overlap**: Flag if the channel is already in `channels.yaml` (not a reason to skip, but note it)
3. **Relevance score** (1-5):
   - 5 = Directly covers AI-assisted development practices (agentic coding, Claude Code, skills, agent teams)
   - 4 = Covers adjacent topic with clear connection (prompt engineering, AI tooling, SDLC changes)
   - 3 = General AI/LLM content with some relevance
   - 2 = Tangentially related (general coding, productivity)
   - 1 = Not relevant — exclude from results
4. **Novelty assessment**: Does this cover ground not already in existing sources? Check against tag taxonomy.

#### Step 5: Output curated list

Print results scored 3+ in a structured report:

```markdown
## Discovery: "<topic>" — YYYY-MM-DD

### Top Finds (score 4-5)

| # | Video | Channel | Score | Why |
|---|-------|---------|-------|-----|
| 1 | [Title](url) | Creator (tracked/new) | 5 | Brief relevance note |
| 2 | [Title](url) | Creator (new) | 4 | Brief relevance note |

### Worth a Look (score 3)

| # | Video | Channel | Score | Why |
|---|-------|---------|-------|-----|
| 3 | [Title](url) | Creator | 3 | Brief relevance note |

### Skipped
- N videos excluded (already indexed or score < 3)

---
**Next steps:**
- `/ingest <url>` to ingest a video
- `/discover channels` if any new creators look promising
```

---

### Mode 2: Trending Scan (`/discover trending`)

#### Step 1: Load context

1. Read `sources/README.md` for existing coverage
2. Read the tag taxonomy from `.claude/skills/synthesize-source/REFERENCE.md`
3. Read `watchlist/discovery-log.md` to see what was recently searched (avoid redundant scans)

#### Step 2: Build search queries from taxonomy

Generate search queries from the tag taxonomy, focusing on tags with active coverage:

**Priority queries** (core topics):
- `"claude code" tips 2026`
- `"agentic coding" workflow 2026`
- `"AI agent" teams coding 2026`
- `"prompt engineering" AI development 2026`
- `"vibe coding" 2026`
- `AI coding assistant security 2026`
- `"AI bubble" economics 2026`
- `"MCP" model context protocol 2026`

**Secondary queries** (broaden the net):
- `AI software development lifecycle 2026`
- `"AI coding" best practices 2026`
- `multi-agent orchestration coding 2026`
- `AI infrastructure economics compute 2026`

Skip any query that was already run in the discovery log within the past 7 days.

#### Step 3: Execute searches

For each query (up to 8 per session to avoid rate limiting):

1. Use WebSearch: `site:youtube.com <query>`
2. Collect results — title, URL, channel, description snippet
3. Dedup against existing sources and against results from prior queries in this session

#### Step 4: Cross-reference trending signals

Look for **convergence signals**:
- Multiple creators covering the same topic = trending signal
- Note when 2+ independent channels release videos on the same theme within a week

#### Step 5: Output trending report

```markdown
## Trending Scan — YYYY-MM-DD

### Trending Signals
Topics with coverage from multiple creators:

**<Topic>** — N creators
- [Video 1](url) by Creator A
- [Video 2](url) by Creator B
- Assessment: Brief note on whether this is worth tracking

### Individual Finds

| # | Video | Channel | Query | Relevance |
|---|-------|---------|-------|-----------|
| 1 | [Title](url) | Creator | query used | Brief note |

### Queries Run
- `query 1` — N results, M relevant
- `query 2` — N results, M relevant

---
**Next steps:**
- `/ingest <url>` for high-value finds
- `/discover <topic>` to deep-dive a trending topic
```

---

### Mode 3: Channel Scout (`/discover channels`)

#### Step 1: Load context

1. Read `watchlist/channels.yaml` for existing channels
2. Read `sources/README.md` to identify creators who appear in sources but aren't on the watchlist
3. Read `watchlist/discovery-log.md` for previously scouted channels

#### Step 2: Mine existing sources for unlisted creators

Check if any creators in `sources/README.md` are not yet in `channels.yaml`. These are immediate candidates.

#### Step 3: Search for new channels via Playwright

For each high-value search query:

1. Navigate to YouTube search with channel filter:
   `https://www.youtube.com/results?search_query=<query>&sp=EgIQAg%3D%3D` (filter: channels)
2. Take a snapshot, extract channel names and subscriber counts
3. Also try WebSearch:
   ```
   site:youtube.com "claude code" OR "agentic coding" OR "AI coding" channel 2026
   ```

#### Step 4: Evaluate channel candidates

For each candidate channel:

1. Navigate to their channel page via Playwright
2. Take a snapshot of their recent uploads
3. Assess:
   - **Content alignment**: How many recent videos are relevant to AI-assisted development?
   - **Frequency**: How often do they upload?
   - **Unique angle**: Do they offer a perspective not already covered by existing watchlist channels?
   - **Quality signal**: Subscriber count, production quality, depth of content

#### Step 5: Output channel recommendations

```markdown
## Channel Scout — YYYY-MM-DD

### Recommended Additions

| Channel | Handle | Focus | Why Add | Suggested Priority |
|---------|--------|-------|---------|--------------------|
| Name | @handle | Brief focus | What they bring that's new | high/medium/low |

### Already Tracked (from sources)
- Creator X — already in channels.yaml as @handle

### Evaluated but Not Recommended
- Channel Y — Reason (e.g., too broad, overlaps with existing)

---
**Next steps:**
- Approve additions → I'll update `watchlist/channels.yaml`
- `/discover <topic>` to check a specific channel's content
```

---

## Post-Discovery: Update Log

After every discovery session (any mode), append an entry to `watchlist/discovery-log.md`:

```markdown
### YYYY-MM-DD — Mode: <topic|trending|channels>

**Queries**: list of search queries used
**Results**: N videos found, M scored 3+
**Actions taken**: What the user decided to ingest or skip
**New channels**: Any channels added to watchlist
```

## Rate Limiting

- **Playwright YouTube browsing**: Max 10 page loads per session. Use WebSearch as primary, Playwright for enrichment.
- **WebSearch**: Max 12 queries per session across all modes
- Pause 2-3 seconds between Playwright navigations (use `browser_wait_for` with `time: 3`)
- If a CAPTCHA is encountered, stop Playwright browsing and fall back to WebSearch only

## Notes

- This skill creates no source files — it only reports findings for human review
- The discovery log (`watchlist/discovery-log.md`) is the only file modified
- Use `/ingest <url>` to process any discovered content
- Redundancy check: if 4+ existing sources cover a topic, flag new finds as "likely redundant unless novel angle"
- Always respect existing channel priorities — don't recommend upgrading without clear justification
