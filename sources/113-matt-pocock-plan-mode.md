---
source_id: "113"
title: "I was an AI skeptic. Then I tried plan mode"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=WNx-s-RxVxk"
date: "2026-01-15"
duration: "12:21"
type: "video"
tags: ["agentic-coding", "claude-code", "context-engineering", "prompt-engineering"]
curriculum_modules: ["02-prompt-engineering", "03-context-engineering", "04-agentic-patterns"]
---

# 113: I was an AI skeptic. Then I tried plan mode

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-01-15 | **Duration**: 12:21

## Summary

Pocock describes his conversion from AI coding skeptic to advocate, crediting Claude Code's plan mode as the turning point. He argues that the plan-execute-test-commit loop is indispensable for getting quality outputs from coding agents, and that skipping the planning step is the single most common mistake developers make with AI tools.

The video explains the mechanics of plan mode — disabling file writes so the agent explores the codebase and builds context before making changes — and why this benefits both the agent (loaded context, pattern awareness) and the developer (clarified requirements through iterative rubber-ducking). Pocock walks through a real trace from his own project, showing how the agent explored his database schema, identified a migration bug, asked clarifying questions, and then executed a clean fix. He shares a key CLAUDE.md configuration — just three lines demanding extreme conciseness in plans — that he considers essential for making plan mode practical at scale.

## Key Concepts

### The Plan-Execute-Test-Commit Loop ([00:30](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=30))

Pocock's core workflow: enter plan mode, iterate on a plan with the AI, switch to execution mode, run tests (unit, type checking, or manual QA), then commit. This loop repeats for each unit of work. Skipping the plan step leads to most of the failure modes developers experience with AI coding tools.

### Plan Mode as Context Loading ([03:30](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=210))

In plan mode, the agent's write capability is disabled, forcing it into exploration. Claude Code often uses cheap, fast models like Haiku 4.5 in sub-agents to scan the codebase efficiently, then summarizes findings to the parent agent. This front-loads the context window with relevant patterns, schemas, and conventions before any code is written.

### Planning as Rubber-Ducking ([05:00](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=300))

The Pragmatic Programmer's observation that "no one ever knows what they want" applies directly to AI coding. The iterative planning process — the AI suggests, the developer refines — forces both parties to clarify requirements. The developer often discovers unstated assumptions and edge cases, making execution straightforward afterward.

### Concise Plans via CLAUDE.md ([08:30](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=510))

Three lines in the CLAUDE.md file transform plan quality: "Make the plan extremely concise. Sacrifice grammar for the sake of concision." Plus: "At the end of each plan, give me a list of unresolved questions to answer if any." This cuts 2,000-word plans to 400 words and puts the agent in an appropriately paranoid mode that surfaces unknowns.

### When to Skip Plan Mode ([10:00](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=600))

Pocock acknowledges that when you know the codebase deeply and the change is simple, you can be faster than the LLM. But these cases are limited — plan mode shines for unfamiliar repos, complex architectural changes, and cross-language work. He argues developers should invest in AI familiarity now because the tools will only get faster, eroding speed-based advantages.

## Practical Takeaways

- **Always plan before executing**: The plan step loads the agent's context with relevant code patterns and clarifies requirements for both the developer and the AI.
- **Add conciseness rules to CLAUDE.md**: Three lines demanding concise plans and unresolved questions dramatically improve plan readability and surface hidden unknowns.
- **Use dictation tools**: Pocock recommends Whisper Flow or Super Whisper for dictating prompts, noting it dramatically speeds up the input side of the workflow.
- **Share plans as RFCs**: Plans can be posted to GitHub issues or PRs for team review, functioning as lightweight request-for-comment documents.
- **Keep CLAUDE.md instructions minimal**: Fewer instructions preserve more of the LLM's "instruction budget" for actual work. Concision in configuration yields better overall steering.

## Notable Quotes

> "Every piece of code I write now goes through this loop where I first plan it in plan mode with an AI. I then get the AI to execute the plan. We then test it together. Then we commit the code and the process starts again." — Matt Pocock ([00:30](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=30))

> "Hashing out the requirements before you get to code is something we've been doing for 50 years as developers. And there's no reason why we should stop now." — Matt Pocock ([06:00](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=360))

> "If your only advantage over AI is your speed, then that advantage will get eroded more and more and more." — Matt Pocock ([11:00](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=660))

## Related Sources

- [005: Vibe Coding Readiness](005-nate-b-jones-vibe-coding-readiness.md) — Specification-first approach to AI coding
- [024: Agentic Coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) — Broader agentic coding workflow patterns
- [064: One Prompt Every Agentic Codebase Should Have](064-indydevdan-agentic-prompt.md) — Complementary CLAUDE.md configuration strategies
- [115: Ralph Wiggum Technique](115-matt-pocock-ralph-wiggum-technique.md) — Pocock's loop-based execution technique that builds on plan mode

## Related Curriculum

- [Module 02: Prompt Engineering](../curriculum/02-prompt-engineering/README.md) — CLAUDE.md configuration and instruction design
- [Module 03: Context Engineering](../curriculum/03-context-engineering/README.md) — Context loading strategies and sub-agent exploration
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Plan-execute loops and agent workflow design
