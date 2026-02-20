---
source_id: "101"
title: "I Built a Self-Improving Agent Swarm. It Rewrote Its Own Code."
creator: "Jaymin West"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=97irLVqYJCI"
date: "2026-02-16"
duration: "14:31"
type: "video"
tags: ["multi-agent", "agent-teams", "agentic-coding", "claude-code"]
curriculum_modules: ["05-team-orchestration", "04-agentic-patterns"]
---

# 101: I Built a Self-Improving Agent Swarm. It Rewrote Its Own Code.

> **Creator**: Jaymin West | **Platform**: YouTube | **Date**: 2026-02-16 | **Duration**: 14:31

## Summary

Jaymin West demonstrates Overstory, his custom agent swarm system built on top of Claude Code, running live on a real codebase. The video shows a coordinator agent receiving a list of GitHub issues, decomposing them into team leads, which in turn spawn builder and reviewer agents -- all operating in isolated git worktrees. In one session, the swarm processed nine issues with 22 agents, produced 26 commits, and ran for about an hour with only two human prompts.

The most striking claim is that Overstory is "self-improving": during the demo run, the swarm implemented its own review loop feature, merged it, and then used that new feature for subsequent tasks within the same session. This is a concrete example of recursive self-modification in a controlled agent system -- the code the agents wrote changed how the agents themselves operated in real time.

## Key Concepts

### Coordinator-Lead-Builder Hierarchy

Overstory uses a three-tier agent hierarchy: a single coordinator orchestrates the entire workflow, team leads gather context and decompose work, and builder agents make actual code changes. Lead agents are deliberately prevented from editing files directly -- they must delegate to builders. This forced delegation pattern keeps context windows fresh and prevents agents from accumulating too much state.

### Isolated Worktrees for Parallel Execution

Each agent operates in its own git worktree, enabling true parallel development without merge conflicts during active work. The coordinator manages a merge queue that integrates completed work back to main. This architectural choice is key to scaling beyond 5-10 agents -- West reports the system handling up to 30 agents and running autonomously for over 2 hours.

### Self-Improving Code in Real Time

The demo's headline feature: the swarm implemented a mandatory code review loop that did not exist before the session started. Once merged, subsequent agents used the new review process. This is recursive self-improvement at the tooling layer -- not the model layer -- but it demonstrates how agent systems can evolve their own workflows during execution.

### Trust and Unpredictability Tradeoffs

West is candid about the challenges: swarms are "highly unpredictable," agents occasionally go rogue (attempting to edit files they should not), and the system requires significant trust. The Overstory framework includes guardrails like denying edit tools to lead agents and using nudges for course correction, but the fundamental unpredictability of many LLMs running concurrently remains an open problem.

## Practical Takeaways

- **Force delegation over direct execution**: Preventing lead/coordinator agents from editing code directly produces better outcomes by keeping builder agents focused with fresh context windows.
- **Git worktrees are essential for multi-agent development**: Isolated worktrees prevent the merge conflicts that would otherwise make parallel agent work impractical.
- **Start with issue trackers as input**: Feeding the swarm a list of tracked issues (via Beads or similar) provides structured context that coordinators can decompose effectively.
- **Expect agent swarms to be unpredictable**: Even well-structured swarms produce surprising behavior -- budget time for monitoring and course correction rather than assuming hands-off operation.
- **Self-improving systems are possible but require guardrails**: Letting agents modify their own tooling is powerful but requires architectural boundaries to prevent runaway modifications.

## Notable Quotes

> "That is sort of the truth of agentic swarms, right? We are very much abstracting our role as the human in the loop to a point of where I am now out of the loop." — Jaymin West

> "I would rather an agent with a fresh context window try and fix a problem than an agent dig itself into a hole trying to fix five problems at once." — Jaymin West

> "The swarm is improving its own code in real time... which is absolutely insane." — Jaymin West

## Related Sources

- [010: Claude Code Multi-Agent Orchestration with Opus 4.6](010-indydevdan-multi-agent-orchestration.md) — IndyDevDan's earlier multi-agent patterns that Overstory builds upon
- [055: I Built an Open-Source Rig That Measures Multi-Agent Architectures](055-brainqub3-multi-agent-measurement.md) — Brainqub3's measurement framework for evaluating multi-agent effectiveness
- [004: Claude Code's New Agent Teams Are Insane](004-bart-slodyczka-agent-teams.md) — First-generation agent team patterns that Overstory extends with self-improvement

## Related Curriculum

- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Coordinator-lead-builder hierarchy and worktree-based parallel execution
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Forced delegation, fresh context windows, and builder/reviewer separation
