---
source_id: "515"
title: "AutoResearch explained.."
creator: "Caleb Writes Code"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=5-ekc3eXNvs"
date: "2026-04-04"
duration: "5:17"
type: "video"
tags: ["agentic-coding", "vibe-coding", "ai-sdlc", "validation"]
curriculum_modules: ["04-agentic-patterns", "02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 515: AutoResearch explained..

> **Creator**: Caleb Writes Code | **Platform**: YouTube | **Date**: 2026-04-04 | **Duration**: 5:17

## Summary

Caleb demonstrates AutoResearch — a framework released by Andrej Karpathy — through two practical examples: a chess engine optimization (from 750 to 2600 ELO) and a restaurant inventory simulation. The core mechanic is an autonomous experimentation loop where the AI iteratively runs experiments, keeps only those that improve a measurable evaluation metric, and discards failures — all without human involvement during iteration. The developer's role shifts to defining the goal, structuring the evaluation function, and constraining what the agent is allowed to modify.

The video draws a sharp distinction between AutoResearch and vibe coding: vibe coding builds features incrementally with humans checking work at each step, while AutoResearch removes the human from the iteration loop entirely. The restaurant example illustrates how the framing of the eval metric matters enormously — optimizing purely for inventory fullness produced a cash-starved business, requiring the creator to redefine the metric to maximize working capital instead. This refinement step was human-driven, not algorithmic.

The creator closes with an honest assessment of AutoResearch's limits: it thrives in narrow, simulatable domains with tight feedback loops and well-defined metrics. Vague goals like "make this restaurant better" cannot drive the process. The paradigm represents a meaningful shift in software development toward problem definition and evaluation design as the primary developer skill, rather than implementation.

---

## Key Concepts

### AutoResearch's Incremental Experiment Loop
AutoResearch operates by running experiments against a fixed evaluation function, retaining only improvements and discarding regressions. This produces a characteristic "flatline then jump" improvement curve — the system appears stalled until a better algorithm is discovered. The loop is fully autonomous; no human approval gates each iteration.

### Structural Constraints Are the Core Design Lever
The framework's power comes from what it *cannot* do. Goals are defined in one file, the evaluation function in another (e.g., `prepare.py`), and the agent is restricted to modifying only the target algorithm. This containment prevents the agent from gaming the metric by modifying the evaluation itself — a critical guardrail for meaningful optimization.

### Eval Metric Design as Developer Responsibility
The restaurant case reveals that choosing the wrong metric produces locally optimal but globally harmful results. Maximizing inventory kept shelves full but depleted working capital. The creator had to intervene and redefine the metric to balance inventory against cash on hand. Metric design — not implementation — is where developer judgment is most consequential.

### AutoResearch vs. Vibe Coding
Vibe coding is human-in-the-loop and feature-sequential; AutoResearch is human-out-of-the-loop and experiment-parallel. Both are agentic, but AutoResearch requires the problem to be fully specified upfront and simulatable, making it a distinct paradigm rather than an extension of vibe coding workflows.

### Domain Constraint: Simulatable Feedback Loops Required
AutoResearch depends on fast, automated feedback — a simulation or test harness that can evaluate each experiment without human judgment. This limits applicability to domains where you can codify "better" in a computable metric and run evaluations cheaply. Open-ended, real-world, or subjective problems resist this structure.

---

## Practical Takeaways

- **Define your eval before writing any code.** AutoResearch (and agentic optimization broadly) lives or dies on the quality of the evaluation function. Invest time there first.
- **Constrain the agent's action space deliberately.** Explicitly forbid modification of files outside the target algorithm to prevent metric gaming and maintain experimental validity.
- **Treat metric misalignment as a design iteration, not a failure.** The shift from "maximize inventory" to "maximize working capital" is normal — expect to refine what you're measuring as you observe emergent behavior.
- **Reserve AutoResearch for simulatable, narrow domains.** If you can't run 50 automated experiments and score them in minutes, the paradigm won't work. Identify whether your problem has this property before investing in the setup.
- **The developer's core skill is becoming problem formulation, not implementation.** Writing the goal, the eval, and the constraints clearly is now the high-leverage activity; the agent handles code generation and iteration.

---

## Notable Quotes

> "Instead of telling AI how to implement this algorithm, it self-optimized the algorithm to maximize the inventory by running different experiments."

> "Auto research is more about what it can't do rather than what it can do."

> "Developing software in this scenario is more about understanding the problem well enough and defining into words and putting the structure around them for the agent to build it successfully."

---
