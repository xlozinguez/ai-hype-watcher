---
source_id: "440"
title: "I Hated Every Coding Agent, So I Built My Own — Mario Zechner (Pi)"
creator: "Mastra"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Dli5slNaJu0"
date: "2026-03-31"
duration: "27:15"
type: "video"
tags: ["agentic-coding", "context-engineering", "claude-code", "ai-landscape", "security"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "06-strategy-and-economics"]
---

# 440: I Hated Every Coding Agent, So I Built My Own — Mario Zechner (Pi)

> **Creator**: Mastra | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 27:15

# I Hated Every Coding Agent, So I Built My Own — Mario Zechner (Pi)

## Summary

Mario Zechner, a veteran open source developer with a game development background, chronicles his journey through the landscape of AI coding agents — from copy-pasting ChatGPT responses to Claude Code to building his own tool called Pi. He frames his dissatisfaction not as hostility toward existing tools but as a mismatch with his specific needs: predictability, deep observability, stable context management, and extensibility. His critique is grounded in technical specifics rather than vibe — he intercepted Claude Code's backend requests to audit injected context, analyzed OpenCode's storage architecture, and articulates precisely why LSP integration mid-edit produces bad model behavior.

The talk offers a rare practitioner-level audit of the major coding agent tools circa 2025: Claude Code (powerful but opaque and rapidly changing), Codex CLI (improved but early friction), AMP (unusually disciplined in subtracting features), Factory (stable but less experimental), and OpenCode (grounded team, but architectural decisions around prompt caching abuse and per-message JSON storage raised red flags). Mario's baseline criterion is control — over context, over model choice, over what gets injected into prompts — and he found that none of the existing tools gave him enough of it.

The talk is a case study in how expert developers evaluate agentic tooling: not by feature count but by the reliability of the control surface, the stability of the tool's behavior across updates, and whether the tool's design philosophy aligns with how the developer thinks about code quality and workflow.

---

## Key Concepts

### Context Engineering as the Central Battleground

Mario argues that the real differentiator between good and bad coding agents is how they manage context — what gets injected, when, and whether the developer can see and control it. He built custom tooling to intercept Claude Code's backend requests and discovered undocumented context injections that changed daily. OpenCode's `session compaction prune` strategy — pruning tool results before the last 40,000 tokens — destroys prompt cache effectiveness. Both examples illustrate that invisible context manipulation is a first-class failure mode, not a minor annoyance.

### LSP Integration as an Anti-Pattern Mid-Edit

OpenCode's built-in Language Server Protocol support injects compiler/type errors directly after each tool call. Mario explains why this is counterproductive: when an agent is making 10 sequential edits to multiple files, the code won't compile cleanly after edit 1 or 2 — that's expected and correct behavior. Surfacing errors at each intermediate step confuses the model, which interprets feedback as criticism of a completed action rather than an in-progress state. His preferred pattern: lint and type-check only at natural synchronization points, when the agent believes it is done.

### Tool Stability vs. Rapid Iteration Tension

A recurring theme is the tension between a tool vendor's need to experiment with a large user base and a power user's need for stable, predictable behavior. Mario describes how daily or every-other-day Claude Code releases would change what context got injected and when — breaking carefully constructed workflows without notice. He acknowledges the structural reason (large user base, rapid product iteration) while arguing it makes Claude Code unsuitable as a foundation for reliable professional workflows.

### Subtractive Design as a Signal of Maturity

Mario highlights AMP as the standout commercial option precisely because it removes features rather than adds them. In a space where every tool is racing to add capabilities, a team that deliberately constrains scope signals architectural discipline and a clearer mental model of what the tool should do. This is presented as a heuristic for evaluating agentic tooling: feature restraint in a hypergrowth market is a credibility signal.

### The Architecture Tells You What the Team Values

Mario uses two OpenCode observations as architectural tea-leaf reading: (1) every session message being written as its own JSON file on disk suggests the storage model wasn't designed with scale or coherence in mind; (2) a default-on server with a remote code execution vulnerability left open for an extended period suggests security wasn't a first-class design concern. His argument is that architectural choices reveal team priorities — and if those priorities don't match yours, use a different tool.

---

## Practical Takeaways

- **Audit what your coding agent injects into context.** If you're on Claude Code or similar, consider intercepting requests to understand what system-level text is being added to your prompts — it may be changing frequently and undermining your workflows without your knowledge.

- **Disable LSP / real-time linting during agentic edits.** Only run lint, type checking, and compilation checks at natural completion checkpoints — not after each intermediate file edit. Mid-edit errors mislead the model about the state of the task.

- **Evaluate tools by what they remove, not what they add.** AMP's subtractive design philosophy is a useful counterexample to the feature-bloat trend. When assessing a new coding agent, ask: what does this tool deliberately not do, and is that restraint principled?

- **Treat prompt cache health as infrastructure.** Strategies like OpenCode's aggressive context pruning that destroy cache prefixes have real cost and latency implications. Understand how your agent interacts with prompt caching before adopting it at scale.

- **Prefer tools with stable, inspectable behavior over tools with maximum features.** For professional workflows, a coding agent you can reason about and predict is more valuable than one with extensive capabilities that change under the hood constantly.

---

## Notable Quotes

> "Cloud code was not a good tool when it comes to observability and actually managing your context... every day or second day there would be a new release where this changed what gets injected at what point, which would basically mess with your existing workflows."

> "I built a bunch of tools in summer 2025 that would allow me to intercept requests being made to their backend from cloud code and finding out what kind of little additional text gets injected into your context behind your back."

> "AMP managed to build a commercial coding harness where they take away features instead of adding them — and most of the choices make a lot of sense to me."

---
