---
source_id: "314"
title: "AI-Generated Code Is Creating a New Kind of Technical Debt"
creator: "Imran Gardezi"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=S5kQRgJ-iug"
date: "2026-03-09"
duration: "11:50"
type: "video"
tags: ["vibe-coding", "ai-sdlc", "validation", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 314: AI-Generated Code Is Creating a New Kind of Technical Debt

> **Creator**: Imran Gardezi | **Platform**: YouTube | **Date**: 2026-03-09 | **Duration**: 11:50

## Summary

Imran Gardezi argues that AI-generated code is producing a new and particularly insidious form of technical debt — one that's harder to detect than traditional debt because it passes tests, ships to production, and looks correct until it catastrophically isn't. Drawing on direct experience managing multiple client codebases, he identifies that the core danger isn't code that fails obviously, but code that "almost works": it clears automated gates, satisfies code review, and only reveals its flaws months later under specific conditions, by which point other code has been built on top of it.

The video catalogs five specific patterns of AI-generated debt: (1) broken workflows that nobody can debug because nobody had to understand the code to write it, (2) suppressed linter/type errors rather than fixed errors, (3) phantom duplicate code and dead exports generated without awareness of the existing codebase, (4) convention violations where AI defaults to internet-wide patterns instead of team-specific ones, and (5) the compounding nature of all four as subsequent AI generations build on flawed foundations. The unifying principle is that plausible code is more dangerous than wrong code, and that trust in AI-generated code among developers is already declining as teams learn this the hard way.

Gardezi's practical response is a three-question PR review framework designed to catch these patterns in under a minute: does the code reuse existing utilities and types, does it follow team conventions, and can the developer explain the logic without leaning on the AI's own comments? He positions AI as a force multiplier that amplifies disciplined teams but makes undisciplined ones dangerous — the tool isn't the problem, the absence of targeted review discipline is.

---

## Key Concepts

### "Almost Right" Debt Is More Expensive Than "Completely Wrong" Code

Wrong code fails fast — tests catch it, builds break, it gets thrown away cheaply. Code that almost works passes review, ships, sits in production for months, and accumulates dependencies before failing. By then the cost isn't fixing one file; it's untangling everything built on a flawed foundation. This asymmetry means the very quality that makes AI output impressive — plausibility — is also what makes its failure modes uniquely costly.

### Five Patterns of AI-Generated Debt

The specific failure modes Gardezi observes across client codebases: **(1) Opaque workflows** — AI generates complex logic (e.g., OAuth PKCE flows) that passes review but nobody understands well enough to debug when it breaks; **(2) Suppressed errors** — AI resolves TypeScript or linter errors by disabling the warnings rather than fixing the underlying issue, silencing the type system's immune response; **(3) Phantom/duplicate code** — AI generates new utilities, types, and exports without knowing what already exists, causing horizontal codebase growth through redundancy rather than features; **(4) Convention drift** — AI applies internet-wide conventions rather than project-specific ones, producing inconsistent naming, error handling, and file structure; **(5) Compounding** — each layer of AI generation builds on the debt of previous layers, amplifying all four patterns.

### The Three-Question PR Review Framework

A lightweight review heuristic targeting AI-specific failure modes: **(1) Does it reuse?** — search for existing utilities, types, or patterns that already serve this purpose before accepting new code; **(2) Does it follow conventions?** — verify naming, file structure, and error handling match the existing codebase identity; **(3) Can the developer explain it without the AI's comments?** — the submitting developer must be able to walk through the logic line by line unaided, otherwise the code is unmaintainable by definition. Each question maps directly to one or more of the five debt patterns.

### AI as Force Multiplier, Not Replacement for Understanding

The military analogy Gardezi uses is precise: night-vision goggles make trained soldiers more effective but are useless and dangerous in untrained hands. AI coding tools amplify whatever discipline (or lack thereof) the team already has. Some code — auth flows, payment processing, data migrations — is too critical to generate without deep understanding by the developer writing it. The time "saved" by AI generating code nobody understands is borrowed time, paid back with interest when debugging begins.

### Type Systems and Linters as Diagnostic Infrastructure

The ESLint-disable pattern is treated as a canary: 200+ suppressed warnings across a codebase represent the type system actively being dismantled. Each suppression is a lie ("this is fine") placed over a real problem. When AI layers new generated code on top of suppressed errors, it inherits and extends the broken type context, adding further suppressions. The practical consequence is that the type system — the primary automated tool for catching semantic errors — becomes progressively meaningless.

---

## Practical Takeaways

- **Audit recent AI-assisted PRs immediately**: Pull the last 10 PRs with AI-generated code and run the three questions. The results will map where debt is already accumulating — patterns will be visible at the codebase level, not just the file level.
- **Make "can you explain this without the AI's comments?" a hard gate**: If a developer can't walk through the logic independently, the PR should be returned regardless of test status. Understanding is a prerequisite for maintainability.
- **Search before accepting new utilities or types**: Before merging any AI-generated helper function, type definition, or constant, do a codebase search for equivalent existing implementations. Dead exports and duplicate types are easy to prevent and expensive to untangle later.
- **Treat ESLint/TypeScript suppressions as blocking red flags in code review**: A new `// eslint-disable` or `@ts-ignore` in AI-generated code should require explicit justification, not pass silently as a formatting quirk. Each one is a masked error, not a solved one.
- **Enforce convention compliance as a review criterion, not an aesthetic preference**: Inconsistent naming and error-handling patterns degrade the shared mental model of the codebase. One mismatch is a quirk; ten is a codebase losing coherence and making the next AI generation less reliable.

---

## Notable Quotes

> "Almost right passes code review. Almost right ships to production. Almost right sits in your codebase for six months before anyone realizes it's wrong."

> "Your type system is your immune system and AI is teaching your codebase to suppress its immune system."

> "When AI writes code nobody understands, you haven't saved time. You borrowed it with interest."

---
