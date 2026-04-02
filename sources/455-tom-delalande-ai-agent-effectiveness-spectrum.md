---
source_id: "455"
title: "I was wrong about AI coding agents"
creator: "Tom Delalande"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=S2FbFgUuOkU"
date: "2026-04-01"
duration: "12:06"
type: "video"
tags: ["ai-hype", "agentic-coding", "context-engineering", "ai-sdlc", "vibe-coding"]
curriculum_modules: ["01-foundations", "02-prompting-and-workflows", "04-agentic-patterns"]
---

# 455: I was wrong about AI coding agents

> **Creator**: Tom Delalande | **Platform**: YouTube | **Date**: 2026-04-01 | **Duration**: 12:06

# I Was Wrong About AI Coding Agents

## Summary

Tom Delalande walks back a previous video where he claimed AI agents were "completely useless," arguing that both the hype and the dismissal are wrong. Rather than picking a side, he maps AI tool effectiveness onto a spectrum: some tasks (rapid prototyping, code review, boilerplate refactoring) are near-certain wins, while others (debugging, open-ended planning, greenfield architecture) become increasingly inconsistent as complexity rises. The key insight is that the *consistency* of AI output degrades as task complexity grows, and there is a "critical thinking line" beyond which the cost of using AI outweighs the benefit.

The video draws heavily on the working styles of Mitchell Hashimoto and Dax Rad as grounded examples of responsible AI use. Both engineers maintain high craft standards and treat AI as a way to *choose what to think about*, not a way to think less. Hashimoto in particular structures his work so that he owns the critical path and delegates low-cognition tasks to agents on his own schedule—notifications off, flow state protected. This framing reframes AI not as a replacement for thinking but as a tool for managing cognitive load strategically.

Delalande closes with practical observations about what makes a codebase AI-ready: domain-driven design with hexagonal architecture (to contain hallucination blast radius), rigorous unit tests, and strict merge standards for simple code. These are conventional engineering best practices that become *more* important under AI-assisted development, not less.

---

## Key Concepts

### The AI Effectiveness Spectrum
AI tools do not have uniform value across all tasks. Effectiveness degrades as complexity increases. Rapid prototyping and throwaway code sit at the high-value end. Code review, simple refactoring, and spike research are moderate wins. Debugging, planning, and novel code generation are inconsistent enough that cost often exceeds benefit. Delalande introduces a "critical thinking line" as the practical cutoff beyond which AI use becomes net-negative.

### Context Management for Humans (Not Just Models)
Most AI discourse focuses on managing the model's context window. Hashimoto's insight is that human context management matters equally. By disabling notifications and deciding *when* to check agent output rather than being interrupted by it, he preserves deep work flow. This is framed as a design decision: you can use AI to do the same work with less effort, or you can use it to do *more* work at the same effort level—the difference is entirely in how you manage your own attention.

### Delegation vs. Abdication
There is a sharp distinction between delegating low-cognition tasks to an agent while you work on high-cognition problems, versus launching an agent and disengaging entirely. The latter produces poor code and leaves the developer feeling unfulfilled reviewing it. The former amplifies developer output without sacrificing craft or understanding. Delalande cites Hashimoto explicitly: identify tasks that require thinking, identify tasks that don't, and delegate only the latter.

### Codebase as Training Signal
When AI is used to write code in an existing codebase, the quality of that codebase directly determines the quality of AI output. The codebase should be a "perfect example of what you want future code to look like." This means stricter-than-usual merge standards for simple code, because that simple code is what the AI will pattern-match against. Conventional best practices—domain-driven design, hexagonal architecture, unit tests—function as guardrails that constrain where hallucinations can propagate.

### Knowing When to Pull the Plug
Because AI code generation is inherently probabilistic ("more like a slot machine"), a key skill is recognizing quickly when an approach isn't working and abandoning it. Persistence with a failing agent run is a trap. The discipline to cut losses early and fall back to manual implementation is as important as knowing when to engage AI in the first place.

---

## Practical Takeaways

- **Start with the easy wins.** Code review, deleting unused code, and tedious multi-file refactors are high-ROI, low-risk uses of AI. Build confidence and workflow there before attempting complex generation tasks.
- **Protect your own flow state.** Disable agent notifications. Check in on agent output when *you* decide to, not when the agent interrupts you. This keeps you on the critical path and prevents context-switching costs from eroding gains.
- **Understand the output domain before delegating.** AI-generated code works best when you already know the shape of what correct output looks like—an existing pattern, a well-understood problem type. If you can't recognize a good answer, don't outsource finding the answer.
- **Invest in architectural hygiene now.** Hexagonal architecture with clear component boundaries limits the scope of any single AI task and prevents hallucinations from leaking between domains. Unit tests double as understanding aids when reviewing AI output.
- **The hype and the dismissal are both wrong.** Calibrate expectations against actual consistency, not best-case demos or worst-case failures. The productive frame is: what tasks does this tool handle *consistently*, and how do I structure my work to stay in that zone?

---

## Notable Quotes

> "If you instead view it as a way to choose what you think about, then I think that you don't need to sacrifice that thinking. But I think the problem is the majority of the population probably won't do that." — Mitchell Hashimoto (quoted by Delalande)

> "Me typing out code is the process by which of figuring out what we should even be doing... I like writing out types. I like writing out how some of the functions might play together." — Dax Rad (quoted by Delalande)

> "To use AI in this way, you have to care more about craftsmanship than before, not less."

---
