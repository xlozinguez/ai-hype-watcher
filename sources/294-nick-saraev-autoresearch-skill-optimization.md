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

Nick Saraev demonstrates how to apply Andrej Karpathy's "AutoResearch" methodology — originally designed to autonomously optimize machine learning training runs — to Claude Code skills. The core insight is that skills are just prompts, and prompts produce noisy, distributional outputs. By treating the skill's markdown file as the "thing to optimize," wrapping it in an automated evaluation loop, and scoring outputs against binary criteria, you can run continuous self-improvement cycles overnight without human intervention.

The practical implementation has three components: a scoring metric (eval pass rate out of a fixed maximum), an automated measurement tool (an agent-written test suite that runs the skill repeatedly and scores each output), and the changeable artifact (the skill prompt itself). The example used is a diagram-generator skill scored across four binary criteria — legibility, color palette adherence, linear layout, and absence of numeric ordering — giving a max score of 40 per 10-run batch. The agent iterates on the prompt between batches, targeting a perfect score.

Saraev argues this approach generalizes well beyond skills: he also applied it to website load-time optimization (reducing load from ~1,100ms to 67ms across 67 iterations) and cold email copy. The compounding value he identifies is the *research log* itself — a full record of every attempted prompt change and its measured effect — which can be handed off to future, more capable models to continue optimization from where the current model left off.

---

## Key Concepts

### AutoResearch Loop Applied to Prompts
Karpathy's AutoResearch repo uses a team of agents to autonomously iterate on a process by measuring it against an objective metric and modifying the underlying artifact. Saraev maps this directly to skills: the skill `.md` file is the artifact (analogous to `train.py`), the agent's high-level instructions are the program spec (analogous to `program.md`), and the eval pass rate is the loss metric. The loop runs on a timer (every 2–5 minutes) without human intervention.

### Eval Sets as Binary Benchmarks
Because prompt outputs are inherently probabilistic distributions, a single run is insufficient to judge quality. The correct approach is to run the skill many times (e.g., 10 per batch), evaluate each output against a fixed set of binary yes/no questions, and track the aggregate score (mode and median across runs). Binary criteria are preferred because they eliminate subjective judgment and enable automated scoring by another agent. For the diagram example: legibility, color palette, linear layout, no numeric ordering — 4 criteria × 10 runs = 40-point max.

### Research Log as a Durable Asset
Each AutoResearch run produces not just an improved prompt but a full log of every change attempted and its measured effect. This log is portable — it can be passed to a more capable future model (GPT-6, Opus 5, etc.) to continue optimization without restarting. Saraev frames accumulated research logs as one of the most valuable AI-era assets: structured experimental history that compounds in value as model capability increases.

### Cost-Bounded Optimization
Running 10 diagram generations per batch at ~$0.02 each costs ~$0.20/batch. At 50 batches to reach target quality, total optimization cost is ~$10. This framing — calculating the dollar cost of getting a skill to production quality — makes the ROI concrete and helps practitioners decide how many iterations to fund.

### Objective Metric Requirement
AutoResearch only works if the evaluation metric is a real number, not a vibe or qualitative judgment. The methodology forces practitioners to operationalize "good output" into measurable, automatable criteria before the loop starts. This constraint is a feature: it surfaces ambiguous quality definitions early and makes the optimization target explicit and reproducible.

---

## Practical Takeaways

- **Define your eval criteria as binary questions before starting** — break "good output" into 3–6 yes/no checks that another agent can answer programmatically. Vague criteria like "looks professional" will not work; specific criteria like "all text is legible and grammatically correct" will.
- **Run batches of 10, not single tests** — prompt outputs are distributions; single-run evaluation is too noisy. Score the aggregate across 10 runs per iteration to get a stable signal for the optimizer.
- **Provide the AutoResearch repo URL directly to the agent** — Saraev's prompt pattern is: paste the repo link + your eval criteria + natural language instructions. The agent reads the repo, builds the test suite, and starts iterating autonomously.
- **Save the research log, not just the final prompt** — the iteration history of what was tried and what scores it produced is the durable asset. Store it alongside the skill file so future agents or more capable models can continue from the last checkpoint.
- **Budget the optimization explicitly** — calculate cost per batch (generations × cost per call) and set a target batch count before starting. A $10–$20 budget is typically sufficient to significantly improve a skill.

---

## Notable Quotes

> "Skills are just prompts, right? And prompts are inherently noisy. What I mean by that is sometimes you'll run a prompt and it'll do X. Another time you run a prompt and it'll do Y."

> "I think this is actually probably soon to be one of the most important and valuable assets of our time — just a bunch of research data."

> "The one thing that matters is just how much time you let it run on. So if it runs for a couple of days, couple of weeks, couple of months, you can..."

---
