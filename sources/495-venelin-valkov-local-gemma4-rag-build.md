---
source_id: "495"
title: "Local Gemma 4 with OpenCode & llama.cpp | Build a Local RAG with LangChain | 🔴 Live"
creator: "Venelin Valkov"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=-_hC-C_Drcw"
date: "2026-04-04"
duration: "75:23"
type: "video"
tags: ["agentic-coding", "context-engineering", "prompt-engineering", "infrastructure"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "06-strategy-and-economics"]
---

# 495: Local Gemma 4 with OpenCode & llama.cpp | Build a Local RAG with LangChain | 🔴 Live

> **Creator**: Venelin Valkov | **Platform**: YouTube | **Date**: 2026-04-04 | **Duration**: 75:23

# Local Gemma 4 with OpenCode & LangChain RAG — Live Build

## Summary

Venelin Valkov livestreams a complete local AI development session, running Google's Gemma 4 27B (26B A4B mixture-of-experts) model via llama.cpp on an Apple M4 with 48GB unified memory. The session tests the model as an AI coding assistant inside OpenCode (an open-source terminal coding agent), while simultaneously building a local RAG application using LangChain, ChromaDB, and Streamlit — all running entirely offline with Ollama serving embeddings and inference for the RAG layer. The session is notable for showing a real-world, unedited workflow including errors, import failures, and debugging loops.

The core technical setup separates concerns deliberately: llama.cpp (served via OpenAI-compatible API) powers OpenCode for the agentic coding assistant, while Ollama handles the RAG application's inference — reserving llama.cpp's faster throughput for the coding agent. The 4-bit quantized Gemma 4 model achieves ~57 tokens/second on M4 hardware, a meaningful improvement over the 8-bit version's ~40 t/s, and the session provides candid hardware reality-checking about the model's actual resource requirements versus Google's "effective parameter" marketing framing.

The RAG build itself follows a standard LangChain architecture: PDF ingestion → markdown conversion → chunking → ChromaDB vector store → retrieval chain → Streamlit chat UI. The session surfaces practical friction points including outdated dependency versions installed by the AI agent, LangChain API migration issues (chains module restructuring), and Python package import path problems — all demonstrating the kinds of real-world debugging loops that occur even with capable local models driving agentic coding workflows.

## Key Concepts

### Gemma 4 Mixture-of-Experts "Effective Parameter" Reality

Google markets Gemma 4 models with "effective" parameter counts (e.g., "2B effective") that are significantly smaller than actual weight counts (~4.5B real parameters for the "2B" model). This matters practically: users must load the full model weights into memory, making these models considerably heavier than their advertised size implies. The 27B model uses ~4B active parameters per forward pass but requires loading the full model. For local deployment, hardware requirements are substantially higher than the effective-size framing suggests.

### llama.cpp as OpenAI-Compatible Local API

Running `llama.cpp` with `--server` mode exposes an OpenAI-compatible REST API at `localhost`. The `opencode.json` configuration file points OpenCode at this endpoint with the exact GGUF filename as the model identifier, a 256K context window specification, and the AI SDK (Versel) as the provider layer. This pattern decouples the model runtime from the coding tool, enabling any OpenAI-compatible client to use local models without code changes.

### Agentic Coding Failure Modes with Outdated Dependencies

A recurring failure pattern emerges: the AI agent installs older library versions (LangChain 0.3 instead of current 1.2+) and then gets confused when expected module paths don't exist (e.g., `langchain.chains` has been restructured in newer versions). The agent then enters debugging loops — checking imports one by one — that consume significant context tokens and slow progress. This illustrates a known risk in agentic coding: agents trained on older code distributions may systematically target outdated APIs.

### Local RAG Architecture: Separation of Inference Concerns

The architecture deliberately separates two inference workloads: the coding assistant (llama.cpp, faster, high context) and the RAG application (Ollama, simpler API). This avoids contention on the same server process and allows different models optimized for different tasks. The RAG stack uses LangChain's `create_retrieval_chain` / `create_stuff_documents_chain` pattern, ChromaDB in-memory vector store, recursive character text splitting, and OllamaEmbeddings — all local, no external API calls.

### Context Window Economics at the Edge

Running the 26B model with a 256K context window on 48GB unified memory is feasible but notable. By contrast, an RTX 4090 (24GB VRAM) user in the chat achieved 100–140 t/s but was limited to ~20K context before CPU offloading became necessary. This illustrates the core local LLM tradeoff: context length scales memory requirements linearly, and the sweet spot between tokens/second, context size, and quantization level is highly hardware-dependent.

## Practical Takeaways

- **Use 4-bit quantization for local coding agents**: The Q4 version of Gemma 4 27B delivers ~57 t/s vs ~40 t/s for Q8 on M4 hardware — a 40%+ throughput gain with acceptable quality for code generation tasks.
- **Pin dependency versions explicitly when using AI coding agents**: Agents frequently install older library versions; specifying `langchain>=0.3,<1.0` or using a lockfile prevents the agent from installing stale versions and then debugging phantom import errors.
- **Separate the coding assistant inference server from the application inference server**: Running llama.cpp for the agent and Ollama for the app prevents resource contention and allows independent optimization of each workload.
- **Configure `opencode.json` with explicit context window limits**: Setting `contextWindow: 262144` in the config helps OpenCode correctly track context usage and avoid silent truncation on long sessions.
- **Treat "effective parameter" counts skeptically for hardware planning**: Always look up the actual stored parameter count and GGUF file size, not the marketing "effective" figure, when estimating VRAM/RAM requirements for local deployment.

## Notable Quotes

> "The effective sizes are something like a mini version of mixture of expert models. So essentially what you need to do is to load the complete model into memory and even though those models say like two billion parameters or four billion parameters, actually the weights are a bit larger."

> "I got 100 to 140 tokens per second but only 20K context... more context would cause CPU offloading."

> "It seems that LangChain chains is not available in the installed LangChain package version in the environment, which is unexpected for such a common module."
