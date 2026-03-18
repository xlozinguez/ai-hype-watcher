---
source_id: "314"
title: "AI-Generated Code Is Creating a New Kind of Technical Debt"
creator: "Imran Gardezi"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=S5kQRgJ-iug"
date: "2026-03-09"
duration: "11:50"
type: "video"
tags: ["vibe-coding", "ai-sdlc", "validation", "enterprise-ai"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 314: AI-Generated Code Is Creating a New Kind of Technical Debt

> **Creator**: Imran Gardezi | **Platform**: YouTube | **Date**: 2026-03-09 | **Duration**: 11:50

# AI-Generated Code Is Creating a New Kind of Technical Debt

## Summary

Imran Gardezi, drawing on 15 years of shipping production systems and managing multiple client codebases, argues that AI-generated code introduces a specific and underdiagnosed form of technical debt. The central thesis is counterintuitive: *almost right* code is more expensive than *completely wrong* code, because broken code fails fast and gets discarded, while plausible-but-flawed code passes review, ships to production, and accumulates compounding interest over months before the failure surfaces. With 66% of developers citing "almost right" as their top frustration with AI tools, this pattern is systemic, not anecdotal.

The video catalogs five concrete debt patterns observed across real client codebases: broken workflows nobody can debug (because the AI wrote them and nobody had to understand them), suppressed errors masquerading as fixes (ESLint/TypeScript warnings silenced rather than resolved), phantom code (duplicate utilities and dead exports generated because AI doesn't know what already exists), and convention violations (AI follows internet conventions, not team conventions). Each pattern shares the same root cause: AI generates *plausible* code, not *correct* code, and plausible is the most dangerous word in software engineering.

The practical response is not to stop using AI but to treat it as a force multiplier that requires disciplined aim. Gardezi proposes reviewing AI-generated PRs like code from a talented contractor who has never seen the codebase—and operationalizes this with a three-question framework: Does it reuse existing code? Does it follow conventions? Can the developer explain it line-by-line without reading the AI's comments? Teams that applied this framework reduced review turnaround from three days to same-day, because reviewers had clear pass/fail criteria rather than open-ended line-by-line reading.

## Key Concepts

### The "Almost Right" Cost Asymmetry
Completely wrong code is cheap—tests fail, builds break, and the code gets thrown away quickly. Almost right code is expensive: it passes automated gates, clears code review, ships to production, and sits silently accruing dependencies for months. When it eventually breaks, the cost isn't fixing one file; it's untangling three months of code built on a flawed foundation. This asymmetry is the defining economic risk of AI-assisted development at scale.

### Error Suppression as Debt Accumulation
A particularly insidious pattern: when AI encounters a TypeScript or linting error, the path of least resistance is suppressing the warning (e.g., `// eslint-disable-next-line`) rather than fixing the underlying type issue. Each suppression is a lie—a comment saying "this is fine" over a type system screaming "this is wrong." These compound: subsequent AI-generated code references the broken types and adds more suppressions, layer on layer, until the type system becomes meaningless. The analogy offered: AI is teaching your codebase to suppress its own immune system.

### Phantom Code and Horizontal Codebase Growth
Because AI generates code from training data rather than from knowledge of your specific codebase, it frequently creates duplicate utilities, redundant type definitions, and dead exports. A codebase with a tested `formatDate` function will grow a second, then a third version as different AI sessions re-solve the same problem. Dead exports persist because new engineers assume they must be used somewhere and build around them. The codebase grows horizontally—not from new features, but from accumulated redundancy—and each subsequent change costs more.

### Understanding Debt as a Pre-Condition for Maintainability
The PKC authentication flow case study illustrates a deeper problem: when AI writes code that nobody had to think through, the team loses the ability to debug it. The bug took two days to reproduce and two hours to fix—the asymmetry caused entirely by absence of understanding, not complexity of the fix. The principle generalizes: if a developer can't explain code without reading the AI's comments, the code isn't ready to ship, because unmaintainable code is effectively dead code on a delay.

### The Three-Question Review Framework
Rather than reading AI-generated PRs line-by-line, Gardezi's team applies three targeted questions with binary pass/fail criteria: (1) **Does it reuse?**—search the codebase for existing utilities, types, or patterns that already solve the problem; if they exist, delete the new code. (2) **Does it follow conventions?**—naming, file structure, error handling, state management; if not, refactor before merge. (3) **Can the developer explain it without the AI's comments?**—delete the annotations mentally and ask for a walkthrough; if they're reading docs, send it back. This narrows review effort to known failure modes and produces faster, higher-confidence outcomes.

## Practical Takeaways

- **Audit existing PRs before assuming you're clean.** Pull the last 10 AI-generated PRs, search for suppressed linting/type comments, duplicate utility functions, and unexplained exports. What you find tells you exactly where debt is already hiding—without needing any new process.
- **Make "does it reuse?" a pre-commit habit, not just a review gate.** Developers should search the codebase for existing solutions before accepting AI-generated code, not after. Reviewers catching duplication after the fact adds friction; developers catching it before submission normalizes reuse.
- **Treat convention violations as blockers, not style suggestions.** One file that doesn't match is a quirk; ten files is a codebase losing its identity. Establish that AI-generated code must match naming, error handling, and structural conventions before merge—period.
- **Require developer comprehension as a shipping requirement.** The question is not "does it work?" but "can this person maintain it when it breaks at 2am under load?" If the answer is no, the time savings from AI generation are borrowed, not real—and borrowed time pays compound interest.
- **Frame AI as a force multiplier requiring disciplined operators.** Night-vision goggles on someone who's never held a weapon are useless and dangerous. Use AI to accelerate developers who already understand the codebase and domain; don't use it to substitute for that understanding on critical paths like auth, payments, or data migrations.

## Notable Quotes

> "Almost right passes code review. Almost right ships to production. Almost right sits in your codebase for six months before anyone realizes it's wrong. And by then, the cost to fix has compounded into something nobody budgeted for."

> "When AI writes code nobody understands, you haven't saved time. You borrowed it with interest."

> "Your type system is your immune system and AI is teaching your codebase to suppress its immune system."
