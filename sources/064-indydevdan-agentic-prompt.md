---
source_id: "064"
title: "One Prompt Every AGENTIC Codebase Should Have (For Engineering Teams)"
creator: "IndyDevDan"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=3_mwKbYvbUg"
date: "2026-01-26"
duration: "22:36"
type: "video"
tags: ["agentic-coding", "claude-code", "prompt-engineering", "context-engineering", "ai-sdlc"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 064: One Prompt Every AGENTIC Codebase Should Have (For Engineering Teams)

> **Creator**: IndyDevDan (Dan Disler) | **Platform**: YouTube | **Date**: 2026-01-26 | **Duration**: 22:36

## Summary

IndyDevDan argues that every agentic codebase should have a standardized install/maintain prompt -- a natural language document that combines deterministic setup scripts with agentic intelligence to handle codebase installation, onboarding, and ongoing maintenance. The video introduces Claude Code's new setup hook (supporting `init` and `maintenance` lifecycle events) and demonstrates how to layer agentic prompts on top of these hooks to create interactive, self-healing installation workflows. The central claim: deterministic scripts alone are not novel, but combining them with agentic prompts that can validate results, resolve common issues, and walk engineers through configuration interactively is a fundamentally better approach to codebase lifecycle management.

The video also introduces the `just` command runner (justfile) as a launchpad for standardizing how engineers and agents interact with a codebase. The justfile serves as a single entry point for all workflows -- setup, maintenance, agent invocations with specific CLI flags -- eliminating the need for engineers or agents to remember or look up commands. IndyDevDan frames this as part of his 2026 theme: increasing trust in agents by combining "the old world of engineering" (deterministic code, scripts, hooks) with "the new world of agents" (prompts, skills, sub-agents, multi-agent orchestration).

The practical pattern is straightforward: a setup hook runs deterministic installation steps (dependency installation, database setup, migrations), logs results, and then an agentic prompt reads those logs, validates the installation, reports status, and -- in interactive mode -- walks the engineer through remaining configuration steps with human-in-the-loop questions. This creates what IndyDevDan calls "a living document that executes" -- natural language instructions that actually perform the work they describe, with intelligence to handle edge cases and common failures.

## Key Concepts

### The Setup Hook: Init and Maintenance

Claude Code's new setup hook runs before sessions start and supports two lifecycle events:

- **Init**: Runs on first setup or when the `--init` flag is passed. Handles dependency installation (`uv sync`, `npm install`), database initialization, and any one-time setup tasks.
- **Maintenance**: Runs periodically for ongoing upkeep -- dependency updates (`npm update`), database migrations, artifact cleanup, security checks, dead code detection.

The hooks themselves are deterministic scripts -- nothing novel for production codebases that already have setup scripts. The value emerges when these hooks are combined with agentic prompts that validate, report, and resolve issues intelligently.

### Deterministic Code + Agentic Prompts = Best of Both Worlds

The core architectural insight: neither deterministic scripts nor agentic prompts alone are sufficient. Scripts provide predictable execution but cannot handle unexpected failures or guide engineers through configuration decisions. Agents provide intelligence and interactivity but lack the reliability of deterministic execution for known steps. The combination delivers:

- **Predictable execution** for known installation steps (scripts)
- **Intelligent oversight** for validation and error resolution (agent)
- **Interactivity** for configuration decisions that require human input (human-in-the-loop prompts)

The pattern: run the deterministic hook first, log everything, then let an agentic prompt read the logs, validate results, and handle whatever comes next.

### The Justfile as Agent Launchpad

The `just` command runner (justfile) serves as a standardized entry point for all codebase operations. IndyDevDan uses it to encode:

- Setup commands (`just setup-frontend`, `just setup-backend`)
- Agent invocations with specific CLI flags and prompts (`just cli`, `just clmm`)
- Maintenance workflows
- Reusable agent configurations

The justfile eliminates the "look up the right flags" problem -- engineers, new hires, and agents themselves can type `just` to see all available commands. It functions as a launchpad that standardizes how both humans and agents interact with the codebase.

### Interactive Installation with Human-in-the-Loop

The most powerful pattern demonstrated is the interactive installation mode. When the `mode` argument is set to interactive, the install prompt shifts from one-shot execution to a guided conversation:

1. The agent asks configuration questions (database handling, installation scope, environment variable setup)
2. The engineer answers (fresh database vs. existing, full vs. minimal install, guided vs. manual env setup)
3. The agent executes steps based on answers, running prerequisite checks (Python, Node, UV versions)
4. The agent configures environment variables, handles blocked files appropriately, and asks for confirmation
5. The agent pulls in external documentation and validates the full setup

This pattern directly addresses onboarding friction -- instead of one to two days of pair programming, Slack messages, and outdated docs, a new engineer runs one command and gets intelligent, interactive guidance through the entire setup process.

### Encoding Common Issues into Prompts

A key maintenance pattern: when installation or maintenance issues recur, encode the problem-solution pairs directly into the prompt. The format is simple:

```
## Common Issues
If you encounter any of the following issues, follow the steps to resolve them.

### Problem: Database corruption
**Solution**: Clear the database and rerun the initialization script.
```

This turns the installation prompt into an evolving knowledge base. Every time a new failure mode is discovered, it gets encoded into the prompt, making the agent progressively better at handling issues without human intervention. The format (markdown, YAML, whatever) does not matter -- agents can read any structured text.

### The Living Document That Executes

IndyDevDan frames the install/maintain prompt as a "living document that executes." Unlike static README files or onboarding docs that go stale, these prompts are actively used every time an engineer sets up the codebase. Because they execute (rather than just describe), they stay accurate -- if the prompt is wrong, the installation fails, forcing an update. This creates a positive feedback loop: the prompt is both the documentation and the implementation, so the two cannot drift apart.

## Practical Takeaways

- **Add an install prompt to every codebase**: Create a `/install` or `/setup` command that combines deterministic setup scripts with an agentic prompt for validation and error resolution. This is the single highest-ROI prompt for engineering teams.
- **Use the Claude Code setup hook for lifecycle management**: Configure `init` and `maintenance` hooks to run deterministic steps before agent sessions start. Log everything so the agent can read and report results.
- **Adopt a justfile as your codebase launchpad**: Standardize all commands -- setup, maintenance, agent invocations -- in a single `justfile`. Engineers and agents type `just` to see everything available.
- **Build interactive mode for onboarding**: Add a human-in-the-loop branch to your install prompt that walks new engineers through configuration decisions interactively, rather than pointing them at a README.
- **Encode failure modes into the prompt**: Every time an installation issue recurs, add a problem/solution pair to the prompt. The agent gets smarter with each iteration.
- **Think about agent sandboxes**: The install prompt pattern is especially valuable for spinning up agent sandboxes and new development environments where codebases need to be set up from scratch repeatedly.

## Notable Quotes

> "You can tell how great an engineering team is by the time it takes for a new engineer to run the project locally." -- IndyDevDan

> "Agents when combined with code beats either alone." -- IndyDevDan

> "When you combine deterministic hooks with standardized agentic prompts, you get the best of both worlds. Predictable execution, intelligent oversight, and interactivity when you need it." -- IndyDevDan

> "We can now communicate action in natural language and encode that for the installation and maintenance of your code bases as they grow." -- IndyDevDan

> "Our theme for this year in 2026 is to increase the trust we have in our agents." -- IndyDevDan

## Related Sources

- [001: Claude Code Task System: ANTI-HYPE Agentic Coding](001-indydevdan-claude-code-task-system.md) -- IndyDevDan's earlier work on task systems and meta-prompts; the install prompt extends these patterns to codebase lifecycle management
- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) -- Skills as lazy-loaded instructions complement the install prompt pattern; skills handle specialized capabilities while the install prompt handles codebase setup
- [010: Claude Code Multi-Agent Orchestration](010-indydevdan-multi-agent-orchestration.md) -- Multi-agent orchestration uses the same justfile and agent sandbox patterns discussed here for scaling across codebases
- [024: You are Not Ready: Agentic coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) -- Covers similar themes of combining prompt engineering with Claude Code hooks for standardized agentic workflows
- [040: Stop Feeding Claude Your Entire CLAUDE.md](040-charlie-automates-claudemd-context.md) -- Context engineering principles that apply to keeping install prompts focused and loading context on demand

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) -- Setup hooks, justfile integration, and the Claude Code lifecycle for codebase management
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) -- The deterministic-plus-agentic pattern, human-in-the-loop workflows, and encoding domain knowledge into reusable prompts
