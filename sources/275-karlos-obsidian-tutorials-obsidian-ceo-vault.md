---
source_id: "275"
title: "How the CEO of Obsidian Takes his Notes (Underrated Genius)"
creator: "Karlos Obsidian Tutorials"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Dq3R3uS0sQ4"
date: "2025-12-05"
duration: "32:18"
type: "video"
tags: ["context-engineering", "meta-prompts", "specification"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials"]
---

# 275: How the CEO of Obsidian Takes his Notes (Underrated Genius)

> **Creator**: Karlos Obsidian Tutorials | **Platform**: YouTube | **Date**: 2025-12-05 | **Duration**: 32:18

## Summary

This video walks through the personal Obsidian vault system of Stefango (Kipano), CEO of Obsidian MD, explaining the philosophy and practical mechanics behind his minimalist, speed-oriented note-taking approach. The core insight is that the system deliberately rejects conventional organization — no deep folder hierarchies, no upfront categorization overhead — in favor of storing almost everything in the vault root and using properties, templates, and links to create emergent structure.

The video covers the technical mechanics step by step: opening the vault, understanding properties as metadata labels on notes, using the unique note creator for timestamped journal entries, applying templates to lazily pre-populate note structure, and navigating via quick switcher shortcuts rather than the file explorer. The emphasis throughout is on reducing friction so that capturing and connecting ideas happens faster than organizing them.

While this content is not directly about AI-assisted development, it represents a knowledge management philosophy that is highly relevant to practitioners building personal systems for tracking AI workflows, research, and prompts. The "file over app" principle and properties-based organization pattern have direct analogues in how effective AI developers structure their context, specifications, and reusable prompt templates.

---

## Key Concepts

### File Over App Philosophy
Steph's first principle is that notes exist as plain markdown (text) files independent of any application. The vault is just a folder; Obsidian is a lens over it. This means notes outlast any software tool. For AI developers, this philosophy applies directly to storing prompts, CLAUDE.md files, and specifications as plain text artifacts that travel with projects and survive tool changes.

### Root-First Organization with Properties
Rather than sorting notes into folders upfront, nearly all notes live in the vault root. Organization is applied retroactively through YAML frontmatter **properties** (metadata labels). A note about a meeting gets a `categories: meetings` property; a journal entry gets a tag. This eliminates the cognitive overhead of deciding where something belongs at creation time — a direct application of the "laziness as a feature" principle.

### Templates as Laziness Infrastructure
Almost every note starts from a template that pre-populates relevant properties. The template does the organizational work so the writer doesn't have to think about structure at capture time. This maps cleanly onto the prompt engineering concept of meta-prompts: reusable scaffolds that enforce consistent structure without requiring the user to reconstruct it each time.

### Links as the Organizing Mechanism
Double-bracket `[[wikilinks]]` create connections between notes, forming a knowledge graph. Unresolved links (pointing to notes that don't exist yet) are acceptable and even useful — they represent future nodes in the network. This mirrors context engineering practices where forward-references and stubs are preferable to incomplete capture.

### Keyboard-Driven Navigation Over File Explorer
The quick switcher (`Cmd+O`) replaces folder browsing as the primary navigation tool. The video recommends custom hotkeys for the most frequent actions: new unique note, insert template, open daily note, add internal link. Speed of access is treated as a first-class design constraint, not an afterthought.

---

## Practical Takeaways

- **Minimize folder overhead for fast capture**: Store most notes at root level and use frontmatter properties for categorization — deciding where something belongs can happen later or be automated by templates.
- **Templates eliminate repeated decision-making**: Pre-built templates for recurring note types (meetings, daily logs, project specs) are the primary mechanism for maintaining consistency without slowing capture.
- **Keyboard shortcuts are the real workflow**: The file explorer is a trap; `Cmd+O` quick-switcher navigation is dramatically faster and should replace most folder-clicking behavior.
- **Properties enable filtered views without manual sorting**: Obsidian Bases (smart tables) can surface all notes sharing a property, making the flat root structure navigable at scale.
- **Plain text is the durable format**: Structuring knowledge in markdown ensures portability across tools — relevant for prompt libraries, CLAUDE.md files, and specification documents that need to survive toolchain changes.

---

## Notable Quotes

> "His system is oriented towards speed and laziness, and he doesn't want the overhead of deciding where things should go."

> "Almost every note I create starts from a template. I use templates heavily because they allow me to lazily add information that will help me find the notes later."

> "If a note is in the root, I know it's something I wrote or relates directly to me."

---
