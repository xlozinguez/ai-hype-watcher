---
source_id: "475"
title: "Simon Willison: Engineering practices that make coding agents work - The Pragmatic Summit"
creator: "The Pragmatic Engineer"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=owmJyKVu5f8"
date: "2026-03-19"
duration: "28:20"
type: "video"
tags: ["agentic-coding", "validation", "prompt-engineering", "ai-sdlc", "security"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns", "06-strategy-and-economics"]
---

# 475: Simon Willison: Engineering practices that make coding agents work - The Pragmatic Summit

> **Creator**: The Pragmatic Engineer | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 28:20

# Simon Willison: Engineering Practices That Make Coding Agents Work

## Summary

Simon Willison (co-creator of Django, creator of Datasette) describes his current developer workflow where AI coding agents write the majority of his code — and explains the engineering practices that make this viable. The conversation covers his phone-based development workflow, the "nobody writes code, nobody reads code" extreme being explored by teams like StrongDM, and how he thinks about trust calibration with modern models like Claude Opus 4.5.

The core thesis is that moving to agent-driven development isn't just about prompting better — it requires adopting specific engineering practices, particularly test-driven development, that give you reliable signals the code works without requiring exhaustive manual review. Willison argues that tests are now effectively free to generate, making them non-optional in any agent workflow. He also introduces a new tool he built called Showboat that produces markdown documentation of manual API testing via curl, bridging the gap between automated tests and real-world validation.

Willison also addresses code quality as a deliberate choice rather than an inherent limitation: agents will follow the patterns in your codebase if that codebase is well-structured, and agents can be directed to refactor code that a human developer might let slide due to time pressure. He closes by raising prompt injection and the "lethal trifecta" as key security concerns when agents are given real-world capabilities.

## Key Concepts

### Red-Green TDD as Agent Discipline
Willison argues that test-driven development — historically tedious for human developers — becomes a natural fit for agents. Instructing an agent to use "red-green TDD" (roughly five tokens) ensures it writes a failing test first, then the minimal implementation to pass it. This prevents agents from over-engineering, provides an objective completion signal, and raises the probability of getting working code significantly. The instruction is portable: all competent coding agents understand the pattern.

### Manual Verification via Curl/Showboat
Automated test suites don't guarantee a web server will actually boot and behave correctly. Willison's practice is to instruct agents to start the server in the background and exercise the API with curl. His new tool Showboat formalizes this: the agent builds a markdown document of each curl command and its output, creating a human-readable record of manual testing that can surface bugs automated tests miss.

### Conformance-Driven Development
For domains with existing language-agnostic test suites (e.g., WebAssembly's specification tests), you can hand the suite to an agent and instruct it to "write code until this test suite passes." Where no conformance suite exists, Willison reverse-engineers one: he asks an agent to build a test suite that passes across multiple reference implementations (Go, Node.js, Django, Starlette) and then uses that synthetic spec to drive a new implementation.

### Codebase as Agent Training Signal
Agents are highly consistent pattern-followers: they will replicate the style, structure, and idioms already present in a codebase. Willison uses cookie-cutter project templates (pre-configured with CI, testing frameworks, and a few seed tests) to ensure agents start in a constrained, high-quality context. A well-structured codebase acts as implicit few-shot context that shapes agent output quality — the same dynamic he observes in human engineering teams.

### Code Quality as a Deliberate Choice
Poor-quality agent output is a choice, not an inevitability. If an agent produces 2,000 lines of messy code and you merge it without review, that's on you. Willison notes that agents can be directed to refactor after the fact — tasks a time-pressured human developer might skip — leading to code that is *higher* quality than hand-written code. The calculus shifts: the cost of refactoring is a prompt plus walking the dog, not an hour at a keyboard.

## Practical Takeaways

- **Always start an agent session by telling it to run tests first**, then use "red-green TDD" in the prompt. This is low-cost (five tokens), broadly understood by modern agents, and substantially improves output reliability.
- **Add a curl-based smoke test step** after automated tests pass: instruct the agent to start the server and exercise endpoints, capturing output. This catches runtime failures that unit tests miss.
- **Invest in project templates (e.g., cookie-cutter)** that encode your preferred test structure, CI setup, and a few seed tests. Agents will inherit and extend these patterns consistently.
- **Treat code quality as a post-generation concern you actively direct**: spot a suboptimal pattern in agent output, feed it back as a refactoring prompt. The marginal cost of agent refactoring is low; the marginal cost of tech debt is not.
- **For disposable one-off tools** (single-page HTML/JS, quick scripts), don't over-review — code quality genuinely doesn't matter if the artifact is ephemeral. Reserve careful review for maintained codebases.

## Notable Quotes

> "Tests are no longer even remotely optional. Tests are step one in getting good results out of them."

> "Having poor quality code from an agent is a choice that you make. Like if the agent spits out 2,000 lines of bad code and you choose to ignore it, that's on you."

> "It's almost like you can reverse-engineer six implementations of a standard to get a new standard and then you can implement the standard."
