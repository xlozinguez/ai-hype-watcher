---
source_id: "070"
title: "Handoff Drift — Why Anthropic PMs Vibe Code Instead of Writing PRDs"
creator: "Dhyey Mavani"
platform: "LinkedIn"
url: "https://www.linkedin.com/in/dhyey-mavani/"
date: "2026-02-14"
type: "article"
tags: ["ai-sdlc", "vibe-coding", "capability-overhang", "enterprise-ai"]
curriculum_modules: ["06-strategy-and-economics", "02-prompting-and-workflows"]
---

# 070: Handoff Drift — Why Anthropic PMs Vibe Code Instead of Writing PRDs

> **Creator**: Dhyey Mavani | **Platform**: LinkedIn | **Date**: 2026-02-14

## Summary

Dhyey Mavani describes a concrete workflow change at Anthropic: product managers don't write PRDs. Instead, they use Claude Code to build the first version of the feature themselves, then ship an experiment. The whole company dogfoods it for weeks, and only then do they ship. This eliminates what Mavani calls **Handoff Drift** — the progressive degradation of intent as a specification passes through multiple handoffs (PM writes spec → Design interprets the spec → Engineering interprets the design → each handoff adds a week).

The results are hard to argue with: run-rate jumped from $18 to $98 in one year, Claude Code alone generated a $500M run-rate, and valuation nearly doubled to $350B. Mavani argues this isn't just an Anthropic-specific advantage — it's a generalizable pattern, but it requires a specific prerequisite: an AI-friendly codebase (Tailwind instead of custom CSS, microservices architecture, reduced codebase size).

## Key Concepts

### Handoff Drift

The central concept: every handoff between roles (PM → Design → Engineering) introduces information loss and interpretation drift. In a traditional org:
1. PM writes a spec
2. Design interprets the spec
3. Engineering interprets the design
4. Each handoff adds a week and introduces drift

The standard 4-week cycle (PRD → Design → Ticket → Sprint) compresses to **days** when the PM can "vibe code" the first prototype version directly. The person with the original intent — the PM — builds the first version, eliminating the telephone game.

### PM-as-Prototyper

This is a concrete evolution of the AI-SDLC: the PM role expands from "specification writer" to "prototype builder." The PM doesn't need to be a production engineer — they need to be able to use Claude Code to translate their intent into a working prototype that the team can dogfood. The engineering team then takes ownership for production hardening, scaling, and maintenance.

This is distinct from "PMs should learn to code" — it's "PMs should learn to direct AI agents that code." The skill is specification and intent communication, not programming.

### AI-Friendly Codebase as Prerequisite

Mavani explicitly calls out that this workflow has a prerequisite: the codebase must be AI-friendly. Requirements include:
- **Tailwind** (instead of custom CSS) — AI models handle utility-first CSS better than bespoke stylesheets
- **Microservices architecture** — smaller, bounded contexts that fit in a context window
- **Reduced codebase size** — less code for the model to navigate and understand

The thesis: infrastructure investment in making your codebase AI-friendly is what allows PMs to "vibe code" directly against production components.

### Compounding Learning Gap

If your experimentation cycle is 6 weeks and your competitor's is 3 days, they are running 13x more experiments per quarter. Compound that gap over a year, and it becomes insurmountable. The competitive advantage isn't just speed — it's the learning velocity that speed enables.

## Practical Takeaways

- **Eliminate handoffs by letting the intent-holder build**: The person who understands the "why" should build the first version, using AI to bridge the skill gap. This applies beyond PMs — designers, domain experts, and stakeholders can all prototype.
- **Invest in codebase AI-readiness**: Tailwind, microservices, clear module boundaries, and small bounded contexts make AI-assisted prototyping feasible. This is infrastructure investment, not cleanup.
- **Measure experimentation velocity, not just shipping velocity**: The compounding advantage is in learning cycles per quarter, not features shipped.
- **Dogfood before you ship**: Anthropic's workflow includes weeks of internal dogfooding between prototype and launch. The PM vibe-codes it, the whole company uses it, and only then does it go to production.

## Notable Quotes

> "Anthropic PMs don't write PRDs. They use Claude Code to build the first version of the feature themselves." — Dhyey Mavani

> "This is what happens when you eliminate Handoff Drift." — Dhyey Mavani

> "If your experimentation cycle is 6 weeks and your competitor's is 3 days, they are running 13x more experiments per quarter." — Dhyey Mavani

> "Question for you: Could your current codebase support a PM 'vibe coding' a feature, or would that break production immediately?" — Dhyey Mavani

## Related Sources

- [005: Most People Aren't Ready for Vibe Coding](005-nate-b-jones-vibe-coding-readiness.md) — Nate's vibe coding readiness assessment; Handoff Drift provides the organizational "why" for vibe coding adoption
- [018: The New AI-Driven SDLC](018-circleci-ai-sdlc.md) — AI-SDLC framework; PM-as-prototyper is a concrete phase evolution
- [042: The Real Problem with Vibe Coding](042-internet-of-bugs-vibe-coding-problem.md) — Counterpoint: vibe coding risks; Mavani's answer is dogfooding + engineering handoff for production hardening

## Related Curriculum

- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — AI-SDLC evolution, experimentation velocity as competitive advantage, organizational restructuring
- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Specification-as-prototype workflow, intent communication patterns
