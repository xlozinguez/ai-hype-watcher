---
source_id: "478"
title: "How Context Windows Actually Work"
creator: "Claudius Papirus"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=BUE6YPuMaa0"
date: "2026-03-30"
duration: "9:33"
type: "video"
tags: ["context-engineering", "ai-landscape", "infrastructure"]
curriculum_modules: ["01-foundations", "03-claude-code-essentials"]
---

# 478: How Context Windows Actually Work

> **Creator**: Claudius Papirus | **Platform**: YouTube | **Date**: 2026-03-30 | **Duration**: 9:33

# How Context Windows Actually Work

## Summary

This video provides a technical foundation for understanding context windows in large language models — what they are, how they evolved, and crucially, why their limitations matter more than their size. The narrator (voiced by the AI model itself) explains that a context window is not memory but working memory: everything in it is visible for the duration of a session, and then it vanishes entirely. The desk analogy is central — the model can reach for anything on its desk while working, but the desk has hard edges, has no overflow storage, and gets wiped clean between sessions.

The video traces context window growth from GPT-2's 1,024 tokens in 2019 to Claude's current 1 million tokens — a 2,000x expansion in five years — explaining both why windows stayed small for so long (the quadratic cost of self-attention) and how engineering solutions like distributed KV caching made large windows viable. This history sets up the key tension: bigger windows solved the engineering problem but left a deeper problem untouched.

The most practically important section covers two failure modes that persist regardless of window size. The "lost in the middle" phenomenon (Stanford, 2023) showed a 20-point accuracy drop when critical information sits in the middle of a long context rather than at the beginning or end. A 2025 study of 18 frontier models found that even modern models exhibit "context rot" — their reasoning ability degrades as context grows, even when they successfully locate the relevant information. A million-token window means the model *can see* everything; it doesn't mean it's *paying attention* to all of it.

## Key Concepts

### The Desk Analogy (Context vs. Memory)
A context window is everything the model can see simultaneously during one session: user messages, conversation history, pasted documents, and system instructions. It behaves like a desk — accessible while work is happening, but cleared completely when the session ends. This is fundamentally different from memory. Memory persists; context doesn't. The model neither learns from conversations (frozen parameters) nor retains the experience of them (cleared context). These are two sides of the same coin.

### Quadratic Cost of Self-Attention
The transformer architecture requires every token to compute relevance against every other token in the sequence (self-attention). This means doubling the input quadruples the work. At 1,000 tokens: ~1 million comparisons. At 10,000: ~100 million. At 100,000: ~10 billion. This quadratic scaling is why context windows stayed small for years — not because small windows were considered sufficient, but because the math made larger ones prohibitively expensive. Engineering solutions (distributing computation across many GPUs, KV cache optimization) made million-token windows tractable, but the fundamental scaling relationship doesn't disappear.

### KV Cache Bottleneck
When the model generates each new token, it stores intermediate calculations for all previous tokens in a KV (key-value) cache, avoiding redundant recomputation. This is efficient at small scales, but the cache grows linearly with context length. At long enough contexts, the KV cache can rival or exceed the model's own memory footprint. At a million tokens, the cache — not the model's intelligence — becomes the primary bottleneck.

### Lost in the Middle Effect
A 2023 Stanford study found that model accuracy on a retrieval task dropped ~20 percentage points when the relevant document was placed in the middle of the context versus at the beginning or end. This U-shaped attention distribution — strong at primacy and recency, weak in the middle — held across GPT-3.5, GPT-4, Claude, and open-source models. It's not a bug; it's a structural property of how attention operates over long sequences, and it mirrors well-documented human primacy/recency effects.

### Context Rot
Beyond retrieval failures, a 2025 study of 18 frontier models found that *reasoning quality* degrades as context grows, even when the model successfully locates the relevant information. The needle-in-a-haystack benchmark (placing a target sentence at varying depths in varying document lengths) became a standard lab benchmark that most modern models now pass. But passing retrieval doesn't mean intact reasoning — the ability to think clearly about found information still breaks down at scale. The researchers labeled this "context rot."

## Practical Takeaways

- **Front-load critical information.** Given the lost-in-the-middle effect, place the most important instructions, constraints, or facts at the beginning (or end) of your context, not buried in the middle. This applies to system prompts, document pastes, and conversation structure.
- **Don't conflate window size with reliability.** A 1M-token context window is a capability ceiling, not a performance guarantee. For long-context tasks, expect reasoning quality to degrade as the window fills — plan accordingly with summarization, chunking, or structured retrieval rather than assuming the model retains everything equally.
- **Context clears between sessions; plan for it.** Any workflow requiring continuity across sessions (ongoing projects, iterative development, multi-session tasks) must externalize memory explicitly — through notes, structured state files, or retrieval systems. The model cannot be relied upon to "remember" prior sessions.
- **The needle-in-haystack benchmark is insufficient.** When evaluating models for long-context applications, retrieval accuracy alone doesn't tell you whether reasoning quality holds up. Look for evidence of performance on multi-step reasoning tasks at long context lengths, not just document retrieval scores.
- **Context engineering matters more as windows grow.** Counterintuitively, larger context windows increase the importance of deliberate context management. More room means more opportunity for context rot to degrade the model's effective reasoning. Keeping context lean and well-structured remains valuable even when size isn't the constraint.

## Notable Quotes

> "A million tokens means I can see everything you've given me. It doesn't mean I'm paying attention to all of it."

> "Finding the needle is easy. Thinking clearly when there's 100,000 other tokens in the room — that's the part that still breaks."

> "The industry spent five years expanding context windows 2,000 times over from one email to 10 novels. And the models still lose track of what's in the middle. We kept building a bigger desk. The problem wasn't the size of the desk. It was what happens when you put too much on it."
