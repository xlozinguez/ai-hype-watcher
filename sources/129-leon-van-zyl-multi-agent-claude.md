---
source_id: "129"
title: "One Claude Code Agent? That's Your First Mistake"
creator: "Leon van Zyl"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=6nFRJftouI0"
date: "2026-02-20"
duration: "15:31"
type: "video"
tags: ["agentic-coding", "claude-code", "multi-agent", "vibe-coding"]
curriculum_modules: ["04-agentic-patterns", "05-multi-agent"]
---

# 129: One Claude Code Agent? That's Your First Mistake

> **Creator**: Leon van Zyl | **Platform**: YouTube | **Date**: 2026-02-20 | **Duration**: 15:31

## Summary

Van Zyl demonstrates Git worktrees as a practical technique for running multiple Claude Code instances in parallel on the same codebase. The core problem: developers ask Claude to make a change, dislike the result, ask for a rollback, try a different approach, and often lose valuable work in the process. This serial workflow leaves significant Claude Code capability on the table. Git worktrees solve this by creating independent copies of the project directory that share the same Git history, enabling parallel experimentation.

The video walks through a concrete example — redesigning a fitness tracker app's UI using three different approaches simultaneously: one worktree using a front-end design skill, another using a reference image to build a design system, and a third using Gemini 3.1 Pro instead of Claude entirely. Each worktree gets its own Claude Code (or competing model) instance working independently. The results can be compared side-by-side, and the preferred variant is merged back into the main branch while discarding the rest. Git tracks all relationships between worktrees and main, making the merge clean.

This is a simple but high-leverage technique that transforms AI-assisted development from a serial, trial-and-error process into a parallel exploration workflow. It also enables practical side-by-side model comparison — testing Claude against Gemini on the exact same codebase with the exact same starting point.

## Key Concepts

### Git Worktrees for Parallel AI Development ([02:00](https://www.youtube.com/watch?v=6nFRJftouI0&t=120))

Git worktrees create full replicas of a project directory at the filesystem level, but unlike copy-paste, the main branch maintains awareness of all worktrees. Each worktree can have its own Claude Code instance running independently. This enables parallel exploration: one agent works on a feature in worktree A while another fixes a bug in worktree B, and completed work from either can be merged back to main without affecting the other.

### Parallel Design Exploration ([05:00](https://www.youtube.com/watch?v=6nFRJftouI0&t=300))

The demonstrated workflow creates three design variants simultaneously: (1) Claude Code with a front-end design skill from skills.sh, (2) Claude Code with a reference image and generated design system stored in docs/design, and (3) Google's Antigravity IDE with Gemini 3.1 Pro. Each approach produces a distinct result that can be reviewed side-by-side before committing to a direction. This replaces the common serial pattern of try-revert-try-revert.

### Model Comparison on Identical Baselines ([09:00](https://www.youtube.com/watch?v=6nFRJftouI0&t=540))

Because each worktree starts from the exact same codebase state, worktrees provide a controlled environment for comparing models. Van Zyl notes that Gemini 3.1 Pro produced notably strong animations and SVG work, while Claude with a design skill produced bold, distinctive styling. The worktree approach makes these comparisons fair and practical rather than anecdotal.

## Practical Takeaways

- **Use worktrees for any non-trivial design decision**: Instead of asking Claude to try approach A, reverting, then trying approach B, create worktrees and let separate agents explore each approach in parallel.
- **Worktrees enable model A/B testing**: Same codebase, same starting point, different models or different techniques — worktrees make side-by-side comparison practical.
- **Close worktree terminals before merging**: When ready to merge a preferred worktree back to main, close all terminal sessions referencing other worktrees to avoid conflicts.
- **Let Claude create the worktrees**: You do not need to know Git commands — simply ask Claude Code to create the worktrees and it handles the setup.
- **Combine with skills for maximum variance**: Assign different skills, reference images, or models to each worktree to maximize the diversity of solutions generated.

## Notable Quotes

> "You ask Claude to make a change and if you don't like it, you ask Claude to back out everything and then try a different approach. And sometimes you actually lose a lot of valuable work along the way." — Leon van Zyl ([00:10](https://www.youtube.com/watch?v=6nFRJftouI0&t=10))

> "It's kind of like having multiple universes where each has a very different take on the exact same project." — Leon van Zyl ([09:30](https://www.youtube.com/watch?v=6nFRJftouI0&t=570))

## Related Sources

- [027: Devs Can No Longer Avoid Learning Git Worktree](027-joshua-morony-git-worktree.md) — Joshua Morony's earlier case for worktrees in AI-assisted development
- [014: I Gave Opus 4.6 an Entire Dev Team](014-leon-van-zyl-agent-teams.md) — Van Zyl's earlier work on multi-agent Claude Code patterns
- [013: Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) — The skills system used in worktree variant 1

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Git worktrees as parallel exploration infrastructure, skills-based design
- [Module 05: Multi-Agent](../curriculum/05-multi-agent/README.md) — Running multiple independent agent instances on shared codebase
