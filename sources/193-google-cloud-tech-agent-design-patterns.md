---
source_id: "193"
title: "Single, Sequential, and Parallel Agent Design Patterns with ADK"
creator: "Google Cloud Tech"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=GDm_uH6VxPY"
date: "2026-02-27"
duration: "08:21"
type: "video"
tags: ["agentic-patterns", "multi-agent"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 193: Single, Sequential, and Parallel Agent Design Patterns with ADK

> **Creator**: Google Cloud Tech | **Platform**: YouTube | **Date**: 2026-02-27 | **Duration**: 08:21

## Summary

This episode from Google Cloud Tech's agentic pattern series introduces the three foundational multi-agent design patterns using Google's Agent Development Kit (ADK): single agent, sequential agent, and parallel agent. Each pattern is demonstrated with a trip-planning scenario, complete with code examples and live ADK Web UI demos showing tracing and session state. The video frames these as building blocks that trade off simplicity, control, and speed.

The key insight is that pattern selection is driven by the nature of the task. Single agents are flexible but unreliable for complex multi-step logic because LLMs are non-deterministic. Sequential agents add control through fixed ordering but sacrifice flexibility. Parallel agents maximize speed for independent subtasks but require a synthesis/aggregation step. The series previews more advanced patterns (loop/critique, orchestrator, agent-as-tool) for a future episode.

## Key Concepts

### Single Agent Pattern

One agent with a comprehensive system prompt and a set of tools (e.g., Google Search). The agent uses the model's reasoning to determine step sequence. Works well for straightforward tasks but becomes unreliable as complexity grows — the non-deterministic nature of LLMs means multi-step logic in a single prompt cannot be guaranteed to execute consistently.

### Sequential Agent Pattern

An assembly-line model where specialized sub-agents execute in fixed order. Each agent's output feeds into the next via shared session state (a "shared scratch pad"). Communication happens through curly-brace variable interpolation in system prompts. Provides high control and predictability but is inflexible — the rigid structure cannot adapt to dynamic situations.

### Parallel Agent Pattern

Multiple specialized agents run independently and concurrently on tasks that do not depend on each other. Results are combined by a final aggregator agent in a sequential step. Significantly reduces latency but incurs higher initial cost (multiple agents running simultaneously) and adds complexity through the required synthesis step.

### Shared Session State

The mechanism by which agents in sequential and parallel patterns communicate. Acts as short-term memory — one agent writes findings to the state, the next reads from it using template variables in its system prompt. This is the key coordination primitive across all ADK multi-agent patterns.

## Practical Takeaways

- **Start with single agent for simple tasks**: Only escalate to multi-agent patterns when the task has genuinely distinct components or requires reliability guarantees.
- **Use sequential for repeatable, ordered workflows**: When step order matters and each step feeds the next, sequential agents add control without much complexity.
- **Use parallel for independent subtasks**: When tasks can be decomposed into parts that do not depend on each other, parallel execution cuts latency significantly.
- **Always plan for aggregation**: Parallel patterns require a synthesis step — budget for the complexity of combining independent agent outputs into a coherent result.

## Notable Quotes

> "Since AI is non-deterministic, you cannot always guarantee that it will follow your multi-step logic perfectly every time." — Google Cloud Tech

> "The output of one sub-agent becomes the direct input for the next sub-agent. It's like an assembly line." — Google Cloud Tech

## Related Sources

- [020: Agent Teams Deep Dive](020-simon-scrapes-agent-teams.md) — Claude's implementation of multi-agent coordination
- [146: Pi Coding Agent](146-indydevdan-pi-coding-agent.md) — Multi-agent orchestration patterns in alternative tools

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Core agent orchestration patterns
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Multi-agent coordination and parallel execution
