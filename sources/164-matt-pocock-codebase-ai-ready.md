---
source_id: "164"
title: "Your codebase is NOT ready for AI (here's how to fix it)"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=uC44zFz7JSM"
date: "2026-02-26"
duration: "8:50"
type: "video"
tags: ["agentic-coding", "context-engineering", "ai-sdlc"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 164: Your codebase is NOT ready for AI (here's how to fix it)

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-02-26 | **Duration**: 8:50

## Summary

Matt Pocock argues that codebase design is the single biggest influence on AI coding output — more than prompts, more than agent configuration files. Most codebases are not structured for AI because they consist of shallow, highly interconnected modules that are difficult for a stateless agent to navigate.

His central thesis draws from John Ousterhout's "A Philosophy of Software Design" and the concept of deep modules: large chunks of implementation behind simple interfaces. Pocock extends this idea by treating these modules as "graybox modules" where humans design the interfaces and write tests, while AI handles the internal implementation. This maps directly to the idea that AI is a perpetual new starter with no memory of the codebase.

## Key Concepts

### Deep Modules for AI Navigation

Drawing from "A Philosophy of Software Design," Pocock advocates replacing many small, shallow modules with fewer deep modules — large implementations controlled by simple interfaces. When each module lives in its own folder with a clear public API, AI agents can progressively discover the codebase: read the interface first, understand what a module does, and only dive into implementation when needed.

### Graybox Modules and the Human-AI Boundary

Deep modules become "graybox modules" — the developer designs the interface and writes tests that lock down behavior, while AI manages the internal implementation. The developer can look inside if needed (to apply taste, improve performance), but as long as tests pass, the internals are delegated. This creates a natural seam between human judgment and AI execution.

### AI as a Perpetual New Starter

AI agents have no memory of your codebase. Every session is like onboarding a new developer. This reframes codebase quality as an onboarding problem: if the file system doesn't match the mental map of the codebase, AI will struggle to find things, understand relationships, and run tests. The same 20-year-old software practices that help human new starters — clear boundaries, good tests, navigable structure — are exactly what AI needs.

## Practical Takeaways

- **Restructure around deep modules**: Replace webs of small interconnected files with bounded services that have simple, well-typed interfaces. This enables progressive disclosure of complexity for AI agents.
- **Design interfaces first, delegate implementation**: Every coding session should start by thinking about which modules are affected and how interfaces will change. Let AI handle the internals, locked down by tests.
- **Make the file system match the mental map**: If your codebase has implicit groupings that aren't reflected in the directory structure, AI cannot see them. Enforce the map structurally.
- **Invest in tests as AI feedback loops**: Tests are essential for AI agents just as they are for new starters — they provide the fast feedback that tells the agent whether its changes had the intended effect.

## Notable Quotes

> "Your codebase, way more than the prompt that you used, way more than your agents.mmd file, is the biggest influence on AI's output." — Matt Pocock

> "AI when it jumps into your codebase, it has no memory. It has not experienced your codebase before. It's like the guy from Memento who just steps in and goes, okay, I'm here, what am I doing?" — Matt Pocock

> "We need to stop thinking about AI as like this superpowered developer and understand that it's got some weird limitations. And the limitations that it has are that it's a new starter in your codebase." — Matt Pocock

## Related Sources

- [163: Addy Osmani — Vibe Coding vs Reality](163-addy-osmani-vibe-coding-reality.md) — Both address the gap between AI coding hype and the engineering discipline required

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Codebase structure as context for AI workflows
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Deep modules as architectural pattern for agent delegation
