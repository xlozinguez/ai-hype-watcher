---
source_id: "293"
title: "Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP"
creator: "Eric Elliott"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=dj2nF5ToEyY"
date: "2026-03-12"
duration: "56:45"
type: "video"
tags: ["cursor", "claude-code", "agentic-coding", "multi-agent", "security", "ai-sdlc", "prompt-engineering"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 293: Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

> **Creator**: Eric Elliott | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 56:45

# Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

## Summary

Eric Elliott demonstrates a live training session introducing new features in the AIDD (AI-Driven Development) framework, with particular focus on a new `aid churn` command that performs code hotspot analysis. The tool combines multiple deterministic metrics — commit frequency, cyclomatic complexity, line count, and information density — to surface files that are most likely to benefit from refactoring. This shifts code quality targeting from guesswork to data-driven prioritization.

A significant portion of the session covers the feedback loop problem in AI-assisted development: AI agents consistently repeat the same mistakes across PRs regardless of how much "thinking time" they're given, and expensive solutions like Anthropic's $25/run code review tool may not solve structural pattern-repetition issues. Elliott proposes a telemetry-driven system that logs recurring AI mistakes and automatically converts them into rules and task epics, creating a self-improving feedback cycle where the AI trains itself the more it's used.

The session also touches on Cursor's parallel web agents (up to 4 simultaneous sub-agents), security pitfalls in token comparison (timing-safe compare is a false standard due to compiler optimizations), and practical architectural patterns like command dispatch tables to reduce cyclomatic complexity. The broader theme is moving AI-assisted development from reactive bug-fixing toward proactive, metrics-informed code health management.

## Key Concepts

### Code Hotspot Analysis via `aid churn`

The `aid churn` command surfaces high-risk files by combining four signals: (1) **commit frequency** over a 90-day window as a churn indicator (frequent commits suggest active bug-fixing, not just feature work), (2) **cyclomatic complexity** — the number of independent code paths through a function, with a target of ~9 or below, (3) **information density** — measured by comparing gzip-compressed vs. uncompressed file size as a proxy for copy-paste repetition and abstraction opportunities, and (4) **raw line count** as a clutter/surface-area proxy. Files scoring poorly across these dimensions become prioritized refactoring targets.

### Cyclomatic Complexity and the Command Dispatch Pattern

High cyclomatic complexity (many nested if/else branches) creates combinatorial test explosions and hides bugs. Elliott advocates for **command dispatch tables** — a single keyed lookup that maps to individual single-path functions — as a structural solution. This reduces branching, makes each path independently testable, and limits how many ways a bug can enter the system.

### AI Mistake Telemetry and Self-Improving Feedback Loops

Because AI agents repeat the same coding mistakes across sessions and PRs regardless of prompt length or "thinking budget," Elliott proposes a **telemetry service** that logs recurring errors and their mitigations. Periodically (e.g., via Claude Code's built-in `insights` command), these logs are analyzed, converted into new rules and task epics, and fed back into the agent's instruction set. The result is a compounding improvement cycle: the more the system is used, the fewer mistakes it repeats.

### Timing-Safe Token Comparison is a False Standard

A persistent AI failure mode: agents replace correct constant-time hash comparison logic with `timingSafeCompare` functions that compilers optimize away — defeating the timing-safety guarantee. Modern compilers short-circuit comparisons when they can predict the result, leaking timing information that enables hangman-style brute-force attacks. The mitigation requires explicit code comments *and* framework-level security rules, but even then agents override them. This illustrates a class of security bugs where AI confident wrong answers are worse than no answer.

### Parallel Sub-Agent Workflows with Cursor Web Agents

Elliott uses Cursor's web agent mode to fork up to **4 parallel sub-agents**, organized around dependency chains: one wave resolves foundational dependencies, the next wave builds on them. This matches the natural DAG structure of most development tasks and provides meaningful throughput gains without requiring complex orchestration infrastructure.

## Practical Takeaways

- **Use commit frequency + complexity + density together** to prioritize refactoring targets rather than gut feel. A file touched 7 times in 90 days with cyclomatic complexity of 15 and low density is a high-priority target even if it has no obvious bugs today.
- **Don't pay for "more thinking"** to solve AI pattern-repetition problems. Expensive multi-step review tools (e.g., $25/run) may not outperform targeted rules because the issue is model priors, not reasoning depth. Invest in better rules and telemetry instead.
- **Log AI PR feedback repeatedly flagged by reviewers** and convert high-frequency items into CLAUDE.md rules or framework-level constraints. This is the highest-leverage improvement action available to teams using AI coding assistants.
- **Add explicit `// DO NOT REPLACE` comments** around security-critical code patterns (especially token comparison logic) and back them up with framework security rules — but treat these as temporary mitigations while pursuing proper abstraction.
- **Structure parallel agent work around dependency waves**: identify which tasks are truly independent, run those in parallel first, then trigger the next wave. Four parallel agents working in two waves outperforms eight agents with unmanaged dependencies.

## Notable Quotes

> "No matter how much the AI agents think about that, they still mess it up and they still don't catch that security flaw... we literally have to leave code comments in there saying 'don't do that.'"

> "The more that it talks to itself, the more it digs its heels in about making the same mistakes... what you're paying for with that $25 is just a lot of thinking, a lot of tokens — it's just talking to itself a lot."

> "The AI trains itself as you continue to use it. So the more you use it, the better it gets just automatically in this perpetual positive feedback cycle."
