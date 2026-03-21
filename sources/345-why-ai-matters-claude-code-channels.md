---
source_id: "345"
title: "This New Claude Feature Is Actually Insane"
creator: "Why AI Matters"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=3ZpFVmx4La8"
date: "2026-03-20"
duration: "7:59"
type: "video"
tags: ["claude-code", "mcp", "multi-agent", "agentic-coding", "agent-teams"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 345: This New Claude Feature Is Actually Insane

> **Creator**: Why AI Matters | **Platform**: YouTube | **Date**: 2026-03-20 | **Duration**: 7:59

# This New Claude Feature Is Actually Insane

## Summary

This short-form reaction video covers Anthropic's release of **Claude Code Channels**, a feature enabling developers to control Claude Code sessions remotely via messaging platforms, starting with Telegram and Discord. The creator, Eloher, responds enthusiastically to the announcement, framing it as a significant competitive move against OpenAI's Codex and positioning Claude as a serious agentic coding platform. The feature is described as a research preview with plans to expand to additional integrations.

The core capability allows developers to interact with Claude Code sessions from their phones through MCP-connected messaging apps. This opens the door to multi-agent orchestration across Discord or Telegram channels, where multiple agents can operate in parallel and even communicate asynchronously. The creator notes this reduces his personal urgency to build custom robotic/agentic infrastructure, since Claude now provides scheduling and remote access natively.

The video is primarily enthusiast commentary rather than a technical deep-dive, but it surfaces a few meaningful architectural points: the feature uses the Agent SDK (not OAuth), is positioned as a "hackable" alternative to Claude's own Dispatch feature, and works with Claude in Amazon Bedrock. The creator briefly contrasts Channels with Dispatch, noting Anthropic's explicit intent to give developers multiple remote interaction patterns.

## Key Concepts

### Claude Code Channels
A new Anthropic release (described as a research preview) that connects Claude Code sessions to external messaging platforms via MCP integrations. Initially supports Telegram and Discord, allowing developers to send messages to and receive updates from active Claude Code sessions without being at their machine.

### MCP as the Integration Layer
Claude Code Channels is built on the Model Context Protocol (MCP), with Telegram and Discord as the first supported MCPs. This positions MCP not just as a tool-calling mechanism but as a **remote control interface** for agentic sessions — a meaningful expansion of MCP's practical role.

### Multi-Agent Orchestration via Messaging Channels
By routing Claude Code through Discord or Telegram channels, developers can theoretically run multiple agents in parallel across different channels and coordinate their outputs. The creator highlights this as enabling complex, asynchronous multi-agent workflows without custom infrastructure.

### Channels vs. Dispatch
Anthropic drew a distinction between two remote interaction patterns: **Dispatch** (the more polished, product-oriented approach) and **Channels** (designed for developers who want something "hackable" and customizable). This two-track strategy signals Anthropic is targeting both end-users and technical builders simultaneously.

### Competitive Positioning Against Codex
The creator explicitly frames Claude Code Channels as a direct answer to OpenAI Codex, arguing Claude Code now covers equivalent functionality with Claude's model quality behind it. The addition of scheduling and remote access narrows the gap between purpose-built agentic tools and Claude's native offering.

## Practical Takeaways

- **Remote Claude Code control is now possible via Telegram or Discord** — developers no longer need custom webhook infrastructure to interact with running Claude Code sessions from a mobile device.
- **Use the Agent SDK, not OAuth**, when integrating Claude Code Channels to maintain full agentic capability through the messaging interface.
- **Multi-agent setups can be structured around Discord/Telegram channels** — each channel can host a different agent or workflow, enabling lightweight orchestration without dedicated orchestration tooling.
- **Works with Claude on Amazon Bedrock**, making this feature accessible to enterprise teams already routing Claude through AWS infrastructure.
- **Channels is explicitly designed to be hackable** — developers should treat it as a building block for custom workflows rather than a finished product, as Anthropic plans to expand it over time.

## Notable Quotes

> "You can set up multiple agents to be doing multiple things on channels. You can get as complicated as you want. You can have it talking to itself at all times."

> "Channels is more focused on devs who want something hackable." — Anthropic (quoted via social media post in video)

> "Claude Code does everything that Codex does except it's with Claude behind it."
