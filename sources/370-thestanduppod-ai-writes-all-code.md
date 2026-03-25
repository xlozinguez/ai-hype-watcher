---
source_id: "370"
title: "AI Writing Essentially All The Code"
creator: "TheStandupPod"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=r5vMPfnDth8"
date: "2026-03-24"
duration: "15:25"
type: "video"
tags: ["ai-hype", "ai-landscape", "ai-sdlc", "enterprise-ai", "vibe-coding"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 370: AI Writing Essentially All The Code

> **Creator**: TheStandupPod | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 15:25

# AI Writing Essentially All The Code

## Summary

This episode of TheStandupPod responds to Anthropic CEO Dario Amodei's claim that AI will be writing 90% of code within 3-6 months and essentially all code within 12 months. The hosts — practicing software engineers — push back with grounded skepticism, interrogating what "writing all the code" actually means in practice and whether the framing holds up against real-world software development constraints.

The panel surfaces several underappreciated counterarguments: that AI currently generates additive, entropy-increasing code rather than simplifying systems; that massive regulated industries (banking, aerospace, healthcare, government) face legal and policy barriers to LLM adoption; and that legacy codebases with tribal knowledge represent an enormous portion of real-world engineering work that LLMs demonstrably cannot yet navigate. Casey offers a particularly useful distinction between AI generating glue-layer boilerplate code (plausible soon) vs. AI producing genuinely novel, expert-quality code (no evidence yet, requires breakthroughs).

The discussion also raises a sharp incentive-structure critique: if AI companies truly had code-generation capability sufficient to replace engineers, they would use it to capture markets themselves rather than selling it to developers. The fact that their own chat interfaces and developer tools remain beatable by small indie teams (e.g., Theo's T3 Chat outcompeting large-company products) is treated as indirect evidence that current AI capability is being overstated relative to the timeline claims.

## Key Concepts

### Entropy Reduction as the Real Capability Test
One host argues that the meaningful test for AI coding capability is not how much code it can generate, but whether it can *reduce* system complexity. Current LLMs tend to wrap problems in additional layers rather than simplifying them. Until AI can take a complex system and make it genuinely simpler — reducing entropy — human expertise remains essential and the "billions of lines of code" framing is misleading volume theater.

### Glue Code vs. Expert Code Distinction
Casey draws a sharp line between two categories of code: (1) glue-layer boilerplate that connects libraries and frameworks in mediocre but functional ways — which AI can already approximate — and (2) genuinely expert code that a skilled programmer would write, which would not have required the intermediate layers at all. Most "AI writes all the code" claims conflate these, but the economic value is concentrated in the second category where AI shows no demonstrated capability.

### Legacy Systems and Tribal Knowledge as an AI Moat
A significant portion of real-world engineering involves undocumented legacy systems where knowledge lives in people, not codebases. LLMs trained on public code have no path into this domain: they cannot recover the intent behind a misnamed function written by a departed engineer, or understand an internal library with no documentation. This represents a large fraction of enterprise engineering work that is structurally resistant to near-term AI replacement.

### Regulated Industry Exclusion
Banking, aerospace, medical, and government sectors — which collectively represent a dominant share of professional software development — face legal, compliance, and competitive-secrecy barriers that currently prohibit or severely restrict LLM use in production codebases. Timeline predictions that ignore these constraints are describing a much smaller slice of the actual software industry than implied.

### Incentive-Structure Critique of AI Capability Claims
If an AI company possessed software-generation capability sufficient to autonomously replace engineers, the rational move would be to use that capability to build and capture product markets, not sell access to developers. The fact that AI labs are selling developer tools rather than disrupting industries directly suggests their actual capability level is lower than the boldest public claims imply. The revenue model requires keeping developers employed and purchasing subscriptions.

## Practical Takeaways

- **Treat "AI writes X% of code" claims as ambiguous until the speaker defines code type** — glue-layer integration code and expert systems code are fundamentally different in value and difficulty, and most headline claims blend them together.
- **Entropy reduction is a useful personal benchmark**: before being impressed by AI-generated code, ask whether the output simplifies or complicates the system. If it only adds layers, its long-term value is limited regardless of how much it generates.
- **Legacy codebase expertise remains a durable human advantage** — the ability to navigate undocumented, tribal-knowledge-heavy systems is not a skill LLMs can replicate from public training data and may represent the most defensible engineering niche in the near term.
- **Industry and regulatory context should filter AI adoption timelines**: predictions that omit regulated sectors are describing a subset of software development, and organizations in those sectors should calibrate adoption expectations accordingly.
- **Watch what AI labs ship, not what they claim**: the quality of their own products (chat interfaces, developer tools) relative to small-team competitors is a real-time signal of actual capability versus marketing narrative.

## Notable Quotes

> "AI right now is not generating very usable code from the standpoint of actually doing a good job. But on the flip side, the average programmer in their job is also not generating that kind of code... the AI can easily generate that code."
> — Casey, distinguishing glue code from expert code

> "If it can never reduce entropy then my earlier prediction/joke will come true because it will have to continue generating billions of lines of code to continue to wrap all of the complicated stuff... I don't see human expertise being useless."
> — TJ, on entropy reduction as the real capability threshold

> "You will never find out that they have proper AGI from a press announcement. You will find out when they've remade your business in an afternoon... they are not going to give you that shovel. They're just going to use it for themselves."
> — Host, on the incentive structure of AI capability disclosure
