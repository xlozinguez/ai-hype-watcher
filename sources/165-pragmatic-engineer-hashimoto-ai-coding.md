---
source_id: "165"
title: "Mitchell Hashimoto on AI Coding, Ghostty, and the Open Source Quality Crisis"
creator: "The Pragmatic Engineer"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=WjckELpzLOU"
date: "2026-02-25"
duration: "1:58:23"
type: "video"
tags: ["agentic-coding", "claude-code", "vibe-coding", "ai-landscape"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "01-foundations"]
---

# 165: Mitchell Hashimoto on AI Coding, Ghostty, and the Open Source Quality Crisis

> **Creator**: The Pragmatic Engineer | **Platform**: YouTube | **Date**: 2026-02-25 | **Duration**: 1:58:23

## Summary

A deep two-hour conversation between Gergely Orosz (The Pragmatic Engineer) and Mitchell Hashimoto, co-founder of HashiCorp and creator of Terraform, Vagrant, and Ghostty. The interview covers Hashimoto's full journey — from self-taught teen programmer to building the infrastructure tools that power modern cloud — before diving into how he integrates AI coding tools into his daily workflow and the crisis AI is creating for open source.

Hashimoto's approach to AI coding is pragmatic and hands-on: he always keeps an agent running in the background, uses Claude Code and Codex daily, and adjusts his review rigor based on stakes. For his terminal project Ghostty, he reviews everything; for a family wedding website, he ships without reading the code. His perspective on open source is especially sharp — AI contributions have degraded signal-to-noise ratios so severely that Ghostty is moving to an invite-only contribution system inspired by Lobsters.

## Key Concepts

### Always Have an Agent Running

Hashimoto's core workflow principle is that an agent should always be doing something while he works. If he's coding, an agent is planning. If an agent is coding, he's reviewing. He occasionally runs two agents in competition on harder tasks (Claude vs Codex) but caps at two because cleanup overhead becomes counterproductive.

### Effort-for-Effort Review Philosophy

The level of code review he applies matches the effort the contributor (human or AI) invested. For AI-generated PRs with no associated issue and no human investment, he closes without reading. For his own AI-assisted code on Ghostty, he reviews everything. This principle also drives his open source policy: if someone spent minutes generating a PR, he won't spend hours fixing it.

### Open Source Trust Crisis from AI

AI has made it trivial to create plausible-looking but incorrect contributions. Ghostty receives 2-3 low-quality AI-generated PRs daily, identifiable by Claude's telltale pattern of opening a draft PR with no body, editing the body, then reopening. Hashimoto is implementing an invite-only vouching system (inspired by Lobsters) where existing community members stake their reputation to vouch for new contributors. Bad actors result in the voucher and their entire invite tree being banned.

### HashiCorp Origin and Cloud Infrastructure History

The first half of the interview provides rare firsthand perspective on the early cloud era — AWS's arrogance, Microsoft Azure's business competence despite technical complexity, Google Cloud's engineering brilliance paired with total business indifference. Terraform was seventh to market in infrastructure-as-code, not first, contradicting a common industry narrative.

## Practical Takeaways

- **Keep an agent running in the background at all times**: While you code, have an agent plan. While an agent codes, review or research. Maximize parallel throughput between human and AI.
- **Match review intensity to stakes**: Review AI code rigorously for production systems. For throwaway projects (wedding sites, prototypes), ship if it renders correctly — don't waste time reading code that will be deleted in weeks.
- **Run competing agents on hard tasks**: For tasks with uncertain approaches, launch Claude and Codex on the same problem and compare outputs.
- **Open source maintainers should implement trust gates**: The vouching/invite system provides a scalable defense against AI spam without banning AI usage entirely. The key insight is that the contribution method doesn't matter — what matters is whether a trusted human stands behind it.

## Notable Quotes

> "I endeavor to always have an agent doing something at all times. If I'm coding, I want an agent planning. If they're coding, I want to be reviewing." — Mitchell Hashimoto

> "It's ever for effort. If you put in hours, I'm going to put in hours back and I'm going to help you. But if you put in a few minutes and never read anything and throw it over the wall, then I should be able to read it in a few minutes, say no thank you, and close it." — Mitchell Hashimoto

> "Open source has always been a system of trust. Now it's just default deny and you must get trust." — Mitchell Hashimoto

> "AI gave a huge boost to terminals which is a funny thing. The amount of time spent in a terminal has gone up. If you told me in 2023 terminal usage would go up I would say no." — Mitchell Hashimoto

## Related Sources

- [164: Matt Pocock — Your Codebase is NOT Ready for AI](164-matt-pocock-codebase-ai-ready.md) — Both address how codebase design affects AI coding effectiveness

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — Industry perspective on AI's impact from a major infrastructure builder
- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Practical Claude Code workflow from an expert practitioner
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Always-on agent and competitive agent patterns
