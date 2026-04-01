# Curriculum

A progressive 8-module learning path for AI-assisted development — from foundational concepts to team-scale orchestration, with critical perspective on career impact, quality engineering, and industry economics. Compiled from 438 curated source notes.

## Modules

| # | Module | Description | Sources |
|---|--------|-------------|---------|
| 01 | [Foundations](01-foundations/README.md) | AI landscape, capability overhang, model releases, hype vs reality, agent failure rates | 214 sources |
| 02 | [Prompting & Workflows](02-prompting-and-workflows/README.md) | Prompt engineering, context engineering, spec-first development, builder-validator, supply chain security | 86 sources |
| 03 | [Claude Code Essentials](03-claude-code-essentials/README.md) | Setup, CLAUDE.md, skills system, context discipline, computer use, memory patterns | 129 sources |
| 04 | [Agentic Patterns](04-agentic-patterns/README.md) | Agent species, builder/validator, meta-prompts, hooks, phoenix architecture, evals | 183 sources |
| 05 | [Team Orchestration](05-team-orchestration/README.md) | Agent teams, multi-tier hierarchies, persistent expertise, dispatch, fleet management | 74 sources |
| 06 | [Strategy & Economics](06-strategy-and-economics/README.md) | AI-driven SDLC, infrastructure economics, security, adoption frameworks, labor market | 239 sources |
| 09 | [Career & Organizational Transformation](09-career-and-transformation/README.md) | Workforce bifurcation, apprenticeship crisis, cognitive debt, forced adoption, career strategy | 45 sources |
| 10 | [Quality, Validation & Evals](10-quality-and-validation/README.md) | Builder/validator, evals, anti-slop engineering, hallucination reduction, harness engineering | 38 sources |

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

09 Career & Organizational Transformation (requires 01)
10 Quality, Validation & Evals (requires 02, cross-references 04)
```

## Building the Curriculum

Use the `/compile-curriculum` skill to rebuild module content from tagged sources:

```
/compile-curriculum all          # Rebuild all modules
/compile-curriculum 04           # Rebuild a specific module
/compile-curriculum agentic      # Rebuild by module name
```
