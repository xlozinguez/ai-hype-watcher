---
source_id: "051"
title: "You're using Claude Code Wrong - These 10 Tips Will Change Everything"
creator: "Simon Scrapes | AI Automation"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=V9atNrDjnZs"
date: "2026-02-13"
duration: "20:27"
type: "video"
tags: ["claude-code", "agent-teams", "skills", "context-engineering", "skills-ecosystem", "validation"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 051: You're using Claude Code Wrong - These 10 Tips Will Change Everything

> **Creator**: Simon Scrapes | AI Automation | **Platform**: YouTube | **Date**: 2026-02-13 | **Duration**: 20:27

## Summary

Simon Scrapes presents ten Claude Code techniques organized as a progressive stack, where each tip builds on the previous ones to create compounding returns. Unlike isolated trick compilations, the video emphasizes how agent teams, skills, hooks, slash commands, plugins, and CLAUDE.md discipline form an interconnected system. The framing is explicitly non-developer: the content creation pipeline (LinkedIn posts, blog articles, newsletters) serves as the running example throughout, making this one of the clearer introductions to Claude Code's extensibility model for non-engineering audiences.

The video's strongest contribution is a practical mental model for distinguishing four commonly confused Claude Code concepts: slash commands (user-triggered actions), skills (auto-invoked context bundles), hooks (zero-LLM programmatic checks), and plugins (distributable packages of all three). It also covers research workarounds using Gemini CLI as a fallback for sites Claude cannot access, the "last 30 days" community skill for trend research, and practical output formatting techniques like clipboard-native LinkedIn formatting. The fact-checking tip at the end introduces lightweight verification discipline into content workflows.

## Key Concepts

### The Claude Code Extensibility Stack: Commands, Skills, Hooks, Plugins

The video provides a clear disambiguation of four concepts that users frequently conflate. **Slash commands** are single-file markdown triggers in `.claude/commands/` that execute when the user explicitly invokes them (e.g., `/linkedin-post`). **Skills** are richer context bundles in `.claude/skills/` with a `SKILL.md` descriptor; Claude reads the description and auto-invokes the skill when contextually relevant, without explicit user activation. **Hooks** are purely programmatic (zero LLM tokens) and run deterministic checks at defined lifecycle points, such as scanning output drafts for banned words. **Plugins** are the distribution layer: a packaged collection of commands, skills, hooks, and agents that can be installed from a marketplace in two commands. ([4:33](https://www.youtube.com/watch?v=V9atNrDjnZs&t=273))

### CLAUDE.md Discipline: Point, Don't Dump

Most users overload their CLAUDE.md file with entire brand guides, audience research, and example content. This wastes context window on every conversation. The recommended approach is to keep CLAUDE.md lean (20-30 lines) and use it as a pointer to skills and reference files that Claude loads on demand. This preserves a clean, scannable root configuration while keeping detailed context available when needed without eating into the token budget of every session. ([7:04](https://www.youtube.com/watch?v=V9atNrDjnZs&t=424))

### Agent Teams vs. Sub-Agents: A Graduation Model

Agent teams extend the sub-agent pattern by adding a shared task list and peer-to-peer communication between teammates. In the sub-agent (hub-and-spoke) model, all communication flows through the main agent, creating a bottleneck. Agent teams allow teammates to coordinate directly, making them essential for complex projects where multiple agents have interdependencies (e.g., API, frontend, and testing agents in a Next.js app). However, the additional token cost makes them overkill for simple delegation tasks. The recommended progression: start with single agents, graduate to sub-agents, then reach for agent teams only when genuine cross-collaboration is required. ([0:31](https://www.youtube.com/watch?v=V9atNrDjnZs&t=31))

### Research Workarounds: Gemini CLI and Community Skills

Claude Code cannot fetch from many sites (Reddit, paywalled content, some social platforms). A workaround credited to YK (ykdojo) installs the Gemini CLI as a fallback research tool. A custom skill instructs Claude to route blocked-site requests through Gemini's broader web access. Additionally, the community-built "last 30 days" skill (by mvanhorn on GitHub) scans Reddit and X for discussions within a 30-day window, synthesizes patterns, and generates ready-to-use prompts. The demo showed it producing structured research on nano banana prompting techniques, Claude Code news, and trending YouTube content in under three minutes per query. ([10:05](https://www.youtube.com/watch?v=V9atNrDjnZs&t=605))

### Fact-Checking as Workflow Discipline

Asking Claude to "double check every claim and statistic and make a table of what you could and couldn't verify, including the source" produces a verification matrix that catches hallucinated statistics before publication. In the demo, 3 of 8 claims in generated LinkedIn posts were flagged as unverifiable, with Claude recommending removal or softening of specific claims. This transforms fact-checking from an afterthought into a systematic final step in content workflows. ([18:46](https://www.youtube.com/watch?v=V9atNrDjnZs&t=1126))

## Practical Takeaways

- **Distinguish the four extension types**: Slash commands = user-triggered single-file actions. Skills = auto-invoked context bundles with descriptions. Hooks = zero-token programmatic checks. Plugins = distributable packages of all three. Understanding when to use each avoids overengineering simple workflows.

- **Keep CLAUDE.md under 30 lines**: Use it as an index that points to skills and reference files rather than dumping full brand guides, audience personas, or example content directly into it. Every line in CLAUDE.md costs tokens on every conversation.

- **Install Gemini CLI as a research fallback**: When Claude cannot access Reddit, X, or paywalled sites, route requests through a Gemini CLI skill to leverage its broader web access. Add a skill that detects blocked-site requests and delegates to Gemini automatically.

- **Use the clipboard for cross-platform formatting**: Tell Claude to copy output directly to clipboard in platform-native format (e.g., LinkedIn-native with emoji bullets, no markdown headers) to avoid formatting loss when pasting between applications.

- **Add a fact-check step to content workflows**: After generating content with claims or statistics, prompt Claude to verify each claim, produce a source table, and flag unverifiable assertions. This catches hallucinated statistics before publication.

- **Recover conversation context across sessions**: Use Claude Code's project history to search and resume previous conversations. Ask "what have we spoken about in the last week across all projects?" to restore context from closed sessions.

## Notable Quotes

> "Most tutorials show isolated tricks, and what they don't show you is how those techniques can compound when used together." — Simon Scrapes ([0:00](https://www.youtube.com/watch?v=V9atNrDjnZs&t=0))

> "Keep CLAUDE.md lean and point to where the detail lives. Don't dump the detail itself." — Simon Scrapes ([7:04](https://www.youtube.com/watch?v=V9atNrDjnZs&t=424))

> "Don't start with agent teams. Start simple. Graduate to sub agents and then when you reach the point where the complexity and the collaboration is necessary, then reach for agent teams." — Simon Scrapes ([4:33](https://www.youtube.com/watch?v=V9atNrDjnZs&t=273))

> "Hooks don't require any LLM tokens at all and it's for stuff that can be done programmatically without the need for AI." — Simon Scrapes ([6:34](https://www.youtube.com/watch?v=V9atNrDjnZs&t=394))

## Related Sources

- [020: Simon Scrapes - How & When to Use Claude Code Agent Teams](020-simon-scrapes-agent-teams.md) — Same creator's dedicated deep-dive on agent teams with complexity ranking system
- [013: Leon van Zyl - Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) — Comprehensive skills system tutorial with hands-on installation and custom skill building
- [015: IndyDevDan - I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) — Engineering-level analysis of skills architecture, lazy-loading, and SKILL.md frontmatter
- [017: ThePrimeagen - Skills Security](017-primeagen-skills-security.md) — Security implications of the skills ecosystem and supply chain risks

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md discipline, skills system, context management
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Hooks, slash commands, sub-agent patterns
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Agent teams, shared task lists, cross-agent collaboration
