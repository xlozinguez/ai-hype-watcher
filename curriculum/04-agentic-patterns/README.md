# Module 04: Agentic Patterns

> Learn the architectural patterns that make AI agents reliable — builder/validator, task systems, meta-prompts, and lifecycle hooks.

## Overview

Moving from single prompts to autonomous agents requires architectural discipline. This module covers the patterns that working engineers use to get reliable results from AI agents: the builder/validator pattern for quality assurance, task systems for dependency management, meta-prompts for consistency, and lifecycle hooks for safety.

## Prerequisites

- [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md)

## Key Topics

- Builder/Validator pattern (implementation agent + read-only review agent)
- Task system (TaskCreate, TaskUpdate, TaskList, TaskGet) and dependency DAGs
- Meta-prompts over ad-hoc prompting
- Lifecycle hooks for deterministic control
- The "Core Four" framework: Context, Model, Prompt, Tools
- Ralph and the evolution of autonomous coding loops

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [#001: Claude Code Task System](../sources/001-indydevdan-claude-code-task-system.md) | IndyDevDan | Task system, builder/validator, meta-prompts, hooks |
| [#008: Phase Transition](../sources/008-nate-b-jones-phase-transition.md) | Nate B Jones | Ralph, Gas Town, capability overhang, "Big Three" framework |
| [#014: Skills Decision Framework](../sources/014-indydevdan-skills-framework.md) | IndyDevDan | Composability hierarchy, Core Four framework |

## Further Reading

*Content will be compiled from sources using `/compile-curriculum 04`*
