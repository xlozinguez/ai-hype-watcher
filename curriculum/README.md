# Curriculum

A progressive 6-module learning path for AI-assisted development — from foundational concepts to team-scale orchestration, with critical perspective on industry economics.

## Modules

| # | Module | Description | Sources |
|---|--------|-------------|---------|
| 01 | [Foundations](01-foundations/README.md) | AI landscape, capability overhang, hype vs reality | #003, #007, #008, #015, #018 |
| 02 | [Prompting & Workflows](02-prompting-and-workflows/README.md) | Prompt engineering, sticky workflows, spec-first development | #005, #006 |
| 03 | [Claude Code Essentials](03-claude-code-essentials/README.md) | Setup, CLAUDE.md, skills system, context discipline | #012, #014 |
| 04 | [Agentic Patterns](04-agentic-patterns/README.md) | Subagents, builder/validator, meta-prompts, hooks | #001, #008, #014 |
| 05 | [Team Orchestration](05-team-orchestration/README.md) | Agent teams, multi-agent coordination, observability | #004, #010, #013 |
| 06 | [Strategy & Economics](06-strategy-and-economics/README.md) | AI-driven SDLC, infrastructure economics, security, adoption | #002, #009, #016, #017 |

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
