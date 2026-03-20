---
source_id: "321"
title: "Building a REAL feature with Claude Code: every step explained"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=hX7yG1KVYhI"
date: "2026-03-18"
duration: "44:16"
type: "video"
tags: ["claude-code", "agentic-coding", "specification", "context-engineering", "prompt-engineering", "skills"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows", "04-agentic-patterns"]
---

# 321: Building a REAL feature with Claude Code: every step explained

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-18 | **Duration**: 44:16

# Building a REAL Feature with Claude Code: Every Step Explained

## Summary

Matt Pocock demonstrates his actual development workflow using Claude Code on his production "course video manager" application (~1,200 commits, 637 closed issues). Rather than presenting a curated demo, he works through a real feature request in real time: streamlining the ghost/real lesson workflow (eliminating unnecessary two-step creation and deletion) and exploring ghost course functionality. The video is explicitly a response to audience requests for a practical, not philosophical, demonstration of his AI-assisted development approach.

The core methodology on display is treating Claude Code as a capable delegate you collaborate with rather than a tool you command. Key practices shown include: starting sessions with a "Grill Me" prompt that invites the AI to challenge requirements, using an `explore` subagent phase to read the codebase efficiently before reasoning, maintaining a ubiquitous language file to establish shared domain terminology, and using side-question mode for quick context queries that don't pollute chat history. The workflow is explicitly pre-agentic — grounding and requirement refinement happen before any code is written.

The video also illustrates the value of documenting the *why* behind features, not just the *what*. Pocock shows how explaining intent (e.g., "I want ghost courses so I can plan freely without committing to a file system shape") enables Claude to surface contradictions in the requirements, propose alternatives, and ask clarifying questions — something it cannot do when given only a feature specification without motivation.

## Key Concepts

### The "Grill Me" Prompt Pattern
A structured prompt that instructs Claude Code to challenge the user's framing before producing a spec or plan. It triggers an `explore` phase (a subagent that reads relevant files and returns a summary to the parent context), then asks pointed questions that surface gaps or contradictions. Pocock uses this to produce a Product Requirements Document (PRD) that hardens vague ideas into precise, implementable specs before any coding begins.

### Explore Phase as Token-Efficient Context Loading
When Claude Code invokes `explore`, it spins up a subagent with its own context window to read many files in parallel, then returns only a distilled summary to the parent agent. This allows comprehensive codebase understanding without exhausting the parent agent's context budget — particularly valuable on mature codebases with thousands of files.

### Ubiquitous Language File (Domain-Driven Design Applied to AI Pairing)
Inspired by Eric Evans' *Domain-Driven Design*, Pocock maintains a file containing precise definitions of all domain terms used in the codebase (e.g., "ghost lesson: a lesson that exists in the database but not yet on the file system"). This file serves as shared vocabulary between the developer (domain expert) and the LLM (developer), enabling precise communication and preventing semantic drift across sessions.

### Why-First Requirement Framing
Providing the *reason* behind a feature request — not just the desired behavior — enables Claude to act as a genuine design collaborator. When Pocock explains *why* he wants ghost courses (to plan without committing to a file system shape), Claude can ask whether "ghost lesson inside ghost course" is even a coherent concept given the system's constraints, something it could not do with only a feature description.

### Side-Question Mode for Context Queries
A Claude Code interaction mode for quick, isolated questions (e.g., "describe the shape of the course write service") that do not enter the main conversation history. This keeps the primary planning thread clean while allowing the developer to build understanding on demand — useful when orienting in an unfamiliar part of a large codebase.

## Practical Takeaways

- **Start every feature session with a Grill Me pass, not a build pass.** Use Claude's explore capability to read the codebase, then have it challenge your requirements before writing a single line of code. This surfaces UI gaps (like "delete real lesson" existing in the service but not exposed in the UI) that would otherwise waste build time.
- **Maintain a ubiquitous language file.** A living glossary of domain terms significantly improves cross-session consistency and forces you to articulate implicit assumptions that the LLM would otherwise have to guess at.
- **Always explain the "why" alongside the "what."** Without motivation, Claude optimizes for the literal request. With motivation, it can propose better alternatives, flag contradictions, and ask clarifying questions that sharpen the spec.
- **Use side-question mode liberally to orient yourself.** On large codebases, quick isolated queries to understand a service or module are cheaper (in context and cognitive overhead) than reading code manually or embedding the question in the main planning thread.
- **Treat the PRD as a session artifact, not a formality.** The output of a Grill Me session is a document that feeds future build sessions. Investing time in requirement refinement upfront amortizes across all subsequent coding sessions on that feature.

## Notable Quotes

> "You get the most out of it when you treat it like someone you would delegate to in your team. In other words, you focus on the architecture, you focus on making sure that you've got good feedback loops — you focus on all the things we've been doing for the last 20 years."

> "I'm the domain expert and the LLM is the dev. And we need some kind of shared language so that we can talk together precisely."

> "If the LLM has the what, then it understands what you want to build. But if it doesn't know the why, then it can't suggest alternatives."
