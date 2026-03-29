---
source_id: "407"
title: "A Practical Guide to AI Skills — Dori Wilson | Data Debug SF"
creator: "Recce"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Sgp5JH0ZcFc"
date: "2026-03-25"
duration: "13:00"
type: "video"
tags: ["skills", "claude-code", "mcp", "meta-prompts", "context-engineering", "agentic-coding", "prompt-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "02-prompting-and-workflows"]
---

# 407: A Practical Guide to AI Skills — Dori Wilson | Data Debug SF

> **Creator**: Recce | **Platform**: YouTube | **Date**: 2026-03-25 | **Duration**: 13:00

# A Practical Guide to AI Skills — Dori Wilson | Data Debug SF

## Summary

Dori Wilson, a data practitioner at Recce, presents a hands-on approach to building and iterating Claude Code skills for analytics engineering workflows. Skills are structured markdown files containing prompts, step-by-step workflows, golden examples, anti-patterns, rules/guardrails, links to other skills, and external references. Wilson argues that skills are the primary lever for getting consistent, personalized output from LLMs — superior to relying on out-of-the-box model behavior or SaaS tooling because they travel with you across models and remain fully under your control.

The talk centers on Wilson's analytics repository as a live case study: she connected dbt, Recce, and Notion MCPs and wired them into layered skills for source ingestion, staging, and intermediate table workflows. A concrete bug example shows how a staff analytics engineer persona embedded in a code review skill automatically caught a `MAX()` aggregation error in a weekly distinct-user rollup — a mistake the base model might not have flagged — and then the handoff skill captured that decision into a persistent memory file, updated the review skill to check for it going forward, and patched the code itself. This self-improving loop is the core mechanism Wilson advocates.

Wilson closes with a practical ramp-up path: start by turning your most-reused prompts into skills, let Claude draft and iterate the skill files from your existing PRs and session history, use MCP integrations to eliminate manual source-of-truth maintenance, and run post-session handoffs to continuously improve skill quality. She also notes Claude Code's built-in skills creator with eval support as an underused tool, and warns that proliferating too many skills (she hit 31) confuses the model — consolidation to 7–10 improved performance.

## Key Concepts

### Skills as Structured Markdown Workflows
A skill is a markdown file with defined sections: prompt (core instruction), step-by-step workflow, golden examples (what good looks like), anti-patterns, links to other skills, rules/guardrails, and references to external docs or schemas. Rather than re-prompting repeatedly, baking common instructions into skills means the LLM calls them automatically at the right moment without manual invocation. Wilson distinguishes between CLAUDE.md as global memory and skills as local, context-specific rules that fire when a particular task is underway.

### The Self-Improving Skill Loop
Every coding session feeds back into skill improvement. Wilson runs a post-session handoff that prompts multiple specialist personas (staff analytics engineer, AI engineer) to evaluate the session, captures decisions into a persistent decision doc, and rewrites relevant skills to encode new learnings. The key behavior change is narrating *why* you're asking for a change during the session so that reasoning is available for the handoff to capture — not just "fix this" but the rationale, as if briefing a junior engineer.

### Persona-Layered Code Review
A single code review skill can invoke multiple sub-prompts embodying different expert perspectives — staff analytics engineer, AI engineer, head of DevRel, chief of staff — depending on the repo context and audience. This pattern catches domain-specific errors (like the `MAX()` vs. `COUNT DISTINCT` bug) that a generic reviewer would miss, without requiring the practitioner to manually run each review themselves.

### MCP Integration as Source-of-Truth Automation
Wilson connects three MCPs to her analytics repo — dbt MCP, Recce MCP (for production vs. dev comparison), and Notion MCP (for event documentation maintained by engineers). Skills call these MCPs at the right workflow steps: e.g., when reviewing a PR, automatically pull Notion docs and check whether new events are correctly modeled in the int and fact layers. This eliminates manual data contract maintenance and cross-referencing.

### Skill Portability and Ownership
Because skills are plain markdown files in your own repo, there is no vendor lock-in. When a better model arrives, the skills transfer immediately. Wilson frames this as a fundamental shift from delegating workflow intelligence to SaaS tools toward owning it locally — the analytics equivalent of owning your own playbooks rather than licensing a vendor's methodology.

## Practical Takeaways

- **Start with your most-reused prompts.** If you're copy-pasting a prompt repeatedly in chat or CLI, that's the first skill to create. Hand it to Claude, describe your repo context, and let it draft the markdown file — then iterate from real sessions.
- **Use handoff skills to capture session reasoning.** Narrate your decisions during coding sessions so the handoff skill can extract and persist them. This turns every bug fix into a permanent guardrail in the relevant skill.
- **Keep the skill count manageable.** More than ~10 skills can degrade model performance. Use Claude Code's built-in skills creator and eval tooling to identify redundancy and consolidate.
- **Layer MCPs into skills rather than calling them manually.** Embed MCP calls (dbt, Recce, Notion, etc.) directly in the relevant skill so the agent knows when and how to use each tool without you specifying it each session.
- **Feed the AI your reasoning, not just your requests.** Explicitly stating *why* you want a change during a session enables the handoff skill to encode that reasoning into future skills, making the improvement loop much richer than just observing code diffs.

## Notable Quotes

> "Skills are just markdown files with structure... This is where you should be starting if you're new to skills or working on your own how-tos."

> "Every session creates knowledge. What my handoff skill does is it prompts a bunch of different agents... you want prompts that are customized to your repo and what you're trying to do."

> "Skills aren't a one-time build. They're a practice. Iterate on them. That's how you get involved."
