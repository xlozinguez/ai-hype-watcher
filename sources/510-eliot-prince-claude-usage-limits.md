---
source_id: "510"
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

# 510: Why Claude Keeps Hitting Usage Limits (& how to fix it)

> **Creator**: Eliot Prince | **Platform**: YouTube | **Date**: 2026-04-03 | **Duration**: 26:11

# Why Claude Keeps Hitting Usage Limits (& How to Fix It)

## Summary

Eliot Prince investigates why Claude users have been hitting session usage limits more frequently, tracing it to a quiet Anthropic policy change: during peak hours (5am–11am Pacific / 1pm–7pm GMT), session limits are consumed faster than before, even though weekly limits remain unchanged. The video demystifies the two distinct limit types—5-hour session caps and 200,000-token context windows—and explains how they interact to constrain productive AI work.

The bulk of the video is a 14-tip practical framework for using Claude more efficiently. Prince demonstrates the `/context` command as a diagnostic tool, showing how background MCPs, system prompts, extended thinking, and always-on connectors silently drain tokens before a user even types a message. The core insight is that token waste is largely invisible until you instrument it—and most of it comes from overhead, not actual work.

Prince's recommendations cluster around three levers: model selection (Sonnet over Opus for most tasks), conversation hygiene (new chat per task, specific prompts, batched requests), and aggressively pruning inactive tools and connectors. He also introduces "extra usage" credits as a tactical escape valve for avoiding mid-task interruptions.

## Key Concepts

### Session Limits vs. Context Windows
These are two separate constraints that compound each other. The **5-hour session limit** governs how much total work Claude will do within a rolling window—this is what has been throttled during peak hours. The **context window** (typically 200,000 tokens per chat) governs how much information Claude can hold in a single conversation. Burning through the context window degrades response quality (triggering auto-compaction); burning through the session limit stops work entirely. Efficient usage requires managing both simultaneously.

### Token Overhead from Background Tools
Using the `/context` command reveals that significant tokens are consumed before any user message is sent. In Prince's example: ~20,000 tokens from system/custom instructions, ~45,000 tokens from active MCP tools, plus additional tokens from Skills and memory files. This means a chat with many connectors active starts with 30–65k tokens already spent, dramatically accelerating both context window and session limit consumption—even when those tools aren't being used for the current task.

### Model Token Cost Multipliers
Different Claude models consume tokens at vastly different rates against session limits. Opus 4.6 costs approximately **5× more tokens** than Sonnet 4.6 for equivalent work. This makes model selection a primary lever for extending session longevity. However, Prince cautions against defaulting to Haiku for everything: for complex, multi-step tasks, a less capable model may require more round-trips and actually be less efficient in aggregate—analogous to moving people one-by-one versus in bulk transport.

### Conversation Hygiene as Efficiency
Every message in a conversation thread adds to the token overhead for all subsequent messages in that thread—prior context is re-processed with each prompt. This means a 30-message conversation costs significantly more per exchange than a 5-message one on the same topic. Starting a **new chat per discrete task** prevents context accumulation from unrelated work. Batching multiple small requests into single prompts further reduces per-request overhead costs.

### Extended Thinking as a Hidden Token Drain
The "extended thinking" toggle is identified as a major silent token consumer. When enabled, Claude generates intermediate reasoning steps that consume additional output tokens and drive more back-and-forth. Users who enable it once and forget about it experience accelerated session drain. Disabling it for routine tasks is one of the highest-ROI single changes a user can make.

## Practical Takeaways

- **Run `/context` in any Claude chat** to get a diagnostic breakdown of what's consuming your tokens before you even begin work—MCP tools, system prompts, and Skills each show their individual token costs, making it easy to identify what to disable.
- **Default to Sonnet, escalate to Opus deliberately**: Use Sonnet 4.6 for everyday tasks and only switch to Opus when the task genuinely requires it with plenty of session budget remaining; never leave Opus selected as a default.
- **One task, one chat**: Resist the temptation to use a single long-running conversation for multiple different topics. New task context means starting a fresh chat to prevent prior message history from silently inflating every subsequent prompt's token cost.
- **Disable connectors and MCPs you're not actively using**: Tools like always-on browser extensions (e.g., Claude in Chrome), Apify, Gmail, and Notion integrations consume tokens passively. Toggle them off between task sessions and only enable what the current task needs.
- **Add a small extra usage credit** (a few dollars/pounds) as a tactical buffer: this prevents the worst failure mode—Claude stopping mid-task—and lets work complete before the session refills, rather than abandoning half-finished outputs.

## Notable Quotes

> "Specificity is efficiency. Don't get it to summarize a whole document and then zero down—say like, I want to summarize the financial risks in section three of this PDF so Claude knows exactly where to look."

> "Every time I run a prompt, it's going to remember all of the stuff that went before, and that's going to add to that token usage overhead and drag things down even more. It's like carrying extra baggage with you."

> "You might actually find that just using Haiku for everything is taking a lot longer. And actually, it's not actually that much more efficient when you break down how many trips back and forth and things it's having to work out."

---
