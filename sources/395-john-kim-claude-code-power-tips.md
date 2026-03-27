---
source_id: "395"
title: "How I use Claude Code (Meta Staff Engineer Tips)"
creator: "John Kim"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=mZzhfPle9QU"
date: "2026-02-07"
duration: "46:12"
type: "video"
tags: ["claude-code", "context-engineering", "validation", "mcp", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 395: How I use Claude Code (Meta Staff Engineer Tips)

> **Creator**: John Kim | **Platform**: YouTube | **Date**: 2026-02-07 | **Duration**: 46:12

# How I Use Claude Code (Meta Staff Engineer Tips)

## Summary

John Kim, a Staff Engineer at Meta, shares 50 practical tips accumulated from six months of daily Claude Code use. Having largely transitioned away from writing code manually, Kim now spends roughly 12 hours a day pair-programming with Claude Code while reviewing every line of generated output. His central thesis is that effective AI-assisted development is fundamentally a discipline of **context engineering** — managing what Claude knows, when it knows it, and how much of the context window is consumed by competing signals.

The video is structured around four areas: foundational setup (project initialization, CLAUDE.md configuration), keyboard shortcuts for power users, essential slash commands, and git workflow integration. A recurring theme is that most of Claude Code's built-in tooling exists specifically to help engineers manage and optimize the context window — from `/context` auditing to compaction to careful MCP discipline. Kim repeatedly emphasizes that bloated or stale context degrades output quality just as much as a poorly worded prompt.

A second major theme is the importance of **validation loops**. Kim argues that giving Claude a reliable build/test cycle to run against is one of the highest-leverage interventions an engineer can make — more so than prompt refinement alone — because it enables autonomous self-correction across iteration cycles.

---

## Key Concepts

### CLAUDE.md as Structured Project Context
The CLAUDE.md file (generated via `/init`) is the primary mechanism for injecting persistent, project-specific context into every Claude Code session. Kim recommends keeping it under ~300 lines and including: high-level technical architecture, domain context, key file paths, design patterns, and critically, the **build/validation loop** commands. Larger files consume more initial tokens and dilute Claude's attention — brevity improves reliability. The file participates in a hierarchy: a project-level CLAUDE.md in the root directory, plus an optional global user-level file at `~/.claude/claude.md`.

### Plan Mode as a Default Starting Point
Kim uses plan mode (toggled via Shift+Tab) almost exclusively when beginning a new feature, treating it as a mandatory alignment step before allowing Claude to make edits. Planning first lets the engineer verify Claude's assumptions about the codebase and intended approach before any code is written. This reduces the cost of course-correction and avoids wasted iteration cycles caused by early wrong-direction execution.

### Context Window as the Core Resource to Manage
Kim frames nearly every tool and workflow decision around context economy. The `/context` slash command provides a visual audit of what is consuming the context window — MCPs are called out as a frequent "blowup" source. His rule: *"context is best served fresh and condensed."* He recommends auditing context regularly, disabling unused MCPs per-directory, and using `/clear` between unrelated tasks to prevent old task context from polluting new ones.

### Validation Loops as the Highest-Leverage Agentic Primitive
Embedding a working build and test cycle in CLAUDE.md (or project setup) is described as the single most impactful thing an engineer can do for agentic workflows. When Claude can run a real compile/test step after each change, it can self-correct autonomously — turning a one-shot prompt into a self-improving loop. Kim generalizes this beyond Claude Code: good AI agentic systems are defined by the quality of their validation feedback cycle.

### MCP Discipline: Powerful but Costly
MCPs (Model Context Protocol integrations) are powerful for teaching Claude to interact with third-party systems (e.g., Xcode), but Kim actively avoids installing them unless strictly necessary for the project. Each MCP connection adds token overhead that compounds across a long session. His approach: maintain project-specific MCP configurations, remove or disable anything not actively needed, and prefer writing scripts or custom tooling over reaching for an MCP by default.

---

## Practical Takeaways

- **Run `/init` at project start** to auto-generate a CLAUDE.md scaffold from your codebase; then curate it to ~300 lines covering architecture, file structure, patterns, and build commands.
- **Start every new feature in plan mode** (Shift+Tab) before switching to edit/execute mode — this catches bad assumptions cheaply before code is written.
- **Audit your context regularly with `/context`** — identify which MCPs or accumulated tool calls are consuming the most tokens, and disable them if they're not actively needed for the current task.
- **Embed your build/test loop in CLAUDE.md** — a working validation cycle is the single most reliable way to improve Claude's autonomous output quality across long sessions.
- **Use `/clear` or open a fresh instance between unrelated tasks** — carrying forward stale task context is a leading cause of regressions and erratic behavior in long sessions.

---

## Notable Quotes

> "Context is best served fresh and condensed."

> "If you ever felt like Claude Code has regressed and things are not working the way it is, or your cost and usage bill is going up, you really want to look at [/context] and then see which are the biggest offenders."

> "Validation, I think as a side tip, is probably one of the most important topics that you should really think about when you're thinking about trying to build good AI agentic coding systems or any workflows — really what is the validation loop, because that will dramatically improve how good your AI will be."

---
