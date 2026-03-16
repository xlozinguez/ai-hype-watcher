---
source_id: "293"
title: "Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP"
creator: "Eric Elliott"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=dj2nF5ToEyY"
date: "2026-03-12"
duration: "56:45"
type: "video"
tags: ["agentic-coding", "cursor", "multi-agent", "validation", "security", "ai-sdlc", "prompt-engineering"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 293: Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

> **Creator**: Eric Elliott | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 56:45

# Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

## Summary

Eric Elliott demonstrates new features in the AIDD (AI-Driven Development) framework during a live team training session, with a focus on a new `aid churn` command that performs automated hotspot analysis on codebases. The tool combines multiple deterministic metrics—commit churn frequency, cyclomatic complexity, information density, and lines of code—to identify files that are most likely to harbor bugs or benefit from refactoring. The session shows this hotspot analysis being run as part of a broader automated code review workflow using parallel cursor web agents.

A significant portion of the session explores the challenge of AI agents repeating the same mistakes across PRs—particularly around security patterns like timing-safe token comparisons where AI models consistently regress toward incorrect conventional wisdom. Elliott outlines a planned solution: a telemetry service that tracks recurring AI mistakes and their mitigations, feeding back into rules and agent constraints in a self-improving loop. This "AI trains itself" feedback cycle is positioned as a key competitive moat.

The session also touches on the economics of AI code review tools (Anthropic's new code review tool at ~$25/run vs. in-house approaches), the team's use of parallel sub-agents for dependency-wave workflows, and upcoming work on customizable scaffold manifests. The discussion reveals a mature, opinionated approach to AI-assisted development that prioritizes deterministic tooling alongside AI reasoning.

## Key Concepts

### Code Hotspot Analysis (`aid churn`)
The `aid churn` command performs a 90-day lookback on git commit history to identify files with high churn rates (frequent commits as a proxy for bug-fix cycles). Combined with cyclomatic complexity scores and information density measurements, it produces a prioritized list of refactoring targets. High churn alone isn't always a bug signal (new feature work also drives churn), so the multi-metric approach reduces false positives. The goal is surfacing files where complexity and instability intersect.

### Information Density as a Code Quality Metric
Density is measured by running gzip compression on source files and comparing compressed-to-uncompressed size ratios. High compressibility signals repetition—likely copy-paste code or unabstracted boilerplate. Each duplicated instance of a bug multiplies the bug count (15 copies = 15 bugs), making density a practical proxy for abstraction opportunities. This is a deterministic, language-agnostic metric that complements AI-based code review.

### Cyclomatic Complexity and Testability
Cyclomatic complexity counts the number of independent code paths through a function. Elliott targets a maximum around 9, noting that values above that create a combinatorial explosion of test cases for full coverage. The recommended mitigation is replacing nested if/else branching with keyed command dispatch tables—one entry point, one path per key—which collapses complexity and makes unit testing straightforward.

### AI Mistake Telemetry and Self-Improving Feedback Loops
A recurring AI failure mode is described: agents repeatedly regress to incorrect patterns (e.g., replacing cryptographically correct hash-based token comparison with "timing-safe" compares that compilers optimize away, reintroducing timing vulnerabilities). The proposed solution is a telemetry service logging recurring AI errors and their mitigations, which then feeds back into framework rules and agent skills automatically. More usage generates better constraints, creating a compounding improvement cycle.

### Parallel Sub-Agent Workflows
Elliott describes using Cursor web agents forked into up to four parallel sub-agents at a time. Work is structured in dependency waves: independent tasks run in parallel first, then subsequent waves build on their outputs. This pattern significantly accelerates throughput compared to sequential agentic coding while staying within manageable coordination overhead.

## Practical Takeaways

- **Use deterministic metrics alongside AI review**: Commit churn, cyclomatic complexity, and information density give you objective, reproducible signals that AI reasoning alone may miss or contradict—run them as part of every code review pipeline.
- **Cap cyclomatic complexity around 9 and prefer dispatch tables over nested conditionals**: This single refactoring pattern dramatically reduces test surface area and the probability of AI agents introducing path-specific bugs.
- **Leave explicit code comments on security-sensitive patterns AI consistently gets wrong**: Even with rules files, AI agents will regress on subtle security issues (e.g., timing-safe comparisons); inline comments saying "do not replace this" are a necessary guardrail.
- **Log AI review feedback to build a mitigations corpus**: Tracking what the AI gets wrong repeatedly—per project and per team—creates the raw material for evolving rules files and agent skills that improve automatically over time.
- **Evaluate third-party AI review tools against cost-per-run, not just quality**: At ~$25/run, high-cost review services need a clear quality delta over in-house prompt-based review to justify the spend; benchmark before committing.

## Notable Quotes

> "No matter how much what you're paying for with that $25 is just a lot of thinking, a lot of tokens, it's just talking to itself a lot for that $25. And what I found is that sometimes the more that it talks to itself the more it digs its heels in about making the same mistakes."

> "The AI trains itself as you continue to use it. So the more you use it, the better it gets just automatically in this perpetual positive feedback cycle."

> "More clutter equals more surface area for bugs equals more bugs. More places for bugs to hide."
