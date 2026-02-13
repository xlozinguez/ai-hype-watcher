# PR Description

Generate a pull request description that summarizes new knowledge introduced by source notes, curriculum updates, and synthesis docs.

## Input

- A branch name or PR number to describe
- Or: run after committing to auto-detect changes

## Workflow

### Step 1: Identify new sources

Check `git diff` against the base branch (usually `main`) for new source note files in `sources/`. Read the Summary section of each new source note.

### Step 2: Identify other changes

Check for modifications to:
- `curriculum/` modules — note which modules were updated
- `briefings/` — note new headlines added
- `synthesis/` — note new synthesis docs created
- `sources/README.md` — confirm index updated

### Step 3: Write the PR description

Use this structure:

```markdown
## Summary

One sentence: what was ingested and what was updated.

## New findings

For each new source (or cluster of related sources), write a **bolded one-line thesis** followed by 2-3 sentences of supporting detail. Focus on:
- What's genuinely new knowledge (not just "video was ingested")
- Concrete data points, quotes, or claims that matter
- How the source challenges or reinforces existing curriculum themes

Keep each finding to a short paragraph. Don't summarize every source — cluster related ones and highlight what's most interesting.

## Sources

| ID | Title | Creator | Key theme |
|----|-------|---------|-----------|
| NNN | Title | Creator | 3-5 word theme |

## Files changed

Bullet list of categories:
- N new source notes (NNN-NNN) with timestamped quotes
- N VTT + raw transcript drafts
- New synthesis: "Title"
- Curriculum modules NN-NN updated
- Daily briefing updated with N headlines, N detail sections
- Indexes updated

## Test plan

- [ ] Source notes render with valid YAML frontmatter
- [ ] Curriculum modules maintain existing content integrity
- [ ] Cross-references link to valid files
- [ ] Timestamp links point to correct video moments

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

### Step 4: Apply the description

If a PR number is provided, update the PR body using:
```
gh api repos/OWNER/REPO/pulls/NUMBER -X PATCH -f body="BODY"
```

If no PR number, output the description for the user to copy.

## Style guidelines

- **New findings is the core section** — this is what makes someone want to read the PR
- Write findings as insights, not summaries ("Agent team demos are marketing, not engineering" > "Source 041 critiques Anthropic's compiler experiment")
- Include concrete numbers when available ($20K, 15-20% context, 733 lines)
- Bold the thesis statement of each finding
- Keep the whole description scannable — someone should get the key points in 30 seconds
- Don't pad with generic statements about "updating curriculum" — the Files Changed section covers logistics
