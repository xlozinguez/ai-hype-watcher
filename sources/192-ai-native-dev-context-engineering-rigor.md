---
source_id: "192"
title: "Applying Software Engineering Rigor to Context Engineering"
creator: "AI Native Dev"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=TlC7jq4ooSM"
date: "2026-02-25"
duration: "29:35"
type: "video"
tags: ["context-engineering", "skills-ecosystem", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 192: Applying Software Engineering Rigor to Context Engineering

> **Creator**: AI Native Dev | **Platform**: YouTube | **Date**: 2026-02-25 | **Duration**: 29:35

## Summary

Drew Knox (Head of Product and Design at Tessle, former research scientist leading language modeling teams at Grammarly) argues that context engineering should adopt the same disciplined tooling that traditional software development relies on: static analysis, unit tests, integration tests, observability, automation, and package management. The core thesis is that developers have become tech leads managing agent workers rather than writing code themselves, and context is effectively their new code — which means it deserves the same rigor.

The talk systematically maps every SDLC practice to a context engineering analog. Static analysis becomes LLM-as-judge validation against best practices. Unit tests become eval scenarios run multiple times with statistical averaging. Integration tests become full-repo coding scenarios with grading rubrics. Observability means mining agent chat logs for failure patterns. Build automation means CI/CD that detects when PRs should trigger context updates. Package managers (skills.sh, Tessle's registry) handle reuse, with the added wrinkle that context often describes versioned dependencies that can drift.

## Key Concepts

### Context as Code — The Full Analogy

Every traditional software tool has a context engineering counterpart. Static analysis maps to LLM-as-judge linting against Anthropic's best practices. Unit tests map to eval scenarios — prompts paired with grading rubrics, run N times to measure statistical improvement. Integration tests map to full-repo coding scenarios that stress-test all context together. Observability maps to mining agent session logs for patterns (search for "sorry" and "you're absolutely right" as failure indicators). Build scripts map to CI/CD that auto-generates context update PRs when code changes. Package managers handle reusable context with version-pinning challenges.

### Eval Design for Context

Rather than writing unit tests with example projects and test suites (which developers won't maintain), the recommended approach is writing grading rubrics checked by LLM-as-judge. This catches things unit tests cannot — like whether idiomatic code was written or the intended library was actually used instead of a reimplementation. About five eval scenarios per piece of context provides reliable measurement. Crucially, evals should be run with and without context to prove the context actually helps.

### The Dumb Zone and Context Pruning

Too much context degrades agent performance — a phenomenon called "the dumb zone." Evals help detect when context should be deleted, not just added. Example: Python style guides were essential six months ago but Claude Opus 4.6 writes good Python without them. Running evals without changing context also catches model regressions — a recent Gemini version stopped reading tools and context, requiring beefed-up instructions.

### Keeping Context Fresh via Automation

Out-of-date context destroys agent performance. The solution is CI/CD automation: on every PR, have an agent scan changes and identify markdown files that need updating. Because PRs tend to be focused, agents handle this surprisingly well. A related challenge is version drift between context describing a library and the library's actual pinned version.

## Practical Takeaways

- **Validate context statically**: Check that skills compile, trigger descriptions are specific, and best practices are followed — put this in CI/CD as table stakes.
- **Write eval scenarios, not unit tests**: Five prompt-plus-rubric pairs per context piece, run multiple times, compare with-context vs. without-context statistical averages.
- **Mine agent logs for insight**: Search chat transcripts for apology patterns ("sorry", "you're absolutely right") to identify missing or broken context.
- **Automate context freshness**: Set up PR-triggered agents that scan for documentation that needs updating when code changes.
- **Delete context as models improve**: Use evals to detect when agents no longer need specific guidance, and strip it to save tokens.

## Notable Quotes

> "We have effectively had general purpose agentic development machines for 50 years. We just called them software engineers. You never just wrote somebody a Slack message and expected them to go build an entire system and just like make all the best decisions." — Drew Knox

> "If you cloned me, I would still code review my code. I would never accept anyone to submit things without looking at it." — Drew Knox (quoting his wife, a staff engineer at Meta)

> "We had style guides for Python. Claude Opus 4.6 writes a pretty damn good Python. It doesn't need a style guide anymore. Your eval can tell you that and help you delete context that you no longer need." — Drew Knox

## Related Sources

- [040: Automating CLAUDE.md Context](040-charlie-automates-claudemd-context.md) — Practical implementation of context engineering for Claude Code
- [115: The Ralph Wiggum Technique](115-matt-pocock-ralph-wiggum-technique.md) — Context window management across agent iterations
- [160: Agentic Coding Missing Semester](160-missing-semester-agentic-coding.md) — Context discipline and agent workflow patterns
- [154: Claude Code Power Features](154-diy-smart-code-claude-code-features.md) — Skills, context engineering, and MCP in practice

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md, skills, context discipline
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Eval-driven context iteration, agent observability
