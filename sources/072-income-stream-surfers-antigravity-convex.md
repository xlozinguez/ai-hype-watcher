---
source_id: "072"
title: "Build ANYTHING: Google Antigravity + Convex + Clerk"
creator: "Income stream surfers"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=tamKDJ9n91k"
date: "2026-02-14"
duration: "09:41"
type: "video"
tags: ["vibe-coding", "ai-landscape"]
curriculum_modules: ["02-prompting-and-workflows"]
---

# 072: Build ANYTHING: Google Antigravity + Convex + Clerk

> **Creator**: Income stream surfers | **Platform**: YouTube | **Date**: 2026-02-14 | **Duration**: 09:41

## Summary

A practical walkthrough demonstrating how to scaffold a full SaaS application in roughly 15 minutes using Google AI Studio (Antigravity), Convex as a backend/database, and Clerk for authentication. The creator responds to a common viewer complaint — "vibe coding never works for me" — by showing that the real issue is trying to build everything in a single giant prompt rather than incrementally setting up the project's foundation first.

The video is a lightweight tutorial with limited critical analysis, but it captures the current state of low-friction app scaffolding and illustrates both the appeal and the shallow ceiling of the "build fast" approach. The creator uses Gemini 3 Flash (explicitly called "not the best model") to prove that even weaker models can handle structured, step-by-step prompting.

## Key Concepts

### Incremental Foundation Over Monolithic Prompts

The central thesis is that vibe coding fails when people dump a massive prompt and expect a working app. Instead, the creator advocates setting up authentication, database, and backend incrementally — each step verified before moving to the next. This echoes the spec-first philosophy seen in more rigorous workflows, albeit at a much simpler level.

### Backend-as-a-Service Stack (Convex + Clerk)

The workflow chains together Convex (real-time backend/database) and Clerk (auth) as pre-configured building blocks before adding AI-generated UI on top. The pattern reduces the surface area that AI needs to handle, making success more likely even with weaker models.

### Speed vs. Completeness Trade-off

The creator acknowledges the result is not a complete SaaS — it lacks Stripe, a homepage, and polish. The 15-minute build demonstrates scaffolding velocity but not product readiness, which is a recurring gap in vibe-coding content.

## Practical Takeaways

- **Set up infrastructure before prompting for features**: Auth, database, and backend should be configured and verified before asking AI to build UI or business logic.
- **Tag rules files for better results**: The creator notes that tagging `convex-rules.mdc` improves model output when using weaker models like Gemini 3 Flash.
- **Verify each integration step**: Checking that users actually appear in the Convex database after sign-up prevents compounding errors downstream.

## Notable Quotes

> "This is the biggest mistake that people do with vibe coding — they don't spend the time to sit and make sure that everything is working first." — Income stream surfers ([06:00](https://www.youtube.com/watch?v=tamKDJ9n91k&t=360))

> "If I had tried to do this with vibe coding where I just gave this giant prompt to even Claude Code, it would have taken a lot longer and it probably wouldn't have even managed to do it." — Income stream surfers ([09:04](https://www.youtube.com/watch?v=tamKDJ9n91k&t=544))

## Related Sources

- [005: Most People Aren't Ready for Vibe Coding](005-nate-b-jones-vibe-coding-readiness.md) — Nate B Jones makes the same argument about incremental specification vs. monolithic prompting at a more conceptual level
- [042: Vibe Coding is a Trap](042-devforge-vibe-coding-trap.md) — DevForge's senior dev perspective on the gap between scaffolding speed and production readiness

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Illustrates the incremental prompting workflow vs. single-shot approach
