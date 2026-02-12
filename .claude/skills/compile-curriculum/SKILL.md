---
name: compile-curriculum
description: Rebuild curriculum sections from tagged source notes. Reads sources mapped to each module and compiles teaching-oriented content.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
argument-hint: "<module-number|module-name|all>"
---

# Compile Curriculum

Rebuild curriculum module content by reading source notes and compiling them into a progressive learning path.

## Input

One of:
- A module number (e.g., `01`, `04`)
- A module name (e.g., `foundations`, `agentic-patterns`)
- `all` to rebuild all modules

## Workflow

### Step 1: Read reference material

Read `.claude/skills/compile-curriculum/REFERENCE.md` for module structure and compilation guidelines.

### Step 2: Identify target modules

Parse the input to determine which module(s) to compile. Map module names to directory paths:
- `01` or `foundations` → `curriculum/01-foundations/`
- `02` or `prompting` → `curriculum/02-prompting-and-workflows/`
- `03` or `claude-code` → `curriculum/03-claude-code-essentials/`
- `04` or `agentic` → `curriculum/04-agentic-patterns/`
- `05` or `teams` → `curriculum/05-team-orchestration/`
- `06` or `strategy` → `curriculum/06-strategy-and-economics/`

### Step 3: Find tagged sources

For each target module, search all files in `sources/` for frontmatter containing the module name in `curriculum_modules`. Read each matching source file.

### Step 4: Compile module content

For each module, create or update the module's `README.md` with:
- **Overview**: What this module covers and why it matters
- **Core Concepts**: Key ideas synthesized from the tagged sources, organized as a teaching progression
- **Patterns & Practices**: Practical patterns with examples drawn from the sources
- **Common Pitfalls**: What to avoid, based on creator warnings and critical perspectives
- **Hands-On Exercises**: Suggested exercises to practice the concepts
- **Source Material**: Links to the source notes that inform this module
- **Further Reading**: External resources for deeper exploration

### Step 5: Detect orphan sources

After compilation, check for sources that aren't mapped to any curriculum module. Report these so they can be tagged appropriately.

### Step 6: Update curriculum README

Update `curriculum/README.md` with current module summaries and source counts.

## Output

List of updated module files and any orphan sources detected.
