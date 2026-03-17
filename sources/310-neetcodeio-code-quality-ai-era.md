---
source_id: "310"
title: "The future of Coding and Code Quality"
creator: "NeetCodeIO"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=baIHCeccbbw"
date: "2026-03-13"
duration: "20:56"
type: "video"
tags: ["agentic-coding", "ai-sdlc", "vibe-coding", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 310: The future of Coding and Code Quality

> **Creator**: NeetCodeIO | **Platform**: YouTube | **Date**: 2026-03-13 | **Duration**: 20:56

## Summary

This conversation between NeetCode (Navdeep Singh) and Dax Raad covers the relationship between technical debt, code quality, and AI-assisted development. The central argument is that the "move fast, break things" trade-off narrative is largely a rationalization for inexperience rather than a genuine strategic choice — and that this dynamic is unchanged by AI tooling. A more experienced developer, the argument goes, doesn't have to choose between speed and quality the way a less experienced one does, because good patterns come naturally with experience.

The second major thread concerns how AI tooling has paradoxically *increased* the importance of codebase cleanliness. Because LLMs learn from existing patterns in a codebase and cannot distinguish between "old way" and "new way" practices, inconsistent or legacy-laden codebases now actively poison AI-generated output. This creates a strong incentive to maintain rigorous, consistent patterns across every file — arguably more discipline than most teams exercised before AI.

The conversation also touches on the practical reality of code review: even before AI, not every line of code was carefully reviewed at large companies. The current approach described by Dax involves calibrated review — thorough scrutiny in unstable or novel areas, lighter review in well-established pattern areas — while acknowledging the genuine risk that unreviewed AI-generated code can silently corrupt future LLM generations.

## Key Concepts

### Technical Debt is Mostly a Skill Issue, Not a Strategic Trade-Off

The core claim is that roughly 95% of technical debt is attributable to inexperience or context overload, not genuine intentional trade-offs. When developers revisit a system they built quickly, they typically find that a more experienced version of themselves *could have* built it correctly at the same speed — they simply didn't know how yet. This reframes the "we moved fast so the quality suffered" narrative as largely post-hoc rationalization.

### AI Tooling Raises the Stakes for Codebase Consistency

LLMs have "photographic memory but are stupid" — they faithfully replicate whatever patterns exist in a codebase without being able to apply judgment about which patterns are current and intentional. A codebase with multiple eras of conflicting conventions will produce degraded AI output as the model averages across those conventions. This means that maintaining a single, clean, intentional pattern throughout every file is now a prerequisite for effective AI-assisted development, not just an aesthetic preference.

### Calibrated Code Review as a Risk Management Practice

Rather than reviewing every line or reviewing nothing, the approach described is risk-stratified review: areas with mature, well-established patterns receive lighter review (a "quick glance — does this roughly look right?"); areas with less stable patterns demand more diligent human scrutiny. The underlying principle is trust earned through observed reliability of outputs in a given domain, similar to how senior engineers extend trust to junior developers over time.

### Experience-Adjusted Speed: AI as a Vertical Lift, Not an Equalizer

AI tools accelerate everyone, but they don't flatten the gap between skill levels. An experienced team can build higher-quality artifacts at the same speed as a less experienced team ships lower-quality ones — AI amplifies existing capability rather than substituting for missing capability. The example given is building a terminal framework from scratch in Zig with React/SolidJS bindings at comparable velocity to a team shipping a rougher prototype.

### Unreviewed AI Code as a Compounding Risk

When AI-generated code is committed without thorough review, there is a known risk that technically incorrect but functionally "working" code will be used as a training example for future LLM generations within the codebase. This compounding effect means that short-term tolerance for unreviewed code can degrade the long-term quality of all future AI-generated code in that project — making the cleanup cost higher the longer it is deferred.

## Practical Takeaways

- **Audit and standardize your codebase before leaning heavily on AI generation.** Every legacy pattern or inconsistency becomes amplified by LLM output. Treat codebase hygiene as infrastructure work, not cosmetic cleanup.

- **Adopt opinionated frameworks and patterns deliberately.** Domain-driven design and frameworks with strong built-in conventions give LLMs less ambiguity to navigate, resulting in more predictable and correct output.

- **Apply risk-stratified code review.** Identify which areas of your codebase have mature, battle-tested patterns (lighter review acceptable) versus experimental or evolving areas (mandatory thorough review). Never let zero humans understand a given piece of code.

- **Treat post-mortems on AI-assisted work seriously.** Shipping something that worked is not evidence that the process was optimal. Reflecting on what could have been done better without time cost is how developers close the experience gap.

- **Flag and remediate technically incorrect but working AI code promptly.** Even if a feature works from a user perspective, known structural issues should be marked for cleanup before they become the "old way" that poisons future generations.

## Notable Quotes

> "5% of that was intentional trade-offs, the other 95% of that was inexperience… The next time I went and did that, I got almost all that stuff right up front. There was actually no additional time cost, no additional anything. It was my own ability and my own experience that was really limiting everything."

> "Our code bases are now cleaner than they've ever been… Your LLM can't differentiate between the old way and the new way. It's going to look at the old way and be like, 'Oh, that's how I do it.' And it's going to generate all this crap."

> "We have a bunch of idiots working for us now — these LLMs that will work very hard and have like photographic memory, but are stupid, and we can't… they can't understand the simple idea that hey, there's like a better way to do stuff."
