---
source_id: "404"
title: "Never Trust An LLM"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=9VNG0h4pLh0"
date: "2026-03-27"
duration: "14:00"
type: "video"
tags: ["prompt-engineering", "validation", "security", "context-engineering", "ai-hype"]
curriculum_modules: ["02-prompting-and-workflows", "01-foundations"]
---

# 404: Never Trust An LLM

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-27 | **Duration**: 14:00

## Summary

Matt Pocock, a software developer and TypeScript educator, makes the case that LLMs hallucinate so frequently and in so many ways that developers should adopt a baseline posture of never trusting LLM output implicitly. Drawing on a comprehensive academic taxonomy of hallucination types and an OpenAI paper on why hallucinations occur, he walks through the most common failure modes: factual errors from training data, fabricated entities (including non-existent packages), and contextual inconsistencies where the model ignores information explicitly provided to it.

The core explanation for why hallucinations happen centers on compression and incentive structures. LLM training is fundamentally a lossy compression of vast datasets, meaning the model's "memory" is a degraded representation of the original information. Compounding this, benchmarking systems reward confident guessing over honest uncertainty, training models to attempt answers rather than admit ignorance — a structural problem that may not be fully solvable.

Despite this, Pocock remains pro-AI because reliability improves dramatically when the model works from *intrinsic* information (content you explicitly provide in context) rather than *extrinsic* knowledge (its training data). He offers a practical mitigation strategy: always supply relevant documents or data, and use the four-word prompt "use your search tool" to force the model to fetch current information rather than confabulate from stale training weights.

## Key Concepts

### Intrinsic vs. Extrinsic Hallucinations
The paper Pocock cites distinguishes two hallucination sources. **Intrinsic hallucinations** occur when a model contradicts or ignores information already present in the current conversation context — e.g., an airline chatbot fabricating a bereavement policy even though the real policy was in its context window. **Extrinsic hallucinations** occur when the model invents information not present anywhere in the conversation, drawing instead on (faulty) training data. Extrinsic hallucinations are far more common and harder to detect.

### LLM Training as Lossy Compression
LLMs are trained by compressing enormous datasets down to a size that fits on a GPU. This compression necessarily discards detail. Pocock uses a progressively JPEG-compressed photo as an analogy: broad strokes survive but fine detail is destroyed. When a model answers from training data, it's reconstructing from this degraded representation — capable of coarse facts but unreliable on specifics, citations, and edge cases.

### Benchmark Incentives Reward Guessing Over Refusal
An OpenAI paper Pocock cites argues hallucinations persist because training and evaluation procedures reward confident answers over admitting uncertainty. Benchmark leaderboard performance improves when models guess rather than abstain, so models are implicitly optimized to attempt every answer. This creates a structural tension: the same confidence that enables deep reasoning also produces hallucinated facts.

### Fabricated Entities and Supply Chain Risk
LLMs readily invent software packages, government departments, laws, and other entities that don't exist. For developers, this creates a concrete security risk: attackers can register malicious packages with the names LLMs commonly hallucinate, causing developers who blindly install AI-recommended dependencies to execute malware. This is a live, documented attack vector, not a theoretical one.

### Contextual Inconsistency
Even when you explicitly provide accurate information in the context window, models can ignore or contradict it. This is the most surprising failure mode — it means RAG pipelines, document-grounded chatbots, and agentic systems that inject context are not immune to hallucination. For high-stakes domains (legal, medical, financial), explicit verification steps are still necessary even with well-constructed context.

## Practical Takeaways

- **Default to providing context, not querying training memory.** Pass relevant documents, codebases, or data directly into the conversation. Intrinsic (context-provided) information produces far more reliable responses than extrinsic (training-data) recall.
- **Use "use your search tool" as a forcing function.** This four-word prompt overrides the model's tendency to answer confidently from stale training data, directing it to fetch current information and cite sources — effectively converting an extrinsic query into an intrinsic one.
- **Never trust LLM-recommended packages without verification.** Always verify that suggested libraries actually exist on the relevant registry (npm, PyPI, etc.) before installing. This directly mitigates the supply chain attack vector created by fabricated entity hallucinations.
- **For critical outputs, treat contextual inconsistency as a real risk.** Even when you've provided the ground-truth document, add explicit verification steps or secondary checks for legal, medical, financial, or safety-sensitive use cases. Do not assume context injection eliminates hallucination risk.
- **Calibrate trust to the task type.** LLMs are highly reliable for reasoning over provided content, code transformation, and synthesis tasks. They are unreliable for factual recall, citation generation, and knowledge about recent events — use search grounding for all of the latter.

## Notable Quotes

> "LLMs hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty." — OpenAI paper cited by Pocock

> "When you're using AI, you need to always make sure that you're providing it the information it needs to succeed."

> "Even if you're an airline and you have a chatbot with a bereavement policy explicitly passed to it, it might still get it wrong."
