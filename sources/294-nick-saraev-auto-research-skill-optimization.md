---
source_id: "294"
title: "Stop Fixing Your Claude Skills. Autoresearch Does It For You"
creator: "Nick Saraev"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=qKU-e0x2EmE"
date: "2026-03-13"
duration: "16:32"
type: "video"
tags: ["claude-code", "skills", "prompt-engineering", "agentic-coding", "validation", "meta-prompts"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "02-prompting-and-workflows"]
---

# 294: Stop Fixing Your Claude Skills. Autoresearch Does It For You

> **Creator**: Nick Saraev | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 16:32

## Summary

Nick Saraev introduces a technique for automatically improving Claude Code skills over time by adapting Andrej Karpathy's "auto-research" methodology — originally designed for autonomous ML model optimization — to prompt engineering. The core idea is to treat a Claude Code skill's markdown prompt file the same way auto-research treats a training script: run it repeatedly, evaluate outputs against a standardized binary test suite, and let an agent iteratively refine the prompt until it consistently passes. The practical demo centers on a "diagram generator" skill, where the agent generates 10 diagrams per run, scores them against four criteria (legibility, color palette, linearity, absence of numbering), and revises the skill instructions between iterations.

The method requires three ingredients: an objective numeric metric (the eval pass rate), an automated measurement tool (a test suite run by an agent), and something to change (the skill's prompt instructions). Saraev estimates that optimizing a skill to near-perfect pass rates across a meaningful eval set costs roughly $10 in model API spend, offering an attractive ROI compared to manual prompt iteration. He also notes that the accumulated research data — the log of every attempted prompt change and its score — becomes a durable asset transferable to future, more capable models.

The broader implication Saraev stresses is that auto-research is not limited to skills or prompts. He applies the same loop to website load-time optimization (achieving an 81.3% reduction) and cold email copy, suggesting the pattern is a general-purpose autonomous optimization primitive applicable wherever you have a measurable objective, an automated evaluator, and a changeable artifact.

---

## Key Concepts

### Auto-Research as a General Optimization Loop
Karpathy's auto-research repo uses a small team of agents to autonomously iterate on a process (ML model training) by repeatedly running it, measuring performance against an eval, and modifying the process. Saraev's contribution is recognizing this as a domain-agnostic pattern: substitute the training script with any artifact (a prompt, a website's codebase, email copy), substitute the loss metric with any measurable objective, and the loop generalizes immediately.

### Eval Sets for Prompt Reliability
Because LLM outputs are stochastic distributions rather than deterministic functions, a single run cannot reliably assess prompt quality. The solution is to run the skill many times (e.g., 10 per iteration) and score each output against binary yes/no criteria. Aggregating scores across runs gives a stable signal — the "evaluation pass rate" — that can be compared across prompt versions. This transforms the fuzzy problem of "is this prompt good?" into a measurable optimization target.

### Binary Criteria as Evaluation Design
Effective evals decompose qualitative goals into specific, binary-checkable questions. For the diagram example, vague goals like "looks professional" are broken into: (1) is all text legible and grammatically correct? (2) does it use the defined pastel color palette? (3) does layout flow left-to-right or top-to-bottom? (4) is it free of numbers and ordinals? Each criterion is independently verifiable by a reviewer agent, making scoring consistent and automatable without human judgment in the loop.

### Research Data as a Durable Asset
Each auto-research run produces a log of attempted prompt changes and their scores. Saraev argues this accumulated record of what worked and what didn't is itself valuable: it can be handed to a more capable future model (e.g., GPT-6, Claude Opus 5) to continue optimization from where the previous agent left off. This reframes research data not as a byproduct but as a compounding asset with increasing value as frontier models improve.

### Cost-Benefit Framing for Prompt Optimization
Saraev explicitly calculates the economics: ~$0.02 per diagram generation × 10 diagrams per test = $0.20 per iteration; ~50 iterations to reach a well-optimized skill = ~$10 total. Framing autonomous prompt optimization in dollar terms makes it tractable as a business decision rather than an open-ended engineering task, and provides a natural stopping condition (diminishing returns relative to cost).

---

## Practical Takeaways

- **Define your eval before you optimize.** Identify 3–5 binary yes/no questions that capture what "good output" means for your skill. Vague criteria like "looks better" cannot be scored automatically; specific binary checks can.
- **Run skills in batches, not singles.** Because LLM outputs are distributions, evaluate 10+ runs per iteration and aggregate scores. A single run result is too noisy to trust as a signal for prompt improvement.
- **Feed the auto-research repo URL directly to your agent.** Saraev's workflow is simply: paste the Karpathy repo link + your eval criteria + a natural-language instruction into Claude Code. The agent reads the repo, builds the test suite, and begins iterating autonomously.
- **Set a total score cap to create a clear target.** Structuring evals as X criteria × Y runs = maximum score (e.g., 4 criteria × 10 runs = 40 points) gives the agent a concrete optimization target and makes progress visible in a real-time dashboard.
- **Save the iteration log.** The record of every prompt change attempted and its score is reusable. When better models arrive, pass this log in as context so the new agent starts from accumulated knowledge rather than scratch.

---

## Notable Quotes

> "Skills are just prompts. And prompts are inherently noisy. What I mean by that is sometimes you'll run a prompt and it'll do X. Another time you run a prompt and it'll do Y."

> "I think this is actually probably soon to be one of the most important and valuable assets of our time — just a bunch of research data."

> "What might be 32 out of 40 for me might have started for you at like a two out of 100. The one thing that matters is just how much time you let it run."

---
