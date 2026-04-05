# Curriculum

A progressive 6-module learning path for AI-assisted development — from foundational concepts to team-scale orchestration, with critical perspective on industry economics. Compiled from 516 curated source notes. Last compiled: 2026-04-04, informed by STATE.md validated theses.

## Modules

| # | Module | Description | Sources |
|---|--------|-------------|---------|
| 01 | [Foundations](01-foundations/README.md) | AI landscape, capability overhang, METR 14-hour milestone, inference-time scaling, bubble thesis with financial distress signals, agent failure spectrum | 251 sources |
| 02 | [Prompting & Workflows](02-prompting-and-workflows/README.md) | Context engineering (industry consensus), spec-first development with dedicated tooling, planner-generator-evaluator pattern, hallucination as structural | 105 sources |
| 03 | [Claude Code Essentials](03-claude-code-essentials/README.md) | CLAUDE.md, skills as open standard (cross-platform), hooks (21 lifecycle events), computer use (Mac + Windows), AutoDream, memory patterns | 147 sources |
| 04 | [Agentic Patterns](04-agentic-patterns/README.md) | Agent species, builder/validator, meta-prompts, hooks (21 events), CLI + MCP strategic use, phoenix architecture, evals, harness engineering | 220 sources |
| 05 | [Team Orchestration](05-team-orchestration/README.md) | Agent teams, multi-tier hierarchies, persistent expertise, harness engineering (recognized discipline), dispatch, fleet management, coordination collapse | 89 sources |
| 06 | [Strategy & Economics](06-strategy-and-economics/README.md) | Power as binding constraint, infrastructure economics ($660-690B capex), security, junior developer crisis (73% decline), token austerity, two-bubble thesis | 286 sources |

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
