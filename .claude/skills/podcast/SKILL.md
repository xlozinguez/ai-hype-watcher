---
name: podcast
description: "Generate a two-host AI podcast episode from briefings, synthesis docs, or source notes. Writes a dialogue script and optionally renders audio via ElevenLabs TTS + ffmpeg."
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
argument-hint: "<briefing-date | synthesis-path | source-ids | 'latest' | --draft>"
---

# Podcast

Generate a two-host podcast episode script from AI Hype Watcher content. Two hosts — The Builder (technically optimistic) and The Skeptic (economics-focused, hype-checking) — discuss the material in a natural, engaging conversation.

## Input

One of:
- **Briefing date** (e.g., `2026-04-03`) — read that briefing + its referenced source notes
- **Synthesis path** (e.g., `synthesis/2026-04-03-weekly-themes.md`) — read that synthesis doc + referenced sources
- **Source ID range** (e.g., `401-424`) — read sources in that range, group by theme
- **`latest`** — find the most recent briefing and use it
- **`--draft` flag** — stop after script generation, skip audio rendering

Multiple inputs can be combined (e.g., `2026-04-03 --draft`).

## Workflow

### Step 1: Read reference material

Read `.claude/skills/podcast/REFERENCE.md` for host personas, dialogue guidelines, script structure, and quality rules.

### Step 2: Read show config

Read `podcast/_config.yaml` for show metadata and the next episode number.

### Step 3: Resolve input to content

**If briefing date**: Read `briefings/YYYY-MM-DD.md`. Extract all source IDs referenced in the briefing. Read each referenced source note from `sources/` to get full detail (Summary, Key Concepts, Practical Takeaways, Notable Quotes).

**If synthesis path**: Read the synthesis document. Extract source IDs from frontmatter. Read those source notes.

**If source ID range**: Use Glob to find `sources/NNN-*.md` files in the range. Read each one. Group them by shared tags or curriculum modules to identify themes.

**If `latest`**: Read `briefings/README.md`, find the most recent entry, then resolve as a briefing date.

### Step 4: Read the script template

Read `podcast/_template-script.md` for the expected script format.

### Step 4b: Cross-reference STATE.md

Read `STATE.md`. When topics overlap with tracked theses, the hosts should reference current status — e.g., "this is now a confirmed pattern" or "new evidence is challenging this idea."

### Step 5: Generate the dialogue script

Using the content bundle from Step 3 and the guidelines from REFERENCE.md, write a two-host dialogue script:

1. **Identify 3-4 segments** from the content — cluster related sources into narrative threads
2. **Write the cold open** — hosts tease the most surprising or provocative finding (~30 sec)
3. **Write the intro** — show name, brief framing of today's episode (~15 sec)
4. **Write each segment** — both hosts engage with the material, cite specific sources by creator name, reference concrete numbers and claims. Follow the dialogue quality rules from REFERENCE.md
5. **Write the rapid-fire section** (if sources remain) — shorter treatment of 2-4 additional items
6. **Write the closing** — key takeaways, what to watch next, sign-off (~1 min)

Target length: ~2,250 words (~15 minutes at conversational pace). For smaller content bundles (single source or thin briefing), target ~1,200 words (~8 minutes).

### Step 6: Write the script file

Write to `podcast/scripts/EPNNN-YYYY-MM-DD.md` using the episode number from config and today's date (or the briefing date if specified).

### Step 7: Update episode counter

Edit `podcast/_config.yaml` to increment `next_episode`.

### Step 8: Render audio (unless --draft)

If `--draft` flag is NOT set and `ELEVENLABS_API_KEY` is found in `.env`:

```bash
python3 podcast/compose.py podcast/scripts/EPNNN-YYYY-MM-DD.md
```

This parses the script, calls ElevenLabs TTS for each speaker segment, and uses ffmpeg to compose the final episode.

If `--draft` is set or no API key is found, skip audio rendering and report:
- Script file path
- Estimated duration
- Character count (for TTS budgeting)

### Step 9: Report

Print:
- Episode number and title
- Script path
- Audio path (if rendered)
- Segment count and estimated duration
- Sources covered
- Character count used (for TTS budget tracking)

## Error Handling

- **Briefing not found**: Report available briefing dates, ask user to pick one
- **Source notes missing**: Warn which source IDs couldn't be found, continue with available content
- **Content too thin** (< 500 words of source material): Suggest combining with additional sources or a different date range
- **TTS API failure**: Save partial audio, report which segments failed, allow re-running `compose.py` to retry only failed segments
- **No API key**: Skip audio rendering, output script only with character count for budget planning
