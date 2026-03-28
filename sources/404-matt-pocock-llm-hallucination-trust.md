---
source_id: "404"
title: "Never Trust An LLM"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=9VNG0h4pLh0"
date: "2026-03-27"
duration: "14:00"
type: "video"
tags: ["prompt-engineering", "validation", "context-engineering", "security", "ai-hype"]
curriculum_modules: ["02-prompting-and-workflows", "01-foundations"]
---

# 404: Never Trust An LLM

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-27 | **Duration**: 14:00

# Never Trust An LLM

## Summary

Matt Pocock makes a practical, developer-focused case for why treating LLM outputs as inherently untrustworthy is the correct default stance — not out of pessimism, but as a prerequisite for using these tools effectively. Drawing on a comprehensive academic taxonomy of hallucination types and an OpenAI paper on why hallucinations occur, he argues that the combination of lossy training compression and benchmark incentives that reward confident guessing over humble uncertainty-acknowledgment makes hallucinations a structural feature of LLMs, not a bug that will simply be patched away.

The video categorizes hallucinations along two axes: **intrinsic** (contradicting or ignoring information the user explicitly provided in context) and **extrinsic** (confabulating from the model's training data when no grounding context is given). Extrinsic hallucinations are the more dangerous and common failure mode — fabricated packages, invented laws, nonexistent government departments — while intrinsic hallucinations are rarer but deeply alarming when they occur, as in the Air Canada chatbot case where a bereavement policy explicitly in context was contradicted anyway.

Despite the critique, Pocock remains pro-LLM. His core insight is that reliability is strongly correlated with how much grounding information you supply: models working with rich intrinsic context (a codebase, a document, web search results) perform dramatically better than models operating purely from training memory. His practical framework centers on engineering situations where the LLM has what it needs — and treating anything without that grounding as suspect.

## Key Concepts

### Intrinsic vs. Extrinsic Hallucinations
The academic taxonomy distinguishes between hallucinations that contradict information *you provided* in the conversation (intrinsic) versus hallucinations that confabulate facts from the model's training data (extrinsic). Extrinsic hallucinations are far more common and harder to catch because you often don't have the ground truth to check against. Intrinsic hallucinations are rarer but arguably more alarming — they mean the model ignored something you explicitly told it.

### Training as Lossy Compression
LLM training is fundamentally a compression process: a massive corpus of data is squished into a parameter set small enough to fit on a GPU. Like aggressively JPEG-compressing a photo, the low-level details get smeared away while broad structure survives. When you query a model about something at the edge of its training distribution, you're working from a blurry, degraded representation — and the model often doesn't know how degraded it is.

### Benchmark Incentives Reward Guessing
Per the OpenAI paper Pocock cites, LLMs hallucinate partly because training and evaluation procedures reward confident answers over uncertainty admissions. Benchmark scores depend on getting answers right, and "I don't know" never scores points. This creates a structural bias toward confident guessing — you can't score on shots you don't take. There's also a fundamental tension: the confidence that enables deep reasoning is the same confidence that produces hallucination.

### Contextual Inconsistency as a Distinct Failure Mode
Even when you've correctly supplied grounding context, models can still ignore or contradict it — a failure mode the taxonomy calls contextual inconsistency. The Air Canada case is illustrative: a bereavement policy was presumably in the chatbot's context window, yet the model fabricated different terms. This means intrinsic information reduces but does not eliminate hallucination risk, which matters especially for high-stakes deployments.

### "Use Your Search Tool" as a Forcing Function
Pocock's practical mitigation for extrinsic hallucinations is prompting the LLM explicitly to use its web search tool. This converts an extrinsic query into an intrinsic one: the model fetches current documents, pulls them into context, and reasons from them with citations. The key insight is that overconfident models will skip search if they think they already know the answer — explicit prompting overrides that tendency.

## Practical Takeaways

- **Default to distrust for extrinsic queries.** If you haven't given the model the relevant information, treat any factual claim — especially package names, legal details, government programs, APIs — as a hypothesis to verify, not a fact to act on.
- **Supply context aggressively.** When working with LLMs on code, pass the actual files. For research, attach the documents. The more grounding you provide, the closer to reliable the output becomes. Never rely on training memory when you can avoid it.
- **Explicitly prompt for search.** Say "use your search tool" when asking questions you don't already have answers to. Don't assume the model will decide it needs to look something up — it may be too confident to bother.
- **Apply extra skepticism to fabricated entities.** Package hallucinations are an active security vector: attackers create malicious packages with the names LLMs tend to fabricate. Never install a package an LLM recommends without independently verifying it exists via the actual package registry.
- **Treat high-stakes domains as requiring human verification regardless.** For health, legal, or financial decisions, even well-grounded LLM outputs need independent verification. Contextual inconsistency means you cannot fully trust even intrinsic answers for consequential calls.

## Notable Quotes

> "LLMs hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty."
> — OpenAI paper, cited by Pocock

> "If you're relying on their extrinsic knowledge from their training set, then you're going to be disappointed."

> "Use your search tool. Most chatbots and most agent harnesses have some kind of tool that the LLM can use in order to search the web... because then it will pull the articles into its context and it will answer based on those articles and you'll be less likely to get hallucinations because you're relying on intrinsic information."
