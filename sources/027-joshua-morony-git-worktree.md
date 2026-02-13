---
source_id: "027"
title: "Devs can no longer avoid learning Git worktree"
creator: "Joshua Morony"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=S8_AsOuAwLo"
date: "2026-02-04"
duration: "5:26"
type: "video"
tags: ["agentic-coding", "ai-sdlc"]
curriculum_modules: ["04-agentic-patterns"]
---

# 027: Devs can no longer avoid learning Git worktree

> **Creator**: Joshua Morony | **Platform**: YouTube | **Date**: 2026-02-04 | **Duration**: 5:26

## Summary

Joshua Morony makes the case that `git worktree` — a feature many developers have long ignored — has become essential in the age of agentic AI coding. The core problem: when AI agents execute multi-phase tasks autonomously for 15-60 minutes, they occupy your file system. You cannot safely work in the same codebase while agents are making edits to files on the same branch. Previously, the main use case for worktrees was occasional context switching (hot fixes, PR reviews), which could be sidestepped with stashing or careful commit hygiene. Agentic workflows make the conflict unavoidable and frequent.

Morony describes his own agentic workflow — a phased "track" system where a script launches successive AI agents to complete work and open a PR — and explains how he integrated worktree creation directly into that pipeline. Each new track automatically creates a dedicated worktree and branch, isolating agent work from the developer's main working directory. This lets the developer continue working on the primary codebase while agents operate in parallel, then review and merge the PR when ready.

The video is concise and practical, framing git worktrees not as an advanced Git trick but as fundamental infrastructure for anyone running autonomous AI agents against a codebase. The conceptual model is simple: worktrees let you have multiple branches checked out simultaneously in separate directories, all sharing the same Git history.

## Key Concepts

### The File System Contention Problem ([01:29](https://www.youtube.com/watch?v=S8_AsOuAwLo&t=89))

When agentic AI processes run for non-trivial durations (15-60 minutes), they monopolize the developer's file system. The developer faces an unproductive choice: wait idle, or risk conflicts by editing the same files the agents are modifying. Unlike traditional context-switching scenarios (hot fixes, PR reviews), this conflict is structural and recurring in agentic workflows — it cannot be solved by stashing or committing early.

### Git Worktrees as Parallel Workspaces ([03:02](https://www.youtube.com/watch?v=S8_AsOuAwLo&t=182))

A git worktree creates a copy of the project in a separate directory on the same file system, sharing the same Git tracking. This allows different branches to be checked out simultaneously in different directories. The key constraint: the same branch cannot be checked out in both the main repo and a worktree. Worktrees can be created via CLI (`git worktree add`) or through tools like LazyGit. Once work is complete, the worktree branch merges back like any normal branch.

### Automated Worktree Creation in Agentic Pipelines ([04:19](https://www.youtube.com/watch?v=S8_AsOuAwLo&t=259))

Rather than manually creating worktrees, Morony integrates worktree creation into his agentic workflow script. When agents begin work on a new track, they automatically create a worktree and branch, then operate exclusively within that worktree. This keeps the main project directory free for the developer. When the track completes, agents open a PR from the worktree branch for human review and merge.

### Detached HEAD for Reviewing Agent Work ([04:40](https://www.youtube.com/watch?v=S8_AsOuAwLo&t=280))

Since a branch checked out in a worktree cannot also be checked out in the main repo, Morony uses a detached HEAD checkout of the latest commit on the agent's branch to inspect work-in-progress from the main directory. This provides a read-only view of agent progress without interfering with the worktree. Alternatively, developers can switch to working directly in the worktree folder for hands-on changes.

## Practical Takeaways

- **Integrate worktree creation into your agentic scripts**: Automate `git worktree add` at the start of each agent task so isolation is the default, not an afterthought.
- **Use sibling directories for worktrees**: Morony places worktrees in a sibling directory (e.g., `project-worktrees/`) alongside the main repo, keeping the workspace organized.
- **Inspect agent branches via detached HEAD**: When you need to check on agent progress without disrupting its branch checkout, use `git checkout <commit-hash>` from the main repo for a read-only view.
- **Treat worktrees as disposable**: Each agent task gets its own worktree and branch; merge the PR and clean up the worktree when done.

## Notable Quotes

> "The problem is that these AI agents are using your file system and you want to use your file system, too." — Joshua Morony ([02:28](https://www.youtube.com/watch?v=S8_AsOuAwLo&t=148))

> "I get my agents to start executing on a task that is going to take 15 minutes, 30 minutes, an hour maybe, and I just what? Watch YouTube for a bit until the PR is ready to review." — Joshua Morony ([02:34](https://www.youtube.com/watch?v=S8_AsOuAwLo&t=154))

> "Whenever agents begin work on a new track, they will first create a work tree and branch for it. And they will only work within that work tree, which means I am then free to work on the main codebase as I please." — Joshua Morony ([04:24](https://www.youtube.com/watch?v=S8_AsOuAwLo&t=264))

## Related Sources

- [010: Claude Code Multi-Agent Orchestration with Opus 4.6](010-indydevdan-multi-agent-orchestration.md) — Demonstrates parallel agent teams using Tmux and sandboxes, a different approach to the same file system contention problem
- [024: You are Not Ready: Agentic coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) — Covers the broader agentic coding maturity ladder that contextualizes why worktrees become necessary at the "on-the-loop" and multi-agent levels
- [001: Claude Code Task System: ANTI-HYPE Agentic Coding](001-indydevdan-claude-code-task-system.md) — Task-based agentic workflow that benefits from worktree isolation

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Worktrees as infrastructure for sustained autonomous agent execution
