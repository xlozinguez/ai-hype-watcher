---
source_id: "460"
title: "Codex Plugins - are they any good?"
creator: "Gareth Jones"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=RkyWtx9-UI4"
date: "2026-03-29"
duration: "39:01"
type: "video"
tags: ["skills", "skills-ecosystem", "specification", "meta-prompts", "agentic-coding", "chatgpt"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "02-prompting-and-workflows"]
---

# 460: Codex Plugins - are they any good?

> **Creator**: Gareth Jones | **Platform**: YouTube | **Date**: 2026-03-29 | **Duration**: 39:01

# Codex Plugins — Are They Any Good?

## Summary

Gareth Jones walks through a live session building and packaging a Codex plugin called "Jones Mode" — a bundle of three personal workflow skills (Grill Me, Write PRD, and PRD-to-Issues) intended to make it easier to port his AI-assisted development patterns across machines and projects. The session is raw and exploratory, with Jones navigating incomplete documentation in real time, demonstrating both the appeal and the friction of the Codex plugin system as it exists in early 2026.

The core workflow Jones is assembling reflects a deliberate, planning-heavy approach to agentic coding: start with intensive AI-driven questioning (Grill Me), produce a lightweight requirements document (Write PRD), then decompose that into GitHub issues (PRD-to-Issues) for the agent to work against. His preference for GitHub Issues as the record of work — rather than direct file manipulation — is a recurring architectural choice, offering abstraction, editability, and a place to add comments that the agent can consume.

The video is as much a product review as a tutorial. Jones surfaces genuine usability complaints about Codex: unclear plugin invocation syntax compared to Claude Code, an Electron app that doesn't support VPS workflows, and changelogs that don't accompany daily updates. He concludes with a working plugin installation and a partial demo of skill invocation, giving a realistic picture of where Codex plugins are useful and where the developer experience still needs work.

## Key Concepts

### Codex Plugins as Skill Distribution Packages
Codex plugins are described as a packaging mechanism for bundling skills, MCPs, and callable functions into a portable, installable unit. Jones frames them as a solution to a real portability problem: he runs multiple machines and a VPS, and previously had to clone GitHub repos or use submodules to carry his skill definitions around. Plugins offer a cleaner distribution path, though the installation UX is still rough and documentation is sparse on the sharing/consumption flow.

### The "Jones Mode" Planning Stack (Grill Me → Write PRD → PRD-to-Issues)
Jones's plugin bundles three sequentially-used skills that encode his planning philosophy:
- **Grill Me**: Instructs the model to "interview the user relentlessly" about every aspect of a feature, exploring the codebase when a question can't be answered from conversation alone. This front-loads thinking before any code is written.
- **Write PRD**: Guides production of a lightweight requirements document covering problem framing, user stories, and eventual GitHub issue creation.
- **PRD-to-Issues**: Takes the requirements document and decomposes it into discrete GitHub Issues, each representing an implementation task for the agent.

The stack reflects a specification-first philosophy where the agent's working context is shaped by structured planning artifacts rather than ad-hoc prompts.

### GitHub Issues as Agent Work Records
A notable architectural preference in Jones's workflow is using GitHub Issues — rather than files on disk — as the primary record of planned work. He argues this offers: (1) native editing UI outside the repo, (2) a place to capture agent comments and context, and (3) a useful abstraction layer when a model struggles with a specific problem, allowing it to riff on an issue ticket rather than directly on a codebase file.

### Model Selection and Cross-Tool Tradeoffs
Jones uses GPT-4.5 (referred to as "GBD5.4") with extended thinking for this session, explicitly noting it performs well on coding problems despite his general appreciation for Claude models. He observes that switching from Claude Code to Codex requires remembering different invocation syntax (the `$` prefix for skills), and that Codex's daily update cadence without in-app changelogs creates unnecessary friction. The Mac desktop app's Electron architecture and lack of VPS support are cited as reasons he hasn't fully adopted it.

### Plugin Scaffolding and Documentation Gaps
Jones uses a "plugin creator" skill to scaffold the Jones Mode plugin, going through a live plan-then-execute loop. He encounters gaps where the documentation doesn't lead with the most common user journey (install → share → consume) and has to infer the correct directory structure (`~/.local/share/codex/plugins` or equivalent) from context. His observation: the docs optimize for creation over consumption discovery, which may be backwards given that plugin sharing/distribution is the primary value proposition.

## Practical Takeaways

- **Front-load planning with a "relentless interviewer" skill**: Even a minimal skill prompt — "interview me relentlessly, explore the codebase if I can't answer" — meaningfully improves the quality of work that follows by surfacing assumptions before code is written.
- **Use GitHub Issues as the agent's task surface**: Abstracting planned work into Issues (rather than inline comments or local files) gives you editability, threading, and a persistent context artifact the agent can reference across sessions.
- **Package personal workflows as plugins early**: Even simple skill bundles become high-value when you work across multiple machines or share with a team. The portability benefit compounds with the number of machines/collaborators.
- **Expect documentation lag on new plugin features**: Codex plugin docs (as of early 2026) don't clearly surface the install-from-local-path workflow. Budget time to experiment with directory structure or query the agent directly about config paths.
- **Validate plugin JSON files immediately after scaffolding**: The plugin creator skill outputs two JSON manifests; Jones confirms both should pass validation before attempting installation. Catching a typo (e.g., "grill me" vs "grillme") at this stage saves debugging time later.

## Notable Quotes

> "I spend a lot of time on planning… I find it really useful to spend quite a bit of concentrated time with a model at the start."

> "It's useful to sort of have that abstracted somewhere else [GitHub Issues]. Rather than have it riff on an individual file on a machine — you can add comments and a bunch of other stuff to it that will pull down."

> "How is this so big? I assume it's an Electron app, similar to Slack. I would much prefer it just be a Swift native application — I just think it's going to be more performant on my machine."
