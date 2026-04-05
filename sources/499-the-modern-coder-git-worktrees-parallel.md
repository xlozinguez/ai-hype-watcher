---
source_id: "499"
title: "Git Worktrees: Work on all your ideas at once"
creator: "The Modern Coder"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=jmAJQEooFhg"
date: "2026-03-23"
duration: "7:44"
type: "video"
tags: ["multi-agent", "agentic-coding", "ai-sdlc"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 499: Git Worktrees: Work on all your ideas at once

> **Creator**: The Modern Coder | **Platform**: YouTube | **Date**: 2026-03-23 | **Duration**: 7:44

# Git Worktrees: Work on All Your Ideas at Once

## Summary

Git worktrees solve a fundamental friction point in development workflows: the single working directory constraint that forces developers to stash or throwaway-commit in-progress work before switching context. A worktree is a new, independent folder on disk that contains a full copy of project files at a given branch, but crucially shares the same underlying Git repository, commit history, and objects as every other worktree in the project. This means switching between parallel workstreams requires nothing more than navigating into a different directory.

The mechanics are deliberately simple: three commands (`git worktree add`, `git worktree list`, `git worktree remove`) and filesystem navigation are all that's needed. Each worktree folder contains a `.git` file that is merely a pointer back to the main repository—no duplicated history, no duplicated objects—which is why worktree creation is nearly instantaneous compared to cloning. The one key constraint is that a branch can only be checked out in one worktree at a time, preventing conflicting edits to the same branch across workspaces.

For AI-assisted development specifically, worktrees are a natural fit for running multiple agents in parallel. Each agent can operate in its own clean worktree without interfering with in-progress work elsewhere, and any commits made in one worktree are immediately available to all others through the shared history. The pattern eliminates the stash/unstash ceremony that compounds quickly when context switching is frequent.

## Key Concepts

### Worktrees as Independent Working Directories
A worktree is a directory on disk containing a copy of project files at a specific branch state, completely isolated from other in-progress changes. Unlike cloning—which duplicates the entire repository history—a worktree only copies project files. The `.git` entry inside each worktree folder is a simple pointer back to the main `.git` directory, making creation instant and storage lightweight.

### Shared Commit History Across All Worktrees
All worktrees within a project share the same underlying Git repository, history, and object store. A commit made inside one worktree is immediately visible and accessible from any other worktree. Merging, staging, and branching all work with standard Git commands—there is no new syntax or mental model required beyond navigation.

### Branch Locking Constraint
When a branch is checked out in a worktree, that branch is locked to that worktree and cannot be simultaneously checked out in another. `git branch` output marks locked branches with a `+` symbol and the currently active branch with `*`. This constraint prevents conflicting edits and is enforced automatically by Git.

### Switching Worktrees via Filesystem Navigation
There is no `git worktree switch` command. Switching between worktrees is simply a matter of `cd`-ing into the target worktree's directory. Git automatically reflects whichever branch that worktree has checked out. The default worktree always lives at the project root; additional worktrees are sibling folders by convention.

### Practical Parallel Workflow Pattern
The primary use case is isolating concurrent workstreams: leave in-progress feature work untouched, `git worktree add` a new folder from a stable branch (e.g., `main` for a hotfix, or a teammate's PR branch for review), do the work, remove the worktree when done. No stashing, no throwaway commits, no manual cleanup of unfinished state.

## Practical Takeaways

- **Replace stash/throwaway-commit habits with worktrees** when needing to context switch: `git worktree add <name> <branch>` creates a clean workspace in seconds without disturbing in-progress work.
- **Use worktrees instead of cloning** when parallel work on the same repository is needed—creation is instant and storage cost is minimal since history is shared.
- **Reviewing a teammate's PR** is a clean two-command workflow: `git fetch` + `git worktree add testing <their-branch>`, test in isolation, then `git worktree remove testing` to clean up completely.
- **Running multiple AI agents in parallel** maps naturally onto worktrees—each agent gets its own clean working directory and branch, with no interference and full access to shared history.
- **`git worktree remove`** deletes project file copies and frees the locked branch, but all commits and history remain in the repository safely.

## Notable Quotes

> "If you're context switching a lot or running multiple AI agents in parallel, that friction can compound faster than you think."

> "That's why creating a worktree is instant. Git is only copying project files, not your entire project history. It's another reason why you might want to use worktrees instead of cloning if you need to work on multiple things simultaneously."

> "All these fancy tech YouTubers with all their worktree jargon, they can come fight me."
