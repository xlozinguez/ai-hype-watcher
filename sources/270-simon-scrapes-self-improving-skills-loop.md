---
source_id: "270"
title: "Build Self-Improving Claude Code Skills. The Results Are Crazy."
creator: "Simon Scrapes"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=wQ0duoTeAAU"
date: "2026-03-13"
duration: "11:02"
type: "video"
tags: ["claude-code", "skills", "agentic-coding", "validation", "meta-prompts"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 270: Build Self-Improving Claude Code Skills. The Results Are Crazy.

> **Creator**: Simon Scrapes | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 11:02

# Build Self-Improving Claude Code Skills. The Results Are Crazy.

## Summary

This video demonstrates how to apply Andrej Karpathy's "auto-research" loop concept to Claude Code skills, creating a system where skills automatically improve themselves overnight without human intervention. The core idea: define binary (true/false) assertions about desired skill output quality, run an evaluation loop, and have Claude autonomously edit the skill.md file, commit improvements, or revert failed changes — repeating until a perfect score is reached or the user interrupts.

The setup distinguishes between two separate skill improvement problems. The first is *activation* — ensuring the skill triggers at the right time — which is handled by Anthropic's built-in skill creator tool and its description improvement loop. The second is *output quality* — ensuring the skill produces structurally correct, on-brand results — which is what the Karpathy-style binary assertion loop addresses. Together they form a two-layer self-improvement system.

A critical insight is the emphasis on *binary assertions* over subjective quality metrics. Checks like "final line is not a question," "word count under 300," or "contains at least one specific number" can be validated programmatically as true/false, enabling full automation. Qualitative criteria like "compelling tone" still require human judgment and are handled separately through the skill creator's side-by-side dashboard workflow covered in the creator's prior video.

## Key Concepts

### Karpathy Auto-Research Loop Applied to Skills
The original pattern from Andrej Karpathy involves: make a change to a training script, run a test, read the metric, commit if improved, revert if worse, and never stop until manually interrupted. This video maps that pattern directly onto Claude Code skills by substituting the training script with `skill.md`, and the performance metric with a pass rate across binary assertions. The instruction "never stop" is explicitly included in the prompt to prevent the agent from pausing for human approval.

### Binary Assertions as the Automation Primitive
Binary (true/false) assertions are the key mechanism that makes the loop automatable. An `eval.json` file contains 25 assertions per skill (e.g., "first line appears as a standalone sentence," "total word count under 300," "does not contain em-dashes"). These are structurally checkable without human judgment, enabling fully autonomous pass/fail scoring. Subjective criteria like "compelling subject line" are explicitly excluded from this loop because two evaluators can disagree, breaking automation.

### Two-Layer Skill Self-Improvement
Layer 1 addresses *skill activation*: using the skill creator's built-in description improvement loop to ensure Claude triggers the skill reliably. Community testing showed activation rates as low as 20% with vague YAML descriptions. Layer 2 addresses *skill output*: the Karpathy-style binary assertion loop that iteratively edits `skill.md` to improve structural compliance. The layers are complementary and solve distinct problems.

### Git as the Rollback Mechanism
The improvement loop uses git commits to manage changes. When an assertion pass rate improves, the change is committed and the next iteration begins. When the score drops, the repository is reset to the previous commit and a different change is attempted. This gives the autonomous agent a reliable undo mechanism without any custom state management, making the system robust to bad edits.

### Eval Folder Structure and Bootstrap
Each skill gets an `eval/` subfolder containing an `eval.json` file. Each entry in the JSON specifies a prompt, an expected output type, and a list of binary assertions to check. The creator notes that Claude Code can generate this `eval.json` automatically by analyzing the existing `skill.md` — you ask it to "create an evals.json with assertions that can be validated as true/false based on my skill.md" — lowering the setup cost significantly.

## Practical Takeaways

- **Use binary assertions exclusively in autonomous eval loops.** Any assertion that requires subjective judgment (e.g., "is this compelling?") must be either reformulated as a structural rule or moved to a human-reviewed qualitative evaluation. Only true/false checkable criteria can be automated reliably.
- **Generate your `eval.json` with Claude Code.** Rather than hand-writing 25 assertions per skill, prompt Claude Code to analyze your `skill.md` and produce assertions it can validate programmatically. This bootstraps the loop quickly and ensures assertions match the actual documented behavior.
- **Include an explicit "never stop" instruction in your loop prompt.** Without this, Claude will pause and ask for permission to continue between iterations. The instruction should state the agent is autonomous, the human may be away, and it should loop until manually stopped or a perfect score is achieved.
- **Start with mature skills to validate your loop setup.** The example skill had already gone through ~5 iterations and scored 23/25 on first run, reaching perfect score in just two loops. A brand-new skill will need many more iterations — confirm the loop mechanics work before running it overnight on a fresh skill.
- **Reserve qualitative evaluation for reference file and tone checks.** The binary loop cannot verify whether the skill is correctly using context from reference files (tone guides, persuasion toolkits, example posts). Use the skill creator's side-by-side dashboard for those qualitative checks as a separate, human-in-the-loop process.

## Notable Quotes

> "Never stop. Once the experiment loop has begun, do not pause to ask the human if you should continue. Do not ask if I should keep going or is this a good stopping point. The human might be asleep or gone from the computer and expects you to continue working indefinitely until you are manually stopped. You are autonomous."

> "Triggering reliably and producing actual great outputs from the skills are different problems."

> "The binary loop handles structure, format, word counts, forbidden patterns, but it does not handle tone of voice, creative quality, whether your skill is actually using the context you've put in your reference files properly. Those still need a bit of human judgment."
