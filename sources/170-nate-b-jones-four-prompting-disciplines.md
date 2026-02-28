---
source_id: "170"
title: "Four Prompting Disciplines — From Prompt Craft to Specification Engineering"
creator: "Nate B Jones"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=BpibZSMGtdY"
date: "2026-02-27"
duration: "41:11"
type: "video"
tags: ["prompt-engineering", "context-engineering", "specification", "enterprise-ai"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 170: Four Prompting Disciplines — From Prompt Craft to Specification Engineering

> **Creator**: Nate B Jones | **Platform**: YouTube | **Date**: 2026-02-27 | **Duration**: 41:11

## Summary

Nate B Jones argues that "prompting" has silently diverged into four distinct disciplines, and most people are only practicing one of them. As autonomous agents now run for hours or days without human intervention, the synchronous chat-based prompting skills from 2025 have become table stakes. The real differentiator is a stack of four cumulative skills: prompt craft, context engineering, intent engineering, and specification engineering.

The piece is both a conceptual framework and a practical guide. Jones draws on examples from Anthropic's agent harness, Shopify CEO Toby Lutke's context engineering philosophy, and Klarna's cautionary tale of optimizing for the wrong metric. He defines five learnable primitives for specification engineering and provides concrete training exercises for each. The central thesis is that the shift from synchronous to autonomous AI work demands a fundamentally different communication discipline — one that benefits human-to-human collaboration as much as human-to-AI interaction.

## Key Concepts

### The Four Disciplines of Prompting

Jones presents a cumulative framework where each layer builds on the ones below:

1. **Prompt Craft** — The original skill: structuring clear instructions with examples, guardrails, output format, and ambiguity resolution. Now table stakes.
2. **Context Engineering** — Curating the optimal set of tokens for an LLM task: system prompts, tool definitions, retrieved documents, memory systems, MCP connections. Your 200-token prompt is 0.02% of what the model sees; the other 99.98% is context engineering.
3. **Intent Engineering** — Encoding organizational purpose, goals, values, trade-off hierarchies, and decision boundaries into infrastructure agents can act against. The Klarna example: their agent resolved 2.3M conversations but optimized for resolution time instead of customer satisfaction.
4. **Specification Engineering** — Writing documents that autonomous agents can execute against over extended time horizons without human intervention. Thinking of your entire organizational document corpus as agent-readable specifications.

### The Synchronous-to-Autonomous Shift

The traditional prompting model assumes synchronous interaction: you see output in real time, correct mistakes immediately, provide context when the model asks. Long-running agents break every assumption in that model. Everything you relied on in conversation — catching mistakes, providing missing context, course-correcting drift — must be encoded before the agent starts.

### Five Specification Primitives

Jones identifies five learnable primitives for specification engineering:

1. **Self-contained problem statements** — State a problem with enough context that the task is plausibly solvable without the agent fetching more information
2. **Acceptance criteria** — Describe what "done" looks like so an independent observer can verify the output without asking questions
3. **Constraint architecture** — Define musts, must-nots, preferences, and escalation triggers (the CLAUDE.md pattern is a practical implementation)
4. **Decomposition** — Break tasks into components that can be executed independently, tested independently, and integrated predictably
5. **Evaluation design** — Build test cases with known good outputs to verify quality measurably and consistently

### Organizational Implications

Jones references Shopify CEO Toby Lutke's observation that much of what people call "politics" in big companies is actually bad context engineering for humans — sloppy communication that relies on shared context that does not actually exist. Better specification engineering surfaces hidden assumptions and implicit disagreements, improving both agent performance and human collaboration.

## Practical Takeaways

- **Treat prompt craft as table stakes**: If you cannot write a clear, well-structured prompt, you are the 1998 person who cannot send email — but it will not differentiate you
- **Build personal context infrastructure**: Write a CLAUDE.md equivalent for your work with goals, constraints, communication preferences, and quality standards regardless of which AI tool you use
- **Write acceptance criteria for every delegation**: Three sentences an independent observer could use to verify output without asking any questions
- **Think of constraint architecture as failure mode prevention**: Before delegating, write down what a smart, well-intentioned person might do that would technically satisfy the request but produce the wrong outcome
- **Decompose to 2-hour subtasks**: Break projects into independently executable and verifiable components — this is the granularity at which agents work best

## Notable Quotes

> "The prompt by itself is dead. The specification, the context, the organizational intent — that is where the value in prompting is moving toward." — Nate B Jones

> "Your 200 tokens are 0.02% of what the model sees. The other 99.98% — that's context engineering." — Nate B Jones

> "If you can't describe what done looks like, an agent can't know when to stop." — Nate B Jones

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — The four-discipline framework redefines what effective prompting means
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — Organizational specification engineering and intent alignment at enterprise scale
