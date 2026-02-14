# AI Hype Watcher — Claude Code Context

Curated AI-assisted development learning resource — from fundamentals to agentic orchestration. Includes critical perspective on AI industry economics and hype cycles.

## Repository Structure

```
sources/          → Individual video/article notes (NNN-creator-topic.md)
curriculum/       → Progressive 6-module learning path
briefings/        → Dated findings entries
synthesis/        → Cross-source analyses
resources/        → Curated external links
watchlist/        → YouTube channel watchlist and scanning config
```

## Conventions

### Source Notes (`sources/`)
- Files are named `NNN-creator-topic.md` with 3-digit zero-padded IDs
- Each file has YAML frontmatter with: source_id, title, creator, platform, url, date, duration, type, tags, curriculum_modules
- Template: `sources/_template.md`
- Index: `sources/README.md` — must be updated when adding/removing sources

### Curriculum (`curriculum/`)
- 6 modules numbered 01-06
- Each module has a README.md with overview and section links
- Content is compiled from tagged sources using `/compile-curriculum`

### Briefings (`briefings/`)
- Files named `YYYY-MM-DD.md`
- Template: `briefings/_template.md`
- Index: `briefings/README.md`

### Synthesis (`synthesis/`)
- Cross-source analysis documents
- Files named `YYYY-MM-DD-topic.md`

## Skills

| Skill | Purpose |
|-------|---------|
| `/ingest` | Full pipeline orchestrator — transcribe, synthesize, and index a source in one step |
| `/synthesize-source` | Convert a YouTube video or article URL into a structured source note |
| `/compile-curriculum` | Rebuild curriculum sections from tagged sources |
| `/daily-briefing` | Generate a dated findings briefing |
| `/youtube-transcriber` | Extract YouTube video transcript via Playwright and prepare for synthesis |
| `/scan-channels` | Scan YouTube watchlist RSS feeds for new relevant content |
| `/pr-description` | Generate a PR description summarizing new knowledge introduced by source notes |

## Common Workflows

### Single source ingestion
```
/ingest <youtube-url>       # Transcribe + synthesize in one step
/ingest <article-url>       # Fetch + synthesize
```

### Batch ingestion (playlist or multiple URLs)
1. Download VTT files: `yt-dlp --write-auto-sub --sub-lang en --skip-download -o "sources/_drafts/NNN-vtt" <url>`
2. Convert each VTT to raw transcript markdown in `sources/_drafts/NNN-raw-transcript.md`
3. Run `/synthesize-source` for each (can be parallelized via Task agents — one per source)
4. Update curriculum modules with new source content
5. Create or update a synthesis doc if 4+ sources cluster around a theme
6. Create or update the daily briefing
7. Commit, push, and create PR with `/pr-description`

### Daily workflow
```
/ingest scan                # Discover new content from watchlist
/daily-briefing             # Generate today's briefing
```

### Post-ingest checklist
After ingesting a batch of sources, always:
- [ ] Update relevant curriculum modules (01-06)
- [ ] Create a synthesis doc if sources share a theme (`synthesis/YYYY-MM-DD-topic.md`)
- [ ] Create or update the daily briefing (`briefings/YYYY-MM-DD.md`)
- [ ] Update all README indexes (sources, briefings, synthesis)

## Date Conventions

- **Briefings and synthesis docs** are dated by the day they are created/published, not by the source publication dates
- **Source notes** record the original publication date in frontmatter (`date` field)
- If a batch spans multiple work sessions, split briefings/synthesis by session date

## Parallel Processing

- **Transcript extraction**: Sequential (Playwright rate limiting)
- **VTT download via yt-dlp**: Sequential per playlist, but multiple playlists can run in parallel
- **VTT-to-transcript conversion**: Parallelizable (one Task agent per file)
- **Source synthesis**: Parallelizable (one Task agent per source)
- **Curriculum/briefing/synthesis updates**: Parallelizable (one Task agent per concern), but watch for conflicts on shared files like `sources/README.md`

## Rules

- Never fabricate quotes — only include quotes that appear in source material
- Always attribute ideas to their original creator
- When synthesizing videos, focus on key concepts and practical takeaways — do not attempt to transcribe
- Maintain skeptical perspective: acknowledge both genuine capabilities and hype dynamics
- Keep source IDs sequential — check `sources/README.md` for the next available ID
- Tags should be lowercase, hyphenated (e.g., `claude-code`, `agent-teams`, `prompt-engineering`)
