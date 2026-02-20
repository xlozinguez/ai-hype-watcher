---
source_id: "103"
title: "Inside Claude Code With Its Creator Boris Cherny"
creator: "Y Combinator"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=PQU9o_5rHC4"
date: "2026-02-17"
duration: "50:11"
type: "video"
tags: ["claude-code", "anthropic", "agentic-coding", "ai-landscape", "context-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "01-foundations"]
---

# 103: Inside Claude Code With Its Creator Boris Cherny

> **Creator**: Y Combinator | **Platform**: YouTube | **Date**: 2026-02-17 | **Duration**: 50:11

## Summary

Boris Cherny, the creator of Claude Code, sits down with Y Combinator partners for an extensive conversation covering the origin story, design philosophy, and future direction of Claude Code. The interview reveals that Claude Code started as a simple terminal chat app built to learn the Anthropic API -- the CLI form factor was an accident born of laziness ("I didn't have to build a UI"), not a deliberate design choice. The tool gained internal traction organically when colleagues started using the prototype within days of its creation.

The conversation is dense with product philosophy and concrete operational detail. Key revelations include: Anthropic's CLAUDE.md is only two lines long (enable auto-merge, post PRs to Slack), plan mode was built in 30 minutes on a Sunday night based on latent demand, the Claude Code plugins feature was entirely built by an agent swarm over a weekend with no human intervention, and productivity per engineer at Anthropic has grown 150% since Claude Code's introduction. Cherny's core advice for builders: build for the model six months from now, never bet against the model, and treat all product scaffolding as temporary tech debt that the next model will eliminate.

## Key Concepts

### Latent Demand as the Core Product Principle

Every major Claude Code feature emerged from observing what users were already trying to do. Plan mode came from users telling Claude "don't code yet." CLAUDE.md came from users writing markdown files and having the model read them. Cowork came from non-technical employees jumping through hoops to install a terminal tool. Cherny calls latent demand "the single biggest idea in product" -- you cannot get people to do new things, only make what they already do easier.

### Build for the Model Six Months From Now

Anthropic's core product philosophy: do not optimize for current model capabilities. Build for where the model will be. The reason is competitive -- if you find product-market fit for today's model, you get leapfrogged by someone building for the next model, which ships every few months. This explains why Claude Code stayed in the terminal: "we felt there is no UI we could build that would still be relevant in 6 months because the model was improving so quickly."

### Scaffolding as Temporary Tech Debt

Product scaffolding -- code written to compensate for model limitations -- provides 10-20% performance gains but gets "wiped out with the next model." The Bitter Lesson (Sutton) hangs framed on the Claude Code team's wall: never bet against the model. CLAUDE.md itself is scaffolding; Cherny recommends deleting it and starting fresh with each model upgrade, adding back instructions only when the model gets off track.

### The Terminal as Accidental Design Constraint

Claude Code's terminal form factor was not a principled choice but an accident that worked. The constraint (80x100 characters, 256 colors, no mouse, one font) forced novel UX decisions. The spinner alone went through 50-100 iterations. The terminal proved surprisingly durable -- Cherny predicted a three-month lifespan but has been repeatedly wrong about when it would be replaced.

### Coding Is Practically Solved

Cherny claims coding is "practically solved" for him personally -- he uninstalled his IDE and lands ~20 PRs per day using only Claude Code with Opus. At Anthropic, 70-90% of code is AI-generated depending on the team. The prediction: the title "software engineer" will evolve into something more like "builder" or "product manager" as coding becomes one of many generalist skills rather than a specialist discipline.

## Practical Takeaways

- **Keep CLAUDE.md minimal**: Cherny's personal CLAUDE.md is two lines. The team's is a couple thousand tokens. If yours is bloated, delete it and start fresh -- add instructions back only when the model demonstrably goes off track.
- **Use plan mode for 80% of sessions**: Even as its inventor predicts plan mode has "a limited lifespan," Cherny starts 80% of sessions in plan mode, opening multiple parallel tabs to generate plans simultaneously.
- **Calibrate sub-agent count to task difficulty**: For hard research or debugging tasks, explicitly request 3, 5, or even 10 sub-agents to research in parallel. For simple tasks, one is enough.
- **Watch how the model wants to use tools**: The best product insights come from observing what the model tries to do unprompted -- the same principle applies to prompt engineering and skills design.
- **Hire for beginner's mindset and ability to be wrong**: The most effective engineers are either hyper-specialists or hyper-generalists who "do weird stuff." The key interview question: "Tell me about a time you were wrong."
- **Evaluate engineers by their Claude Code transcripts**: YC is experimenting with this approach -- transcripts reveal whether someone understands systems, uses plan mode, catches errors, and thinks about testing.

## Notable Quotes

> "We don't build for the model of today. We build for the model six months from now." — Boris Cherny

> "There is no part of Claude Code that was around six months ago. It's just constantly rewritten." — Boris Cherny

> "Plan mode... all it does is it adds one sentence to the prompt that's like please don't code. That's all it is." — Boris Cherny

> "The model just wants to use tools. That's all it wants." — Boris Cherny

> "Half my ideas are bad and you just have to try stuff... this is the skill that I think in the past was very important for founders, but now I think it's very important for every engineer." — Boris Cherny

> "Since Claude Code came out, productivity per engineer at Anthropic has grown 150%." — Boris Cherny

## Related Sources

- [024: You are Not Ready: Agentic coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) — Van Eyck's agentic coding overview that Cherny's insights operationalize
- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) — Skills system as scaffolding that Cherny predicts models will eventually internalize
- [040: Stop Feeding Claude Your Entire CLAUDE.md](040-charlie-automates-claudemd-context.md) — Charlie Automates' CLAUDE.md optimization advice aligns with Cherny's "delete and start fresh" recommendation
- [056: Dario Amodei Interview](056-dwarkesh-patel-dario-amodei-interview.md) — Amodei's vision of AI trajectory that Cherny is operationalizing in product form
- [070: Handoff Drift — Why Anthropic PMs Vibe Code](070-dhyey-mavani-handoff-drift.md) — The organizational shift Cherny describes where "everyone codes"

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md philosophy, plan mode mechanics, and minimal configuration approach
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Sub-agent calibration, plan-then-execute workflow, and agent swarm for feature development
- [Module 01: Foundations](../curriculum/01-foundations/README.md) — The Bitter Lesson, building for future model capabilities, and the "coding is solved" thesis
