---
source_id: "350"
title: "How I Organize My Second Brain Using Obsidian Bases + Claude Code"
creator: "Noah Vincent"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=r4nea7QCkfQ"
date: "2026-03-20"
duration: "25:58"
type: "video"
tags: ["claude-code", "prompt-engineering", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials"]
---

# 350: How I Organize My Second Brain Using Obsidian Bases + Claude Code

> **Creator**: Noah Vincent | **Platform**: YouTube | **Date**: 2026-03-20 | **Duration**: 25:58

# How I Organize My Second Brain Using Obsidian Bases + Claude Code

## Summary

Noah Vincent presents a PKM (personal knowledge management) architecture that replaces folder-based organization with a flat-note system navigated through Obsidian's Bases feature and YAML metadata properties. The core insight is that folders force a single-location decision for every note, creating cognitive overhead at both capture and retrieval time. By storing all notes in a single flat folder and tagging them with `categories` and `subjects` properties, notes become findable from multiple angles simultaneously—something hierarchical folder structures like PARA fundamentally cannot achieve.

The architecture uses two navigation layers: **categories** (what type of object a note is—YouTube script, newsletter, book, SOP) and **subjects** (what topic it concerns—psychology, AI, creativity). Each category and subject is itself a note containing an embedded Obsidian Base that dynamically queries all notes linking back to it. Templates auto-fill the YAML frontmatter on note creation, meaning the organizational work happens in one keystroke rather than through deliberate folder placement.

Claude Code is positioned as an automation layer sitting alongside Obsidian—particularly for processing the inbox. The video promises a free downloadable vault template and frames Claude Code as handling the "emptying" of captured material, though the detailed Claude Code workflow is implied rather than fully demonstrated in the available transcript portion.

## Key Concepts

### Flat-Folder + Metadata Architecture
All notes live in a single `/notes` directory with no subfolders. Organization is entirely expressed through YAML frontmatter properties (`categories`, `subjects`, `status`, `type`) rather than file location. This eliminates the "where does this belong?" decision at capture time and replaces it with "what is this and what is it about?"—a lighter cognitive lift that can also be templated away entirely.

### Obsidian Bases as Dynamic Filtered Views
Bases is a native Obsidian plugin that turns notes into queryable databases (similar to Notion). Each category and subject note contains an embedded Base with a filter rule: *show all notes in this vault that link to this file*. Because the link exists in YAML rather than folder path, a single note can satisfy multiple containers simultaneously—a YouTube script tagged with both `YouTube Videos` and `Scripts` appears in both views with no duplication or compromise.

### Categories vs. Subjects as Orthogonal Axes
Categories answer **what type** of object a note is (newsletter, permanent note, project, book). Subjects answer **what topic** it concerns (AI, productivity, psychology). These two axes are independent and combinable: a newsletter about psychology appears in the Newsletter category container *and* the Psychology subject container. This two-dimensional retrieval replaces both folder hierarchies and tag-based systems, while being more visible and navigable than Obsidian tags.

### Template-Driven Auto-Organization
Each category has a corresponding note template that pre-populates all required YAML frontmatter. Applying the "Newsletter" template auto-inserts `categories: [[Newsletter]]`, a default status, and a content scaffold. The organizational act collapses to a single template selection at note creation—no manual property typing required. This is the mechanism that makes the system low-friction enough to sustain.

### Claude Code as Inbox Processor
Claude Code (run via terminal alongside Obsidian) is used to automate the processing of the inbox folder. Captured raw notes land in `/inbox` and Claude Code handles classification, template application, or routing—offloading the triage step that would otherwise require manual review. This closes the loop on frictionless capture without creating a backlog burden.

## Practical Takeaways

- **Collapse all notes into one flat folder** and resist the urge to create subfolders—the navigation layer is built from metadata, not file paths, so location carries no meaning.
- **Design categories around object types you actually produce**, not abstract domains (e.g., "Newsletter," "YouTube Script," "SOP" rather than "Content" or "Work"). This makes template selection obvious and reduces ambiguity.
- **Use YAML links (not plain text) for category and subject properties**—the `[[WikiLink]]` syntax is what Obsidian Bases filters on; plain text strings won't be picked up by the dynamic views.
- **Build one template per category** that auto-fills all frontmatter; the goal is that the writer never manually types a property value—organization becomes a side-effect of note creation rather than a separate task.
- **Let Claude Code handle inbox triage** rather than scheduling manual processing sessions; pairing an AI agent with a structured metadata schema means raw captures can be automatically classified and routed without human review of each item.

## Notable Quotes

> "With folders, every time you open your second brain, you have to manage the system instead of using it. And the system that was supposed to free up thinking instead is consuming it."

> "In the folder system, you store notes by deciding where they belong. But in this system, you tag notes by what they are and then the system finds them for you."

> "The moment it clicked for me is that I realized I had stopped thinking about where to put notes and I was just thinking about what I was writing—because it's a big mental shift."
