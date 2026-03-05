---
source_id: "206"
title: "Building a Persistent AI Second Brain with Obsidian and Claude Code"
creator: "Noah Vincent"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=BLdO-32I6Yc"
date: "2026-02-27"
duration: "35:11"
type: "video"
tags: ["claude-code", "context-engineering", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows"]
---

# 206: Building a Persistent AI Second Brain with Obsidian and Claude Code

> **Creator**: Noah Vincent | **Platform**: YouTube | **Date**: 2026-02-27 | **Duration**: 35:11

## Summary

Noah Vincent presents a system for using Claude Code directly inside an Obsidian vault to create a persistent, context-aware AI workspace. The core argument is that generic AI output stems not from bad prompts but from lack of accumulated context --- every chat session starts from zero, and built-in memory features from AI providers are unstructured and unreliable. By running Claude Code inside a local folder of markdown files, the AI reads CLAUDE.md and memory.md at startup and immediately knows who you are, what you are building, and what you have done in past sessions.

The video walks through terminal basics (pwd, ls, cd), installing and launching Claude Code, and the two files that power the system: CLAUDE.md (persistent identity, project structure, writing rules) and memory.md (session log of decisions and patterns). Vincent demonstrates live use cases including searching a 500-note Zettelkasten, generating a newsletter from vault content, and converting ad-hoc workflows into reusable Claude Code skills. He also covers MCP connections to external tools like Things (task management) and Tana (voice note capture), and addresses security concerns around prompt injection and supply chain attacks on MCP servers.

The system costs roughly $20/month (Obsidian is free, Claude Pro subscription covers usage), which Vincent contrasts favorably against API-token-based alternatives and proprietary platforms like Notion that charge margins on top of AI usage.

## Key Concepts

### The Context Persistence Problem

Every AI session starts from zero. Built-in memory systems from Claude and ChatGPT save arbitrary snippets without hierarchy, structure, or editorial judgment. They mix contexts across projects and surface irrelevant information. The solution is to put the AI inside your knowledge system rather than going to the AI --- Claude Code opens inside your vault and reads your notes, projects, and context from the first prompt.

### CLAUDE.md and memory.md as Compounding Context

CLAUDE.md is read at every session startup and contains identity, project structure, writing rules, and guidelines. It can be nested per-folder for scoped context (e.g., a separate CLAUDE.md inside an SOPs directory). Memory.md records key decisions, patterns, and actions after every session, providing continuity across conversations. After five sessions Claude knows your projects and voice; after twenty it becomes a personalized operating system that knows more about your knowledge base than you consciously remember.

### Skills as Repeatable Workflows

Any workflow built interactively with Claude Code can be converted into a permanent slash command. Vincent demonstrates creating a `/newsletter` skill live: Claude reads the existing SOP template, creates a full agent definition with eight steps (search, confirm, calibrate, read, plan, write, generate metadata, assemble), and saves it as a callable skill. This turns the system into a self-extending toolkit where every solved problem becomes a reusable automation.

### MCP for External Tool Integration

MCP (Model Context Protocol) connects Claude Code to external apps beyond the local vault. Vincent uses it with Things (task management) and Tana (voice note capture/transcription). He demonstrates a voice-note-to-newsletter pipeline that fetches from Tana, translates from French, formats, and saves to the vault. He warns about prompt injection risks and supply chain attacks, recommending self-hosted MCPs, disabled auto-updates, and restricting Claude Code to the vault folder only.

## Practical Takeaways

- **Context beats prompts**: Invest time in building CLAUDE.md and memory.md rather than perfecting individual prompts --- accumulated context produces better output than clever one-off instructions.
- **Nest CLAUDE.md files per folder**: Scope context to specific project areas so Claude loads relevant instructions when navigating into subdirectories.
- **Convert workflows to skills**: After completing any multi-step workflow interactively, ask Claude to write an SOP and create a skill command so the process becomes one-shot repeatable.
- **Self-host MCPs and restrict permissions**: Avoid third-party MCP servers you do not control; disable auto-updates to prevent supply chain attacks; only open Claude Code inside the vault folder, never at the system root.
- **Use the terminal shortcut**: Right-click a folder in Finder and select "New Terminal at Folder" to skip manual navigation.

## Notable Quotes

> "Most people blame the prompt, but the prompt isn't the problem. Context is everything when it comes to having good AI output." — Noah Vincent

> "After five sessions Cloud knows your projects, your voice, your preferences, your standards better than most collaborators will." — Noah Vincent

> "Every workflow you build becomes a permanent callable command. The system grows in capability the more you use it." — Noah Vincent

## Related Sources

- [174: Greg Isenberg on Obsidian and Claude Code](174-greg-isenberg-obsidian-claude-code.md) — Another perspective on the Obsidian + Claude Code combination
- [040: Charlie Automates on CLAUDE.md Context](040-charlie-automates-claudemd-context.md) — Deep dive into CLAUDE.md configuration
- [084: Dylan Davis on Context Rot and the 60% Rule](084-dylan-davis-context-rot-60-rule.md) — Context management challenges in long sessions
- [013: Leon van Zyl on Claude Code Skills](013-leon-van-zyl-claude-code-skills.md) — Skills creation and usage patterns

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLAUDE.md configuration, skills creation, context discipline
- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Context engineering over prompt engineering
