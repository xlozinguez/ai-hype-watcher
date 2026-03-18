---
source_id: "308"
title: "5 Claude Code skills I use every single day"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=EJyuu6zlQCg"
date: "2026-03-16"
duration: "16:42"
type: "video"
tags: ["claude-code", "skills", "agentic-coding", "specification", "meta-prompts", "ai-sdlc", "prompt-engineering", "context-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "02-prompting-and-workflows"]
---

# 308: 5 Claude Code skills I use every single day

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 16:42

# 5 Claude Code Skills I Use Every Single Day

## Summary

Matt Pocock, a software engineer with nearly a decade of experience, argues that as AI coding agents become central to development workflows, **process design becomes the critical skill**. Because AI agents have no persistent memory, developers must encode their processes into reusable "skills" (structured prompt templates) that guide agent behavior consistently. Pocock shares five skills he uses daily, demonstrating how well-designed prompts — even very short ones — can dramatically improve code quality and agent output.

The video walks through a complete development workflow: from exploring an idea ("Grill Me"), to formalizing it ("Write a PRD"), to decomposing it into actionable work ("PRD to Issues"), and finally to executing it with high code quality ("TDD"). Each skill encodes developer intuition — design tree exploration, vertical slicing, red-green-refactor — into reusable instructions that compensate for the agent's lack of memory and accumulated judgment. The skills also reflect a deeper philosophy: codebase architecture (large modules with thin interfaces) makes AI-assisted development significantly more tractable.

A recurring theme is that **skills need not be long to be powerful**. The "Grill Me" skill is just three sentences yet can drive 45-minute design sessions with 30–50 targeted questions. The value is in choosing the right words at the right moment to steer the agent down a well-defined path.

## Key Concepts

### The "Grill Me" Skill — Design Tree Exploration
A three-sentence skill that instructs Claude to "interview me relentlessly about every aspect of this plan until we reach a shared understanding," walking down each branch of the design tree and resolving dependencies one by one. Rooted in Frederick Brooks' concept of the design tree, this forces the LLM to surface all ramifications of a design decision before any code is written. Where Claude in plan mode tends to prematurely generate plans, this skill enforces a genuine back-and-forth dialog — Pocock has experienced sessions of 30–50 questions on complex features.

### PRD-First Workflow with GitHub Issues
After shared understanding is reached, a "Write a PRD" skill formalizes the design into a Product Requirements Document submitted as a GitHub issue. The PRD captures user stories and high-level implementation decisions without being overprescriptive (to remain durable as code evolves). A follow-on "PRD to Issues" skill then decomposes the PRD into **vertical slices** — thin tasks that cut through all integration layers rather than horizontal layers — establishing blocking relationships between them. This kanban structure enables parallel agent execution and rapid discovery of unknown unknowns.

### Vertical Slicing and Tracer Bullets
Borrowing the "tracer bullet" concept, Pocock's decomposition approach prioritizes tasks that validate integration feasibility first. If a new service integration or novel cross-cutting concern is part of a feature, that work comes first — its success or failure gives early feedback on whether the overall approach is valid. This is contrasted with horizontal slicing (building one layer completely before the next), which delays integration feedback.

### TDD Skill — Red-Green-Refactor Loop for Agents
The TDD skill enforces a structured loop: confirm interface changes with the user, design interfaces for testability, then cycle through writing one failing test at a time, writing code to pass it, and looking for refactor candidates. Pocock identifies TDD as "the most consistent way I've improved agent outputs." He notes that agents are reluctant to refactor code still in their context window (they're "precious" about it), but the skill still enforces the discipline. TDD is most effective when the codebase has clear module boundaries with thin interfaces.

### Codebase Architecture as an AI Force Multiplier
Underpinning all skills is a structural principle: codebases with large, well-bounded modules and thin exported interfaces are dramatically easier for AI agents to navigate and test. In a fragmented codebase of many small undifferentiated modules, agents struggle to understand dependencies and test boundaries. Restructuring into deep modules with clear interfaces lets agents test at boundaries, reduces context needed to reason about the code, and makes all the above skills more effective. Pocock has a dedicated "improve codebase" skill (briefly mentioned) to drive this restructuring.

## Practical Takeaways

- **Short, precise skills beat long instructions.** The three-sentence "Grill Me" skill can generate 45 minutes of structured design questioning — word choice at the right moment matters more than volume.
- **Encode your workflow sequentially.** Stack skills in order: Grill Me → Write PRD → PRD to Issues → TDD. Each hands off structured context to the next, maintaining coherence across a no-memory agent.
- **Use vertical slices, not horizontal layers.** Break PRDs into tasks that flush out unknown unknowns quickly by cutting through all integration layers — this is where the tracer bullet analogy is most actionable.
- **Structure your codebase for AI legibility.** Deep modules with thin interfaces make testing boundaries obvious and reduce the cognitive load on agents navigating the repo; this amplifies the effectiveness of TDD and all other skills.
- **Blocking relationships between issues enable parallelism.** Tracking which issues block others lets you fire multiple agents simultaneously on independent slices, and keeps future QA issues properly sequenced.

## Notable Quotes

> "At your fingertips now you have access to a fleet of middling to good engineers that you can deploy at any time. But the weird thing about these engineers is they have no memory. They do not remember things they've done before. And so you need extremely strict and well-defined processes to get those agents to actually do things that are useful."

> "Skills don't have to be long to be impactful. You've just got to choose the right words for the LLM at the right time."

> "TDD has been the most consistent way that I've improved agents' outputs."
