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

# Claude Code `/init` Improvements — Honest Assessment

## Summary

Matt Pocock revisits Claude Code's `/init` command after publicly criticizing it three weeks earlier for generating bloated, unhelpful `CLAUDE.md` files. Following community feedback (including Pocock's own suggestion to use "progressive disclosure" and keep `CLAUDE.md` extremely minimal), the Claude Code team shipped a new experimental version of `/init` that asks setup questions, explores the codebase, and proposes skills and hooks rather than dumping everything into a monolithic config file. Pocock runs it live against his real work repo to give honest feedback.

The new `/init` represents a genuine improvement: it proposes skills and hooks as first-class outputs rather than cramming guidance into `CLAUDE.md`, and it asks clarifying questions before acting. However, Pocock pushes back hard on nearly every proposed `CLAUDE.md` addition, arguing that most content is either trivially discoverable from the codebase itself, already enforced by hooks deterministically, or too narrow/ephemeral to earn a place in the LLM's "instruction budget." He ends up deleting nearly everything `/init` suggested for `CLAUDE.md`, keeping only one useful skill file.

The video doubles as a practical lesson in context discipline: every line in `CLAUDE.md` consumes part of a finite instruction budget the LLM has for following guidance. Pocock's mental model is that the LLM can only reliably act on roughly 500 instructions at once, so the bar for including anything in `CLAUDE.md` should be high — only information that is not discoverable from code, not enforced by hooks, and likely to persist over time.

---

## Key Concepts

### Instruction Budget as a Finite Resource

Pocock frames `CLAUDE.md` management through the lens of a fixed "instruction budget" — the LLM can only reliably process and act on a limited number of instructions (estimated ~500) at any time. Every line in `CLAUDE.md` competes with the actual conversation context and other directives. This framing provides a principled test for inclusion: does this line earn its spot, or is it redundant with something more authoritative (the codebase itself, a hook, a skill)?

### Progressive Disclosure via Skills

Rather than documenting everything in `CLAUDE.md` upfront, the preferred pattern is to encode specialized knowledge in skills that are only loaded into context when relevant. Example from the video: instead of a `CLAUDE.md` line about always using `npm install --force` for Effect packages (a rare operation), create a dedicated skill that gets invoked specifically for that scenario. This keeps base context lean while making specialized knowledge available on demand.

### Hooks as Deterministic Enforcement

Hooks already enforce certain behaviors deterministically (e.g., a hook that intercepts `npx tsc` and redirects to `npm run type-check`). Documenting the same rule in `CLAUDE.md` is redundant — the hook guarantees the behavior regardless of whether the LLM reads and follows the instruction. The test: "What does this `CLAUDE.md` line add that the hook doesn't already guarantee?"

### Codebase Discoverability Test

Before adding a pattern to `CLAUDE.md`, ask whether Claude would discover it naturally during an explore phase. If the codebase consistently uses `useEffectReducer` instead of `useReducer`, Claude will observe that pattern in existing code. Similarly, integration test patterns (specific DB setup utilities, etc.) will be found in existing test files. Only patterns that can't be inferred from the code warrant explicit documentation.

### Anti-Sycophancy Prompting

Pocock demonstrates a practical technique for getting more honest LLM responses during setup/planning: explicitly instruct the model to "stand up to me" and provide the "steelman argument" for its recommendation. LLMs default toward agreement, so asking them to argue for their position produces more useful signal about whether a recommendation is actually well-founded. He notes the new `/init` still falls short here — it agrees too readily when challenged.

---

## Practical Takeaways

- **Run the new `/init` but treat its `CLAUDE.md` proposals skeptically.** For each suggested line, ask: Is this already in the code? Is a hook enforcing this? Is this narrow/ephemeral? If yes to any, cut it.
- **Redirect narrow, rare instructions to skills instead of `CLAUDE.md`.** Skills provide progressive disclosure — the guidance only enters context when the relevant scenario arises.
- **Set `user_invocable: false` on skills that are meant for the agent's reference only**, not for manual invocation. Keeps the skill menu clean.
- **Strip boilerplate from `CLAUDE.md`.** The opener "This file provides guidance to Claude Code when working with code in this repository" wastes tokens — the LLM already knows this.
- **Use "stand up to me / steelman this" as a prompt modifier** when evaluating AI-generated configuration recommendations to counteract sycophantic agreement.

---

## Notable Quotes

> "I'm thinking about this not purely in terms of tokens. I'm thinking about this in terms of the budget that the LLM has for instructions... the LLM can reasonably only handle like 500 instructions. And if you think about it, the conversation itself is full of instructions."

> "What would adding this to the claude.md add that the hook doesn't already guarantee? Nothing. You're right. The hook already enforces it deterministically. Adding it to claude.md would be redundant."

> "Make it less sycophantic. Make it more proactive in suggesting skills and make it provide the steelman argument against why it should include things in claude.md."

---
