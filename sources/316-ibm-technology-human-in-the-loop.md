---
source_id: "316"
title: "What is Human In The Loop with AI? How HITL Shapes AI Systems"
creator: "IBM Technology"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=9iS-YYLIXiw"
date: "2026-03-17"
duration: "10:44"
type: "video"
tags: ["agentic-coding", "ai-safety", "validation", "enterprise-ai"]
curriculum_modules: ["04-agentic-patterns", "06-strategy-and-economics"]
---

# 316: What is Human In The Loop with AI? How HITL Shapes AI Systems

> **Creator**: IBM Technology | **Platform**: YouTube | **Date**: 2026-03-17 | **Duration**: 10:44

## Summary

This IBM Technology explainer introduces Human-in-the-Loop (HITL) as a spectrum of human involvement in AI systems, ranging from strict human approval at every step, to human monitoring with override capability, to full autonomy with no human involvement. The video frames HITL not as a binary choice but as a maturity curve: systems typically start with heavy human involvement and gradually earn the right to operate more autonomously as trust is established.

The video maps human involvement to three distinct intervention points in an AI system's lifecycle: training time (data labeling and active learning), tuning time (RLHF and preference ranking), and inference time (confidence thresholds, approval gates, and escalation queues). Each injection point solves a different problem — labeling gives the model knowledge, preference tuning gives it judgment, and runtime oversight gives it guardrails.

The content is particularly relevant for agentic AI systems, where agents don't just generate content but take real-world actions like executing code and modifying databases. In this context, runtime oversight patterns like approval gates (where an agent must get explicit human approval before modifying a filesystem) become critical safety mechanisms. The video closes by acknowledging HITL tradeoffs around scalability bottlenecks and human inconsistency, while emphasizing that the goal is always to move along the autonomy spectrum as systems prove themselves trustworthy.

---

## Key Concepts

### The HITL Spectrum
Human-in-the-loop is not a single mode but a three-point spectrum. **Human in the loop (strict HITL):** the system stops and waits for human approval before proceeding — a human gives the final go command. **Human on the loop:** the AI operates autonomously while a human monitors and retains veto/override power. **Human out of the loop:** full autonomy with no human intervention, sometimes because the system operates at speeds where intervention is physically impossible (e.g., high-frequency trading).

### Three Injection Points for Human Involvement
Human oversight can be embedded at three stages: (1) **Training time** — humans label data or, via active learning, focus labeling effort on the uncertain cases the model can't resolve itself; (2) **Tuning time** — humans provide preference rankings between model outputs (RLHF), which trains a separate reward model that then coaches the LLM, encoding human judgment without requiring humans at runtime; (3) **Inference time** — live production systems use confidence thresholds, approval gates, or escalation queues to route uncertain or high-stakes decisions to humans.

### Active Learning as Efficient HITL
Rather than requiring humans to label entire datasets, active learning has the model train on a small labeled set, then identify the unlabeled examples it is most uncertain about and request human labels only for those. This concentrates expensive human effort on the cases that actually move the needle, making large-scale labeling tractable without requiring exhaustive human review.

### RLHF: Encoding Judgment, Not Rules
Reinforcement Learning from Human Feedback (RLHF) solves the problem of aligning model behavior to qualities that can't be expressed as explicit rules (e.g., "be helpful but not creepy"). A human compares two model outputs and picks the better one — expressing a preference rather than writing a correction. Thousands of these preference pairs train a reward model, which then guides the LLM via reinforcement learning. The human's judgment is baked in at tuning time, removing the need for a human at runtime.

### Runtime Oversight Patterns for Agentic AI
For AI agents that take real-world actions (executing code, modifying databases, calling APIs), three runtime patterns manage risk: **Confidence thresholds** route low-certainty predictions to humans while the AI handles the high-confidence majority. **Approval gates** require explicit human sign-off before the agent executes a proposed action — the standard pattern in coding agents before filesystem changes. **Escalation queues** let the agent handle routine cases end-to-end but flag edge cases for human review.

---

## Practical Takeaways

- **Design HITL placement intentionally, not by default.** Each injection point (training, tuning, inference) solves a different problem. Putting humans at the wrong stage wastes effort without reducing risk.
- **Use approval gates for irreversible agentic actions.** When an agent can modify a filesystem, database, or external service, an explicit human approval step before execution is the minimal viable safety mechanism — consistent with how leading coding agents already work.
- **Active learning is the scalable alternative to exhaustive labeling.** If building a supervised system, start with a small labeled set, let the model identify its own uncertainty, and direct human labeling effort to those uncertain examples only.
- **Treat HITL as a temporary scaffold, not a permanent fixture.** The goal is to accumulate enough evidence of system reliability to move from strict HITL → human on the loop → human out of the loop for appropriate tasks. Every autonomous system started with heavy human involvement.
- **Account for human-shaped bottlenecks in system design.** Every approval gate or review queue is a throughput constraint. At high decision volumes, HITL must be selective and strategically placed, not applied uniformly across all decisions.

---

## Notable Quotes

> "The goal of human in the loop was never to keep humans in the loop forever. It's to keep them there until the system earns enough trust to move along that spectrum."

> "Labeling has given the model knowledge. Our preference tuning here has given the model judgment and runtime oversight has given the model guardrails."

> "Agents take actions. They execute code. They modify databases."

---
