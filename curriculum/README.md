# Curriculum

A progressive 6-module learning path for AI-assisted development — from foundational concepts to team-scale orchestration, with critical perspective on industry economics. Compiled from 209 curated source notes.

## Modules

| # | Module | Description | Sources |
|---|--------|-------------|---------|
| 01 | [Foundations](01-foundations/README.md) | AI landscape, capability overhang, model releases, hype vs reality | 109 sources |
| 02 | [Prompting & Workflows](02-prompting-and-workflows/README.md) | Prompt engineering, context engineering, spec-first development, sticky workflows | 34 sources |
| 03 | [Claude Code Essentials](03-claude-code-essentials/README.md) | Setup, CLAUDE.md, skills system, context discipline, cowork, memory patterns | 61 sources |
| 04 | [Agentic Patterns](04-agentic-patterns/README.md) | Subagents, builder/validator, meta-prompts, hooks, agent design patterns | 79 sources |
| 05 | [Team Orchestration](05-team-orchestration/README.md) | Agent teams, multi-agent coordination, narrow agents, observability | 30 sources |
| 06 | [Strategy & Economics](06-strategy-and-economics/README.md) | AI-driven SDLC, infrastructure economics, security, SaaS disruption, adoption | 112 sources |

## Learning Path

```
01 Foundations
  ↓
02 Prompting & Workflows
  ↓
03 Claude Code Essentials
  ↓
04 Agentic Patterns
  ↓
05 Team Orchestration

06 Strategy & Economics (independent — take alongside any module)
```

## Building the Curriculum

Use the `/compile-curriculum` skill to rebuild module content from tagged sources:

```
/compile-curriculum all          # Rebuild all modules
/compile-curriculum 04           # Rebuild a specific module
/compile-curriculum agentic      # Rebuild by module name
```
