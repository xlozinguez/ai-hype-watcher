---
source_id: "500"
title: "Everyone Says Don’t Do This in Software… Big Tech Does It Anyway"
creator: "Uma Abu"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=mdCOGh4UFU4"
date: "2026-03-26"
duration: "10:18"
type: "video"
tags: ["enterprise-ai", "ai-sdlc", "infrastructure"]
curriculum_modules: ["06-strategy-and-economics"]
---

# 500: Everyone Says Don’t Do This in Software… Big Tech Does It Anyway

> **Creator**: Uma Abu | **Platform**: YouTube | **Date**: 2026-03-26 | **Duration**: 10:18

## Summary

This video examines why some of the world's largest technology companies — Google, Meta, Microsoft, Uber, Airbnb — organize significant portions of their codebases in a single version-controlled repository (monorepo), despite this practice running counter to conventional software development wisdom around modularization and separation of concerns. The creator draws on personal experience working in Microsoft's Substrate monorepo, engineering blog research, and a LinkedIn survey of developers who have worked inside these systems to explain the reasoning behind the approach.

The core argument is that monorepos are not a rejection of good software architecture principles but rather a pragmatic response to the specific coordination costs that emerge at massive scale. When hundreds of repositories need to stay in sync across thousands of engineers, version mismatches, fragmented dependency management, and slow cross-codebase refactoring become genuinely expensive problems. A monorepo with the right tooling investment can solve those problems more efficiently than a fragmented multi-repo structure. Crucially, the video clarifies a common misconception: a monorepo does not mean a monolithic application — services still build, deploy, and run independently; they simply share a common version-controlled home.

The video also emphasizes that the monorepo approach only works because of substantial infrastructure investment. Google built Piper and Bazel, Meta built Buck 2, and Microsoft built a virtual file system layer — all purpose-built to make large-scale monorepos tractable. Without this kind of tooling, the approach would collapse under its own complexity.

## Key Concepts

### Monorepo vs. Monolith
The most important conceptual clarification in the video: a monorepo is a version control strategy, not an architectural pattern. Multiple independent services and applications can live in subdirectories of a single repository while still building, deploying, and running in complete isolation from one another. The only thing that changes is where the code is stored, not how it executes.

### Scale-Driven Trade-offs
The decision to adopt a monorepo is framed explicitly as a trade-off that makes sense at a certain scale threshold. Small teams generally benefit from the simplicity of polyrepos. At Google/Meta/Microsoft scale, however, coordinating changes across hundreds of separate repositories introduces compounding costs — dependency drift, version mismatches, slow large-scale refactors — that a monorepo with proper tooling resolves more efficiently.

### Purpose-Built Tooling as a Prerequisite
Monorepos at scale are only viable because of significant custom infrastructure: smart build systems (Bazel, Buck 2) that rebuild only affected code paths, virtual file systems that prevent engineers from having to clone billions of lines locally, and internal version control systems (Google's Piper) designed for the load. The video treats tooling not as a nice-to-have but as the entire foundation that makes the approach work.

### Single Version Policy
A key operational benefit that emerges in monorepos is organizational convergence on a single version of shared dependencies. Rather than each team quietly drifting to different library versions and creating compatibility emergencies later, the default expectation becomes that everyone moves forward together. This reduces integration incidents and prevents technical debt accumulation that becomes "someone else's emergency."

### Code Visibility and Collaborative Velocity
Because all code is co-located, engineers can search the entire codebase instantly, trace API usage across services, and propose fixes in other teams' code directly rather than filing tickets. This visibility accelerates large-scale migrations (e.g., propagating a security fix across the entire company in a single change) and functions as an organic learning resource — developers can study real production patterns from other teams.

## Practical Takeaways

- **Don't conflate storage with execution**: Moving to a monorepo doesn't require changing how services are built or deployed — clarifying this mental model is the biggest barrier to adoption for developers coming from polyrepo environments.
- **Tooling investment is non-negotiable**: Before adopting a monorepo at any meaningful scale, evaluate whether your build system can do incremental/affected-only builds. Without this, build times will become the primary pain point.
- **Monorepos shine for large-scale refactors and security patches**: If your organization frequently needs to propagate changes across many services simultaneously, the ability to do that in a single atomic commit is a concrete, measurable advantage.
- **Independent deployments must be preserved**: The developers surveyed identified independent deployment per service — not coordinated release trains — as a critical condition for monorepos to work well in practice. Shared code, independent deploys.
- **Scale is the deciding variable**: The video's implicit advice is to treat monorepo adoption as a function of coordination costs, not ideology. If cross-repo dependency management is already painful, investigate monorepo tooling; if it isn't, the complexity may not be worth it.

## Notable Quotes

> "The biggest challenge when moving to a monorepo is realizing that just because everything lives in the same repository doesn't mean everything runs together."

> "Tooling is everything."

> "The monorepo isn't a rejection of those principles [modular design, separation of concerns]. It's a different answer to a different problem."
