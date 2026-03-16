---
source_id: "302"
title: "Build My Own ChatGPT? Testing w/ Karpathy's Nanobot Model Training"
creator: "Onchain AI Garage"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=jZB0VeXlETU"
date: "2026-03-13"
duration: "16:18"
type: "video"
tags: ["ai-economics", "infrastructure", "ai-landscape"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 302: Build My Own ChatGPT? Testing w/ Karpathy's Nanobot Model Training

> **Creator**: Onchain AI Garage | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 16:18

# Build My Own ChatGPT? Testing w/ Karpathy's Nanobot Model Training

## Summary

This video documents a hands-on experiment training a miniature GPT-2-style language model locally using Andrej Karpathy's open-source NanoChat repository, on a consumer gaming laptop (RTX 4070, 8GB VRAM). The creator walks through the full pipeline: downloading NVIDIA's ClimateMix 400B dataset (8 shards), training a tokenizer, running pre-training for ~2.5 hours, and then performing a truncated supervised fine-tuning (SFT) pass to produce a functional (if incoherent) chatbot — all at zero cloud cost.

The experiment is framed around the dramatic collapse in LLM training costs: training GPT-2 cost $43,000 in 2019 and took 168 hours; researchers like Karpathy are now achieving equivalent results in under 2 hours for ~$48 on cloud H100s, and AI agents (via AutoResearch) are actively optimizing those training runs further. The video positions this as accessible educational infrastructure — NanoChat requires no frontier model, no Claude Code, just math running on a GPU.

The final chatbot result is honest and unpolished: the model produces topically adjacent but largely incoherent responses, primarily because the SFT step was cut short (10 steps instead of the full run) due to hardware constraints. The creator notes the logical next step would be running AutoResearch on top of the trained NanoChat model to optimize hyperparameters — the same approach Karpathy himself has been experimenting with.

## Key Concepts

### NanoChat as a Self-Contained LLM Training Stack
NanoChat is Karpathy's minimal, single-GPU-compatible harness covering all LLM stages: tokenization, pre-training, fine-tuning (SFT), evaluation, inference, and chat UI. A single `depth` parameter (number of transformer layers) controls model scale. It requires no external AI model — training is purely mathematical optimization on local hardware. This makes it genuinely educational and hackable.

### The Training Cost Collapse
The video anchors a striking data point: GPT-2-equivalent training fell from $43,000 / 168 hours (2019) to ~$48 / <2 hours (2025-2026), a ~900x cost reduction in roughly 6 years. AI agents (AutoResearch) are now accelerating this further by autonomously tuning training recipes. This trajectory has direct implications for who can train capable models and at what cost.

### Pre-training vs. Supervised Fine-Tuning (SFT)
Pre-training teaches a model to predict the next token by reading massive text corpora — it produces a text completer, not a chatbot. SFT is the subsequent step that teaches the model to respond in a conversational format using synthetic human/assistant turn data. The video demonstrates this distinction concretely: the pre-trained model produces incoherent streams of text; the (truncated) SFT model at least attempts to respond to prompts, even if poorly.

### Validation Loss (BPB) as a Training Signal
The model's quality is tracked via Bits Per Byte (BPB), a validation loss metric. The local run started at 3.17 and reached 0.94 after ~142 minutes of training. Karpathy's research targets ~0.74 BPB for GPT-2-level capability. This gives a concrete, interpretable signal for comparing consumer hardware results against research-grade baselines.

### AutoResearch + NanoChat as a Compound Loop
Karpathy's current approach combines NanoChat (trains the model weights) with AutoResearch (optimizes the training recipe itself via AI agents). The creator draws an explicit conceptual parallel: NanoChat adjusts internal model weights to reduce prediction error; AutoResearch adjusts hyperparameters and training configuration to reduce the same metric. Both are feedback-driven optimization loops — differing only in what they adjust.

## Practical Takeaways

- **Consumer gaming hardware is sufficient to complete the NanoChat pipeline end-to-end** — an RTX 4070 with 8GB VRAM can finish pre-training in ~2.5 hours, though SFT at full scale requires more powerful hardware (the full SFT run was estimated at 10 hours on this machine).
- **SFT truncation has severe quality consequences** — skipping or heavily abbreviating the fine-tuning step leaves the model unable to follow conversational format, even if pre-training metrics look reasonable. Don't evaluate chatbot quality on a pre-training checkpoint.
- **The `depth` parameter is the primary hardware-scaling knob** — adjusting the number of transformer layers is how you tune NanoChat to fit your specific GPU's VRAM budget.
- **Using an AI assistant (Claude) to navigate dependency issues** is a practical shortcut — GPU/CUDA dependency configuration varies significantly by hardware, and the creator found Claude helpful for troubleshooting WSL2 environment setup.
- **The logical extension is running AutoResearch on top of a local NanoChat checkpoint** — rather than using default or repo-recommended hyperparameters, AutoResearch agents could search for optimal settings for specific consumer GPU configurations, potentially recovering quality lost to hardware constraints.

## Notable Quotes

> "In 2019, it cost $43,000 to train a GPT-2 model. And right now, what Karpathy and other researchers are doing is they're doing the same result with just $48 using cloud GPUs."

> "With the NanoChat training we did here, it tries to predict the next token. It measures how wrong it was and then adjusts the weights... With AutoResearch, it was trying to make a parameter change, then it measured the val BPB, and then just kept it if it was better... Both are just making a guess, measuring the results, and updating it based on the feedback. The difference is just what gets adjusted."

> "I give real results on this channel. I won't make stuff up."
