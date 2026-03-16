---
source_id: "274"
title: "I Didn't Know This Was Possible Until Now"
creator: "AI LABS"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=LqN_ItMqovA"
date: "2026-03-13"
duration: "11:43"
type: "video"
tags: ["mcp", "context-engineering", "claude-code", "skills", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 274: I Didn't Know This Was Possible Until Now

> **Creator**: AI LABS | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 11:43

# I Didn't Know This Was Possible Until Now

## Summary

This video explores MCP2 CLI, a tool that addresses the well-documented context window bloat problem with Model Context Protocol (MCP) servers. Rather than exposing tool schemas and descriptions directly in the context window, MCP2 CLI converts MCP servers into bash-callable CLI tools, injecting their outputs only when explicitly requested. The video situates this solution within a broader community effort — referencing Cloudflare's original diagnosis, Anthropic's acknowledgizing paper, and Docker's earlier "code mode" approach — positioning MCP2 CLI as the most flexible runtime solution to date.

The team demonstrates a practical build using Claude Code with four MCP servers (Supabase, GitHub, Puppeteer, Context7) totaling 78 tools, showing how MCP2 CLI keeps context lean while supporting dynamic updates, caching (1-hour TTL), and secure credential handling via environment variables. A key workflow insight emerges around skills vs. CLAUDE.md instructions: skills load their descriptions directly into the agent's context, making tool availability and usage patterns explicit without relying on the agent to read a markdown file.

The most significant unlock demonstrated is redirecting large MCP outputs to files instead of the context window — then using bash tools like `grep` to extract only the needed data. This mirrors a workflow Cursor had introduced natively, but MCP2 CLI makes it available in any agent environment that supports bash. Token efficiency benchmarks using the `tiktoken` library back the claims quantitatively.

---

## Key Concepts

### Runtime vs. Build-Time MCP Conversion
MCP2 CLI converts MCP servers into bash commands at the moment of invocation (runtime), not ahead of time (build time). This means any upstream changes to an MCP server are automatically reflected without manual updates. A caching layer (1-hour TTL by default) prevents the performance cost of repeated conversions, balancing freshness with speed.

### Context Window Output Redirection
Because MCP tools are now treated as bash commands, their outputs can be piped to files rather than injected into the context window. The agent can then use bash utilities like `grep` to extract only the relevant data, dramatically reducing token consumption for large outputs — a pattern previously only available natively inside Cursor.

### Skills vs. CLAUDE.md for Tool Awareness
The video draws a practical distinction between skills and CLAUDE.md instructions. Skills have their descriptions loaded directly into the agent's active context, so the agent intrinsically knows what tools exist and when to invoke them. CLAUDE.md instructions are passive — the agent must "choose" to reference them. For tool orchestration, skills are the more reliable mechanism.

### Token-Efficient Output Formatting (Tune Format)
MCP2 CLI supports a `tune` output format that combines indentation with CSV-style lists, compacting large structured data more efficiently than JSON or YAML. The video recommends instructing the agent (via CLAUDE.md or skills) to use this format for output-heavy MCPs like Context7, reducing unnecessary token consumption.

### Secure Credential Handling in CLI Contexts
Running API keys and access tokens as CLI arguments poses a security risk since they can appear in process listings. MCP2 CLI handles credentials through environment variables, file path references, or a runtime-injected secret manager — keeping sensitive data out of command-line arguments entirely.

---

## Practical Takeaways

- **Redirect large MCP outputs to files** rather than accepting them into the context window; use `grep` or similar bash tools to extract only what's needed — this is the highest-leverage context management technique shown.
- **Use skills over CLAUDE.md for critical tool instructions**: if you need the agent to reliably use a specific MCP before writing code, encode that in a skill whose description is always loaded, not in a markdown file the agent may skip.
- **Create per-MCP skills** that document each server's available tools, usage patterns, and invocation timing — Claude can generate these automatically once the MCPs are connected.
- **Specify output format explicitly** for verbose MCPs: instruct the agent to use `tune` format (or equivalent compact format) when querying documentation or data-heavy servers like Context7.
- **Get access tokens before installation**: configure credentials first to avoid mid-setup errors; MCP2 CLI's skill handles the rest of the configuration workflow automatically once credentials are available.

---

## Notable Quotes

> "Skills are better because their descriptions are loaded directly into the agent's context. So it already knows what tools are available and when to use them rather than us just dumping instructions into claude.md and hoping it reads them."

> "An agent that can click and scroll and interact with its own UI catches things that static code review never can."

> "The biggest unlock came from something that wasn't even possible when MCPs were handled natively by agents... now with this CLI, it's possible because MCPs are treated as bash command tools."

---
