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

Chase AI surveys ten tools that extend Claude Code's capabilities, ranging from database integrations to browser automation frameworks. The video is structured around four dimensions for each tool: why it matters, how to use it, how to install it, and a concrete use case. The selection spans CLI tools, MCPs, skills, and orchestration frameworks, with an emphasis on tools the creator actively uses rather than theoretical recommendations.

A significant portion of the video is devoted to a CLI-versus-MCP argument triggered by the Supabase example. The creator admits he was using the Supabase MCP when the Supabase CLI was superior all along—using this as a teaching moment: CLI tools are purpose-built for terminal-resident AI agents like Claude Code and carry less overhead than MCPs, which were designed to bridge AI assistants to external systems before agents lived in the terminal. The general principle articulated is: when both a CLI and an MCP exist for the same service, always prefer the CLI.

The tools covered include Supabase CLI, Anthropic's skill creator skill, the GSD ("Get Sh*t Done") orchestration framework, the NotebookLM-PI CLI, Obsidian for personal assistant workflows, the Vercel CLI, and the Playwright CLI for browser automation. Each CLI-based tool is paired with the recommendation to install a corresponding skill so Claude Code knows how to use it idiomatically.

## Key Concepts

### CLI Tools Preferred Over MCPs for Agent Workflows

MCPs (Model Context Protocol) were Anthropic's 2024 standard for connecting AI assistants to external data systems. However, because Claude Code now operates natively in the terminal, CLI tools offer a more direct, lower-overhead path to the same integrations. The creator's rule of thumb: if a CLI and an MCP exist for the same service, use the CLI. The Supabase case illustrates this concretely—the Supabase CLI can do everything the MCP does, without the additional abstraction layer.

### Skills as Companions to CLI Tools

Installing a CLI tool is only half the integration. Claude Code also needs a skill (a purpose-built prompt) that teaches it how to use that CLI idiomatically. Most mature CLI tools (Supabase, Vercel, NotebookLM-PI) now ship official Claude Code skills in their documentation or GitHub repos. The pattern is: install the CLI dependency, then install the corresponding skill via the marketplace or a terminal command.

### Skill Creator Skill: Measurable Prompt Optimization

Anthropic's skill creator skill (available via `/plugin` in Claude Code) allows users to create, modify, and evaluate skills with actual performance data rather than gut feeling. It supports A/B testing—comparing a skill against no skill, or comparing two versions of a skill—providing empirical signal about whether a given skill is actually improving outputs. This shifts skill development from intuition-based to evidence-based iteration.

### GSD Framework: Spec-Driven Orchestration

The GSD (Get Sh*t Done) framework is an orchestration layer on top of Claude Code designed for building new projects from scratch. It enforces spec-driven development (extensive planning before execution), breaks work into phases and features, and manages context rot by ensuring each execution phase starts with a fresh context window via sub-agents. It is invoked via `/gsd new project` and kicks off an extended planning mode before any code is written.

### NotebookLM-PI: Unofficial API Integration via CLI

NotebookLM has no official API, but the NotebookLM-PI CLI tool enables Claude Code to drive NotebookLM from the terminal—performing research, analysis, and content generation (podcasts, slide decks, flashcards, infographics) through plain-language commands. This makes it a high-value, low-cost addition to research workflows within Claude Code, and it follows the same install-CLI-then-install-skill pattern.

## Practical Takeaways

- **Default to CLI over MCP**: When evaluating any new integration, check whether a CLI exists before reaching for an MCP. CLIs have less overhead and are architecturally better suited to terminal-based AI agents.
- **Always pair a new CLI with a skill**: After installing any CLI tool, search the tool's GitHub or docs for an official Claude Code skill. Installing the skill is what makes Claude Code use the CLI correctly and consistently.
- **Use the skill creator for evidence-based skill improvement**: Rather than guessing whether a skill is helping, use Anthropic's skill creator to run A/B evaluations and iterate on skill performance with data.
- **Apply GSD for greenfield projects**: If starting a new project from scratch, GSD's phase-by-phase, fresh-context-window approach reduces context rot and enforces enough upfront planning to avoid mid-build course corrections.
- **Match tools to use-case context**: Not every tool is universal. Obsidian integration, for example, adds value in personal assistant workflows with sprawling markdown context, but is largely irrelevant in standard coding projects.

## Notable Quotes

> "All things being equal, if you are looking at something and there's a CLI and there's an MCP version, go with the CLI. It's essentially purpose-built for AI coding agents like Claude Code."

> "Before this skill, it was kind of just random, right? Did we know the skill was actually making things better? Maybe. But did you have any actual data? … I can do AB tests with the skill, without the skill."

> "If you feel like you're overwhelmed, I promise you're okay. Even I struggle to keep up with these tools even when it comes to tools I use consistently."

---
