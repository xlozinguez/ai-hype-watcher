---
source_id: "346"
title: "This New Claude Feature Is Actually Insane"
creator: "Why AI Matters"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=3ZpFVmx4La8"
date: "2026-03-20"
duration: "7:59"
type: "video"
tags: ["claude-code", "agentic-coding", "multi-agent"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 346: This New Claude Feature Is Actually Insane

> **Creator**: Why AI Matters | **Platform**: YouTube | **Date**: 2026-03-20 | **Duration**: 7:59

## Summary

Eloher from Why AI Matters reacts to the release of Claude Code Channels — a new feature that allows users to control Claude Code sessions through messaging platforms like Telegram and Discord via MCP integrations. The video captures the immediate community reaction and positions the feature as a competitive shift against OpenAI's Codex product.

The core development is that Claude Code sessions can now be accessed remotely through third-party messaging apps rather than requiring a direct terminal connection. This enables use cases like managing coding agents from a phone, setting up multiple agents on different Discord channels handling different tasks, and creating always-on agent workflows. The feature is described as a "research preview" by Anthropic with plans for expansion. The creator also references the existing Dispatch feature for remote Claude Code access, noting that Channels is positioned as a more "hackable" alternative for developers.

While the video is enthusiastic to the point of hype, it captures an important product development: the decoupling of agentic coding interfaces from traditional IDE/terminal paradigms, allowing Claude Code to operate as a persistent background service controlled through familiar communication channels.

## Key Concepts

### Claude Code Channels — Remote Agent Control

Claude Code Channels allows users to interact with Claude Code sessions through Telegram and Discord MCPs, effectively turning messaging platforms into remote control interfaces for coding agents. This decouples the agent interaction from the terminal/IDE, enabling phone-based oversight of long-running coding tasks. The feature represents Anthropic's approach to the "remote agent" problem — rather than building a proprietary interface, they leverage existing messaging infrastructure via MCP.

### Multi-Agent Communication Architecture

The Discord integration in particular enables a multi-agent communication pattern: different Claude Code instances can be assigned to different channels, potentially communicating with each other or handling parallel workstreams. This maps to existing patterns where developers use Slack/Discord for team coordination, but replaces some human team members with Claude Code agents. The creator envisions agents "talking to itself at all times" across channels, pointing toward persistent autonomous agent architectures.

### Competitive Parity with Codex

The video explicitly positions Channels as making Claude Code functionally equivalent to OpenAI's Codex product for remote/asynchronous coding — but with Claude's underlying model quality. Combined with Claude's existing Cowork mode and scheduling capabilities, the feature set closes the gap on Codex's primary differentiator of background task execution and remote monitoring.

## Practical Takeaways

- **Use Telegram for mobile oversight**: Claude Code Channels via Telegram enables checking on and directing long-running agent sessions from your phone without needing terminal access.
- **Discord for multi-agent setups**: Setting up different Claude Code instances on different Discord channels creates a lightweight multi-agent coordination layer using familiar infrastructure.
- **Channels vs. Dispatch**: Channels is the "hackable" developer-focused option for remote Claude Code access; Dispatch is the more polished alternative — choose based on customization needs.
- **Agent SDK required**: Using Channels requires the Agent SDK rather than standard OAuth, which affects how subscriptions and billing work.

## Notable Quotes

> "Claude Code and Claude Cowork are basically now OpenAI Codex." — Why AI Matters

> "You can have it talking to itself at all times." — Why AI Matters

## Related Sources

- [281: Ray Amjad - Claude Code Interruptions](281-ray-amjad-claude-code-interruptions.md) — Remote Claude Code interaction patterns
- [283: Income Stream Surfers - Loops Skills Memory](283-income-stream-surfers-loops-skills-memory.md) — Claude Code agent workflow features

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Claude Code feature ecosystem and remote access patterns
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Multi-agent communication via messaging channels
