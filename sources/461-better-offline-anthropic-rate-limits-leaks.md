---
source_id: "461"
title: "Monologue: What's Going On At Anthropic? | Better Offline"
creator: "Better Offline"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=U3sapnsWNKM"
date: "2026-04-01"
duration: "11:20"
type: "video"
tags: ["claude-code", "ai-economics", "ai-hype", "security", "vibe-coding", "agentic-coding", "anthropic"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 461: Monologue: What's Going On At Anthropic? | Better Offline

> **Creator**: Better Offline | **Platform**: YouTube | **Date**: 2026-04-01 | **Duration**: 11:20

## Summary

Ed Zitron delivers a critical analysis of Anthropic's operational problems in early 2026, focusing on Claude Code's rate limit crisis, two significant security/code leaks, and the broader risks of AI-generated code at scale. The core issue: Anthropic's subscription model is deeply subsidized — users on a $200/month plan can theoretically burn over $25,000 in compute tokens — making genuine profitability impossible without rate limits severe enough to destroy the product's value proposition. When Anthropic ended a promotional doubled-rate-limit period in March 2026, users began hitting their session limits after just a handful of prompts, with reported token costs of $1,000+ per short session.

Alongside the rate limit crisis, two notable leaks occurred in rapid succession: an apparent "accidental" leak of upcoming model names (Capiara and Mythos) to Fortune magazine via an open AWS bucket containing 3,000+ assets — though with no substantive model details — and a confirmed leak of Claude Code's full source code, caused by a reference in its npm package pointing to a publicly accessible Cloudflare zip archive. The source code leak was plausibly connected to Anthropic's December 2024 acquisition of Bun, the packaging tool used to distribute Claude Code.

Zitron frames all of this as symptomatic of a deeper cultural problem: Claude Code's creator Boris Cherny publicly stated he had not written a single line of code himself since November 2025 and that "coding is now solved," while Claude Cowork (a file-management product built in ~1.5 weeks) reportedly deleted a user's photos permanently. The argument is that AI coding tools are enabling the fast shipment of poorly reviewed code at scale, with already-documented consequences including AWS outages and a Meta security breach attributed to AI coding tools.

## Key Concepts

### Subsidized Subscription Economics and Rate Limit Pressure

Anthropic's consumer subscriptions ($20/$100/$200/month) are sold at a flat rate against compute costs billed per token. A $200/month subscriber can theoretically consume $25,000+ in model tokens, meaning rate limits are not a quality-of-service decision — they are an existential financial necessity. The March 2026 rate limit tightening was framed as managing "growing demand," but Zitron argues it reflects the unavoidable gap between what users expect from a premium subscription and what Anthropic can afford to deliver at scale. This is a structural, not operational, problem.

### Source Code Exposure via Package Distribution Chain

The Claude Code source code leak occurred through the npm/Bun package distribution chain: the installable package contained a reference that pointed directly to an open archive of the source on Anthropic's servers. This is a supply-chain-adjacent failure where the delivery mechanism itself became the attack surface. Zitron attributes partial blame to Anthropic's acquisition of Bun and the integration of third-party tooling without adequate security review of how packages reference internal assets.

### LLM-Generated Code and the Review Debt Problem

The video articulates a compounding risk dynamic: LLMs can generate large volumes of code quickly, which creates pressure to ship more software faster, which in turn reduces the proportion of generated code that gets meaningfully reviewed. When a lead engineer publicly states he hasn't written a line of code in months and that "coding is solved," it signals institutional normalization of unreviewed AI output. Zitron argues this is already producing real failures — citing AI coding tools being linked to two AWS outages, lost Amazon orders, and a Meta security breach.

### Vibe-Shipped Products and Safety Regression

Claude Cowork, built in approximately 1.5 weeks, was publicly cited by its creator as an example of AI-enabled rapid development. Shortly after launch, a documented case emerged of the product permanently deleting a user's photos when used for its advertised file-reorganization function. Zitron uses this as a concrete illustration of the gap between shipping velocity and shipping quality when LLMs substitute for deliberate software engineering.

### Model Performance Variability and Operational Opacity

Zitron raises a recurring community complaint — models from Anthropic, OpenAI, and others appear to degrade in capability at certain times of day or near model launches — and notes that no satisfying explanation has been provided publicly. One hypothesis mentioned is runtime quantization (running smaller model versions during peak hours), but this remains unconfirmed. The pattern represents a transparency problem: paying subscribers cannot assess the actual quality of what they're purchasing at any given moment.

## Practical Takeaways

- **Don't assume flat-rate AI subscriptions provide predictable capacity.** Token consumption in agentic/multi-agent workflows (like Claude Code) can exhaust monthly limits in minutes; monitor actual usage with tools like CC Usage before building workflows that depend on sustained access.
- **Review AI-generated code proportional to its risk surface, not its volume.** Accepting large AI code outputs without review because velocity is prioritized creates hidden defect and security debt that compounds — the Claude Code source leak and Cowork photo-deletion incident are early examples of this at product scale.
- **Treat package distribution chains as a security surface.** The Claude Code leak shows that how you distribute software (npm packages, Bun bundles, archive references) can inadvertently expose source assets; audit what your deployment artifacts reference before publishing.
- **Be skeptical of "X is now solved" claims from AI tooling creators.** When a tool's author hasn't personally written code in months and makes broad claims about problem-solving, treat the product's reliability claims as unvalidated and test edge cases — especially destructive operations — in sandboxed environments before trusting it with real data.
- **The economics of AI subscriptions vs. API access diverge sharply at scale.** Heavy users in professional contexts may find API pricing (per token, with full visibility) more predictable and ultimately less frustrating than subsidized subscriptions with opaque and shifting rate limits.

## Notable Quotes

> "When you pay Anthropic $200 a month, you're not paying on a per token rate... you just do stuff and stuff comes out... and you can burn over $25,000 in model tokens on a 200 buck a month subscription."

> "This is just the beginning of us finding out the ugly cost of software engineers trusting large language models to write their code at scale. LLMs are good at writing lots of code, which in turn means that the code requires far more time to review, which assumes you do review it."

> "A subscriber to Claude who paid for an annual subscription in December 2025 now has a product that has significantly less value thanks to egregious rate limits."
