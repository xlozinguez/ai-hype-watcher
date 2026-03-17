---
source_id: "291"
title: "10 Claude Code Plugins to 10X Your Projects"
creator: "Chase AI"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=OFyECKgWXo8"
date: "2026-03-09"
duration: "17:47"
type: "video"
tags: ["claude-code", "mcp", "skills", "agentic-coding", "context-engineering", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 291: 10 Claude Code Plugins to 10X Your Projects

> **Creator**: Chase AI | **Platform**: YouTube | **Date**: 2026-03-09 | **Duration**: 17:47

# 10 Claude Code Plugins to 10X Your Projects

## Summary

Chase AI walks through 10 tools that augment Claude Code workflows, ranging from CLI integrations and MCPs to frameworks and personal productivity tools. The video's central thesis is practical and opinionated: CLI tools are almost always superior to their MCP equivalents because they are purpose-built for terminal-native AI agents like Claude Code, and the two should not be treated as interchangeable. The presenter uses the Supabase MCP-vs-CLI comparison as the anchor example to make this point concrete, admitting he himself had been using the inferior MCP version until recently.

Beyond the CLI-vs-MCP argument, the video introduces tools covering the full development lifecycle: database/auth (Supabase), spec-driven project scaffolding (GSD framework), research automation (NotebookLM CLI), browser automation (Playwright), deployment management (Vercel CLI), and personal knowledge management (Obsidian). Each tool is paired with the recommendation to install a corresponding Claude Code **skill** so the agent knows how to use the new CLI effectively. The skill creator tool from Anthropic is highlighted as the most powerful addition, enabling AB-tested, measurable skill creation and iteration rather than guesswork.

The video is aimed at practitioners already using Claude Code who want to expand their toolchain deliberately rather than chase every new release. The framing throughout is "tools I actually use" with explicit install commands, use cases, and workflow integration tips for each.

---

## Key Concepts

### CLI > MCP as a General Principle

MCPs (Model Context Protocol, introduced by Anthropic in 2024) were designed to connect AI assistants to external data systems. However, because Claude Code lives natively in the terminal, CLI tools accomplish the same integration with less overhead and are purpose-built for agentic use. The presenter argues: *if a CLI and an MCP version of the same tool both exist, always prefer the CLI.* He uses the Supabase example — where he himself defaulted to the MCP despite knowing CLIs are generally better — to illustrate how easy it is to miss the superior option even when deeply embedded in the ecosystem.

### Pairing CLI Tools with Skills

Installing a CLI tool alone is insufficient; Claude Code needs to know *how* to use it appropriately. The recommended pattern is: install CLI → locate the tool's purpose-built Claude Code skill (usually on their GitHub or docs) → install the skill. This is demonstrated for Supabase, NotebookLM, and Vercel. Skills function as text-based prompt files that encode tool-specific conventions and command patterns for the agent.

### The Skill Creator Skill (Anthropic)

Anthropic released a first-party skill whose purpose is creating, modifying, and evaluating other skills. The key differentiator is **measurability**: previously, skill quality was assessed by gut feel. The skill creator enables AB testing — comparing a new skill version against the previous one with actual performance data. This transforms skill development from intuition-driven to data-driven iteration, which the presenter identifies as a significant step change in Claude Code capability management.

### GSD (Get Shit Done) Framework for Spec-Driven Development

GSD is an orchestration layer on top of Claude Code that enforces spec-driven, phase-by-phase project creation. It addresses two common failure modes: under-specified requirements (by running an intensive planning mode before any code is written) and context rot (by ensuring each execution phase uses a fresh context window via sub-agents). It is positioned as the right tool when starting a greenfield project that requires disciplined, structured decomposition.

### Context Window Management via Sub-Agents

Both the GSD framework and the general multi-agent pattern discussed in the video reflect a recurring principle: deliberately managing context window usage by isolating work into fresh sub-agent sessions. Rather than allowing a single long-running context to degrade output quality as it fills, the preferred pattern is segmenting tasks so each phase starts clean. This is treated as a core discipline for maintaining quality in longer, more complex builds.

---

## Practical Takeaways

- **Default to CLIs over MCPs** whenever both options exist for the same integration — CLIs have less overhead and are better suited to terminal-native agentic workflows like Claude Code.
- **Always pair a new CLI installation with its corresponding skill** — check the tool's GitHub or docs for a pre-built Claude Code skill; this is what actually teaches the agent to use the tool correctly.
- **Use the Skill Creator skill for any serious skill development** — the AB-testing and eval capabilities remove guesswork and let you measure whether a skill change actually improves outputs before committing to it.
- **Use GSD for greenfield projects** that benefit from heavy upfront planning and context-isolated execution phases; it is not a general-purpose upgrade but excels in structured, multi-phase builds.
- **Scope tool choices to their appropriate context** — Obsidian integration, for example, is valuable in personal assistant/knowledge management workflows but adds little value in typical coding projects.

---

## Notable Quotes

> "All things being equal, if you are looking at something and there's a CLI and there's an MCP version, go with the CLI. It's essentially purpose-built for AI coding agents like Claude Code."

> "Before this skill, it was kind of just random, right? Did we know the skill was actually making things better? Maybe. But did you have any actual data? Well... you now do. I can do AB tests with the skill, without the skill."

> "If you feel like you're overwhelmed, I promise you're okay. [Even] someone who is very deep in the space... I struggle to keep up with these tools even when it comes to tools I use consistently."

---
