---
source_id: "137"
title: "I'm using claude --worktree for everything now"
creator: "Matt Pocock"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=yv8VZpov8bk"
date: "2026-02-21"
duration: "7:57"
type: "video"
tags: ["claude-code", "agentic-coding", "multi-agent"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 137: I'm using claude --worktree for everything now

> **Creator**: Matt Pocock | **Platform**: YouTube | **Date**: 2026-02-21 | **Duration**: 7:57

## Summary

Matt Pocock explores Claude Code's built-in git worktree support, which allows multiple agents to work in parallel on separate branches without interfering with each other. He walks through both manual git worktree usage and the `claude --worktree` command, discovering a key gotcha: worktrees branch from the current branch, so agents may accidentally push commits to main unless explicitly told to push to a named branch.

Despite the paper cut, Pocock is enthusiastic about the feature's potential for free parallelization — each worktree's lifecycle is tied to a single agent session, and subagents can also use worktrees. He sees this as a fundamental workflow enabler where every new idea can immediately spawn an isolated agent working toward a PR.

## Key Concepts

### Git Worktrees Primer ([00:00](https://www.youtube.com/watch?v=yv8VZpov8bk&t=0))

Git worktrees allow multiple branches to be checked out simultaneously in separate directories. Each worktree has its own git state and can be modified independently. VS Code picks up worktrees in its source control panel, enabling branch-specific commits and PRs without leaving the IDE.

### Claude --worktree Integration ([03:01](https://www.youtube.com/watch?v=yv8VZpov8bk&t=181))

Running `claude --worktree` automatically creates a worktree at `.claude/worktrees/` with a randomly generated name. Claude operates inside this isolated directory, makes commits, and can push work. On exit, the user chooses to keep or remove the worktree — removing it before pushing loses all commit history.

### Branch Naming Gotcha ([04:16](https://www.youtube.com/watch?v=yv8VZpov8bk&t=256))

The worktree branches from the current branch (typically main), so the agent's commits land on main by default. To push to a separate branch, the agent must explicitly specify the branch name in the push command. If main is unprotected, this can result in accidental pushes to main — a significant footgun that needs to be addressed through prompting or hooks.

### Free Parallelization ([06:05](https://www.youtube.com/watch?v=yv8VZpov8bk&t=365))

Worktrees make parallelization much cheaper. Every new idea can spawn a worktree, and the agent's lifecycle is scoped to that worktree. Subagents also support worktrees, enabling orchestrated workflows where multiple agents each produce PRs back to main.

## Practical Takeaways

- **Use worktrees for every Claude session**: Isolates agent work and guarantees clean PRs back to main
- **Always push to a named branch**: Default behavior pushes to the source branch (often main), so prompt or hook the agent to push to the worktree's branch name
- **Protect your main branch**: Without branch protection, worktree agents can accidentally commit directly to main
- **Subagents + worktrees**: Combine for orchestrated parallel workflows where each subagent owns its own branch

## Notable Quotes

> "I'm not sure why you wouldn't want to use git work trees like every single time you use Claude because it just means that you can guarantee that every single time you have an idea or you want to do something you can just like instantly ping up a new work tree, get things working and just like ping that back to main as a PR." — Matt Pocock ([06:16](https://www.youtube.com/watch?v=yv8VZpov8bk&t=376))

> "I just love it when a tool kind of absorbs the complexity of another tool into itself and helps you manage its life cycle." — Matt Pocock ([07:07](https://www.youtube.com/watch?v=yv8VZpov8bk&t=427))

> "AI coding is not that different from human coding. It's just that you need to be a lot more aware of the constraints and you need to be able to teach the AI about all the fundamentals that we've known for 30 years." — Matt Pocock ([07:25](https://www.youtube.com/watch?v=yv8VZpov8bk&t=445))

## Related Sources

- [027: Joshua Morony — Git Worktrees](027-joshua-morony-git-worktree.md) — Earlier coverage of git worktrees for agent workflows
- [113: Matt Pocock — Plan Mode](113-matt-pocock-plan-mode.md) — Pocock's previous Claude Code workflow exploration
- [129: Leon van Zyl — Multi-Agent Claude](129-leon-van-zyl-multi-agent-claude.md) — Multi-agent coordination patterns that benefit from worktree isolation

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Worktree integration as a core Claude Code feature
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Parallelization via worktree-scoped agents
