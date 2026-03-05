---
source_id: "145"
title: "The 7 phases of AI-driven development"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Ah9p7v7nJWg"
date: "2026-03-03"
duration: "8:26"
type: "video"
tags: ["agentic-coding", "specification", "ai-sdlc", "vibe-coding"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 145: The 7 phases of AI-driven development

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-03 | **Duration**: 8:26

## Summary

Matt Pocock distills AI-driven development into seven distinct phases that apply regardless of the specific tooling or methodology (RALPH loops, GSD, SpecKit). The phases move from initial idea through research, prototyping, PRD creation, kanban board decomposition, execution loops, and finally human QA. The framework explicitly rejects "vibe coding" in favor of engineering discipline, emphasizing that each phase exists to reduce ambiguity before agents execute code.

The key insight is that prototyping should happen before the PRD, not after — you need concrete feedback and taste decisions before you can write a good specification. The execution phase then becomes reliable enough to run AFK because all the ambiguity has been resolved in earlier phases.

## Key Concepts

### The Seven Phases

1. **Idea** — The starting point: a feature, bug fix, refactor, or entire application. Can be any size.
2. **Research** — Cache external API documentation, unfamiliar libraries, or difficult-to-explore areas into a research.md asset accessible to agents. Research assets are ephemeral — they expire with the sprint to avoid stale context causing wrong turns.
3. **Prototype** — Iterate with human-in-the-loop to impose taste on the outcome. Generate multiple approaches on throwaway routes, pick the best, and commit it as a reference for later implementation.
4. **PRD (Product Requirements Document)** — Describe the end state with no ambiguity. Have the agent "grill" you through your decision tree. The prototype provides concrete grounding that makes the PRD more precise.
5. **Kanban Board** — Decompose the PRD into tickets with blocking relationships. This enables parallelization — spin up agents for all non-blocking tickets simultaneously.
6. **Execution** — Run agents through tickets in a loop (RALPH loop or sequential). With proper research, prototype, and PRD, this can run unattended.
7. **QA** — Agent produces a QA plan, then a human walks through and QAs the completed work. Produces more tickets, returning to the kanban board. Loop phases 5-7 until the product is complete.

### Prototype Before PRD

Most spec-driven workflows jump from idea to specification. Pocock argues that prototyping first is essential because the PRD becomes too abstract without concrete feedback. By seeing working code and making taste decisions during prototyping, the subsequent PRD is grounded in reality rather than imagination. This prevents the common failure mode where a well-written spec produces technically correct but wrong-feeling output.

### Research as Ephemeral Cache

External API documentation and library specifics should be cached into the repo for agent access, but this research has a natural expiration date. Stale research causes agents to take wrong turns based on outdated information. Treat research assets as sprint-scoped, not permanent documentation.

## Practical Takeaways

- **Prototype before specifying**: Get concrete feedback through human-in-the-loop iteration before writing the PRD. Abstract specs produce technically correct but taste-blind results.
- **Use kanban boards for parallelization**: Decompose PRDs into tickets with blocking relationships. Non-blocking tickets can run as parallel agents.
- **Cache research but let it expire**: Store external API docs and library specifics for agent access, but delete them after the sprint to prevent stale context from causing errors.
- **Loop execution and QA**: Expect to cycle through kanban-execution-QA multiple times. Each QA phase produces new tickets that feed back into execution.
- **The RALPH loop enables AFK execution**: With sufficient upfront investment in research, prototype, and PRD, the execution loop can run unattended with good results.

## Notable Quotes

> "This is not for vibe coders. We are people that are serious about AI engineering and serious about building applications that are built to last." — Matt Pocock

> "By the time we get to the PRD, it's a little bit too abstract. You really need concrete feedback first." — Matt Pocock

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Spec-first development, RALPH loops, structured development workflows
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Task decomposition, execution loops, kanban-driven agent orchestration
