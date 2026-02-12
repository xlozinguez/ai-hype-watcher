# Compile Curriculum — Reference Material

## Module Structure

Each curriculum module follows a consistent structure designed as a progressive learning path.

### Module README Template

```markdown
# Module NN: Title

> One-sentence summary of what this module teaches.

## Overview

2-3 paragraphs explaining the module's scope, why it matters, and how it connects to other modules.

## Prerequisites

- List modules that should be completed first (if any)

## Core Concepts

### Concept 1: Title
Explanation synthesized from source material. Attribution to creators where appropriate.

### Concept 2: Title
...

## Patterns & Practices

### Pattern Name
- **When to use**: Context for applying this pattern
- **How it works**: Step-by-step description
- **Example**: Concrete example from source material
- **Source**: Reference to source note(s)

## Common Pitfalls

- **Pitfall 1**: Description and how to avoid it
- **Pitfall 2**: ...

## Hands-On Exercises

1. **Exercise title**: Brief description of what to practice
2. ...

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [NNN: Title](../sources/NNN-file.md) | Creator | Topics covered |

## Further Reading

- [Resource title](url) — Brief description
```

## Compilation Guidelines

### Teaching Progression
Content within each module should follow a progression from foundational to advanced:
1. Start with "what" and "why" (concepts and motivation)
2. Move to "how" (patterns and practices)
3. End with "watch out" (pitfalls) and "try it" (exercises)

### Source Attribution
- When presenting a concept from a single source, attribute it: "As [Creator] demonstrates in [Source Title]..."
- When synthesizing across multiple sources, note the convergence: "Multiple creators ([#NNN], [#NNN]) emphasize..."
- For direct quotes, use blockquotes with attribution

### Cross-Module References
- When a concept connects to another module, add a cross-reference: "See also: [Module NN: Topic](../NN-module/README.md)"
- Don't duplicate content — reference the authoritative module

### Critical Perspective
- Maintain balanced perspective throughout — acknowledge both capabilities and limitations
- Include counterarguments and skeptical viewpoints where sources provide them
- The curriculum should help learners form their own informed opinions, not sell AI hype

## Module Dependencies

```
01-foundations (no prerequisites)
  ↓
02-prompting-and-workflows (builds on 01)
  ↓
03-claude-code-essentials (builds on 01, 02)
  ↓
04-agentic-patterns (builds on 03)
  ↓
05-team-orchestration (builds on 04)

06-strategy-and-economics (independent, can be taken alongside any module)
```
