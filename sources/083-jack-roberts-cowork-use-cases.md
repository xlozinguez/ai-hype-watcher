---
source_id: "083"
title: "5 INSANE Claude CoWork use cases (Build Anything)"
creator: "Jack Roberts"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=EZdSVpgtjG0"
date: "2026-02-16"
duration: "26:08"
type: "video"
tags: ["claude-code", "skills", "mcp", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 083: 5 INSANE Claude CoWork use cases (Build Anything)

> **Creator**: Jack Roberts | **Platform**: YouTube | **Date**: 2026-02-16 | **Duration**: 26:08

## Summary

Jack Roberts delivers a practical walkthrough of Claude Cowork (Anthropic's desktop agent product), demonstrating five progressively more powerful use cases: file management, browser automation, service connectors (Gmail, Calendar, Fireflies, Canva, Notion), skills creation, and plugins. The video is aimed at entrepreneurs and non-technical business users, positioning Cowork as a "500 IQ personal assistant" rather than a coding tool.

The most interesting pattern Roberts demonstrates is the iterative skill-building workflow: start by having Claude perform a task manually (e.g., grab a YouTube transcript and turn it into a newsletter), refine the output through conversation, and then enshrine the refined process as a reusable skill. He also draws a useful distinction between Cowork (an assistant that uses your computer and logins to do day-to-day tasks) and Antigravity/Claude Code (a developer that builds custom software). The video surfaces both genuine capability -- multi-MCP chaining across Fireflies and Notion, browser-based Canva editing -- and speed limitations that Roberts acknowledges.

## Key Concepts

### Cowork vs. Code: The Assistant vs. Developer Framing

Roberts frames the distinction clearly: Antigravity/Claude Code is "hiring a developer to build you custom software," while Cowork is "hiring an assistant who uses your computer, your files, your logins and does the work for you." Both automate workflows, but they target fundamentally different use cases. Cowork excels at day-to-day operational tasks that require browser interaction and service access.

### Iterative Skill Creation from Manual Workflows

The most valuable pattern demonstrated is a three-step workflow: (1) have Claude perform a task through conversation, iterating until the output quality is satisfactory, (2) refine rules and style preferences through back-and-forth dialogue, (3) enshrine the entire process as a skill for autonomous future execution. This mirrors the prompt-engineering-to-automation pipeline seen in developer workflows.

### Multi-Connector MCP Chaining

Roberts shows Claude pulling meeting action items from Fireflies (via MCP connector), then creating a Notion document with those items -- chaining two different service connectors in a single workflow. This demonstrates MCP's promise as a universal integration layer for non-technical users, though the setup still requires connector configuration.

### Browser Automation as API Bypass

When API access isn't available, Cowork's browser automation acts as a universal fallback -- navigating YouTube to scrape comments, editing Canva designs, and downloading files. Roberts notes this is "a little bit slow" but powerful for services without API access.

## Practical Takeaways

- **Start manual, then automate**: Build skills by first doing the task conversationally with Claude, refining through feedback, then saving as a skill
- **Use connectors to chain services**: Gmail + Calendar + Fireflies + Notion can be orchestrated through a single Claude Cowork conversation
- **Browser automation fills API gaps**: When no API exists, Cowork can navigate the browser to accomplish tasks -- slower but functional
- **Plugins bundle skills + connectors**: Multiple related skills and their required connectors can be packaged as a shareable plugin
- **Break complex tasks into steps**: Roberts emphasizes that "the more tasks we give to an AI, the worse it performs" -- decompose into title, opening line, body, etc.

## Notable Quotes

> "Antigravity is like hiring a developer to build you custom software. Whereas Cloud Co-work is like hiring an assistant who uses your computer, your files, your login and does the work for you." — Jack Roberts ([01:45](https://www.youtube.com/watch?v=EZdSVpgtjG0&t=105))

> "Typically speaking, the more tasks that we give to an AI, the worse it performs. So, we're going to break this down step by step." — Jack Roberts ([16:26](https://www.youtube.com/watch?v=EZdSVpgtjG0&t=986))

> "We're only really limited by our imagination." — Jack Roberts ([12:20](https://www.youtube.com/watch?v=EZdSVpgtjG0&t=740))

## Related Sources

- [063: Claude Cowork Just Became 10x Better (Plugins Guide)](063-ben-ai-cowork-plugins.md) — Complementary deep-dive on Cowork plugins system
- [066: How to use Claude Cowork better than 99% of people](066-brooke-wright-cowork-tutorial.md) — Another Cowork tutorial with different use cases
- [013: Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) — Skills system from the developer perspective
- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) — Technical skills engineering contrasting with Roberts' non-technical approach
- [043: Claude Code just replaced your ad agency](043-agrici-daniel-claude-ad-agency.md) — Similar pattern of using Claude skills for content creation workflows

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system and MCP connectors fundamentals
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Skill creation as a form of agentic automation pattern
