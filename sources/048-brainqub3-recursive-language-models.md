---
source_id: "048"
title: "Before You Build Another Agent, Understand This MIT Paper"
creator: "Brainqub3"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=m1Tc5Xzw1tM"
date: "2026-01-15"
duration: "17:47"
type: "video"
tags: ["context-engineering", "agentic-coding", "ai-landscape"]
curriculum_modules: ["01-foundations", "04-agentic-patterns"]
---

# 048: Before You Build Another Agent, Understand This MIT Paper

> **Creator**: Brainqub3 | **Platform**: YouTube | **Date**: 2026-01-15 | **Duration**: 17:47

## Summary

Brainqub3 breaks down the Recursive Language Models (RLM) paper by Alex Zhang, Tim Kraska (MIT), and Omar Khattab, arguing it represents a paradigm shift for AI agents working with complex, high-context tasks outside of software engineering. The core insight is that complex documents like legal contracts and codebases should be modeled as dependency graphs rather than linear text, and that a surprisingly simple mechanism — code execution plus recursion — can unlock reliable reasoning over them.

The video systematically explains why prior approaches (context stuffing, summarization, and RAG) fail when task complexity is high, introduces the concept of "context rot" as a two-dimensional problem (context length x task complexity), and presents the RLM's REPL-based architecture as a solution. Rather than feeding documents into the context window, RLMs load them as variables in a Python environment and let the model programmatically search, slice, and recursively delegate sub-tasks to smaller models. The result is cheaper, higher-performance reasoning over documents orders of magnitude larger than advertised context windows.

## Key Concepts

### Context Rot Is Two-Dimensional

Context rot — performance degradation as context grows — is not simply a function of token count. It is the product of context length and task complexity. A model with a million-token window will deteriorate well before reaching capacity if the task requires multihop reasoning across internally self-referencing documents. This reframes the problem: bigger context windows alone do not solve complex reasoning tasks.

### Complex Documents Are Dependency Graphs, Not Textbooks

Legal contracts, codebases, and policy documents contain dense internal cross-references — clauses referencing other clauses, functions calling other functions. The right mental model is a dependency graph with nodes (clauses, functions) and edges (references, calls), not a linear narrative. This explains why sequential reading or naive context stuffing fails: the model needs to traverse a graph, not scan a stream.

### The REPL + Recursion Architecture (RLM)

The RLM approach is deceptively simple. Instead of placing documents in the context window, the system assigns them to variables in a Python REPL. The model then operates through four primitives: **Read** (inspect the data object), **Evaluate** (run any programmatic function — slicing, keyword matching, filtering), **Print** (return results to the interpreter), and **Loop** (continue until the task is solved). A recursive layer allows the orchestrating model to hand off sub-tasks to smaller models that focus on specific portions of the data. This enables flexible, intelligent search over the document graph rather than brute-force context consumption.

### Why Prior Approaches Break Down

- **Context stuffing**: Expensive, slow, and actively harmful — additional context can bury the signal in noise, reducing reliability.
- **Summarization/compaction**: Lossy by nature. Deciding what to keep is itself a hard problem, and agents gradually drift off task as summarized context diverges from the original.
- **RAG**: Effective for simple Q&A via semantic similarity, but brittle for complex tasks. Semantic retrieval cannot capture logical relationships needed for multihop reasoning, and chunking strategies are domain-specific and do not scale.

## Practical Takeaways

- **Model complex documents as graphs**: When building agents for legal analysis, policy review, or codebase reasoning, design your architecture around dependency traversal rather than sequential context processing.
- **Use code execution as a reasoning primitive**: Giving an LLM a code interpreter to programmatically explore data objects is more effective than stuffing those objects into the prompt. This is the core insight behind both RLMs and tools like Claude Code's codebase navigation.
- **Match the approach to the complexity**: RLMs shine when tasks involve both long context and high complexity (multihop reasoning). For short context or simple retrieval, a direct LLM call often outperforms the overhead. For long context with low complexity, a REPL without recursion may suffice.
- **Implement guardrails for recursive agents**: The paper limits recursion to one layer deep and uses synchronous workflows to prevent runaway costs. The 95th percentile of tasks can become very expensive when recursion loops spiral. Budget caps and depth limits are essential.
- **Frontier models are still required**: Performance degraded meaningfully between GPT-5 and the Qwen 340B coding model in the experiments. Smaller models are not yet validated for this scaffold.

## Notable Quotes

> "Context window is basically only half the story. The other half of the story is task complexity." — Brainqub3 ([01:02](https://www.youtube.com/watch?v=m1Tc5Xzw1tM&t=62))

> "What this leads to is models that are confidently wrong. And that's the quickest way to break down trust in any AI agent that you produce." — Brainqub3 ([03:39](https://www.youtube.com/watch?v=m1Tc5Xzw1tM&t=219))

> "Rather than trying to model these things as a storybook that you read end to end, I think it helps much more to model these things as dependency graphs." — Brainqub3 ([07:50](https://www.youtube.com/watch?v=m1Tc5Xzw1tM&t=470))

> "Code execution and recursion allows you to intelligently search over that context and build those dependency graphs that allow you to then synthesize correct answers while reasoning over that long context." — Brainqub3 ([17:10](https://www.youtube.com/watch?v=m1Tc5Xzw1tM&t=1030))

## Related Sources

- [011: Confluent Developer — Context Engineering](011-confluent-developer-context-engineering.md) — Complementary perspective on context window management strategies
- [004: Bart Slodyczka — Agent Teams](004-bart-slodyczka-agent-teams.md) — Multi-agent coordination patterns that could benefit from recursive delegation

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — Context rot and the limits of context-window scaling inform the foundations of AI capability assessment
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — REPL + recursion as a primitive for agentic reasoning over complex data
