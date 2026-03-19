---
source_id: "321"
title: "Building a REAL feature with Claude Code: every step explained"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=hX7yG1KVYhI"
date: "2026-03-18"
duration: "44:16"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "specification", "prompt-engineering", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows", "04-agentic-patterns"]
---

# 321: Building a REAL feature with Claude Code: every step explained

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-18 | **Duration**: 44:16

# Building a REAL Feature with Claude Code: Every Step Explained

## Summary

Matt Pocock demonstrates his actual Claude Code workflow on a real production project—a 1,200-commit personal course video manager built with React Router, TypeScript, Drizzle ORM, and PostgreSQL. Rather than presenting polished theory, he records himself mid-work on a genuine feature request: streamlining the ghost/real lesson distinction so users can create real lessons directly (skipping the ghost-first ceremony) and delete real lessons without first converting them to ghosts. He also introduces a new concept—"ghost courses"—as a second feature to explore in the same session.

The core methodology on display is the "Grill Me" skill: submitting rough, unpolished requirements to Claude Code and letting it interrogate the framing, surface UI gaps the developer hadn't noticed, and sharpen vague language into precise product requirements. Pocock walks through every decision point—whether to combine features into one PRD or separate them, how much context to give the LLM, when to explain *why* not just *what*—narrating his reasoning in real time.

A secondary thread throughout the video is the importance of ubiquitous language (borrowed from Domain-Driven Design): maintaining a shared glossary between developer and LLM so that domain concepts like "ghost lesson" or "materialize" mean exactly the same thing in every conversation, reducing ambiguity and improving the precision of AI-generated code.

## Key Concepts

### The "Grill Me" Skill
Pocock's primary tool for requirements hardening. Instead of writing a detailed spec upfront, he dictates rough, stream-of-consciousness requirements and invokes the Grill Me skill, which prompts Claude Code to challenge his framing, ask clarifying questions, and surface gaps. The output is a product requirements document (PRD) that is far more precise than what he would have written alone. The key insight is that the LLM's interrogation replaces the expensive cognitive work of pre-planning—it finds the holes for you.

### Explore Phase and Sub-Agent Token Efficiency
Claude Code's `explore` phase works by spinning up a sub-agent to read large portions of the codebase, then returning only a summary to the parent agent. This keeps the parent context window lean while still providing the parent with the code understanding it needs. Pocock uses this deliberately, stepping away while the explore phase runs and treating the summary as the raw material for subsequent prompts.

### Ubiquitous Language as LLM Interface Contract
Drawing from Domain-Driven Design, Pocock maintains a "ubiquitous language" file in his repo that defines precise terms (e.g., "ghost lesson," "materialize"). This file serves a dual purpose: it aligns the LLM's vocabulary with the developer's domain knowledge, and it acts as a discoverable reference the LLM can retrieve during explore phases. When the LLM searches for "ghost lessons," it encounters these definitions and can reason about domain concepts accurately rather than inferring them from code patterns alone.

### Why > What in LLM Prompting
Pocock explicitly pauses mid-dictation to add the *reason* for the ghost courses feature—not just what he wants, but why (planning courses without committing to a file system shape). He notes that without the "why," the LLM can generate what was asked but cannot suggest alternatives or push back on the framing intelligently. The "why" is what enables the LLM to act as a collaborative thinking partner rather than a pure executor.

### PRD as Session Artifact
Each Grill Me session produces a PRD that becomes the input for future build sessions. Pocock treats the decision of what to include in a single PRD as an architectural question in itself—are these features the same concern or separate concerns? Bundling them produces one reusable planning document; splitting them produces two. This deliberate scoping of PRDs reflects the same planning discipline he'd apply to any team delegation.

## Practical Takeaways

- **Start sessions with rough intent, not polished specs.** Dictate what you want and why in natural language, including uncertainty ("I'm not sure about that flow—maybe we can work on that together"). The LLM's interrogation phase will sharpen the requirements.
- **Always explain the "why" alongside the "what."** This enables the LLM to challenge your framing, suggest alternatives, and catch contradictions—functions that are impossible if the LLM only knows the desired output.
- **Maintain a ubiquitous language file in your repo.** Define domain terms precisely and keep this file discoverable. It dramatically reduces drift between your mental model and the LLM's understanding across sessions.
- **Use the "by the way" / side-question feature for quick context checks** without polluting chat history. Asking the LLM to describe a service's shape before prompting it to modify that service costs little and prevents misaligned edits.
- **Treat the LLM like a team member you're delegating to, not a code generator.** Focus your energy on architecture, feedback loops, and requirements clarity—the same skills that made developers effective before AI tools.

## Notable Quotes

> "You get the most out of it when you treat it like someone you would delegate to in your team. In other words, you focus on the architecture, you focus on making sure that you've got good feedback loops."

> "If the LLM has the what, then it understands what you want to build. But if it doesn't know the why, then it can't suggest alternatives."

> "Notice how rough this is. This is just a super hashed out sort of idea that I'm kind of, you know, just spewing out to the LLM and making it do all the work."
