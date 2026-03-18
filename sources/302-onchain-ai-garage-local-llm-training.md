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

## Summary

The creator attempts to train a miniature GPT-2-class language model from scratch using Andrej Karpathy's open-source NanoChat repository, running entirely on a local gaming laptop (RTX 4070, 8GB VRAM). The experiment demonstrates the full LLM training pipeline — tokenization, pre-training on NVIDIA's ClinicalMix 400B dataset, and supervised fine-tuning (SFT) — without using any frontier model or cloud GPU, completing pre-training in approximately 2 hours 22 minutes.

The video serves as a practical cost-comparison benchmark: training GPT-2 cost $43,000 in 2019, researchers like Karpathy now achieve equivalent results for ~$48 on cloud H100s, and this experiment pushes toward $0 on consumer hardware. The pre-training run reduced validation BPB (bits per byte) from 3.17 to 0.94, short of the ~0.74 target for GPT-2-level capability, attributable to the constrained hardware. The SFT step was heavily truncated (from ~10 hours to ~1 hour) due to the same GPU limitations, resulting in a chatbot that is thematically coherent but semantically incoherent.

The creator draws an insightful conceptual parallel between NanoChat's training loop (adjust model weights → measure prediction error → repeat) and AutoResearch's optimization loop (adjust training hyperparameters → measure validation BPB → keep improvements → repeat), framing both as feedback-driven optimization systems differing only in *what* gets adjusted. The proposed next step is using AutoResearch on top of the trained NanoChat model to automatically tune hyperparameters — mirroring Karpathy's own recent workflow.

---

## Key Concepts

### NanoChat as a Minimal LLM Training Harness
NanoChat is Karpathy's open-source framework for training a GPT from scratch on a single GPU node. It covers the full pipeline: tokenization, pre-training, SFT, evaluation, inference, and a chat UI. A single parameter — `depth` (number of transformer layers) — controls model scale, making it accessible and hackable. It requires no frontier model API; all computation is local math on GPU weights.

### The Cost Collapse of GPT-2 Training
Training GPT-2 cost ~$43,000 and 168 hours in 2019. Karpathy's current runs achieve equivalent results in under 2 hours on a single H100 for ~$48. This video pushes further: consumer hardware (RTX 4070) replicates the pipeline for effectively $0 in cloud costs, though with degraded results due to VRAM and compute constraints. This illustrates the broader trend of AI compute economics collapsing over time.

### Pre-training vs. Supervised Fine-Tuning (SFT)
Pre-training teaches the model to predict the next token across massive text corpora — it produces a text completer, not a chatbot. SFT loads the pre-trained checkpoint and fine-tunes on structured human/assistant conversation data (in this case, Karpathy's `identity_conversations.jsonl`), teaching the model to respond in a chat format with a defined personality. Skipping or truncating SFT results in thematically related but conversationally incoherent outputs.

### Bits Per Byte (BPB) as a Training Metric
BPB (bits per byte) is the validation metric used to track training progress. Lower values indicate better next-token prediction. The experiment started at 3.17 BPB, reached 0.94 after full pre-training, versus the ~0.74 target for GPT-2-class capability. BPB provides a hardware-agnostic, comparable benchmark across different training runs and setups.

### Optimization Loops as a Unifying Framework
Both NanoChat training and AutoResearch are framed as the same fundamental pattern: make a change, measure the result, keep improvements, repeat. NanoChat adjusts *model weights* based on prediction error across training tokens. AutoResearch (as covered in the creator's prior videos) adjusts *training hyperparameters* based on validation BPB. This abstraction helps practitioners understand AI optimization methods as variations on a single feedback loop, not fundamentally different techniques.

---

## Practical Takeaways

- **Consumer gaming GPUs (RTX 4070, 8GB VRAM) can run the full NanoChat pipeline**, but expect degraded results versus cloud H100s — plan for truncated SFT and lower final BPB. Budget 2–3 hours for pre-training and potentially 10+ hours for full SFT.
- **WSL2 is required on Windows** for NanoChat; GPU dependency setup is non-trivial and hardware-specific. Using an AI assistant (the creator used Claude) to navigate dependency issues significantly reduces friction.
- **Truncating SFT has severe quality consequences**: the difference between a text completer and a functional (if incoherent) chatbot is the SFT step. Even a heavily shortened SFT run is better than none for chat-format output.
- **AutoResearch layered on top of NanoChat** is Karpathy's current workflow for hyperparameter optimization — using AI agents to tune the training recipe on top of the trained base model is the natural next step for hobbyists wanting to push past default parameters.
- **BPB is a useful cross-run benchmark**: tracking starting and ending BPB gives a comparable, hardware-agnostic signal of training effectiveness and lets you contextualize local results against published research benchmarks.

---

## Notable Quotes

> "In 2019, it cost $43,000 to train a GPT-2 model. And right now, what Karpathy and other researchers are doing is they're doing the same result with just $48 using cloud GPUs."

> "NanoChat adjusts the model's internal weights. AutoResearch was adjusting the training recipe itself. So slightly different but pretty similar in concept."

> "This does not require any LLM to train. This is just training it on its own based on the math and based on judging the data it had."

---
