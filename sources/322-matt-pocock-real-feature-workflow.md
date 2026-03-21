---
source_id: "322"
title: "Building a REAL feature with Claude Code: every step explained"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=hX7yG1KVYhI"
date: "2026-03-18"
duration: "44:16"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "specification", "agentic-coding", "prompt-engineering"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows", "04-agentic-patterns"]
---

# 322: Building a REAL feature with Claude Code: every step explained

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-18 | **Duration**: 44:16

# Building a REAL Feature with Claude Code: Every Step Explained

## Summary

Matt Pocock walks through a live, unscripted Claude Code session on his production "course video manager" application (~1,200 commits, 637 closed issues), demonstrating how he actually uses AI-assisted development in real work rather than toy examples. The goal is to show practical technique: how he formulates vague requirements, uses a "Grill Me" skill to interrogate and harden ideas, and progressively refines a feature specification through dialogue with Claude Code. The session covers two related feature requests — streamlining ghost/real lesson creation and deletion, and introducing the concept of "ghost courses" — showing how ambiguous product ideas get sharpened through structured AI conversation.

A central theme is that the skills that made developers effective before AI still matter most: focusing on architecture, maintaining tight feedback loops, not over-planning upfront, and treating the LLM as a team member you delegate to rather than a magic oracle. Pocock also demonstrates concrete workflow patterns like the "Grill Me" skill (which generates a PRD through Socratic questioning), the "by the way" side-query mechanism (an ephemeral question that doesn't pollute chat history), and the use of subagents for token-efficient codebase exploration.

The session also surfaces domain-driven design concepts applied to AI collaboration — specifically maintaining a "ubiquitous language" glossary so the LLM and developer share precise terminology. This bridges the gap between the developer-as-domain-expert and the LLM-as-implementer, enabling more precise specifications and better alternative suggestions from the model.

## Key Concepts

### The "Grill Me" Skill for PRD Generation
Rather than writing a specification document upfront, Pocock dictates rough, half-formed ideas to Claude Code via a custom "Grill Me" skill. The skill triggers an explore phase (a subagent reads the codebase and returns a summary), then enters Socratic dialogue — challenging assumptions, exposing ambiguities, and forcing the developer to clarify the "why" behind each feature, not just the "what." The output is a hardened Product Requirements Document (PRD) that can guide future build sessions. This replaces the trap of over-specifying upfront or under-specifying entirely.

### Subagent Explore Phase for Token Efficiency
Claude Code's `explore` invocation spawns a sub-agent that reads large swaths of the codebase, then returns only a compressed summary to the parent agent. This allows deep codebase understanding without exhausting the parent context window. Pocock describes this as "getting a lot of juice" from exploration cheaply — a key technique for working on mature, complex codebases where naively loading all files would be prohibitively expensive.

### "By the Way" Side Queries (Ephemeral Questions)
A workflow pattern where quick, clarifying questions are asked of Claude Code in a mode that doesn't enter the main chat history. Pocock uses this to get a description of the `CourseWriteService` without polluting the ongoing Grill Me session with that tangent. This preserves context discipline — keeping the main conversation focused while still satisfying curiosity or verifying assumptions on the fly.

### Ubiquitous Language as Shared Developer-LLM Vocabulary
Drawing from Domain-Driven Design, Pocock maintains a glossary file ("ubiquitous language") in his repo that defines precise terms like "ghost lesson" (exists in the database but not on the file system) and "real lesson." This file is discoverable by Claude Code during exploration, ensuring the LLM uses terminology consistently with the developer. The analogy: the developer is the domain expert, the LLM is the implementer — they need shared language for precise communication and so the LLM can suggest meaningful alternatives.

### Well-Tested Codebases as AI Force Multipliers
Pocock's `CourseWriteService` has comprehensive end-to-end tests that spin up a real test database and a temporary git repo. He notes this makes the feature build "relatively simple" because the feedback loop is tight and regressions are caught automatically. A mature test suite isn't just a quality gate — it's infrastructure that makes AI-assisted changes safer and faster, letting Claude Code make bolder edits with confidence. This reinforces the core philosophy: existing software engineering discipline amplifies AI effectiveness.

## Practical Takeaways

- **Always explain the "why" to the LLM, not just the "what."** Without the motivation behind a feature, the model can't suggest better alternatives or flag when your proposed solution doesn't match your actual goal. Rough, honest rationale ("I hate having to commit to a file system shape before I know if I want the course") is more useful than polished requirements.

- **Use a Grill Me / Socratic PRD pattern before coding.** Entering a dialogue where the LLM challenges your framing surfaces hidden assumptions early (e.g., "what does 'real' mean for a lesson inside a ghost course that has no file system?"). This is far cheaper than discovering the ambiguity mid-implementation.

- **Keep ephemeral questions out of main context.** Side-query mechanisms (or just opening a separate conversation) prevent tangential investigations from degrading the signal-to-noise ratio of your primary session. Context discipline is an active practice, not a default.

- **Maintain a ubiquitous language file in your repo.** A glossary of domain terms that Claude Code can discover during exploration dramatically reduces miscommunication across sessions, especially in large codebases where terminology is non-obvious. Treat it as living documentation.

- **Invest in integration tests that mirror production conditions.** Tests that use real databases and real file system interactions give Claude Code a reliable oracle for verifying changes, enabling more autonomous operation with less manual review per change.

## Notable Quotes

> "You get the most out of it when you treat it like someone you would delegate to in your team. In other words, you focus on the architecture, you focus on making sure that you've got good feedback loops, you focus on all the things we've been doing for the last 20 years."

> "I'm the domain expert and the LLM is the dev. And we need some kind of shared language so that we can talk together precisely."

> "Notice how rough this is. This is just a super hashed out sort of idea that I'm kind of, you know, just spewing out to the LLM and making it do all the work."
