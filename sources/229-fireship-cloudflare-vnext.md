---
source_id: "229"
title: "Cloudflare just slop forked Next.js..."
creator: "Fireship"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=abbeIUOCzmw"
date: "2026-03-02"
duration: "5:17"
type: "video"
tags: ["ai-sdlc", "ai-landscape", "vibe-coding"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 229: Cloudflare just slop forked Next.js...

> **Creator**: Fireship | **Platform**: YouTube | **Date**: 2026-03-02 | **Duration**: 5:17

## Summary

Fireship covers Cloudflare's release of V-Next, a re-implementation of the Next.js API built on Vite, and the corporate rivalry it intensified between Cloudflare and Vercel. The project is notable as a case study in AI-assisted large-scale code generation: Cloudflare's team used AI coding agents to rebuild 94% of the Next.js API in one week for approximately $1,100 in tokens. The video tests V-Next on a real app (the Fireship newsletter site) and finds it promising but not production-ready.

The broader significance is what this signals about "slop forks" -- AI-generated reimplementations of open-source projects. Vercel's CTO called V-Next a "slop fork" and pointed out security vulnerabilities. The episode illustrates both the power and limits of AI-assisted coding: impressive speed on the reimplementation itself, but fragility in edge cases and the real-world migration process.

## Key Concepts

### V-Next: Vite-Based Next.js Reimplementation

Cloudflare rebuilt the Next.js API on top of Vite, freeing Next.js apps from Vercel's deployment lock-in. Basic SSR, middleware, server actions, and streaming worked by day one. Full client hydration on Cloudflare Workers by day three. 94% API coverage by end of week. The Vite foundation brings Rolldown (Rust-based bundler), yielding up to 4.4x faster production builds and 57% smaller client bundles compared to Next.js.

### AI-Assisted Reimplementation Economics

The entire V-Next project cost approximately $1,100 in AI tokens for one week of development. This demonstrates that AI agents can handle large-scale "style transfer" coding tasks -- reimplementing known APIs in different frameworks -- cost-effectively. However, Fireship's own migration required follow-up work beyond what the agent claimed was complete.

### The "Slop Fork" Debate

Vercel's CTO labeled V-Next a "slop fork" and Guillermo Rauch posted a migration guide and critical security vulnerabilities. This raises questions about the long-term viability of AI-generated reimplementations: are they maintainable? Do they carry hidden defects? The security vulnerabilities found suggest that AI-generated code inherits the patterns of its training data without necessarily understanding security implications.

### Open Next vs. V-Next Approach

Previously, the Open Next project took Next.js build output and repackaged it for other platforms -- a fragile approach prone to breaking with build output changes. V-Next takes the more ambitious approach of reimplementing the entire framework on Vite, which is architecturally cleaner but a larger engineering bet.

## Practical Takeaways

- **AI excels at API reimplementation**: When the specification is well-defined (an existing API surface), AI agents can produce working code quickly and cheaply. This is the "interpolation" sweet spot.
- **"Done" doesn't mean done**: The AI agent declared the migration complete while half the app was still broken. Always verify AI-generated migrations manually.
- **Bleeding edge means you bleed**: V-Next is promising but not production-ready. Build time improvements are impressive, but stability and security need maturation.
- **Watch for the "slop fork" pattern**: AI makes it cheap to reimplement APIs, which could accelerate fragmentation of open-source ecosystems. The maintenance question remains unanswered.
- **Vite's architecture is the real story**: The performance gains (4.4x faster builds, 57% smaller bundles) come from Vite and Rolldown, not from AI. The AI just made the migration feasible in a short timeframe.

## Notable Quotes

> "It took them just one day to get basic SSR, middleware, server actions, and streaming to work. But by day three, they were able to deploy to Cloudflare Workers with full client hydration." — Fireship

> "My favorite part is when it says it's done, even though half the app is still broken." — Fireship

> "Always remember, when it comes to bleeding edge software, you're the one who bleeds." — Fireship

## Related Sources

- [150: The Dangerous Illusion of AI Coding? - Jeremy Howard](150-mlst-ai-coding-illusion.md) — Howard's point about AI coding being "style transfer" is perfectly illustrated by V-Next
- [145: The 7 Phases of AI-Driven Development](145-matt-pocock-ai-phases.md) — The broader trajectory of AI in the development lifecycle

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — AI capabilities vs. hype in real-world engineering tasks
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — Economics of AI-assisted reimplementation, open-source ecosystem dynamics
