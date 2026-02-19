---
source_id: "099"
title: "How AI Agents Search Their Memory"
creator: "Damian Galarza"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=SpReZZk_13w"
date: "2026-02-17"
duration: "13:26"
type: "video"
tags: ["context-engineering", "agentic-coding", "multi-agent"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 099: How AI Agents Search Their Memory

> **Creator**: Damian Galarza | **Platform**: YouTube | **Date**: 2026-02-17 | **Duration**: 13:26

## Summary

Damian Galarza provides a detailed technical breakdown of how AI agents search their memory, using OpenClaw's default memory system as a concrete implementation example. The video covers the full pipeline: keyword search (grep, BM25), semantic search (embeddings, vector databases), hybrid fusion approaches, reranking, and incremental sync. Galarza notes that the Claude Code team started with a vector database but found grep-based agentic search actually performed better and was easier to maintain — a counter-intuitive finding that challenges the assumption that semantic search is always superior.

The core architectural insight is that no single search approach is sufficient. Keyword search excels at exact matches (error codes, function names) but misses semantic relationships. Semantic search finds conceptually related content but fails on literal string matching. OpenClaw's solution combines both via weighted score fusion (70% vector, 30% keyword), then optionally reranks results using an LLM for nuanced relevance judgment. The two-tool pattern — `memory_search` for discovery, `memory_get` for retrieval — keeps context windows lean by fetching only the specific content the agent actually needs.

## Key Concepts

### Keyword vs. Semantic Search Trade-offs

Keyword search (grep, BM25) matches literal text and works well for specific identifiers, error codes, and function names. BM25 improves on basic grep by ranking results based on term frequency and uniqueness across the corpus. Semantic search converts text into embeddings — high-dimensional vectors that represent meaning — enabling matches between conceptually related but lexically different text. However, semantic search fails on exact-match queries. The Claude Code team's finding that grep-based search outperformed their initial vector database implementation demonstrates that simpler approaches often win in practice.

### Hybrid Search with Weighted Score Fusion

OpenClaw runs keyword and semantic searches in parallel, then combines results using weighted score fusion: 0.7 times the vector similarity score plus 0.3 times the BM25 text score. Results appearing in both searches get combined scores; results from only one search get zero for the other. Both searches use a 4x candidate multiplier (requesting 24 candidates when 6 results are needed) to give the fusion step more to work with. An alternative approach, Reciprocal Rank Fusion (RRF), uses position rather than score strength — simpler but less precise. The final results are filtered by a minimum threshold of 0.35.

### Chunking and Embedding Architecture

OpenClaw breaks markdown memory files into chunks of roughly 400 tokens with 80-token overlap between chunks. Each chunk stores its text, embedding vector, and the line range from the original file — enabling agents to cite exactly where a memory came from. An embedding cache table prevents redundant API calls by hashing chunk text and caching embeddings keyed by provider and model. This is a meaningful cost optimization since embedding API calls accumulate quickly across frequent memory syncs.

### Search-Then-Get Two-Tool Pattern

OpenClaw exposes two tools: `memory_search` returns an array of snippets (file path, line numbers, relevance score, 700-character preview) and `memory_get` retrieves specific sections of a memory file by path and line range. This deliberate two-step pattern mirrors how humans search — scan results for relevance, then read only what matters. It prevents loading entire files into the context window, keeping token usage efficient. The system prompt describes `memory_search` as a "mandatory recall step" that agents must use before answering questions about prior work, decisions, or preferences.

## Practical Takeaways

- **Combine keyword and semantic search**: Neither approach alone is sufficient. Keyword search handles exact matches; semantic search handles conceptual relationships. Weighted fusion at 70/30 vector/keyword is OpenClaw's empirically derived ratio.
- **Chunk with overlap for context preservation**: 400-token chunks with 80-token overlap ensure that ideas split across chunk boundaries are still discoverable in both adjacent chunks.
- **Cache embeddings aggressively**: Hashing chunk text and caching embeddings by provider/model avoids redundant API calls when files are rechunked but content hasn't changed.
- **Use a two-step search-then-retrieve pattern**: Return lightweight previews first, then fetch full content only for relevant results. This keeps context windows lean and reduces token waste.
- **Start simple before adding complexity**: Claude Code's team found grep outperformed their vector database. BM25 via SQLite FTS5 is production-quality keyword search that requires no external service.

## Notable Quotes

> "Interestingly, the Claude Code team started with a vector database, but they found that grep-based agentic search actually performed better and was easier to maintain." — Damian Galarza

> "Semantic search does not perform well for literal string searches. For example, looking for an error code like 'error connection refused' — semantic search may not find relevant results." — Damian Galarza

> "OpenClaw's memory system is a masterclass in practical AI architecture." — Damian Galarza

## Related Sources

- [032: OpenClaw: 160,000 Developers Just Showed Us What People Actually Want From AI](032-nate-b-jones-openclaw.md) — OpenClaw's broader significance and adoption that provides context for the memory system described here
- [058: The TRUTH About OpenClaw AI Agents](058-krakowski-openclaw-agents.md) — Practical OpenClaw usage patterns that complement this technical deep-dive
- [048: Before You Build Another Agent, Understand This MIT Paper](048-brainqub3-recursive-language-models.md) — Theoretical foundations for context management in recursive language models
- [084: This Simple 60% Rule Stops Context Rot](084-dylan-davis-context-rot-60-rule.md) — Context window management strategies that relate to the search-then-get pattern for keeping context lean
- [040: Stop Feeding Claude Your Entire CLAUDE.md](040-charlie-automates-claudemd-context.md) — Context discipline principles that the two-tool memory pattern exemplifies

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Context engineering fundamentals and the practical trade-offs between search approaches
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Agent memory architectures, the search-then-get pattern, and hybrid retrieval as an agentic design pattern
