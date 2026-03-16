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
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "03-claude-code-essentials"]
---

# 285: Context Engineering for Agents

> **Creator**: LangChain | **Platform**: YouTube | **Date**: 2025-07-02 | **Duration**: 22:06

# Context Engineering for Agents

## Summary

Lance from LangChain introduces "context engineering" as an umbrella framework for managing what information flows into an LLM's context window at each step of an agent's trajectory. Drawing on definitions from Andrej Karpathy and Toby from Shopify, the video frames context engineering using an OS analogy: just as an operating system curates what fits in RAM, context engineering is the discipline of deciding what needs to fit in the limited working memory of an LLM. This becomes especially critical for agents because they face larger context utilization from long-running tasks and accumulated tool-call feedback.

The video distills context engineering into four practical strategies: **writing** (saving information outside the context window for later retrieval), **selecting** (pulling the right context in at the right time), **compressing** (retaining only the most relevant tokens), and **isolating** (splitting context across separate agents or state objects). Each strategy is illustrated with real examples from production agents including Claude Code, Windsurf, Anthropic's multi-agent researcher, OpenAI's Swarm, and Hugging Face's open-deep-research.

The core argument is that context engineering—not prompt engineering alone—is the primary engineering discipline when building capable agents. Context failures (poisoning, distraction, conflicting information, hallucination injection) increase with context length, making deliberate context management the difference between agents that work and agents that degrade unpredictably at scale.

---

## Key Concepts

### Writing Context: Scratchpads and Memories
Agents can persist information outside the context window in two ways. **Scratchpads** store working notes relevant only to the current session—Anthropic's multi-agent researcher saves its research plan to memory early so the plan survives even if the 200K token context limit is reached. **Memories** persist across sessions, enabling agents to learn from past interactions. Cursor, Windsurf, and ChatGPT all auto-generate memories from user-agent interactions. The distinction matters for architecture: scratchpads are ephemeral per-task state, memories are durable cross-session knowledge.

### Selecting Context: RAG, Tools, and Memory Types
Selection is the art of pulling the right information into the window at the right moment. This covers semantic memory (facts retrieved via embedding similarity or graph databases), episodic memory (few-shot examples), and procedural memory (instructions/rules files like `CLAUDE.md`). Tool selection is a non-obvious subtlety: research shows agent performance degrades after ~30 tools and collapses at ~100, making RAG over tool descriptions—embedding tool descriptions and retrieving by semantic similarity—an important technique. Knowledge retrieval at the scale of code agents (Windsurf) requires chunking along semantic code boundaries, combining embedding search with BM25/grep-style file search, knowledge graphs, and LLM-based re-ranking.

### Compressing Context: Summarization and Trimming
When context grows too large, summarization reduces token bloat while preserving meaning. Claude Code auto-compacts at 95% of the 200K context window. Summarization can be applied broadly (full session) or narrowly (only completed work sections, or at agent-to-subagent handoff boundaries as Cognition describes). Trimming is a complementary approach: heuristic removal of older messages, or learned LLM-based context pruning to selectively drop tokens known to be irrelevant.

### Isolating Context: Multi-Agent and State Objects
Context isolation splits the problem so no single context window bears the full load. Multi-agent architectures (OpenAI Swarm, Anthropic's parallel sub-agents) give each agent its own context window, enabling the overall system to process more total tokens than any single agent could. Code agents like Hugging Face's open-deep-research isolate token-heavy objects (images, audio, intermediate tool outputs) inside a persistent sandbox that maintains state across turns—only passing back to the LLM the lightweight return values it actually needs. Runtime state objects (e.g., Pydantic models in LangGraph) provide another isolation mechanism: typed fields act as named buckets, letting developers precisely control which context is surfaced to the LLM at each stage.

### Context Failures as the Root Cause of Agent Degradation
Drew Brun's taxonomy of context failures—poisoning, distraction, curation failures, and context clash—explains why naive context accumulation breaks agents. As tool-call feedback and multi-turn history pile up, the probability of conflicting information, injected hallucinations influencing downstream decisions, and the model losing track of the task all increase. This makes context engineering proactive rather than reactive: the goal is to prevent these failure modes by design, not debug them after the fact.

---

## Practical Takeaways

- **Use scratchpads for long-running tasks.** If your agent's session could hit context limits, have it write its plan or key intermediate findings to an external store (file, state object, database) early. This ensures continuity even when the context must be compacted or restarted.

- **Apply RAG to tools, not just knowledge.** If your agent has more than ~30 tools available, embed tool descriptions and retrieve only the relevant subset per task. This is a low-effort intervention with large performance impact.

- **Compress at natural boundaries.** Don't wait until context is full to summarize—apply compression at logical seams (completed subtasks, agent handoffs, section completions) to prevent token bloat from accumulating in the first place.

- **Design state objects as explicit context buckets.** In LangGraph or similar frameworks, model your agent state with typed fields that represent distinct kinds of context (scratchpad, memories, tool results, instructions). Decide explicitly what each LLM call receives rather than dumping the full state.

- **Treat multi-agent as a context scaling strategy, not just a complexity tool.** Running parallel sub-agents isn't only about specialization—it multiplies total token processing capacity, enabling richer outputs from research or analysis tasks than a single-agent architecture could produce.

---

## Notable Quotes

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy (cited)

> "Context engineering is effectively the number one job of engineers building AI agents." — Cognition (cited)

> "The ability to use multi-agent expands the number of tokens that the overall system can process because each agent has its own context window and can independently research a subtopic." — Lance (paraphrasing Anthropic multi-agent researcher post)

---
