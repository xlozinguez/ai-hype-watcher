---
source_id: "293"
title: "Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP"
creator: "Eric Elliott"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=dj2nF5ToEyY"
date: "2026-03-12"
duration: "56:45"
type: "video"
tags: ["agentic-coding", "claude-code", "cursor", "validation", "security", "ai-sdlc", "multi-agent"]
curriculum_modules: ["04-agentic-patterns", "06-strategy-and-economics"]
---

# 293: Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

> **Creator**: Eric Elliott | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 56:45

# Learn AIDD Code Hotspot Analysis, AI Prompt Testing & a Better MCP

## Summary

Eric Elliott demonstrates new features in the AIDD (AI-Driven Development) framework, focusing on a new `aid churn` command that performs automated hotspot analysis on codebases. The tool combines multiple deterministic code quality metrics—churn frequency, cyclomatic complexity, lines of code, and information density—to identify files that are most likely to harbor bugs and benefit from refactoring. This is framed as a core part of an AI-assisted code review workflow that runs alongside or instead of expensive proprietary solutions like Anthropic's $25-per-run code review tool.

A significant portion of the session covers the organizational feedback loop problem: AI agents consistently repeat the same mistakes across PRs because they lack persistent memory of prior corrections. Elliott outlines a planned telemetry service that tracks recurring AI mistakes and their mitigations, automatically converting them into framework rules and task epics so the agent effectively trains itself over time. Claude Code's built-in `insights` command is cited as a model for this kind of self-improving feedback cycle.

The session also touches on a concrete security failure pattern where AI agents persistently replace correct constant-time hash comparisons with timing-unsafe token comparisons—even when explicitly told not to—illustrating why deterministic rules and code comments are necessary guardrails against well-intentioned but incorrect AI "improvements."

## Key Concepts

### Churn Hotspot Analysis (`aid churn`)
The `aid churn` command identifies refactoring targets by analyzing a 90-day git history window. It combines four signals: **churn** (number of commits to a file, indicating bug-fix cycles), **cyclomatic complexity** (number of independent code paths, which determines testability), **lines of code** (surface area for bugs), and **information density** (gzip compression ratio as a proxy for code repetition and copy-paste patterns). Files scoring poorly across multiple dimensions are flagged as high-priority refactoring targets.

### Cyclomatic Complexity as a Testability Metric
Cyclomatic complexity measures the number of independent paths through a function. High complexity creates a combinatorial explosion of test cases and makes unit testing impractical. The recommended mitigation is replacing nested if/else branching with keyed command dispatch tables—one switch, one path per key—so each path can be tested independently. The target threshold mentioned is roughly 9 or below; the `bin/aid` file at 15 was flagged as problematic.

### Information Density via Compression Ratio
Code information density is measured by running gzip on a file and comparing compressed to uncompressed size. High compressibility (low density score) indicates repetition—likely copy-paste boilerplate. Each duplicated instance of a buggy pattern multiplies the bug count, so low-density code is a signal to abstract repeated patterns into callable functions.

### AI Self-Training Feedback Loop
Elliott describes a planned telemetry system to track recurring AI mistakes and their corrections across PRs and code reviews. These logs are semantically indexed and periodically surfaced (similar to Claude Code's `insights` command) to automatically generate rules, constraints, and task epics. The goal is a perpetual positive feedback cycle where the AI framework improves the longer it is used, without manual rule authoring per incident.

### Parallel Sub-Agent Workflows with Cursor
Elliott describes using Cursor web agents in parallel forks of up to four simultaneous sub-agents. The pattern exploits dependency chains: agents working on independent tasks run concurrently in the first wave, then a second wave builds on those outputs. This is presented as a practical ceiling for parallelism given real dependency structures in most codebases.

## Practical Takeaways

- **Use deterministic metrics for refactoring prioritization**: Churn + cyclomatic complexity + lines of code + density gives a more reliable signal than LLM intuition alone when deciding what to refactor next.
- **Never rely on AI to catch its own slop**: For recurring mistakes (e.g., timing-unsafe token comparisons), explicit code comments, hardcoded rules, and framework-level constraints are necessary—more AI "thinking" tokens do not reliably fix the pattern.
- **Track AI mistake telemetry from day one**: The earlier a team instruments PR review feedback and recurring correction patterns, the faster the self-training feedback loop compounds—this is framed as a key competitive differentiator.
- **Constant-time comparison security note**: Timing-safe compare functions are frequently optimized away by compilers, making them ineffective. The correct approach is a hash-based comparison; AI agents will revert this to unsafe patterns without explicit enforcement.
- **Expensive proprietary AI reviews may not justify cost**: At $25/run, Anthropic's code review tool may offer marginal quality improvement over a well-tuned local review pipeline, particularly for systematic issues that require persistent memory rather than more tokens.

## Notable Quotes

> "No matter how much the AI agents think about that, they still mess it up and they still don't catch that security flaw. Um, so I had to be really really explicit about how to do it right and why to do it right. And even then, an AI agent will still come along and make a secure version insecure."

> "The sooner that we get that [feedback loop] up and running, the further ahead we'll get in front of everybody else... the AI trains itself as you continue to use it. So the more you use it, the better it gets just automatically in this perpetual positive feedback cycle."

> "More clutter equals more surface area for bugs equals more bugs. More places for bugs to hide."
