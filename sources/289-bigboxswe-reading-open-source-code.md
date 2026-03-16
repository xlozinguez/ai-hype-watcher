---
source_id: "289"
title: "The programming habit I wish I started sooner"
creator: "bigboxSWE"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=XLVY6jr3JTw"
date: "2026-03-10"
duration: "4:31"
type: "video"
tags: ["vibe-coding", "ai-sdlc"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 289: The programming habit I wish I started sooner

> **Creator**: bigboxSWE | **Platform**: YouTube | **Date**: 2026-03-10 | **Duration**: 4:31

## Summary

BigBoxSWE argues that reading open-source code is the single most underrated programming habit, vastly more valuable than the commonly emphasized activity of contributing to open source. The core insight is that open source represents freely accessible, production-grade knowledge covering topics — systems scaling, performance optimization, architectural patterns — that formal education and textbooks simply don't address. The video reframes open source repos not as contribution targets but as living textbooks written by engineers at scale.

The practical framework offered is deceptively simple: start with tools you already use and care about, clone the repo rather than just browsing GitHub, and investigate the codebase as if it were your own project. The emphasis on genuine curiosity is notable — the author argues that caring about the software is a prerequisite for learning from it, which filters out performative "OPSEC bro" repo-collecting in favor of deep, motivated exploration.

While the video is not directly about AI-assisted development, it is highly relevant context for developers building skills in the AI era. Understanding real production codebases — how they're structured, how features evolved via git history, how build systems work — is precisely the kind of grounded, concrete knowledge that makes someone an effective collaborator with AI coding tools rather than a passive consumer of generated code.

---

## Key Concepts

### Reading Over Contributing
The dominant narrative around open source focuses on contribution as the primary value. BigBoxSWE flips this: reading and understanding a codebase provides approximately 90% of the learning benefit, and contribution is a downstream outcome of deep familiarity rather than an entry point. This reframes the relationship to open source from obligation to exploration.

### Motivation-Gated Learning
The author emphasizes that the project must be something you genuinely use and care about. Arbitrary "impressive repo" lists are nearly useless unless there's intrinsic interest in how the software is built. Examples given — PostHog's UI structure, Ghostty's performance, Rectangle's keyboard shortcuts — illustrate how personal obsession with a product creates the curiosity needed to sustain deep code reading.

### Clone and Investigate, Don't Browse
There's a meaningful distinction between skimming a GitHub repository online and cloning it locally to treat it as your own project. Local investigation enables using familiar tooling, tracing git history to understand feature evolution, reading commit messages, identifying original authors, and compiling from source — all of which are inaccessible or cumbersome in the browser UI.

### Git History as Documentation
Using `git log`, `git blame`, and related commands to trace who built a feature and what it looked like in earlier iterations is highlighted as an underutilized learning technique. This turns version control from a collaboration tool into a narrative record of engineering decisions, providing context that the current code alone cannot.

### Compiling from Source as Systems Education
Building a project from source is presented as a distinct learning modality: it teaches the build system, reveals dependencies, and surfaces knowledge about how the underlying computer and OS work. The author notes that even something seemingly simple like Python is "a lot harder than you think" when compiled from source.

---

## Practical Takeaways

- **Start with your own toolchain.** Your editor, window manager, browser, CLI tools, databases, and developer utilities are likely already open source — this gives you immediate context and motivation before you read a single line.
- **Clone locally and use your full dev environment.** Browser-based repo browsing is a shallow substitute; local investigation with your editor, search tools, and git CLI unlocks the full learning surface.
- **Use git history deliberately.** `git blame` and `git log` on files or features you find interesting reveals the reasoning behind current design choices and how the code evolved — a form of documentation that doesn't exist anywhere else.
- **Try compiling from source at least once.** Even if you don't do it regularly, building a non-trivial project from source (Linux kernel, Python, FFmpeg) provides concrete systems knowledge that tutorials don't cover.
- **Treat interesting code patterns as templates.** When you find an architectural or UI pattern you want to emulate, the open source codebase becomes a reference implementation you can directly study rather than approximate from documentation.

---

## Notable Quotes

> "Open source is free ball knowledge. You can learn so much about scaling systems, writing highly performant, robust, and reliable code... These are things that just aren't covered in programming courses or books."

> "To actually learn from open source, find a project that you already use... if you don't actually care about how the software is built, none of this matters."

> "You should treat it as if it were your own project and go through the parts of the codebase that interest you."

---
