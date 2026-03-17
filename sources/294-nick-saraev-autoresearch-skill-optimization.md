---
source_id: "294"
title: "Stop Fixing Your Claude Skills. Autoresearch Does It For You"
creator: "Nick Saraev"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=qKU-e0x2EmE"
date: "2026-03-13"
duration: "16:32"
type: "video"
tags: ["skills", "claude-code", "prompt-engineering", "agentic-coding", "validation", "meta-prompts"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "02-prompting-and-workflows"]
---

# 294: Stop Fixing Your Claude Skills. Autoresearch Does It For You

> **Creator**: Nick Saraev | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 16:32

## Summary

Nick Saraev introduces a method for autonomously improving Claude Code skills by adapting Andrej Karpathy's "AutoResearch" framework—originally designed for optimizing ML training runs—to the problem of prompt reliability. The core insight is that Claude Code skills are essentially prompts, and prompts are noisy (Saraev estimates ~70% reliability on a good day), but if you can define an objective metric, a measurement tool, and something to change, you can run an automated optimization loop that makes the skill progressively better without manual intervention.

The practical workflow involves three components: (1) a skill file (analogous to `train.py` in Karpathy's repo), (2) an agent with high-level instructions (analogous to `program.md`), and (3) an eval test suite consisting of binary yes/no questions that score each output. The agent generates batches of outputs, scores them against the eval suite, modifies the skill prompt to improve the score, and repeats on a timer. Saraev demonstrates this on a "diagram generator" skill, running 10 generations per cycle against 4 binary criteria (max 40 points), watching it climb from 32/40 toward a perfect score over successive iterations.

Saraev argues this approach is broadly applicable beyond skills—he applies it to website load-time optimization (1100ms → 67ms) and cold email reply rates—and that the accumulated research log of attempted changes becomes a durable, transferable asset: future, more capable models can pick up where current ones left off, compounding the value of the optimization data over time.

---

## Key Concepts

### AutoResearch as a General Optimization Framework
Karpathy's AutoResearch repo uses a small team of agents to autonomously optimize a target process by repeatedly measuring performance against an objective metric and making incremental changes. The framework requires only three ingredients: an objective metric (a number, not a vibe), a measurement tool (ideally automated, no human in the loop), and something to change. Saraev generalizes this pattern beyond ML training to any iterative artifact—website code, email copy, or skill prompts.

### Eval Test Suites for Prompt Optimization
Because LLM outputs are probability distributions, a single run is not a reliable signal. To assess prompt quality, you must run many iterations and evaluate each output against a standardized set of binary (yes/no, true/false) questions. These questions act as a benchmark, converting subjective quality judgments into a numeric score. For a diagram generator, Saraev's four criteria are: text legibility, adherence to pastel color palette, linear layout (left-to-right or top-to-bottom), and absence of numeric ordinals.

### Skills as Prompts Subject to Noise
Claude Code skills are markdown prompt files, and like all prompts they are inherently noisy—the same skill can produce good results 70% of the time and poor results 30% of the time. Treating a skill as an optimization target (rather than a static artifact) reframes maintenance: instead of manually editing the prompt when something goes wrong, you define success criteria upfront and let an automated loop converge on a more robust prompt.

### Accumulated Research Logs as Durable Assets
A side effect of running many optimization iterations is a log of every change attempted and its effect on the score. Saraev argues this log is itself valuable intellectual property: as frontier models improve, you can pass the full history of attempted changes to a more capable model (e.g., GPT-6 or a future Claude Opus) and it can continue the optimization from where its predecessor stopped. The research data compounds in value over time independently of any specific model.

### Cost-Bounded Experimentation
Because each generation has a known cost (Saraev cites ~$0.02 per diagram using a fast model), the total optimization budget is predictable. Ten generations per cycle costs ~$0.20; reaching a good optimum within 50 cycles costs ~$10. This makes it straightforward to frame skill optimization as a business decision with a clear ROI calculation relative to the value the skill generates.

---

## Practical Takeaways

- **Define binary evals before running AutoResearch.** Break your quality criteria into yes/no questions that an agent can score without human judgment. Vague criteria ("does it look good?") cannot be automated; specific binary criteria ("is all text legible?") can.
- **Run batches, not single tests.** Because prompt outputs are distributions, score each version of your skill across at least 10 runs and use the aggregate score (out of `N runs × M criteria`) as your optimization target.
- **Mirror Karpathy's file structure conceptually.** Treat your skill `.md` file as `train.py` (the thing being optimized) and your agent instructions as `program.md` (the optimizer). This mental model clarifies what the agent should and should not change.
- **Set a timer-driven loop.** Instruct the agent to re-run the eval suite on a fixed interval (e.g., every 2–5 minutes) and halt when the score plateaus or hits a target threshold, rather than running indefinitely.
- **Save every iteration's change log.** The record of what was tried and what effect it had is reusable with future models and represents compounding value beyond the immediate skill improvement.

---

## Notable Quotes

> "Skills are just prompts, and prompts are inherently noisy. What I mean by that is sometime you'll run a prompt and it'll do X. Another time you run a prompt and it'll do Y."

> "You don't just have to use it for skills… over the course of about 67 different tests, this auto research methodology took my load speed from about 1100 milliseconds literally down to 67."

> "I think this is actually probably soon to be one of the most important and valuable assets of our time—just a bunch of research data."

---
