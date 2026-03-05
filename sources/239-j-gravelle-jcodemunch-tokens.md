---
source_id: "239"
title: "Claude MCP Tool That Cuts Token Costs by 99% — jCodeMunch"
creator: "J. Gravelle"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=vzCy44o3JwA"
date: "2026-03-01"
duration: "8:17"
type: "video"
tags: ["mcp", "claude-code", "ai-economics", "context-engineering"]
curriculum_modules: ["03-claude-code-essentials", "06-strategy-and-economics"]
---

# 239: Claude MCP Tool That Cuts Token Costs by 99% — jCodeMunch

> **Creator**: J. Gravelle | **Platform**: YouTube | **Date**: 2026-03-01 | **Duration**: 8:17

## Summary

J. Gravelle introduces jCodeMunch, an MCP server he built that dramatically reduces token consumption when working with codebases in Claude Code or any MCP-compatible tool. The core idea is simple: instead of Claude reading entire files to answer questions (the "read every volume of the encyclopedia" approach), jCodeMunch indexes code by symbols and serves only the relevant portions. A benchmark on a real work project showed 700 tokens consumed with jCodeMunch versus 3,850 without — a 5.5x reduction on a single lookup, with larger codebases seeing up to 99.7% savings (480 vs. 141,000 tokens).

The tool automatically reindexes as code changes, requiring no manual maintenance. Gravelle frames this as a pattern that will eventually be built into LLMs natively, but for now represents a significant cost and speed optimization for developers paying per-token.

## Key Concepts

### Symbol-Based Code Indexing

Rather than reading entire files, jCodeMunch pre-indexes code by symbols (functions, classes, variables) and serves only the relevant indexed portions when Claude needs to look something up. This is analogous to using an encyclopedia index rather than reading every volume — you go directly to the "P" section for pomegranates instead of reading A through Z.

### Automatic Reindexing

As code changes during a development session, jCodeMunch automatically reindexes to keep the symbol index current. This means the tool stays accurate without requiring manual intervention, making it practical for real development workflows where files change frequently.

### Token Economics at Scale

The savings compound dramatically with codebase size. A single lookup saved 3,150 tokens (700 vs. 3,850). A larger project showed 141,000 tokens reduced to 480 — a 99.7% reduction. Gravelle estimates annual savings of ~$15,000 for sustained development work on a single project, making the cost of Opus queries (one question cost him $6) far more manageable.

## Practical Takeaways

- **Install jCodeMunch as an MCP server**: Clone from GitHub and install — Claude can handle the setup process itself
- **Works with any MCP-compatible tool**: Not Claude-specific; any tool supporting MCP servers benefits from the token reduction
- **Biggest impact on large codebases**: Small projects see 5-6x savings; large codebases see 99%+ reduction
- **Monitor your token usage**: Gravelle emphasizes tracking per-query costs, noting that a single Opus query can cost $6 without optimization

## Notable Quotes

> "It's kind of like if you need to look something up in the encyclopedia, currently Claude takes every volume and reads it. All you needed was the P volume." — J. Gravelle, on the fundamental problem jCodeMunch solves

## Related Sources

- [164-bart-slodyczka-openclaw-token-reduction](164-bart-slodyczka-openclaw-token-reduction.md) — Complementary token optimization strategies for OpenClaw

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — MCP server integration and context optimization
- [Module 06: Strategy & Economics](../curriculum/06-strategy-and-economics/README.md) — Token economics and cost management for AI-assisted development
