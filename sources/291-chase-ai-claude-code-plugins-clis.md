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

Chase AI walks through his top 10 Claude Code plugins, CLIs, and skills — tools he personally uses and considers genuine productivity multipliers. The video is organized around four dimensions for each tool: why it matters, how to use it, how to install it, and a real use case. Tools span database management, research workflows, browser automation, deployments, and project orchestration.

A central thesis of the video is that **CLIs are almost always preferable to MCPs** when both options exist. Claude Code lives in the terminal, so CLI tools are purpose-built for it — MCPs add unnecessary overhead by trying to replicate what a CLI already does natively. Chase uses his own story of belatedly discovering the Supabase CLI (despite being a heavy Supabase MCP user) as an honest illustration of how hard it is to keep up with the ecosystem even for specialists.

The 10 tools covered (in order) are: Supabase CLI, the Anthropic Skill Creator skill, GSD (Get Stuff Done) framework, NotebookLM CLI/skill, Obsidian, Vercel CLI, and Playwright CLI — with the remaining tools cut off in the available transcript. Throughout, the video emphasizes pairing each new CLI tool with an appropriate skill so Claude Code knows how to use it correctly.

## Key Concepts

### CLI-First Over MCP
When a tool offers both a CLI and an MCP interface, the CLI is almost always the better choice for Claude Code. MCPs were introduced in 2024 as a standard for connecting AI assistants to external systems, but since Claude Code operates inside the terminal, CLI tools are natively accessible without the extra abstraction layer. MCPs add overhead and were largely designed for contexts where the AI wasn't terminal-native. Default to CLIs; use MCPs only when no CLI alternative exists.

### Pairing CLI Tools with Skills
Installing a CLI tool is only half the job. Claude Code needs explicit instruction on *how* to use that CLI in the intended way — this is what skills provide. Whenever you add a new CLI to your stack, check the tool's GitHub or documentation for purpose-built Claude Code skills. Tools like Supabase, Vercel, and NotebookLM already ship official skills. This pairing pattern (CLI + skill) is the repeatable unit of extending Claude Code's capabilities.

### Skill Creator for Measurable Skill Improvement
Anthropic's skill creator skill allows users to not just create new skills but to evaluate and iterate on existing ones with actual performance data. This replaces gut-feel skill tuning with A/B testing — comparing a skill's output with and without it, or comparing current vs. previous skill versions. The ability to measure skill performance is a significant shift from the earlier "hope the skill is working" dynamic.

### Spec-Driven Orchestration with GSD Framework
The GSD (Get Stuff Done) framework is an orchestration layer on top of Claude Code designed for building new projects from scratch. It enforces spec-driven development by heavily front-loading the planning phase and manages context rot by executing each phase in a fresh context window using sub-agents. This addresses two common failure modes in agentic coding: underspecified projects and degraded output quality from context window exhaustion.

### Connecting External Tools for Research Workflows
The NotebookLM CLI/skill pairing demonstrates a broader pattern: wrapping tools that have no official API with a CLI interface and a skill, then routing work to them from Claude Code via natural language. NotebookLM's research, analysis, and content creation capabilities (podcasts, flashcards, slide decks) become accessible through the terminal for free, despite no official API existing. This pattern — unofficial CLI + skill = terminal-accessible capability — is likely to generalize to other tools.

## Practical Takeaways

- **Audit your current MCP usage**: If you're using an MCP for a tool that also has a CLI (e.g., Supabase), switch to the CLI. The overhead isn't worth it and Claude Code will handle CLI tools more reliably.
- **Always check for an official skill when installing a new CLI**: Supabase, Vercel, and NotebookLM all ship ready-made Claude Code skills. Using official skills is faster and more reliable than writing your own from scratch.
- **Use GSD for greenfield projects**: If starting a new project from scratch, GSD's enforced planning phase and sub-agent context management will produce more consistent results than ad-hoc prompting.
- **Use the Skill Creator to validate skill performance**: Don't assume a skill is working — use the skill creator's evaluation tooling to A/B test skills and measure actual output improvement before committing to them.
- **Obsidian integration is context-specific**: The Supabase/Vercel/NotebookLM integrations are broadly useful, but Obsidian + Claude Code only adds real value in personal assistant contexts with large, growing markdown-based knowledge stores — not typical coding projects.

## Notable Quotes

> "All things being equal, if you are looking at something and there's a CLI and there's an MCP version, go with the CLI. It's essentially purpose-built for AI coding agents like Claude Code."

> "Before this skill, it was kind of just random, right? Did we know the skill was actually making things better? Maybe. But did you have any actual data? Well, if we look at stuff like this, we now do."

> "Me, who again this is like my profession, didn't even realize [the Supabase CLI] existed. So if you feel like you're overwhelmed, I promise you're okay."
