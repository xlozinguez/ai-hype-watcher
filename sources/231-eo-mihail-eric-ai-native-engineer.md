---
source_id: "231"
title: "From Writing Code to Managing Agents — Most Engineers Aren't Ready"
creator: "EO (Mihail Eric)"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=wEsjK3Smovw"
date: "2026-02-26"
duration: "14:20"
type: "video"
tags: ["ai-sdlc", "agentic-coding", "multi-agent", "ai-landscape", "capability-overhang"]
curriculum_modules: ["01-foundations", "04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 231: From Writing Code to Managing Agents — Most Engineers Aren't Ready

> **Creator**: EO (Mihail Eric) | **Platform**: YouTube | **Date**: 2026-02-26 | **Duration**: 14:20

## Summary

Mihail Eric, who leads AI at an early-stage San Francisco startup and teaches "The Modern Software Developer" at Stanford, argues that the engineering profession is undergoing a fundamental shift from writing code to managing agents. The class — the first at Stanford focused on AI across the entire SDLC — filled instantly with over 100 students, reflecting intense demand for this skill set.

Eric identifies a perfect storm hitting junior developers: post-COVID overhiring followed by mass layoffs, a tripled CS graduate pipeline, and AI tools reducing headcount requirements. But rather than writing off junior engineers, he argues they have a unique advantage — they are "sponges" without the ingrained habits that make senior developers resistant to AI tools. The talk covers agent-friendly codebases, the importance of taste in software, and why multi-agent orchestration requires the same skills as good human management.

## Key Concepts

### The AI-Native Engineer

The emerging "AI-native engineer" combines traditional CS fundamentals (system design, algorithmic thinking) with fluency in agentic workflows. This is not about replacing coding knowledge but layering agent orchestration on top of it. Eric draws a parallel to learning math: CS teaches you how to think about complex systems, and that thinking remains essential even when agents write the code.

### Incremental Multi-Agent Orchestration

Eric advises building up agent usage piecemeal rather than jumping to 10 parallel agents. Start with one agent doing complex work well, then add a second for an isolated task (fix the logo), then a third for another independent change (update header copy). The key skill is context switching between agents — knowing what each is working on and intervening when they get stuck. This is fundamentally the same skill as being a good human engineering manager.

### Agent-Friendly Codebases

For agents to work effectively, codebases need: (1) comprehensive test coverage as "contracts that define software correctness," (2) consistent READMEs that match the actual code, (3) consistent design patterns (don't have two different APIs for the same operation), and (4) linting and style checking for consistent formatting. Agents compound errors quickly — one misunderstanding in step one doubles down in step two. The codebase must be "airtight" before agents touch it.

### Taste and the Last Mile

The difference between functional software and incredible software is taste — and taste is built in the last mile of effort beyond minimum requirements. Eric observed that his best Stanford students were the ones who kept building beyond the assignment, eventually turning class projects into startups. Even the Claude Code team at Anthropic rewrites their own tool weekly, experimenting constantly. Experimentation must be embedded into the developer workflow.

## Practical Takeaways

- **Build up agents incrementally**: Master one agent, then add isolated tasks for additional agents. Don't start with 10 parallel agents.
- **Context switching is the core multi-agent skill**: Track what each agent is doing, intervene when stuck, and maintain enough context to push work forward. This is management.
- **Make your codebase agent-friendly**: Comprehensive tests, consistent READMEs, uniform design patterns, and linting. Agents only operate on explicitly defined contracts.
- **Junior developers have an AI advantage**: No ingrained habits, willing to experiment, and they become the most nimble AI-native engineers.
- **Embed experimentation in your workflow**: The best engineers constantly iterate on their tools and processes, not just their code.

## Notable Quotes

> "Adding more agents doesn't always create a better system. In fact, it can make for a lot worse systems if you just let them go and do whatever they want." — Mihail Eric

> "Agents can compound errors very quickly. If an agent has one misunderstanding in step one, it can double down and create another error in step two." — Mihail Eric

> "What I've described is basically what makes a good manager — a good human manager. It has nothing to do with an agent." — Mihail Eric

> "The arrogance of a developer sees any problem and thinks software is the solution — it's the confidence to say, I'm going to try and fix this in a way that I know how to use." — Mihail Eric

## Related Sources

- [145: The 7 Phases of AI-Driven Development](145-matt-pocock-7-phases.md) — Progressive model of AI adoption in development workflows

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — AI-native engineer identity, junior developer landscape
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Multi-agent orchestration, incremental agent adoption
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Context switching, agent-as-manager paradigm
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — AI-driven SDLC transformation, workforce impact
