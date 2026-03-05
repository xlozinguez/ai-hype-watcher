---
source_id: "232"
title: "Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)"
creator: "Cole Medin"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=m3fqyXZ4k4I"
date: "2026-03-02"
duration: "9:53"
type: "video"
tags: ["claude-code", "skills", "validation"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 232: Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)

> **Creator**: Cole Medin | **Platform**: YouTube | **Date**: 2026-03-02 | **Duration**: 9:53

## Summary

Cole Medin shares a Claude Code skill he built for generating Excalidraw diagrams, packaging his entire visual workflow into a reusable, open-source skill. The skill teaches Claude Code how to "argue visually" — creating diagrams that convey concepts through structure and layout, not just boxes and text. The workflow includes a self-validation loop where the agent renders the diagram as a PNG, examines the screenshot, and iterates on imperfections before returning control to the user.

The video demonstrates a practical philosophy: coding agents are inherently weak at visual tasks, so the skill compensates by giving them explicit design patterns, color palettes, and validation criteria. Medin is transparent that diagrams are never perfect on the first pass (too many micro-decisions for any LLM) but emphasizes that the skill creates an excellent starting point that takes 2-3 iterations to refine — saving hours of manual work weekly.

## Key Concepts

### Teaching Agents to Argue Visually

The skill's core philosophy is that diagrams should make visual arguments, not just display information. The LLM is prompted to ask itself: "Does the visual structure mirror the concept's behavior?" and "Could someone learn something concrete from this diagram?" The skill includes design pattern examples to prevent the default LLM behavior of producing simplistic box-and-arrow layouts.

### Self-Validation Loop

After generating the Excalidraw JSON, the agent renders it as a PNG using a Python script, views the image, identifies imperfections (janky arrows, poor colors, missing information), and directly edits the JSON. This typically runs 2-4 iterations. The pattern compensates for the LLM's lack of visual reasoning by giving it explicit feedback on its own output.

### Depth Assessment for Complex Diagrams

The workflow first assesses diagram complexity. Simple diagrams can be generated in one pass, but complex ones must be built section by section to avoid hitting Claude Code's 32,000-token output limit. This adaptive approach prevents errors while supporting both simple concept maps and detailed multi-section architectures.

### Customizable Color Palettes and Design Patterns

The skill includes a reference folder with color palette definitions (hex codes for consistent branding) and element templates. Users can customize these to match their brand or preferences, and the agent will consistently apply them across all generated diagrams.

## Practical Takeaways

- **Package visual workflows as skills**: If you create diagrams regularly, encode your design preferences, color palettes, and validation criteria into a Claude Code skill for repeatable results.
- **Use self-validation for visual output**: Have the agent render its output, examine the result, and iterate — essential for any task where the LLM cannot directly perceive quality.
- **Expect 2-3 iterations**: LLMs make too many micro-decisions (color, layout, positioning) for first-pass perfection. The skill provides a starting point, not a finished product.
- **Build section by section for complex diagrams**: Break large diagrams into chunks to stay within token output limits.
- **Excalidraw works with Obsidian and the web**: Render diagrams via excalidraw.com (free) or the Obsidian Excalidraw plugin — no paid tools required.

## Notable Quotes

> "Coding agents are not very visual tools. They need the ability to check their own work, and we can do that with Excalidraw." — Cole Medin

> "It has to decide every color, every shape, the entire layout, the position of everything. There's so many micro decisions going into creating just this single rather simple diagram." — Cole Medin

## Related Sources

- [149: How to Use Claude Code Skills Like the 1%](149-simon-scrapes-skills-top1.md) — Skills design patterns and best practices

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system, reference files, skill packaging
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Self-validation loops, builder-validator pattern
