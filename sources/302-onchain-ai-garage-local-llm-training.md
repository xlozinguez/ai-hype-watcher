---
source_id: "302"
title: "Build My Own ChatGPT? Testing w/ Karpathy's Nanobot Model Training"
creator: "Onchain AI Garage"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=jZB0VeXlETU"
date: "2026-03-13"
duration: "16:18"
type: "video"
tags: ["ai-economics", "infrastructure", "agentic-coding"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 302: Build My Own ChatGPT? Testing w/ Karpathy's Nanobot Model Training

> **Creator**: Onchain AI Garage | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 16:18

# Build My Own ChatGPT? Testing w/ Karpathy's Nanobot Model Training

## Summary

The creator walks through a hands-on experiment training a miniature GPT-2-style language model from scratch on a consumer gaming laptop (RTX 4070, 8GB VRAM) using Andrej Karpathy's open-source `nanogpt` / NanoChat repository. The pipeline covers the full LLM training lifecycle: downloading a real dataset (Nvidia's ClinVar Mix 400B), training a tokenizer, running pre-training, and then applying supervised fine-tuning (SFT) to produce a working chatbot — all without using any frontier LLM or cloud compute. Training completed in approximately 2 hours 22 minutes, bringing the validation BPB from 3.17 down to 0.94.

The video is a raw, unpolished experiment — the resulting chatbot is incoherent but technically functional as a chat interface. The creator draws an illuminating analogy between NanoChat's weight-update loop and AutoResearch's hyperparameter-search loop, framing both as the same optimization primitive operating at different levels of abstraction. The proposed next step is combining the two: using AutoResearch (via Claude) on top of the trained NanoChat model to tune its training recipe — mirroring what Karpathy himself has been doing.

The broader context is compelling: training a GPT-2-class model cost $43,000 in 2019 and took 168 hours. The same result now runs in under 2 hours on $48 of cloud H100 time, and a rough approximation runs for free on a $2,000 gaming laptop. This cost compression is a concrete data point for AI economics.

## Key Concepts

### NanoChat as a Minimal LLM Training Harness
NanoChat (by Andrej Karpathy) is a single-file, educational implementation of the full LLM pipeline: tokenization, pre-training, supervised fine-tuning, evaluation, and chat UI. A single `depth` parameter (number of transformer layers) controls model scale, making it accessible for experimentation on consumer hardware. It is explicitly designed to be minimal and hackable rather than production-grade.

### The Two-Stage Training Pipeline: Pre-training → SFT
Raw pre-training on a large text corpus teaches the model to predict the next token but produces an incoherent text-completion engine, not a chatbot. Supervised fine-tuning (SFT) on synthetic human/assistant conversation data then reshapes the model's output format into chat turns and instills a basic personality. Skipping or truncating SFT (as the creator had to do due to hardware limits) produces a model that can follow topics but gives rambling, off-target responses.

### Optimization Loops at Different Abstraction Levels
The creator surfaces a useful mental model: both NanoChat training and AutoResearch are the same primitive — make a change, measure the result, keep improvements, repeat. NanoChat adjusts the model's internal weights to minimize next-token prediction loss. AutoResearch adjusts the training recipe itself (hyperparameters, architecture choices) to minimize the same loss. Framing ML training and meta-learning as nested optimization loops clarifies how they can be composed.

### AI Training Cost Compression as a Trend
GPT-2-class training went from $43,000 / 168 hours (2019) to $48 / ~2 hours (2025–26 cloud H100) to effectively $0 on consumer hardware with degraded but real results. This is not an abstraction — the creator ran the experiment. It illustrates the `ai-economics` theme concretely: the cost floor for meaningful ML experimentation has collapsed.

### Consumer GPU Constraints and Practical Tradeoffs
An RTX 4070 with 8GB VRAM can complete pre-training in ~2.5 hours but cannot run the full SFT pipeline in reasonable time (estimated 10 hours vs. Karpathy's 8×H100 setup). The practical workaround is truncating SFT steps, which visibly degrades output quality. This demonstrates where the consumer hardware ceiling sits today and what "free" actually buys you.

## Practical Takeaways

- **You can run the full NanoChat pipeline on a $2,000 gaming laptop** — expect ~2.5 hours for pre-training on 8 shards of ClinVar Mix 400B, and plan for SFT to be the bottleneck if your VRAM is limited.
- **SFT is not optional for usable chat output** — skipping or heavily truncating it produces a model that completes text rather than converses; budget time and VRAM accordingly before starting.
- **WSL2 + matching CUDA/GPU dependencies is the main setup friction** — the creator used an AI coding assistant (Claude) to resolve dependency issues, which is a reasonable first step when GPU driver/library versions conflict.
- **Use `--max_tokens 150` or equivalent inference flags** to prevent the undertrained model from rambling into incoherence; output length control is a cheap quality mitigation.
- **The natural next experiment is AutoResearch on top of NanoChat** — using an AI agent to search the hyperparameter/training-recipe space on your already-trained checkpoint could improve results without full retraining, and is what Karpathy himself is doing.

## Notable Quotes

> "In 2019, it cost $43,000 to train a GPT-2 model. And right now, what Karpathy and other researchers are doing is they're doing the same result with just $48 using cloud GPUs."

> "Both are just making a guess, measuring the results, and updating based on the feedback. The difference is just what gets adjusted. NanoChat adjusts the model's internal weights. AutoResearch was adjusting the training recipe itself."

> "This does not require any LLM to train. This is just training it on its own based on the math and based on judging the data it had."
