---
source_id: "248"
title: "Formalizing a proof in Lean using Claude Code"
creator: "Terence Tao"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=JHEO7cplfk8"
date: "2026-03-08"
duration: "26:29"
type: "video"
tags: ["claude-code", "agentic-coding", "context-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 248: Formalizing a proof in Lean using Claude Code

> **Creator**: Terence Tao | **Platform**: YouTube | **Date**: 2026-03-08 | **Duration**: 26:29

## Summary

Fields Medal-winning mathematician Terence Tao demonstrates using Claude Code to formalize a mathematical proof in the Lean theorem prover. The task — proving that equation 1689 implies equation 2 in an equational theories project — was previously done semi-manually with GitHub Copilot over a laborious step-by-step process. Tao's experience reveals that even world-class domain experts must adopt specific strategies to get productive results from AI coding agents.

After an initial failed attempt where Claude ran for 45 minutes, crashed his computer, and ran out of tokens without producing anything useful, Tao developed a step-by-step decomposition approach: define notation first, create a proof skeleton with placeholder `sorry` values, then fill in proofs incrementally. This mirrors the broader pattern seen across agentic coding — breaking complex tasks into constrained subtasks consistently outperforms giving agents large open-ended goals.

## Key Concepts

### Step-by-Step Decomposition Beats Monolithic Delegation

Tao's first attempt — asking Claude to formalize the entire proof at once — failed completely after 45 minutes and a system crash. His second attempt, breaking the task into discrete steps (define notation, skeletonize lemmas, fill in proofs one at a time), succeeded in about 25 minutes. The agent would "overthink" and backtrack endlessly when given the full problem, but performed well on constrained subtasks.

### Human-Agent Parallel Workflows

Tao demonstrates a practical coworking pattern: while Claude skeletonizes one lemma, he manually fills in proofs for another. When Claude struggled with a particular step, Tao stepped in, fixed it with a one-liner, and let Claude continue with the next task. The agent "didn't mind" that he was editing the same file — it independently applied its own edits alongside his. This co-editing workflow is a concrete example of keeping the human in the loop while still leveraging agent autonomy.

### Keeping Proofs Aligned with Informal Structure

Tao emphasizes the importance of instructing the agent to follow the informal proof's structure rather than inventing its own approach. When given free rein, Claude would "toss what you gave it and do its own thing," producing proofs that were harder to read, debug, and verify. By constraining the agent to formalize the existing human proof line by line, the output remained tractable and verifiable.

### Calibrating Automation Level

Tao explicitly discusses choosing "the level of automation that you're comfortable with." He could have done everything manually, delegated everything to Claude, or (as he chose) worked at an intermediate level — directing the agent on high-level structure while intervening on specific steps. This calibration mirrors the broader theme of humans as architects directing AI execution.

## Practical Takeaways

- **Decompose before delegating**: Write a step-by-step recipe for the agent rather than giving it a single monolithic task. Tao's markdown-style instructions in the Lean file guided Claude through each phase.
- **Use `sorry` as scaffolding**: In formal verification (and analogously in coding), create skeleton structures with placeholder implementations first, then fill in incrementally. This prevents the agent from going down rabbit holes.
- **Work in parallel with the agent**: Edit the same file simultaneously — pick the tasks you want to understand deeply, delegate the ones you're confident about.
- **Expect overthinking on "easy" steps**: Claude spent disproportionate time on what Tao considered the simplest proof steps, producing 5-line proofs where 2 lines would suffice. Token cost scales with agent uncertainty, not task complexity.
- **Prepare for crashes and restarts**: Step-by-step workflows are more resilient to interruptions. Tao's system crashed mid-session but he could resume cleanly because each step was independently meaningful.

## Notable Quotes

> "When I first did this, it would spend quite a lot of time working out how to prove these lemmas and then making mistakes and catching it and then redoing it and not actually getting anything done. Just overthinking it quite a bit." — Terence Tao

> "I think the best use case is where you keep involved, you just pick and choose the tasks that you want to work on so that you get some idea as to what's going on, and then in the background, things that you're not so worried about, you give to this agent." — Terence Tao

> "If you rely too much on these tools and something goes wrong, you may have no idea what to do other than just call it over and over again." — Terence Tao

## Related Sources

- [004: Agent Teams Setup](004-bart-slodyczka-agent-teams.md) — Task decomposition patterns for agent workflows
- [011: Context Engineering](011-confluent-developer-context-engineering.md) — Managing context windows for complex tasks

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Practical Claude Code usage patterns
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Human-agent collaboration and task decomposition
