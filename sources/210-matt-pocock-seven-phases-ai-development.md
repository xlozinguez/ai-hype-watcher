---
source_id: "210"
title: "The 7 Phases of AI-Driven Development"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Ah9p7v7nJWg"
date: "2026-03-04"
duration: "8:26"
type: "video"
tags: ["agentic-coding", "ai-sdlc", "specification", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 210: The 7 Phases of AI-Driven Development

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-04 | **Duration**: 8:26

## Summary

Matt Pocock presents a seven-phase framework for shipping production-quality work with AI coding assistants like Claude Code. The framework is tool-agnostic — whether using Ralph loops, GSD, or SpecKit — and covers the full lifecycle from initial idea through human QA. The central argument is that serious AI-assisted development requires structured phases, not ad hoc prompting, and that the process is explicitly "not for vibe coders."

The seven phases are: idea, research, prototype, PRD, implementation planning (kanban board), execution (agent loop), and QA (human verification). The last three phases iterate in a loop until quality standards are met. Pocock emphasizes that the upfront investment in research, prototyping, and specification pays off by enabling agents to run autonomously during execution — you can literally go AFK and get good results.

## Key Concepts

### Phase 1: Idea

The starting point can be anything from an entire app to a narrow bug fix or refactor. The size doesn't matter — the process scales from small focused tasks to ambitious projects. The key is having a clear reason for invoking the workflow.

### Phase 2: Research

If the idea involves external dependencies or hard-to-explore APIs (e.g., a Stripe integration), cache the research in a `research.md` asset accessible to the agent. This prevents every fresh context window from re-exploring difficult-to-access information. Research assets are ephemeral — they live only for the sprint lifetime and should be discarded afterward to prevent context rot ([02:00](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=120)).

### Phase 3: Prototype

Prototyping is essential when you need to impose taste on the outcome — UI that needs to look or behave a certain way. Pocock's approach: throw up multiple ideas on a throwaway route, iterate in a couple of human-in-the-loop sessions, then commit the chosen prototype for the agent to reference during implementation. This also applies to software architecture decisions and external service integrations, not just visual design ([02:30](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=150)).

### Phase 4: PRD (Product Requirements Document)

After research and prototyping provide concrete context, formally describe the destination. The PRD doesn't need to specify implementation decisions — just the end state the user will see and how it behaves. Crucially, the agent should "absolutely grill" you during PRD creation, walking down every branch of your decision tree. Pocock uses a dedicated "writer PRD" skill for this ([03:32](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=212)).

### Phase 5: Implementation Planning (Kanban Board)

Break the PRD into tickets with blocking relationships. This enables parallelization — find all unblocked tickets and spin up an agent for each one. Pocock uses GitHub Issues for both the PRD and the kanban board, noting that GitHub lacks built-in blocking relationships (Linear does better here). A dedicated skill converts the PRD into separate issues ([04:33](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=273)).

### Phase 6: Execution (Agent Loop)

Run a coding agent to complete all tickets. Most of the time, a sequential agent working through each ticket suffices — parallelization isn't always necessary. For Pocock, this is the Ralph loop. With the prior phases done properly, execution can run fully AFK with good results ([05:03](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=303)).

### Phase 7: QA (Human Verification)

The agent generates a QA plan, then a human walks through and verifies the completed work. This typically produces more tickets for the kanban board, triggering another execution-QA cycle. QA also includes reading the code the agent produced — though this may not always be needed with "gray box architecture" approaches. Phases 5–7 loop iteratively until quality converges ([05:34](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=334)).

## Practical Takeaways

- **Cache research early**: External API docs, library specifics, and hard-to-explore information should be captured in ephemeral research assets before the agent starts coding — but discard them when the sprint ends to prevent context rot.
- **Prototype before specifying**: Concrete feedback from prototyping makes PRDs much stronger than going straight from idea to spec. This applies to architecture decisions, not just UI.
- **Let the agent interrogate you**: During PRD creation, prompt the agent to challenge every decision. The spec should survive scrutiny before execution begins.
- **Invest in the kanban breakdown**: Tickets with blocking relationships enable parallelization and make execution loops more predictable.
- **Expect iteration**: The execution-QA loop is designed to run multiple times. Ship quality through convergence, not perfection on the first pass.

## Notable Quotes

> "This is not for vibe coders. We are people that are serious about AI engineering and serious about building applications that are built to last." — Matt Pocock ([00:44](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=44))

> "We really need to hammer out the design. And this means we need to prompt the agent to absolutely grill us walking down every part of our decision tree." — Matt Pocock ([04:03](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=243))

> "With all of this setup — with the research, with the prototype, with the kanban board, with the PRD helping it — you can totally run this execution loop AFK and the results will be really good." — Matt Pocock ([07:07](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=427))

## Related Sources

- [115: Ship working code while you sleep with the Ralph Wiggum technique](115-matt-pocock-ralph-wiggum-technique.md) — The Ralph loop execution method referenced as Pocock's primary approach for Phase 6
- [113: I was an AI skeptic. Then I tried plan mode](113-matt-pocock-plan-mode.md) — Plan mode as an implementation of Phase 5 (implementation planning)
- [126: How I use Claude Code for real engineering](126-matt-pocock-claude-code-engineering.md) — Earlier articulation of Pocock's engineering-first AI coding philosophy
- [164: Deep Modules for AI — Designing Codebases Agents Can Navigate](164-matt-pocock-codebase-ai-ready.md) — The "gray box architecture" that reduces QA burden in Phase 7
- [108: The 5 Levels of AI Coding](108-nate-b-jones-five-levels-ai-coding.md) — Complementary framework mapping developer maturity in AI-assisted workflows
- [118: No Vibes Allowed: Solving Hard Problems in Complex Codebases](118-dex-horthy-no-vibes-complex-codebases.md) — Similar emphasis on specification and research before execution

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Specification-first development, PRD creation, and structured workflows
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Agent execution loops, task decomposition, and iterative QA cycles
