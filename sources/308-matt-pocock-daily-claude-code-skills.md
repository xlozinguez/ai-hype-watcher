---
source_id: "308"
title: "5 Claude Code skills I use every single day"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=EJyuu6zlQCg"
date: "2026-03-16"
duration: "16:42"
type: "video"
tags: ["claude-code", "skills", "specification", "agentic-coding", "meta-prompts", "ai-sdlc", "task-system"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "02-prompting-and-workflows"]
---

# 308: 5 Claude Code skills I use every single day

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 16:42

# 5 Claude Code Skills I Use Every Single Day

## Summary

Matt Pocock, an engineer with nearly a decade of experience, argues that working with AI coding agents requires treating them like stateless engineers who need extremely well-defined processes to produce quality output. Because agents have no memory between sessions, the developer's primary job becomes building and invoking structured "skills" — short, precisely-worded reusable prompt templates — that constrain and guide agent behavior at each stage of development. He shares a curated library of skills that have meaningfully improved the quality of AI-generated code in his workflow.

The video walks through five skills in depth: **Grill Me** (structured interview to reach shared design understanding), **Write a PRD** (convert understanding into a durable specification as a GitHub issue), **PRD to Issues** (decompose PRD into vertical-slice tasks with blocking relationships), **TDD** (enforce red-green-refactor loops for implementation), and a codebase restructuring skill (implied but transcript cuts off). Together these skills map to a complete AI-assisted SDLC: ideation → specification → task decomposition → implementation.

A key meta-insight is that skill brevity doesn't limit effectiveness — the "Grill Me" skill is just three sentences but regularly drives 30–50 question deep-dive sessions. The real leverage comes from choosing the right words at the right moment in the workflow to constrain agent behavior in useful directions.

## Key Concepts

### The Design Tree (Grill Me Skill)
Borrowed from Frederick P. Brooks' *The Design of Design*, the design tree is a framework for systematically exploring all branches of a design decision before committing to code. Each design choice opens sub-decisions (e.g., choosing "advanced search" requires deciding filters and sort methods), and the Grill Me skill forces the agent to walk the entire tree through iterative questioning. This prevents premature planning documents and ensures the developer and agent reach genuine shared understanding before writing any spec.

### Vertical Slice Task Decomposition (PRD to Issues)
Rather than breaking a PRD into horizontal layers (e.g., "do all the database work, then all the API work"), the PRD to Issues skill enforces **vertical slices** — thin tasks that cut through all integration layers at once, analogous to the "tracer bullet" pattern from *The Pragmatic Programmer*. This surfaces unknown unknowns early and keeps each task independently deliverable. The skill also establishes explicit blocking relationships between issues, enabling parallel agent execution and future extensibility.

### Interface-First TDD with Agents
The TDD skill is designed around the insight that AI agents perform poorly in codebases with many small, undifferentiated modules because they can't easily discern boundaries or responsibilities. The skill explicitly forces the agent to confirm interface changes with the user first, then design for testability at module boundaries before writing any implementation. The red-green-refactor loop is enforced programmatically because agents are reluctant to refactor code they've just written (it's still in their context window and they're "precious" about it).

### Skills as Process Encoding
Skills are reusable, composable prompt templates that encode developer process into a form agents can follow repeatably. They don't need to be long — the Grill Me skill is three sentences. The key design principle is that each skill corresponds to a specific stage in the workflow and uses precise language that predictably constrains agent behavior. Skills can be chained together (Grill Me → Write PRD → PRD to Issues → TDD) to walk an agent through an entire feature from idea to implementation.

### Stateless Agent Management
The core framing of the video is that AI coding agents should be treated as "middling to good engineers with no memory." This reframes the developer's role: less about direct code authorship, more about process design and agent steering. Because agents forget everything between sessions, all knowledge and decision context must be externalized into artifacts — PRDs, GitHub issues, skill files — that can be loaded back into context on demand. This is what makes structured workflows and specification artifacts load-bearing rather than optional.

## Practical Takeaways

- **Start with "Grill Me" before any planning.** Invoke a structured interview skill before writing specs or plans to prevent the agent from generating premature, shallow planning documents. Even for complex features, three sentences of well-chosen instruction can drive 30–50 clarifying questions.
- **Write PRDs as GitHub issues, not documents.** Storing the PRD as a GitHub issue makes it fetchable by agent loops, enables issue references in commits, and integrates naturally with blocking relationships between downstream tasks.
- **Break features into tracer-bullet vertical slices.** When decomposing a PRD into tasks, prioritize slices that prove integration feasibility first — especially when combining unfamiliar systems or services. This fails fast and validates approach before significant investment.
- **Enforce TDD to improve code quality consistently.** Red-green-refactor loops are the single most consistent lever for improving AI-generated code quality. The skill needs to be explicit about the loop because agents will skip refactoring if left to their own devices.
- **Keep skills short but precise.** Effective skills are about word choice and timing, not length. Over-engineering a skill's length can actually reduce its effectiveness if it introduces ambiguity or over-specifies behavior.

## Notable Quotes

> "Skills don't have to be long to be impactful. You've just got to choose the right words for the LLM at the right time."

> "At your fingertips now you have access to a fleet of middling to good engineers that you can deploy at any time. But the weird thing about these engineers is they have no memory. They do not remember things they've done before. And so you need extremely strict and well-defined processes to get those agents to actually do things that are useful."

> "While its own code is sitting in its own context window, it's quite reluctant to change it."
