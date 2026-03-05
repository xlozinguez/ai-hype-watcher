---
source_id: "162"
title: "Making Claude Code Actually Remember Things"
creator: "Artem Zhutov"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=RDoTY4_xh0s"
date: "2026-02-28"
duration: "42:10"
type: "video"
tags: ["claude-code", "context-engineering", "mcp", "skills"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 162: Making Claude Code Actually Remember Things

> **Creator**: Artem Zhutov | **Platform**: YouTube | **Date**: 2026-02-28 | **Duration**: 42:10

## Summary

Artem Zhutov demonstrates a comprehensive memory system for Claude Code built on QMD (a semantic search engine by Toby, CEO of Shopify) and Obsidian. The system addresses the "cold start problem" — every new Claude Code session starts from zero, losing decisions and context from previous sessions. His solution combines three retrieval paths (temporal, topic-based, and graph visualization) with automatic session indexing via hooks, creating persistent cross-session memory that dramatically outperforms brute-force grep approaches.

The video benchmarks three search strategies against a personal Obsidian vault: native grep (slow, noisy, 200+ irrelevant files), BM25 keyword search via QMD (fast, relevant), and semantic vector search (finds meaning beyond keywords). The hybrid approach delivers the best results but takes ~35 seconds. Zhutov recommends starting with BM25 for speed, adding semantic search for brain dumps and transcripts where exact keywords are absent.

## Key Concepts

### The Cold Start Problem

Every new Claude Code terminal session starts with zero context about previous work. Users must re-explain decisions, project state, and goals. The brute-force approach — telling Claude to search your vault — takes 3+ minutes, consumes massive tokens, and produces noisy results (finding "sleep" in system calls alongside actual sleep journal entries). This problem compounds across sessions: 700 sessions in 3 weeks means enormous context that no single session can efficiently recover.

### QMD as a Retrieval Layer

QMD provides BM25 full-text search and vector-based semantic search over markdown collections. Each Obsidian vault folder maps to a QMD collection for focused searches. Compared to Claude's native grep: QMD searches return in seconds vs. minutes, produce more relevant results, consume far fewer tokens, and don't require subagent spawning. The semantic search capability goes beyond keywords — querying "days when I was happy" surfaces journal entries about shipping milestones and good sleep, not just entries containing the word "happy."

### Three Recall Paths

The memory system offers three ways to reconstruct context: (1) Temporal — reconstruct what you were doing yesterday, last week, or at a specific time by parsing Claude conversation logs; (2) Topic — use QMD BM25/semantic search to find all sessions and files related to a subject like "graph research"; (3) Graph — visual knowledge graph showing session blobs color-coded by recency with connections to created files, enabling spatial exploration of work history.

### Automatic Session Indexing Pipeline

A hook triggers on terminal close, exporting Claude conversation history as clean markdown (stripping system prompts, tool calls, and roles to keep only user messages as signal) into Obsidian, then embedding into QMD. This keeps the index always fresh without manual reindexing. The recall skill can then surface any past conversation instantly.

## Practical Takeaways

- **Start with BM25 search**: It gets 80% of the way there with near-instant results — add semantic search later for unstructured content like brain dumps
- **Map vault folders to QMD collections**: One-to-one mapping enables focused, efficient searches by category (daily notes, sessions, transcripts)
- **Use hooks for automatic indexing**: Export and embed sessions on terminal close so the index stays fresh without manual intervention
- **Parse signal from noise**: Strip system prompts and tool calls from conversation exports — only user messages contain retrievable context
- **External sources work too**: Download YouTube transcripts, articles, or any text content into QMD collections for semantic querying — similar to NotebookLM but locally controlled

## Notable Quotes

> "Your context stays. Even a year from now or 10 years, your context stays." — Artem Zhutov, on investing in personal knowledge infrastructure

> "Your notes stop being passive. They actually start doing things." — Artem Zhutov, on AI-connected knowledge bases

## Related Sources

- [148-noah-vincent-obsidian-claude](148-noah-vincent-obsidian-claude.md) — Another Obsidian + Claude Code integration approach

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Memory systems and context management for Claude Code
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Hook-based automation and recall skill patterns
