---
source_id: "146"
title: "Anthropic Just Dropped Claude Code Skills 2.0"
creator: "Ray Amjad"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=qXWz-V_XMOc"
date: "2026-03-04"
duration: "12:48"
type: "video"
tags: ["skills", "claude-code", "validation"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 146: Anthropic Just Dropped Claude Code Skills 2.0

> **Creator**: Ray Amjad | **Platform**: YouTube | **Date**: 2026-03-04 | **Duration**: 12:48

## Summary

Ray Amjad walks through Anthropic's updated Skill Creator plugin for Claude Code, which introduces eval-driven skill development, A/B testing, and trigger optimization. The new workflow replaces the previous vibes-based approach to skill creation (do it once, turn it into a skill, ship it) with a systematic process: create the skill, generate test cases, run parallel agents with and without the skill, blind-grade the results, and iterate on the skill instructions until they measurably improve output.

The video demonstrates two key capabilities: capability evaluation (does the skill produce better output?) and trigger optimization (does the skill activate reliably for the right prompts?). Anthropic's own testing showed their PDF skill achieving a 13.5% higher success rate with 22% faster task completion when the skill was loaded.

## Key Concepts

### Two Categories of Skills

Anthropic identifies two distinct skill types. **Capability uplift** skills fill gaps where the base model underperforms — handling PDFs, filling forms, creating PowerPoints. These have a natural retirement date: when the base model improves enough to match the skill's performance, the skill becomes unnecessary or even counterproductive. **Workflow/preference** skills encode specific processes or compliance requirements — release workflows, code review checklists, report generation from MCP servers. These persist as long as the workflow exists.

### Eval-Driven Skill Development

The Skill Creator spawns parallel agents — some with the skill loaded, some without — running identical prompts. A blind comparator grades the outputs without knowing which used the skill. This produces concrete metrics: success rate differential, completion time, and token usage. The process can run after model upgrades to determine whether existing skills are still needed, preventing skills from holding back improved base model capabilities.

### Trigger Optimization Loop

Skill descriptions determine when Claude Code activates them. The Skill Creator generates realistic prompts (both should-trigger and should-not-trigger), splits them into training and testing sets (60/40), and iteratively refines the skill description to maximize reliable triggering. The process identified that overly generic descriptions cause Claude to handle tasks without consulting the skill, even when the skill would produce better results.

## Practical Takeaways

- **A/B test your skills**: Use the Skill Creator to verify skills actually improve output. A skill that was useful three months ago may now be counterproductive with newer models.
- **Re-evaluate skills after model upgrades**: Capability uplift skills have natural retirement dates. Run the benchmark suite when moving to a new model version.
- **Optimize trigger descriptions**: If a skill isn't firing reliably, the Skill Creator can iteratively refine the description using a train/test split of realistic prompts.
- **Skills can be counterproductive**: If a skill encodes patterns the base model already handles well, loading it can hold the model back from its native capabilities.
- **Procedural evals for domain-specific skills**: For compliance or domain workflows, provide example inputs with expected outputs (e.g., insurance claim triage rules) and let the eval loop verify correctness automatically.

## Notable Quotes

> "Most people are developing Claude skills based exclusively on vibes." — Ray Amjad

> "It may be the case that Opus 4.6 isn't really that good at SEO auditing, but Opus 5 will be. So when Opus 5 comes around, you can run this skill comparison A/B test on any pre-existing skills." — Ray Amjad

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system, skill creation, plugin ecosystem
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Eval-driven development, validation patterns, A/B testing for agent tooling
