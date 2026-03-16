---
source_id: "266"
title: "Inheritance in Prompting"
creator: "Jaymin West"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Y6EyN9OI4RU"
date: "2026-03-13"
duration: "9:33"
type: "video"
tags: ["prompt-engineering", "multi-agent", "agent-teams", "meta-prompts", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns", "05-team-orchestration"]
---

# 266: Inheritance in Prompting

> **Creator**: Jaymin West | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 9:33

# Inheritance in Prompting

## Summary

Jaymin West introduces the concept of applying object-oriented programming inheritance patterns to prompt engineering for multi-agent systems. The core idea is treating prompts as structured, composable code rather than flat markdown files — enabling consistency across agent networks without duplicating context. By establishing a base prompt that child agent prompts extend and specialize, teams can maintain a single source of truth for shared agent behavior.

The video covers four key techniques borrowed from OOP: single inheritance (base → child), mixins (horizontal capability additions), section overriding (selectively replacing inherited sections), and variables (parameterizing prompts for reuse across projects). West demonstrates these concepts using his own project "Overstory" and a tool he built called "Canopy" that implements prompt inheritance in practice. The framing throughout is that prompts should be treated as a real engineering discipline with proper abstractions, not ad-hoc text files.

The practical motivation is scale: as agent counts grow, manually keeping dozens of prompt files consistent becomes untenable. Inheritance solves the problem of duplicated context (where 50 prompt files share 60–70% of the same content), makes updates propagate automatically from base to child prompts, and allows specialization without bloat.

## Key Concepts

### Prompt Inheritance (Base → Child)
Directly analogous to class inheritance in OOP. A base prompt defines shared identity, constraints, communication protocols, and failure modes for all agents. Child prompts inherit this foundation and extend it with role-specific additions. This ensures every agent in a system operates from a consistent behavioral baseline, and a change to the base prompt propagates to all children automatically.

### Mixins as Horizontal Capabilities
Where inheritance is "vertical" (who you are), mixins are "horizontal" (what you can do or know). A builder agent might inherit the base prompt but also receive a safety rules mixin; a scout agent might receive an architecture information mixin. Mixins prevent prompt bloat by keeping specialized knowledge out of the base and out of agents that don't need it — instead of cramming everything into the base prompt, capabilities are appended selectively.

### Section Overriding
Child prompts can selectively override specific sections of the base prompt rather than inheriting them wholesale. For example, a coordinator agent and a builder agent share the same communication protocol section (inherited), but each has different constraints sections (overridden). This granular composability means agents can diverge where necessary without duplicating the shared context — eliminating the problem of near-identical prompt files that drift out of sync.

### Prompt Variables
Parameterizing prompts with variables (e.g., `{{quality_gate}}`, `{{tracking_tool}}`, `{{tech_stack}}`) decouples project-specific details from the prompt structure itself. Instead of hard-coding `bun test` into a prompt, a variable resolves to the appropriate test command at runtime. This lets the same prompt template serve multiple projects or configurations by swapping variable values, dramatically reducing the number of prompt files needed.

### Prompts as Composable Units
Each section of a prompt (constraints, communication protocol, completion protocol, failure modes, tooling) is treated as a discrete, swappable unit rather than a monolithic blob. This section-level composability is what makes inheritance, mixins, and overrides practical — you can target exactly the sections that need to change for a given agent role without rewriting everything else.

## Practical Takeaways

- **Start with a base prompt** that captures universal agent behavior: communication protocols, output formats, failure handling, and project-wide constraints. All role-specific agents should inherit from this rather than being written from scratch.
- **Use mixins to add capabilities, not the base prompt** — if only one or two agents need a specific piece of knowledge (e.g., architecture docs, safety rules), keep it out of the base and inject it selectively via mixin to avoid polluting agents that don't need it.
- **Override sections explicitly** rather than duplicating full prompts. Identify which sections vary by role (typically constraints and tooling) versus which should be universal (communication protocol), and design your inheritance structure accordingly.
- **Parameterize anything project-specific**: test commands, linters, task tracking tools, tech stacks. This turns a single prompt template into a reusable asset across multiple projects or configurations.
- **Treat prompt files as code**: apply the same engineering discipline you'd apply to source code — avoid duplication, create abstractions, and think about how changes propagate through the system. Tools like Canopy (West's own) can enforce these structures programmatically.

## Notable Quotes

> "Inheritance being vertical — you know who you are. And then mixins are more horizontal — what you can do, what you know."

> "This just leads to prompt bloating where you now have like safety rules in a child node that doesn't necessarily need to have access to that information."

> "Treating prompting like an actual practice is just helpful when it comes to orchestrating tons of agents in a codebase."
