---
source_id: "291"
title: "10 Claude Code Plugins to 10X Your Projects"
creator: "Chase AI"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=OFyECKgWXo8"
date: "2026-03-09"
duration: "17:47"
type: "video"
tags: ["claude-code", "mcp", "skills", "agentic-coding", "skills-ecosystem", "context-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 291: 10 Claude Code Plugins to 10X Your Projects

> **Creator**: Chase AI | **Platform**: YouTube | **Date**: 2026-03-09 | **Duration**: 17:47

# 10 Claude Code Plugins to 10X Your Projects

## Summary

Chase AI walks through 10 tools — CLIs, MCPs, skills, and frameworks — that he actively uses to extend Claude Code's capabilities. The video is structured around four dimensions for each tool: why it matters, how to use it, how to install it, and a concrete use case. Tools covered include Supabase CLI, the Anthropic skill creator skill, the GSD framework, NotebookLM CLI, Obsidian, Vercel CLI, and Playwright, among others.

A core thesis runs through the entire video: **CLIs are almost always preferable to MCPs**. Because Claude Code lives in the terminal, CLI tools are purpose-built for the agent context, while MCPs introduce unnecessary overhead by replicating what CLIs already do. The creator uses his own experience defaulting to the Supabase MCP — despite knowing better — as a candid illustration of how hard it is to keep pace with the ecosystem even for practitioners deeply embedded in it.

The video also emphasizes pairing every new CLI tool with an appropriate **skill** that teaches Claude Code how to use it correctly. Several covered tools (Supabase, NotebookLM, Vercel) ship their own official skills, making adoption straightforward. The overall message is that productivity gains come from deliberately layering the right CLI tools, skills, and frameworks rather than chasing every new release.

## Key Concepts

### CLI Tools vs. MCPs
MCPs were introduced by Anthropic in 2024 as a standard for connecting AI assistants to external systems. However, because Claude Code operates natively in the terminal, CLI tools accomplish the same integration without the additional overhead of the MCP abstraction layer. The guiding rule: if a CLI and an MCP version of a tool both exist, always prefer the CLI. It's purpose-built for agent workflows and more reliable in practice.

### Skills as the Complement to CLIs
Installing a CLI is only half the job. Claude Code also needs to know *how* to use that CLI correctly — which commands to invoke, in what order, with what flags. This is where skills come in. Many major tools (Supabase, Vercel, NotebookLM) now ship official Claude Code skills on their GitHub or documentation sites. The best practice is: install the CLI, then immediately find and install the matching skill.

### Skill Creator Skill (Anthropic)
Anthropic's skill creator skill allows users to create new skills, modify and improve existing ones, and — critically — **measure skill performance via A/B testing**. Before this, skill quality was assessed by gut feeling. Now practitioners can run controlled comparisons (skill vs. no skill, old version vs. new version) with actual performance data. This makes iterative skill improvement a rigorous, data-driven process rather than guesswork.

### GSD (Get Shit Done) Framework
GSD is an orchestration layer that sits on top of Claude Code and changes how it behaves for greenfield project creation. It enforces spec-driven development — breaking work into phases and features — and actively manages context rot by executing each plan segment in a fresh context window with sub-agents. It's positioned as "plan mode on steroids," forcing thorough upfront planning before any code is written.

### NotebookLM CLI Integration
Despite there being no official NotebookLM API, the NotebookLM-CLI tool allows Claude Code to interact with NotebookLM entirely from the terminal. This means research workflows, document analysis, and deliverable generation (slide decks, podcasts, flashcards, infographics) can be orchestrated directly through Claude Code — effectively offloading these tasks to NotebookLM for free. An official skill ships with the CLI to teach Claude Code the correct commands.

## Practical Takeaways

- **Default to CLIs over MCPs** when both exist for a tool. MCPs add overhead and are largely redundant for terminal-native agents like Claude Code.
- **Pair every new CLI with its official skill** — check the tool's GitHub or docs for a pre-built Claude Code skill before writing your own. Supabase, Vercel, and NotebookLM all ship official skills.
- **Use the Anthropic skill creator skill to A/B test your skills** rather than relying on gut feel. Measure whether a new or modified skill actually improves outputs before committing to it.
- **Use GSD for greenfield projects** where you want enforced spec-driven development and automatic context window hygiene via sub-agents.
- **Obsidian integration is context-dependent** — it adds genuine value in personal assistant / knowledge management workflows with large collections of markdown files, but is not a general-purpose coding productivity tool.

## Notable Quotes

> "All things being equal, if you are looking at something and there's a CLI and there's an MCP version, go with the CLI. It's essentially purpose-built for AI coding agents like Claude Code."

> "Before this skill, it was kind of just random, right? Did we know the skill was actually making things better? Maybe. But did you have any actual data? Well... we now do. I can do AB tests with the skill, without the skill."

> "Even me, who again this is like my profession, didn't even realize [the Supabase CLI] existed... if you feel like you're overwhelmed, I promise you're okay."
