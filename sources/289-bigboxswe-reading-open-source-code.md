---
source_id: "289"
title: "The programming habit I wish I started sooner"
creator: "bigboxSWE"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=XLVY6jr3JTw"
date: "2026-03-10"
duration: "4:31"
type: "video"
tags: ["ai-sdlc", "vibe-coding"]
curriculum_modules: ["02-prompting-and-workflows"]
---

# 289: The programming habit I wish I started sooner

> **Creator**: bigboxSWE | **Platform**: YouTube | **Date**: 2026-03-10 | **Duration**: 4:31

## Summary

bigboxSWE makes a simple but underappreciated argument: the single most valuable programming habit is reading open-source code, not contributing to it. The framing challenge is that most developer discourse around open source fixates on contribution metrics, which the creator estimates captures only about 10% of the available benefit. The real value lies in passive, deep reading of production-grade codebases that scale to billions of users — knowledge that no course or textbook reliably delivers.

The practical method is straightforward: start with tools you already use daily (editor, browser, CLI tools, databases), find a specific part of the project that genuinely interests you, clone the repo, and treat it as your own codebase. The creator emphasizes authentic curiosity as the prerequisite — browsing a GitHub repo without caring how the software works produces nothing. The concrete examples given span the range from PostHog's UI architecture to Ghostty terminal (written in Zig) to the Linux kernel and FFmpeg, demonstrating that every layer of the stack has accessible, high-quality open-source references.

A bonus point connects reading to contributing: becoming a power user who understands a codebase organically is the only sustainable path to meaningful open-source contribution. This reframes contribution not as a resume checkbox but as a natural byproduct of genuine engagement with software you depend on.

---

## Key Concepts

### Reading Over Contributing
The dominant framing of open-source participation emphasizes pull requests and contribution counts, but the creator argues this misses the primary educational value. Passive, deep reading of mature codebases exposes developers to architectural decisions, performance optimizations, and maintenance patterns that are never formally taught. A cited example — a 400% performance gain from a 40-line change — illustrates the kind of insight available only in production code, not tutorials.

### Authentic Interest as the Entry Condition
Randomly cloning high-profile repos produces little learning. The method requires identifying projects you already use and finding specific subsystems that genuinely interest you — a UI pattern you want to emulate, a performance characteristic you find remarkable, a feature you rely on daily. This emotional investment sustains the focus needed to actually comprehend unfamiliar, large-scale code.

### Clone and Investigate, Don't Browse
There is a meaningful difference between skimming a GitHub repo in the browser and cloning it locally to investigate. Local investigation enables using `git log` and `git blame` to trace feature history, understand why decisions were made, and identify the humans behind specific changes. Compiling from source adds another layer, teaching build systems and system-level behavior that web browsing cannot surface.

### Breadth of Available Knowledge
Open-source codebases span the full stack and include code from organizations normally considered black boxes — Meta, Google, Supabase, GitLab (entire platform open-sourced), Jane Street (quant trading in OCaml), and open-weight AI models like DeepSeek. This breadth means developers at any level working on any part of the stack have access to production-grade reference implementations.

### Reading as the Foundation for Contributing
The creator repositions contribution as downstream of deep reading rather than a parallel activity. Sustainable, high-quality contributions emerge from being a power user who understands the codebase well enough to genuinely want to fix something — not from searching for "good first issues" as a portfolio exercise.

---

## Practical Takeaways

- **Start with your own toolchain**: List the open-source tools you use every day (editor, terminal, browser, database, libraries) — these are the highest-leverage starting points because you already have context about what the software is supposed to do.
- **Pick a specific feature, not a whole codebase**: Narrow your focus to something you want to understand or emulate (e.g., how a specific UI pattern is implemented, how a particular performance optimization works) rather than trying to comprehend an entire project.
- **Use git history as a learning tool**: `git log`, `git blame`, and `git diff` on interesting files reveal the evolution of decisions and the reasoning behind them, often more valuable than the current code state alone.
- **Compile from source at least once per project**: The build process exposes dependency graphs, system assumptions, and configuration complexity that reading source files alone does not — particularly useful for understanding infrastructure-adjacent tools.
- **Don't limit yourself to GitHub**: Codeberg and GitLab host projects not mirrored on GitHub; the same methodology applies and broadens the available reference pool.

---

## Notable Quotes

> "Most of the discourse around open source is how quickly you can contribute, which misses almost 90% of the benefit."

> "Open source is free ball knowledge. You can learn so much about scaling systems, writing highly performant, robust, and reliable code."

> "Be an actual user. Be a power user. Understand the codebase and contribute to it because you actually want to fix a product you use."

---
