---
source_id: "407"
title: "A Practical Guide to AI Skills — Dori Wilson | Data Debug SF"
creator: "Recce"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Sgp5JH0ZcFc"
date: "2026-03-25"
duration: "13:00"
type: "video"
tags: ["skills", "claude-code", "mcp", "context-engineering", "meta-prompts", "prompt-engineering", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 407: A Practical Guide to AI Skills — Dori Wilson | Data Debug SF

> **Creator**: Recce | **Platform**: YouTube | **Date**: 2026-03-25 | **Duration**: 13:00

# A Practical Guide to AI Skills — Dori Wilson | Data Debug SF

## Summary

Dori Wilson presents a practical framework for building and iterating on AI skills—structured markdown files that encode prompts, workflows, golden examples, anti-patterns, and guard rails for LLM-assisted development. Drawing from her analytics engineering work, she demonstrates how skills move beyond one-off prompting into a self-improving system where the AI is guided by accumulated institutional knowledge. The talk is grounded in real data workflows (dbt, S3 ingestion, fact tables) but the principles apply broadly across engineering contexts.

The core argument is that skills compound. Rather than treating each LLM session as disposable, Wilson's approach captures decisions, bugs, and reasoning into memory files and skill updates so future sessions inherit past learning. A handoff skill runs at the end of every session to extract decisions, update rule files, and refine existing skills—turning each coding session into an investment in the system's long-term quality. She also introduces a self-improving loop where Claude itself acts as a reviewer (in the persona of a staff analytics engineer or AI engineer) to critique and update the skills after each session.

Wilson is notably opinionated about skills hygiene: she went from 31 skills down to 7–10 after finding that too many skills confused the model. She also advocates for portability—owning your skills means no lock-in to any platform or model, and customized skills outperform generic out-of-the-box behavior. MCPs (dbt, Recce, Notion) are treated as integration points that skills coordinate rather than primary tools.

## Key Concepts

### Skills as Structured Knowledge Files
Skills are markdown files containing prompts, step-by-step workflows, golden examples of good output, anti-patterns to avoid, links to other skills, blocking rules/guard rails, and references (schemas, docs, MCPs). They function as persistent, composable context that the AI loads when executing specific tasks—replacing the need to re-explain preferences and standards in every session.

### The Self-Improving Loop
After each coding session, Wilson runs a handoff skill that prompts Claude to review the session from multiple personas (staff analytics engineer, AI engineer), captures decisions into a decision log, and rewrites existing skills based on newly discovered bugs or edge cases. This turns iterative development into a ratchet: skills only get more accurate and more specific over time.

### Golden Examples and Anti-Patterns as Guardrails
LLMs have no inherent sense of what "good" looks like for a specific codebase. Skills bridge this gap by encoding concrete examples of correct outputs and explicit anti-patterns (e.g., "never use `MAX()` for weekly distinct user counts—use `COUNT(DISTINCT)`"). This is where skills provide value that generic model behavior cannot: they capture domain-specific correctness standards.

### Skill-Scoped Memory
Rather than loading all context into a single bloated `CLAUDE.md` file, skills can call separate, scoped memory files for specific layers (e.g., int layer preferences vs. staging layer rules). This prevents context pollution and gives the model cleaner, more relevant working memory for each task type.

### MCPs as Skill-Coordinated Integrations
MCPs (dbt, Recce, Notion) connect the AI to live systems—running queries, comparing production vs. development, and checking documentation alignment. Skills encode *when* and *how* to invoke these MCPs, so the model knows to pull Notion docs during a review or use Recce for production/dev diffs without the user having to orchestrate this manually each time.

## Practical Takeaways

- **Start from a prompt you already reuse.** If you're typing the same instruction repeatedly in a chat box or CLI, that's your first skill. Have Claude structure it into a proper skill file using your existing codebase and any past PRs as raw material.
- **Feed the AI your reasoning, not just your commands.** When working with Claude, explain *why* you're making a change—this reasoning gets captured by the handoff skill and improves future skill quality. Treat it like a junior engineer call you're documenting for the record.
- **Keep skill count disciplined.** More than ~10 skills degrades model performance as it struggles to choose correctly. Use Claude Code's built-in skills creator and eval runner to audit and consolidate.
- **Turn bugs into rules immediately.** When the AI makes a mistake (like the `MAX` vs `COUNT DISTINCT` example), don't just fix the code—update the relevant skill's anti-patterns and decision log so the same bug cannot recur in future sessions.
- **Skills are portable assets.** Don't outsource this knowledge to SaaS tooling. Skills you maintain locally move with you across models and platforms and perform better than generic alternatives because they're tuned to your specific repo and workflows.

## Notable Quotes

> "AI skills are just markdown files with structure... Golden examples—what does good look like? LLMs have no effing idea. But the skills can tell them, right? And this is where to put it—in the place that the AI needs it most, which is when it's trying to do a new action."

> "Skills aren't a one-time build. They're a practice. Iterate on them. That's how you get value."

> "No more lock-in. Own your skills... Take your skills with you when there's a better model. Just use it. Don't rely on their models, their skills. You can just have your own."
