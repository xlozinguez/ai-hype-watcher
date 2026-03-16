---
source_id: "290"
title: "How locked in are we?"
creator: "ThePrimeagenHighlights"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=nDDFjwu4gV0"
date: "2026-03-14"
duration: "12:53"
type: "video"
tags: ["ai-hype", "ai-landscape", "security", "ai-economics", "vibe-coding"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 290: How locked in are we?

> **Creator**: ThePrimeagenHighlights | **Platform**: YouTube | **Date**: 2026-03-14 | **Duration**: 12:53

# How Locked In Are We?

## Summary

ThePrimeagen opens with a broad critique of AI's societal costs — ruined social media writing, degraded customer experience, skill atrophy, monopoly formation, security risks, and inflated hardware costs — before pivoting to his central hypothesis: that LLMs may be systematically promoting certain commercial platforms (e.g., Vercel, Netlify) through what he calls "LLM SEO" or training data poisoning. The concern is grounded in Anthropic's own research on LLM poisoning: if a company can get favorable representation in training data, the model will recommend that company disproportionately in response to relevant queries — regardless of whether the promotion is intentional.

To test this hypothesis, Primeagen builds a live instrumented server that fires questions at varying experience levels (e.g., "how to host a website at a junior level") through an LLM routing layer, then tallies which companies are recommended and with what frequency. Early results show Vercel receiving ~62% of recommendations, Netlify ~25%, and GitHub Pages ~12.5%. He notes the scoring needs refinement to weight the *depth* of endorsement (e.g., a full walkthrough vs. a brief mention), and references Claude Code's day-over-day benchmark tracker as an analogous attempt to instrument and reason about opaque model behavior.

The broader project goal — "Locked In" — is to build a Cloudflare-native pipeline (cron jobs, Workers, Durable Objects) that continuously polls LLMs with varied questions, tracks company mentions over time, and surfaces statistical patterns in commercial bias. This is framed as essential infrastructure for reasoning about whether AI recommendations are trustworthy or subtly captured by training-time incentives.

## Key Concepts

### LLM SEO / Training Data Poisoning
The hypothesis that companies can gain disproportionate LLM recommendation share by ensuring their products appear favorably and frequently in training data — analogous to traditional SEO but operating at the model-weight level. Primeagen traces this to Anthropic's published research on LLM poisoning, which demonstrated that targeted data injection can steer model outputs toward specific keywords or entities. The implication is that "best tool for the job" recommendations from LLMs may reflect training corpus composition rather than objective merit.

### Instrumented Recommendation Auditing
The practical method being built: a server that submits structured prompts (varying question type, user experience level) to LLMs through a routing layer, parses responses to extract mentioned company/product names, and accumulates weighted frequency scores. This creates a longitudinal dataset for detecting recommendation drift or commercial bias — a form of model observability applied to output content rather than latency or accuracy.

### Hype Anxiety
Primeagen coins this term for the psychological phenomenon where users are told AI is transformative but don't personally experience the promised gains, leading to a sense that something is wrong with *them* rather than the technology. This is distinct from skepticism — it's the internalized anxiety produced by the gap between marketing narrative and lived experience.

### Skill Atrophy and Personal Stagnation
A recurring concern: habitual AI delegation degrades practitioners' own capabilities over time. Primeagen frames this not just as a productivity tradeoff but as a qualitative shift in engagement — doing *more* while feeling less present or competent. This connects to a broader critique of "vibe coding" practices where AI does the thinking and the human rubber-stamps output.

### Legitimate vs. Hollow AI Value
Despite the critical framing, Primeagen explicitly enumerates genuine high-value AI use cases: code review, semantic search within codebases, proof-of-concept PR generation, quick documentation from source repos, placeholder data generation, image upscaling, and weird one-off automation tasks (e.g., porting types across languages). The implicit framework is that narrow, well-scoped tasks with verifiable outputs are where AI earns its keep.

## Practical Takeaways

- **Treat LLM tool recommendations with skepticism**: When an LLM suggests a specific platform, hosting provider, or library, the recommendation may reflect training data exposure rather than objective fitness — especially for commoditized choices like hosting or CI/CD.
- **Instrument your LLM outputs**: The "Locked In" server pattern — sending calibrated prompts, parsing responses for entity mentions, and tracking frequencies — is a replicable audit methodology any team can adapt to evaluate whether their AI toolchain has implicit commercial biases.
- **Weight endorsement depth, not just mention frequency**: A response that walks through Vercel's full deployment flow is a stronger signal than a passing mention. Scoring systems for recommendation auditing should account for depth and prominence, not just co-occurrence counts.
- **Use AI for proof-of-concept generation, not final answers**: Getting a skeleton PR to understand how an unfamiliar library works is a high-signal use case. Using AI to *complete* work you haven't reasoned through yourself is where skill atrophy risk is highest.
- **Cloudflare's cron + Workers + Durable Objects stack** is highlighted as a capable and learnable platform for building lightweight, persistent automation pipelines — relevant for anyone building continuous LLM monitoring or scheduled agentic workflows.

## Notable Quotes

> "This is a problem even if the promotion is not intentional — it's just really who has the most poisoning. It's a form of LLM SEO."

> "You have been told all these amazing things are happening, but you yourself haven't experienced it, and so therefore you actually feel like something's wrong with you. I'm going to call it hype anxiety."

> "I didn't say good code. I just said make code."

---
