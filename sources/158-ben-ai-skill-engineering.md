---
source_id: "158"
title: "How to build Claude Skills Better than 99% of People"
creator: "Ben AI"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=X3uum6W2xEI"
date: "2026-02-24"
duration: "18:36"
type: "video"
tags: ["skills", "claude-code", "context-engineering", "prompt-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 158: How to build Claude Skills Better than 99% of People

> **Creator**: Ben AI | **Platform**: YouTube | **Date**: 2026-02-24 | **Duration**: 18:36

## Summary

Ben AI presents a comprehensive framework for building agent skills — the reusable instruction packages that teach AI agents how to perform specific processes. The video positions skills as the middle ground between isolated chat interfaces (projects, custom GPTs) and fully deterministic automation platforms: skills provide guardrails and SOPs while preserving human-in-the-loop judgment and the ability to self-improve through use.

The core framework covers skill anatomy (skill.md as the process instruction, plus reference files for context), progressive disclosure (only metadata loads into context until the skill is triggered), and a structured approach to building skills: define triggers, set objectives, specify tool/MCP usage, lay out step-by-step processes with human-in-the-loop checkpoints, define output expectations, and add rules for edge cases. The video emphasizes iterative improvement — skills are never finished and get better with use.

## Key Concepts

### Skill Anatomy and Progressive Disclosure

A skill is a folder containing a skill.md (the process instruction) plus optional reference files (text docs, assets, code scripts). Progressive disclosure is the mechanism that makes thousands of skills viable: only the name and description sit in agent memory at all times. The full skill.md loads only when triggered, and reference files load only when the skill instructions call for them. This minimizes context window cost.

### Reference File Types

Skills can include text files (style guides, ICP documents, example outputs), MCP instruction files (how to use a specific tool for this process), non-text assets (images, presentations for output examples), and code scripts (Python/JS functions for API calls or custom actions). The skill.md should stay clean and process-focused; all additional context belongs in reference files.

### Skills vs. Plugins

Plugins are bundled packages of multiple skills, commands (workflow triggers that chain skills), specialized agent teams, and connectors. Plugins enable department-level distribution (sales plugin, marketing plugin) and are versionable across accounts. Three layers of skills are emerging: general-purpose (from Anthropic/OpenAI), marketplace skills (third-party, potentially monetizable), and company/individual customizations.

### The Skill Engineering Framework

1. **Define name and trigger** — how the agent recognizes when to use the skill
2. **Set objective** — concise goal statement
3. **Specify connectors/MCPs** — which tools and how to use them
4. **Lay out the process** — step-by-step with human-in-the-loop checkpoints, reference file usage per step, and expected outputs per step
5. **Add rules** — predict failure modes, enforce reference file usage, require multiple variations at decision points
6. **Enable progressive updates** — instruct the skill to self-improve by saving approved outputs as examples and updating rules based on user corrections

## Practical Takeaways

- **Prepare reference files before building** — business description, ICP, voice/personality guide, and strategy documents are reusable across multiple skills and dramatically improve output quality
- **Keep skill.md focused on process** — additional context belongs in reference files, not inline; this improves performance and maintainability
- **Always request multiple variations at human-in-the-loop steps** — choosing from 5 options is far more productive than iterating on single outputs
- **Build self-improving feedback loops** — instruct skills to save approved outputs as good examples and update rules when users flag issues
- **Iterate rather than perfect upfront** — the best skills are built through 4-5 rounds of use and refinement, not a single perfect prompt
- **Use structured QA boxes** — checkboxes, single-select, and open fields at decision points create better UX than free-form conversation

## Notable Quotes

> "Skills sit in the middle. They're essentially instructions for an AI agent on how to do a specific process. They can self-improve. They have human in the loop. But unlike a project or custom GPT, thousands of skills can be accessed by the same agent." — Ben AI

> "Building good skills is kind of like an art. It's the art of putting your domain expertise of a process into something productizable and usable for an agent." — Ben AI

## Related Sources

- [154: Why Most Developers Are Using Claude Code Wrong](154-diy-smart-code-claude-code-features.md) — Overview of where skills fit in the five-feature Claude Code model
- [157: How to actually force Claude Code to use the right CLI](157-matt-pocock-hooks-cli-enforcement.md) — Complementary hooks approach for deterministic enforcement

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system, context engineering
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Skill architecture, progressive disclosure, self-improving agents
