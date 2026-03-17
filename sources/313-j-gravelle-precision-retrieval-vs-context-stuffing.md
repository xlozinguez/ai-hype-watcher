---
source_id: "313"
title: "Claude’s $5, Million Token Prompts vs a tiny 5¢ Prompt!"
creator: "J. Gravelle"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=1VfnlQP2Uro"
date: "2026-03-16"
duration: "10:15"
type: "video"
tags: ["context-engineering", "ai-economics", "prompt-engineering", "ai-hype"]
curriculum_modules: ["03-claude-code-essentials", "06-strategy-and-economics"]
---

# 313: Claude’s $5, Million Token Prompts vs a tiny 5¢ Prompt!

> **Creator**: J. Gravelle | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 10:15

# Claude's $5 Million Token Prompts vs a Tiny 5¢ Prompt

## Summary

J. Gravelle pushes back on Anthropic's marketing around million-token context windows, pointing out that 79% retrieval accuracy at 1M tokens means roughly one-in-five queries fail — at a cost of $5 per question. His core argument: a large context window is not a retrieval strategy. Cramming entire codebases into a prompt is brute force, not engineering, and the benchmark Anthropic is bragging about actually reveals degrading performance at scale, not a triumph.

The video demonstrates this using "J Munch Workbench," a tool Gravelle built around precision retrieval (via Jcode Munch and JDoc Munch). Rather than dumping an entire repo into context, the tool indexes the codebase and retrieves only the specific symbols, functions, or doc passages actually needed to answer a question. A live demo on a single query shows 575,000+ tokens excluded from context — roughly $2.88 saved on one question — while producing a cleaner, more focused answer.

The broader principle is **context control over context stuffing**: instead of feeding the model a haystack and hoping it finds the needle, you give it only what it needs. The result is simultaneously cheaper, faster, and more accurate. Gravelle acknowledges large context windows have legitimate uses but argues using them as the *default* coding retrieval strategy is "expensive, sloppy, and usually unnecessary."

---

## Key Concepts

### Context Stuffing vs. Precision Retrieval
The dominant pattern of dumping entire repos or large file sets into a context window is characterized as a brute-force fallback, not a strategy. Precision retrieval — identifying and fetching only the specific symbol, function, class, or passage the model actually needs — produces better results at a fraction of the cost. The analogy: don't hand someone a homeowner's manual when they ask where the bathroom is.

### The Real Cost of Large Context Benchmarks
At ~$5/million input tokens, a 79% accuracy rate at 1M tokens means spending $5 per query with a ~21% failure rate. Gravelle reframes this not as a capability milestone but as a casino-like expected value problem. The benchmark demonstrates the *ceiling* of brute-force retrieval, not a reason to adopt it.

### RAG as a Partial Fix (Still a Haystack)
RAG is acknowledged as an improvement over raw file dumps, but most RAG implementations are described as "sending a smaller haystack" — still filling context with chunks the model doesn't need, still paying for noise. True precision retrieval goes further, targeting specific indexed symbols rather than approximate semantic chunks.

### Context Control
The positive framing of Gravelle's approach: rather than managing *how much* to stuff into a window, control *what* goes in. Indexed retrieval tied to repo structure (files, functions, classes, methods, doc passages) lets the model work with exactly the relevant material. This is presented as the engineering discipline that large context windows let developers skip — at a cost.

### Benchmarkable Token Savings
The workbench demo makes token savings concrete and verifiable rather than theoretical. Running a baseline query (full repo dump) vs. a munched query on the same question and model isolates the retrieval strategy as the variable. The 575K token delta on a single query illustrates that at scale (many queries per day), retrieval strategy is a significant cost driver.

---

## Practical Takeaways

- **Don't use context window size as a proxy for retrieval quality.** A model that *can* ingest 1M tokens doesn't mean that's the right approach for your codebase question.
- **Index your repo and retrieve by symbol, not by file.** Targeting the specific function or class needed rather than including whole files dramatically reduces token spend without sacrificing answer quality.
- **Measure your own token usage per query.** Tools like J Munch Workbench make it easy to compare baseline vs. precision retrieval on your actual codebase — don't assume the large-context path is "good enough."
- **RAG is a step in the right direction but isn't sufficient.** If your RAG pipeline is still returning large chunks of loosely relevant text, you're still padding context — just less so.
- **Accuracy and cost tend to improve together with precision retrieval.** When the model isn't rummaging through irrelevant code, answers are cleaner and more focused — this isn't a cost/quality tradeoff, it's a joint improvement.

---

## Notable Quotes

> "You can spend $5 to ask a question and still have about a one in five chance the model doesn't actually make proper use of the amount of crap you just shoved in its throat. That's not a triumph. That's a casino."

> "A million token window is not some magical get-out-of-engineering-free card."

> "I'd rather spend five cents and be a lot more right."

---
