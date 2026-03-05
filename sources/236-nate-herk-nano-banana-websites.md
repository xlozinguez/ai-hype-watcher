---
source_id: "236"
title: "The NEW Nano Banana 2 + Claude Code = $10k Websites"
creator: "Nate Herk"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=q0TgUtj6vIs"
date: "2026-03-03"
duration: "20:15"
type: "video"
tags: ["claude-code", "skills", "vibe-coding"]
curriculum_modules: ["03-claude-code-essentials"]
---

# 236: Nano Banana 2 + Claude Code = $10k Websites

> **Creator**: Nate Herk | **Platform**: YouTube | **Date**: 2026-03-03 | **Duration**: 20:15

## Summary

Nate Herk demonstrates a workflow for building premium animated product landing pages using Claude Code skills combined with Nano Banana 2 (an image generation model) and Cling 3.0 (a video generation model). The process involves generating product images, creating transition videos between states (e.g., empty blender to filled blender), then using a custom Claude Code skill to build scroll-driven animated websites from those videos.

The video walks through the complete pipeline from image generation to deployed website, showing how Claude Code's plan mode, skills, and iterative feedback loop produce professional-looking results. The key technical mechanism is frame extraction — ffmpeg splits the video into individual frames that are then associated with scroll positions, creating a stop-motion animation effect as users scroll through the page.

## Key Concepts

### Video-to-Website Skill Pipeline

The workflow chains multiple AI tools: Nano Banana 2 generates start and end frame images, Cling 3.0 interpolates between them to create a video, and a custom Claude Code skill converts the video into a scroll-driven animated website. The skill handles frame extraction via ffmpeg, HTML/CSS/JS generation, and scroll position mapping. This demonstrates how skills can encode complex multi-tool workflows into repeatable processes.

### Plan Mode for Quality Control

Using Claude Code's plan mode before implementation produces significantly better results on the first try. The agent reads the video, asks clarifying questions about branding and layout preferences, and produces a detailed implementation plan before writing any code. This plan-first approach reduces iteration cycles and gives the user control over creative direction before tokens are spent on implementation.

### Iterative Skill Refinement

Each website built with the skill generates feedback that can be folded back into the skill itself — fixing timing issues, layout preferences, and animation behavior. This creates a flywheel where the skill improves with every use, encoding accumulated best practices for scroll-driven animated websites.

## Practical Takeaways

- **Use plan mode for creative projects**: Let Claude Code read inputs and create a detailed plan before implementation — it produces better first iterations and saves context
- **Chain AI tools via skills**: Encode multi-tool pipelines (image gen, video gen, web development) into skills for repeatable workflows
- **Clear context between iterations**: At 50%+ context usage, start a new conversation to avoid context rot when iterating on designs
- **Deploy with GitHub + Vercel**: Claude Code can handle the entire deployment pipeline from local development to live URL

## Notable Quotes

> "I dropped in a prompt that said, 'Here's a video. Create a one-page landing page.' That was basically it. It used the skill and it created a plan for us." — Nate Herk

## Related Sources

- [156: Build Beautiful Diagrams with Claude Code](156-cole-medin-diagrams-workflow.md) — Creative output workflows with Claude Code
- [146: Anthropic Just Dropped Claude Code Skills 2.0](146-ray-amjad-skills-upgrade.md) — Skills system capabilities

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills, plan mode, and iterative workflows
