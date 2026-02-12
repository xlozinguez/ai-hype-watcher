# Ingest — Reference Material

## Pipeline Flow

```
/ingest <youtube-url>          /ingest <article-url>         /ingest scan
        │                              │                           │
        ▼                              ▼                           ▼
  ┌─────────────┐              ┌──────────────┐           ┌───────────────┐
  │  Playwright  │              │   WebFetch   │           │  RSS Feeds +  │
  │  transcript  │              │   content    │           │  keyword scan │
  │  extraction  │              │   fetch      │           │               │
  └──────┬──────┘              └──────┬───────┘           └───────┬───────┘
         │                            │                           │
         ▼                            ▼                           ▼
  ┌──────────────┐             ┌──────────────┐           ┌───────────────┐
  │  Save draft  │             │              │           │ Present hits  │
  │  to _drafts/ │             │              │           │ to user       │
  └──────┬──────┘             │              │           └───────┬───────┘
         │                     │              │                   │
         ▼                     ▼              │                   ▼
  ┌─────────────────────────────────┐         │    ┌──────────────────────┐
  │  Synthesize: read template,     │         │    │  User confirms which │
  │  read reference, apply tags,    │◄────────┘    │  items to process    │
  │  map to curriculum, write note  │              └──────────┬───────────┘
  └──────────────┬──────────────────┘                         │
                 │                                            ▼
                 ▼                                   Loop: Mode A or B
  ┌─────────────────────────────┐                    for each confirmed URL
  │  Update sources/README.md   │
  │  Report created file path   │
  └─────────────────────────────┘
```

## Error Handling

### Transcript Extraction Failure
- **Cause**: No captions, consent dialog, age restriction, selector changes
- **Response**: Log the failure, suggest manual alternatives, skip to next item in batch
- **Recovery**: User can manually paste transcript and run `/synthesize-source` directly

### Rate Limiting
- YouTube may rate-limit Playwright automation if too many pages are loaded quickly
- **Mitigation**: Process videos sequentially with natural pauses between them
- **Signs of rate limiting**: Empty page loads, CAPTCHA prompts, error pages

### Source ID Conflicts
- Always re-read `sources/README.md` before writing a new source file
- In batch mode, increment IDs sequentially (don't pre-assign all IDs upfront)

## Mode Selection Logic

| Input | Detected As | Mode |
|-------|------------|------|
| `https://youtube.com/watch?v=...` | YouTube URL | A (transcribe + synthesize) |
| `https://youtu.be/...` | YouTube URL | A (transcribe + synthesize) |
| `https://example.com/blog/...` | Article URL | B (fetch + synthesize) |
| `scan` | Keyword | C (discover + process) |
| `scan all` | Keyword | C (scan all channels) |

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| `/youtube-transcriber` | Ingest Mode A runs this workflow internally |
| `/synthesize-source` | Ingest Modes A+B run this workflow internally |
| `/scan-channels` | Ingest Mode C runs this workflow internally |
| `/compile-curriculum` | Run separately after ingesting new sources |
| `/daily-briefing` | Run separately; can reference newly ingested sources |
