---
source_id: "312"
title: "Claude Code + Nano Banana 2 + Kling =  $15K Animated Sites"
creator: "Nick Saraev"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=ZfYvv-0l9NA"
date: "2026-03-16"
duration: "13:58"
type: "video"
tags: ["claude-code", "skills", "skills-ecosystem", "vibe-coding", "prompt-engineering", "ai-economics", "capability-overhang"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 312: Claude Code + Nano Banana 2 + Kling =  $15K Animated Sites

> **Creator**: Nick Saraev | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 13:58

## Summary

Nick Saraev demonstrates a three-step workflow for building high-end animated marketing websites in under 15 minutes for approximately $2–5 in token/credit costs. The pipeline combines Claude Code (via an "anti-gravity" IDE setup) with a community-shared Claude skill called "Nano Banana 2" — created by a 16-year-old and shared on Twitter — that instills luxury design principles and spacing schematics into the model, enabling consistent one-shot website generation from minimal prompts. The third component is Kling 3.0 (accessed via Higgsfield) for generating bespoke 3D animated video assets that are then integrated as hero headers and scroll-sequenced backgrounds.

The workflow illustrates how the Claude skills ecosystem dramatically lowers the barrier to high-quality output: rather than crafting elaborate prompts from scratch, users reference a shared skill URL and Claude fetches the design principles automatically. The video generation step (roughly $0.37 per clip at Higgsfield Pro pricing) produces assets like rotating globes, exploding-view architecture diagrams, and panning interior scenes that previously would have required motion graphics professionals. Claude Code then handles the technical integration work — frame extraction, JPEG pre-loading for scroll sequences, gradient masking, and asset compression — through plain-language instructions.

The creator contextualizes the economics explicitly: websites of this caliber previously sold for $5,000–$10,000 and took days of developer time. The total cost here is approximately $3–5 in Kling credits plus ~$1 in Claude Code tokens, with hosting free. This represents a concrete, reproducible example of the capability-adoption gap closing in real time for freelance and agency web development work.

---

## Key Concepts

### The Nano Banana 2 Skill (Community Claude Skill)
A publicly shared Claude Code skill repository created by a community member and distributed via Twitter/X. When referenced by URL in a Claude Code prompt, it automatically fetches and applies a set of high-end website design principles — luxury spacing, visual hierarchy, component schematics — that produce consistent, polished one-shot results without requiring the user to encode those principles in every prompt. This is a live example of the skills ecosystem in action: reusable, shareable, community-vetted design context injected into the model's working context.

### AI Video Generation as Web Asset Production
Kling 3.0 (via Higgsfield) is used not for narrative video but as a tool for generating short, looping 3D animated assets — rotating globes, exploding architectural diagrams, panning interior scenes — specifically designed for use as website backgrounds and scroll sequences. The prompting strategy emphasizes white backgrounds, no text, 16:9 aspect ratio, and bounded motion so assets integrate cleanly into web layouts. Generating 2–3 variants per asset and selecting the best is recommended at the low per-clip cost (~$0.37 each).

### Scroll-Sequenced Video via Frame Extraction
Rather than embedding raw MP4 files (which cause lag), Claude Code is instructed to extract video frames as optimized JPEGs and bind each frame to the scroll position using locomotive scroll or similar libraries. This technique — which the creator notes would have taken him three days as a working web developer — is accomplished through a plain-language instruction to "make it load significantly faster." Claude Code autonomously handles the frame extraction, pre-loading logic, and scroll binding, compressing assets significantly (demonstrated: 5.3MB → 252KB for a hero video).

### Iterative Plain-Language Refinement
The entire polish cycle — fixing text contrast, smoothing animation choppiness, strengthening gradient masks, compressing assets — is accomplished through conversational follow-up prompts like "make it load significantly faster" and "the fuzzy gradient isn't strong enough." This represents the practical workflow pattern for vibe-coding polished production assets: one-shot the structure, then iterate on aesthetics and performance through natural language without touching code manually.

### Skills as Design System Injection
The Nano Banana 2 skill functions as a portable design system: it standardizes luxury aesthetics across projects without requiring the user to re-specify design principles each time. This pattern — encoding domain expertise (here: high-end web design) into a shareable skill that can be fetched by reference — generalizes beyond web dev to any domain where consistent quality standards need to be applied repeatedly across Claude Code sessions.

---

## Practical Takeaways

- **Reference community skills by URL in your Claude Code prompt** to inherit battle-tested design or domain principles without manual prompt engineering — search Twitter/X and GitHub for shared skills relevant to your use case before writing prompts from scratch.
- **Use Kling 3.0 (via Higgsfield) for web asset generation**, not just video content: prompt for white backgrounds, no text, bounded motion, and 16:9 format to produce drop-in hero and scroll assets. Generate 2–3 variants per asset to maximize selection quality.
- **Instruct Claude Code to extract video frames as pre-loaded JPEGs** tied to scroll position rather than embedding raw MP4 for scroll animations — this is the practical fix for laggy scroll-jacked video sequences and can be requested in plain language.
- **Budget realistically**: ~$1 in Claude Code tokens + $3–4 in Kling credits covers a full animated landing page. Hosting via free tiers (Vercel, Netlify, etc.) keeps the total under $5.
- **Iterate on performance and polish verbally**: compression, gradient tuning, text contrast, and animation smoothing are all achievable through follow-up natural language instructions — treat Claude Code as a senior developer you can direct without knowing the implementation details.

---

## Notable Quotes

> "A few years back, this would probably be $5 to $10,000 a pop. And I know that because I used to sell websites for a living. Now you can literally do it in less than 10 minutes for somewhere around $2 to $3 in tokens."

> "As a former web developer, some of the stuff that this thing does blows my mind. It would have taken me like 3 days to do what this just did in 30 seconds."

> "You can do that three or four times and then assess whatever the quality decreases to get it to that fast point and then eventually have like a really really clean look despite it also being pretty heavy asset-wise."

---
