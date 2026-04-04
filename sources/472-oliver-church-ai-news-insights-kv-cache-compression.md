---
source_id: "472"
title: "Day-1 TurboQuant in llama.cpp: 6X Smaller KV Cache After Reading the Actual Paper"
creator: "Oliver Church - AI News & Insights"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=TsSTgMBjHWc"
date: "2026-04-01"
duration: "12:25"
type: "video"
tags: ["infrastructure", "ai-landscape", "context-engineering"]
curriculum_modules: ["06-strategy-and-economics", "01-foundations"]
---

# 472: Day-1 TurboQuant in llama.cpp: 6X Smaller KV Cache After Reading the Actual Paper

> **Creator**: Oliver Church - AI News & Insights | **Platform**: YouTube | **Date**: 2026-04-01 | **Duration**: 12:25

## Summary

Oliver Church documents a day-one engineering effort to implement TurboQuant — a KV cache compression algorithm from Google's ICLR 2026 paper — inside llama.cpp, achieving a 4.57× reduction in KV cache memory. The core problem: running a 70B model at 72K context on dual consumer 3090 GPUs is physically impossible without compression, since the KV cache alone would require 23 GB of VRAM that simply doesn't exist after loading the model weights. Church traces the full implementation arc from a broken community prototype through three distinct engineering phases, fixing bugs, upgrading quantization precision, and ultimately re-enabling flash attention to make long context computationally tractable.

The key algorithmic insight from the TurboQuant paper is to normalize KV vectors to unit length, apply a Walsh-Hadamard Transform (WHT) to produce approximately Gaussian-distributed values across all dimensions, then quantize to 3 bits using a single set of 8 Lloyd-Max centroids — no calibration data required. The result is 3.5 bits per value versus the baseline 16, a 4.57× compression ratio. Church's breakthrough in Phase 3 was recognizing that dequantizing K before flash attention makes the query-side WHT unnecessary, collapsing what had been an architectural conflict into a simple on-the-fly dequantization step. This re-enables flash attention's tiled computation, keeping attention memory effectively constant regardless of context length.

The final benchmark numbers are concrete and sobering in both directions: perplexity on Wikitext-2 rises 7.6% versus the float16 baseline (comparable to weight quantization's own degradation), generation speed drops to 5.1 tokens per second at 72K context, but the critical metric — whether it runs at all — flips from impossible to achievable on sub-$2,000 hardware. Church explicitly credits the TurboQuant authors, a community developer (unix-cydev) for the initial llama.cpp scaffolding, and documents his own specific contributions: the normalization bug fix, the 3-bit upgrade, V-cache compression, and the flash-attention re-enablement insight.

---

## Key Concepts

### KV Cache as the True Context Bottleneck
Token-per-second speed is a comfort metric; context length is the capability ceiling. In a 70B model with 80 layers, 8 KV heads, and 128 dimensions, every token costs ~0.31 MB in the KV cache. At 72K context, that's 23 GB — physically more VRAM than is available after loading the quantized model. This makes KV cache compression a prerequisite for long-context local inference, not an optimization.

### Walsh-Hadamard Transform for Uniform Quantization
TurboQuant's elegance comes from a two-step normalization: first save the vector's L2 norm separately, then apply the WHT to spread information uniformly across all dimensions. The WHT produces approximately Gaussian-distributed coordinates, allowing a *single* optimal quantizer (8 Lloyd-Max centroids) to work for every vector without per-channel calibration. This is why the algorithm requires no training data and generalizes across model architectures.

### The Flash Attention Conflict and Its Resolution
K-cache compression and V-cache compression initially had contradictory flash attention requirements: K needed flash attention *off* (the flash kernel can't apply the query-side WHT), while quantized V needed flash attention *on* (only the flash kernel reads quantized V directly). Church's Phase 3 insight resolves this entirely — dequantizing K before passing it to flash attention makes the query-side WHT unnecessary. The cache stays compressed in VRAM; dequantization happens on-the-fly; flash attention's tiled computation then handles arbitrarily long contexts with near-constant memory overhead.

### V-Cache Transposition Problem in GGML
GGML stores the V-cache transposed for matrix operation efficiency. Block quantization formats like TurboQuant require groups of 32 contiguous elements, but transposed storage writes one element at a time — causing alignment assertion failures in CUDA kernels. The fix is to store V non-transposed when quantized, then explicitly transpose *after* dequantization in the computation graph, a non-obvious change to a deep assumption in the backend's memory layout.

### Quality-Cost Trade-offs at the System Level
The 7.6% perplexity increase from full K+V TurboQuant compression is roughly comparable to what 4-bit weight quantization itself contributes (2–7%). This frames KV cache quantization as a peer trade-off alongside weight quantization, not a catastrophic loss. The V-only compression adds ~1% beyond K-only, suggesting most degradation comes from the quantization math rather than V-specific factors.

---

## Practical Takeaways

- **Context length unlocks qualitatively new use cases.** An agent that can reason over an entire codebase is categorically different from a chatbot — TPS benchmarks don't capture this distinction, but VRAM constraints make it absolute.
- **N² attention memory is a second bottleneck.** Even with KV cache fully compressed, the attention score matrix scales quadratically with context. Without flash attention's tiled computation, 20K context explodes to 16 GB of compute buffers — re-enabling flash attention was as important as the compression itself.
- **CPU/GPU pipeline parallelism creates hidden backend constraints.** Multi-GPU setups route some layers through CPU host memory; llama.cpp's CPU backend only dequantizes to float32, not float16. Intermediate representations must match the lowest-common-denominator backend capability.
- **Single-constant bugs can invalidate entire algorithms.** The difference between the original broken implementation and a working one was `1/32` vs `1/√32` in the normalization step — a trivially small change with total functional impact.
- **Fused WHT + flash attention kernel is the clear next optimization target.** The current approach dequantizes before flash attention, recovering correctness but leaving performance on the table. An in-kernel WHT would close the ~7% speed gap versus baseline.

---

## Notable Quotes

> "Everyone in the local LLM community obsesses over tokens per second. But here's what actually matters: context length. TPS is a comfort metric. Context length is the capability ceiling."

> "I compressed the KV cache by 4.57 times and the context length barely improved... The KV cache was tiny thanks to compression, but the attention map was eating up all the VRAM."

> "This isn't a marginal improvement. This is a capability shift that didn't exist before on this hardware class."

---
