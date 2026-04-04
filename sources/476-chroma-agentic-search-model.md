---
source_id: "476"
title: "Chroma Context-1 | A 20B Agentic Search Model"
creator: "Chroma"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=4sAJLLWPAh4"
date: "2026-03-26"
duration: "13:20"
type: "video"
tags: ["multi-agent", "agentic-coding", "context-engineering", "ai-landscape", "validation"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "01-foundations"]
---

# 476: Chroma Context-1 | A 20B Agentic Search Model

> **Creator**: Chroma | **Platform**: YouTube | **Date**: 2026-03-26 | **Duration**: 13:20

# Chroma Context-1 | A 20B Agentic Search Model

## Summary

Chroma introduces Context-1, a 20 billion parameter open-weights model purpose-built for agentic search tasks. The model achieves frontier-level retrieval performance comparable to models an order of magnitude larger (e.g., GPT-4-class systems) while operating at significantly lower cost and latency. It is released alongside an agentic search benchmark and the full synthetic data generation pipeline used to train it, making this a significant open contribution to the search-agent ecosystem.

The core insight is that agentic search—iterative LLM-driven loops using search and document-reading tools—is now a fundamental subtask in many agentic workflows, including coding agents. Context-1 is designed as a *search sub-agent* that retrieves relevant documents for a downstream answering model rather than answering questions directly. The model is evaluated on recall and precision (via F1), with an emphasis on recall since missing a critical document is unrecoverable downstream. Training combines supervised fine-tuning on teacher-generated rollouts with on-policy reinforcement learning using GRPO-style optimization.

Three emergent behaviors distinguish Context-1 from its base model: parallel tool calling (issuing multiple search queries per turn rather than sequentially), more deliberate upfront planning, and aggressive use of a pruning tool to remove irrelevant context and extend effective search range. These behaviors arise naturally from the harness design and reward structure, not from explicit behavioral constraints—a strong signal that the training incentives are well-aligned with search quality.

## Key Concepts

### Agentic Search as a Multi-Hop Retrieval Loop
Unlike single-shot retrieval where one query produces a fixed document set, agentic search is an iterative loop: the agent searches, reads results, forms new hypotheses, and searches again. Each step depends on what was discovered previously (multi-hop). Context-1 is given four tools—`search` (hybrid sparse+dense vector search), `grab` (regex pattern matching for specific facts), `read_document` (full document retrieval by ID), and `prune` (context pruning)—and operates in a loop until it outputs a final ranked document set.

### Context Management via the Prune Tool
In multi-turn search, context accumulates rapidly as documents are retrieved. Context-1's `prune` tool allows the agent to actively remove irrelevant chunks from its context window, keeping attention focused and enabling longer search trajectories without hitting context limits. The model is made aware of its current token count to inform pruning decisions. This is a practical pattern for any agentic system that accumulates tool outputs over many turns.

### Curriculum Learning: Recall-First, Precision-Later
Training uses a two-phase curriculum. Early training biases toward single-hop tasks with recall-heavy rewards, encouraging broad exploration and document discovery. As training progresses, harder multi-hop tasks are introduced and the reward objective shifts toward balanced F1 (precision + recall), teaching the model to be selective rather than just thorough. This staged approach prevents premature optimization for precision at the cost of coverage.

### Synthetic Data Generation with LLM-as-Judge Verification
Training data is generated synthetically across four domains (web, finance, legal, email). Each task is constructed from supporting documents → clues → question/answer. Crucially, an LLM judge verifies that supporting documents actually support the clues *and* that no other corpus documents also contain the answer (preventing false negatives). Human labels are used to calibrate the judge prompt until high alignment is achieved, then the verified pipeline scales to thousands of tasks without ongoing human labeling effort.

### GRPO-Style On-Policy RL with Within-Group Centering
After supervised fine-tuning on teacher rollouts, Context-1 is trained with reinforcement learning using GRPO (Group Relative Policy Optimization). Multiple independent rollouts are generated per query; rewards are compared *within the group* so the model learns which strategies outperform others on the same task rather than against an absolute standard. Groups where all rollouts score identically are discarded (no learning signal). SISO (a clipped importance-sampling variant) is used for stability and to prevent entropy collapse over long training runs.

## Practical Takeaways

- **Parallel tool calling is a trainable behavior**: Context-1 learns to issue multiple search queries per turn rather than sequentially—doing more work per step and converging in fewer turns. When designing agentic systems, structuring harnesses to reward parallel actions can meaningfully reduce end-to-end latency.
- **Prune as a first-class agent action**: Giving agents an explicit tool to remove their own context (rather than truncating passively) enables longer, more focused search trajectories. This pattern is directly applicable to coding agents, research agents, or any system where tool outputs accumulate across turns.
- **Sub-agent specialization beats generalist answering**: Context-1 doesn't answer questions—it only retrieves documents. Separating the search role from the answer role allows the search agent to be optimized purely on retrieval metrics (recall/precision) without conflating objectives. This mirrors the builder/validator separation seen in coding agent architectures.
- **Recall before precision in reward design**: For search tasks where missing evidence is catastrophic downstream, weighting recall more heavily in early training (and in the reward function generally) is a principled choice. Only shift toward precision once the model reliably covers the relevant document space.
- **LLM-judge calibration enables scalable data verification**: Manually labeling a *subset* to calibrate an LLM judge, then using the judge at scale, is a practical and reproducible approach to synthetic data quality control for agentic training pipelines.

## Notable Quotes

> "Context one operates as a search sub agent. It does not answer questions directly but searches a corpus to retrieve supporting documents for an answering model."

> "Parallel searching, planning, and pruning—these behaviors are strong evidence that the model is improving at the process of search. Importantly, they emerge naturally from a harness design and the incentives in the training reward."

> "We intentionally weigh recall more heavily because if a critical document is missing, the downstream model can't recover that information."
