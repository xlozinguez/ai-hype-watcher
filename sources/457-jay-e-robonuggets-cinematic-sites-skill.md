---
source_id: "457"
title: "This AI Agent Builds $15K Cinematic Websites on Autopilot (Claude Code + Nanobanana 2)"
creator: "Jay E | RoboNuggets"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=bUt1WpDlI6E"
date: "2026-04-01"
duration: "15:59"
type: "video"
tags: ["claude-code", "skills", "agentic-coding", "meta-prompts", "prompt-engineering"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 457: This AI Agent Builds $15K Cinematic Websites on Autopilot (Claude Code + Nanobanana 2)

> **Creator**: Jay E | RoboNuggets | **Platform**: YouTube | **Date**: 2026-04-01 | **Duration**: 15:59

# This AI Agent Builds Cinematic Websites on Autopilot (Claude Code + Imagen 3)

## Summary

Jay from RoboNuggets demonstrates a multi-step agentic workflow he calls "Cinematic Sites" that automates the creation of high-end, scroll-animated websites from a single input URL. The agent — driven by a `skill.md` instruction file — analyzes an existing website's brand identity, generates AI imagery and video scenes, then scaffolds a fully animated HTML/CSS site and deploys it to Vercel. The demo runs via a Telegram-connected Claude Code session, illustrating how a long-running agent terminal session can be orchestrated through conversational interfaces.

The core technical stack chains Google's Imagen 3 (accessed via free $300 Google Cloud credits) for image generation, Kling v3 via WaveSpeed for image-to-video animation, and Claude Code for orchestration, brand analysis, and HTML/CSS construction. The "cinematic" effect is achieved by extracting individual frames from the generated video and mapping them to scroll position, creating a parallax-style scrub animation. The entire four-step pipeline — brand analysis → scene generation → website build → deployment — is encoded in a single markdown skill file that any compatible agentic platform can consume.

The video is primarily a product showcase for the creator's community ("RoboNuggets"), but contains meaningful practical content about how skills-based agent workflows chain external APIs, manage human approval checkpoints, and use free-tier cloud credits to reduce costs. The pattern of feeding API documentation directly to an agent so it can self-configure tool calls is highlighted as a reusable technique.

---

## Key Concepts

### Skill Files as Agent Instruction Manuals
The entire workflow is encoded in a `skill.md` markdown file that functions as a structured instruction manual. It defines the four pipeline steps, methodology for brand extraction, code templates for API calls (Imagen 3, Kling), design system rules, and explicit pause/approval points. This makes the workflow portable across Claude Code, OpenClaw, and other agentic platforms — the skill is the unit of capability transfer, not the platform.

### Human-in-the-Loop Approval Checkpoints
The pipeline deliberately pauses at two points: after brand card generation (so the user can verify colors, typography, and messaging) and after scene/video generation (so the user can select the best output before the site is built). This reflects a practical pattern for probabilistic generative outputs — volume + human selection beats automated single-pass selection, especially for visual creative work.

### Feeding API Documentation to Agents for Self-Configuration
Rather than hardcoding tool integrations, the creator's approach is to paste the raw documentation page (e.g., WaveSpeed's Kling API docs, Google's Imagen API docs) directly into the agent context. The agent then reads the documentation and constructs the correct API calls autonomously. This is a scalable pattern for adding new tool capabilities without manual prompt engineering for each integration.

### Free Cloud Credits as Cost Arbitrage
The workflow defaults to Google Cloud's Imagen 3 API specifically because new Gmail accounts receive $300 in free credits — enough for substantial image generation volume. Combined with WaveSpeed's pay-per-use model (no subscription), this keeps per-site costs low. The creator explicitly frames this as an alternative to subscription platforms like HiDream or Freepik for the same underlying models.

### Scroll-Scrub Video Animation Pattern
The cinematic effect is technically achieved by extracting frames from a short AI-generated video clip and binding each frame's display to the user's scroll position. This creates the illusion of a "video playing as you scroll" without autoplay. The technique is codified in the skill file's design system section, making it a reusable component the agent applies automatically.

---

## Practical Takeaways

- **Structure multi-step agent workflows as numbered skill files** with explicit pause points between stages — this gives you quality control without manual re-prompting at every step.
- **Point agents at raw API documentation URLs** rather than writing wrapper prompts; agents like Claude Code can read and implement from official docs directly, reducing integration overhead.
- **Use volume + human selection for generative media** — generating 2–3 video options and picking the best one outperforms trying to prompt-engineer a single perfect output.
- **Google Cloud's $300 new-account credit** covers substantial Imagen 3 usage; this is a practical cost-reduction lever for client work or prototyping before committing to paid subscriptions.
- **The skill.md pattern is platform-agnostic** — the same instruction file works across Claude Code, OpenClaw, and Telegram-connected agent sessions, making it a transferable asset rather than a platform-locked workflow.

---

## Notable Quotes

> "You don't need to go through third-party resellers like HiDream or Freepick for the same models."

> "For each Gmail account that you have, they actually give you a $300 welcome credit, which lasts you a long time, especially if you're just using their Imagen or VO models."

> "If you want to give your agent the skill to actually use Imagen 3, all you need to do is provide your agent with this link which is just all the documentation that Google has — and your agent will scour this page in order to find the right commands."

---
