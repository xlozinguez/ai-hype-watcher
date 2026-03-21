---
source_id: "322"
title: "Building a REAL feature with Claude Code: every step explained"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=hX7yG1KVYhI"
date: "2026-03-18"
duration: "44:16"
type: "video"
tags: ["claude-code", "agentic-coding", "specification", "context-engineering", "task-system"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 322: Building a REAL feature with Claude Code: every step explained

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-18 | **Duration**: 44:16

## Summary

Matt Pocock walks through his complete end-to-end workflow for building a real feature using Claude Code in a mature production application (1,200+ commits, 637+ closed issues). The feature involves adding "ghost courses" and streamlined lesson creation/deletion to his course video manager application. The video demonstrates three distinct phases: a structured requirements-gathering session using a custom "Grill Me" skill, automated implementation via an AFK "Ralph" loop that processes GitHub issues sequentially, and a QA feedback cycle where bugs discovered during testing are filed as new issues and picked up by the running agent.

The key insight is that the human's primary job has shifted from writing code to thinking through requirements, reviewing outputs, and QA-ing the results. Pocock spends roughly 22 minutes in a grilling session to produce 8 bullet points of requirements, then hands implementation off to an autonomous agent while he goes for a walk. The entire workflow emphasizes treating AI as a delegatee rather than adopting some entirely new paradigm -- applying established software engineering practices (domain-driven design, testable modules, clear interfaces) to AI-assisted development.

## Key Concepts

### The Grill Me Pattern

Pocock uses a custom Claude Code skill called "Grill Me" that reverses the typical prompt flow. Instead of the developer telling the AI what to build, the AI asks probing questions to flesh out vague requirements. The skill uses subagent explores to examine the codebase, then challenges the developer's assumptions and asks edge-case questions. Pocock compares it to working with a skilled lead developer who asks smart questions for hours. The conversation produces a rich Q&A document that collocates questions with answers, creating hot spots for the attention mechanism.

### Ubiquitous Language as Context Bridge

Borrowing from Domain-Driven Design, Pocock maintains a "ubiquitous language" document in his codebase that defines precise terminology (e.g., "ghost lesson," "materialize," "materialization cascade"). This shared vocabulary bridges the gap between the human domain expert and the AI developer. When the AI encounters terms like "materialization cascade," it knows exactly what is meant. The document is updated after each grilling session to capture new terminology.

### The PRD-to-Issues Pipeline

After the grilling session, Pocock invokes a "Write PRD" skill that synthesizes the Q&A conversation into a concise product requirements document, which is then automatically posted as a GitHub issue. A second skill breaks the PRD into individual implementation issues with blocking relationships. These issues become the work queue for the AFK agent.

### The Ralph Loop (AFK Agent)

Pocock's "Ralph" loop spins up a Docker container that mounts the working directory, runs Claude Code headlessly, pulls GitHub issues, implements them sequentially, runs tests and type checks on every commit, and patches commits back to the local repo. The agent ran through 5 iterations producing 6 commits while Pocock was away for 90 minutes. The Docker isolation ensures safety, and commits are extracted as patches.

### Day Shift / Night Shift Model

The workflow splits naturally into human "day shift" work (thinking, grilling, QA) and AI "night shift" work (implementation). While the AFK agent implements previous sessions, the developer can open another terminal for a new grilling session. This parallelization is what makes the approach revolutionary -- the developer's work is essentially done once the thinking is complete, until QA.

### QA as Feedback Loop

During QA, Pocock uses an in-app feedback button that files issues directly to GitHub via Haiku-generated titles. He filed 6 issues in 8 minutes, and the Ralph loop picked them up in the background while he continued testing. This creates a tight QA-fix loop where human testing and AI fixing happen concurrently.

## Practical Takeaways

- **Spend more time on requirements than implementation**: Pocock spent 22 minutes grilling on requirements for 8 bullet points, then the AI did the rest. The more time invested in fleshing out ideas, the less correction needed later.
- **Maintain a ubiquitous language document**: Keep a glossary of domain terms that both humans and AI reference, updated after each session. This eliminates ambiguity in prompts.
- **Think in modules and interfaces, not implementation**: Review how modules change and how interfaces look, not the code itself. This is the human's value-add.
- **Use subagent explores for codebase understanding**: The "explore" pattern delegates codebase scanning to a subagent that returns a summary, keeping the parent agent's context window lean.
- **File QA issues while the agent is running**: Concurrent QA and fixing dramatically compresses the feedback cycle.
- **Specs-to-code alone will never work**: Edge cases surface during QA that are nearly impossible to plan for upfront. The iterative loop of build-QA-fix is essential.

## Notable Quotes

> "The more we do here, the less we're going to end up needing to do when we actually guide the LLM."

> "This is how I'm working with AI a lot. I block out half an hour in my calendar to work out exactly the feature I want. And from here, it's pretty much all on Rails."

> "This kind of stuff makes me think that the specs to code approach is just never going to work because when you're in there, when you're in the QA loop, when you're iterating towards something, you are going to find little weird edge cases like this that is really hard to plan for before."

> "I'm reviewing inputs and outputs. I'm interested in the code. Absolutely. I'm interested in how the interfaces are changing... But for me really what I'm doing is reviewing the outputs that come from AI."

## Related Sources

- [280: Leon van Zyl - Claude Code Loop](280-leon-van-zyl-claude-code-loop.md) — similar AFK agent loop pattern
- [281: Ray Amjad - Claude Code Interruptions](281-ray-amjad-claude-code-interruptions.md) — context management approaches
- [260: Chase - AI Six Levels Claude Code](260-chase-ai-six-levels-claude-code.md) — progressive skill levels in Claude Code usage

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — skills, CLAUDE.md, context discipline
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — subagents, builder/validator, AFK loops
