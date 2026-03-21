---
source_id: "328"
title: "we're so back"
creator: "ThePrimeagen"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=5DP0az1q_8M"
date: "2026-03-19"
duration: "10:49"
type: "video"
tags: ["agentic-coding", "ai-landscape", "claude-code", "validation"]
curriculum_modules: ["01-foundations", "03-claude-code-essentials"]
---

# 328: we're so back

> **Creator**: ThePrimeagen | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 10:49

## Summary

ThePrimeagen reacts to a widely-discussed thread by Mitchell Hashimoto (creator of Ghostty terminal) about a 6-month-old bug that Codex 53 "extra high" reasoning solved in minutes for $4.14, while other models (including Opus 4.6 and lower reasoning levels of Codex) failed. The bug was a visual flicker in Ghostty's GTK split view, caused by leaf nodes in GTK surfaces being destroyed and recreated instead of reused. The AI's breakthrough was reading GTK4 source code directly -- something the other models and reasoning levels never attempted.

While framing this as an "it's so over" moment for AI skeptics, ThePrimeagen draws a more nuanced conclusion. He highlights the critical role of Mitchell's thorough code review and manual cleanup after the AI produced its fix, noting that the AI introduced two simpler bugs while fixing the complex one. The real value was in synthesizing massive amounts of source code across two codebases (Zig and GTK) to identify the root cause -- work that would have taken a human months of codebase archaeology. ThePrimeagen uses this to reflect on his own AI usage, recognizing he tends to operate in extremes (writing entirely by hand or fully delegating) when the most productive mode is the middle ground: letting AI do the 80% research and providing human judgment for the final 20%.

## Key Concepts

### The "Extra High" Reasoning Difference

The critical factor was reasoning effort level. Lower reasoning levels and other models never ventured into the GTK4 source code -- they stayed within the Ghostty codebase. Only Codex 53 at "extra high" reasoning took the initiative to read upstream library source code, which is where the root cause lived. This suggests that for deep cross-codebase bugs, maximum reasoning investment pays disproportionate returns.

### The Review-and-Cleanup Phase

Mitchell did not simply accept the AI's output. He performed thorough code review, questioned specific implementation decisions, asked the AI to explain its fix in detail, requested changes to failure modes, and made manual cleanups. ThePrimeagen contrasts this with "vibe coders" who "put the code in the bag" the moment something works, especially younger developers who trust AI output too readily. The reviewing process took meaningful time but was dramatically less than the months of source code archaeology needed to find the root cause.

### AI Excels at Codebase Archaeology

The specific category of work AI excels at is not writing new features but synthesizing large volumes of source code to find hidden root causes. ThePrimeagen connects this to his own experience investigating Honey's browser extension behavior -- combing through minified JavaScript that would take months manually but that AI can process and return candidate results in minutes. This strips away what he considers the "least pleasurable" part of programming.

### The 80/20 Usage Mode

ThePrimeagen recognizes he typically operates in one of two extremes: writing entirely by hand or fully delegating ("Sam Altman take the wheel"). The Hashimoto example demonstrates the most productive middle ground: let AI do the research-heavy 80% (codebase archaeology, synthesizing documentation, identifying root causes), then apply human judgment for the remaining 20% (code review, style decisions, edge case handling).

### Hyrum's Law Connection

ThePrimeagen connects the GTK flicker bug to Hyrum's Law: "with a sufficient number of users of an API, it does not matter what you promise in the contract. All observable behaviors of your system will be depended on by somebody." The bug was an undocumented GTK behavior that Ghostty depended on, exactly the kind of deep cross-system issue where AI's ability to read upstream source code provides the most value.

## Practical Takeaways

- **Maximize reasoning effort for cross-codebase bugs**: The reasoning level matters more than the model for bugs that span multiple codebases or require reading upstream library source code.
- **Never skip the review phase**: AI solving a hard bug while introducing two simple ones is the expected pattern. The review and cleanup phase is non-negotiable.
- **AI's highest ROI is codebase archaeology**: Synthesizing large volumes of code to find hidden root causes saves the most human time. This is different from (and more valuable than) feature generation.
- **Find the 80/20 usage mode**: Neither fully manual nor fully delegated -- use AI for research and root-cause identification, apply human judgment for implementation quality.
- **Younger developers especially need review discipline**: The tendency to accept AI output without rigorous review is more pronounced in less experienced developers, making code review skills more important, not less.

## Notable Quotes

> "The average vibe coder, shall we call him, the average AI Andy from San Francisco, typically at this point, they put the code in the bag."

> "It fixed a really, really difficult one and then produced two simple ones."

> "This is truly stripping away the things in programming that I find to be the least pleasurable parts of it."

> "The best thing that Codex did was eventually start reading the GTK4 source code." -- Mitchell Hashimoto (quoted by ThePrimeagen)

## Related Sources

- [282: Tom Wells - Agents Architecturally Blind](282-tom-wells-agents-architecturally-blind.md) — limitations of AI code understanding
- [280: Leon van Zyl - Claude Code Loop](280-leon-van-zyl-claude-code-loop.md) — iterative AI coding workflows

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — AI capabilities and limitations
- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — practical AI-assisted coding workflows
