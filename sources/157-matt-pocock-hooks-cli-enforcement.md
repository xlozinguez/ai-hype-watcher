---
source_id: "157"
title: "Hooks Over CLAUDE.md — Deterministic CLI Enforcement for Agents"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=3CSi8QAoN-s"
date: "2026-02-25"
duration: "06:51"
type: "video"
tags: ["claude-code", "context-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 157: Hooks Over CLAUDE.md — Deterministic CLI Enforcement for Agents

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-02-25 | **Duration**: 06:51

## Summary

Matt Pocock demonstrates why CLAUDE.md is the wrong place for CLI enforcement rules (like "use pnpm not npm") and shows how to use Claude Code hooks instead. The key argument is that CLAUDE.md instructions are probabilistic — they reduce the chance of unwanted commands but don't prevent them — while hooks are deterministic, blocking commands with certainty while consuming zero context window budget.

The video walks through a complete workflow: taking a CLAUDE.md instruction, converting it into a pre-tool-use hook with a bash script that intercepts npm commands and exits with code 2 (blocked), then removing the instruction from CLAUDE.md to free up context budget. Pocock frames this as part of a broader philosophy: move enforcement out of the LLM's instruction budget and into deterministic feedback loops.

## Key Concepts

### Deterministic vs. Probabilistic Enforcement

CLAUDE.md rules are instructions to the LLM — they consume context tokens every session and only reduce the probability of unwanted behavior. Hooks are shell commands that execute on events — they deterministically block or transform behavior with zero context cost. Negative instructions ("never run git push") are especially wasteful in CLAUDE.md because they burn instruction budget without guaranteeing prevention.

### Instruction Budget as a Finite Resource

LLMs have an effective instruction budget of roughly 500 instructions before compliance degrades. Every irrelevant instruction in CLAUDE.md (PR review checklists during debugging, deployment procedures during testing) competes for this budget. Moving deterministic rules to hooks frees budget for the complex reasoning that actually needs LLM attention.

### The Hook-Based Workflow

A pre-tool-use hook matching the bash tool intercepts commands before execution. A simple bash script checks if the command starts with "npm", echoes a redirect message ("use pnpm, not npm"), and exits with code 2 to block execution. Claude Code then automatically retries with the correct tool (pnpm). The hook configuration lives in `.claude/settings.json`.

## Practical Takeaways

- **Convert deterministic CLAUDE.md rules into hooks** — use a prompt to analyze your CLAUDE.md and identify rules that can be enforced deterministically (CLI preferences, command blockers), then generate hook scripts
- **Use exit code 2 in hook scripts to block commands** — this tells Claude Code the action was denied, prompting it to retry with the correct approach
- **Remove migrated rules from CLAUDE.md** — the whole point is to free up instruction budget for complex, non-deterministic guidance
- **Extend the pattern to linting** — ESLint rules can enforce style preferences (e.g., no positional parameters) as deterministic feedback loops, further reducing CLAUDE.md bloat
- **Think in feedback loops** — the most effective Claude Code configurations create just-in-time correction mechanisms rather than upfront instruction dumps

## Notable Quotes

> "By adding this, we're reducing our chances of running git push or reducing our chances of running npm, but we're not preventing it." — Matt Pocock

> "You get to take instructions out of your instruction budget and enforce them deterministically." — Matt Pocock

## Related Sources

- [154: Why Most Developers Are Using Claude Code Wrong](154-diy-smart-code-claude-code-features.md) — Broader overview of the five Claude Code customization features including hooks
- [158: How to build Claude Skills Better than 99% of People](158-ben-ai-skill-engineering.md) — Complementary skill engineering approach

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md optimization, context discipline
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Hooks, event-driven automation, deterministic enforcement
