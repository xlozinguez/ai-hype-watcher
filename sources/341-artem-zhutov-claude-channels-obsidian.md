---
source_id: "341"
title: "Claude Code + Obsidian: 100 Skills From Your Phone (Channels Setup)"
creator: "Artem Zhutov"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=9G6IPxSXU8s"
date: "2026-03-21"
duration: "22:23"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "multi-agent", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 341: Claude Code + Obsidian: 100 Skills From Your Phone (Channels Setup)

> **Creator**: Artem Zhutov | **Platform**: YouTube | **Date**: 2026-03-21 | **Duration**: 22:23

## Summary

Artem Zhutov demonstrates how Anthropic's new Channels feature enables remote interaction with Claude Code sessions running inside an Obsidian vault, accessible from a phone via Telegram or Discord. The core insight is that running Claude Code from within an Obsidian vault gives the agent access to 100+ skills, extensive CLAUDE.md context, and memory files -- all of which make it far more capable than a generic chatbot. The video covers setup for both Telegram and Discord channels, a loop-based pattern for proactive scheduled agents, an orchestrator pattern using tmux workspaces, and a detailed comparison with OpenClaw.

The demo shows practical examples including generating diagrams and PDFs from Discord, running Reddit sentiment analysis via custom skills, setting up scheduled automation (cron-style loops for periodic reports), and using tmux-based orchestration to spawn and manage multiple Claude Code workspaces from a single Discord channel.

## Key Concepts

### Channels as Mobile Bridge to Local Agent Context
The fundamental value proposition: Claude Code running from an Obsidian vault has rich personal context (skills, memory, CLAUDE.md, notes) that makes it a powerful personal assistant. Channels bridges the gap between this local, context-rich agent and mobile accessibility. The agent is not a generic chatbot -- it knows the user's writing voice, file organization, personal preferences, and has access to 150+ packaged skills.

### OpenClaw vs. Claude Code + Channels Comparison
Zhutov provides a detailed comparison. OpenClaw advantages: 23+ platform integrations (WhatsApp, Signal, etc.), built-in heartbeats, a skills marketplace. Claude Code + Channels advantages: deeper observability (you can read any skill's markdown source), subscription-based pricing (Claude Max at $200/month provides token usage worth thousands in API costs), Opus model access (better "vibes" for personal assistant use than OpenAI models), and the ability to inspect and tune skills directly in Obsidian.

### Loop Pattern for Proactive Agents
A built-in loop skill enables cron-style scheduling: set an interval (hours, minutes) and a prompt or skill to execute. Examples include a therapy-style check-in every 2 hours, a Reddit/Twitter/YouTube source analysis every 8 hours, or a morning briefing at 7:00 AM that scans previous day's notes. This transforms Claude Code from reactive (waits for user input) to proactive (autonomously performs tasks on schedule).

### Tmux Orchestrator Pattern
For multi-agent workflows before native Discord channel isolation is available, Zhutov uses a tmux-based approach: one "orchestrator" agent runs in the main workspace and can spawn additional workspaces (e.g., "weekly-plan") via a tmux skill. The orchestrator reads the screen of sub-workspaces to monitor their progress and can report status back to Discord. This is a practical workaround for the current limitation of one Claude Code session per channel.

### Observability Gap and Mitigation
A key concern: when an agent runs in the background processing a request from a mobile device, there is no visibility into what it is doing until it produces a final result. If it goes off track, there is no way to interrupt or redirect. Zhutov suggests instructing the agent to use the MCP reply command to send progress notifications before major actions -- a crude but functional observability layer.

## Practical Takeaways

- **Run Claude Code from your Obsidian vault for maximum context**: The vault provides skills, memory, CLAUDE.md, and notes that transform a generic agent into a personalized assistant
- **Claude Max subscription provides significant token subsidy**: Zhutov estimates $200/month provides thousands of dollars worth of API-equivalent token usage, though notes this is "heavily subsidized" and may not last
- **Use loop skills for proactive automation**: Schedule recurring tasks (source scanning, morning briefings, periodic check-ins) without manual intervention
- **Package completed work as skills**: After finishing a task in a Claude Code session, package the workflow as a reusable skill -- this compounds over time and makes each future session more capable
- **Treat agent output formatting as a training problem**: Expect to iterate on how agents deliver results (inline markdown vs. file attachments vs. chat messages) -- "you need to be very patient with those agents to teach them the way you want results to be produced"

## Notable Quotes

> "The one thing I couldn't do is to reach it from my phone, and now with the channels I can." — Artem Zhutov

> "The problem with OpenAI models is that their vibes are just not great. They're not really great for personal assistant." — Artem Zhutov

> "When agent is working I don't really see what's happening... I can't control it, I can't stop it, I just have to guess." — Artem Zhutov

## Related Sources

- [337: Code Agents, AutoResearch, and the Loopy Era of AI](337-karpathy-code-agents-autoresearch.md) — Karpathy's "Dobby the elf claw" is the same pattern: persistent agent entity accessible via messaging
- [342: Vibe Coding Is Broken. This Claude Code Framework Fixes It.](342-charlie-automates-claude-code-framework.md) — complementary approach to skills and framework organization in Claude Code

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md, skills, and memory as the foundation for powerful agent workflows
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — loop patterns, orchestrator agents, and tmux-based multi-workspace management
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — multi-agent coordination through Discord channels and tmux workspaces
