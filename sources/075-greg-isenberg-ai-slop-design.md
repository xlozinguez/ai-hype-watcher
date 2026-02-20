---
source_id: "075"
title: "Stop Shipping AI Slop. Design with Weavy AI, Claude etc."
creator: "Greg Isenberg"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=9OnN4O4uapI"
date: "2026-02-13"
duration: "54:12"
type: "video"
tags: ["vibe-coding", "ai-landscape", "prompt-engineering"]
curriculum_modules: ["02-prompting-and-workflows"]
---

# 075: Stop Shipping AI Slop. Design with Weavy AI, Claude etc.

> **Creator**: Greg Isenberg | **Platform**: YouTube | **Date**: 2026-02-13 | **Duration**: 54:12

## Summary

A detailed walkthrough with designer Sariah (who sold her last company to Snap) demonstrating how to transform a generic vibe-coded app into a professionally branded product. The core argument is that vibe coding has solved the "what does the app do" problem but has created a new problem: everything looks the same and nobody wants to download yet another generic app. The solution is a design-first workflow that chains together Claude (for brand strategy and prompt generation), Weavy AI (for visual asset generation using node-based AI pipelines), Cosmos (mood boards), Figma (composition), and image models like Flux 2 Pro and Ideogram v3.

The episode uses a voice journaling app called "Cassette" as a live demo, taking it from a generic Google AI Studio prototype to a distinctive analog-themed product with cassette tape metaphors, custom AI-generated assets, and cohesive branding — all for roughly 30-40 Weavy credits (essentially free on the free tier).

## Key Concepts

### The AI Slop Problem

Vibe coding tools can now build functional apps quickly, but the results are visually homogeneous — they all look like the same AI generated them. In a crowded app market, this means nobody downloads your app because it looks like everything else. The "what it does" is a solved problem; "how it makes you feel" is the differentiator.

### Feelings-First Design

Before touching any visual tool, the workflow starts by defining how the app should make users feel. For the journaling app: calm, analog, not screen-like, not needy. These emotional specifications become the filter for every subsequent design decision — from color palettes to button styles to the core metaphor (cassette tapes that age with use).

### AI-Assisted Brand Pipeline

The practical workflow chains multiple AI tools in a specific sequence: (1) Claude for defining brand personality and generating prompts, (2) Cosmos for mood board inspiration, (3) Weavy AI with Flux 2 Pro for generating visual assets from mood board references, (4) Ideogram v3 for typography and logos, (5) Figma for compositing, and (6) Google AI Studio for one-shot prototyping from the composed references. Claude serves as the brainstorming and prompt-refinement layer throughout.

### One Image as Brand Foundation

A key insight: find one image you love and build the entire brand around it. Sariah notes that Jony Ive built Apple's design language from Dieter Rams' 1950s-60s work — the same pattern applies here. The "used cassette tape" image became the anchor for the entire Cassette app's visual identity.

## Practical Takeaways

- **Define emotional specifications before visual design**: Write out how users should feel, what the app is not, and who you are building for — then use Claude to expand this into brand guidelines.
- **Use Weavy AI for rapid asset generation**: Feed mood board images as inputs to Flux 2 Pro for color palettes, buttons, and visual elements; use Ideogram v3 for logos and typography.
- **Maintain consistency through color palettes, not character consistency**: Product design is easier than character consistency in AI images — you just need colors, shadows, and lighting to match.
- **Remove backgrounds as a final composition step**: Generate assets with whatever background AI produces, then use Weavy's background removal to make them compositable in Figma.
- **Claude Code is the preferred tool for real codebase work**: Sariah confirms Claude Code as her primary tool for day-to-day development, with Cursor + Gemini model for UI/shader work.

## Notable Quotes

> "Anyone can build an app now. It's amazing. So much has changed, but now everything looks the same." — Sariah ([03:52](https://www.youtube.com/watch?v=9OnN4O4uapI&t=232))

> "Most people stop here — vibe coding focuses a lot on what does the thing do. But that's not what a product is." — Sariah ([09:14](https://www.youtube.com/watch?v=9OnN4O4uapI&t=554))

> "Really the only benefit of being a designer at this point is knowing maybe a little bit about what to react to, but that's really really minuscule." — Sariah ([38:07](https://www.youtube.com/watch?v=9OnN4O4uapI&t=2287))

## Related Sources

- [042: Vibe Coding is a Trap](042-devforge-vibe-coding-trap.md) — The technical debt side of shipping fast without design thinking
- [038: When the Interface Flattens Into a Prompt](038-interface-studies-prompt-interface.md) — Deeper analysis of how AI is collapsing design and specification into prompting
- [005: Most People Aren't Ready for Vibe Coding](005-nate-b-jones-vibe-coding-readiness.md) — The specification gap that this design workflow helps address

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Multi-tool AI workflow patterns for design and prototyping
