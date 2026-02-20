---
source_id: "105"
title: "How to Use Claude Cowork Better Than 99% of People (Full Guide)"
creator: "Ben AI"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=HTu1OGWAn5w"
date: "2026-01-31"
duration: "21:07"
type: "video"
tags: ["claude-code", "skills", "mcp", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 105: How to Use Claude Cowork Better Than 99% of People (Full Guide)

> **Creator**: Ben AI | **Platform**: YouTube | **Date**: 2026-01-31 | **Duration**: 21:07

## Summary

A comprehensive walkthrough of Claude Cowork — Anthropic's desktop-based agent interface that bridges Claude's chat capabilities with real-world computer actions. The video covers setup, file access, MCP connectors, browser use, skills creation, and code execution. Ben positions Cowork as the middle ground between Claude (brainstorming/Q&A) and Claude Code (production applications), optimized for day-to-day office workflows that need human-in-the-loop iteration.

The most substantive section focuses on skills as the successor to projects, custom GPTs, and system prompts. The key workflow: walk through a task manually with Claude once, then save it as a repeatable skill. Skills load specific instructions and knowledge sources only when triggered, avoiding context window overload. The video demonstrates converting old Claude projects and custom GPTs into Cowork skills and chaining multiple skills within a single context window — a pattern that makes iterative, context-dependent tasks like content creation significantly more repeatable.

## Key Concepts

### Cowork's Position in the Claude Ecosystem

Claude is for brainstorming and Q&A. Claude Code is for building production applications. Cowork is for day-to-day office tasks that require file access, software connections, and repeatable workflows. It inherits planning capabilities from Claude Code and adds folder access, MCP connectors, browser automation, and skills — all through a desktop-only interface requiring a paid subscription.

### Skills as Workflow Automation

Skills are instruction sets with attached knowledge sources that trigger on demand within a conversation. Unlike projects or custom GPTs where you're locked into one context, skills can be combined in a single context window. The pattern: build skills from manual walkthroughs with Claude, from existing system prompts, or from third-party skill marketplaces (Smithery.ai, SkillHub, SkillsMPP). Each skill defines a step-by-step process and only loads its context when invoked.

### The Human-in-the-Loop Sweet Spot

Many day-to-day tasks are too context-dependent and iterative for fully automated n8n/Make.com workflows, but too repetitive for ad-hoc LLM conversations. Skills fill this gap by encoding the process while keeping the human in the loop for decisions — choosing from suggestions, approving steps, iterating on outputs. This makes them superior to rigid automation for content creation, ad copy, newsletters, and similar creative-operational work.

### MCP and Browser Use as Connection Layers

Three ways to connect Cowork to external software: built-in connectors (Notion, etc.), custom MCP servers (set up manually via config.json or through n8n), and browser automation as a fallback for software without APIs or MCPs. Browser tasks can run in the background while working on other tasks.

## Practical Takeaways

- **Convert existing projects to skills**: Copy system prompts and knowledge sources from Claude projects or custom GPTs and ask Claude to create a skill — immediate productivity gain
- **Build skills by doing**: Walk through a task manually with Claude once, then save the conversation as a skill for future repetition
- **Chain skills in one context window**: Unlike projects, multiple skills can be invoked in a single conversation, enabling complex multi-step workflows
- **Use skills marketplaces for starting points**: Smithery.ai, SkillHub, and SkillsMPP have thousands of community-built skills that can be downloaded and customized
- **Background browser tasks**: Browser automation runs in the background, allowing parallel task execution within Cowork

## Notable Quotes

> "I think Cloud Cowork is the next evolution of how we use LLMs, and I think we'll see massive adoption in 2026." — Ben AI

> "I see skills as the next evolution of projects or custom GPTs or system prompts. Skills basically save a specific instruction or process and knowledge sources to best execute a specific task or workflow." — Ben AI

> "For many day-to-day jobs and tasks, we actually need a lot of human in the loop. Many tasks are very context dependent, are iterative, and require a lot of that human in the loop." — Ben AI

## Related Sources

- [063: Ben AI Cowork Plugins](063-ben-ai-cowork-plugins.md) — Earlier coverage of Cowork plugin ecosystem by the same creator
- [066: Brooke Wright Cowork Tutorial](066-brooke-wright-cowork-tutorial.md) — Another Cowork tutorial perspective
- [083: Jack Roberts Cowork Use Cases](083-jack-roberts-cowork-use-cases.md) — Practical Cowork use cases
- [079: Mark Kashef Claude Skills Guide](079-mark-kashef-claude-skills-guide.md) — Skills-focused guide
- [015: IndyDevDan Skills Engineering](015-indydevdan-skills-engineering.md) — Skills system from the Claude Code perspective

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system, context management
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Workflow automation through skills and agent patterns
