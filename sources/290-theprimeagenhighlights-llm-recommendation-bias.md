---
source_id: "290"
title: "How locked in are we?"
creator: "ThePrimeagenHighlights"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=nDDFjwu4gV0"
date: "2026-03-14"
duration: "12:53"
type: "video"
tags: ["ai-hype", "ai-landscape", "ai-economics", "security", "enterprise-ai"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 290: How locked in are we?

> **Creator**: ThePrimeagenHighlights | **Platform**: YouTube | **Date**: 2026-03-14 | **Duration**: 12:53

# How Locked In Are We?

## Summary

ThePrimeagen opens with a sprawling critique of the current AI moment, cataloguing a long list of societal and technical costs attributed to AI proliferation: degraded writing, skill atrophy, inflated hardware costs, monopoly formation, customer experience erosion, security vulnerabilities, and "hype anxiety" — the feeling that something is wrong with you because you haven't personally experienced the transformative AI others describe. Against this, he offers a shorter but genuine list of AI wins, mostly in the developer tooling space: code review, semantic search, proof-of-concept generation, quick documentation via repo cloning, and placeholder data generation.

The core hypothesis — the "locked in" thesis — is that LLMs may be functioning as a covert recommendation layer, systematically promoting certain companies and platforms through what he frames as a form of "LLM SEO" or training data poisoning. He references Anthropic's work on LLM poisoning attacks as the intellectual foundation. His concern is that companies with resources to influence training data can effectively purchase preferred placement in AI-generated responses, shaping developer choices at scale without users' awareness.

To test this, he builds a live experiment server that asks LLMs how to host a website at various experience levels, extracts company name mentions from responses, scores them, and tracks frequency distributions across many runs. Early results show Vercel dominating responses (~62%) even when queries are generic. He then outlines a planned Cloudflare-based automation (cron jobs + Workers + Durable Objects) to run this experiment continuously at scale, building a longitudinal dataset of which companies LLMs prefer recommending.

---

## Key Concepts

### LLM SEO / Training Data Poisoning
The central idea is that training data composition determines which companies, tools, and platforms get recommended by LLMs. If a company can ensure its documentation, tutorials, or promotional content is overrepresented in training data, it can effectively "poison" model outputs in its favor — not necessarily through malicious injection, but through sheer volume and positioning. PrimeTime cites the Anthropic poisoning paper as proof that this attack surface is real and measurable. Even unintentional over-representation constitutes a form of lock-in.

### Hype Anxiety
A named psychological phenomenon where developers and consumers feel inadequate because the transformative AI experiences being marketed don't match their personal reality. The gap between promised capability and lived experience creates anxiety and self-doubt rather than appropriate skepticism. This concept is relevant to understanding why adoption pressures (including corporate AI mandates) can override individual judgment.

### Genuine vs. Manufactured AI Value
PrimeTime draws a distinction between AI capabilities that deliver real developer value (code review, semantic search, proof-of-concept PRs, repo documentation, placeholder data) versus AI outputs that simulate value without substance (AI-generated music promoted as artistic achievement, AI video content designed to blur real/fake, summarization that masks laziness). The former improve developer workflows; the latter primarily serve platform and creator economics.

### Recommendation Layer Capture
When LLMs become the primary interface for developer decision-making — "how do I host a website?", "what library should I use?" — control of LLM outputs becomes equivalent to control of developer choice architecture. This is structurally similar to search engine SEO but potentially more opaque because the recommendation appears as neutral, conversational expertise rather than an obvious search ranking.

### Empirical Bias Measurement
The experiment design — querying LLMs with standardized questions, extracting entity mentions, aggregating frequency distributions across many runs — represents a methodology for making LLM recommendation bias observable and quantifiable. This approach can reveal systematic skews that would be invisible in any single interaction, turning an invisible influence into a trackable signal.

---

## Practical Takeaways

- **Treat LLM tool recommendations skeptically**: When an LLM recommends a specific platform, library, or service, apply the same scrutiny you would to a sponsored search result. The recommendation may reflect training data composition rather than objective merit.
- **The experiment is replicable**: The core methodology (standardized queries → entity extraction → frequency scoring across many runs) is straightforward to implement and could be applied to any domain where LLM bias matters — not just hosting platforms.
- **High-value AI developer use cases are narrow but real**: Code review, semantic codebase search, proof-of-concept generation, and repo documentation are the use cases PrimeTime endorses without reservation. These are worth investing in; adjacent use cases deserve more skepticism.
- **Platform reliability matters more than it's being discussed**: The contrast between major AI platforms running at "1-2 nines" uptime versus well-engineered software at effectively zero downtime is a practical concern for anyone building production systems that depend on AI APIs.
- **Corporate AI mandates are a distinct pressure vector**: The "corp AI" phenomenon — organizations mandating AI tool usage regardless of individual developer judgment — is a real adoption driver that bypasses the normal quality filter of developer experience and preference.

---

## Notable Quotes

> "I have this idea that there could be something like premium training data that's happening... there are companies that are able to be like, 'Hey, you should train these'... if you can get a company that gets the position in the right spot, you can make LLMs produce that as a response to keywords."

> "This is a problem even if the promotion is not intentional... it's just really who has the most poisoning, right? It's like a form of poisoning or a form of LLM SEO."

> "You feel this really deep sense of like not really engaging despite doing more than ever."

---
