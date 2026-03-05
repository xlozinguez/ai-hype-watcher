---
source_id: "160"
title: "MIT Missing Semester — Agentic Coding Fundamentals and Context Management"
creator: "Missing Semester"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=sTdz6PZoAnw"
date: "2026-02-19"
duration: "1:00:34"
type: "video"
tags: ["agentic-coding", "claude-code", "context-engineering", "mcp"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 160: MIT Missing Semester — Agentic Coding Fundamentals and Context Management

> **Creator**: Missing Semester | **Platform**: YouTube | **Date**: 2026-02-19 | **Duration**: 1:00:34

## Summary

MIT's Missing Semester course dedicates an entire lecture to agentic coding, covering the conceptual foundations, practical usage, and advanced features of coding agents like Claude Code. The lecture walks through how language models work as probability distributions over token sequences, how agent harnesses wrap these models in tool-calling loops, and how context management is the key skill for effective agent use.

The lecture is notable for its pedagogical clarity: it demystifies coding agents by explaining the LLM-harness loop, demonstrates live demos of feature implementation and bug fixing with Claude Code, and systematically covers advanced topics including parallel agents with git worktrees, MCP connectors, context compaction, CLAUDE.md / agents.md files, skills as lazy-loaded context, and sub-agents for context isolation. The instructor consistently emphasizes that AI is not magic — these are probabilistic models that require careful review and human judgment.

## Key Concepts

### The LLM + Agent Harness Architecture

A coding agent consists of two parts: an underlying language model (a probability distribution over completions given prompts) and an agent harness that calls the LLM in a loop, dispatches tool calls (bash, file read/write, search), feeds results back as additional context, and repeats until the model emits a final text response. Understanding this loop is essential for using agents effectively.

### Context Management as Core Skill

The lecture dedicates significant time to context management techniques: clearing context between unrelated tasks, rewinding conversation history, compaction (LLM-summarized history compression), agents.md/CLAUDE.md files for persistent project instructions, skills as on-demand context loading (one level of indirection to avoid bloating the initial context), and sub-agents for context isolation during subtasks like web fetching.

### Parallel Agents and Git Worktrees

For working on multiple tasks simultaneously, the lecture recommends using git worktrees to create isolated directory checkouts, then running separate agent instances in each worktree. This prevents file conflicts between agents and enables parallel workflows where one agent fixes a bug while another implements a feature.

### Test-Driven Agent Development

Coding agents work particularly well with feedback loops. Writing a failing test first (or having the agent write one), then instructing the agent to make it pass, creates a tight iteration cycle. The agent runs the test, reads code, identifies the bug, applies a fix, and re-runs the test — mirroring effective human development practice.

## Practical Takeaways

- **Use agents as intelligent shells**: For complex command-line operations where remembering flags and regex syntax is hard, describe what you want in natural language and let the agent generate and run the command.
- **Approve tool calls selectively**: Allow file edits autonomously (review via git later) but require approval for bash commands and other state-mutating operations to maintain security.
- **Keep context clean**: Clear context between unrelated tasks, use compaction for long sessions, and leverage skills files to avoid bloating the initial context window.
- **Use sub-agents for isolation**: When an agent needs to fetch web content or perform a subtask, spinning up a sub-agent keeps the parent's context window focused on the main task.

## Notable Quotes

> "A coding agent is basically just a conversational AI model with access to some tools that will help it write code." — Missing Semester

> "Sometimes verifying code can actually be harder than just writing the correct code yourself. So for really critical things, oftentimes I will just do the thing myself instead of even trying to call an AI tool." — Missing Semester

## Related Sources

- [159: Mo Bitar — After Two Years of Vibecoding](159-mo-bitar-vibecoding-handwriting.md) — Counterpoint on the limits of agent-generated code quality

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Agent harness architecture, CLAUDE.md, context management
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Sub-agents, parallel workflows, tool-calling loops
