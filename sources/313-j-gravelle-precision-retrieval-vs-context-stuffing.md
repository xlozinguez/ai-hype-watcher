---
source_id: "313"
title: "A $5 Prompt that's 79% Accurate vs a $.05 Prompt that's 95% - You Make The Call!"
creator: "J. Gravelle"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=1VfnlQP2Uro"
date: "2026-03-16"
duration: "10:15"
type: "video"
tags: ["context-engineering", "ai-economics", "prompt-engineering", "ai-hype"]
curriculum_modules: ["03-claude-code-essentials", "06-strategy-and-economics", "02-prompting-and-workflows"]
---

# 313: A $5 Prompt that's 79% Accurate vs a $.05 Prompt that's 95% - You Make The Call!

> **Creator**: J. Gravelle | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 10:15

# A $5 Prompt that's 79% Accurate vs a $.05 Prompt that's 95% - You Make The Call!

## Summary

J. Gravelle challenges the prevailing industry excitement around large context windows, using Anthropic's own benchmark data as a foil. At 1 million input tokens, Claude achieves roughly 79% accuracy on long-context retrieval tasks — meaning a $5 query still fails roughly one in five times. Gravelle frames this not as a triumph but as a casino: expensive, probabilistic, and architecturally lazy. The argument is not that large context windows are worthless, but that using them as a *default* retrieval strategy for coding tasks is sloppy engineering dressed up as capability.

The video demos Gravelle's own tooling — J Munch Workbench, built on JCode Munch and JDoc Munch — which indexes a local repository and retrieves only the specific symbols, files, functions, or doc passages the model actually needs to answer a question. On a single test query ("where is OAuth implemented?"), the precision retrieval approach excluded 575,000+ tokens from the context, saving approximately $2.88 on one request while producing a cleaner, more focused answer. The comparison is direct: same repo, same question, same model, different retrieval strategy.

The underlying principle is *context control* versus *context stuffing*. RAG is acknowledged as an improvement over raw file dumps, but Gravelle argues most RAG implementations still send a "smaller haystack" rather than surgically targeting what the model needs. Precision retrieval treats the context window as a precision instrument, not a landfill — and the payoff is simultaneously cheaper, faster, and more accurate outputs.

---

## Key Concepts

### Context Stuffing vs. Context Control
Dumping entire repositories into a context window is characterized as brute-force retrieval — the AI equivalent of handing someone a homeowner's manual when they ask where the bathroom is. Context control means identifying the exact symbol, file, function, class, or doc passage needed before any tokens are sent to the model. This distinction is the core engineering argument of the video.

### The Cost-Accuracy Trap of Large Context Windows
Using Anthropic's own benchmark, the video illustrates that 1M token queries cost ~$5 and yield ~79% accuracy. This creates a concrete economic frame: high spend does not guarantee high accuracy, and the two failure modes (wasted cost, wrong answers) compound each other. The $5 vs. $0.05 framing makes the ROI argument visceral and testable.

### Precision Retrieval as an Engineering Discipline
Rather than RAG (which typically narrows the haystack without eliminating it), precision retrieval means asking: *which exact symbol do you need?* The JCode Munch / JDoc Munch approach pre-indexes the repo structure so queries target specific artifacts. This is framed as treating AI-assisted coding like a "grownup piece of software" — index-first, fetch-specific.

### RAG as a Partial Solution
RAG is acknowledged as better than raw file injection, but criticized for often being "a smaller haystack, still a haystack." The distinction Gravelle draws is between *reducing volume* (RAG's typical approach) and *targeting precision* (his preferred approach). Both reduce tokens, but only the latter systematically removes irrelevant content rather than merely compressing it.

### Benchmark Literacy
The video models a critical reading of vendor benchmarks: Anthropic's chart showing ~79% accuracy at 1M tokens is presented by Anthropic as impressive, but reframed here as an admission that 21% of expensive queries fail. This is a transferable skill — reading performance curves to find the cost/accuracy regime you're actually operating in, not just the headline number.

---

## Practical Takeaways

- **Don't use context window size as your retrieval strategy.** A large context window is infrastructure, not an engineering plan. Default to targeted retrieval; use large context only when the use case genuinely requires it.
- **Benchmark cost per correct answer, not just accuracy or cost alone.** A 95%-accurate $0.05 query dominates a 79%-accurate $5.00 query on every meaningful metric. Calculate expected cost per correct answer when evaluating retrieval approaches.
- **Index before you query.** Pre-indexing a repo's structure (files, functions, classes, symbols) enables surgical context selection. This is the architectural precondition for precision retrieval.
- **Compare retrieval strategies on your own repo.** Gravelle's workbench demo illustrates a replicable experiment: run the same question with baseline (full context) and precision retrieval, then compare answer quality and token savings. This is a methodology, not just a product pitch.
- **RAG is necessary but not sufficient.** If your RAG implementation is selecting document chunks by similarity without targeting the specific symbol or section needed, you're still over-indexing on volume. Push retrieval precision further downstream.

---

## Notable Quotes

> "You can spend $5 to ask a question and still have about a one in five chance the model doesn't actually make proper use of the amount of crap you just shoved in its throat. That's not a triumph. That's a casino."

> "The real question isn't can your model survive a million token dump. The question is why the hell are you dumping a million tokens in there in the first place?"

> "A giant context window is not a substitute for retrieval. It's just not. A million token window is not some magical get-out-of-engineering-free card."

---
