---
source_id: "293"
title: "Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP"
creator: "Eric Elliott"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=dj2nF5ToEyY"
date: "2026-03-12"
duration: "56:45"
type: "video"
tags: ["agentic-coding", "multi-agent", "cursor", "claude-code", "security", "ai-sdlc", "prompt-engineering", "validation"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 293: Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

> **Creator**: Eric Elliott | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 56:45

# Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

## Summary

Eric Elliott demonstrates new tooling built into the AIDD (AI-Driven Development) framework, with a focus on the `aid churn` command — a code hotspot analysis tool that combines cyclomatic complexity, commit frequency ("churn"), line count, and information density metrics to identify files most in need of refactoring. The session shows how deterministic, measurable code quality signals can be fed into AI-assisted workflows to produce targeted, actionable refactoring recommendations rather than relying on broad AI judgment alone.

A significant portion of the discussion covers the challenge of AI agents repeating the same mistakes across PRs — particularly a concrete security example where agents persistently replace secure constant-time hash comparisons with vulnerable timing-safe-but-not-actually-timing-safe token comparisons. The team discusses building a telemetry service to track recurring AI mistakes and automatically feed mitigations back into project rules, creating a self-improving feedback loop where the AI system learns from its own errors over time.

The session also introduces the concept of multi-agent parallelism via Cursor web agents (up to four concurrent sub-agents), where dependency chains can be mapped so parallel waves of agents build on each other's outputs — and touches on how the team plans to use semantic indexing of mistake logs to systematically improve RAG strategies for their AI development workflows.

## Key Concepts

### Code Hotspot Analysis (`aid churn`)
The `aid churn` command is a deterministic refactoring-target tool that scores files across four signals: **commit churn** (number of commits to a file in the last 90 days, indicating bug-fix cycling), **cyclomatic complexity** (number of independent code paths, where higher values make testing combinatorially harder), **line count** (code surface area as a proxy for bug-hiding potential), and **information density** (gzip compression ratio as a repetition/copy-paste detector). Files that score poorly across multiple signals become prioritized refactoring targets. This approach gives AI agents concrete, measurable anchors rather than asking them to make subjective quality judgments.

### Cyclomatic Complexity Reduction via Command Dispatch
Rather than deeply nested `if/else` branching, the recommended pattern is to route logic through a keyed command dispatch (e.g., a switch/lookup table), which reduces cyclomatic complexity to near-linear paths. Each path can then be unit-tested independently, eliminating the combinatorial explosion of test cases required to cover nested conditional logic. This is a structural refactoring target the `aid churn` command surfaces automatically.

### Information Density as a Code Quality Metric
By running gzip compression on a source file and comparing compressed-to-uncompressed size ratios, the tool estimates how much repetition exists in the code. High compressibility suggests copy-pasted boilerplate or missed abstraction opportunities — each duplicated instance of a buggy pattern multiplies the bug count. Low density scores flag candidates for abstraction into callable functions, reducing both maintenance burden and bug surface area.

### AI Mistake Telemetry and Self-Improving Feedback Loops
A recurring problem in AI-assisted development is that agents repeat the same class of mistakes across sessions and PRs — the timing-safe token comparison example illustrates how even explicit rules and code comments don't fully prevent regressions. The proposed solution is a telemetry service that logs recurring AI errors and auto-generates mitigations (new rules, constraints, epic tasks) back into the project's AI configuration. Combined with tools like Claude Code's built-in `insights` command, this creates a compounding feedback loop: the longer a team uses the system, the better it gets at catching its own failure modes.

### Parallel Sub-Agent Workflow with Dependency Waves
Cursor web agents support forking up to four concurrent sub-agents. The practical pattern is to map the dependency graph of a task, assign independent work to the first wave of agents, and then launch a second wave that builds on the first wave's outputs. This mirrors how human engineering teams parallelize work across dependency chains and significantly reduces wall-clock time on large refactoring or feature tasks.

## Practical Takeaways

- **Use deterministic metrics to guide AI refactoring tasks.** Rather than asking an AI to "find code quality issues," feed it objective hotspot scores (churn, cyclomatic complexity, density, LOC) so it has measurable anchors for prioritization.
- **Compress-to-detect repetition.** The gzip density trick is a cheap, language-agnostic way to flag copy-paste boilerplate without requiring AST analysis — useful for bootstrapping code quality signals in any codebase.
- **Never trust AI to self-correct known failure modes without explicit structural guardrails.** The timing-safe comparison bug shows that even expensive "more thinking" ($25/run code review tools) doesn't reliably catch mistakes that conflict with an AI's training priors. Code comments, rules files, and telemetry-driven mitigations are necessary complements.
- **Build a mistake telemetry loop early.** The sooner teams start logging recurring AI errors and converting them to rules/epics, the faster the compounding improvement cycle starts — teams that do this earlier gain a durable competitive advantage.
- **Map dependency chains before parallelizing agents.** Blindly spawning parallel agents on a large task creates merge conflicts and wasted work; identifying which tasks are genuinely independent (and which must sequence) unlocks safe 4x parallelism.

## Notable Quotes

> "No matter how much the AI agents think about that, they still mess it up... no matter how much what you're paying for with that $25 is just a lot of thinking, a lot of tokens, it's just talking to itself a lot. And what I found is that sometimes the more that it talks to itself the more it digs its heels in about making the same mistakes."

> "The AI trains itself as you continue to use it. So the more you use it, the better it gets just automatically in this perpetual positive feedback cycle. And the sooner that we get that up and running, the further ahead we'll get in front of everybody else."

> "More clutter equals more surface area for bugs equals more bugs — more places for bugs to hide."
