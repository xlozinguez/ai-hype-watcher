---
source_id: "494"
title: "Everything We Got Wrong About Research-Plan-Implement -  Dexter Horthy"
creator: "MLOps.community"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=YwZR6tc7qYg"
date: "2026-03-24"
duration: "26:46"
type: "video"
tags: ["prompt-engineering", "agentic-coding", "context-engineering", "meta-prompts", "ai-sdlc"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 494: Everything We Got Wrong About Research-Plan-Implement -  Dexter Horthy

> **Creator**: MLOps.community | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 26:46

# Everything We Got Wrong About Research-Plan-Implement

## Summary

Dexter Horthy (Dex) presents a candid retrospective on the Research-Plan-Implement (RPI) methodology for AI-assisted coding, which his team developed and open-sourced to significant adoption. Rather than defending their original approach, he acknowledges core failures discovered through working with thousands of engineers across startups and Fortune 500 companies: the workflow required "magic words" to function correctly, planning prompts exceeded the instruction budget of frontier LLMs (~150-200 reliable instructions), and the advice to read plans instead of code was actively harmful. The methodology produced great results for expert practitioners who internalized its nuances but failed to transfer well to broader teams.

The core errors cluster around two themes: context window mismanagement and misplaced human oversight. Monolithic planning prompts with 85+ instructions competed with system prompts, tool definitions, and MCP configs, causing models to inconsistently follow the workflow. Meanwhile, telling engineers to review 1000-line plan files instead of code was not leverage—plans and code diverged, requiring double the review work. Dex is emphatic that "no slop" is the 2026 imperative, targeting 2-3x productivity gains with near-human quality rather than 10x gains that require throwing everything away in six months.

The talk closes with architectural fixes: separating context windows to prevent the research phase from being contaminated by implementation intent, reducing instruction counts per prompt to stay within reliable adherence limits, and making the "work back and forth with me" behavior deterministic rather than prompt-dependent. The central philosophical position—do not outsource the thinking—remains unchanged, but the mechanisms to enforce it have been redesigned.

## Key Concepts

### The Instruction Budget Problem
Frontier LLMs reliably follow approximately 150-200 instructions. Once a prompt—combined with system prompt, tool definitions, MCP configuration, and CLAUDE.md—exceeds that budget, the model begins inconsistently attending to instructions. A monolithic planning prompt with 85+ instructions stacked on top of everything else explains why the workflow skipped critical interactive steps for ~50% of users. The fix is decomposition: smaller, focused prompts with clearly bounded tasks rather than one giant orchestration prompt.

### Research Contamination and Context Separation
Good research should be purely factual—an objective compression of how the codebase works today. If the model knows what is being built during the research phase, it produces opinions and implementation suggestions instead of facts. The solution is deterministic context separation: one context window generates research questions, and a fresh context window with no knowledge of the planned feature executes the research. This mirrors query planning patterns from information retrieval and prevents the model from front-loading its implementation biases into the research artifact.

### Plans vs. Code: Leverage Inversion
The original RPI advice was to read and review plans (sometimes via PR), not code. This was wrong. Plans and implementation diverge—surprises happen—so a reviewer who approves the plan must re-review the code anyway, doubling effort rather than creating leverage. The corrected position is: skip reviewing plan files, read the actual code. Since both require roughly the same effort, the plan review step was pure overhead with false confidence as a side effect.

### "Magic Words" as a Tool Design Failure
The planning workflow only reliably produced interactive, question-driven behavior when users said the phrase "work back and forth with me starting with your open questions and outline before writing the plan." This was not the users' fault—it was a tool design failure. If a professional workflow requires undocumented incantations discovered through hours of practice, the tool is broken. The lesson generalizes: any agentic workflow that depends on a user knowing the magic words to unlock correct behavior needs to be redesigned so the correct behavior is the default.

### Quality Ceiling and the Slop Problem
Chasing 10x productivity multipliers with autonomous agent swarms generates technical debt that collapses the gains—the team's own experience involved ripping out and replacing large parts of a system built without reading the code. The more durable target is 2-3x productivity at near-human quality levels. This reframes the goal: not maximum velocity, but sustained velocity without accumulation of unreviewed AI-generated code that nobody understands or owns.

## Practical Takeaways

- **Read the code, not the plan.** Plan files and implementation diverge; reviewing both is not leverage. Allocate your review budget to the actual code going to production.
- **Decompose prompts aggressively.** Keep each prompt in an agentic workflow well under the ~150-200 instruction reliability ceiling. Stack planning prompts on top of system prompts, MCP, and tool definitions mentally before deploying—total instruction count matters.
- **Separate research context from implementation intent.** Never tell the research sub-agent what you're building. Use a dedicated context window for question generation, then a fresh context for codebase exploration, to get facts rather than opinions.
- **Make correct behavior the default, not the reward for saying magic words.** If your workflow only works when users know undocumented phrases, redesign it so the interactive/validation steps are structurally enforced, not prompt-dependent.
- **Target 2-3x productivity with quality, not 10x with slop.** Unreviewed AI code accumulates hidden debt; the engineer remains accountable and must own the code. Velocity without comprehension is not sustainable.

## Notable Quotes

> "If you built a tool that requires hours and hours of training and reps to get good results from, go fix the tool."

> "Leverage is about doing less work to get more output. So the new advice: don't read the plans. Please read the code."

> "We tried not reading the code for like six months. It did not end well. We had to rip out and replace large parts of that system."

---
