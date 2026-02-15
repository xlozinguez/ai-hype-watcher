---
source_id: "062"
title: "Every Level of Claude Code Explained in 39 Minutes"
creator: "Simon Scrapes"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Y09u_S3w2c8"
date: "2026-02-07"
duration: "39:22"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "mcp", "agentic-coding", "multi-agent", "agent-teams", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 062: Every Level of Claude Code Explained in 39 Minutes

> **Creator**: Simon Scrapes | **Platform**: YouTube | **Date**: 2026-02-07 | **Duration**: 39:22

## Summary

Simon Scrapes presents a structured progression through seven levels of Claude Code mastery, from basic prompting with intent all the way to fully autonomous pipelines. Drawing from 150+ hours of hands-on usage and studying resources from Claude Code creator Boris Cherny, he walks through each level using a practical running example: building a social media content creation system.

The video is particularly valuable as a comprehensive map of the Claude Code capability surface. Rather than focusing on any single feature, it shows how plan mode, CLAUDE.md, slash commands, skills, hooks, MCP servers, sub-agents, and autonomous loop frameworks (GSD and RAWL) layer on top of each other progressively. The key insight is that most users plateau at level two or three, never reaching the agent orchestration and automation tiers that unlock the real leverage.

The framing is pragmatic rather than hype-driven. Simon repeatedly emphasizes planning before execution, keeping CLAUDE.md lean, and understanding when to use each tool (skills for context-rich thinking, hooks for mechanical checks, commands for manual triggers). The video serves as a solid reference architecture for anyone building out their Claude Code workflow incrementally.

## Key Concepts

### The Seven Levels of Claude Code

Simon organizes Claude Code proficiency into a clear progression:

1. **Prompting with Intent** — Using plan mode (Shift+Tab) before execution; iterating on plans before touching code
2. **CLAUDE.md Personalization** — Setting up project rules, brand voice, and guardrails via the CLAUDE.md file
3. **Slash Commands, Skills, and Hooks** — Reusable prompts (commands), context-rich background knowledge (skills), and automatic post-action triggers (hooks)
4. **MCP Connections** — Bridging Claude Code to external apps (Air Table, Notion, etc.) via Model Context Protocol servers
5. **Planning Frameworks (GSD)** — Using structured planning frameworks that break large projects into phases with plan-execute-verify loops and persistent state files to combat context rot
6. **Agent Teams** — Running sub-agents for specialized tasks (researcher, writer, reviewer) either sequentially in one terminal or in parallel across multiple terminals
7. **Fully Autonomous Pipelines** — Using loop frameworks like RAWL that run Claude autonomously against a PRD with acceptance criteria, iterating through fresh context windows until completion

### Context Rot and Mitigation

A critical concept Simon surfaces is "context rot" — as the context window fills up (approaching 95% capacity), Claude auto-compresses context into summaries, degrading output reliability. At around 10,000 tokens (~7,500 words), approximately 50% of context fidelity is lost. The GSD framework mitigates this by keeping context in individual phase-level files rather than one massive conversation, and the RAWL loop addresses it by feeding state back into fresh context windows after each completed task.

### The Skills-Commands-Hooks Mental Model

Simon offers a clean mental model for the three main automation primitives:
- **Skills** = how Claude *thinks* (background context loaded automatically when relevant)
- **Hooks** = what happens *automatically after* Claude acts (mechanical checks requiring no LLM tokens)
- **Commands** = what you *manually trigger* (saved prompts with dynamic arguments)

### The "Don't Dump" Principle for CLAUDE.md

A recurring theme is keeping CLAUDE.md lean — under 30 instructions, readable in 60 seconds. Instead of dumping all context into CLAUDE.md, reference external files and folders (brand voice docs, style guides, examples). The CLAUDE.md should tell Claude *where to find* details, not contain them all. Boris Cherny's team version-controls their shared CLAUDE.md on Git and tags it to track changes.

## Practical Takeaways

- **Always start in plan mode**: Use Shift+Tab to enter plan mode before execution. Iterate with Claude's "ask user questions" tool until the plan is solid, then switch to auto-accept mode for one-shot execution.
- **Keep CLAUDE.md lean with external references**: Aim for under 30 instructions readable in 60 seconds. Use file references (e.g., "see docs/brand-voice.md") for detailed context rather than inlining everything.
- **Use hooks for mechanical validation, not LLM-dependent tasks**: Banned word checks, word count limits, and formatting rules should be hooks (zero token cost), not prompt instructions that Claude might forget.
- **Run /init on existing projects**: Claude Code can generate a starter CLAUDE.md by scanning your repository, which you then refine and trim.
- **Set max iterations on autonomous loops**: When using RAWL or similar autonomous frameworks, always set a max iteration count to prevent runaway token spend on large projects.
- **Match the framework to the task scope**: Use RAWL for well-defined execution tasks (clear acceptance criteria). Use GSD for larger projects that need planning first (unclear scope that needs phase decomposition).
- **Curate skills selectively**: Rather than importing entire skill libraries, pull in specific skills you understand and can audit — this prevents unintended context blending.

## Notable Quotes

> "The difference between somebody who's a beginner with Claude Code and someone who's going to get real results is one single habit — planning before building." — Simon Scrapes

> "Keep it short, keep it specific, and only include what Claude can't figure out for itself." — Simon Scrapes, on CLAUDE.md

> "Skills is how Claude thinks. Hooks are what happens automatically after Claude Code acts. And commands are stuff that we want to trigger manually." — Simon Scrapes

> "Boris himself runs five Claudes in parallel in his terminal... but he also runs 5 to 10 Claudes on claude.ai/code as well in parallel with the local." — Simon Scrapes, on Boris Cherny's workflow

## Related Sources

- [051: You're using Claude Code Wrong - These 10 Tips Will Change Everything](051-simon-scrapes-claude-code-tips.md) — Simon's earlier Claude Code tips video; this levels video expands that into a structured progression
- [020: How & When to Use Claude Code Agent Teams in 13 Mins](020-simon-scrapes-agent-teams.md) — Simon's focused breakdown of agent teams, which corresponds to level six here
- [001: Claude Code Task System: ANTI-HYPE Agentic Coding](001-indydevdan-claude-code-task-system.md) — IndyDevDan's deep-dive on the task system and builder-validator patterns that align with levels 5-7
- [013: Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) — Leon van Zyl's skills-focused video complementing level three here
- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) — IndyDevDan's skills engineering approach, relevant to the skills portion of level three
- [040: Stop Feeding Claude Your Entire CLAUDE.md](040-charlie-automates-claudemd-context.md) — Charlie Automates' CLAUDE.md optimization aligns with the "don't dump" principle at level two
- [024: You are Not Ready: Agentic coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) — Broader agentic coding overview covering similar terrain from a different angle

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Levels 1-3 (plan mode, CLAUDE.md, commands, skills, hooks) map directly to this module
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Levels 5-6 (GSD framework, sub-agents, context isolation) inform agentic pattern discussions
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Levels 6-7 (agent teams, parallel terminals, RAWL autonomous loops) are core team orchestration content
