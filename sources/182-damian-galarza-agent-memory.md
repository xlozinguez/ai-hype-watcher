---
source_id: "182"
title: "How AI Agent Memory Systems Work: Sessions, Compaction, and Persistence"
creator: "Damian Galarza"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Seu7nksZ_4k"
date: "2026-02-11"
duration: "9:05"
type: "video"
tags: ["context-engineering", "agentic-coding", "claude-code"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 182: How AI Agent Memory Systems Work: Sessions, Compaction, and Persistence

> **Creator**: Damian Galarza | **Platform**: YouTube | **Date**: 2026-02-11 | **Duration**: 9:05

## Summary

Damian Galarza breaks down how AI agents achieve persistent memory despite being inherently stateless. He explains the two-layer architecture — session memory (conversation history) and long-term memory (what survives between sessions) — and uses Google's November 2025 white paper on context engineering to categorize memory into episodic, semantic, and procedural types.

The video uses OpenClaw as a concrete case study, showing how its entire memory system is built on markdown files rather than vector databases. The key insight is that the files themselves are only half the story — what matters are the four mechanisms that trigger reads and writes at the right moments in a conversation's lifecycle.

## Key Concepts

### Session Memory and Compaction

AI models are stateless — conversation history must be passed on each call. As context windows fill up, compaction summarizes the history to continue without losing critical details. Three compaction strategies exist: count-based (token/turn threshold), time-based (idle timeout), and event-based/semantic (task completion detection). Event-based is the most intelligent but hardest to implement correctly.

### Three Types of Long-Term Memory

Google's "Context Engineering: Sessions and Memory" white paper (November 2025) categorizes agent memory into three types: episodic (what happened in past interactions), semantic (facts and user preferences), and procedural (workflows and learned routines). An effective memory system must filter what is worth remembering, consolidate duplicate or contradictory entries, and overwrite outdated information — typically handled by a secondary LLM instance.

### OpenClaw's Markdown-Based Memory Architecture

OpenClaw implements memory with three components: a `memory.md` file (semantic store, 200-line cap, loaded into every prompt), daily logs (episodic, append-only), and session snapshots (raw conversation excerpts from the last 15 meaningful messages, not summaries). Four mechanisms activate these: bootstrap loading at session start, pre-compaction flush (write-ahead log pattern before context is lost), session snapshot on `/new` or `/reset`, and direct user instruction ("remember this").

## Practical Takeaways

- **Memory does not require complex infrastructure**: Markdown files with clear read/write triggers can implement a complete agent memory system — no vector database needed.
- **Pre-compaction flush is a write-ahead log**: Converting a destructive operation (context loss) into a checkpoint by writing to the daily log before compaction fires is a pattern borrowed from database design.
- **Three questions define any memory system**: What is worth remembering? Where does it go? When does it get written? Answering these is sufficient to build agent memory.
- **Claude Code uses the same approach**: Claude Code's recently shipped memory feature also uses markdown files, validating the simplicity of this pattern.

## Notable Quotes

> "You don't need a complex setup to give an agent memory. You just need clear instructions to three questions. What's worth remembering? Where does it go? And when does it get written?" — Damian Galarza

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Memory.md and context management in Claude Code
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Agent memory architecture and compaction strategies
