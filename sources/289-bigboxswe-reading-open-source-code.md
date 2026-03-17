---
source_id: "289"
title: "The programming habit I wish I started sooner"
creator: "bigboxSWE"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=XLVY6jr3JTw"
date: "2026-03-10"
duration: "4:31"
type: "video"
tags: ["vibe-coding", "ai-sdlc", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 289: The programming habit I wish I started sooner

> **Creator**: bigboxSWE | **Platform**: YouTube | **Date**: 2026-03-10 | **Duration**: 4:31

## Summary

bigboxSWE argues that reading open-source code is the single most underrated programming habit, and that most developers miss its primary value by focusing on contribution rather than comprehension. The video frames open-source repositories not as places to submit PRs, but as free access to production-grade, battle-tested code from companies like Meta, Google, GitLab, and Jane Street — covering techniques (performance optimization, system scaling, robust architecture) that no course or book adequately teaches.

The core method is straightforward: start with tools you already use and care about, clone the repository, and treat it as your own codebase. The creator gives concrete examples — studying PostHog's UI patterns, Ghostty's performance (written in Zig), and Rectangle's keyboard shortcut implementation — to illustrate that genuine curiosity about a specific feature is the prerequisite for learning anything useful. Passive GitHub browsing yields nothing; active investigation does.

While this video is not directly about AI-assisted development, it surfaces a foundational practice highly relevant to developers working with AI coding tools: understanding how real production codebases are structured, what patterns they use, and how features evolve over time (via Git history) directly improves the quality of context, specifications, and prompts a developer can provide to an AI agent. Reading code at scale builds the mental models that make AI-assisted development more effective.

---

## Key Concepts

### Reading Over Contributing
The dominant discourse around open source emphasizes contribution, but the creator argues this misses roughly 90% of the value. Passive comprehension — understanding *how* and *why* code is structured the way it is — yields insights into scaling, performance, and reliability that formal education doesn't cover. A cited example: a developer finding a 400% performance improvement in a 40-line change, the kind of insight only visible by reading production code deeply.

### Genuine Interest as a Filter
The method only works if you care about what you're reading. The recommendation is to start with tools you already use daily — code editors, terminal emulators, window managers, databases, CLI tools — and then narrow to a specific feature or quality you want to emulate. Curiosity about *why* something works well (e.g., Ghostty's speed, Rectangle's keyboard shortcuts) is the prerequisite for actually absorbing what the code teaches.

### Cloning and Active Investigation
Rather than browsing a GitHub repo superficially, the creator recommends cloning the repo and treating it as a personal project. This enables use of Git to trace feature history, identify authors, and see how implementations evolved — turning a static snapshot into a dynamic learning tool. Compiling from source is also recommended as a way to learn about build systems and low-level computer behavior.

### Open Source as Mental Model for AI Context
Though not stated explicitly in the video, this practice has compounding value for AI-assisted development: developers who have read production-scale codebases are far better at writing precise specifications, structuring prompts with realistic architectural context, and recognizing when AI-generated code matches or diverges from proven patterns. The mental models built through reading code directly improve the quality of context engineering.

### Breadth of Available Sources
The creator pushes back against GitHub-centrism, noting that Codeberg and GitLab host excellent projects. He highlights non-obvious sources like Jane Street's OCaml repositories (quantitative trading) and open-source AI models like DeepSeek — emphasizing that every layer of the stack has representative open-source projects worth studying.

---

## Practical Takeaways

- **Start with what you already use**: Identify 3–5 tools in your daily workflow that are open source and pick one feature in each that impresses or puzzles you — this is your reading list.
- **Clone, don't browse**: Downloading a repo locally and using your editor's tooling (go-to-definition, git blame, git log) transforms passive reading into active investigation.
- **Use Git history as a learning layer**: `git log` and `git blame` reveal the *intent* behind code, not just its current state — understanding why a decision was made is more valuable than what the decision is.
- **Compile from source at least once**: The build process exposes dependencies, system assumptions, and architectural decisions invisible in the source files alone.
- **Apply patterns to your own projects deliberately**: After reading, identify one specific pattern or structure worth emulating and implement a version in a personal project to solidify the learning.

---

## Notable Quotes

> "Open source is free ball knowledge. You can learn so much about scaling systems, writing highly performant, robust, and reliable code... These are things that just aren't covered in programming courses or books."

> "Most people just look at a GitHub repo, flick through the app directory, and call it a good day."

> "Find parts of a project that you actually care about or even parts that you want to emulate."

---
