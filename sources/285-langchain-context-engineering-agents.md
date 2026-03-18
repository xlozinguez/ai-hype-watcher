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

Lance from LangChain introduces "context engineering" as an umbrella discipline for managing what information flows into an LLM's context window at each step of an agent's trajectory. Drawing on definitions from Andrej Karpathy and Toby Lütke (Shopify), the video frames the context window as analogous to RAM in an operating system — a limited working memory that must be carefully curated. For agents specifically, this challenge is amplified because long-running tasks and tool call feedback cause context to balloon across many turns, creating failure modes like context poisoning, distraction, and conflicting information.

The core of the video organizes context engineering strategies into four categories: **writing** context (saving information outside the context window for later retrieval), **selecting** context (pulling the right information in at the right time), **compressing** context (trimming or summarizing to reduce token bloat), and **isolating** context (splitting context across agents or sandboxes). Each category is illustrated with concrete examples from production agents like Claude Code, Cursor/Windsurf, Anthropic's multi-agent researcher, Cognition's Devin, and Hugging Face's open-deep-research.

The video concludes by noting that LangGraph is specifically designed to support all four strategies — through its state object model, memory APIs, and multi-agent primitives — positioning context engineering as the central discipline for any engineer building serious agentic systems.

---

## Key Concepts

### Writing Context: Scratchpads and Memory
Agents can persist information *outside* the context window to avoid token overflow while retaining critical state. **Scratchpads** store information within a single session (e.g., Anthropic's multi-agent researcher saves its research plan to a file so it survives a 200K-token overflow). **Memories** persist across sessions — tools like ChatGPT, Cursor, and Windsurf auto-generate memories from past interactions. The key distinction: scratchpads are ephemeral task aids; memories are long-term agent knowledge that accumulates over time.

### Selecting Context: Retrieval-Driven Injection
Not all available context should be in the window simultaneously. Selection strategies include embedding-based similarity search for facts and memories, RAG over tool descriptions (research shows agent performance degrades sharply past ~30 tools and fails at ~100), and rules/instruction files like `CLAUDE.md` loaded at session start. Windsurf's approach exemplifies production-grade selection: semantic code chunking, graph databases, BM25 file search, and LLM-based re-ranking layered on top of embeddings — illustrating that knowledge selection at scale is highly non-trivial.

### Compressing Context: Summarization and Trimming
When context grows too large, compressing it retains only the tokens necessary for the next decision. Claude Code auto-triggers summarization at 95% context utilization. More surgical approaches include summarizing only completed work sections (Anthropic's researcher) or summarizing at agent handoff boundaries (Cognition's approach). Trimming via heuristics (keep only recent messages) or learned LLM-based pruning offers an alternative to summarization when specific tokens can be identified as no longer relevant.

### Isolating Context: Multi-Agent and Sandboxes
Context isolation splits processing across separate context windows or execution environments. Multi-agent architectures (OpenAI Swarm, Anthropic's parallel sub-agents) give each agent its own context window, expanding total system token throughput without overloading any single window. Code agent sandboxes (as in Hugging Face's open-deep-research) execute tools in a persistent environment, storing heavy outputs like images and audio there and passing back only lightweight return values to the LLM — preventing token-heavy objects from ever entering the context window.

### Context Failures as First-Order Risks
The video references Drew Brun's taxonomy of context failures — poisoning, distraction, curation failure, and clash — as concrete risks that grow nonlinearly with context length. These aren't abstract concerns: conflicting information across a long trajectory can corrupt agent decisions, and injected hallucinations early in context can persistently distort downstream reasoning. This frames context engineering not as optimization but as risk management.

---

## Practical Takeaways

- **Use scratchpads for in-session state persistence**: When an agent's task might exceed context limits, have it explicitly write its plan or intermediate findings to a retrievable location (file, state object) rather than relying on the context window to hold everything.
- **Implement RAG over tools, not just knowledge**: If your agent has more than ~30 tools, embed tool descriptions and retrieve only the relevant subset per task — performance degrades significantly with large tool sets loaded wholesale.
- **Layer retrieval strategies for production knowledge selection**: Pure embedding similarity is insufficient at scale; combine it with keyword search, knowledge graphs, and LLM-based re-ranking for reliable retrieval in code or document-heavy contexts.
- **Apply summarization at natural boundaries**: Rather than summarizing the entire context at once, summarize completed sections, finished sub-tasks, or at agent handoff points to preserve the most actionable recent context while compressing historical detail.
- **Design state objects as context partitions**: Use typed state models (e.g., Pydantic) with distinct fields as named buckets for different context types — this makes it explicit what gets passed to the LLM at each step and prevents accidental context bloat.

---

## Notable Quotes

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy (as cited)

> "Context engineering is effectively the number one job of engineers building AI agents." — Cognition (as cited)

> "The ability to use multi-agent expands the number of tokens that the overall system can process because each agent has its own context window and can independently research a subtopic." — Lance, summarizing Anthropic's multi-agent researcher findings

---
