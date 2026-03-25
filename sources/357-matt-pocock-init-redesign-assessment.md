---
source_id: "357"
title: "Claude Code tried to improve /init... Is it any better?"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=llwTBpPqo9A"
date: "2026-03-23"
duration: "11:17"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "prompt-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 357: Claude Code tried to improve /init... Is it any better?

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-23 | **Duration**: 11:17

# Claude Code `/init` Redesign — Hands-On Assessment

## Summary

Matt Pocock follows up on his earlier critique of Claude Code's `/init` command, which he argued produced bloated, unhelpful `CLAUDE.md` files. After publicly pushing for improvements — specifically advocating for progressive disclosure and minimal context files — the Claude Code team shipped a new experimental version of `/init` and Pocock tests it live against his real work repository.

The new `/init` asks upfront questions about project vs. personal `CLAUDE.md` files and whether to set up skills and hooks, then explores the codebase before making recommendations. Pocock walks through each proposed addition, aggressively challenging the agent to justify inclusions — often successfully getting it to drop items as redundant with hooks, existing code patterns, or skills. The session ends with a nearly empty `CLAUDE.md` (the one surviving line is later deleted too) and a single narrow skill for Effect package installation.

The overall verdict is cautious improvement: the new `/init` is meaningfully better than before, but still has weaknesses. It over-relies on the `ask_user` question UI (which Pocock finds unusable), accepts pushback too easily without steelmanning its own recommendations, and doesn't proactively suggest skills aggressively enough. Pocock frames the exercise explicitly as feedback to the Claude Code team.

## Key Concepts

### Instruction Budget as a Mental Model
Pocock treats the LLM's ability to act on instructions as a finite budget — not purely a token budget, but a cognitive/attention budget. He estimates around 500 usable instructions before quality degrades. Every line added to `CLAUDE.md` consumes from this budget, which means each inclusion must compete for space against the conversation context itself. This reframes the question from "is this useful?" to "is this *worth the cost* given everything else in context?"

### Progressive Disclosure via Skills
Rather than front-loading all project knowledge into `CLAUDE.md`, the preferred architecture keeps the root file minimal and offloads specific, rare, or complex guidance into skills that are only loaded when relevant. The Effect package installation example illustrates this: because installing Effect packages is rare, putting that guidance in a skill means the LLM only consumes those instructions when the skill is invoked, not on every task.

### Redundancy with Discoverable Context
A recurring test Pocock applies to each proposed `CLAUDE.md` line: *is this trivially discoverable from the codebase itself?* Testing patterns (like `create_test_db` and `truncate_all_tables`) appear in existing test files; build commands appear in `package.json`; library preferences are visible from actual usage. If Claude will explore the codebase anyway, documenting already-visible patterns is waste. The corollary: `CLAUDE.md` is most valuable for things that are *not* obvious from reading the code — conventions that run counter to defaults, or rationale that isn't encoded anywhere.

### Hook-First Enforcement
Where a hook can deterministically enforce a behavior (e.g., intercepting `npx tsc` and redirecting to `npm run type-check`), adding the same instruction to `CLAUDE.md` is redundant. Hooks provide guaranteed enforcement; `CLAUDE.md` provides probabilistic guidance. Pocock's preference is to reserve `CLAUDE.md` instructions for situations where no deterministic enforcement mechanism exists.

### LLM Sycophancy as a Real Problem in Agentic UX
Pocock notices throughout the session that the agent accepts nearly all of his pushback without resistance, often responding with "you're right" or "smart" rather than defending its original recommendations. He explicitly prompts the agent to steelman its own suggestions. This surfaces a design critique of `/init` itself: an init tool that caves to every user objection will produce under-specified setups for users who don't already have strong opinions. The tool should argue back more, not less.

## Practical Takeaways

- **Challenge every proposed `CLAUDE.md` line** by asking: (1) Is this already enforced by a hook? (2) Is this discoverable from the codebase? (3) Is this rare enough to belong in a skill instead? If any answer is yes, the line probably shouldn't be in `CLAUDE.md`.
- **Set `user_invocable: false` on skills that are only for agent use**, not human invocation — keeps your skills list clean and signals intent clearly.
- **Avoid the `ask_user` question UI in Claude Code skills** — the UX is broken enough that it actively harms the interaction; prefer the agent presenting a proposal document the user can react to in natural language.
- **Use the "stand up to me" prompt pattern** when you want Claude to justify a decision rather than capitulate: explicitly tell it to give you the strongest possible argument for its position before you accept or reject it.
- **Treat `/init` output as a starting draft, not a finished config** — even the improved version requires active curation. Users without strong context-management opinions will likely end up with over-specified files.

## Notable Quotes

> "The LLM can reasonably only handle like 500 instructions. And if you think about it, the conversation itself is full of instructions, right? I already have a hook that checks npx tsc. I would like you to stand up to me on this one. That's another one in the budget gone."

> "I don't want to burn it on something that doesn't happen very often... let's put the effect package installation stuff inside a specific skill that's invoked whenever we run effect packages. Then we'll be able to progressively disclose the rationale."

> "Make it less sycophantic. Make it more proactive in suggesting skills and make it provide the steelman argument against why it should include things in `claude.md`."
