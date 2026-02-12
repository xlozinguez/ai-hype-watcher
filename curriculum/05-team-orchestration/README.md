# Module 05: Team Orchestration

> Coordinate multiple AI agents working together — agent teams, multi-agent patterns, sandboxes, and observability.

## Overview

When single agents aren't enough, teams of agents can tackle complex, multi-faceted projects. This module covers the architecture of multi-agent systems: how agent teams differ from sub-agents, coordination patterns, sandbox environments for safe execution, and the observability tooling needed to maintain trust at scale.

## Prerequisites

- [Module 04: Agentic Patterns](../04-agentic-patterns/README.md)

## Key Topics

- Agent Teams vs. sub-agents (shared task list + peer messaging vs. isolated context)
- Multi-agent orchestration patterns (Tmux, E2B sandboxes)
- The devil's advocate pattern
- Emergent hierarchy in agent teams
- Human-in-the-loop controls (stopping, redirecting individual agents)
- Observability for multi-agent systems (160+ tool calls/minute)
- Token cost tradeoffs (~5x for teams vs. single agents)

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [#004: Agent Teams](../sources/004-bart-slodyczka-agent-teams.md) | Bart Slodyczka | Agent Teams demo, single vs. team comparison |
| [#010: Multi-Agent Orchestration](../sources/010-indydevdan-multi-agent-orchestration.md) | IndyDevDan | Opus 4.6 orchestration at scale, Tmux, E2B |
| [#013: Full Dev Team](../sources/013-leon-van-zyl-full-dev-team.md) | Leon van Zyl | Five-agent teams, devil's advocate, peer messaging |

## Further Reading

*Content will be compiled from sources using `/compile-curriculum 05`*
