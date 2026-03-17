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

Lance from LangChain introduces "context engineering" as the discipline of filling an agent's context window with precisely the right information at each step of its trajectory. Drawing on definitions from Andrej Karpathy and Toby from Shopify, the video frames context as analogous to RAM in an operating system — finite working memory that must be actively curated. The core argument is that context engineering is the number one job of engineers building AI agents, because agents face compounding context challenges: long-running tasks and tool-call feedback loops cause context to accumulate in ways that lead to concrete failure modes (poisoning, distraction, curation conflicts, and context clash).

The video organizes all context engineering strategies into four categories: **writing** (saving information outside the context window for later retrieval), **selecting** (pulling the right context in at the right time), **compressing** (summarizing or trimming to reduce token bloat), and **isolating** (splitting context across agents or runtime state objects to avoid overload). Each strategy is illustrated with concrete examples from production agents: Anthropic's multi-agent researcher, Claude Code's auto-compact feature, OpenAI's Swarm, Hugging Face's open deep research code agent, and Windsurf/Cursor's memory systems.

The video closes by positioning LangGraph as a framework designed to support all four strategies natively — persistent state objects, memory stores, and graph-based agent architectures that enable context isolation across subagents. The practical message is that building reliable agents is inseparable from deliberate context management at every stage of the agent loop.

## Key Concepts

### The Four Context Engineering Strategies
The video's central framework groups all context management approaches into four bins: (1) **Writing** — persisting information to scratch pads or cross-session memory stores while the agent works; (2) **Selecting** — retrieving relevant instructions, facts, few-shot examples, tools, or knowledge into the window at the right moment; (3) **Compressing** — using summarization or heuristic/learned trimming to keep token count manageable; (4) **Isolating** — splitting context across multiple agents or runtime state fields so no single context window becomes overloaded. These categories are mutually reinforcing and most production agents use all four simultaneously.

### Scratch Pads vs. Cross-Session Memory
Scratch pads persist information *within* a single agent session — Anthropic's multi-agent researcher saves its research plan to a file so it survives context window limits during a single run. Cross-session memories (as seen in ChatGPT, Cursor, and Windsurf) persist *across* sessions by synthesizing and storing learnings from past interactions. Both are forms of "writing context," but they differ in scope and retrieval patterns. The distinction matters architecturally: scratch pads are ephemeral task state; memories are durable user/project knowledge.

### Selective Tool and Knowledge Retrieval
Agents degrade significantly with large tool sets — referenced research shows performance drops after ~30 tools and near-complete failure at ~100. The solution is RAG over tool descriptions: embed tool metadata and retrieve only relevant tools for the current task. The same principle applies to knowledge bases: Windsurf's CEO describes a layered retrieval stack combining semantic embeddings, code-boundary-aware chunking, GPT file search, knowledge graphs, and LLM-based re-ranking — illustrating that production-grade knowledge selection is highly non-trivial.

### Summarization as Context Compression
Summarization is the primary compression technique across production agents. Claude Code triggers auto-compact at 95% context utilization, summarizing the entire session history. Anthropic's multi-agent researcher applies summarization more surgically — only to completed work sections. Cognition uses summarization at subagent handoff boundaries, compressing the parent agent's context before passing it downstream. The common principle: summarization controls token bloat while preserving task-relevant signal.

### Context Isolation via Multi-Agent and Runtime State
Multi-agent architectures are fundamentally a context isolation strategy: each subagent has its own context window, enabling the overall system to process far more tokens in parallel than any single agent could. Hugging Face's code agent extends this by executing tool calls in a persistent sandbox that houses token-heavy objects (images, audio) and returns only selective outputs to the LLM. Runtime state objects (e.g., Pydantic models in LangGraph) provide a complementary isolation mechanism — different fields act as named buckets that can be selectively surfaced to the LLM at appropriate pipeline stages.

## Practical Takeaways

- **Design your agent's memory architecture before you design its tools.** Decide upfront which information lives in scratch pads (session-scoped), cross-session memory stores, or RAG indices — and build retrieval into the agent loop rather than dumping everything into the system prompt.
- **Use summarization proactively, not just reactively.** Don't wait for context limits; apply summarization at natural task boundaries (completed subtasks, subagent handoffs) to prevent token bloat from compounding across long trajectories.
- **RAG your tool descriptions if you have more than ~30 tools.** Embedding tool metadata and retrieving only relevant tools for the current task is a well-evidenced technique for maintaining agent reliability at scale.
- **Treat multi-agent decomposition as a context budget strategy, not just a parallelism strategy.** Splitting work across subagents isn't just faster — it lets the system process more total tokens than any single context window allows, enabling richer outputs.
- **Use typed runtime state objects (e.g., Pydantic models) to explicitly control what enters the LLM context at each step.** Named state fields enforce context discipline architecturally rather than relying on prompt instructions to ignore irrelevant information.

## Notable Quotes

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy (quoted by Lance)

> "Context engineering is effectively the number one job of engineers building AI agents." — Cognition (quoted by Lance)

> "The ability to use multi-agent expands the number of tokens that the overall system can process because each agent has its own context window and can independently research a subtopic — and that allows for richer generation of reports because the system was able to process more tokens across these various subagents." — Lance summarizing Anthropic's multi-agent researcher post
