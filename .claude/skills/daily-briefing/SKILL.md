---
name: daily-briefing
description: Generate a dated findings briefing. Can process provided URLs, search for latest AI dev news, or both.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
argument-hint: "[urls or topic keywords]"
---

# Daily Briefing

Generate a dated briefing entry covering recent AI development findings, tools, and perspectives.

## Input

One or more of:
- URLs to articles/videos to cover
- Topic keywords to search for (e.g., "claude code update", "ai agent security")
- Nothing (auto-search for latest AI development news)

## Workflow

### Step 1: Read the template

Read `briefings/_template.md` for the expected structure.

### Step 2: Read reference material

Read `.claude/skills/daily-briefing/REFERENCE.md` for briefing guidelines and topic categories.

### Step 3: Gather content

**If URLs provided**: Use WebFetch to read each URL and extract key information.

**If keywords provided**: Use WebSearch to find recent (last 7 days) articles and discussions matching the keywords. Use WebFetch to read the most relevant results.

**If neither**: Use WebSearch to find the latest news across these topics:
- Claude Code updates and features
- AI agent orchestration developments
- AI coding tool releases and comparisons
- AI industry economics and infrastructure
- AI safety and security developments

### Step 4: Cross-reference existing sources

Read `sources/README.md` to check if any of the gathered content overlaps with existing source notes. Note connections and new perspectives.

### Step 5: Synthesize the briefing

Write a briefing covering:
- **Headlines**: 3-5 most significant findings (tag each with `[critical]`, `[tools]`, `[economics]`, `[patterns]`, `[security]`, `[research]`, `[ecosystem]`)
- **Details**: 1-2 paragraph synthesis for each headline item. Reference source IDs with links (e.g., `[038](../sources/038-interface-studies-prompt-interface.md)`)
- **Also Ingested**: Brief 2-3 sentence summaries for sources that don't warrant full detail sections
- **Connections to Existing Sources**: Pairwise connections between new and existing sources (e.g., `038 ↔ [011: Context Engineering]`). Explain what each connection reveals.
- **Action Items**: Anything that warrants a new source note, curriculum update, or further investigation
  - Check for recent `/scan-channels` results or run a lightweight RSS check on high-priority channels
  - Surface any undiscovered content with ready-to-run `/ingest` commands
  - **Synthesis opportunities**: If 4+ sources cluster around a theme, suggest a synthesis doc

### Step 6: Write the briefing file

Write to `briefings/YYYY-MM-DD.md` using today's date. If a briefing already exists for today, append a sequence number (e.g., `2026-02-11-2.md`).

### Step 7: Update the briefings index

Edit `briefings/README.md` to add the new briefing to the index.

## Output

The path to the newly created briefing file.
