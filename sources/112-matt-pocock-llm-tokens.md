---
source_id: "112"
title: "Most devs don't understand how LLM tokens work"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=nKSk_TiR8YA"
date: "2025-09-19"
duration: "10:58"
type: "video"
tags: ["ai-landscape", "prompt-engineering", "context-engineering"]
curriculum_modules: ["01-foundations", "03-context-engineering"]
---

# 112: Most devs don't understand how LLM tokens work

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2025-09-19 | **Duration**: 10:58

## Summary

Pocock delivers a practical deep dive into how LLM tokenization works, motivated by the observation that only about a third of developers at his AI workshop could explain what a token is. Using TypeScript code examples throughout, he walks through the full lifecycle: encoding text into numeric tokens, LLM processing, and decoding output tokens back into text.

The video explains why different model providers produce different token counts for the same input by exploring how tokenizer vocabularies are built. Starting from a character-level tokenizer and progressing to subword-level tokenization (the approach used in practice), Pocock demonstrates how vocabulary size creates trade-offs between token efficiency and model size. He shows that more common words and languages produce fewer tokens, giving commonly-used programming languages a concrete efficiency advantage in the AI era.

## Key Concepts

### Tokens as LLM Currency ([00:30](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=30))

Tokens are the fundamental unit of LLM computation. Input text is broken into chunks, each mapped to a numeric ID in the model's vocabulary. The LLM processes these numbers — not text — and outputs new token IDs that are decoded back into text. Users are billed per token, with input and output tokens priced differently.

### Tokenizer Vocabularies Differ Between Providers ([04:30](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=270))

Each model provider trains its own tokenizer with a different vocabulary. The same "hello world" prompt produces 11 input tokens on Anthropic's Claude 3.5 Haiku but only 4 on Google's Gemini 2.0 Flash Lite. This is because vocabularies assign different subword groupings, so identical text maps to different token counts.

### Vocabulary Size Trade-offs ([06:30](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=390))

Larger vocabularies (e.g., 200K tokens) produce fewer tokens per input because they can match longer subword chunks, making LLM processing more efficient. However, larger vocabularies require bigger models and more memory. This is a core engineering trade-off that model providers make differently — OpenAI's GPT-4o uses the O200K base tokenizer.

### Subword Tokenization via Byte-Pair Encoding ([05:30](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=330))

Tokenizers are trained by identifying frequently co-occurring character groups in the training corpus. Starting from individual characters, the algorithm iteratively merges the most common pairs into larger tokens. Real tokenizers repeat this process to build groups of groups, producing subword tokens that balance vocabulary size with compression efficiency.

### Language Frequency Affects Token Efficiency ([09:00](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=540))

Unusual words like Lewis Carroll's "frabjous" get split into more tokens because they appear rarely in training data. This extends to spoken languages underrepresented in the training corpus and to less common programming languages — 20 lines of JavaScript will produce fewer tokens than 20 lines of Haskell, giving mainstream languages a practical cost and context-window advantage.

## Practical Takeaways

- **Understand your token costs**: Input and output tokens are billed at different rates. Use the usage object from SDK responses to track actual consumption per API call.
- **Vocabulary size matters for context budgets**: Fewer tokens per input means more room in the context window. When optimizing for context efficiency, be aware that token counts vary by provider for the same text.
- **Common languages are cheaper**: Widely-used programming languages and natural languages produce fewer tokens, meaning lower costs and more efficient context window usage.
- **Use provider tokenizer tools to estimate**: Libraries like JS tiktoken let you pre-calculate token counts before sending requests, enabling better cost and context management.

## Notable Quotes

> "Tokens are the currency of LLMs. When you send an input of Hello World to an LLM, that gets broken down into its constituent tokens." — Matt Pocock ([00:30](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=30))

> "While you think that the LLM is dealing with text, it's actually dealing with these numeric representations of chunks of text." — Matt Pocock ([04:00](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=240))

> "Unusual words are split up into more tokens than words that occur more frequently in the data set. This also means that if you're querying the LLM in a language that's not present in the data set much, it's likely to break it up into more tokens." — Matt Pocock ([09:00](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=540))

## Related Sources

- [011: Prompt Engineering is Dead](011-confluent-developer-context-engineering.md) — Context engineering as the evolution beyond prompt engineering
- [031: 9 AI Concepts Explained](031-bytebyteai-ai-concepts.md) — Broader overview of AI fundamentals including tokenization
- [084: The 60% Rule Stops Context Rot](084-dylan-davis-context-rot-60-rule.md) — Practical context window management strategies
- [114: Most devs don't understand how context windows work](114-matt-pocock-context-windows.md) — Pocock's companion video on context windows

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — Core LLM mechanics including tokenization
- [Module 03: Context Engineering](../curriculum/03-context-engineering/README.md) — Token efficiency and context window optimization
