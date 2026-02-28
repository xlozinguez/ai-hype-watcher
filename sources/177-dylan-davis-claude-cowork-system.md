---
source_id: "177"
title: "Three-Level Framework for Claude Co-Work Automation"
creator: "Dylan Davis"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=W9AOkjmt-XU"
date: "2026-02-26"
duration: "16:06"
type: "video"
tags: ["agentic-coding", "multi-agent", "context-engineering", "claude-code"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 177: Three-Level Framework for Claude Co-Work Automation

> **Creator**: Dylan Davis | **Platform**: YouTube | **Date**: 2026-02-26 | **Duration**: 16:06

## Summary

Dylan Davis presents a three-level framework for using Claude Co-Work (Anthropic's desktop agent tool) to move from ad-hoc AI assistance toward fully autonomous, memory-enhanced workflows. The framework progresses through "Do" (single task execution), "Make" (multi-system orchestration with sub-agents), and "Know" (compounding memory across sessions).

The key shift Davis highlights is that tools like Claude Co-Work and Codex can both read and write to files and connected systems, unlike traditional chat interfaces that are limited to reading. He demonstrates how system instructions via CLAUDE.md files eliminate the need for re-prompting, and how sub-agents can parallelize independent tasks for speed and quality.

## Key Concepts

### Three Levels: Do, Make, Know

The framework builds progressively. "Do" is giving the AI a single task (e.g., rename and organize files in a folder). "Make" involves dropping a single input (like a meeting transcript) and having the AI orchestrate across multiple systems (Gmail, calendar, CRM) to produce finished deliverables. "Know" adds a persistent memory file that compounds insights across sessions, transforming the AI from a disposable tool into a reusable asset.

### System Instructions via CLAUDE.md

Each working folder can contain a CLAUDE.md file that acts as persistent system instructions. The AI reads this file before executing any task, eliminating the need to re-prompt. This is analogous to custom instructions in GPT Projects, Claude Projects, or Gemini Gems, but scoped to a specific folder and workflow.

### Sub-Agent Parallelization

For complex multi-output tasks, Davis recommends explicitly instructing the AI to spawn sub-agents that work simultaneously on independent deliverables (e.g., one drafting an email, another building a spreadsheet, a third creating a PDF summary). Benefits include speed, higher quality from dedicated context windows (~200K tokens each), and prevention of context overflow that degrades single-agent performance.

### Memory Files for Compounding Knowledge

The "Know" level introduces a memory file that the AI reads at session start and updates at session end. Over recurring engagements (e.g., weekly client meetings), the AI accumulates client preferences, recurring themes, and key decisions. Davis emphasizes append-only memory (never remove previous entries) and structured entries covering communication preferences, themes, and decisions.

## Practical Takeaways

- **Use changelog files for large tasks**: Have the AI log every action to a changelog.txt so it can resume correctly after context compaction, avoiding duplicate work.
- **Scope folders to workflows**: Each Claude Co-Work folder should map to a specific workflow with its own CLAUDE.md instructions, enabling "type go and walk away" automation.
- **Spawn sub-agents only for independent tasks**: Sub-agents are valuable when tasks do not depend on each other; dependent tasks should remain sequential.
- **Build memory incrementally**: Start with level 1 (Do), add multi-system orchestration (Make), then layer in memory (Know) for recurring workflows.

## Notable Quotes

> "We're taking AI and transforming it from a tool to an asset that compounds in value over time." — Dylan Davis

> "When the AI's memory gets wiped and it keeps going, it can check this file and see exactly what's been done and not redo work." — Dylan Davis

## Related Sources

- [178: Multi-Agent Orchestration for AI-Native Engineers](178-eo-multi-agent-orchestration.md) — Complementary perspective on managing multiple agents and context switching

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Sub-agent spawning and context management patterns
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Multi-agent coordination and parallel task execution
