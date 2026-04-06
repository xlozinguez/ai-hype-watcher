---
source_id: "511"
title: "Why Claude Keeps Hitting Usage Limits (& how to fix it)"
creator: "Eliot Prince"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=vnocKrxasg4"
date: "2026-04-03"
duration: "26:11"
type: "video"
tags: ["context-engineering", "prompt-engineering", "mcp"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials"]
---

# 511: Why Claude Keeps Hitting Usage Limits (& how to fix it)

> **Creator**: Eliot Prince | **Platform**: YouTube | **Date**: 2026-04-03 | **Duration**: 26:11

# Why Claude Keeps Hitting Usage Limits (& How to Fix It)

## Summary

Eliot Prince investigates a frustrating pattern many Claude users have experienced: hitting session usage limits faster than expected. The root cause turns out to be a quiet policy change Anthropic made—during peak hours (5am–11am Pacific / 1pm–7pm GMT), users consume their 5-hour session allowance faster than before. Weekly limits remain unchanged, but peak-hour usage now costs more "against the clock," analogous to peak-hour train ticket pricing.

The video is primarily a practical guide to understanding how tokens and context windows interact with session limits, then optimizing both. Prince demonstrates the `/context` command as a diagnostic tool—revealing that background tools, MCP connectors, system prompts, and extended thinking can silently consume tens of thousands of tokens before a user types a single word. He also clarifies the distinction between session limits (5-hour block caps that reset), weekly limits (unchanged), and context windows (200k tokens per chat, occasionally 1M).

The bulk of the video covers 14 concrete tips to reduce token burn: switching to Sonnet instead of Opus, batching prompts, starting fresh chats per task, disabling unused connectors and extended thinking, and writing tighter prompts. The core insight is that inefficient usage habits—not just volume of work—are often the primary driver of hitting limits early.

## Key Concepts

### Session Limits vs. Weekly Limits vs. Context Windows
These are three distinct constraints that interact. **Session limits** are 5-hour rolling blocks with a token cap; during peak hours the cap is effectively lower. **Weekly limits** remain unchanged regardless of peak hours. **Context windows** (200k tokens per chat, sometimes 1M) are per-conversation caps—as conversation history grows, every new prompt carries that entire history as overhead, accelerating both context exhaustion and session burn.

### Token Cost Varies by Model
Not all Claude models consume tokens at the same rate. Opus costs roughly **5x more tokens** than Sonnet for the same task. Haiku is cheaper per token but may require more back-and-forth iterations, potentially making it less efficient for complex tasks than a single well-scoped Sonnet prompt. Model selection is a lever for managing session burn, not just output quality.

### The `/context` Command as a Diagnostics Tool
Running `/context` in a Claude chat exposes a breakdown of what's consuming tokens before any user content is processed: system prompts, MCP tools, Claude skills, memory files, and other connectors. In the video's example, system prompt instructions alone consume ~20,000 tokens and MCP tools add ~45,000 tokens—meaning roughly 65k of the 200k context window is pre-consumed on load. This is the most actionable diagnostic step for users whose limits feel unexpectedly low.

### Background Tools and Connectors as Silent Token Drain
MCP connectors, always-on integrations (Google Drive, Gmail, Notion, Apify, browser control extensions), and extended thinking all add token overhead even when not actively used in a given task. Extended thinking in particular compounds cost by generating intermediate reasoning outputs. Disabling unused connectors and toggling off extended thinking when not needed can meaningfully extend session runway.

### Conversation Hygiene: Batching and Task Isolation
Accumulated chat history is carried as context overhead on every subsequent message. After 20–30 messages, the background weight of prior conversation significantly inflates per-prompt token cost. Two habits mitigate this: (1) **start a new chat per distinct task** to avoid cross-topic context bloat, and (2) **batch related instructions into single prompts** rather than issuing sequential single-step requests—each message incurs a full overhead cost regardless of size.

## Practical Takeaways

- **Run `/context` first** when hitting limits unexpectedly—it reveals which background tools, system prompts, and connectors are pre-consuming tokens before you type anything, giving you a clear prioritization list for what to disable.
- **Default to Sonnet, escalate to Opus deliberately**—for everyday tasks Sonnet delivers strong results at 1/5 the token cost of Opus; only switch up when task complexity genuinely justifies it.
- **Disable extended thinking and unused connectors by default**—treat these as opt-in for specific tasks rather than always-on features; they are among the largest silent contributors to token burn.
- **One chat per task, batch your prompts**—start a fresh conversation when switching task types to avoid compounding context overhead, and consolidate multi-step instructions into a single message to cut redundant per-message overhead charges.
- **Add small credits as a backstop, not a first resort**—a few dollars of extra usage credit can prevent mid-task interruptions without needing to change workflows, but it doesn't replace optimization; it just buys time when limits are hit at an inconvenient moment.

## Notable Quotes

> "Specificity is efficiency. Don't get it to summarize a whole document and then zero down. Say like, actually, I want to summarize the financial risks in section three of this PDF so Claude knows exactly where to look."

> "Every time I run a prompt, it's going to remember all of the stuff that went before, and that's going to add to that token usage overhead and drag things down even more. It's like carrying extra baggage with you."

> "You can think of this almost like the public transport system here in the UK. During peak travel hours, tickets are more expensive because there's more demand. And this is kind of what's been coming to AI and particularly Claude."
