---
name: research-curriculum
description: Validate curriculum concepts against sources and external evidence. Produces research reports with concept strength analysis, contradiction detection, and update recommendations.
allowed-tools: Read, Glob, Grep, Write, WebSearch, WebFetch, Agent, mcp__second-brain__search
argument-hint: "<module-number> [section] | all"
---

# Research Curriculum — Concept Validation Agent

Walk curriculum sections, validate concepts against internal sources and external evidence, and produce structured research reports. Uses a hybrid approach: bulk source scanning for support analysis, Claude for external validation and reasoning.

## Input

- A module number + optional section: `04 core-concepts`, `01 patterns`, `06`
- Or `all` to validate all modules (runs one section at a time)

Section names: `core-concepts`, `patterns`, `pitfalls`, `exercises`

## Workflow

### Step 1: Load concept inventory

Read the target module's `curriculum/NN-*/README.md`. For each concept in the target section(s):
- Extract the concept title and ID
- Extract inline source references (`[#NNN]`, `(#NNN)`)
- Note the concept's strength data from `dashboard/data.json` (strength score, classification, support count, creator count, last supported date)

Prioritize review order:
1. `stale` concepts (low support + old sources) — highest priority
2. `emerging` concepts (few sources) — validate or flag
3. `established` concepts — spot-check for evolution
4. `evergreen` concepts — confirm stability (sample 2-3)

### Step 2: Internal cross-reference (within KB)

For each concept being validated:

1. **Find supporting sources**: Grep `sources/` for keywords from the concept title. Read the Key Concepts and Practical Takeaways sections of matches.

2. **Check for contradictions**: Search for sources that present opposing views on the same topic. Look for phrases like "however", "contrary to", "unlike", "this contradicts".

3. **Check for evolution**: For concepts supported by sources > 6 months old, search for newer sources in the same module that may have updated the pattern. Compare claims.

4. **Record findings**: For each concept, note:
   - Supporting source IDs with dates and creators
   - Any contradicting sources
   - Any evolutionary progression (Pattern X in source #100 → refined in source #400)

### Step 3: External validation (WebSearch + WebFetch)

For concepts classified as `stale`, `emerging`, or flagged with contradictions in Step 2:

1. **WebSearch**: Query the concept title + "2026" + relevant tool/framework name
   - Example: `"builder validator pattern" "claude code" 2026`
   - Example: `"MCP vs CLI" token efficiency 2026`

2. **WebFetch** 2-3 authoritative results:
   - Official documentation (Anthropic, OpenAI, framework docs)
   - Reputable tech blogs (Simon Willison, Hacker News top stories, engineering blogs)
   - Academic or industry reports

3. **Compare**: Does external evidence confirm, evolve, or contradict the curriculum claim?

For `evergreen` concepts: spot-check 1-2 externally to confirm they haven't been superseded.

### Step 4: Produce research report

Write the report to `research/YYYY-MM-DD-module-NN-section.md` with this format:

```markdown
---
type: research-validation
date: YYYY-MM-DD
module: NN-module-name
section: section-name
concepts_reviewed: N
confirmed: N
evolved: N
needs_update: N
---

# Research: Module NN [Section] Validation

> Validated on YYYY-MM-DD. N concepts reviewed across N sources.

## Summary

Brief overview of findings — what's solid, what's changed, what needs attention.

## Confirmed Evergreen (N)

### Concept N: Title
- **Status**: Confirmed
- **Support**: N sources, N creators, latest YYYY-MM-DD
- **Evidence**: Brief explanation of why this remains valid

## Evolved (N)

### Concept N: Title
- **Status**: Evolved
- **Original claim**: What the curriculum currently says
- **Current state**: What has changed
- **Evidence**: [external URL] or [#NNN]
- **Recommended update**: Specific text change suggestion

## Needs Update (N)

### Concept N: Title
- **Status**: Needs update
- **Issue**: What's wrong or outdated
- **Evidence**: [source]
- **Recommended action**: Specific fix

## Emerging — Needs More Support (N)

### Concept N: Title
- **Status**: Emerging, insufficient support
- **Current support**: N sources
- **Recommendation**: Watch for reinforcement or consider merging with related concept
```

### Step 5: Report summary

After writing the report, output a brief summary:
- Module health: X% confirmed, Y% evolved, Z% needs update
- Top 3 urgent updates
- Top 3 strongest concepts

## Rules

- Never fabricate external evidence — only cite URLs you actually fetched
- Always attribute claims to their source (internal or external)
- Distinguish between "this is wrong" (needs update) and "this has evolved" (needs nuance, not removal)
- Enduring engineering principles should not be penalized for age — a builder/validator pattern from 6 months ago confirmed by 15 sources is evergreen, not stale
- The strength score is a first filter, not the final word — low-scoring concepts with unique titles may still be valid and important
- Research reports are recommendations, not automatic curriculum changes — human reviews before any edit
