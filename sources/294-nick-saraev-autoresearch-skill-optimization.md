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

# Stop Fixing Your Claude Skills. Autoresearch Does It For You

## Summary

Nick Saraev introduces a technique for autonomously improving Claude Code skills by adapting Andrej Karpathy's "autoresearch" methodology — originally designed for iterative machine learning optimization — to the problem of prompt reliability. The core insight is that skills (Claude Code prompt files) are noisy by nature, succeeding roughly 70% of the time, and that systematic automated iteration against a defined eval set can drive them toward much higher pass rates without manual tinkering.

The approach requires three ingredients: an objective numeric metric (an eval pass rate), an automated measurement tool (a test suite run by an agent), and something to change (the skill's markdown prompt). In Saraev's demonstration, he configures an agent to generate 10 diagrams per iteration, score each against four binary criteria (legibility, color palette adherence, linear layout, absence of ordinal numbers), and then autonomously revise the skill prompt to improve the score — targeting 40 out of 40. He achieves a measurable jump from 32 to 37 within early iterations.

Saraev frames this as broadly applicable beyond skills: he shows the same method improving a web app's load time from ~1100ms to 67ms (an 81% reduction). The more durable takeaway is that the accumulated research log — every tested variation and its score — becomes a reusable knowledge asset that can be handed off to future, more capable models to continue optimizing from where the current run left off.

## Key Concepts

### Autoresearch as a Prompt Optimization Loop
Adapted from Karpathy's autoresearch repo, the pattern maps neatly onto prompt engineering: the skill file (`skill.md`) plays the role of `train.py` (the thing being optimized), and a `program.md` gives a high-level agent its instructions. The agent runs the skill repeatedly, scores outputs against an eval suite, and rewrites the prompt incrementally — looping on a timer (every 2–5 minutes) until the score converges or reaches a target.

### Eval Sets as the Core Primitive
Because LLM outputs are distributions rather than deterministic results, a single run cannot reliably distinguish a good prompt from a bad one. Saraev recommends running each prompt version at least 10 times and evaluating against binary (true/false) criteria to get a stable numeric score. The eval questions must be specific and measurable — not "does it look good?" but "is all text legible?", "does it use only pastel colors?", "is the layout strictly left-to-right or top-to-bottom?", and "is it free of numerical ordinals?".

### Research Log as a Durable Asset
Every iteration produces a record: what was changed, what score resulted, and why. Saraev argues this accumulated diff-and-score log is itself valuable — independent of the final optimized prompt. When more capable models become available, the entire research history can be passed to them as context, allowing optimization to resume without starting from zero. He positions this accumulated data as "one of the most important and valuable assets of our time."

### Cost-Bounded Optimization Budget
The method has a concrete economics model: at ~$0.02 per skill run and 10 runs per test, each iteration costs ~$0.20. Fifty iterations (enough to meaningfully optimize most skills) costs roughly $10. Saraev frames this as straightforward ROI for any repeatable professional workflow — the one-time cost to push a skill from ~80% to ~98% reliability is small compared to the downstream value of reliable outputs.

### Generalization Beyond Skills
The same three-ingredient structure (metric + measurement tool + changeable artifact) applies to any iterative AI optimization problem. Saraev demonstrates it on website load time (metric: milliseconds via Lighthouse; artifact: code) and cold email copy (metric: reply rate via Instantly analytics; artifact: email text). The pattern is a general-purpose agentic loop, not a skill-specific technique.

## Practical Takeaways

- **Define your eval before running autoresearch.** Start by listing 3–5 binary yes/no questions that a passing output must satisfy. These become your scoring rubric and determine what "better" means. Vague criteria ("looks professional") will produce useless scores.
- **Run 10 samples per iteration minimum.** Single runs are too noisy to distinguish prompt quality. Scoring the mode and median across 10 outputs gives a stable signal the optimizer can act on.
- **Let an agent write the test suite.** Pass your eval criteria and the autoresearch repo link to Claude Code and ask it to scaffold the evaluation harness, dashboard, and optimization loop. You provide the criteria; the agent handles the plumbing.
- **Save the research log, not just the final prompt.** The history of attempted changes and their scores is a reusable asset. Archive it alongside the skill so future model upgrades can continue where this run left off.
- **Budget ~$10–20 for 50–100 iterations.** At ~$0.20 per 10-sample test, meaningful skill optimization is cheap. Set a maximum iteration count or a target score threshold to avoid runaway costs.

## Notable Quotes

> "All machine learning and all AI outputs are distributions of data. And so in order for us to control against that and allow us to make iterations and improvements on them, we just need to run them many, many times."

> "I think this is actually probably soon to be one of the most important and valuable assets of our time — just a bunch of research data."

> "At any point in time over the course of the next few years, you just take this big list of things, just pass it on to the next agent. You could take this big list and pass it on to GPT-6 or Opus 5.0 and it'll be able to pick up where its predecessors left off."
