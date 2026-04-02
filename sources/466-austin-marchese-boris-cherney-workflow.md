---
source_id: "466"
title: "How Claude Code’s Creator Starts EVERY Project"
creator: "Austin Marchese"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=KWrsLqnB6vA"
date: "2026-04-01"
duration: "12:16"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "prompt-engineering", "validation", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows", "04-agentic-patterns"]
---

# 466: How Claude Code’s Creator Starts EVERY Project

> **Creator**: Austin Marchese | **Platform**: YouTube | **Date**: 2026-04-01 | **Duration**: 12:16

## Summary

Austin Marchese synthesizes publicly available interviews, tweets, and threads from Boris Cherney — creator of Claude Code — to reconstruct his personal workflow for starting and managing every project. The video focuses on six principles Boris applies consistently: beginning in plan mode before any code is written, maintaining a minimal CLAUDE.md file, giving Claude a self-verification loop, running parallel sessions for independent tasks, systematizing repeated workflows as slash commands or Claude Skills, and building with the assumption that models will continue improving rapidly.

The throughline across all six principles is disciplined context management: front-loading thinking, keeping instructions lean, and preserving fresh perspectives through parallel sessions. Boris's approach contrasts sharply with the common pattern of jumping straight into building, and the video grounds each principle with concrete failure modes (e.g., a bug fix that silently corrupted database values because the problem wasn't properly scoped upfront).

The final section introduces "the bitter lesson" framing — the idea that general model capability will always outpace specific scaffolding tricks — as a strategic lens for deciding where to invest effort. The implication is that time spent crafting elaborate prompts or bloated instruction files has diminishing returns, while time spent on information architecture and repeatable systems compounds.

---

## Key Concepts

### Plan Mode as a Pre-Build Gate
Boris reports starting ~80% of sessions in plan mode (Shift+Tab twice in the terminal), treating it as a mandatory thinking phase before any execution. The core insight is that AI optimizes for speed of resolution, not correctness of problem framing — so an under-specified request reliably produces a technically valid but wrong solution. The suggested interview-style prompt ("What are the core problems this solves? Who is this for? What does success look like? What should this not do?") forces explicit alignment before any code is written.

### Minimal and Iterative CLAUDE.md
Boris keeps his CLAUDE.md to a few thousand tokens and advocates deleting the entire file and rebuilding from scratch when it becomes bloated. His reasoning: model capability improves with each release, so rules that were necessary months ago are often now redundant — and a long instruction file introduces noise that causes Claude to miss the rules that actually matter. The prescribed discipline is to add rules only when the same problem recurs, not preemptively.

### Verification Loops
Boris's core claim is that giving Claude a tool to observe the output of its own work (e.g., opening a browser, running a workflow) produces 2–3x quality improvements. The practical implementation is to declare in CLAUDE.md how work should be verified *before* a task begins, so Claude states its verification plan upfront. This converts Claude from a one-shot executor into a feedback-aware agent.

### Parallel Sessions with Partitioned Contexts
Boris runs multiple Claude sessions simultaneously, each scoped to non-overlapping tasks. The key principle is that two context windows that have no knowledge of each other tend to produce better individual results — a fresh session has no accumulated assumptions fogging its judgment. This is positioned as a force multiplier: independent parallel work, not redundant concurrent work on the same problem.

### Inner Loop Systematization via Claude Skills
Repeated daily workflows (inner loops) should be codified as slash commands or Claude Skills — documented processes that execute consistently every time they're invoked. The distinction drawn is between a prompt (ad hoc instruction) and a skill (a full, repeatable play). The payoff is that once a workflow is captured, it runs identically on every future invocation without re-prompting.

---

## Practical Takeaways

- **Always enter plan mode before building**: Use Shift+Tab twice and run an interview-style prompt to surface unstated assumptions before any code is generated. The planning conversation is where the real quality leverage lives.
- **Keep CLAUDE.md short and reactive**: Add rules only when a problem repeats; periodically audit for redundancy using a cleanup prompt, or delete and restart. Bloat degrades rule adherence.
- **Embed verification intent into CLAUDE.md**: Instruct Claude to state how it will verify any work before starting — this surfaces tasks that lack clear success criteria and enables self-correction loops.
- **Partition parallel sessions deliberately**: Run concurrent sessions only on independent, non-overlapping tasks. Fresh context windows catch things that deeply-contextualized sessions miss.
- **Identify and document your inner loops as Claude Skills**: List repeated daily workflows and codify them as skills that execute consistently. A one-time documentation investment yields indefinitely repeatable execution.

---

## Notable Quotes

> "Probably 80% of my sessions I start in plan mode. And once the plan is good, it just stays on track. And it'll just do the thing exactly right almost every time."
> — Boris Cherney

> "Do the minimal possible thing in order to get the model on track. And if you delete your Claude.md and then the model is getting off track, that's when you kind of add back a little bit at a time."
> — Boris Cherney

> "Give Claude a way to verify its work. If Claude has that feedback loop, it will two to three x the quality of the final result."
> — Boris Cherney (via Twitter)

---
