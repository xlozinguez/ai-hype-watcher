---
source_id: "459"
title: "The \"PI\" (coding) agent is so much more than just another amazing coding agent!"
creator: "Maximilian Schwarzmüller"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=wVe3XOnio7M"
date: "2026-03-12"
duration: "15:25"
type: "video"
tags: ["agentic-coding", "context-engineering", "skills", "mcp", "multi-agent"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 459: The "PI" (coding) agent is so much more than just another amazing coding agent!

> **Creator**: Maximilian Schwarzmüller | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 15:25

## Summary

Maximilian Schwarzmüller introduces the PI coding agent as a philosophically distinct alternative to Claude Code, Codex, and Cursor. Rather than shipping a feature-rich, opinionated tool, PI provides a minimal core — essentially just read, write, edit, and a bash tool — and achieves flexibility through a deliberately lean system prompt and a first-party extensions system. The result is a smaller context window footprint and an agent that can be precisely shaped for any task, both coding and non-coding.

The video's central argument is that PI's minimal-core-plus-extensibility model makes it more versatile than tools that bake in more functionality upfront. The extensions system allows hooking into specific steps of the agentic loop (adding plan mode, custom slash commands, sub-agents, web access, etc.), while an agent skills system loads context lazily on demand rather than eagerly polluting the context window. Notably, PI deliberately omits MCP support, preferring workarounds like the MCPorter tool to avoid the context overhead MCP registration typically introduces.

Schwarzmüller demonstrates PI used outside of coding entirely — running a stock research task that fetches web data, spins up temporary scripts, and delivers an executive-style analysis — illustrating that a well-configured minimal agent with bash access is effectively a general-purpose automation tool. He also notes that OpenClaw (an open-source project) uses PI internally, signaling that the tool is gaining traction as a building block for higher-order agent systems.

---

## Key Concepts

### Minimal Core + Bash Tool as Universal Capability

PI's design philosophy is to ship the smallest possible toolset: read, write, edit, and bash. The bash tool is treated as a force multiplier — because agents can invoke any CLI from bash, they gain access to HTTP requests, script execution, JSON parsing, and arbitrary system control without needing dedicated tool wrappers. This keeps the system prompt lean, preserves context window space, and avoids locking the agent into a fixed set of pre-built integrations.

### Lazy-Loaded Agent Skills

PI implements an agent skills system (compatible with a shared standard also used by Codex) where skill files are markdown documents containing names, descriptions, and additional context/prompts. The agent reads only the name and description initially, then loads the full skill file on demand when it determines the skill is relevant to the current task. This is a direct context-engineering optimization — skills contribute zero tokens to the context window unless actively needed.

### First-Party Extensions and the Agentic Loop

Unlike skills (which are prompt-level context), PI extensions hook directly into the agentic loop itself — blocking certain tools during plan mode, modifying the terminal UI, adding slash commands, or injecting new capabilities like sub-agents or web fetching. Extensions can be shared via a package/marketplace model and installed globally or per project. This makes PI functionally composable: the base agent is nearly a blank slate that becomes whatever its extension configuration demands.

### Deliberate MCP Exclusion as Context Discipline

PI's maintainer explicitly excludes MCP support on the grounds that MCP tool registration fills the context window with capability descriptions the agent may never use. This is a concrete example of context engineering as a design constraint rather than an afterthought. The workaround — using a tool like MCPorter invoked dynamically via bash, described in a skill file — achieves MCP-like access without the upfront context cost.

### Per-Project Agent Specialization

Because skills and extensions can be scoped per project rather than only globally, PI enables distinct agent personas for different workspaces — a research-specialized agent in one directory, a stock-analysis agent in another, a system-diagnostics agent in a third. This project-level configurability is positioned as a meaningful advantage over tools like Claude Code and Codex, which have more uniform, globally-configured behaviors.

---

## Practical Takeaways

- **Treat bash access as the core capability, not a fallback.** An agent with a reliable bash tool and minimal other tooling is not underpowered — it can invoke any CLI, script, or HTTP utility available on the system. Design around that rather than waiting for dedicated tool wrappers.
- **Use lazy-loaded skill files to manage context discipline.** Structure agent knowledge as named skill files with clear descriptions so the model can self-select relevant context rather than loading everything upfront. This pattern scales better than a monolithic CLAUDE.md as project complexity grows.
- **Consider PI for non-coding agentic tasks.** The minimal core with web access and bash makes it viable as a general research or automation agent — not just a coding tool. A single agent configuration can handle tasks from stock analysis to system diagnostics.
- **Extensions are the right abstraction for agentic loop control.** If you need to block tools, add UI feedback, or inject plan/review phases, hooking into the loop via extensions is more robust than trying to prompt-engineer the same behavior.
- **Per-project agent configuration is an underutilized pattern.** Scoping skills and extensions to individual project directories allows highly specialized agents without polluting global config — worth adopting in any multi-project AI-assisted workflow.

---

## Notable Quotes

> "It only comes with read, write, edit, and a bash tool. And the bash tool of course is the powerful one because if you have a bash tool you essentially have access to everything."

> "Instead of packing a lot of stuff in there, you get an agent that is super extensible... you get an agent that has a context window that's not cluttered up and that's really flexible to do whatever you want it to do."

> "You could have one project on your system that has a research expert, another project that has a stocks research expert, and a third project that has a totally different expert... And that's also the reason probably why OpenClaw is using PI internally."

---
