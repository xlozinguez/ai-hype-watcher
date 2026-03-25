---
source_id: "359"
title: "The Library Meta-Skill: How I Distribute PRIVATE Skills, Agents and Prompts"
creator: "IndyDevDan"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=_vpNQ6IwP9w"
date: "2026-03-16"
duration: "26:32"
type: "video"
tags: ["skills", "claude-code", "agent-teams", "multi-agent", "meta-prompts", "agentic-coding", "security"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 359: The Library Meta-Skill: How I Distribute PRIVATE Skills, Agents and Prompts

> **Creator**: IndyDevDan | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 26:32

# The Library Meta-Skill: Distributing Private Skills, Agents, and Prompts

## Summary

IndyDevDan presents a solution to a coordination problem that emerges when engineers work across 10+ codebases with AI agents: skills, agents, and prompts get duplicated, fall out of sync, and become impossible to coordinate across team members and devices. His answer is a "library" meta-skill — a single YAML-based reference file (analogous to `package.json`) that points to GitHub repositories or local file paths rather than storing copies of the artifacts themselves. Because it stores pointers rather than content, staying synchronized across projects, teammates, and devices reduces to syncing one file.

The system is explicitly agent-first: there is no traditional code execution engine — the library is itself a Claude Code skill that an agent runs. The workflow is: **build** a prompt/skill/agent inside its native value-generating repo → **catalog** it by adding a reference to the library YAML → **distribute** by running `library.use` in any new project or device → **sync** to pull the latest versions from source. The video demonstrates this live between a local Mac and a Mac Mini agent device, showing how the meta-skill clones referenced repos and installs artifacts into `.claude/skills`.

A key design principle is privacy. The author stresses that high-value specialized skills and agents should live in private GitHub repos, not public ones. The library file itself can be public (it's just pointers), but the referenced content stays private. This architecture is positioned as foundational infrastructure for teams running agent fleets across multiple devices and domains — a pattern the author predicts will become increasingly common as engineers move from single agents to coordinated agent teams.

## Key Concepts

### The Library as a Package Manager for Agentics
The core abstraction mirrors familiar dependency management: a single YAML file stores references (GitHub URLs or local paths) to skills, agents, and prompts — never the artifacts themselves. Just as `package.json` doesn't contain npm packages, the library file doesn't contain skill code. This means updates to source repos propagate everywhere with a single `library.sync` command, eliminating the copy-paste drift that plagues multi-repo agentic setups.

### Meta-Skill Architecture
A meta-skill is a skill that unlocks or coordinates other skills — a higher-order capability. The library skill exposes a small API: `add`, `use`, `push`, `list`, `search`, and `sync`. Critically, this is a pure agentic solution with no backing runtime code; the agent itself interprets and executes these commands. This positions the pattern as an early example of what the author predicts will be a broader category of "pure agentic solutions" — functionality delivered entirely through skilled agents rather than traditional software.

### Three Agentic Primitives: Skills, Agents, Prompts
The author draws a clear distinction between the three building blocks: **skills** are raw capabilities (discrete, reusable tool actions); **agents** provide scale and parallelism (autonomous actors that can run concurrently); **prompts** are single-file orchestration instructions that coordinate the layers below. A common mistake is overloading skills with logic that should live in agents or prompts. The library is designed to manage all three as distinct artifact types.

### Private Distribution as a First-Class Concern
The system is explicitly designed around private GitHub repositories. High-value, specialized agentic tooling represents competitive IP and should not be publicly distributed. The architecture separates the shareable reference layer (the library YAML, which can be public) from the proprietary content layer (the actual skill/agent/prompt repos, which stay private). Team members and agents only need git access to the private repos — the library file handles discovery and installation.

### Build-in-Place, Reference-and-Reuse
A deliberate workflow principle: don't interrupt native development by building skills in a separate "library repo." Build skills, agents, and prompts inside the value-generating repository where they're first needed. Once stable, catalog them by adding a reference to the library. This preserves development flow while enabling later reuse. The library acts as a registry layer on top of existing repos rather than a migration destination.

## Practical Takeaways

- **Create one library YAML per team/domain**, not per project. Store it in its own repo alongside the library meta-skill. Think of it as your team's `package.json` for agentic tooling — everyone clones it, runs `library.sync`, and gets the latest skills/agents/prompts instantly.
- **Keep private skills in private repos.** Use the library's reference mechanism to point at private GitHub URLs. Team members and agents authenticate via their existing git credentials — no special infrastructure required.
- **Run `library.sync` as part of agent bootstrapping.** When spinning up an agent on a new device or cloud sandbox, the first step should be syncing the library to ensure the agent has access to all current team capabilities.
- **Distinguish the library engineer repo from the library reference repo.** The former contains the actual reusable skill/agent/prompt files; the latter is just the YAML pointer file plus the meta-skill. Keeping them separate makes it easy to have multiple domain-specific libraries (e.g., sales, support, infra) pointing at shared or specialized source repos.
- **Treat the `library.use` command as installation.** Running it clones the referenced source and places artifacts in `.claude/skills` (or equivalent). This means you can add agent capabilities to any project in a single agent command without manual file copying.

## Notable Quotes

> "We have one skill to unlock them all. I want a coordinated solution to distribute my agentics over and over and over across my devices, teams, and agents."

> "I know a lot of vibe coders, you think that everything is just out there in the public. Trust me, it's not. We need a way to distribute this privately."

> "It's not having an agent run rampant on your device. It's having a team of agents that can operate very very well against your specific domain problems. That's where all the value is."
