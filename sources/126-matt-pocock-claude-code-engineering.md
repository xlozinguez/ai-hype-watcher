---
source_id: "126"
title: "How I use Claude Code for real engineering"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=kZ-zzHVUrO4"
date: "2025-10-27"
duration: "10:12"
type: "video"
tags: ["claude-code", "agentic-coding", "context-engineering", "prompt-engineering"]
curriculum_modules: ["03-context-engineering", "04-agentic-patterns"]
---

# 126: How I use Claude Code for real engineering

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2025-10-27 | **Duration**: 10:12

## Summary

Matt Pocock demonstrates his complete Claude Code workflow for real engineering tasks, walking through a multi-phase feature implementation on a live codebase. The video focuses on practical technique rather than capability hype — showing how to break large features into phases, preserve context across windows, and use GitHub issues as external memory to overcome context window limitations.

The core workflow starts with plan mode for exploration and clarifying questions, progresses through multi-phase planning, then shifts to auto-accept execution phase by phase. Pocock emphasizes two key rules in his memory file: extreme concision in all outputs (sacrificing grammar for readability) and forcing unresolved questions at the end of each plan. When context runs low, he creates a GitHub issue containing the checked-off plan, clears the context window, and resumes by fetching the issue. The result is a repeatable engineering process that chains multiple context windows together through external state.

## Key Concepts

### Plan Mode First, Always ([00:30](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=30))

Pocock begins every large feature in plan mode (activated via shift-tab in Claude Code). This forces the model to explore the codebase and ask clarifying questions before writing any code. The plan mode interaction becomes a multi-step form — the model asks specific implementation questions, Pocock answers, and the model refines its plan until no unresolved questions remain.

### Multi-Phase Planning ([03:30](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=210))

When a plan feels too large for a single context window, Pocock tells Claude to "make the plan multi-phase." This breaks the implementation into discrete phases that can be executed independently, each small enough to fit within context limits. Phases leave TODO markers in code for subsequent phases, creating natural handoff points.

### GitHub Issues as External Memory ([06:30](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=390))

Rather than storing plans in local files, Pocock uses `gh issue create` to save the current plan (with completed phases checked off) as a GitHub issue. After clearing the context window, he resumes work by telling Claude to "get GitHub issue #24 and enact phase 4." This creates an external memory store that persists across context windows and is shareable with collaborators.

### Concision as the Top Rule ([04:30](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=270))

Pocock's user memory file contains a directive: "In all interactions and commit messages, be extremely concise and sacrifice grammar for the sake of concision." He calls this his favorite rule — it produces plans that are easy to scan and reduces context consumption. Combined with the "unresolved questions" rule, it creates a tight feedback loop between planning and execution.

## Practical Takeaways

- **Start every large feature in plan mode**: Force the model to explore and ask questions before writing code. Use dictation to quickly answer clarifying questions.
- **Break plans into phases**: Tell Claude to "make the plan multi-phase" when a feature is too large. Execute phases sequentially, checking context usage between them.
- **Use GitHub issues for context persistence**: Create issues containing plans with checked-off phases. This lets you clear the context window and resume from any phase.
- **Add concision rules to memory**: "Be extremely concise, sacrifice grammar" dramatically improves plan readability and reduces token consumption.
- **Monitor context usage**: Run `context` between phases to check remaining window. Stage or commit changes between phases for clear diffs.

## Notable Quotes

> "Whenever I embark out on a big piece of work, I'm always thinking about creating a plan first." — Matt Pocock ([00:45](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=45))

> "Be extremely concise and sacrifice grammar for the sake of concision. That's why that plan is so concise and easy to read... it's 100% my favorite thing I've added to rules and I'm never taking it out." — Matt Pocock ([04:45](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=285))

> "The cool thing about having a multi-phase plan is that we can preserve it between different context windows and the LLM should have all the information it needs to carry it on." — Matt Pocock ([06:30](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=390))

## Related Sources

- [024: Agentic Coding 2026](024-jo-van-eyck-agentic-coding-2026.md) — Similar workflow patterns for agentic coding
- [064: Agentic Prompt Engineering](064-indydevdan-agentic-prompt.md) — Complementary prompt engineering techniques for agents
- [084: 60% Context Rot Rule](084-dylan-davis-context-rot-60-rule.md) — Context window management strategies
- [051: Claude Code Tips](051-simon-scrapes-claude-code-tips.md) — Additional Claude Code workflow optimizations
- [062: Claude Code Levels](062-simon-scrapes-claude-code-levels.md) — Progressive Claude Code mastery framework

## Related Curriculum

- [Module 03: Context Engineering](../curriculum/03-context-engineering/README.md) — External memory patterns, context window management, memory file configuration
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Plan-then-execute workflows, multi-phase implementation, agent-human feedback loops
