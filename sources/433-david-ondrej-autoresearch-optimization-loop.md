---
source_id: "433"
title: "The only AutoResearch tutorial you’ll ever need"
creator: "David Ondrej"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=uBWuKh1nZ2Y"
date: "2026-03-27"
duration: "19:52"
type: "video"
tags: ["agentic-coding", "prompt-engineering", "multi-agent", "ai-landscape", "ai-sdlc"]
curriculum_modules: ["04-agentic-patterns", "02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 433: The only AutoResearch tutorial you’ll ever need

> **Creator**: David Ondrej | **Platform**: YouTube | **Date**: 2026-03-27 | **Duration**: 19:52

# The Only AutoResearch Tutorial You'll Ever Need

## Summary

This video introduces AutoResearch, an open-source project by Andrej Karpathy that enables AI agents to autonomously run experiments, keep what improves a metric, and discard what doesn't — effectively creating a self-improving loop with minimal human involvement. The core architecture consists of three files: `prompt.md` (human-defined goals and constraints), `train.py` (the single file the agent can modify), and `prepare.py` (the locked evaluation metric). By fixing a time budget per experiment and preventing the agent from touching the scoring function, the loop produces genuinely comparable results across hundreds of overnight runs.

The video's central argument is that AutoResearch is widely misunderstood as a machine learning tool when it is actually a general-purpose optimization framework. Any domain with a clear scalar metric and an automated evaluation function — trading strategies, marketing copy, prompt engineering, code performance — is a candidate for an AutoResearch loop. The three necessary conditions are: one measurable metric, an automated (human-free) evaluation, and one editable file. Where success is subjective or the evaluation loop requires human judgment, the approach breaks down.

The tutorial closes with a hands-on walkthrough using Claude Code and Cursor to clone the AutoResearch repository and scaffold a simple web app as a target for optimization, demonstrating that the pattern is accessible to non-ML practitioners. Karpathy's broader vision — distributed AutoResearch loops running across millions of machines, analogous to SETI@home — is presented as a plausible near-term trajectory for frontier AI labs and independent developers alike.

---

## Key Concepts

### The Three-File Architecture
AutoResearch operates on a strict separation of concerns across three files. `prompt.md` is the human's contract with the agent — goals, rules, and constraints. `train.py` is the sole file the agent is permitted to edit; it can be code, config, a prompt template, or any other artifact being optimized. `prepare.py` defines the evaluation metric and is immutable to the agent. Locking the evaluation file is critical: without it, the agent could rewrite the scoring function to fabricate improvements rather than achieve them.

### Time-Boxing as a Fairness Constraint
Each experiment is allocated a fixed time budget (approximately five minutes in the ML example). This ensures every candidate solution competes on equal footing — a longer training run cannot masquerade as a better idea. The analogy given is hiring: giving one candidate seven days and another seven minutes produces incomparable results. Time-boxing eliminates that confound and forces the agent to win on the raw quality of the hypothesis alone.

### AutoResearch as a General Optimization Pattern
The most significant conceptual claim is that AutoResearch is domain-agnostic. The loop — hypothesize, modify, evaluate, commit or revert — applies wherever there is a scalar metric and an automated evaluator. Concrete examples include trading strategy optimization (Sharpe ratio as metric), marketing AB testing (conversion rate), prompt engineering (task success rate), and code performance (load time). The constraint is objectivity: metrics that require human aesthetic judgment or subjective interpretation cannot drive a stable loop.

### The Three Failure Modes
AutoResearch fails when: (1) the metric is poorly chosen — the agent will confidently optimize the wrong thing; (2) the evaluation requires a human in the loop — the loop becomes too slow to be "auto"; or (3) success is inherently subjective — brand design, UX feel, pricing intuition. Recognizing these boundaries is as important as knowing when to apply the pattern.

### Knowing What to Measure as the Scarce Skill
As AI execution costs approach zero and agents can run thousands of experiments autonomously, the strategic leverage shifts entirely to metric selection and constraint design. The video frames this as the defining skill of the coming period — not coding, not prompt writing, but the ability to identify what to measure, how to measure it cleanly, and what constraints prevent gaming.

---

## Practical Takeaways

- **Apply the three-file template beyond ML**: Identify any workflow producing a scalar outcome (conversion rate, latency, Sharpe ratio, test pass rate) and structure it as `prompt.md` + one editable artifact + a locked evaluator — the same pattern applies.
- **Lock your evaluator before the agent touches anything**: The `prepare.py` immutability constraint is the single most important safeguard; without it, agents optimize the measurement rather than the outcome.
- **Time-box every experiment**: A fixed per-experiment budget makes results comparable and prevents longer runs from masquerading as better ideas — apply this discipline to any autonomous loop, not just model training.
- **Use Claude Code to scaffold the loop quickly**: The walkthrough shows that cloning the AutoResearch repo and wiring up a target project via Claude Code is accessible without deep ML knowledge — the tooling barrier is low.
- **Audit your metric before launching overnight runs**: A bad metric produces confident, useless results at scale. Invest disproportionate upfront effort in validating that your scalar captures what you actually care about.

---

## Notable Quotes

> "Give AI one file, one metric, and let it run hundreds if not thousands of experiments by itself while you sleep and watch it improve."

> "If you give it a bad metric, it will very confidently optimize the wrong thing."

> "What will become valuable is knowing what to measure, picking the right metric, and setting the right constraints. This is the skill that is going to make millionaires in the future."

---
