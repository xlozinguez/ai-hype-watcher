---
source_id: "312"
title: "Claude Code + Nano Banana 2 + Kling =  $15K Animated Sites"
creator: "Nick Saraev"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=ZfYvv-0l9NA"
date: "2026-03-16"
duration: "13:58"
type: "video"
tags: ["claude-code", "skills", "vibe-coding", "agentic-coding", "ai-economics", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 312: Claude Code + Nano Banana 2 + Kling =  $15K Animated Sites

> **Creator**: Nick Saraev | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 13:58

## Summary

Nick Saraev demonstrates a three-step workflow for building high-end animated websites in under 15 minutes for roughly $2–5 in AI tokens. The core stack combines Claude Code (accessed via an IDE called "anti-gravity") with a community-shared skills repository called "Nano Banana 2" (created by a 16-year-old and shared on Twitter) to enforce luxury design principles, plus Kling 3.0 via Higsfield for AI-generated video assets. The result is websites that would previously have cost $5,000–$10,000 to commission from a professional agency.

The workflow is: (1) pass the Nano Banana skill URL to Claude Code to prime it with high-end design principles, (2) generate 3D animated video assets using Kling 3.0 at ~$0.36 per clip, and (3) instruct Claude Code to integrate the video as background hero media with scroll-sequenced frame extraction. The video walks through live construction of an interior design landing page, showing iterative prompting to fix text visibility, gradient masking, scroll choppiness, and asset compression—all via plain English instructions.

A key performance optimization is demonstrated: when a scroll-sequenced animation runs slowly, Claude Code automatically extracts video frames as optimized JPEGs, ties each frame to scroll position, and adds preloading—a task the creator estimates would have taken a professional web developer three days to implement manually. Hosting is described as free (likely via static site deployment), bringing total cost to approximately $5 per site.

---

## Key Concepts

### Nano Banana 2 Skill (Community Design Skill)
A publicly shared Claude Code skill repository that encodes high-end website design principles—spacing, luxury aesthetics, layout schematics—into a reusable context. By passing the repo URL to Claude Code at the start of a session, it enables consistent one-shot generation of polished landing pages without per-prompt design instruction. This illustrates how the skills ecosystem democratizes specialized design knowledge.

### AI Video Asset Generation with Kling 3.0
Kling 3.0 (accessed via Higsfield) generates short 3D-rendered video clips (e.g., rotating globes, exploding house diagrams, interior pans) that serve as animated hero backgrounds and scroll-sequenced assets. At ~7.5 credits per clip and $29/600 credits on the pro plan, individual assets cost roughly $0.36. Running two or three generations in parallel improves output quality selection without significant cost increase.

### Scroll-Sequenced Video Frame Extraction
Rather than embedding raw MP4s in scroll animations (which causes lag), Claude Code extracts individual video frames as compressed JPEGs, maps each frame to a scroll position, and implements preloading. This pattern converts a heavy cinematic asset into a performant web experience. The creator notes this would have been a multi-day engineering task previously accomplished in ~30 seconds of agentic execution.

### Iterative Plain-English Refinement
The workflow demonstrates a tight feedback loop: take a screenshot, describe the visual problem in plain English ("the fuzzy gradient isn't strong enough," "make it load significantly faster"), and let Claude Code resolve both the diagnosis and the implementation. No specific technical instructions are needed—the model infers the correct optimization strategy (JPEG extraction, preloading, compression from 5.3MB to 252KB).

### Economics of AI-Generated Web Deliverables
The video explicitly benchmarks the cost collapse: $5,000–$10,000 agency sites now cost ~$5 in tokens. The breakdown is ~$3–4 for Kling video generation (2–3 clips), ~$1 for Claude Code tokens, and $0 for hosting. This reframes web design as a near-zero marginal cost deliverable, with the title's "$15K" figure representing former market rate, not current cost.

---

## Practical Takeaways

- **Prepend any Claude Code session with a design skill URL** to get consistent, high-quality one-shot output without verbose per-prompt design instructions—the Nano Banana 2 repo is a working example of this pattern.
- **Generate 2–3 Kling video variants simultaneously** when you have credits to spare; parallel generation is cheap (~$0.36/clip) and dramatically improves the chance of getting a usable output on the first pass.
- **Use plain-English performance directives** ("make it load significantly faster") rather than prescribing technical solutions—Claude Code will infer and implement the correct optimization (frame extraction, preloading, compression) autonomously.
- **Inward masking gradients** are the standard fix for video-background bleed into surrounding site sections; prompt Claude Code to apply them by default when integrating any video asset into a hero header.
- **Static/free hosting** eliminates the final cost variable—combine with ~$5 in AI spend to deliver a complete animated site, making this viable for high-volume freelance or agency production.

---

## Notable Quotes

> "A few years back, this would probably be $5 to $10,000 a pop. And I know that because I used to sell websites for a living. Now you can literally do it in less than 10 minutes for somewhere around $2 to $3 in tokens."

> "As a former web developer, some of the stuff that this thing does blows my mind. It would have taken me like 3 days to do what this just did in 30 seconds."

> "Isn't that wild how you could literally just say 'make it load significantly faster.'"

---
