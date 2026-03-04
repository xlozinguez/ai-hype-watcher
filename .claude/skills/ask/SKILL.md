---
name: ask
description: Ask a natural language question and get an answer synthesized from curriculum modules and source notes with citations.
allowed-tools: Read, Glob, Grep
argument-hint: "<question>"
---

# Ask — Curriculum Knowledge Query

Answer natural language questions using the knowledge base of 209+ source notes, 6 curriculum modules, and synthesis documents. All answers are grounded with inline citations.

## Input

A natural language question. Examples:
- `What are the best practices for agent memory?`
- `What's the learning path for someone new to Claude Code?`
- `Compare what different creators say about AI economics`
- `What security risks exist with AI coding tools?`

## Workflow

### Step 1: Analyze the question

1. Extract 3-5 key search terms from the question
2. Identify likely curriculum modules using the module mappings in REFERENCE.md
3. Determine if the question is:
   - **Conceptual** — best answered from curriculum Core Concepts sections
   - **Comparative** — needs multiple source perspectives
   - **Navigational** — user wants to find where to learn about a topic
   - **Factual** — needs specific claims from source notes

### Step 2: Search curriculum modules

For each likely module identified in Step 1:

1. Read `curriculum/<module>/README.md` — check the overview and section list
2. Grep within `curriculum/<module>/` for the key search terms
3. Read matching curriculum section files for Core Concepts content — this is the highest-quality synthesized material

Curriculum modules:
- `curriculum/01-foundations/` — AI landscape, capability overhang, hype vs reality
- `curriculum/02-prompting-and-workflows/` — Prompt engineering, spec-first, validation
- `curriculum/03-claude-code-essentials/` — Setup, CLAUDE.md, skills, context discipline
- `curriculum/04-agentic-patterns/` — Subagents, builder/validator, meta-prompts, hooks
- `curriculum/05-team-orchestration/` — Agent teams, multi-agent coordination
- `curriculum/06-strategy-and-economics/` — AI-driven SDLC, infra economics, security

### Step 3: Search source notes for specifics

1. Grep `sources/` for key search terms to find relevant source files
2. Read frontmatter + Key Takeaways section from the top 5-8 most relevant sources
3. Note source IDs, creators, and specific claims for citation

### Step 4: Search synthesis documents

1. Grep `synthesis/` for key search terms
2. Read any matching synthesis docs — these contain cross-source analysis that may directly answer comparative questions

### Step 5: Compose grounded answer

Write a clear, well-structured answer following these rules:

**Citation format**:
- Source notes: `[#NNN]` (e.g., `[#099]`, `[#148]`)
- Curriculum modules: `[Module 04]` or `[Module 04: Agentic Patterns]`
- Synthesis docs: `[Synthesis: topic-name]`
- When quoting or paraphrasing a specific creator: `Creator Name [#NNN]`

**Answer structure**:
1. **Direct answer** — 2-4 sentences answering the question directly
2. **Details** — Supporting evidence organized by theme, not by source
3. **Sources** — Brief list of the most relevant sources at the end

**Quality rules**:
- Never fabricate claims — only include information found in the knowledge base
- If the knowledge base doesn't cover a topic, say so clearly
- Attribute ideas to their original creators
- For comparative questions, present multiple perspectives fairly
- For navigational questions, recommend a learning path through modules
- Keep answers concise — aim for 200-400 words unless the question demands more

## Output Format

```markdown
## Answer

[Direct answer to the question, 2-4 sentences with inline citations]

### [Theme/Detail heading if needed]

[Supporting details with citations like [#NNN] and [Module 04]]

### Sources

- **[#NNN]** Creator — Title (most relevant sources only, 3-8 items)
- **[Module 04]** Agentic Patterns (if curriculum was a key source)
```

## Edge Cases

- **Question too broad** (e.g., "Tell me everything about AI"): Narrow the scope, suggest 2-3 more specific questions
- **Topic not covered**: State that clearly and suggest related topics that ARE covered
- **Single-source answer**: If only one source covers the topic, note that the perspective is limited
- **Conflicting views**: Present both sides with attribution — the knowledge base includes both optimistic and skeptical perspectives
