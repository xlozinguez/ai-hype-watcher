---
source_id: "011"
title: "Prompt Engineering is dead."
creator: "Confluent Developer (Tim Berglund)"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Cs7QiSi8KLY"
date: "2026-02-10"
duration: "17:15"
type: "video"
tags: ["context-engineering", "prompt-engineering", "agentic-coding", "mcp"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 011: Prompt Engineering is dead.

> **Creator**: Confluent Developer (Tim Berglund) | **Platform**: YouTube | **Date**: 2026-02-10 | **Duration**: 17:15

## Summary

Tim Berglund returns to the Confluent Developer lightboard to argue that prompt engineering — the art of crafting the perfect instruction to an LLM — is being superseded by **context engineering**, a broader discipline concerned with managing everything that goes into an LLM's context window. The shift matters because agentic applications aren't single-prompt interactions anymore; they're iterative, tool-calling, resource-retrieving workflows that accumulate context over time. A million-token context window sounds large until you account for system prompts, tool descriptions, resources, conversation history, and tool call records all competing for the same space.

The video provides a clear schema for understanding the six components that occupy a context window, then offers four practical tools for managing them: system prompt engineering, precise tool descriptions, intelligent data retrieval (moving beyond naive RAG toward MCP-based resource discovery), and long-horizon strategies like compaction, memory, and agent decomposition. The framing is practical and aimed at engineers building production agentic systems, not chatbot users tweaking prompts.

## Key Concepts

### The Stateless Box

Berglund starts from first principles: an LLM is a stateless function that takes tokens in and produces likely tokens out. It doesn't remember anything between calls. Everything it needs to know must fit in the context window — roughly 60,000 to 700,000 words depending on the model. For agentic applications that make iterative LLM calls and use tools, this constraint becomes the central engineering challenge.

### The Six Components of Context

Every LLM call contains up to six types of content competing for context window space:

1. **User message** — The initial input (human prompt or agent instruction)
2. **System prompt** — Personality, guardrails, and behavioral instructions (always present, set once)
3. **Tools** — Descriptions and schemas of available tools the agent can call
4. **Resources** — Business-specific data the LLM was never trained on (internal docs, tickets, user records)
5. **Assistant messages** — History of the LLM's previous responses (grows with iteration)
6. **Tool calls and responses** — Record of intermediate tool invocations and their results (grows with iteration)

The critical insight: items 1-4 are relatively static, but items 5-6 **grow as the agent runs**, eventually consuming the entire window. This is why long-running agents degrade — it's not the model getting "tired," it's the context window filling up with history.

### The Goldilocks Problem in System Prompts

System prompts need to hit a sweet spot between too vague ("do a good job") and too prescriptive (encoding if-then logic). The right approach: define **outcomes and broad approaches**, and let the LLM figure out the implementation details. If you find yourself writing conditional logic in a system prompt, you're doing the LLM's job for it.

### Beyond RAG: Intelligent Resource Retrieval

RAG (Retrieval Augmented Generation) — stuffing related documents from a vector database into the context — was the first-generation approach to giving LLMs business-specific knowledge. It works for information-search chatbots, but it's not precise enough for production agents.

The next step is **MCP (Model Context Protocol)**, which exposes queryable resources with text descriptions and parameter schemas. Instead of dumping everything that might be relevant into context, you:
1. Include resource descriptions (not full content) in one LLM call
2. Let the LLM decide which resources it actually needs
3. Retrieve only those resources for the next call
4. Use economical representations (e.g., pass a user ID instead of a full user record, with a tool available to fetch the full record if needed)

This is fundamentally about **precision over volume** — putting exactly what's needed in context rather than everything that might be relevant.

### Long-Horizon Strategies

For agents that iterate extensively, three strategies prevent context window exhaustion:

- **Compaction**: Use an LLM call to summarize large resources or conversation history into condensed versions. LLMs are excellent at summarization — a 50,000-token document can often be compressed to 500 words without losing decision-relevant information.

- **Memory**: A key-value store local to the agent where intermediate results, structured data, or lengthy outputs can be parked and retrieved on demand rather than persisted in the context window across every call.

- **Agent decomposition**: Split complex agents into composed sub-agents. If your agent has a complex document-search workflow, that's its own agent. The parent agent can ask the sub-agent for a concise summary rather than carrying the full search context. This mirrors microservice decomposition — agents naturally evolve from monoliths to composed systems.

### The 60-70% Rule

Research consistently shows that filling a context window to 100% capacity doesn't give the best results. Performance peaks at roughly 60-70% of the window's capacity. This means effective context engineering isn't just about fitting everything in — it's about being selective enough to leave headroom.

## Practical Takeaways

- **Context engineering > prompt engineering**: The system prompt is one of six context components, and not always the most impactful one. Engineer the entire context, not just the prompt.
- **Budget your context window**: Map out how much space each component takes and monitor growth over agent iterations. The 60-70% utilization target means your actual budget is smaller than the stated window size.
- **Tool descriptions matter as much as the tools themselves**: Specific, schema-complete tool descriptions let the LLM make good decisions about when and how to use tools.
- **Move from RAG to MCP-style resource discovery**: Instead of vector-search everything, describe available resources and let the LLM request what it needs.
- **Use compaction aggressively**: Summarize large resources and conversation history before they consume the window.
- **Plan for agent decomposition early**: If a sub-workflow is complex enough to need its own iterative reasoning, it should be its own agent.
- **Pass references, not full objects**: Use IDs and descriptions where possible, with tools available to fetch full records on demand.

## Notable Quotes

> "Prompt engineering was always a little bit ridiculous, but context is king." — Tim Berglund

> "More isn't always better. Somewhere in the 60 to 70% of the capacity of the context window is probably where you get your best results." — Tim Berglund

> "Context engineering is the present and future of agentic AI development." — Tim Berglund

## Related Sources

- [#001: Claude Code Task System](001-indydevdan-claude-code-task-system.md) — IndyDevDan's Core Four framework (Context, Model, Prompt, Tools) aligns directly with Berglund's context schema
- [#005: Vibe Coding Readiness](005-nate-b-jones-vibe-coding-readiness.md) — Context window discipline as a key skill
- [#008: Phase Transition](008-nate-b-jones-phase-transition.md) — Task system as a solution to context window management at scale
- [#014: Skills Decision Framework](014-indydevdan-skills-framework.md) — MCP servers "torch your context window" — Berglund explains why and offers alternatives

## Related Curriculum

- [Module 02: Prompting & Workflows](../curriculum/02-prompting-and-workflows/README.md) — Context engineering as the evolution of prompt engineering
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Agent decomposition, compaction, and memory as patterns for long-running agents
