---
source_id: "290"
title: "How locked in are we?"
creator: "ThePrimeagenHighlights"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=nDDFjwu4gV0"
date: "2026-03-14"
duration: "12:53"
type: "video"
tags: ["ai-hype", "ai-landscape", "security", "ai-economics"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 290: How locked in are we?

> **Creator**: ThePrimeagenHighlights | **Platform**: YouTube | **Date**: 2026-03-14 | **Duration**: 12:53

# How Locked In Are We?

## Summary

ThePrimeagen opens with a sweeping critique of AI's societal footprint — cataloguing a long list of negative externalities including degraded writing, social media manipulation, open source disruption, poor platform reliability, rising hardware costs, skill atrophy, misinformation, and monopolistic consolidation. The framing is intentionally provocative, balanced against a shorter list of genuine wins: code review, semantic search, proof-of-concept generation, documentation exploration, and niche automation tasks. The net-negative accounting serves as setup for the central hypothesis.

The core project introduced is "Locked In" — an experiment to detect whether LLMs are systematically promoting specific companies in their responses. The demo involves a local server that routes questions (e.g., "how do I host a website?") through an LLM, parses the company names mentioned in responses, and scores their relative frequency. In early runs, Vercel consistently surfaces as the dominant recommendation, prompting questions about whether this reflects genuine best-practice consensus or something closer to training-data-level SEO — an idea grounded in Anthropic's own research on LLM poisoning via injected training data.

The stream then pivots to building out the measurement infrastructure: Cloudflare cron jobs firing every 30 minutes, Workers, Durable Objects, and container orchestration to run parallel queries at scale. The technical build is secondary to the conceptual point — that developers and end users have no reliable way to know whether AI recommendations are neutral, biased by training data composition, or the result of intentional "premium" data deals. This is framed as an underappreciated form of lock-in distinct from API or platform lock-in.

## Key Concepts

### LLM Recommendation Bias / "LLM SEO"
The hypothesis that companies mentioned most frequently in training data — whether through organic web presence or deliberate poisoning — will be disproportionately recommended by LLMs in response to neutral queries. This mirrors traditional SEO but operates at the training layer rather than the retrieval layer. The Anthropic poisoning paper is cited as foundational: if carefully crafted content is inserted at training time, it can durably shift model output toward preferred recommendations, even without explicit prompting.

### Hype Anxiety
A coined term for the psychological state where users are told transformative AI is happening all around them but haven't personally experienced meaningful gains — leading to a feeling that something is wrong with *them* rather than with the hype cycle. This is distinct from skepticism; it's the internalization of marketing as personal inadequacy.

### Skill Atrophy and Personal Stagnation
The observation that heavy reliance on AI for problem-solving can suppress the discomfort-driven learning loop that produces genuine skill development. The concern is not that AI assistance is bad, but that offloading cognitive friction entirely means individuals stop growing — they feel busy and productive while actually plateauing.

### Reliability as a Quality Signal
The video draws a sharp contrast between the "1–2 nines" uptime of major AI platforms and a counterexample (Turso) running at effectively 100% with no downtime. This is used to argue that the AI industry has normalized infrastructure quality that would be unacceptable in traditional SaaS — and that users have been conditioned to accept it.

### Legitimate AI Wins (Developer-Scoped)
The honest accounting of where AI actually delivers: code review, semantic search within codebases, proof-of-concept PRs to explore unfamiliar libraries, quick documentation generation from cloned repos, placeholder data, and weird niche automation (e.g., porting library types to Lua). The list is notably narrower and more precise than industry marketing suggests, and is almost entirely scoped to developer workflows.

## Practical Takeaways

- **Treat LLM tool/platform recommendations as potentially biased signals**, not neutral best-practice advice. When an LLM repeatedly recommends the same vendor (e.g., Vercel for hosting), consider whether that reflects genuine consensus or training-data composition effects — and cross-check against independent sources.
- **Use AI for proof-of-concept generation and code exploration, not as a replacement for understanding.** Getting a working PR from an unfamiliar library is high-value; letting AI write production code you don't understand is how skill atrophy compounds.
- **Uptime and reliability matter — don't normalize AI platform instability.** If your production workflows depend on external AI APIs running at 1–2 nines, build fallback paths or evaluate self-hosted alternatives.
- **The "locked in" problem is layered**: there's API lock-in, ecosystem lock-in, and now potentially training-data-level lock-in where the model itself steers you toward specific vendors. Awareness of all three layers is necessary for informed architectural decisions.
- **Measuring LLM behavior empirically is tractable.** The demo shows that a relatively simple server + scoring loop can surface statistically meaningful vendor-recommendation patterns across model outputs — a useful pattern for teams wanting to audit AI tooling advice before adopting it.

## Notable Quotes

> "I have this idea that there could be something like premium training data that's happening — companies that are able to say 'you should train these' — because remember where this really all comes from is Anthropic's poison LLM article. If you can get a company that gets the position in the right spot, you can make LLMs produce that as a response to keywords."

> "This is a problem even if the promotion is not intentional — it's just really who has the most poisoning. It's like a form of poisoning or a form of LLM SEO."

> "You'll notice that you feel this really deep sense of like not really engaging despite doing more than ever. Skill atrophy."
