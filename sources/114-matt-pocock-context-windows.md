---
source_id: "114"
title: "Most devs don't understand how context windows work"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=-uW5-TaVXu4"
date: "2025-10-22"
duration: "9:33"
type: "video"
tags: ["context-engineering", "agentic-coding", "claude-code"]
curriculum_modules: ["01-foundations", "03-context-engineering"]
---

# 114: Most devs don't understand how context windows work

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2025-10-22 | **Duration**: 9:33

## Summary

Pocock argues that the most common skill gap among developers using coding agents is not understanding context windows — the total set of input and output tokens an LLM can see at once. He frames context window management as the single most impactful thing developers can learn to improve their AI coding results, and demonstrates practical techniques using Claude Code.

The video covers the anatomy of a context window (system prompt, user messages, assistant responses), hard-coded model limits, and why those limits exist. The critical insight is the "lost in the middle" problem: LLMs deprioritize information in the middle of long conversations, strongly favoring content at the start and end. Pocock demonstrates Claude Code's `context` command showing token usage, and compares `clear` (blank slate) versus `compact` (summarized context) as strategies for managing bloat. He warns specifically against MCP server proliferation and oversized rules files as context window killers.

## Key Concepts

### Context Window Anatomy ([00:30](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=30))

The context window comprises all input tokens (system prompt, user messages) and output tokens (assistant responses). As conversations grow, the window fills until hitting a hard-coded limit set by the model provider. This limit can be hit by accumulated conversation length or by a single oversized message (document upload, image transcription).

### Lost in the Middle Problem ([03:30](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=210))

All LLMs — from tiny to frontier — suffer from degraded attention to information in the middle of their context window. Content at the start (primacy) and end (recency) of the conversation has disproportionate influence on outputs. This is an emergent property of the attention mechanism, not intended behavior, and it worsens as context length increases.

### Bigger Is Not Better ([02:30](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=150))

Models like Meta's Llama 4 Scout advertise 10 million token context windows, but in practice suffer severe lost-in-the-middle degradation. Gemini 2.5 Pro's 2M token window is a selling point, but the real metric is how well a model retrieves and acts on information within its context, not the raw size. The needle-in-a-haystack benchmark is misleading because real tasks require acting on distributed information, not finding a single sentence.

### Clear vs. Compact ([05:30](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=330))

Claude Code offers two context management strategies. `clear` wipes conversation history for a blank slate — the default choice for most situations. `compact` uses an LLM to summarize the conversation into a compressed message, preserving intention and vibes while dramatically reducing token count (from 70K+ to ~4K in Pocock's demo). Compact is useful when you want to preserve context continuity.

### MCP Servers as Context Bloat ([07:30](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=450))

MCP servers are attractive for extending agent capabilities but can consume a large portion of the context window just by existing in the system prompt. Pocock warns that adding multiple MCP servers can push system prompt consumption to a third or more of available context, leaving little room for actual work. He advocates extreme caution in MCP server selection.

## Practical Takeaways

- **Monitor context usage regularly**: Use Claude Code's `context` command to check how much of your context window is consumed by system prompt, messages, and tools.
- **Clear aggressively**: When starting new work, default to `clear` rather than carrying forward stale conversation. Reserve `compact` for when you need continuity.
- **Get scared at 50% usage**: Pocock starts worrying when only ~50K tokens remain of a 200K limit and recommends clearing at that point.
- **Minimize MCP servers**: Only add MCP servers you actively need. Each one consumes context budget that could be used for actual code exploration and reasoning.
- **Keep rules files lean**: Oversized CLAUDE.md or cursor rules files contribute to lost-in-the-middle problems. Concise instructions leave more budget for productive work.

## Notable Quotes

> "If there is a skill issue that I see most often with devs, it is not thinking enough about the context window. The context window is the main constraint that most AI coding agents face these days." — Matt Pocock ([00:15](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=15))

> "The more information that you give a model, the worse it's going to perform. All models suffer from a problem of retrieving information from their own context." — Matt Pocock ([03:00](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=180))

> "I tend to be extremely cautious about adding MCP servers to my setup because I know how important having a lean context window is." — Matt Pocock ([08:00](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=480))

## Related Sources

- [011: Prompt Engineering is Dead](011-confluent-developer-context-engineering.md) — Context engineering as the key discipline for AI-assisted development
- [048: Before You Build Another Agent, Understand This MIT Paper](048-brainqub3-recursive-language-models.md) — Theoretical limits of LLM context processing
- [084: The 60% Rule Stops Context Rot](084-dylan-davis-context-rot-60-rule.md) — Quantitative context management strategy
- [112: Most devs don't understand how LLM tokens work](112-matt-pocock-llm-tokens.md) — Pocock's companion video on tokenization fundamentals

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — Core LLM architecture including context windows
- [Module 03: Context Engineering](../curriculum/03-context-engineering/README.md) — Context window management and optimization strategies
