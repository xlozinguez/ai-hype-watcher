---
name: digest
description: Thematic digest of a source range — what's genuinely new vs. reinforcement of existing coverage, clustered by theme.
allowed-tools: Read, Glob, Grep
argument-hint: "range:<start>-<end> | recent"
---

# Digest — Batch Thematic Summary

Generate a thematic digest for a set of sources, identifying what's genuinely new territory vs. deepened coverage of existing themes. Clusters sources by shared topics and assesses curriculum impact.

## Input

One of:
- `range:<start>-<end>` — digest sources in this ID range (e.g., `range:172-209`)
- `recent` — digest the last 25 sources by ID

## Workflow

### Step 1: Identify the source set

1. Parse the input to determine the source range
2. Use `Glob` to find matching source files: `sources/[0-9][0-9][0-9]-*.md`
3. Filter to the requested range or take the last 25 for `recent`

### Step 2: Read source metadata

For each source in the set, read the frontmatter and extract:
- `source_id`, `title`, `creator`, `date`
- `tags` (full list)
- `curriculum_modules`
- The **Key Takeaways** or first summary section (read ~40 lines to capture this)

### Step 3: Compute tag distribution for the batch

Count tag occurrences across the batch sources. This reveals the thematic focus of this batch.

### Step 4: Compare against the full knowledge base

1. Grep across ALL sources (not just the batch) to count total occurrences of each tag
2. For each tag in the batch, compute:
   - **New territory**: Tags that appear in the batch but have ≤2 sources outside the batch → this batch introduces a new topic
   - **Deepened coverage**: Tags that appear both in the batch and in 3+ prior sources → reinforcement
   - **Unique to batch**: Tags exclusive to this batch (0 prior sources)

### Step 5: Cluster sources by theme

Group batch sources into 3-6 thematic clusters based on shared tags:

1. Find tag pairs that co-occur in 2+ batch sources
2. Group sources that share the most tags into clusters
3. Name each cluster with a descriptive theme label
4. For each cluster, write a 2-3 sentence summary of what these sources collectively teach

### Step 6: Check for existing briefings and synthesis

1. Glob `briefings/*.md` and `synthesis/*.md` for docs that reference any batch source IDs
2. If briefings/synthesis exist, note them and incorporate their thematic analysis
3. If none exist, note this as a gap

### Step 7: Assess curriculum impact

For each curriculum module (01-06):
- Count how many batch sources map to it
- Note if the batch significantly expands a module's coverage
- Flag if any batch sources cover topics not yet represented in curriculum

## Output Format

```markdown
## Digest: Sources #<start>–#<end>

**<N> sources** | **<date range>** | **<M> unique creators**

### New Territory

Topics this batch introduces or significantly expands:

- **<Topic>** — <2-3 sentence description of what's new>
  Sources: [#NNN], [#NNN]

### Deepened Coverage

Topics reinforced by this batch (already well-covered in knowledge base):

- **<Topic>** — <1-2 sentence note on what's added>
  Sources: [#NNN], [#NNN]
  Prior coverage: N existing sources

### Theme Clusters

#### 1. <Cluster Name>
<2-3 sentence summary>
- [#NNN] Creator — Title
- [#NNN] Creator — Title

#### 2. <Cluster Name>
<2-3 sentence summary>
- [#NNN] Creator — Title

[...3-6 clusters total]

### Curriculum Impact

| Module | Batch Sources | Impact |
|--------|--------------|--------|
| 01 Foundations | N | Brief note |
| 02 Prompting | N | Brief note |
| 03 Claude Code | N | Brief note |
| 04 Agentic Patterns | N | Brief note |
| 05 Team Orchestration | N | Brief note |
| 06 Strategy & Economics | N | Brief note |

### Coverage Gaps

- [Note any existing briefings/synthesis docs, or flag if none exist]
- [Note topics that might warrant a new synthesis doc]

---
**Next steps:**
- `/compile-curriculum` to update modules with new content
- `/daily-briefing` to create a briefing if none exists
- `/ask <topic>` to explore a specific theme in depth
```

## Edge Cases

- **Very small range (< 5 sources)**: Skip clustering, just list themes per source
- **All sources same creator**: Note this is a single-creator batch and focus on topic progression
- **No new territory found**: That's a valid finding — note that the batch reinforces existing knowledge
