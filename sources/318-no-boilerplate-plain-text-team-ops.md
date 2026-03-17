---
source_id: "318"
title: "The Unreasonable Effectiveness Of Plain Text"
creator: "No Boilerplate"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=WgV6M1LyfNY"
date: "2023-10-13"
duration: "14:37"
type: "video"
tags: ["specification", "ai-sdlc", "context-engineering", "enterprise-ai"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 318: The Unreasonable Effectiveness Of Plain Text

> **Creator**: No Boilerplate | **Platform**: YouTube | **Date**: 2023-10-13 | **Duration**: 14:37

# The Unreasonable Effectiveness Of Plain Text

## Summary

This video argues that the single most effective organizational improvement a tech team can make is standardizing all documentation, project management, and communication artifacts on plain text files — specifically Markdown stored in Git repositories. The core thesis is that the "Ulysses Pact" framework applies here: by deliberately constraining your toolset to plain text now, you protect your future team from the constant churn of adopting new productivity tools, each of which fragments institutional knowledge and erodes the motivation to document anything at all.

The video walks through a practical implementation using GitHub as the foundation: wikis for documentation, issues and milestones for lightweight project management, project boards as minimal kanban, pull requests for change review, and GitHub Actions for automation. The argument is that this stack covers 90% of team needs with a fraction of the complexity of specialized tools like Jira, Confluence, or Notion — and crucially, the data remains portable, offline-accessible, and permanently readable.

While the video predates the current wave of AI-assisted development, its insights are directly applicable to AI-native workflows: plain text Markdown is the format AI models read and write most naturally, Git provides the audit trail and diff visibility that agentic workflows require, and the offline/local-first nature of Git repos aligns perfectly with how tools like Claude Code and Cursor operate against local file systems.

## Key Concepts

### The Ulysses Pact as a Tool Selection Framework
Tris uses Odysseus tying himself to the mast as a metaphor for making a binding commitment to a constrained toolset *before* you are tempted to abandon it. The insight is that tool churn is predictable and damaging — every new project management or documentation tool takes teams off the same page, makes existing documentation feel "legacy," and disincentivizes future documentation. Standardizing on plain text is a pre-commitment device that prevents this failure mode.

### Plain Text as Permanent, Portable Data
Unlike proprietary app formats (Notion databases, Jira tickets, Confluence pages), plain text Markdown files are readable by any tool now and in the future, exportable without vendor lock-in, and editable offline. The video frames this as a compounding advantage: instead of institutional knowledge becoming *less* valuable over time as tools deprecate, plain text data becomes *more* valuable as the network of tooling around Markdown grows.

### Git/GitHub as a Minimum Viable Team Operating System
The video proposes a complete team infrastructure using only GitHub primitives: repos for project structure, wikis for documentation, issues for task capture, milestones for deadlines, project boards for kanban visualization, pull requests for change review with audit trails, and Actions for automation. The key insight is that this stack avoids the "Jira effect" — when a tool has burndown charts, velocity points, and time tracking, teams feel compelled to use all features even when they add no value.

### Internal Open Source as a Default Permission Model
Rather than restricting access by default and managing permissions as overhead, the video recommends giving all team members write access to all repositories — the "internal open source" pattern. This captures network effects (more contributors, more cross-pollination), reduces administrative overhead, and treats trust as the default rather than the exception.

### Offline-First as a Superpower
When all company data lives in Git repositories, every file is available locally. This enables bulk operations (find-and-replace across 10,000 files), fast search without API round-trips, and resilience to service outages. The video contrasts this with fragmented SaaS stacks where a basic find-and-replace across a Google Drive is impossible — and notes that the reason is likely deliberate, since rollback from such an operation would be manual and catastrophic in a non-versioned system.

## Practical Takeaways

- **Use GitHub's built-in primitives before reaching for specialized tools**: wikis before Confluence, issues/milestones before Jira, project boards before Trello. Upgrade to specialized tools only when you have a concrete, demonstrated need the simpler tool cannot meet.
- **Write down decisions and get confirmation**: after any meeting or discussion, document what was concluded and have the other party confirm it. The ADR (Architecture Decision Record) format is specifically recommended for technical decisions.
- **Run standups by walking the board right-to-left**: focus on work in progress and blockers rather than asking what people did yesterday. Time-box strictly. Eliminate the scrum master as a permanent role — it's a rotating hat.
- **Automate via GitHub Actions against plain text inputs**: spell checking on PR, image resizing, audio processing, document validation — any repeatable quality check can be enforced as a PR gate, removing human error from routine quality control.
- **Treat "regression to the mean" as an active threat**: even good teams adopting good tools will drift toward complexity over time. The Ulysses Pact framing means the decision to stay on plain text should be explicit and documented, not just a default that erodes.

## Notable Quotes

> "In order to do more you must have the discipline to do less."

> "Tying yourself to the mast by standardizing on one tool and not only that but a plain text tool means your data will live forever and the network effect can make it more and more valuable over time instead of less and less."

> "If you have a tool that is packed full of time tracking, velocity points, and so on, the temptation is to use all these features even if they give no value and complicate your process."
