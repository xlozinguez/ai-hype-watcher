---
source_id: "499"
title: "Everyone Says Don’t Do This in Software… Big Tech Does It Anyway"
creator: "Uma Abu"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=mdCOGh4UFU4"
date: "2026-03-26"
duration: "10:18"
type: "video"
tags: ["enterprise-ai", "infrastructure", "ai-sdlc"]
curriculum_modules: ["06-strategy-and-economics"]
---

# 499: Everyone Says Don’t Do This in Software… Big Tech Does It Anyway

> **Creator**: Uma Abu | **Platform**: YouTube | **Date**: 2026-03-26 | **Duration**: 10:18

# Everyone Says Don't Do This in Software… Big Tech Does It Anyway

## Summary

This video explores why major tech companies—Google, Meta, Microsoft, Uber, Airbnb, and others—organize large portions of their codebases in monorepos, despite conventional software engineering wisdom favoring separate repositories per service. The creator draws on personal experience working in Microsoft's Substrate monorepo, engineering blogs, and a developer survey to explain both the rationale and the practical realities of this approach. The core clarification is that a monorepo is not one giant application—it's many independent projects sharing a single version-controlled repository while still building, testing, and deploying separately.

The video traces how monorepos solve specific coordination problems that emerge at massive scale: version mismatches across hundreds of repos, expensive cross-cutting refactors, slow dependency upgrades, and fragmented code visibility. But it's equally honest that monorepos create their own complexity—managing concurrent commits from thousands of developers, preventing build time explosions, and handling dependency resolution—and that these companies have invested heavily in custom tooling (Google's Piper/Bazel, Meta's Buck 2, Microsoft's virtual file system) to make the model viable.

The throughline is that monorepos are not a rejection of good software architecture principles like separation of concerns or modular design. They are a different answer to a different problem: at sufficient organizational scale, a well-tooled monorepo simplifies coordination overhead in ways that a fragmented poly-repo structure cannot. The choice is always a trade-off calibrated to the specific demands of a team's scale and situation.

## Key Concepts

### Monorepo vs. Application Monolith
The most common misconception is conflating a monorepo with a monolithic application. A monorepo simply means multiple independent projects share one version-controlled repository. Services still build, test, and deploy independently. Teams still own distinct code boundaries. The only thing that changes is *where* the code lives, not *how it runs*. This mental model shift—"same repo, independent systems"—is the primary hurdle for developers coming from poly-repo environments.

### Tooling as the Enabling Constraint
Monorepos at scale are only viable because of purpose-built infrastructure. Git alone is insufficient for millions of files and thousands of concurrent committers. Companies have built or heavily modified version control systems (Google's Piper, Meta's enhanced Mercurial), virtual file systems so developers never clone the full repo, and smart build tools that incrementally rebuild only affected code paths (Bazel, Buck 2). The lesson: the architectural pattern and the tooling investment are inseparable. Without the tooling, the pattern fails.

### Single Version Policy
Rather than letting each service drift to different versions of shared dependencies, monorepo organizations typically standardize on a single version across the codebase. This eliminates a whole class of compatibility bugs and prevents teams from quietly falling behind on dependencies until they become a crisis. Teams can pin specific versions when genuinely needed, but the default expectation is that the entire organization moves forward together—creating shared momentum toward a healthier codebase.

### Large-Scale Refactoring and Security Response
Code visibility across the entire codebase unlocks operational capabilities that are difficult or impossible in poly-repo setups. A single search can identify every consumer of an internal API. A security fix to a shared library can be propagated across hundreds of services in one coordinated change rather than filed as dozens of separate tickets across separate repositories. This makes both planned migrations and emergency security responses significantly more tractable.

### Independent Deployment Within a Shared Repository
Monorepos work best when teams retain deployment autonomy. The high-functioning implementations described in the video deliberately avoid forcing services into coordinated release trains. Dependencies are centrally managed; deployments remain independent per team. This balance—shared code location and visibility, decoupled release cadence—is what distinguishes a productive monorepo from one that creates bottlenecks.

## Practical Takeaways

- **Don't evaluate a monorepo in isolation from its tooling.** The architecture is only as good as the build system, virtual file system, and CI/CD infrastructure supporting it. If you're considering a monorepo without a plan for incremental builds and selective checkout, you're adopting the complexity without the benefits.
- **Monorepos shift coordination costs, they don't eliminate them.** Poly-repos shift coordination costs to dependency versioning and cross-repo refactoring; monorepos shift them to tooling investment and build system maintenance. Know which cost your team is better positioned to absorb.
- **Code visibility is a genuine multiplier for large engineering orgs.** Universal search, direct cross-team bug fixes, and studying real production patterns from other teams are concrete collaboration benefits—not just theoretical ones.
- **The single version policy prevents dependency debt accumulation.** If adopting a monorepo, standardizing dependencies from the start and enforcing forward momentum prevents the "someone else's emergency" problem of long-neglected dependency upgrades.
- **Reserve monorepos for sufficient scale.** The video is explicit that there is no universally correct answer. For smaller teams or fewer services, the tooling investment required to make a monorepo work may not be justified by the coordination benefits gained.

## Notable Quotes

> "The biggest challenge when moving to a mono repo is realizing that just because everything lives in the same repository doesn't mean everything runs together."

> "Tooling is everything."

> "The mono repo isn't a rejection of those principles [modular design, separation of concerns]. It's a different answer to a different problem."
