---
source_id: "152"
title: "Why Auto-Generated CLAUDE.md Wastes Your Context Window"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=9tmsq-Gvx6g"
date: "2026-02-24"
duration: "10:37"
type: "video"
tags: ["claude-code", "context-engineering", "prompt-engineering"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows"]
---

# 152: Why Auto-Generated CLAUDE.md Wastes Your Context Window

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-02-24 | **Duration**: 10:37

## Summary

Matt Pocock argues strongly against running `claude /init` to generate CLAUDE.md files, demonstrating that auto-generated context files are filled with trivially discoverable information that wastes tokens on every request. He breaks down the agent's context window into four phases — system prompt, exploration, implementation, and testing — and explains why bloating the system prompt phase (which is fixed and non-flexible) directly reduces capacity for actual work.

The core argument is that LLMs have an effective instruction budget of 300-500 instructions, and filling CLAUDE.md with architecture descriptions, file paths, and commands that the agent can easily discover on its own squanders that budget. Information that exists in the codebase (package.json scripts, file structure, dependency imports) should not be duplicated in documentation that will rot as soon as the underlying code changes.

## Key Concepts

### The Four Phases of Agent Context Usage

Every agent session has four phases competing for context window space: (1) system prompt (fixed, includes CLAUDE.md), (2) exploration (discovering the codebase), (3) implementation (writing code), and (4) testing/debugging (feedback loops). The system prompt is the only non-flexible phase — everything else can expand or contract based on task complexity. Minimizing the system prompt maximizes available space for actual work.

### Instruction Budget

LLMs have a realistic instruction budget of 300-400 instructions (up to ~500 for larger models). Each statement in CLAUDE.md counts against this budget regardless of whether it's relevant to the current task. Architecture docs, file references, and command listings consume instructions globally even when only a fraction applies to any given task.

### Discoverable vs. Undiscoverable Information

Information that exists in source code (package.json scripts, import statements, file structure, config files) is trivially discoverable by the agent during its exploration phase. Duplicating this in CLAUDE.md creates a maintenance burden and risks going out of date. The only information worth putting in CLAUDE.md is things the agent genuinely cannot discover — like running on WSL, or behavioral preferences the agent consistently gets wrong.

### Skills as an Alternative to Global Context

Rather than putting steering information in CLAUDE.md (where it loads on every request), Matt advocates for putting it in skills that the agent can discover on demand. This way, React-specific guidance only loads during React work, not during API or documentation tasks.

## Practical Takeaways

- **Never run `/init`**: The generated CLAUDE.md is filled with trivially discoverable information that wastes tokens and will rot as code changes
- **Minimize CLAUDE.md to the absolute essential**: Matt's own CLAUDE.md contains a single line: "you are on WSL on Windows"
- **Use skills for domain-specific guidance**: Put React patterns, API conventions, etc. in discoverable skills rather than global context
- **Trust the exploration phase**: Modern agents are good at discovering codebase structure, commands, and patterns through their built-in exploration step
- **Every CLAUDE.md entry should pass the test**: "Does the agent consistently get this wrong, and can it not discover the correct answer on its own?"

## Notable Quotes

> "So either that means you need to burn tokens to keep this up to date which just feels crazy to me or you just delete it." — Matt Pocock

> "LLMs really only have a realistic instruction budget of around 300 to 400 instructions." — Matt Pocock

## Related Sources

- [153: Theo - Delete Your CLAUDE.md](153-theo-delete-claudemd.md) — Same topic from a different perspective, references a study on context file effectiveness

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md best practices and context management
- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Context engineering and instruction budgets
