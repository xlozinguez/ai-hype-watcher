---
source_id: "453"
title: "How We Used Observational Memory To Build A Coding Agent"
creator: "Mastra"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=VWsJjyk1lBM"
date: "2026-03-30"
duration: "26:30"
type: "video"
tags: ["context-engineering", "multi-agent", "agentic-coding", "claude-code", "skills", "agent-teams"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "03-claude-code-essentials"]
---

# 453: How We Used Observational Memory To Build A Coding Agent

> **Creator**: Mastra | **Platform**: YouTube | **Date**: 2026-03-30 | **Duration**: 26:30

# How We Used Observational Memory To Build A Coding Agent

## Summary

Mastra (a framework for AI engineering) presents "observational memory," a new approach to agent memory that challenges the dominant retrieval-augmented pattern. The core insight is that traditional memory systems retrieve and re-inject relevant messages on every turn, causing constant prompt cache misses, added latency from vector search and re-ranking, and a fragmented context that never builds a continuous picture of a conversation. Instead of retrieval, observational memory uses background "observer" and "reflector" agents to progressively compress and summarize conversation history in place, resulting in a stable, cacheable context window that grows denser over time rather than being rebuilt each turn.

The team built a coding agent called Monstercode primarily as a testbed for observational memory, and in doing so developed strong opinions about what constitutes a proper "agent harness." Their definition goes well beyond the common "model + tools" framing: a harness is a stateful orchestrator composed of dynamic system prompts assembled at runtime, slash commands for active steering, workspaces (file system + sandbox + tools + skills), cost analysis, and event/streaming infrastructure. The talk draws explicit comparisons to Claude Code's compaction problem as the real-world pain point that motivated both the memory architecture and the harness concept.

A key economic argument underlies the memory design: prompt caching is 8–10x cheaper than uncached prompts. By keeping context stable and append-only rather than rewriting it on every turn, observational memory makes aggressive use of cache hits. The async "buffering mode" means compression never blocks the agent — observations happen in the background without the lull that plagues Claude Code's compaction step.

## Key Concepts

### Observational Memory vs. Retrieval-Augmented Memory

Traditional memory systems embed incoming messages, query a vector database, re-rank results, and inject the top results back into context on every single turn. This pattern has three compounding costs: it invalidates the prompt cache on every message, adds latency from the search/re-rank pipeline, and produces a context that is reconstructed point-in-time rather than continuously maintained. Observational memory replaces this with two background agents — an **observer** (which fires at configurable observation points to compress recent turns into dense summaries) and a **reflector** (which builds higher-level understanding over time). The resulting context accumulates linearly and is structurally stable, making it highly cacheable.

### Lossy Memory as a Feature

The human memory analogy is central: people don't remember tying their shoes, but they do remember that their mom visited. Forcing agents to process all messages equally and hoping the LLM internally prioritizes is equivalent to "sending 100 messages and hoping it figures out which parts matter." Deliberately discarding low-signal information (e.g., collapsing a full flight-search JSON response into "direct flight to NYC, [date], [time], $X") is framed not as a limitation but as a design goal — it prevents the model from being distracted by irrelevant data and mirrors how effective human cognition works.

### Async Buffering Mode

Two operational modes are available: a **blocking mode** where the agent pauses at an observation threshold while compression occurs (analogous to, but smoother than, Claude Code compaction), and an **async buffering mode** where observations accumulate in a buffer and are inserted transparently while the conversation continues uninterrupted. The async mode eliminates the user-visible "thinking/compressing" lull that makes Claude Code compaction frustrating.

### The Agent Harness

A harness is defined as a stateful orchestrator comprising: (1) **dynamic system prompts** assembled at runtime from layered components (environment context, mode prompt, tool documentation, active tasks, CLAUDE.md/agents.md/memory.md files, and dynamically activated skills); (2) **slash commands** for active in-turn steering (distinct from passive system prompt orientation); (3) **workspaces** that wire together a file system, sandbox, tools, and skills for an agent to operate in; and (4) supporting infrastructure like cost analysis and event streaming. The concept of **modes** — putting the agent in distinct behavioral states like "build mode" or "plan mode" — is highlighted as a key differentiator from simple model+tools architectures.

### Skills vs. MCP

Skills are described as markdown files in a directory that get dynamically activated and deactivated based on the agent's current situation. The distinction from MCP is framed memorably: "Skills are to MCP as knowing how to cook is to having a kitchen and the tools." Skills provide procedural knowledge; MCP provides the execution environment and tooling. Both are necessary; they operate at different levels of abstraction.

## Practical Takeaways

- **Don't rebuild context on every turn.** If your memory system re-injects retrieved chunks per query, you're paying full LLM processing costs each turn. Structuring context as a stable, append-only summary that grows denser over time enables aggressive prompt cache reuse (8–10x cost reduction).
- **Treat lossy compression as intentional design.** When summarizing tool call results or conversation history, strip to signal only — dates, amounts, intent — rather than passing raw JSON. Irrelevant data isn't neutral; it distracts the model and consumes context budget.
- **Use async background agents for memory management.** Rather than blocking on compression (Claude Code's compaction problem), run observer/reflector agents asynchronously so the primary agent thread is never stalled waiting for memory operations.
- **Layer system prompts dynamically at runtime.** A static system prompt is insufficient for a capable coding agent. Compose prompts from environment state, mode, tool documentation, active task context, and dynamically loaded skill files — each layer serving a distinct orientation purpose.
- **Evaluate memory systems against prompt cache economics, not just accuracy.** The standard argument for retrieval ("you need less context") ignores the cost of cache invalidation. A larger but stable cached context can be both more accurate and cheaper than a smaller but perpetually-rebuilt retrieval context.

## Notable Quotes

> "Friends don't let friends use compaction — it's never a good sign when it compacts."

> "What if forgetting the non-important things is actually a feature? Why not just forget the non-important things and remember the things that we actually think are important."

> "Skills are to MCP as knowing how to cook is to having a kitchen and the tools. That's the very much the difference."
