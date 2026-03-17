---
source_id: "287"
title: "Claude Code Skills Just Got Even Better"
creator: "Nate Herk | AI Automation"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=RAZVk5NPNtE"
date: "2026-03-05"
duration: "16:15"
type: "video"
tags: ["claude-code", "skills", "prompt-engineering", "meta-prompts", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 287: Claude Code Skills Just Got Even Better

> **Creator**: Nate Herk | AI Automation | **Platform**: YouTube | **Date**: 2026-03-05 | **Duration**: 16:15

# Claude Code Skills Just Got Even Better

## Summary

Nate Herk walks through Anthropic's updated **skill creator skill** — an official plugin that encodes Anthropic's best practices for building, testing, and refining Claude Code skills. The video explains the two fundamental skill types (capability uplift vs. encoded preference), why the distinction matters for long-term durability, and how the new skill creator adds evaluation, benchmarking, and trigger-tuning capabilities that previously required manual iteration.

The second half is a live demo where Nate installs the skill creator plugin and uses a single high-level natural language prompt to generate a "YouTube Weekly Roundup" skill — one that pulls video stats, analyzes engagement, and produces a branded PDF report. The agent plans, builds, and self-evaluates the skill in one session, illustrating the broader trajectory Anthropic has signaled: eventually, a plain-English description of what you want should be sufficient for the model to construct a complete, optimized skill.

The video is practically useful as a workflow guide (installing via `/plugins`, running evals, using plan mode for skill creation) and conceptually useful for understanding how skills age — capability uplift skills may become obsolete as base models improve, while encoded preference skills encoding personal or organizational workflows should remain durable.

---

## Key Concepts

### Capability Uplift vs. Encoded Preference Skills
The two skill types have very different shelf lives. **Capability uplift skills** inject domain knowledge the base model lacks (e.g., design conventions, Excel formulas) — these may become redundant as models improve. **Encoded preference skills** encode a specific, sequential workflow (e.g., a multi-agent idea-mining pipeline) that reflects personal or organizational process; because future models won't be trained on your specific preferences, these skills remain durable and valuable over time. Understanding which type you're building shapes how much you invest in it and when to retire it.

### The Skill Creator Skill
Anthropic released an official plugin (`skill-creator`) that is itself a skill — a markdown file encoding all of Anthropic's best practices for skill design, distilled from their 33-page guidance document. It can create skills from scratch, modify existing ones, run evals against example outputs, produce pass-rate/time/token benchmarks, and tune skill trigger descriptions for more accurate invocation. Installing it via `/plugins → manage plugins → search "skill-creator"` gives any project access to this meta-capability.

### Skill Evaluation and Regression Testing
The eval system serves two opposing purposes: catching **regressions** (a model update causes a previously good skill to underperform) and spotting **growth** (a model improves enough that the skill is no longer needed). Running benchmarks with and without a skill loaded — comparing pass rate, latency, and token usage — gives quantitative signal for both. This reframes skills as living artifacts that need versioned testing, not set-and-forget prompts.

### Trigger Tuning
As a project accumulates 10+ skills, false triggers and misfires become a real problem — the agent calls the wrong skill or no skill at all. The skill creator's trigger-tuning feature analyzes a skill's description, tests a range of natural language invocation phrases, and rewrites the description to improve trigger accuracy. This is distinct from improving the skill's output quality; it's specifically about routing correctness within a multi-skill environment.

### Natural Language Skill Specification (Future Direction)
Anthropic explicitly stated that "over time, a natural language description of what the skill should do may be enough, with the model figuring out the rest." The live demo validates this direction: a single vague prompt ("give me a weekly YouTube roundup as a branded PDF") produced a structured plan, a working skill, an HTML-to-PDF template using brand assets, and a self-evaluation pass — without the creator specifying any technical implementation details. The gap between operator intent and skill implementation is closing rapidly.

---

## Practical Takeaways

- **Install the skill creator as a project plugin** via `/plugins → manage plugins → skill-creator`. Restart Claude Code after install and verify with "do you have the skill creator skill?" before relying on it.
- **Audit your existing skills by type**: review each skill to determine if it's capability uplift or encoded preference. Prioritize maintaining and evaluating the encoded preference ones; schedule periodic benchmark checks on capability uplift skills against new model releases.
- **Use plan mode for new skill creation**: switching to plan mode before prompting the skill creator lets you review the agent's interpretation and propose adjustments before any files are written — especially important for complex, multi-step encoded preference skills.
- **Run benchmarks when a new model drops**: the skill creator's benchmark feature (pass rate, time, tokens — with and without skill loaded) is the fastest way to determine whether to keep, update, or retire a skill after a model update.
- **Give the skill creator feedback in context**: after an initial skill generation, provide explicit qualitative feedback (e.g., "design is good but data sourcing is wrong") rather than starting over. The eval loop is designed for iterative refinement within the same session.

---

## Notable Quotes

> "Over time, a natural language description of what the skill should do may be enough with the model figuring out the rest." — Anthropic (quoted in the video)

> "With an encoded preference skill, these will probably stay pretty durable and accurate because the process is very specific usually to you, which Opus 5 won't be trained on most likely."

> "Most people that are using skills right now are actual just like executives and managers and operators. They're not engineers, which means we're really good at being able to explain what we want, the metrics we need to hit, and why we need that, but maybe not all of those technical nitty-gritty details."

---
