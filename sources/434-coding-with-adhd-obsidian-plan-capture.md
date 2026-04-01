---
source_id: "434"
title: "Auto-Save Claude Code Plans to Obsidian"
creator: "Coding With ADHD"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=blw8OBvXt3U"
date: "2026-03-28"
duration: "5:04"
type: "video"
tags: ["claude-code", "agentic-coding", "task-system", "context-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 434: Auto-Save Claude Code Plans to Obsidian

> **Creator**: Coding With ADHD | **Platform**: YouTube | **Date**: 2026-03-28 | **Duration**: 5:04

## Summary

This video demonstrates how to automatically save Claude Code plan-mode outputs to an Obsidian vault using two technologies in combination: Claude Code hooks and the newly released Obsidian CLI. The core problem being solved is that Claude Code stores engineering plans in a global `~/.claude/plans` directory with randomized filenames, making them effectively unsearchable and disconnected from any project context or personal knowledge system.

The solution is a shell script (`capture-plan.sh`) registered as a Claude Code hook that fires on the `exit_plan_mode` lifecycle event. When triggered, the script uses Claude (running headless via `claude -p` with the Haiku model) to generate a summary and tags for the plan, then uses the Obsidian CLI to write a properly formatted note into the vault and append a wiki-linked summary entry to the daily journal. The entire pipeline runs automatically — no copy-pasting, no window switching.

The broader significance is the combination of two emerging automation surfaces: Claude Code's hooks system (which allows shell scripts to intercept specific agent lifecycle events) and the Obsidian CLI (which breaks the vault out of the GUI and into scriptable terminal access). Together they enable AI agents to write structured, interlinked notes into a personal knowledge base as a natural side effect of development work.

---

## Key Concepts

### Claude Code Hooks
Hooks are shell scripts registered in Claude Code's settings file that fire at specific lifecycle events within the agent's operation. The hook shown here uses the `permission_request` event scoped to the `exit_plan_mode` matcher — meaning it fires precisely when Claude finishes constructing a plan and is about to ask permission to proceed. This event-driven architecture allows developers to intercept and act on agent state without modifying the agent's core behavior.

### Obsidian CLI
Obsidian recently released a command-line interface that exposes vault operations — creating notes, appending content, setting front matter properties — directly from the terminal. Once enabled in settings and added to the system path, it makes the vault a first-class target for shell scripts and automation pipelines. The three key commands used here are `obsidian create`, `obsidian append`, and `obsidian property set`.

### Headless Claude for Summarization (Meta-Agent Pattern)
The script invokes Claude Code itself in headless mode (`claude -p` with `--bare` output and `--max-turns 1`) to summarize the plan content it just generated. This is a lightweight meta-agent pattern: using the same AI system to post-process its own outputs before storing them. Haiku is used deliberately — it's fast and cheap for a simple summarization task.

### Plan Mode as Decision Records
Claude Code's plan mode generates detailed engineering artifacts — architecture decisions, implementation steps, tradeoffs. The video frames these as ADRs (Architecture Decision Records) in all but name: valuable documentation of *why* something was built a certain way. The problem is the default storage makes them inaccessible. Routing them into a structured vault with proper front matter, dates, and wiki links transforms ephemeral agent output into durable, searchable project knowledge.

### Structured Note Templates with Front Matter
Each saved plan note is written with full YAML front matter: created date, status, tags, source (`claude-code plan-mode`), session ID, hook event, and source type. It also includes a wiki link back to the daily journal entry. This bidirectional linking pattern — plan links to journal, journal links to plan — is what makes the notes valuable inside a second brain system rather than just an archive.

---

## Practical Takeaways

- **Register hooks in `~/.claude/settings.json`** scoped to specific matchers (e.g., `exit_plan_mode`) to keep automation surgical — the script fires exactly once, at exactly the right moment, and never during unrelated operations.
- **Use `claude -p` with `--max-turns 1` and a lightweight model (Haiku) for post-processing tasks** like summarization or tagging — it keeps latency and cost low while leveraging the same toolchain.
- **The Obsidian CLI unlocks vault automation**: once on the system path, any shell script, cron job, or AI agent can read and write structured notes — making it viable as an output target for agentic workflows, not just a manual writing tool.
- **Front matter should include provenance metadata** (session ID, hook event, source type) so notes remain auditable and filterable — especially useful when accumulating many AI-generated notes over time.
- **Bidirectional wiki links between plans and daily journal** create navigable context: you can find what you were working on a given day and immediately jump to the full engineering rationale.

---

## Notable Quotes

> "These plans are valuable. They're basically decision records for why you built something a certain way."

> "We're using Claude to summarize its own plan, which I think is kind of neat."

> "I didn't copy anything. I didn't switch windows. It just happened."

---
