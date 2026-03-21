---
source_id: "343"
title: "How to Design ACTUALLY Beautiful Apps With Google Stitch + Claude Code"
creator: "Build Great Products"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=sZQ7lqaOGMg"
date: "2026-03-19"
duration: "21:25"
type: "video"
tags: ["claude-code", "mcp", "prompt-engineering", "specification", "vibe-coding"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials"]
---

# 343: How to Design ACTUALLY Beautiful Apps With Google Stitch + Claude Code

> **Creator**: Build Great Products | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 21:25

# How to Design ACTUALLY Beautiful Apps With Google Stitch + Claude Code

## Summary

This video demonstrates a workflow for transforming visually generic "vibecoded" apps into polished, professional-looking interfaces using Google Stitch's new design systems feature combined with Claude Code. The creator, Chris (a 15-year product design veteran), walks through taking screenshots of an existing basic app, feeding them into Google Stitch with design direction prompts, and generating a complete design system — including color palettes, typography scales, and component rules — all captured in a `design.md` file.

The central insight is that Google Stitch's new `design.md` paradigm solves a persistent problem in AI-assisted development: how to maintain consistent design language across an entire codebase as you continue building with AI tools. Rather than ad-hoc styling, the workflow produces a structured markdown design system file that Claude Code can reference as a specification when restyling any part of the application.

The video also covers using the Google Stitch MCP (Model Context Protocol) integration with Claude Code, which allows the AI coding agent to directly access the design assets, component code, and design tokens from Stitch — going beyond just the markdown documentation to pull actual implementation-ready styles into the project.

## Key Concepts

### design.md as a Design System Specification
Google Stitch now auto-generates a `design.md` file as part of every project — a markdown document containing the full design system: typography scales (display, headline, label, body), color palettes with tonal scales, elevation/depth rules, component specifications, and explicit dos and don'ts. This file acts as a machine-readable design specification that AI coding tools like Claude Code can consume directly. The pattern mirrors `CLAUDE.md` for project behavior, but focused purely on visual design language.

### Screenshot-to-Redesign Workflow
The practical workflow starts by taking screenshots of an existing (potentially ugly) app and uploading them to Google Stitch alongside a design direction prompt. Stitch's agent interprets the current structure, applies the requested aesthetic (dark mode, editorial, minimal, etc.), generates complementary color palettes, recommends font pairings, and produces redesigned screen mockups — all without needing Figma files or manual design work. This makes it accessible to non-designers building real products.

### Google Stitch MCP Integration with Claude Code
Beyond copy-pasting the `design.md` file, Google Stitch exposes an MCP server that Claude Code can connect to directly. This allows Claude Code to access not just the design documentation but the actual component code and design tokens from Stitch in real-time. Setup requires generating an API key in Stitch settings and running the install command for Claude Code from the Stitch MCP documentation page.

### Iterative Design Refinement via Prompt
Google Stitch treats design iteration as a conversational agent interaction. After the initial generation, you can prompt further changes (e.g., "change primary color from purple to something warmer and more editorial") and Stitch updates both the visual designs and the underlying design system simultaneously, creating a new versioned design system. This keeps the `design.md` spec and the visual designs in sync throughout iteration.

### Plan Mode Before Applying Styles
The creator recommends switching Claude Code into plan mode before executing the redesign, prompting it to "create a plan to redesign the entire UI using the exact instructions from design.md." This surfaces how well the AI has understood the design spec before it starts making file changes — a validation step that reduces the risk of inconsistent or incorrect style application across a large codebase.

## Practical Takeaways

- **Copy `design.md` into your project root** as a first-class specification file; Claude Code will reference it automatically when given redesign tasks, similar to how `CLAUDE.md` governs agent behavior.
- **Start with screenshots of your existing app**, not a blank canvas — this grounds Stitch in your actual UI structure so redesigns preserve functionality while upgrading aesthetics.
- **Use plan mode in Claude Code before applying design changes** to verify the agent's interpretation of the design spec matches your intent, especially when restyling many components at once.
- **Install the Google Stitch MCP** for richer integration beyond markdown — it gives Claude Code access to actual component code and design tokens, reducing translation loss between design intent and implementation.
- **Iterate on design system colors and fonts via prompts** before exporting to code; changes made in Stitch propagate to the `design.md` file, so your specification stays current with your visual decisions.

## Notable Quotes

> "Design.md really represents a step change in the way that we approach design, creating design systems and applying them to our applications using AI coding tools."

> "This is basically solving that problem — how do I design apps that actually look good and not like AI slop? And how do I maintain those styles throughout the rest of my app as I continue to build it with AI?"

> "This is probably one of the fastest ways of going from an existing kind of vibecoded app that you have that kind of looks a bit AI sloppy into something that actually has like a professional look and feel to it."
