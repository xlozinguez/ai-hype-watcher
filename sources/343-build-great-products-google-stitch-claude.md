---
source_id: "343"
title: "Google Stitch + Claude Code = Insane App Design"
creator: "Build Great Products"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=sZQ7lqaOGMg"
date: "2026-03-19"
duration: "21:25"
type: "video"
tags: ["claude-code", "mcp", "vibe-coding", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials"]
---

# 343: Google Stitch + Claude Code = Insane App Design

> **Creator**: Build Great Products | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 21:25

## Summary

Chris from Build Great Products demonstrates a workflow for elevating vibe-coded apps from generic-looking "AI slop" to professional-quality UI using Google Stitch's new design system features combined with Claude Code. The core innovation is Google Stitch's `design.md` paradigm — a markdown file that captures an entire design system (typography, color palettes, spacing, elevation, component rules) in a format that AI coding tools can consume directly.

The video walks through a full loop: importing existing app screenshots into Google Stitch, prompting it to create redesigned screens with professional styling, extracting the auto-generated design system as a `design.md` file, then applying that design system to the actual codebase via Claude Code. A second pass uses the Google Stitch MCP server to give Claude Code direct access to the Stitch designs and their HTML/CSS source code, producing more faithful results than the markdown file alone.

The workflow addresses the persistent gap between design intent and AI-generated code — the same problem that plagues vibe-coding broadly. While Chris acknowledges the approach isn't perfect (fonts and colors don't match 100%), it establishes a design-as-code paradigm that raises the floor for non-designers and gives professional designers a structured way to hand off design intent to AI coding agents.

## Key Concepts

### The design.md Paradigm

Google Stitch now auto-generates a `design.md` file alongside visual designs — a markdown document containing the full design system specification including typography scales, color palettes with shade variants, elevation/depth rules, component guidelines, and explicit dos/don'ts. This file serves as a portable design contract that any AI coding tool can reference. The concept mirrors what many teams were already doing manually by documenting design rules in markdown files, but Stitch automates the generation and keeps it synchronized with visual designs.

### Design System as Context Engineering

The workflow is fundamentally a context engineering problem: how do you give an AI coding agent enough design context to produce visually consistent output? Chris tests two approaches — (1) copying the `design.md` markdown file into the project and referencing it in Claude Code prompts, and (2) using the Google Stitch MCP server so Claude Code can directly query Stitch for design details, screenshots, and HTML/CSS source. The MCP approach produces more faithful results because it gives the agent access to richer context (actual rendered code rather than just written descriptions).

### Bridging the Vibe-Code Quality Gap

The core problem addressed is that AI-coded apps tend toward visual homogeneity — recognizable "AI slop" aesthetics. The Stitch-to-Claude-Code pipeline offers a structured way to break out of generic styling by establishing design direction in a visual tool first, then transferring that intent to code via structured documentation. The design system also helps maintain consistency as the app grows, solving the common problem of style drift during extended AI-assisted development sessions.

## Practical Takeaways

- **Design-first, then code**: Use a visual design tool like Google Stitch to explore design directions before coding, then export the design system as a portable reference file for your AI coding agent.
- **MCP beats markdown for fidelity**: The Google Stitch MCP server gives Claude Code access to actual HTML/CSS source and screenshots, producing more accurate design reproduction than the `design.md` file alone.
- **Watch for feature mismatch**: When using design references, the AI coding agent may try to build features visible in the design mockup that don't exist in the actual app — be explicit about what to include and exclude.
- **Iterative refinement works**: The first pass with `design.md` gets roughly 70-80% of the way there; subsequent prompts with more specific references (MCP, screenshots) close the remaining gap.

## Notable Quotes

> "This is probably one of the fastest ways of going from an existing kind of vibecoded app that you have that kind of looks a bit AI sloppy into something that actually has like a professional look and feel to it." — Build Great Products

> "Design.md is not perfect, but it's giving us a starting point for a design paradigm for how to design in code using a file that stores all of our design system details." — Build Great Products

## Related Sources

- [280: Leon van Zyl - Claude Code Loop](280-leon-van-zyl-claude-code-loop.md) — Both address iterative Claude Code workflows
- [269: Peter Yang - Six Agents App Design](269-peter-yang-six-agents-app-design.md) — Design patterns for AI-built applications

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Design system as structured specification for AI agents
- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — MCP server integration and context file patterns
