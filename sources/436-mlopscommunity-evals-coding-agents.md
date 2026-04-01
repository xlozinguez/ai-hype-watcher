---
source_id: "436"
title: "Stop Shipping on Vibes — How to Build Real Evals for Coding Agents"
creator: "MLOps.community"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=VbX24V_JFQI"
date: "2026-03-31"
duration: "29:09"
type: "video"
tags: ["validation", "agentic-coding", "claude-code", "prompt-engineering", "multi-agent"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns", "05-team-orchestration"]
---

# 436: Stop Shipping on Vibes — How to Build Real Evals for Coding Agents

> **Creator**: MLOps.community | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 29:09

# Stop Shipping on Vibes — How to Build Real Evals for Coding Agents

## Summary

Jess from Braintrust presents the case against shipping AI features based on intuition or informal testing ("vibes"), arguing that teams need structured evaluation frameworks to make defensible shipping decisions. The talk covers the four core components of building evals—datasets, tasks, scoring systems, and experiments—and explains how they fit into a continuous loop connecting production logs, iterative experimentation, and code changes. The core message is that quantified evals (e.g., "94% of 200 test cases passed") replace guesswork and enable nuanced comparisons like "this change improved tone but decreased accuracy by 5%."

The second half of the talk walks through a concrete, complex eval comparing **agentic search** (LLM-driven CLI tool use, as used by Claude Code) against **vector search** (embedding-based retrieval via a database like Pinecone) for coding agent tasks. The experiment used two datasets—Microsoft's TypeScript Go repo and a subset of SWE-Bench Verified (Django rows)—chosen to test performance across different codebase types. Key implementation challenges included preventing Claude Code from falling back to its default agentic search behavior and wiring subprocess traces back to parent trace IDs for full observability.

The talk also surfaces a real-world cautionary example: OpenAI had to revert a model update in April 2025 because optimizing for helpfulness made the model excessively agreeable and therefore less useful—a regression that rigorous evals could have caught earlier. Jess frames evals as a team sport involving engineers, PMs, subject matter experts, and data analysts, each playing a distinct role in the eval lifecycle.

## Key Concepts

### The Four Components of an Eval
Every eval requires: (1) a **dataset** of test cases covering golden paths, edge cases, and failure modes; (2) a **task** definition specifying how the system should behave given inputs (prompt + model choice); (3) a **scoring system** that defines what "good" and "bad" outputs look like, using deterministic scoring, LLM-as-a-judge, or human review; and (4) **experiments** that combine a specific dataset/task/score configuration into a run. Multiple experiment runs can then be compared to detect regressions or improvements.

### Agentic Search vs. Vector Search
Vector search converts code/text into embeddings stored in a vector database; queries retrieve the closest semantic matches. Agentic search (used by Claude Code by default) gives the LLM direct access to CLI tools like `grep`, `find`, `ls`, and `cat`, allowing it to navigate a codebase the way a human developer would—following references, opening files, and iterating. The eval was designed to isolate which approach better serves coding agents on real bug-fix tasks, using Claude Code's `--disallow-tools` flag and explicit prompting to prevent fallback to agentic search in the vector search condition.

### Eval as a Continuous Production Loop
Evals are not a one-time pre-ship gate. The recommended workflow is: wrap production code with an observability SDK → collect live logs → sample 10–20% of logs to build/update a dataset → run evals → apply learnings back to the app. This creates a feedback loop where real user behavior continuously informs and improves the system, rather than relying on synthetic test cases alone.

### Trace Observability for Subprocesses
When an agent (like Claude Code) runs as a subprocess, its traces are orphaned—disconnected from the parent trace tree—making it impossible to see what the agent actually did. The fix is passing parent span IDs as environment variables so subprocess traces attach correctly. This is a practical prerequisite for meaningful observability in agentic coding workflows where multi-step agent behavior needs to be auditable.

### Evals as a Team Sport
Effective evals require multiple roles: engineers bring data and implement changes; PMs or product owners define success criteria and generate hypotheses; subject matter experts (especially in medicine, law, insurance) label data and refine prompts; data analysts define scoring rubrics and interpret results. Treating evals as solely an engineering concern misses the cross-functional inputs needed to define what "good" actually means for a given product.

## Practical Takeaways

- **Replace vibe-based ship decisions with quantified thresholds**: require a defined pass rate on a representative test suite before shipping AI features, and document the criteria explicitly.
- **When constraining agent behavior for experimental control**, use both a tool-blocking flag (e.g., `--disallow-tools`) *and* explicit prompt instructions—one alone is insufficient to prevent fallback behaviors.
- **Use two or more structurally different datasets** when benchmarking search or retrieval strategies: a newer modular codebase (TypeScript Go) and a large legacy codebase (Django/SWE-Bench) can surface performance differences that a single dataset would mask.
- **Fix subprocess tracing early**: before running large agent evals, ensure all subprocess spans are wired to parent trace IDs via environment variables, or you'll have blind spots in exactly the complex multi-step behavior you most need to understand.
- **Sample production logs (10–20%) as a living dataset**: this keeps evals grounded in real user behavior rather than drifting toward synthetic cases that don't reflect actual usage patterns.

## Notable Quotes

> "You're essentially making ship decisions based off of vibes, which is not good. Ideally you would like to be able to quantify when you're shipping by saying things like we ran 200 different test cases and 94% of them passed."

> "In April of 2025, OpenAI actually had to revert an entire model update because the changes they made to make it more helpful actually made it too agreeable and therefore not very useful. This is an example of when it's very easy to overtrain models and so you want to be able to catch these nuances early on."

> "Traces of like an LLM doing a bunch of turns where it hallucinates or drifts is really, really hard to manually read through—Loop is just better, at least faster than what I can do, and it's better at detecting these patterns than I can."
