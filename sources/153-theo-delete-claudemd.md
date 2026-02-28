---
source_id: "153"
title: "Delete your CLAUDE.md (and your AGENT.md too)"
creator: "Theo (t3.gg)"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=GcNu6wrLTJc"
date: "2026-02-23"
duration: "29:15"
type: "video"
tags: ["claude-code", "context-engineering", "prompt-engineering", "ai-hype"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows"]
---

# 153: Delete your CLAUDE.md (and your AGENT.md too)

> **Creator**: Theo (t3.gg) | **Platform**: YouTube | **Date**: 2026-02-23 | **Duration**: 29:15

## Summary

Theo examines a recent study ("Are Repository-Level Context Files Helpful for Coding Agents?") that benchmarked the impact of CLAUDE.md and AGENT.md files on coding agent performance. The findings are stark: developer-provided context files only marginally improved performance (+4% average), while LLM-generated context files had a small negative effect (-3% average). Both increased costs by over 20%. The study tested across Sonnet 4.5, GPT-5, o1-mini, and Qwen 3, finding consistent results.

Theo validates these findings with his own experiment — running Claude Code with and without an init-generated CLAUDE.md on the same question. The version without CLAUDE.md completed faster (1:11 vs 1:29) and produced comparable results. He then shares his philosophy: use CLAUDE.md primarily as a diagnostic tool to discover what agents struggle with in your codebase, then fix the codebase rather than adding more instructions.

## Key Concepts

### The Study Results

A rigorous study tested three conditions: developer-written context files, no context files, and LLM-generated context files. Developer files showed only +4% improvement, LLM-generated showed -3% degradation, and both increased costs by 20%+. Context files led to increased exploration, testing, and reasoning — not better outcomes, just more token usage.

### Context Hierarchy and Distraction

Theo explains the prompt hierarchy: provider instructions > system prompt > developer message (CLAUDE.md/AGENT.md) > user prompt. Everything in the developer message layer is always present in context, costing tokens and potentially distracting the model. Mentioning TRPC in an AGENT.md biased the agent toward using TRPC even though the project had mostly migrated to Convex — the mere mention of a technology makes the model more likely to reach for it.

### The Pink Elephant Problem

Telling an LLM about something — even to say "don't use this" — makes it more likely to think about that thing. This is analogous to "don't think about pink elephants." If information is in context, it influences the model's behavior. The best approach is to not mention things you don't want the model to use, rather than explicitly prohibiting them.

### CLAUDE.md as Diagnostic Tool

Theo's approach: add an instruction telling the agent to flag surprising or confusing things it encounters and propose additions to the CLAUDE.md. He then uses 80% of these proposals not to update the file, but to identify codebase improvements — restructuring code, improving test coverage, or fixing confusing patterns. The CLAUDE.md becomes a signal for what needs fixing in the code itself.

### Strategic Misdirection

Theo advocates for intentionally misleading agents in productive ways. Examples: telling the agent a project is "super greenfield" so it doesn't waste time on migration patterns even when it's already live, or asking for step 3 when you actually need step 2 (the agent will fix step 2 to get to step 3). These prompt engineering tactics can be more effective than detailed context files.

## Practical Takeaways

- **Delete init-generated CLAUDE.md files**: The study shows they hurt more than help, costing 20%+ more with negligible or negative impact on task completion
- **If the model can find it in the code, don't put it in CLAUDE.md**: Package.json scripts, file structure, dependency info — all trivially discoverable
- **Use CLAUDE.md to steer away from consistent mistakes**: Only add entries when you observe repeated incorrect behavior that codebase changes cannot fix
- **Treat CLAUDE.md proposals as codebase diagnostics**: When the agent flags confusion, fix the code rather than adding more instructions
- **Reduce context sources to improve debuggability**: With fewer inputs (no bloated CLAUDE.md, minimal MCP servers, no downloaded rule files), it's easier to diagnose why the agent behaves incorrectly
- **Lie to your agents strategically**: Simplify the agent's mental model of the project to reduce overthinking and unnecessary caution

## Notable Quotes

> "If the info is in the codebase, it probably doesn't need to be in the agent MD file." — Theo

> "Why do we think the AI likes it more than us? Why are we giving them all of this useless information?" — Theo

> "Generally speaking, I feel like developers don't understand how powerful it is to lie or intentionally mislead the agents in ways that set both you and the agent up for more success." — Theo

## Related Sources

- [152: Matt Pocock - Never Run claude /init](152-matt-pocock-never-run-init.md) — Same conclusion from a different angle, focuses on instruction budgets and context window phases

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md best practices and when to use context files
- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Context engineering, prompt hierarchy, strategic prompting techniques
