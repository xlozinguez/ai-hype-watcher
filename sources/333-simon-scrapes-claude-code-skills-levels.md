---
source_id: "333"
title: "Every Level of Claude Code Skills in 27 mins"
creator: "Simon Scrapes"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=-u_igSQHAIo"
date: "2026-03-19"
duration: "27:10"
type: "video"
tags: ["skills", "claude-code", "context-engineering", "validation", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 333: Every Level of Claude Code Skills in 27 mins

> **Creator**: Simon Scrapes | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 27:10

## Summary

Simon Scrapes walks through seven levels of Claude Code skill building, from basic installation through self-improving skill systems that coordinate as a unified AI workforce. The video emphasizes that a skill is fundamentally a folder of knowledge, not just a prompt, and that the relationship between files within that folder determines skill effectiveness. The key technical principle throughout is progressive disclosure -- a three-tier system where Claude loads information only when needed to preserve context window capacity.

The most actionable insight is the 200-line rule for skill.md files: keeping the main skill file under 200 lines and extracting detailed documentation into references folders that Claude loads and unloads on demand. This directly addresses the most common failure mode where developers dump thousands of lines into a single skill.md, bloating the context window and degrading performance. The video also covers Anthropic's built-in evaluation and benchmarking system for skills, feedback loops via learnings files, and inter-skill coordination for complete workflow automation.

## Key Concepts

### Progressive Disclosure (Three-Tier Loading)

Claude Code skills use a three-tier information loading system. Tier 1: YAML frontmatter (always loaded, limited to 15,000 characters across all skills) which includes the skill name, description, trigger words, and negative triggers. Tier 2: the body of skill.md (loaded only when the skill activates). Tier 3: references, scripts, and assets (loaded only when specific steps require them). This means Claude is not loading everything at once but being selective about what information it brings in and when, preserving context window capacity.

### The 200-Line Rule

The golden rule of skill building is keeping skill.md under 200 lines maximum. This limit is based on how much context an LLM can efficiently scan to decide what to load next. The skill.md functions as a table of contents pointing to reference files; detailed documentation goes into the references folder. A real example showed a 400-line skill.md being refactored to 148 lines (60% reduction) by extracting content into four new reference files, with Claude loading and unloading them per step.

### Skill Trigger Engineering

Skill activation rates average around 20% for marketplace skills, meaning four out of five times a downloaded skill won't trigger when relevant. The fix is a three-part description: (1) trigger conditions and keywords, (2) explicit negative triggers (what should NOT activate the skill), and (3) the outcome the skill produces. This dramatically improves activation reliability.

### Evaluation and A/B Testing

Anthropic's skill creator skill includes built-in evaluation capabilities that replace vibes-based quality assessment. Users define specific criteria (3-5 assertions per test), run the skill 5-10 times in parallel, and get structured pass/fail reports. A/B testing allows comparing skill performance with and without specific reference files, revealing which files actually improve output quality and which just cost tokens without benefit.

### Self-Improving Skills via Feedback Loops

Level 6 introduces learnings files that capture observations from every skill interaction. A wrap-up skill runs at the end of each session, generating feedback entries on a skill-by-skill basis. Rules and learnings are always read when the skill.md loads, creating a system where skills accumulate knowledge over time and improve without manual intervention. The key constraint is pruning: learnings files must be kept structured and trimmed weekly to avoid becoming their own context window problem.

### Inter-Skill Coordination

Level 7 connects skills into workflows. A copywriting skill can invoke a humanizer skill as a gate before saving output. A content repurposing skill can call a transcript extraction skill when YouTube transcripts are unavailable. Skills share context through a shared brand context folder containing positioning, ICP, voice profiles, and content pillars, ensuring all skills produce consistent, business-specific output rather than generic AI content.

## Practical Takeaways

- **Keep skill.md under 200 lines**: Extract detailed documentation into references folders; the skill.md should be a table of contents, not an encyclopedia
- **Install no more skills than 15,000 characters of frontmatter allows**: Too many skills bloat the always-loaded Tier 1 context
- **Use three-part trigger descriptions**: Include trigger keywords, negative triggers, and expected output to push activation rates well above the 20% marketplace average
- **A/B test reference files**: Use Anthropic's eval system to determine which reference files actually improve quality vs. which just consume tokens
- **Build a shared brand context folder**: Positioning, ICP, voice profiles, and content pillars shared across all skills prevent generic output
- **Prune learnings files weekly**: Self-improving feedback loops are powerful but create their own context bloat if not maintained
- **Use the skill creator skill to refactor marketplace skills**: Most downloaded skills are poorly structured; refactoring a 1,000-line skill.md into a proper progressive-disclosure structure is straightforward

## Notable Quotes

> "A skill is just a folder of knowledge. That's it. But it's how you build the files inside of the folder and the relationship between those files that actually determines how successful your skills are." — Simon Scrapes

> "The golden rule of skill building: keep your skill.md under 200 lines max." — Simon Scrapes

> "A skill without your business context is basically not worth having at all." — Simon Scrapes

> "That's not an AI tool. That is an AI workforce." — Simon Scrapes

## Related Sources

- [283: Income Stream Surfers - Loops, Skills, Memory](283-income-stream-surfers-loops-skills-memory.md) — Skills architecture patterns
- [260: Chase AI - Six Levels Claude Code](260-chase-ai-six-levels-claude-code.md) — Claude Code proficiency levels

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills architecture, progressive disclosure, CLAUDE.md integration
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Self-improving systems, inter-skill coordination, evaluation loops
