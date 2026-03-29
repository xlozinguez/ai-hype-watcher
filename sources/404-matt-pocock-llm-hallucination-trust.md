---
source_id: "404"
title: "Never Trust An LLM"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=9VNG0h4pLh0"
date: "2026-03-27"
duration: "14:00"
type: "video"
tags: ["prompt-engineering", "validation", "security", "ai-hype", "context-engineering"]
curriculum_modules: ["01-foundations", "02-prompting-and-workflows"]
---

# 404: Never Trust An LLM

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-03-27 | **Duration**: 14:00

# Never Trust An LLM

## Summary

Matt Pocock, a software developer and TypeScript educator, makes a direct case that LLM hallucinations are so frequent and varied that developers should never extend implicit trust to any LLM output. Drawing on a comprehensive academic taxonomy of hallucination types and an OpenAI paper on why hallucinations occur, he walks through concrete, high-stakes examples — including an Alphabet stock drop from a Bard ad and Air Canada's legal liability from a chatbot's fabricated bereavement policy — to demonstrate that hallucinations aren't edge cases but a structural feature of how LLMs work.

The core technical explanation centers on compression: LLMs are trained by compressing massive datasets into a much smaller parameter space, inevitably losing fidelity. When queried about something that survived the compression poorly, the model doesn't admit ignorance — it guesses — because training and evaluation benchmarks reward confident answers over refusals. This creates a fundamental tension: models tuned to be highly capable tend to over-confidently confabulate, while models tuned to acknowledge uncertainty tend to underperform on tasks requiring deep reasoning.

Despite this, Pocock remains pro-LLM. The key distinction he draws is between **intrinsic information** (data explicitly provided in the context window) and **extrinsic information** (knowledge from training data). LLMs are far more reliable when reasoning over content you've given them. His practical guidance centers on forcing models to retrieve fresh information via search tools rather than relying on training-set knowledge, while still treating even in-context responses with healthy skepticism for high-stakes domains.

---

## Key Concepts

### Intrinsic vs. Extrinsic Hallucinations

The academic taxonomy Pocock references distinguishes two hallucination origins. **Intrinsic hallucinations** occur when the model contradicts or ignores information explicitly present in the current conversation — the Air Canada chatbot inventing a bereavement policy refund window despite presumably having the real policy in its context is a clear example. **Extrinsic hallucinations** occur when the model fabricates information from outside the conversation, drawing on (or misremembering) training data — such as inventing a software package that doesn't exist. Extrinsic hallucinations are significantly more common and harder to catch because the user often lacks the reference to spot them.

### LLM Training as Lossy Compression

An LLM's weights are the result of compressing enormous datasets into a fixed parameter budget. Like JPEG compression applied aggressively, fine details are lost first. When the model is queried about something that survived compression poorly, it reconstructs a plausible-sounding answer from the blurry residue — not from any stored fact. This structural limitation means extrinsic knowledge retrieval is inherently unreliable, regardless of how confident the output sounds.

### Guessing Is Rewarded Over Refusal

A key insight from the referenced OpenAI paper: LLMs hallucinate partly because their training and benchmark evaluation procedures reward confident answers over "I don't know." Benchmark leaderboards incentivize models to attempt answers rather than abstain, because abstaining tanks scores on tasks where a guess might be correct. This creates a systemic bias toward over-confident confabulation baked into the models themselves — not a bug that will simply be patched away.

### The "Use Your Search Tool" Prompt

The practical workaround Pocock advocates for bridging the extrinsic knowledge gap: explicitly instructing the model to use its web search tool (e.g., "Use your search tool"). Left to its own devices, a confident model may answer from training data even when a search capability is available. The explicit instruction forces retrieval, pulling current source documents into the context window and converting an extrinsic query into an intrinsic one — dramatically improving reliability. He notes citations appear in the response as a quality signal.

### Contextual Inconsistency as a Residual Risk

Even after converting to intrinsic information via search or direct document injection, a category of hallucination remains: contextual inconsistency, where the model ignores or contradicts content explicitly in its own context window. This means the search-tool workaround reduces but does not eliminate hallucination risk. For legally, medically, or financially consequential outputs, human verification against primary sources remains mandatory regardless of prompt technique.

---

## Practical Takeaways

- **Default to skepticism on all extrinsic claims.** Fabricated packages, non-existent laws, invented statistics — if the LLM is drawing from training data rather than something you gave it, treat the output as a starting hypothesis requiring verification, not a fact.
- **Always append "Use your search tool"** when asking LLMs for current information, specific facts, or anything time-sensitive. This forces retrieval into the context window rather than reliance on compressed training knowledge.
- **Pass documents, codebases, and reference material explicitly.** LLMs reason far more reliably over content in their context window. When possible, provide the source material rather than asking the model to recall it.
- **Never deploy LLM outputs in high-stakes contexts without human verification.** Legal advice, medical information, financial policy, and safety-critical content require human review against authoritative primary sources — the Air Canada case illustrates the legal and financial liability of skipping this step.
- **Watch for package/dependency hallucinations specifically.** This is an active supply chain attack vector: adversaries register packages matching common LLM hallucinations, making fabricated dependency recommendations a real security threat in developer workflows.

---

## Notable Quotes

> "LLMs hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty."
> — OpenAI paper quoted by Pocock

> "When you're using AI, you need to always make sure that you're providing it the information it needs to succeed."

> "Even if you're an airline and you have a chatbot with a bereavement policy explicitly passed to it, it might still get it wrong."

---
