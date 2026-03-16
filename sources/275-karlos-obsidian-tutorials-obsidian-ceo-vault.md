---
source_id: "275"
title: "How the CEO of Obsidian Takes his Notes (Underrated Genius)"
creator: "Karlos Obsidian Tutorials"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Dq3R3uS0sQ4"
date: "2025-12-05"
duration: "32:18"
type: "video"
tags: []
curriculum_modules: []
---

# 275: How the CEO of Obsidian Takes his Notes (Underrated Genius)

> **Creator**: Karlos Obsidian Tutorials | **Platform**: YouTube | **Date**: 2025-12-05 | **Duration**: 32:18

## Summary

This video walks through the personal note-taking vault of Stefango (Kipano), CEO of Obsidian MD, explaining his core philosophy and how to implement it. The creator, Karlos, initially dismissed the system as too sparse and low-effort, but later recognized it as a deliberately minimal, speed-optimized approach to knowledge management. The system prioritizes getting notes captured quickly over organizing them perfectly, using properties, templates, and Obsidian's built-in features to create structure without imposing friction.

The central insight is that Stefango organizes notes primarily through metadata properties rather than folder hierarchies. Most notes live in the vault root, categorized by a `categories` property that powers smart tables (Obsidian Bases) for retrieval. This "file over app" philosophy ensures notes outlast any software — they're just markdown text files. The system leans on templates, unique note creation with auto-timestamps, and quick-switcher keyboard shortcuts to make capturing and retrieving information as fast as possible.

While the content is focused on personal knowledge management (PKM) rather than AI-assisted development, the underlying design principles — flat structure, metadata-driven organization, template-first workflows, and speed/laziness as features rather than bugs — translate directly to how AI development contexts and knowledge systems should be structured for rapid retrieval and reuse.

---

## Key Concepts

### File Over App Philosophy
Stefango explicitly builds his vault around the principle that notes must outlast the software used to write them. Every note is a plain markdown (`.md`) text file stored on disk. If Obsidian disappeared tomorrow, the knowledge remains fully intact and readable. This design choice prioritizes long-term data sovereignty over feature richness.

### Flat Structure with Metadata-Driven Organization
Rather than nesting notes inside category folders, Stefango keeps nearly everything in the vault root. Organization happens via a `categories` property in each note's YAML frontmatter. Obsidian Bases (smart tables) then surface notes filtered by these properties. This eliminates the "where does this go?" decision overhead that stalls most note-takers.

### Templates as Laziness Infrastructure
Almost every note Stefango creates starts from a template. Templates pre-populate relevant properties (date, people, topics, location) so the author never has to remember what metadata to capture. The friction of adding structure is paid once (when building the template) rather than every time a note is created. The video maps out keyboard shortcuts (`Option+Shift+T`) to make template insertion nearly instantaneous.

### Unique Notes with Auto-Timestamps
The "Create New Unique Note" feature generates a note named with the current date and time, automatically adding a `created` property. This means even retitled notes retain their creation timestamp, enabling chronological retrieval without manual date entry. It's a small mechanism with significant compounding value for journals and meeting logs.

### Categories as Navigation Hubs
Category notes (e.g., `meetings.md`) act as index views powered by Obsidian Bases rather than as traditional folders. Because they live in the root like all other notes, they're accessible via the quick-switcher (`Cmd+O`) without touching the file explorer. This makes navigation keyboard-first and very fast.

---

## Practical Takeaways

- **Keep notes flat, not nested.** Resist the urge to build deep folder hierarchies. Use frontmatter properties for categorization instead — it scales better and removes placement decisions that interrupt capture flow.
- **Build templates before you need them.** Every recurring note type (meeting, journal, book summary) should have a template that pre-fills all the metadata you'll want later. The cost is minutes upfront; the payoff is years of consistent structure.
- **Design for retrieval speed, not organizational beauty.** The quick-switcher (`Cmd+O`) plus meaningful note titles beats any folder structure for finding a specific note fast. Optimize your naming and tagging for search, not for browsing.
- **Timestamp everything automatically.** Use unique note creation (or equivalent) to ensure every capture has a machine-generated timestamp. Manual date entry is a habit that breaks under pressure.
- **Embrace "good enough" capture.** Stefango's system is explicitly oriented toward speed and laziness. A note captured imperfectly is infinitely more valuable than a perfectly organized note never written.

---

## Notable Quotes

> "His system is oriented towards speed and laziness, and he doesn't want the overhead of deciding where things should go."

> "Almost every note I create starts from a template. I use templates heavily because they allow me to lazily add information that will help me find the notes later."

> "If a note is in the root, I know it's something I wrote or relates directly to me."

---



> **Curator note:** This video contains no tags from the established taxonomy and maps to no curriculum module — it is a general PKM / Obsidian tutorial with no AI-assisted development content. It may be useful as supplementary material on knowledge base design if the curriculum ever covers note-taking systems for developers, but should not be ingested as core curriculum content in its current form.
