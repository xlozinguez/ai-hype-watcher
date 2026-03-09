---
source_id: "247"
title: "Google's New CLI Is The Missing Piece for Claude Code"
creator: "Better Stack"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=EKG9kX86u0s"
date: "2026-03-08"
duration: "08:31"
type: "video"
tags: ["claude-code", "skills", "mcp", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 247: Google's New CLI Is The Missing Piece for Claude Code

> **Creator**: Better Stack | **Platform**: YouTube | **Date**: 2026-03-08 | **Duration**: 08:31

## Summary

A hands-on walkthrough of Google's new Workspace CLI (GWS), a Rust-based command-line tool that lets AI agents interact with Google Workspace APIs -- reading Drive files, sending emails, creating Slides presentations, managing Calendar events, and more. The video demonstrates the tool working with Claude Code, showing it use minimal context compared to MCP-based approaches. The creator walks through the non-trivial Google Cloud Console setup process and then demonstrates progressively complex tasks: listing emails, drafting messages, creating slide presentations with images, generating spreadsheets, and scheduling calendar events.

The video positions this as part of a broader trend where companies are building CLIs alongside (or instead of) MCP servers for AI agent integration, following Playwright's similar move. It includes a balanced comparison of CLI vs. MCP trade-offs and highlights the agent-first design decisions that make the tool effective.

## Key Concepts

### CLI as Agent-First Interface Design

The GWS CLI was designed from the ground up for AI agents rather than humans. Key design decisions include: nested JSON output (harder for humans to read, easier for agents to parse), runtime-queryable documentation (the agent can discover available commands and parameters via `help` and `schema` subcommands), and field-level filtering to reduce token usage by returning only the data the agent needs. This represents a deliberate inversion of traditional CLI design philosophy.

### CLI vs. MCP Trade-offs

The video provides a balanced comparison. CLIs use fewer tokens (no tool definitions loaded into context), are portable across any agent harness, and make debugging easier since commands can be reproduced independently. MCP servers offer more natural function-calling semantics, better complex step chaining, and don't require a terminal. The GWS project supports both modes, suggesting the ecosystem is converging on offering both options rather than choosing one.

### Dynamic Schema Discovery

A standout feature is how Claude discovers the CLI's capabilities at runtime. When given a task, Claude runs `gws help` once, then navigates the command hierarchy to find the exact service, resource, and method needed. The `gws schema` command provides parameter definitions so the agent self-corrects when it uses wrong parameters. This pattern of self-documenting CLIs that agents can explore autonomously reduces the need for pre-loaded tool definitions.

### Skills as Complementary Guidance Layer

The project includes 100+ downloadable skills from Skillsh that provide agent-specific guidance beyond what the CLI's help system offers -- including helpers, personas, and recipes for complex multi-step actions like blocking focus time or rescheduling meetings. The presenter notes that the basic demos worked without installing any skills, but the skills add higher-level workflow intelligence.

## Practical Takeaways

- **GWS CLI enables Claude Code to control Google Workspace**: Read emails, create drafts, build presentations, manage spreadsheets, and schedule calendar events directly from Claude Code
- **Setup requires Google Cloud Console configuration**: Creating OAuth credentials, setting redirect URIs, and configuring audience access is the most time-consuming part
- **CLIs use significantly less context than MCP tools**: The email listing task used only 9% of context, and the slides creation used 15%, because no MCP tool definitions are loaded
- **Agent-first CLI design principles**: Prefer nested JSON over human-readable output, make documentation queryable at runtime, support field-level filtering to minimize token usage
- **The CLI vs. MCP debate is converging on "both"**: Google's project supports both modes, suggesting the industry will standardize on offering CLI and MCP interfaces for the same capabilities

## Notable Quotes

> "It's clear MCP servers are out, skills and CLIs are in, right? Well, not quite." — Better Stack

> "What's really interesting is that if I as a human wanted to do the same thing, I'd have to use help over and over again. But the agent is able to get this information really quickly and even know the exact params to use." — Better Stack

## Related Sources

- [245: Is Math Research Dead? Cursor's AI and the Rise of Local LLMs](245-innermost-loop-math-research-local-llms.md) — Google's infrastructure strategy and Gemini pricing discussed
- [246: The AI Honeymoon Is Over](246-the-blur-ai-honeymoon-over.md) — Skills system and Claude Code tooling discussed in practical context

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system, CLI tooling integration with Claude Code
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Agent-first tool design, CLI vs. MCP patterns for agent integration
