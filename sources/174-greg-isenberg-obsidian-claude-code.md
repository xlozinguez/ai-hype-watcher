---
source_id: "174"
title: "Using Obsidian and Claude Code as a Personal Thinking Partner"
creator: "Greg Isenberg"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=6MBq1paspVU"
date: "2026-02-23"
duration: "58:57"
type: "video"
tags: ["claude-code", "context-engineering", "agentic-coding", "prompt-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials", "04-agentic-patterns"]
---

# 174: Using Obsidian and Claude Code as a Personal Thinking Partner

> **Creator**: Greg Isenberg | **Platform**: YouTube | **Date**: 2026-02-23 | **Duration**: 58:57

## Summary

Vinh Nguyen (Internet Vin) demonstrates on Greg Isenberg's podcast how he combines Obsidian — a markdown-based note-taking tool with bidirectional linking — with Claude Code to create a deeply personalized AI thinking partner. The key insight is that the quality of AI output is entirely determined by the quality of context you provide, and a well-maintained Obsidian vault of personal notes, reflections, and project descriptions becomes the richest possible context source for AI agents.

Using the Obsidian CLI, Claude Code can access not just the files in the vault but also the inter-relationships between them (backlinks and graph connections). This enables capabilities that would be impossible for a human to perform manually: tracing how an idea evolved over 13 months across scattered notes, surfacing latent patterns across domains, generating deeply contextual ideas, and challenging the user's own stated beliefs against their actual behavior. The discussion positions Obsidian as the "missing link" between personal knowledge and AI agent capability.

## Key Concepts

### Context Engineering Through Personal Vaults

The central thesis: the better the information an agent has about you, the more it can do for you. Vinh maintains extensive context files for each project and area of his life, which can be loaded into Claude Code with a single command. This eliminates the need to re-explain context in every new session. The vault becomes a persistent, structured, always-available knowledge base that any agent session can draw from — solving the fundamental problem of context loss between AI sessions.

### Custom Claude Code Commands as Workflows

Vinh built a suite of custom slash commands that orchestrate Claude Code's interaction with his vault:
- `/context` — loads full life/work context from multiple files
- `/today` — morning review pulling calendar, tasks, iMessages, and a week of daily notes
- `/close` — end-of-day processing extracting action items and updating confidence markers
- `/trace` — tracks how an idea has evolved over time across the vault
- `/connect` — links two domains using the vault's graph structure
- `/emerge` — surfaces ideas the vault implies but never states
- `/drift` — compares stated intentions against actual behavior over 30-60 days
- `/ideas` — deep vault scan with cross-domain pattern detection

### The Obsidian CLI Bridge

The Obsidian CLI gives Claude Code access to both file contents and inter-relationships (backlinks, graph connections). This is fundamentally different from just giving an agent a folder of files — it adds a semantic layer showing how notes connect. The agent can discover that a file about filmmaking is linked to notes on world-building, Shopify's CEO, and a media company concept, enabling cross-domain pattern recognition that would be impractical for a human to do manually.

### Strict Separation: Human Writes, Agent Reads

Vinh maintains a strict rule: the agent never writes into his Obsidian vault. He only wants the agent to find patterns in what he has written, not what it has written. If the agent starts creating files in the vault, pattern detection becomes contaminated — you cannot tell if it is surfacing your patterns or its own. The agent writes output to a separate space, and Vinh decides what gets incorporated.

### From Reflection to Building

The workflow moves from personal reflection to actionable output. The `/ideas` command scans the entire vault and generates categorized suggestions: tools to build, systems to implement, subjects to investigate, conversations to have, and things to publish. It even suggested building a `/graduate` command to promote ideas from daily notes into standalone notes — and then Claude Code built that command on the spot.

## Practical Takeaways

- **Feed agents files, not repeated explanations**: Write project descriptions and preferences into markdown files once, then reference them in every Claude Code session
- **Use Obsidian's backlinks as a semantic layer**: The inter-relationships between notes give agents dramatically richer context than a flat folder of files
- **Build custom commands for recurring workflows**: One-command context loading eliminates session startup friction
- **Keep vault authorship strictly human**: Never let agents write into your primary knowledge base — maintain clean signal for pattern detection
- **Expect longer response times with deep context**: Vault-aware commands take significantly longer as Claude Code reads many interconnected files, but the output quality justifies the wait
- **Let the agent suggest its own improvements**: Ask Claude Code what commands would be most useful based on what it knows about you, rather than only inventing commands yourself

## Notable Quotes

> "The quality of information that the agent has entirely determines what it can do for you. If it doesn't know a lot about you, it's not going to be able to do a lot for you." — Vinh Nguyen

> "I want to maintain that and make it as current and as deep as possible. So whenever I'm talking to an agent, it has the best representation at all times of who I am in that moment." — Vinh Nguyen

> "If you are serious about using LLMs to take your ideas and get the most out of them, and you are not using a centralized note-taking tool that uses markdown as the foundation, then you are not using LLMs properly." — Greg Isenberg

## Related Sources

- [176: OpenClaw Chaos and the State of AI Personal Assistants](176-primetime-openclaw-assistant-chaos.md) — Contrasting perspective on personal AI assistant risks

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Context-driven prompt design and sticky workflows
- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Claude Code setup, context files, and skills system
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Custom command creation and agent-vault integration patterns
