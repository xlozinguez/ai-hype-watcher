---
source_id: "130"
title: "What is Prompt Caching? Optimize LLM Latency"
creator: "IBM Technology"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=u57EnkQaUTY"
date: "2026-02-07"
duration: "09:06"
type: "video"
tags: ["prompt-engineering", "context-engineering", "infrastructure"]
curriculum_modules: ["02-prompt-engineering", "03-context-engineering"]
---

# 130: What is Prompt Caching? Optimize LLM Latency

> **Creator**: IBM Technology | **Platform**: YouTube | **Date**: 2026-02-07 | **Duration**: 09:06

## Summary

IBM Technology provides a clear technical explainer on prompt caching — a technique for reducing LLM latency and cost by caching the precomputed key-value (KV) pairs from the input prompt's prefill phase. The video carefully distinguishes prompt caching from output caching (which stores entire responses for identical queries) and explains why the distinction matters: prompt caching caches only the input processing, allowing different questions to be asked against the same cached context without re-processing it.

The explanation grounds the concept in transformer mechanics. When an LLM receives a prompt, it computes KV pairs at every transformer layer for every input token — the model's internal representation of how words relate to each other. For a short prompt like "What's the capital of France?" this is negligible. For a 50-page document followed by a question, the prefill computation is substantial. Prompt caching stores these KV pairs so that subsequent requests with the same document prefix skip the expensive computation and only process the new question at the end.

The video covers practical considerations: what can be cached (system prompts, documents, few-shot examples, tool definitions, conversation history), how prefix matching works (token-by-token from the beginning, stopping at the first difference), why prompt structure matters (static content must come first, dynamic content last), minimum token thresholds (~1,024 tokens), and cache TTL (typically 5-10 minutes, up to 24 hours). Some providers offer automatic caching while others require explicit cache boundary markers in API calls.

## Key Concepts

### KV Pair Caching vs. Output Caching ([01:00](https://www.youtube.com/watch?v=u57EnkQaUTY&t=60))

Output caching stores the entire response for identical queries — the same question returns the same answer without hitting the model. Prompt caching is fundamentally different: it stores only the precomputed KV pairs from the input prefill phase. The LLM still generates a fresh response, but it skips the expensive step of re-processing the input context. This means you can cache a 50-page document once and ask unlimited different questions against it.

### The Prefill Phase and KV Pairs ([02:30](https://www.youtube.com/watch?v=u57EnkQaUTY&t=150))

Before generating its first output token, an LLM computes key-value pairs at every transformer layer for every token in the input. These KV pairs represent the model's internal understanding of the prompt — how every word relates to every other word, what context matters, what to focus on. For long inputs, this prefill computation is the dominant cost in both latency and compute. Prompt caching stores these KV pairs so they can be reused across requests.

### Prefix Matching and Prompt Structure ([05:30](https://www.youtube.com/watch?v=u57EnkQaUTY&t=330))

The cache matches from the very first token, proceeding token-by-token until it encounters a difference. This makes prompt structure critical: static content (system instructions, documents, few-shot examples) must come first, dynamic content (user questions) last. If the dynamic question is placed before the static document, the cache fails immediately on the second request because the prefix differs. This is the single most important practical consideration for leveraging prompt caching effectively.

### Cacheable Content Types ([04:30](https://www.youtube.com/watch?v=u57EnkQaUTY&t=270))

System prompts are the most common cached content — every chatbot has personality and behavior instructions that remain constant across requests. Documents (product manuals, research papers, legal contracts) are the highest-value target for caching. Few-shot examples, tool and function definitions, and conversation history are also cacheable. The common thread is any content that remains stable across multiple requests.

## Practical Takeaways

- **Structure prompts with static content first**: System instructions, documents, and few-shot examples should precede the user's question. Putting dynamic content early breaks prefix matching and defeats caching entirely.
- **Prompt caching shines for document Q&A workflows**: Upload a long document once and ask multiple questions against it — each subsequent question only processes the new question text, not the entire document.
- **Minimum threshold applies**: Caching typically requires at least 1,024 tokens before the overhead of managing the cache is worthwhile. Short prompts do not benefit.
- **Cache entries expire**: Most caches clear after 5-10 minutes (some up to 24 hours). Design workflows around this TTL if you are batching requests against cached context.
- **Check your provider's caching model**: Some providers (like Anthropic) offer automatic caching based on prefix matching. Others require explicit cache boundary markers in API calls.

## Notable Quotes

> "Prompt caching is about caching only the input prompt so that the LLM doesn't need to process it a second time." — IBM Technology ([01:30](https://www.youtube.com/watch?v=u57EnkQaUTY&t=90))

> "We can think of these KV pairs as the model's internal understanding of your prompt. How every word relates to every other word, what context matters, what information to focus on." — IBM Technology ([03:00](https://www.youtube.com/watch?v=u57EnkQaUTY&t=180))

## Related Sources

- [011: Prompt Engineering is Dead](011-confluent-developer-context-engineering.md) — The shift from prompt engineering to context engineering, where caching becomes a critical optimization
- [084: Context Rot and the 60% Rule](084-dylan-davis-context-rot-60-rule.md) — Context management strategies that interact with caching behavior
- [031: 9 AI Concepts Explained](031-bytebyteai-ai-concepts.md) — Foundational AI concepts including tokenization

## Related Curriculum

- [Module 02: Prompt Engineering](../curriculum/02-prompt-engineering/README.md) — Prompt structure optimization, static-before-dynamic ordering
- [Module 03: Context Engineering](../curriculum/03-context-engineering/README.md) — KV pair caching as context optimization, prefix matching, cache-aware prompt design
