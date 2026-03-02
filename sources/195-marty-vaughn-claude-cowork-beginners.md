---
source_id: "195"
title: "Claude Co-work: Scheduled Tasks, Connectors, Skills, and Plugins"
creator: "Marty Vaughn"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=GVvEnv0Orl8"
date: "2026-02-28"
duration: "16:43"
type: "video"
tags: ["claude-code", "skills-ecosystem", "enterprise-ai"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 195: Claude Co-work: Scheduled Tasks, Connectors, Skills, and Plugins

> **Creator**: Marty Vaughn | **Platform**: YouTube | **Date**: 2026-02-28 | **Duration**: 16:43

## Summary

A beginner-oriented walkthrough of Claude Co-work's major features: working in local folders via a virtual machine, scheduled/automated tasks, connectors (third-party app integrations), skills (reusable prompt templates), and plugins (bundled collections of skills and connectors). The video demonstrates practical examples including organizing a downloads folder, automated email checking via Gmail connector, expense receipt tracking with Excel formulas, and creating custom skills from successful workflows.

The broader framing positions Co-work as Anthropic's bid to become the middleware between users and their entire application ecosystem. The video highlights six advantages over standard Chat: multi-step task management with to-do lists, direct local file access, sub-agent parallelism, parallel output generation (Excel, PowerPoint, documents), long-running tasks without timeouts, and scheduled autonomous tasks. The practical guidance on when to use Chat vs. Co-work is useful: Chat for quick/cheap queries, Co-work for file operations, complex multi-step tasks, and automation.

## Key Concepts

### Virtual Machine Architecture

Co-work runs as a virtual machine on the user's computer, which enables direct file system access and long-running tasks that do not time out. This is the fundamental architectural difference from Chat — Chat operates purely in the cloud, while Co-work operates locally. The tradeoff is higher token usage and slower startup.

### Scheduled Tasks

Truly autonomous task execution on a schedule (e.g., check email every weekday at noon). Currently requires the computer to be awake. The demonstrated workflow — automated email triage that drafts responses for only important unread emails — shows the practical automation potential. Testing before deployment is essential since permissions and prompt specificity issues only surface at runtime.

### Connectors

Third-party app integrations (Gmail, Google Calendar, Slack, Notion, Canva, Excalidraw, and hundreds more). Each connector exposes specific tools with configurable permissions (always allow, needs approval, blocked). The vision is Co-work as a universal middleware layer connecting users to all their work applications through natural language.

### Skills and Plugins

Skills are reusable prompt templates created from successful workflows — the expense receipt tracker example shows Claude generating a detailed skill from a single successful interaction. Plugins are bundles of skills and connectors organized by department (marketing, finance, legal) that can be shared across teams. This is Anthropic's approach to organizational knowledge capture and distribution.

## Practical Takeaways

- **Test scheduled tasks before deploying**: Permission issues and prompt specificity problems only surface at runtime — always use the "run now" button first.
- **Use Chat for quick tasks, Co-work for complex ones**: Co-work consumes significantly more tokens due to skill file injection and virtual machine overhead.
- **Monitor usage actively**: Co-work can burn through session limits quickly — check Settings > Usage regularly.
- **Create skills from successful workflows**: When a complex prompt works well, immediately save it as a skill to avoid re-engineering the prompt later.
- **Be specific about email filtering**: Specifying "unread" emails (not just "important") prevents the agent from drafting responses to already-handled threads.

## Notable Quotes

> "I imagine that in the near future, Claude Co-work is hoping to be your middleman between you and your work and all of the different apps that you use so you can be as productive as possible." — Marty Vaughn

## Related Sources

- [098: Co-work Explained](098-eliot-prince-cowork-explained.md) — Earlier overview of Claude Co-work capabilities
- [194: Claude Code Skills Explainer](194-claude-skills-explainer.md) — Official Anthropic explainer on skills
- [154: Claude Code Power Features](154-diy-smart-code-claude-code-features.md) — Skills and MCP integration

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills, setup, and context discipline
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Sub-agents and autonomous task execution
