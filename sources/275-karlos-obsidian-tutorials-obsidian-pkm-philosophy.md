---
source_id: "275"
title: "How the CEO of Obsidian Takes his Notes (Underrated Genius)"
creator: "Karlos Obsidian Tutorials"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Dq3R3uS0sQ4"
date: "2025-12-05"
duration: "32:18"
type: "video"
tags: ["context-engineering", "specification"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials"]
---

# 275: How the CEO of Obsidian Takes his Notes (Underrated Genius)

> **Creator**: Karlos Obsidian Tutorials | **Platform**: YouTube | **Date**: 2025-12-05 | **Duration**: 32:18

## Summary

This video walks through the personal Obsidian vault and note-taking philosophy of Stephango (Steph Ango), CEO of Obsidian MD. The creator reverse-engineers Steph's system from a publicly available GitHub template, demonstrating its core principles: keep almost everything in the vault root (no deep folder hierarchies), use YAML frontmatter properties for categorization, lean heavily on templates for speed, and navigate via quick-switcher rather than file explorer. The system is explicitly designed around laziness and speed — minimizing the friction of deciding where notes belong so that the act of capturing thoughts remains low-cost.

The video's central insight is that chaos in the file system is acceptable, even intentional, because organization emerges from properties and links rather than folder structure. Categories are just notes with a smart Obsidian Bases table that aggregates all notes sharing a given property value. This flips the traditional hierarchical filing model: instead of placing a note *into* a folder, you *tag a note with* a category and let the system surface it dynamically.

While the video is primarily about personal knowledge management (PKM) in Obsidian rather than AI-assisted development, it demonstrates a structural philosophy — file-over-app, metadata-driven organization, template-first capture — that directly informs how developers might architect knowledge bases, prompt libraries, and context systems for AI workflows.

---

## Key Concepts

### File-Over-App Philosophy
Steph's first principle is that notes should outlast any software. Every note is a plain markdown (`.md`) file — a text file with minor formatting conventions. If Obsidian disappeared tomorrow, the content remains fully accessible. This principle argues against proprietary formats or database-backed note tools and has direct relevance to storing AI prompts, specs, and workflows in version-controlled plaintext.

### Root-First Organization (No Deep Folders)
Rather than nesting notes in category folders, Steph places almost all notes in the vault root. His rule: *if a note is in the root, it relates directly to him.* Folders are avoided because most notes belong to multiple areas of thought, and the overhead of deciding placement creates friction that discourages capture. The few folders that exist (e.g., a `categories` folder) are present only for template-clarity and are themselves migrated to the root in practice.

### Properties as Dynamic Metadata
Obsidian's YAML frontmatter (delimited by `---`) allows attaching structured metadata — `categories`, `date`, `people`, `topics`, `location` — to any note. These properties enable Obsidian Bases (a smart table/query feature) to dynamically aggregate all notes sharing a property value. Instead of filing a meeting note into a `/meetings/` folder, you set `categories: meetings` and the Meetings base auto-populates. This is schema-on-read rather than schema-on-write.

### Template-First Capture
Nearly every note Steph creates begins from a template. Templates pre-populate the relevant YAML properties so the user never has to remember what metadata to add. The video demonstrates a Meeting template that auto-inserts date, people, topics, and location fields. Steph frames this as "lazy" — templates do the cognitive work of structure so the writer only has to do the creative work of content.

### Quick-Switcher Navigation Over File Explorer
The recommended navigation mode is keyboard-driven: `Cmd+O` (quick switcher) to jump to any note by typing a few characters. The file explorer sidebar is treated as a last resort. Combined with hotkeys for new unique note (`Alt+Shift+N`), insert template (`Alt+Shift+T`), and open daily note (`Alt+Shift+D`), the entire capture-and-retrieve loop becomes single-handed and sub-second.

---

## Practical Takeaways

- **Flatten your structure ruthlessly.** Deep folder hierarchies front-load organizational decisions at the moment of capture — the worst possible time. Metadata properties applied post-hoc (or via templates) achieve the same retrieval without the friction tax.
- **Use templates to encode your schema.** Any time you find yourself repeatedly adding the same set of properties to a note type, that's a template waiting to be created. Templates are the cheapest form of structural consistency.
- **Prefer plaintext and version control.** The file-over-app principle applies equally to AI prompt libraries, CLAUDE.md files, and specification documents — store them as markdown in git, not in proprietary tool databases.
- **Keyboard shortcuts compound.** The difference between a 4-keystroke capture flow and a 12-keystroke flow, multiplied across hundreds of notes per year, determines whether a system actually gets used. Map your highest-frequency actions to muscle memory.
- **Let links do organizational work.** Bidirectional links (`[[note name]]`) create a navigable graph without requiring hierarchical placement. A note can be "in" multiple conceptual spaces simultaneously through links and property values, which folders cannot achieve.

---

## Notable Quotes

> "His system is oriented towards speed and laziness, and he doesn't want the overhead of deciding where things should go."

> "Most of my notes are in the root of the vault, not a folder. If a note is in the root, I know it's something I wrote or relates directly to me."

> "Almost every note I create starts from a template. I use templates heavily because they allow me to lazily add information that will help me find the notes later."

---
