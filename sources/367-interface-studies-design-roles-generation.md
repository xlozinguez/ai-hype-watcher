---
source_id: "367"
title: "Who’s a Designer? On Roles, Processes, Tools, and of Course AI!"
creator: "Interface Studies"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=v1WdF7BxpBc"
date: "2026-03-24"
duration: "23:00"
type: "video"
tags: ["specification", "ai-sdlc", "vibe-coding", "ai-landscape"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 367: Who’s a Designer? On Roles, Processes, Tools, and of Course AI!

> **Creator**: Interface Studies | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 23:00

# Who's a Designer? On Roles, Processes, Tools, and of Course AI!

## Summary

This video offers a historically grounded critique of how software design roles evolved commercially over the past 30 years — not as a planned profession, but as a series of labor-market purchasing decisions. Distinct specialist roles (information architect, interaction designer, visual designer, UX researcher) were progressively compressed into the "product designer" title without transferring the underlying depth of knowledge each role had accumulated. The product designer inherited the expectation of covering everything while quietly losing the specialist theory that made each discipline rigorous.

The analysis then traces how design tools — from Photoshop through Sketch to Figma — were never neutral: each encoded a theory of what the design problem actually is. Figma's dominance created not just a commercial lock-in but a cognitive one, where an entire generation learned to think about UI in Figma's spatial abstractions rather than in the underlying platform realities (React, SwiftUI, browser behavior). This is framed through Joel Spolski's "law of leaky abstractions" — the abstraction holds until it doesn't, and practitioners with no underlying framework have nothing to fall back on.

The final argument is that AI generation doesn't solve these structural problems — it accelerates and exposes them. Generation fills unspecified states by defaulting to training data and statistically common patterns. It produces something, but it cannot hold a coherent theory of what a system is for, notice when later components contradict earlier decisions, or detect accumulated drift. This means the real value of a designer in the age of generation is not prompting skill but custodianship of an explicit, legible, maintained theory of the system — something the compressed product designer role was already struggling to preserve.

## Key Concepts

### Role Compression Without Knowledge Transfer

Over the mobile era, specialist design disciplines were consolidated into the product designer role for commercial efficiency. But the knowledge depth of an information architect, an interaction designer, or a UX researcher was not inherited — it was assumed to be present without being formally required. This compression had a cost: the theories underpinning each discipline became invisible, carried informally in experienced practitioners' heads rather than encoded in infrastructure or process.

### The Leaky Abstraction Problem in Design Tooling

Design tools encode theories of the design problem. Figma's spatial model — components, variants, auto layout, conditional logic — became so dominant that it shaped how designers think about UI, not just how they represent it. But Figma's model is not React's model, not SwiftUI's model, not the browser's model. When the abstraction fails at the platform boundary, a designer with no framework beneath the abstraction has no way to diagnose or recover. A unified cross-platform vocabulary also means it serves none of the platforms precisely.

### The Canonical Source of Truth Is Shifting

In the classic handoff model, the designer's Figma file was upstream of code. In emerging AI-native workflows (tools like v0, Stitch, Magic Path), the source of truth is shifting toward code-based component registries — design systems where the component structure and documented decisions become the model's primary context. This restructures what a designer's contribution actually is: less the artboard, more the registry of components, states, and encoded decisions that generation operates within.

### Unspecified States and Default-Filling

The classic handoff model trained developers to translate rather than co-think. Unspecified states — loading, failure, empty states, edge cases, recovery paths — were resolved by whoever was closest to the ticket, however was technically convenient. AI generation is the logical conclusion of this model running faster: it fills every unspecified state by defaulting to training data and statistically common patterns. It doesn't ask about edge cases; it produces something. Multiplying unspecified states multiplies the places where generation quietly guesses.

### Custodianship of Explicit System Theory

What generation cannot supply is a maintained, legible theory of what a system is for — and the capacity to hold that theory consistently enough to recognize when something generated violates it. An AI agent can generate a component encoding a design decision but cannot notice six weeks later that two subsequent components contradicted it. It cannot detect accumulated inconsistency or drift. The specialist roles that were compressed away were, in practice, people keeping a theory legible by defending its consistency against commercial pressure. With generation producing output faster than teams can review manually, invisible theory is no longer sufficient.

## Practical Takeaways

- **Specification is now the primary design work.** If generation fills unspecified states by defaulting, the leverage point is exhaustive state specification before generation runs — not post-hoc review of outputs.
- **Design system rigor is directly load-bearing for AI workflows.** In a registry-based model, a sloppy or underdocumented component library doesn't just slow down developers — it becomes the model's primary context, making the quality of that documentation determinative of output quality.
- **Platform-specific knowledge is a genuine differentiator.** Designers who understand what lives beneath Figma's abstraction — how React actually handles state, what SwiftUI constraints actually mean — are more resilient to the leaky abstraction problem and better positioned to catch generation drift.
- **Treat role compression as a liability to actively manage.** Teams that assumed product designers inherited specialist depth without verifying it are now exposed: invisible theory in practitioners' heads cannot keep pace with generation throughput.
- **The question "what is this system for?" must have an explicit, written answer.** If the design theory only exists informally, no amount of prompting skill can substitute for its absence when agents are generating components at scale.

## Notable Quotes

> "The product designer did not magically inherit the depth of an information architect, the rigor of an interaction designer, or the evidential discipline of a researcher. They inherited the expectation of covering it all."

> "Every abstraction eventually fails to conceal what it's built on. And when it fails, the person relying on it has no framework to understand why."

> "What no generation tool can supply is an explicit, maintained, legible theory of what a system is for and the capacity to hold that theory consistently enough to know when something generated violates it."
