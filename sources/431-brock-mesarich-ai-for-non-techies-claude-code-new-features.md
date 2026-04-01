---
source_id: "431"
title: "All 4 NEW Claude Cowork Features Explained (and how to master them)"
creator: "Brock Mesarich | AI for Non Techies"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=TU5GBkyuOSs"
date: "2026-03-31"
duration: "23:23"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "task-system", "meta-prompts"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 431: All 4 NEW Claude Cowork Features Explained (and how to master them)

> **Creator**: Brock Mesarich | AI for Non Techies | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 23:23

# All 4 New Claude Code Features Explained

## Summary

This video walks through four recently released Claude Code (referred to as "Co-work" throughout) features: Projects, Scheduled Tasks, Dispatch (mobile control), and Computer Use. The presenter frames these features as transforming Claude from a simple chatbot into a persistent, autonomous work environment that remembers context, runs background automations, and can be controlled remotely from a phone.

The core argument is that most users are dramatically underutilizing Claude by treating it as a stateless Q&A tool. Projects solve the memory and organization problem by giving Claude a persistent workspace with custom instructions, files, and conversation history. Scheduled Tasks replace simple automation tools like n8n for non-technical users. Dispatch enables remote task delegation from mobile, while Computer Use gives Claude direct control over desktop applications.

The video is pitched at non-technical users and stays at a conceptual/demo level rather than deep technical implementation. Its value is in illustrating real-world workflows (morning briefings, YouTube analytics tracking, competitor scans, daily wrap-ups) rather than novel technical insights. The "hack" teased in the intro is the Skills system combined with Projects — using reusable workflow prompts triggered on a schedule.

---

## Key Concepts

### Projects as Persistent Memory Contexts
Claude Code Projects create isolated workspaces that maintain memory across sessions — storing custom instructions, files, and conversation history in one place. This solves the statelessness problem that makes CLAUDE.md files unwieldy: rather than cramming all context into a single global file (which loads on every conversation and eats context window), Projects scope memory to specific domains (e.g., one project for YouTube content, another for a client agency). Projects can be created from scratch, imported from existing Claude.ai projects, or pointed at an existing local folder.

### Scheduled Tasks as No-Code Automation
Claude Code now supports native scheduled task execution — recurring automations (hourly, daily, weekly, manual trigger) that run skills or workflows without external tools like n8n or Zapier. Practical examples include: morning email/calendar briefings with drafted replies, YouTube analytics scrapers that log video performance to spreadsheets, competitor content tracking, and end-of-day wrap-up reports. This lowers the barrier to automation for non-technical users who previously needed to configure multi-node workflow tools.

### Dispatch: Asynchronous Mobile-to-Desktop Control
Dispatch creates a persistent, shared conversation thread between the Claude mobile app and the desktop Claude Code instance. Users can send task instructions from their phone; Claude executes them on the desktop (with access to local files, browser, and computer controls) and sends push notifications on completion. Context is continuous — the same thread exists across both surfaces. Requires the "keep awake" toggle enabled so the desktop app doesn't sleep between tasks.

### Skills as Reusable Workflow Units
Skills are pre-written workflow prompts that encode entire multi-step processes into a single invocable unit. They give Claude the "how" knowledge for complex tasks (e.g., how to scrape YouTube data and format it into a spreadsheet) so scheduled tasks and Dispatch commands can be terse. The presenter references a library of 50+ personal skills. This concept maps directly to the skills/meta-prompts pattern: encode complexity once, invoke cheaply thereafter.

---

## Practical Takeaways

- **Segment your CLAUDE.md context with Projects** — instead of one bloated global instructions file, create separate projects per domain/client/content type to avoid context window exhaustion and keep instructions relevant to the task at hand.
- **Start with three high-value scheduled automations**: a morning briefing (email + calendar + drafted replies), a weekly data-pull report from Google Drive, and an end-of-day work summary — these deliver immediate time savings with minimal setup.
- **Enable "keep awake" in Dispatch settings** before relying on mobile-triggered tasks; the desktop app must remain active for any background or remote execution to work.
- **Combine Projects + Skills + Scheduled Tasks** as the core power pattern: Projects provide persistent context and memory, Skills encode the workflow logic, and Scheduled Tasks execute them without manual intervention.
- **Import existing Claude.ai projects into Claude Code** to instantly carry over accumulated context and instructions rather than rebuilding from scratch.

---

## Notable Quotes

> "Without a project, Claude basically forgets who you are. It doesn't remember what you told it yesterday, doesn't have access to your previous conversations, and has no idea what you or your business does."

> "You don't want to have a fully bloated CLAUDE.md file because that's loaded every time you have a conversation with it and you could then hit your context window extremely fast."

> "This isn't just having Claude browse the internet for you answering questions. This is giving Claude actual capabilities to make changes to the folders on your computer."

---
