---
source_id: "439"
title: "China's New AI Wave: AI Agents, Open Source, and OpenClaw with Tom Wang at Hugging Face"
creator: "High Capacity"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=wpiI5QRNzKE"
date: "2026-03-19"
duration: "60:43"
type: "video"
tags: ["ai-landscape", "ai-economics", "ai-hype"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 439: China's New AI Wave: AI Agents, Open Source, and OpenClaw with Tom Wang at Hugging Face

> **Creator**: High Capacity | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 60:43

# China's New AI Wave: AI Agents, Open Source, and OpenClaw with Tom Wang at Hugging Face

## Summary

Tom Wang, Head of Asia Pacific Ecosystems at Hugging Face, provides an insider view of China's open source AI landscape, tracing its evolution from early Chinese LLMs before LLaMA through the current post-DeepSeek wave. He explains how Hugging Face functions as the "GitHub for AI" — a central hub for model weights, datasets, and demos — and how his role involves helping Chinese labs maximize their impact on the global developer community. The conversation covers key players including Qwen, DeepSeek, Kimi, MiniMax, and Jipu, and why open source has become the dominant strategy for Chinese AI labs seeking credibility, investment, and developer adoption.

A central theme is how open sourcing models has replaced traditional marketing and VC pitches as the primary trust mechanism in AI. When a model is open source, anyone can download and test it locally — cutting off the internet to verify it isn't "phoning home" — which provides a level of transparency that demos and benchmark claims simply cannot. This dynamic helped fuel Kimi's valuation growth roughly sixfold and drove the IPOs of MiniMax and Jipu, demonstrating that open source contributions translate directly into commercial outcomes.

The conversation also covers the practical mechanics of getting traction on Hugging Face: good model cards, honest benchmark claims focused on specific strengths, visual demos that show rather than tell, and engaging with community feedback in discussion panels. The derivative model ecosystem — where researchers download, fine-tune, and re-upload models creating lineage trees — is highlighted as a key indicator of genuine community adoption, with Qwen currently leading in derived models on the platform.

## Key Concepts

### Open Source as Trust and Marketing Infrastructure
In an environment where Chinese AI labs were struggling to differentiate themselves during the "hundred models" era (百模大战), open sourcing became the credibility mechanism VCs and developers actually trusted. A released model can be tested by anyone, on local hardware, with the internet disconnected — making it far harder to fake capability than a curated demo. DeepSeek's release of R1 with no traditional marketing, yet topping the App Store, crystallized this dynamic for the entire industry.

### Derivative Model Ecosystems as Adoption Signal
The number of "derived models" — where researchers download a base model, fine-tune it with new data, and re-upload it — is a more reliable signal of genuine community adoption than download counts or self-reported benchmarks. Qwen currently leads on Hugging Face by this metric. Building on popular architectures (e.g., DeepSeek) also provides downstream benefits: existing framework support, toolchain compatibility, and instant credibility with the developer community.

### Model Cards and Positioning for Developer Traction
Simply uploading model weights is insufficient for gaining traction on Hugging Face given the density of competing releases. Effective launches require: a thorough model card explaining the model's purpose and lineage, honest benchmark claims focused on specific strengths rather than broad superiority claims, links to technical reports, a live demo (Hugging Face Space), and a clearly articulated "selling point" (e.g., "spawn many agents with small compute budget"). Visual, shareable outputs — like beautiful AI-generated websites — outperform abstract metric comparisons for organic spread.

### Chinese AI Lab Generations and Key Players
The Chinese open source AI landscape has distinct generations: early Chinese-language models (GLM-6B, pre-LLaMA), Apache-licensed releases like Yi by Kai-Fu Lee, research-focused labs like Qwen (Alibaba), the quietly influential DeepSeek (with MLA architecture and detailed technical reports), and the current cohort including Kimi/Moonshot, MiniMax, and Jipu. Each generation built on prior infrastructure and community trust, with DeepSeek's R1 acting as a global inflection point that brought Western media attention to a trend that had been building for two years.

### Community Feedback as R&D Signal
Discussion panels on Hugging Face and GitHub serve as direct pipelines between model developers and potential users. Tom frames seemingly critical comments not as negative feedback but as engaged potential collaborators pointing to improvement directions, offering data, and describing deployment contexts. This community interaction loop is treated as a valuable R&D input rather than a PR risk.

## Practical Takeaways

- **Benchmark claims need specificity to be believed**: Claiming general superiority over closed-source models won't land with developers. Claims like "efficient multi-agent spawning with small inference budget" are credible and differentiated — broad leaderboard dominance claims are not.
- **Build on established architectures strategically**: Releasing a model derived from DeepSeek inherits its ecosystem support (framework integrations, quantization tooling, community familiarity), dramatically lowering the barrier to adoption — and model lineage metadata on Hugging Face makes this discoverable.
- **Visual and shareable outputs are the best organic marketing**: When a model can produce something people can screenshot and share (beautiful websites, visual artifacts), that spreads faster and more convincingly than numerical benchmark tables.
- **Derived model count is a signal worth tracking**: For evaluating genuine open source adoption and community health of a Chinese AI lab, count how many researchers are building derivative models on Hugging Face — this is harder to game than downloads or self-reported evals.
- **Community discussion panels are early user research**: Engaging with Hugging Face and GitHub discussion threads on model releases is a direct channel to the most motivated potential users — treat criticism there as a feature request backlog, not a reputation risk.

## Notable Quotes

> "The venture capitals is really happy. Like in the past year, we have seen Kimi — the valuation has risen from like 20-something billion to 18 billion... the market cap has risen like six times or even more. Like that's the real power of the open source community."

> "Open source has become a great way for people to justify that they have the muscle. Because once the model is open source, it's putting under the spotlight. And everyone is able to identify if it is a good model or not because everyone can try the model."

> "Deep Seek was very hidden... their leader was attending a Chinese podcast or interview. And other than that, you have nothing. And all of a sudden out of nowhere a great model gets released. Do nothing and win."
