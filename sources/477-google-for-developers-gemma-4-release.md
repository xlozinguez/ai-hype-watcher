---
source_id: "477"
title: "What’s new in Gemma 4"
creator: "Google for Developers"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=jZVBoFOJK-Q"
date: "2026-04-02"
duration: "2:52"
type: "video"
tags: ["ai-landscape", "agentic-coding", "enterprise-ai", "context-engineering", "security"]
curriculum_modules: ["01-foundations", "04-agentic-patterns", "06-strategy-and-economics"]
---

# 477: What’s new in Gemma 4

> **Creator**: Google for Developers | **Platform**: YouTube | **Date**: 2026-04-02 | **Duration**: 2:52

# What's New in Gemma 4

## Summary

Google DeepMind announced Gemma 4, a family of open models designed to run locally on developer-owned hardware — phones, laptops, and desktops. The release marks a significant shift: for the first time, Google is releasing a Gemma model under an Apache 2.0 open-source license, lowering the barrier for commercial use and enterprise adoption. With over 400 million downloads and 100,000 variants of previous Gemma models in the wild, this release responds directly to community demand for more capable, more open, and more deployable local models.

The model family spans four variants targeting different deployment contexts. The 26B mixture-of-experts (MoE) and 31B dense models are designed for personal computers, offering frontier-level reasoning and coding locally. The 2B and 4B "Effective" models target mobile and IoT devices, featuring combined audio and vision support for real-time processing and native support for over 140 languages. The larger models support context windows up to 250,000 tokens, enabling full codebase analysis and multi-turn agentic workflows.

A central design theme across the family is agentic readiness — native tool use, multi-step planning, and complex reasoning optimized for token efficiency. Google positions Gemma 4 as infrastructure for enterprise agentic pipelines, backed by the same security protocols applied to their proprietary Gemini models.

## Key Concepts

### Apache 2.0 Licensing as a Strategic Inflection Point
Previous Gemma models used a custom license that restricted certain commercial uses. The move to Apache 2.0 removes those friction points, making Gemma 4 far more viable for enterprise products, commercial derivatives, and open-source projects. This is a direct competitive response to the permissive licensing of models like Meta's Llama series.

### MoE vs. Dense: Tradeoff-Aware Model Design
The 26B MoE model activates only 3.8B parameters per inference pass, making it significantly faster and more memory-efficient than its parameter count suggests. The 31B dense model trades that speed for output quality. This explicit tradeoff framing helps developers match model choice to workload: latency-sensitive agentic pipelines vs. quality-critical code generation tasks.

### On-Device Multimodal Intelligence
The 2B and 4B Effective models combine audio and vision processing with multilingual support (140+ languages) in a form factor small enough for mobile and IoT deployment. This enables real-time multimodal agents that can operate entirely on-device, without data leaving the user's environment — a meaningful capability for privacy-sensitive enterprise and consumer use cases.

### Context Window Scale for Agentic Use Cases
The larger Gemma 4 models support up to 250,000-token context windows. At that scale, entire codebases or extended multi-turn agentic conversation histories fit within a single context, reducing the need for complex retrieval pipelines or context compression strategies when running local agentic workflows.

### Security Parity with Proprietary Models
Google explicitly claims Gemma 4 undergoes the same security evaluation protocols as their closed Gemini models. For enterprises building on open-weight models, this is a meaningful trust signal — addressing a common objection that open models lack the safety vetting of proprietary alternatives.

## Practical Takeaways

- **Local agentic pipelines are now more viable**: The 26B MoE's 3.8B activated parameter count means fast, capable inference on consumer hardware without API costs or data egress — directly relevant for building private coding agents or multi-step task automation.
- **Apache 2.0 removes the licensing blocker**: Teams that previously avoided Gemma for commercial products can now use Gemma 4 weights freely; worth revisiting any prior "we can't use this" decisions.
- **Match model to deployment target**: Use 26B MoE for speed-sensitive local desktop/laptop agents; 31B dense for quality-sensitive tasks; 2B/4B Effective for mobile or embedded scenarios.
- **250K context window changes codebase analysis locally**: For developers using context engineering approaches with full-repo context, Gemma 4's window size enables on-device workflows previously requiring cloud API calls.
- **Multilingual + multimodal in tiny form factor**: The Effective models' 140-language support and combined audio/vision opens up agent development for non-English markets and voice/vision interface patterns without cloud dependency.

## Notable Quotes

> "For the first time ever, we are releasing Gemini under an open-source Apache 2.0 license."

> "You can run state-of-the-art local reasoning and coding pipeline without needing to upload data outside of your controlled environment."

> "As open models become more central to enterprise infrastructure, security is paramount."
