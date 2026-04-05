---
source_id: "495"
title: "Local Gemma 4 with OpenCode & llama.cpp | Build a Local RAG with LangChain | 🔴 Live"
creator: "Venelin Valkov"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=-_hC-C_Drcw"
date: "2026-04-04"
duration: "75:23"
type: "video"
tags: ["agentic-coding", "context-engineering", "prompt-engineering", "infrastructure", "ai-landscape"]
curriculum_modules: ["01-foundations", "04-agentic-patterns", "06-strategy-and-economics"]
---

# 495: Local Gemma 4 with OpenCode & llama.cpp | Build a Local RAG with LangChain | 🔴 Live

> **Creator**: Venelin Valkov | **Platform**: YouTube | **Date**: 2026-04-04 | **Duration**: 75:23

# Local Gemma 4 with OpenCode & LangChain RAG — Live Build

## Summary

Venelin Valkov live-streams the process of running Google's Gemma 4 27B (26B active parameters, Mixture of Experts) model entirely locally via llama.cpp on an Apple M4 machine with 48GB unified memory, using it to power OpenCode (an AI coding agent) to build a local RAG application. The session covers practical hardware realities of running large open-source MoE models locally, configuration of the llama.cpp OpenAI-compatible server, and using OpenCode with a custom `opencode.json` config to point the agent at the local model endpoint.

The RAG application being built uses Streamlit, LangChain, ChromaDB, and Ollama (kept separate from the llama.cpp server to reserve GPU resources for the coding agent). The build proceeds largely autonomously through OpenCode, though it encounters predictable issues: outdated library versions being selected, import path errors from LangChain's breaking API changes across versions, and module resolution problems with the project structure. The live debugging session illustrates both the power and the current failure modes of using local models for agentic coding tasks.

A key observation throughout is the performance tradeoff between quantization levels: 4-bit quantization yields ~57 tokens/second vs ~40 tokens/second for 8-bit on the same hardware, at some cost to accuracy. The session also touches on Arena AI leaderboard results showing Gemma 4 27B outperforming larger closed models on open-source benchmarks, and community discussion about context window size constraints when running locally (e.g., 20K context on an RTX 4090 with 24GB VRAM to maintain speed).

## Key Concepts

### Gemma 4 as Mixture of Experts (MoE) and "Effective Size" Confusion
Google markets Gemma 4 using "effective parameter" counts that reflect only the active parameters during inference, not total model weights. The 27B model has ~4B active parameters but requires loading the full weight set into memory. This means the model consumes significantly more VRAM/RAM than the advertised parameter count implies — the "2B effective" variant has ~4.5B real parameters. Users need to calibrate hardware expectations against actual weight sizes, not the marketed effective sizes.

### llama.cpp as OpenAI-Compatible Local Server
Running `llama.cpp` (installed via `brew install --HEAD`) exposes an OpenAI-compatible REST API at `localhost`. This allows any tool expecting an OpenAI endpoint to point at a local model. OpenCode is configured via `opencode.json` in the project root, specifying the `llama-cpp` provider, the base URL, the exact GGUF model filename, and a context window size (set to 256K for the coding agent session). This pattern generalizes to any OpenAI-API-compatible client.

### Quantization Level Tradeoffs for Local Inference
4-bit quantization (Q4) runs at ~57 tokens/second vs ~40 tokens/second for 8-bit (Q8) on the same M4 hardware. Higher quantization = faster inference at the cost of potential accuracy degradation. Context window size is also a lever: smaller context windows allow higher tokens/second and avoid CPU offloading on memory-constrained machines (e.g., 20K context enables 100–140 t/s on an RTX 4090 with 24GB VRAM, while larger contexts force offloading).

### Agentic Coding with Local Models: Capability and Failure Modes
OpenCode autonomously scaffolds a multi-file Python project (PDF processor, vector store manager, RAG engine, Streamlit UI) from a single natural language prompt. It demonstrates useful autonomous behaviors: running `uv sync`, creating directory structures, iteratively fixing import errors. However, failure modes are visible: it selects outdated library versions (LangChain 0.3 instead of 1.2+), struggles with LangChain's breaking API changes (e.g., `create_retrieval_chain` import paths), and hits context window limits during extended debugging. Local 26B models are capable but noticeably less robust than frontier models for agentic coding tasks.

### Separating Inference Workloads: llama.cpp for Agent, Ollama for RAG App
The demo deliberately uses two separate local inference backends: llama.cpp serves the OpenCode coding agent (Gemma 4), while the RAG application itself uses Ollama with a different model. This architectural separation ensures the agent's inference server isn't resource-contended by the application under development — a practical pattern when local hardware is the constraint.

## Practical Takeaways

- **Check actual weight sizes, not effective parameter counts**: Before attempting to run a Gemma 4 model locally, look up the GGUF file size on HuggingFace rather than trusting advertised parameter counts — MoE "effective size" marketing understates real memory requirements.
- **Use `opencode.json` with a local llama.cpp server** to wire OpenCode (or any OpenAI-API-compatible agent) to a locally running model; set the context window in config to match your actual hardware budget.
- **Start with 4-bit quantization for speed**: For interactive agentic coding workflows where latency matters, Q4 provides meaningfully faster token generation; reserve Q8 for tasks where output quality is the priority.
- **Pin library versions explicitly when using AI agents to scaffold projects**: Agentic coders tend to select older, well-represented library versions from training data; manually specify current versions in your project configuration (pyproject.toml, requirements.txt) before prompting the agent to build.
- **Monitor context consumption during long agentic sessions**: Extended debugging loops in OpenCode (or similar tools) can exhaust the context window, causing the model to lose track of earlier decisions. Break complex builds into smaller, scoped prompts to stay within effective context limits.

## Notable Quotes

> "Those effective sizes are something like a mini version of mixture of expert models. So essentially what you need to do is to load the complete model into memory and even though those models say like two billion parameters or four billion parameters, actually the weights are a bit larger."

> "I recall that yesterday we got only about 40 tokens per second on the 8-bit quantization and now with this 4-bit quantization we're getting roughly 57 tokens per second. So this is quite a bit faster."

> "I'm going to be using Ollama since I want to reserve the llama.cpp server just for OpenCode."
