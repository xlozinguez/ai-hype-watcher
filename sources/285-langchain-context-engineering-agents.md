---
source_id: "285"
title: "Context Engineering for Agents"
creator: "LangChain"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=4GiqzUHD5AA"
date: "2025-07-02"
duration: "22:06"
type: "video"
tags: ["context-engineering", "multi-agent", "agent-teams", "agentic-coding", "prompt-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 285: Context Engineering for Agents

> **Creator**: LangChain | **Platform**: YouTube | **Date**: 2025-07-02 | **Duration**: 22:06

# Context Engineering for Agents

## Summary

Lance from LangChain provides a structured overview of "context engineering" — the practice of deliberately managing what information enters an LLM's context window at each step of an agent's execution. Drawing on Andrej Karpathy's analogy of the LLM as a CPU and the context window as RAM, the video frames context engineering as the central discipline for building reliable agents, since agents uniquely accumulate large context through long-running tasks and iterative tool calls.

The video organizes context engineering strategies into four categories: **writing** context (persisting information outside the context window for later retrieval), **selecting** context (pulling only relevant information into the window at the right time), **compressing** context (reducing token volume through summarization or trimming), and **isolating** context (splitting context across multiple agents or execution environments). Each category is illustrated with concrete examples from real-world agents including Claude Code, Windsurf, OpenAI Swarm, Anthropic's multi-agent researcher, and Hugging Face's open deep research.

The video also touches on how LangGraph is designed to support all four strategies through its state management primitives, positioning structured agent state as a natural mechanism for context isolation and selective exposure of information to the LLM at each node.

## Key Concepts

### Writing Context: Scratchpads and Persistent Memory
Writing context means saving information *outside* the context window so an agent can retrieve it later. Scratchpads persist working information within a single session (e.g., Anthropic's multi-agent researcher saves its research plan to memory at the start so it survives potential context overflow). Memory systems operate across sessions — products like ChatGPT, Cursor, and Windsurf auto-generate and update memories from past interactions to inform future ones. The implementation varies (files, state objects, external stores), but the principle is the same: write now, recall later.

### Selecting Context: Targeted Retrieval of Instructions, Facts, and Tools
Selection involves pulling only the relevant subset of available context into the window for a given step. This covers procedural memory (rules files like `CLAUDE.md` pulled in at session start), semantic/episodic memory (facts and few-shot examples retrieved via embedding similarity or graph databases), and tools (RAG over tool descriptions to avoid performance degradation beyond ~30 tools). Windsurf's retrieval stack illustrates the complexity: semantic search, file-path search, knowledge graphs, and LLM-based re-ranking are all combined because pure embedding search alone becomes unreliable at scale.

### Compressing Context: Summarization and Trimming
Compression retains only the tokens necessary for the current task. Claude Code's `auto-compact` triggers summarization at 95% context utilization. Anthropic's multi-agent researcher applies narrower summarization only to completed work sections. Cognition uses summarization at agent handoff boundaries to compress context before passing it to sub-agents. Trimming (heuristic or learned) offers a complementary approach — keeping only recent messages or using LLM-based pruning to remove tokens already known to be irrelevant.

### Isolating Context: Multi-Agent and Sandboxed Execution
Isolation splits context across separate execution environments so no single context window bears the full load. Multi-agent architectures (OpenAI Swarm, Anthropic's parallel sub-agents) give each agent its own context window, enabling the overall system to process far more tokens in aggregate. Hugging Face's open deep research demonstrates a complementary technique: a code agent executes tools inside a persistent sandbox, and only selective return values are passed back to the LLM — token-heavy objects like images or audio never enter the context window at all. LangGraph state objects with typed fields serve as another isolation mechanism, letting developers route specific context buckets to specific stages.

### Context Failures as the Core Risk
A referenced blog post by Drew Brun enumerates specific failure modes from uncontrolled context growth: **context poisoning** (hallucinations propagating forward), **distraction** (irrelevant information degrading focus), **curation failures** (missing critical information), and **context clash** (conflicting information causing inconsistent behavior). These failure modes motivate all four engineering strategies and explain why context discipline is especially critical for agents, which are structurally prone to context accumulation.

## Practical Takeaways

- **Use scratchpads for within-session persistence**: When an agent's context might overflow or a plan needs to survive long trajectories, write it to an external file or state object at the start — don't rely on it staying in the window.
- **Apply RAG to tool descriptions, not just knowledge**: With more than ~30 tools, retrieve only the relevant tool descriptions for each step via embedding similarity rather than loading all tools into every prompt.
- **Layer your retrieval stack for knowledge**: Pure embedding search degrades at production scale. Combine it with structural search (file paths, knowledge graphs) and LLM-based re-ranking, as Windsurf does.
- **Compress at natural boundaries**: Apply summarization at session overflow, at completed work sections, or at agent handoff points — not uniformly. Targeted compression preserves more useful signal than blanket truncation.
- **Use typed state objects as context routers**: A structured state model (e.g., Pydantic) with distinct fields for different context types lets you make explicit, reviewable decisions about what each agent node actually sees.

## Notable Quotes

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy (cited)

> "Context engineering is effectively the number one job of engineers building AI agents." — Cognition (cited)

> "The ability to use multi-agent expands the number of tokens that the overall system can process because each agent has its own context window and can independently research a subtopic." — Lance, paraphrasing Anthropic
