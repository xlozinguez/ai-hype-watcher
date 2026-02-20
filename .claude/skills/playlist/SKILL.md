---
name: playlist
description: "Process an entire YouTube playlist — batch-download subtitles, synthesize all videos in parallel via agent teams, and run full post-ingest pipeline (index, synthesis, briefing, curriculum)."
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, Task, TeamCreate, TeamDelete, TaskCreate, TaskList, TaskUpdate, TaskGet, SendMessage, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_click, mcp__playwright__browser_evaluate, mcp__playwright__browser_wait_for, mcp__playwright__browser_close, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_press_key
argument-hint: "<youtube-playlist-url>"
---

# Playlist

Process an entire YouTube playlist end-to-end: extract video URLs, batch-download subtitles, synthesize all videos in parallel via agent teams, then run the full post-ingest pipeline.

## Input

A YouTube playlist URL (any URL containing `list=PLAYLIST_ID`).

## Workflow

### Phase 1: Extract Playlist Metadata (team-lead)

1. Use `yt-dlp --flat-playlist --print url --print title` to extract all video URLs and titles from the playlist
2. Determine next available source ID from `sources/README.md`
3. Deduplicate: check extracted URLs against existing entries in `sources/README.md`
4. Assign sequential source IDs to new (non-duplicate) videos
5. Report: N total videos, M new, K duplicates skipped

### Phase 2: Batch Download Subtitles (team-lead)

Download all VTT files in one `yt-dlp` command:

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download \
  -o "sources/_drafts/playlist-%(playlist_index)03d" \
  "PLAYLIST_URL"
```

Then rename playlist-indexed files to source IDs:
- `playlist-001.en.vtt` → `{first_source_id}-vtt.en.vtt`
- `playlist-002.en.vtt` → `{first_source_id + 1}-vtt.en.vtt`
- etc.

### Phase 3: Convert VTTs to Raw Transcripts (team-lead)

Convert each VTT to a raw transcript using the Python conversion script (see REFERENCE.md):

```bash
python3 -c "SCRIPT" < sources/_drafts/NNN-vtt.en.vtt > sources/_drafts/NNN-raw-transcript.md
```

This can be parallelized — run multiple conversions via background bash commands.

### Phase 4: Gather Video Metadata (team-lead)

For each video, gather metadata:
1. Use `curl -sL "https://noembed.com/embed?url=URL"` for title and creator
2. Use `yt-dlp --print duration --print upload_date` for date and duration
3. Build a metadata map: `{ source_id → { title, creator, url, date, duration } }`

### Phase 5: Parallel Synthesis (agent team)

Spawn a team with synthesis agents. Divide videos into batches of 4-5:

| Agent | Source IDs | Count |
|-------|-----------|-------|
| synth-a | first batch | 4-5 |
| synth-b | second batch | 4-5 |
| synth-c | third batch | 4-5 |
| synth-d | remaining | remainder |

Each agent:
1. Reads `sources/_template.md` and `.claude/skills/synthesize-source/REFERENCE.md`
2. For each assigned source ID:
   - Reads the raw transcript from `sources/_drafts/NNN-raw-transcript.md`
   - Uses the metadata map for frontmatter fields
   - Synthesizes a structured source note (NOT a reformatted transcript)
   - Writes to `sources/NNN-creator-topic.md`
3. Reports completion with list of files created

### Phase 6: Index Update (team-lead, sequential)

Update `sources/README.md` with all new entries in a single edit. Format:
```
| [NNN](NNN-creator-topic.md) | Title | Creator | video | tag1, tag2 |
```

### Phase 7: Cross-Source Synthesis (team-lead)

Write `synthesis/YYYY-MM-DD-playlist-themes.md`:
- Read all newly created source files
- Identify 3-5 cross-cutting themes
- Create a synthesis document following existing patterns in `synthesis/`

### Phase 8: Daily Briefing (team-lead)

Generate `briefings/YYYY-MM-DD.md`:
- Read `.claude/skills/daily-briefing/REFERENCE.md` and `briefings/_template.md`
- Summarize the playlist batch ingestion
- Cross-reference with existing sources
- Update `briefings/README.md`

### Phase 9: Curriculum Recompilation (2 parallel agents)

Spawn 2 agents to recompile curriculum modules:

| Agent | Modules |
|-------|---------|
| curriculum-a | 01-foundations, 02-prompting-and-workflows, 03-claude-code-essentials |
| curriculum-b | 04-agentic-patterns, 05-team-orchestration, 06-strategy-and-economics |

Each agent reads `.claude/skills/compile-curriculum/REFERENCE.md` and all sources tagged for their modules, then rewrites the module READMEs.

## Error Handling

- **No captions**: Report immediately. Try Playwright transcript extraction as fallback. If both fail, skip the source ID and offer to replace with alternative URL.
- **Partial playlist**: If some videos fail, continue with successful ones. Report gaps at end.
- **Rate limiting**: If yt-dlp hits rate limits, pause and retry with `--sleep-interval 5`.
- **Agent failures**: If a synthesis agent fails, the team-lead picks up remaining sources.

## Output

Summary report:
- Number of sources created (with ID range)
- Synthesis document path
- Briefing document path
- Curriculum modules updated
- Any failures or skipped videos
