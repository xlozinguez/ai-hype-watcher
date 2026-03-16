---
source_id: "275"
title: "How the CEO of Obsidian Takes his Notes (Underrated Genius)"
creator: "Karlos Obsidian Tutorials"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Dq3R3uS0sQ4"
date: "2025-12-05"
duration: "32:18"
type: "video"
tags: ["prompt-engineering", "meta-prompts", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows"]
---

# 275: How the CEO of Obsidian Takes his Notes (Underrated Genius)

> **Creator**: Karlos Obsidian Tutorials | **Platform**: YouTube | **Date**: 2025-12-05 | **Duration**: 32:18

## Summary

This video walks through the personal Obsidian vault and note-taking philosophy of Stefango (Kipano), CEO of Obsidian MD. The core philosophy centers on two principles: **file-over-app** (notes are plain markdown files that outlast any software) and **speed through laziness** (minimize friction by avoiding folders, using templates heavily, and letting properties + links do the organizational work). The presenter guides viewers through downloading and configuring Steph's vault template step by step.

The system's central mechanism is using YAML frontmatter **properties** (categories, dates, people, topics) rather than folder hierarchies to organize notes. Most notes live in the vault root rather than nested folders, and navigation happens via Obsidian's quick switcher (Cmd/Ctrl+O) and Bases (smart tables that filter notes by property). Templates auto-populate properties so the user never has to manually categorize from scratch.

The video also covers configuring hotkeys to make the workflow nearly frictionless: new unique note, insert template, open daily note, and add internal link. **Links between notes** are the connective tissue of the system — typed with double brackets — creating a knowledge graph from what would otherwise be a flat pile of files. The presenter frames the apparent chaos of a flat, property-organized vault as intentional: it forces emergent connections rather than predetermined taxonomies.

---

## Key Concepts

### File-Over-App Philosophy
Notes are stored as plain `.md` (Markdown) text files in a folder on disk. The vault is just a folder; Obsidian is just a viewer. This means notes are software-agnostic and permanent — if Obsidian disappeared tomorrow, every note would still be readable in any text editor. This is the philosophical foundation of the entire system.

### Properties as the Primary Organizational Layer
Instead of nested folders, Steph uses YAML frontmatter properties (e.g., `categories: meetings`, `people: Stephango`, `location: Chile`) to tag and sort notes. Obsidian Bases then renders these properties as filterable smart tables. This allows a note to "belong" to multiple categories simultaneously — something folder hierarchies cannot do — without requiring the author to decide upfront where a note lives.

### Flat Root Structure + Quick Switcher Navigation
Virtually all notes live in the vault root (no subfolders) and are retrieved via the quick switcher (Cmd+O) by typing partial titles or property values. The categories and notes folders in the downloadable template exist only for onboarding clarity and are explicitly meant to be collapsed into the root. This trades visual hierarchy for retrieval speed.

### Templates as Lazy Information Capture
Almost every note starts from a template that pre-fills relevant properties. A "Meeting" template auto-inserts date, people, topics, and location fields. This means the cognitive overhead of "how do I structure this?" is solved once at template-creation time, not every time a note is made. Steph's framing: templates let you *lazily* add information that will help you *find* notes later.

### Links as Knowledge Graph Connectors
Double-bracket links (`[[note title]]`) connect notes into a navigable graph. Links can be unresolved (pointing to a not-yet-created note, which auto-creates it on click) or resolved. This mechanism — combined with the flat structure — is what allows emergent connections across topics to surface organically rather than being forced into predetermined folder categories.

---

## Practical Takeaways

- **Start from templates, not blank notes.** Create templates for every recurring note type (meetings, journal entries, evergreen notes) so properties are populated automatically. The cost of template design is paid once; the benefit compounds with every note.

- **Replace folder navigation with hotkeys.** Configure Cmd/Ctrl+O (quick switcher), and hotkeys for new unique note (`Alt+Shift+N`), insert template (`Alt+Shift+T`), daily note (`Alt+Shift+D`), and add link (`Alt+Shift+L`). This reduces context-switching friction to near zero.

- **Use properties instead of folders for multi-dimensional notes.** A meeting with a friend about a book project might be `categories: meetings`, `people: [friend]`, `topics: [book, writing]` — it surfaces in all three filtered views without copying the note.

- **Embrace the flat mess.** Resist the urge to create elaborate folder structures. The discomfort of a chaotic file explorer is the cost of a system optimized for speed of capture and discovery of unexpected connections.

- **Unique note creator sets the timestamp automatically.** Using "Create new unique note" rather than "New note" stamps the creation date/time into the filename and frontmatter, preserving temporal context even if you rename or move the note later.

---

## Notable Quotes

> "His system is oriented towards speed and laziness, and he doesn't want the overhead of deciding where things should go."

> "Most of my notes are in the root of the vault, not a folder. If a note is in the root, I know it's something I wrote or relates directly to me."

> "I use templates heavily because they allow me to lazily add information that will help me find the notes later."

---
