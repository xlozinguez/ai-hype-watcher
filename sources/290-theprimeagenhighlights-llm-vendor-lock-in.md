---
source_id: "290"
title: "How locked in are we?"
creator: "ThePrimeagenHighlights"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=nDDFjwu4gV0"
date: "2026-03-14"
duration: "12:53"
type: "video"
tags: ["ai-hype", "ai-landscape", "ai-economics", "security", "infrastructure"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 290: How locked in are we?

> **Creator**: ThePrimeagenHighlights | **Platform**: YouTube | **Date**: 2026-03-14 | **Duration**: 12:53

# How Locked In Are We?

## Summary

ThePrimeagen opens with a wide-ranging critique of AI's cultural and economic downsides — degraded writing, ruined social media, skill atrophy, hype anxiety, rising infrastructure costs, and AI-enforced corporate mandates — before pivoting to a more focused technical hypothesis: that LLMs may be systematically promoting certain companies and platforms through what he calls "LLM SEO" or "premium training data" poisoning. The core concern is grounded in a referenced Anthropic paper on LLM poisoning, which demonstrated that targeted training data can bias model outputs toward specific keywords or recommendations. This isn't necessarily intentional, but the effect is real regardless of intent.

To investigate, he builds a live experiment: a local server that sends identical natural-language questions (e.g., "how to host a website at a junior level") to LLMs via an OpenRouter routing layer, then parses and scores which companies are mentioned and how prominently. Early results show Vercel appearing at ~62% of recommendations, Netlify at ~25%, and GitHub Pages at ~12%. He frames this as a serious measurement problem — developers are being steered toward products without knowing it, and there's currently no reliable instrument to detect or quantify that steering.

The second half of the video is a live coding session building the infrastructure to run this experiment at scale: a Cloudflare Workers + Durable Objects + Cron Jobs pipeline that would spawn 5–10 containers every 30 minutes, fire batches of queries, track running state, and aggregate recommendation frequencies over time. The project is framed explicitly as a research tool — a "locked in" detector — rather than a finished product.

## Key Concepts

### LLM SEO / Training Data Poisoning as Commercial Risk
The central hypothesis is that companies could (intentionally or not) achieve outsized representation in LLM training data, causing models to disproportionately recommend their products. Primeagen references an Anthropic paper on LLM poisoning as the theoretical foundation. Even without deliberate manipulation, whichever platforms dominate developer documentation, blog posts, and tutorials will naturally dominate model outputs — creating a self-reinforcing lock-in effect invisible to the end user.

### "Locked In" — Measuring Invisible Vendor Bias
The experiment operationalizes the concept of lock-in as a measurable signal: ask the same question many times across routing layers, parse which company names appear in responses, weight by prominence/emphasis rather than just presence, and compute a normalized distribution. Early data shows Vercel capturing ~62% of hosting recommendations — a non-trivial skew that developers following AI advice would reproduce in their architectural decisions without knowing they were being steered.

### Hype Anxiety and the Costs of AI Adoption
Primeagen coins "hype anxiety" — the psychological state of feeling left behind because you haven't personally experienced the promised benefits of AI. He pairs this with "skill atrophy" and "personal stagnation" as underappreciated costs: when you outsource cognition to AI, you stop growing. He also catalogs concrete economic costs (GPU prices, RAM, SSD, electricity, AI platform downtime at "1-2 nines" reliability) against the backdrop of genuine but narrow wins.

### Where AI Actually Delivers Value (Developer Perspective)
The honest accounting from a skeptic: code review (genuinely useful with right tooling), semantic search within codebases, proof-of-concept PRs for unfamiliar libraries, quick documentation via repo cloning + querying, placeholder data generation, porting/type-migration tasks, AI upscaling, and weird automation edge cases. Summarization is flagged as a double-edged sword — useful but promotes laziness over learning.

### Cloudflare Workers + Durable Objects as Research Infrastructure
The technical architecture for the experiment uses Cloudflare Cron Jobs triggering Workers, which spawn Durable Object workflows to manage stateful, long-running parallel request batches. The design choice reflects a learning goal (Primeagen explicitly says he's exploring Cloudflare's utility suite) but also a practical one: distributed, serverless cron-driven workloads are a natural fit for this kind of continuous measurement task.

## Practical Takeaways

- **Don't trust AI recommendations for tool/vendor selection uncritically.** The same mechanism that makes LLMs helpful (pattern matching on training data) makes them susceptible to systematic bias toward overrepresented platforms. Treat AI vendor suggestions the same way you'd treat a blog post with undisclosed sponsorships.
- **Reliability gap is real.** Major AI platforms are operating at 1–2 nines uptime. Before building production-critical workflows on AI infrastructure, benchmark your tolerance for downtime against what providers are actually delivering — not what they advertise.
- **AI's highest-value developer use cases are narrow but real:** code review with the right tooling, semantic codebase search, PoC generation for unfamiliar libraries, and documentation-by-example (clone repo → query it). These are defensible ROI; general "vibe coding" is much harder to justify.
- **Skill atrophy is a compounding cost.** The more cognitive work you offload to AI tools, the slower your own capability growth. This is especially acute for junior developers whose learning curve is being short-circuited before foundational intuitions form.
- **LLM routing layers obscure the model making recommendations.** When using OpenRouter or similar abstractions, you may not know which underlying model is answering — making it even harder to audit or reproduce recommendation patterns. Logging model identity alongside outputs is essential for any serious measurement work.

## Notable Quotes

> "This is a problem even if the promotion is not intentional. It's really just who has the most poisoning — it's like a form of poisoning or a form of LLM SEO."

> "You've been told all these amazing things are happening, but you yourself haven't experienced it, and so therefore you actually feel like something's wrong with you. I'm going to call it hype anxiety."

> "You now just constantly rely on the AIs to do everything for you, so you personally aren't actually growing as a person. You'll notice that you feel this really deep sense of not really engaging despite doing more than ever."
