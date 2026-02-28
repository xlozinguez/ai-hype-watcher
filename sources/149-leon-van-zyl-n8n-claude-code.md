---
source_id: "149"
title: "Stop Using Claude Code Without This Tool"
creator: "Leon van Zyl"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=CQeKmG1o85E"
date: "2026-02-23"
duration: "15:59"
type: "video"
tags: ["claude-code", "mcp", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 149: Stop Using Claude Code Without This Tool

> **Creator**: Leon van Zyl | **Platform**: YouTube | **Date**: 2026-02-23 | **Duration**: 15:59

## Summary

Leon van Zyl argues that n8n (a visual workflow automation platform) and Claude Code are complementary tools rather than competitors. He demonstrates several integration patterns: converting n8n workflow prototypes into full applications via Claude Code, exposing n8n workflows as MCP servers for Claude Code to consume, and using n8n webhooks with Claude Code hooks to receive notifications when agent tasks complete.

The video positions n8n as a rapid prototyping and backend orchestration layer that pairs well with Claude Code's ability to build UIs and full applications. The key insight is that n8n's hundreds of integrations (Gmail, Slack, Telegram, databases) become instantly accessible to Claude Code through the MCP protocol, turning visual workflows into agent-consumable tools.

## Key Concepts

### N8N as Rapid Prototyping Layer

N8n allows building complex multi-step workflows (e.g., generate video script with GPT-5, create video with Sora 2, upload to YouTube) in minutes through visual drag-and-drop. Once a proof of concept works, Claude Code can convert it into a standalone application or build a UI that calls the n8n workflow via webhook.

### Exposing N8N Workflows as MCP Servers

N8n has a built-in MCP server trigger node. By connecting data table operations (get, insert, update) to this trigger, any n8n workflow becomes an MCP-compatible tool that Claude Code can discover and invoke. This gives Claude Code access to n8n's entire integration ecosystem — databases, email, Slack, WhatsApp, and more — without writing custom code.

### Claude Code Hooks for Notifications

Using Claude Code's built-in hooks system (specifically the "stop" hook), you can trigger an n8n webhook whenever the agent completes work. N8n then forwards the notification to Telegram, Slack, or any other platform. This solves the problem of babysitting long-running agent tasks.

## Practical Takeaways

- **Prototype in n8n, productionize with Claude Code**: Build and validate workflows visually, then use Claude Code to build a proper application around them
- **Use MCP to bridge n8n and Claude Code**: The `mcp server trigger` node in n8n exposes any workflow as tools that Claude Code can call directly
- **Set up completion notifications**: Configure Claude Code hooks to call n8n webhooks, which forward to Telegram/Slack so you don't have to watch the agent work
- **N8n as backend infrastructure**: Keep complex orchestration logic in n8n (email + Slack + YouTube + database) while Claude Code builds the frontend

## Notable Quotes

> "From my perspective, it's not really a debate on whether you should use Claude Code or n8n. My answer is use both." — Leon van Zyl

## Related Sources

_None currently in collection from this creator._

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — MCP server integration and hooks configuration
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Tool integration and workflow automation patterns
