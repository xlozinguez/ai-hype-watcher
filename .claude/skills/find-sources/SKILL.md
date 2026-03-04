---
name: find-sources
description: Search and filter the source index by tag, creator, module, date range, keyword, or recency. Returns a formatted table with matches.
allowed-tools: Read, Glob, Grep
argument-hint: "tag:<tag> | creator:<name> | module:<NN> | range:<start>-<end> | keyword:<term> | date:<YYYY-MM> | recent"
---

# Find Sources — Structured Search and Filter

Search the source note index by tag, creator, module, date range, keyword, or recency. Returns a filtered list with summaries and tag distribution.

## Input

One or more filter expressions, space-separated. Filters are combined with AND logic.

| Filter | Example | Matches |
|--------|---------|---------|
| `tag:<tag>` | `tag:agent-teams` | Sources with this tag in frontmatter |
| `creator:<name>` | `creator:Nate` | Sources where creator contains the string (case-insensitive) |
| `module:<NN>` | `module:04` | Sources with this module in `curriculum_modules` |
| `range:<start>-<end>` | `range:172-209` | Sources with IDs in this range |
| `keyword:<term>` | `keyword:security` | Sources mentioning this term in title, tags, or content |
| `date:<YYYY-MM>` | `date:2026-02` | Sources published in this month |
| `recent` | `recent` | Last 25 sources by ID |

Multiple filters: `/find-sources creator:Nate module:06` returns sources by Nate mapped to Module 06.

## Workflow

### Step 1: Parse filters

Extract filter type and value from each argument. If no recognized filter is found, treat the entire input as a keyword search.

### Step 2: Build source file list

1. Use `Glob` to get all source files: `sources/[0-9][0-9][0-9]-*.md`
2. For `range:` filter, narrow to files matching the ID range
3. For `recent` filter, take the last 25 files by ID (highest numbers)

### Step 3: Apply filters by grepping frontmatter

For each filter type, grep the candidate source files:

- **`tag:<tag>`**: Grep for the tag string within the `tags:` frontmatter block
  ```
  Grep pattern: "- <tag>" in each source file, within first 20 lines
  ```
- **`creator:<name>`**: Grep for `creator:.*<name>` (case-insensitive) in frontmatter
- **`module:<NN>`**: Grep for `<NN>-` in the `curriculum_modules` frontmatter field
- **`date:<YYYY-MM>`**: Grep for `date: "<YYYY-MM>` or `date: <YYYY-MM>` in frontmatter
- **`keyword:<term>`**: Grep for the term anywhere in the file (title, tags, content)

For AND logic: start with all candidates, intersect results from each filter.

### Step 4: Extract metadata from matches

For each matched source file, read the frontmatter (first 15-20 lines) and extract:
- `source_id`
- `title`
- `creator`
- `date`
- `tags` (as comma-separated list)
- `curriculum_modules`

### Step 5: Compute tag distribution

Count how many of the matched sources share each tag. This helps users discover related searches.

### Step 6: Output results

## Output Format

```markdown
## Sources: <filter description>

**<N> sources found**

| ID | Title | Creator | Date | Tags |
|----|-------|---------|------|------|
| #NNN | Title text | Creator Name | YYYY-MM-DD | tag1, tag2, tag3 |
| #NNN | Title text | Creator Name | YYYY-MM-DD | tag1, tag2 |

### Tag Distribution

| Tag | Count |
|-----|-------|
| tag-name | N |
| tag-name | N |

### Suggested Filters

- `/find-sources tag:<most-common-tag>` — N sources
- `/find-sources creator:<top-creator>` — N sources
```

## Edge Cases

- **No matches**: Report "No sources found matching <filters>" and suggest relaxing the filters
- **Too many matches (50+)**: Show first 30 with a note that results are truncated, suggest narrowing with additional filters
- **Ambiguous creator name**: If multiple creators match, show all matches grouped by creator
- **Invalid filter syntax**: Treat unrecognized input as a keyword search
