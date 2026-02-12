---
name: synthesize-source
description: Convert a YouTube video or article URL into a structured source note. Gathers metadata, synthesizes key concepts, assigns tags, maps to curriculum modules, and updates the sources index.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
argument-hint: "<url>"
---

# Synthesize Source

Convert a YouTube video or article URL into a structured source note following the repository's template format.

## Input

A URL to a YouTube video or article/blog post. Optionally, the user may provide additional context or notes.

## Workflow

### Step 1: Determine next source ID

Read `sources/README.md` to find the highest existing source ID. The new source gets the next sequential 3-digit zero-padded ID (e.g., if the last is `018`, the new one is `019`).

### Step 2: Gather metadata

Use WebFetch on the provided URL to extract:
- **Title**: Full title of the video/article
- **Creator**: Author or channel name
- **Platform**: YouTube, Blog, etc.
- **Date**: Publication date (YYYY-MM-DD)
- **Duration**: For videos, approximate length (MM:SS)
- **Type**: `video` or `article`

If WebFetch doesn't provide enough metadata, use WebSearch to find additional details (creator name, publication date, etc.).

### Step 3: Read the template

Read `sources/_template.md` for the expected structure.

### Step 4: Read reference material

Read `.claude/skills/synthesize-source/REFERENCE.md` for tag taxonomy and curriculum module mappings.

### Step 5: Synthesize content

Based on the fetched content, write a synthesis (NOT a transcription) covering:
- **Summary**: 2-3 paragraph overview of the source's main argument
- **Key Concepts**: 3-7 subsections covering the most important ideas
- **Practical Takeaways**: Actionable insights for engineering teams
- **Notable Quotes**: Direct quotes from the source (only if clearly present in the content)
- **Related Sources**: Cross-references to other sources in the repo (by ID and filename)
- **Related Curriculum**: Which curriculum modules this source informs

### Step 6: Assign tags and curriculum modules

Using the reference material:
- Assign 2-5 tags from the established taxonomy (or create new ones if needed)
- Map to 1-3 curriculum modules based on content alignment

### Step 7: Write the source file

Write the file to `sources/{ID}-{creator-slug}-{topic-slug}.md` where:
- `{ID}` is the 3-digit zero-padded source ID
- `{creator-slug}` is the creator's name, lowercased and hyphenated
- `{topic-slug}` is a brief topic descriptor, lowercased and hyphenated

### Step 8: Update the sources index

Edit `sources/README.md` to add a new row to the index table with the source's ID, title, creator, type, and tags.

## Output

The path to the newly created source file.
