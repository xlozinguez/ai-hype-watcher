---
source_id: "438"
title: "Claude Code got leaked"
creator: "The PrimeTime"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=GdgRpiQRsis"
date: "2026-04-01"
duration: "11:59"
type: "video"
tags: ["claude-code", "security", "mcp", "vibe-coding", "anthropic"]
curriculum_modules: ["03-claude-code-essentials", "06-strategy-and-economics"]
---

# 438: Claude Code got leaked

> **Creator**: The PrimeTime | **Platform**: YouTube | **Date**: 2026-04-01 | **Duration**: 11:59

# Claude Code Source Map Leak

## Summary

Anthropic accidentally published Claude Code's complete source maps to npm, effectively exposing the full, readable source code of their flagship agentic coding tool. Source maps are files that allow minified JavaScript to be reverse-engineered back into its original, human-readable form with full variable names and structure intact. The root cause traced back to a bug in the Bun runtime's development server that had been reported as a GitHub issue three weeks prior — and notably, a GitHub Actions bot flagged the issue as a duplicate, with the comment that it had been "found via Claude Code," an irony that was not lost on the internet.

The leaked code revealed a number of surprising implementation choices. Sentiment detection for negative user feedback is handled via a hardcoded regex list of phrases like "this sucks" and "damn it" rather than using Claude's own inference capabilities. Safety-critical system prompts ("cyber risk instructions") are embedded as plain strings in the client-side code with a comment asking developers to contact specific team members before modifying. There is also an unreleased Tamagotchi/collectible creature feature planned as an April 1st promotion. An "incognito mode" was found that instructs Anthropic employees using Claude Code in public repositories to hide any attribution or acknowledgment that they are using the tool.

The leak also surfaced a concrete security vulnerability: the `claude mcp get <name>` command will print MCP server URLs, headers, OAuth hints, and — for stdio servers — the entire environment block, meaning secrets stored in environment variables can be trivially exfiltrated to the terminal. PrimeTime closes with a broader warning about Anthropic's terms of service, which prohibit using Claude to build competing products, and reflects on the hypocrisy of a company that allegedly trained on open-source code without restriction now threatening legal action over its own leaked source.

## Key Concepts

### Source Maps as an Accidental Disclosure Vector
Source maps (`.map` files) are a standard web development tool that links minified/compiled JavaScript back to original source code for debugging purposes. They should never ship to production. When Anthropic published Claude Code to npm with source maps included — caused by a bug in their Bun-based build pipeline — anyone who downloaded the package could reconstruct the full original codebase, including variable names, comments, and internal documentation. This is a class of supply chain / build pipeline security failure that is easy to make and hard to catch without explicit CI checks.

### Hardcoded Heuristics in an AI Product
One of the more philosophically interesting findings is that Claude Code uses a static regex list to detect user frustration rather than delegating that task to the underlying model. This is a pragmatic engineering choice (fast, deterministic, no token cost) but it is also emblematic of "vibe-coded" codebases where quick solutions accumulate: the AI capability exists, but simpler legacy patterns get shipped because they are "good enough." It illustrates the gap between a product's marketing (world-class AI) and its implementation details.

### Client-Side Safety Prompt Storage
Safety-critical instructions ("cyber risk instructions") were found embedded as plain strings in the distributed client package with inline comments naming specific human gatekeepers. Storing safety-relevant prompts client-side means they are inspectable, modifiable by a determined user, and now — publicly documented. The more robust architecture would serve such prompts server-side, where they cannot be read or tampered with by the client. This represents a meaningful architectural security gap.

### MCP Credential Leakage Vulnerability
The `claude mcp get <name>` command was found to output the full environment block for stdio-type MCP servers, which can contain API keys, AWS credentials, and other secrets, directly to the terminal. This is a concrete, exploitable security vulnerability now publicly documented. Any developer using Claude Code with MCP servers that reference secrets via environment variables should audit this immediately.

### Terms of Service and Competing Products Clause
Anthropic's ToS prohibits using Claude to build products that compete with Anthropic. The video flags that this clause is broad enough to encompass always-on bots, persistent memory systems, remote planning tools, and multi-agent orchestration frameworks — all categories Anthropic is itself actively developing. The concern is that as third-party builders achieve meaningful traction in these categories, Anthropic has a contractual mechanism to terminate their access. This is a platform risk consideration for anyone building Claude-dependent products in adjacent spaces.

## Practical Takeaways

- **Audit your build pipeline for source map leakage**: Any npm package or web app should have explicit CI checks confirming source maps are excluded from production builds. Do not rely on framework defaults, especially when switching runtimes (e.g., migrating to Bun).
- **Never store sensitive prompts or safety instructions client-side**: System prompts embedded in distributed packages are readable by anyone who downloads them. Route safety-critical instructions through a server-side layer.
- **Audit MCP server configurations for secret exposure**: If you use Claude Code with MCP servers that are configured as stdio type and rely on environment variables for secrets, verify that `claude mcp get <name>` does not expose those secrets to terminal output.
- **Treat Anthropic's competing-products ToS clause as a genuine platform risk**: Builders developing persistent memory, always-on agents, or multi-agent orchestration on top of Claude's API should monitor how Anthropic defines "competing product" as their own product surface expands.
- **Fast-moving AI codebases accumulate exploitable technical debt**: The combination of hardcoded heuristics, client-side safety prompts, and credential leakage in a flagship product from a leading AI lab is a signal that "vibe-coded" velocity creates real attack surface. Treat AI tooling with the same security scrutiny as any other production dependency.

## Notable Quotes

> "There's something so funny about a company that just literally has access to a model that can determine sentiment and they're just like, 'Yeah, we can't use that. That's like that's impossible. We're going to use a 2005 whitelist.'"

> "The safety team has hand-artisanally crafted this string, and if you mess it up, you mess it up for everybody."

> "Claude Code is very vibe-coded. ChatGPT called it staff-level spaghetti. A company moving this fast is just going to have so many flaws. And now it's out there for people to be able to digest and actually take advantage of it."
