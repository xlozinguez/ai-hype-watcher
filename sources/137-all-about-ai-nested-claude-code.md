---
source_id: "137"
title: "Super Nested Claude Code Is Vibecoding On STEROIDS"
creator: "All About AI"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=BlyJKhhbzwA"
date: "2026-03-02"
duration: "16:32"
type: "video"
tags: ["multi-agent", "agentic-coding", "claude-code", "agent-teams", "vibe-coding"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 137: Super Nested Claude Code Is Vibecoding On STEROIDS

> **Creator**: All About AI | **Platform**: YouTube | **Date**: 2026-03-02 | **Duration**: 16:32

## Summary

All About AI demonstrates a nested Claude Code system where a controller Claude Code instance (running Opus) orchestrates multiple child Claude Code instances via tmux terminals. The user provides only a high-level goal, and the controller plans the architecture, decides how many terminals to spawn (up to six), distributes detailed prompts to each child, monitors their output, and integrates the results — creating a fully autonomous multi-agent coding pipeline.

The video showcases two demos: building a procedural 3D space galaxy in Three.js (six parallel terminals for galaxy, objects, renderer, spacecraft, UI, and index) and creating a real-time training visualization dashboard for a micro-GPT language model (four terminals for backend, charts, dashboard, and samples). Both projects are completed end-to-end without additional user prompts after the initial goal.

## Key Concepts

### Controller-Worker Architecture via Tmux

The system uses a single Claude Code instance as a controller running on Opus that spawns child Claude Code instances in tmux terminals. The controller reads outputs from all terminals, can stop/close them, and sends targeted prompts to each. This creates a hierarchical orchestration pattern where the user only provides a goal and the controller handles all planning and delegation.

### Autonomous Planning and Terminal Allocation

The controller decides independently how many terminals to spawn and what role each should play. In the first demo it chose six specialized terminals (galaxy, objects, renderer, spacecraft, UI, index); in the second it chose four (backend, charts, dashboard, samples). Setting terminals to "auto" lets the controller determine the optimal parallelization strategy based on the goal.

### Quality Cascade from Controller to Workers

A key insight is that Opus as the controller generates highly detailed, precise prompts for the child instances, which can run on less capable models (like Sonnet). The detailed instructions compensate for the worker model's lower capability, effectively cascading quality from the planning tier down to the execution tier.

## Practical Takeaways

- **Goal-only prompting**: The user provides a single open-ended goal; the controller handles all subsequent planning, prompting, and coordination across multiple Claude Code instances.
- **Opus controller + cheaper workers**: Running the controller on Opus and children on Sonnet keeps cost down while maintaining output quality through detailed delegation.
- **Screenshot-based verification**: The controller uses Playwright to take screenshots of the running application to verify correctness before declaring the task complete.
- **Mac-only limitation**: The tmux-based approach currently only works on macOS, not Windows.

## Notable Quotes

> "You never do a prompt. You only do the goal and the controller takes control of all the prompts it wants to run." — All About AI

> "Since the controller here is Opus, it gives very detailed instructions. So I did try to just run on Haiku and it seems to run very well even if we just had a lesser model because of the instructions from Opus is so precise." — All About AI

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Nested agent orchestration and controller-worker delegation
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Multi-terminal parallel agent coordination via tmux
