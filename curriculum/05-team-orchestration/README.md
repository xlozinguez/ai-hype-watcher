# Module 05: Team Orchestration

> Coordinate multiple AI agents working in parallel -- from understanding the architecture of agent teams to designing roles, managing coordination, and building observability into multi-agent workflows.

## Overview

Single agents hit a ceiling. When the work is complex enough -- standing up an entire application, reviewing a large codebase from multiple angles, debugging a system that spans frontend, backend, and data layers -- a single context window and a single stream of execution become bottlenecks. Team orchestration is the practice of splitting work across multiple specialized agents that run in parallel, communicate with each other, and coordinate through shared task structures.

This module covers the full spectrum of multi-agent coordination in Claude Code: the architectural differences between sub-agents and agent teams, how to design team compositions and role specializations, the infrastructure options for running agents at scale (Tmux, E2B sandboxes, split-pane terminals), and the observability tooling required to maintain trust and visibility when dozens of agents are executing simultaneously. The core question is not "can I run multiple agents?" but "when should I, and how do I keep them coordinated?"

The concepts here build directly on the agentic patterns from Module 04. Sub-agents (the Task tool) are the foundation; agent teams extend them with peer-to-peer communication and shared coordination layers. Understanding both -- and knowing which to reach for -- is the central skill of this module.

## Prerequisites

- [Module 04: Agentic Patterns](../04-agentic-patterns/README.md) -- Sub-agents, the builder/validator pattern, and the task system are foundational to team orchestration

## Core Concepts

### Concept 1: Sub-Agents vs. Agent Teams -- Two Architectures for Parallel Work

The most important distinction in multi-agent Claude Code is the difference between sub-agents and agent teams. They solve different problems and have different coordination models.

**Sub-agents** (the Task tool) are spawned by a parent agent to handle isolated tasks. Each sub-agent has its own context window but operates in a strictly hierarchical relationship: it receives instructions from the parent, does its work, and reports back. Sub-agents cannot see what other sub-agents are doing. As Leon van Zyl explains: "One sub agent does not have a view of what another sub agent is doing. So, sub agent one in theory could implement a change that's actually not compatible with what sub agent 2 is doing."

**Agent teams** break this isolation. When a team is created, the primary agent becomes the team lead and creates a shared task list that all team members can see. Team members communicate directly with each other via peer-to-peer messaging -- the database expert can align with the API developer on schema design in real time, rather than each working from separate assumptions and hoping the parent agent resolves conflicts after the fact.

As Van Zyl puts it: "This is the equivalent of bringing a bunch of people into the same room and they can converse with each other to work together to achieve a task." Sub-agents are sending five people to separate rooms with instructions to report back. Agent teams bring them into the same room.

| Aspect | Sub-Agents | Agent Teams |
|--------|-----------|------------|
| Communication | One-way: report back to parent only | Peer-to-peer: direct dialogue between teammates |
| Coordination | Parent agent is sole coordinator | Shared task list with self-coordination |
| Context | Each has own window, no shared view | Each has own window plus shared task visibility |
| Sessions | Run within parent's orchestration | Each teammate runs as a full, independent Claude Code instance |
| Token cost | Lower (focused, shorter-lived) | Higher (~5x for a 5-person team) |
| Best for | Isolated, scoped tasks | Complex, interdependent multi-faceted work |

As Bart Slodyczka demonstrates in his side-by-side comparison ([#004](../../sources/004-bart-slodyczka-agent-teams.md)), build times between single-agent and team approaches are comparable (roughly 6-7 minutes for the same task manager application). The advantage of teams is not speed but functional depth: the team approach produced features that were never requested -- board views, export/import capabilities, comprehensive settings panels -- suggesting deeper architectural thinking by the specialized teammates.

### Concept 2: The Shared Task List as Coordination Layer

The shared task list is the architectural heart of agent teams. When a team is created, the team lead's first action is to build this list. It serves as the primary coordination mechanism: team members can see what others are working on, understand dependencies, and communicate about interface boundaries.

As IndyDevDan documents in his orchestration walkthrough ([#010](../../sources/010-indydevdan-multi-agent-orchestration.md)), the full lifecycle follows a clear sequence:

1. **TeamCreate** -- Create the team
2. **TaskCreate** -- Build the task list with dependencies
3. **Spawn agents** -- One per task or work area
4. **Work in parallel** -- Agents communicate via SendMessage
5. **Shut down agents** -- As work completes
6. **TeamDelete** -- Force a clean context reset

The task list replaces the parent agent as the coordination bottleneck. Instead of every question and every dependency resolution flowing through a single orchestrator, team members can check the task list to understand the full picture and message each other directly to resolve interface questions. This is the difference between a hub-and-spoke topology (sub-agents) and a mesh topology (agent teams).

### Concept 3: Team Composition and Role Design

How you structure a team matters as much as whether you use one. The source material reveals two complementary approaches to role design.

**Functional specialization**: Van Zyl's demonstration ([#014](../../sources/014-leon-van-zyl-agent-teams.md)) uses five roles for building a fitness tracker app: UX/UI designer, back-end developer, technical architect, database expert, and a devil's advocate. Each role maps to a distinct area of expertise, and the team's output quality comes from each specialist applying deep domain knowledge within their lane while coordinating at the boundaries.

**Scale-oriented parallelism**: IndyDevDan's approach ([#010](../../sources/010-indydevdan-multi-agent-orchestration.md)) is more about throughput. He creates teams of four Opus agents, each handling one of eight full-stack applications -- the same role replicated across different workloads. When the first team of four finishes, a second team of four handles the remainder. This pattern treats agents as a compute resource to be scaled horizontally.

The key design decision is whether your work decomposes along expertise boundaries (use functional specialization) or along workload boundaries (use parallel replication). Complex, tightly-coupled systems favor specialization. Independent, loosely-coupled workloads favor replication.

### Concept 4: The Devil's Advocate Pattern

Van Zyl's inclusion of a devil's advocate role -- a team member whose explicit job is to "question everything the other team members do" -- represents a built-in quality gate within the team structure. Rather than running a separate validation pass after the team completes its work, the challenger operates as a peer during execution, catching issues in real time.

This maps conceptually to the builder/validator pattern from Module 04 (see also: [Module 04: Agentic Patterns](../04-agentic-patterns/README.md)), but with an important difference: in the builder/validator pattern, validation is sequential -- build, then review. In the team devil's advocate pattern, the challenger works concurrently with the builders, creating a continuous feedback loop rather than a batch review cycle. The tradeoff is that the devil's advocate consumes a full agent's worth of tokens and context, so it is most justified for high-stakes or architecturally complex work.

### Concept 5: Individual Agent Autonomy and Human Interaction

Each agent team member runs as a full Claude Code instance with its own context window, tool access, skills, and MCP servers. This means individual agents can be interrupted, redirected, and instructed independently without affecting the rest of the team.

Van Zyl demonstrates this by pressing Escape to pause just the UI designer while the other four agents continue running. He then sends a targeted message to the paused agent: "please use the front end design skill to assist you with the UI design." This granular control -- the ability to inject skills, correct course, or refine requirements for a single team member mid-execution -- is a significant advantage over monolithic single-agent workflows where any interruption pauses everything.

Navigation between team members uses keyboard shortcuts:
- **Shift + Arrow keys** to toggle between the team lead and individual teammates
- **Shift + Tab** to toggle delegate mode (restricts the lead to coordination-only)
- **Escape** to interrupt a specific agent without affecting others

### Concept 6: Infrastructure for Multi-Agent Execution

Running multiple agents simultaneously requires infrastructure choices that directly affect visibility, safety, and scale.

**Tmux** is the primary tool for multi-agent visualization. As IndyDevDan demonstrates ([#010](../../sources/010-indydevdan-multi-agent-orchestration.md)), the multi-pane view lets you see all agents working simultaneously, providing the visual feedback loop needed for effective oversight. Agent teams can also run in in-process mode within a single terminal, but you lose the ability to see all agents at once. Split-pane mode requires tmux or iTerm2 (not VS Code terminal, Windows Terminal, or Ghostty).

**E2B agent sandboxes** provide cloud-based isolated environments for each agent. IndyDevDan had 24 sandboxes running simultaneously during his demonstration, each running for up to 12 hours. Sandboxes are critical for safety at scale -- agents operating in isolated environments cannot accidentally modify your local machine, corrupt shared state, or interfere with each other's file systems. For privacy-sensitive workflows, a dedicated local device (such as a Mac Mini) serves as an alternative to cloud sandboxes.

**Configuration** is lightweight. Agent teams are enabled by adding `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` to your Claude Code settings.json or exporting it as an environment variable. No Docker containers, no external frameworks -- just configuration and a well-structured prompt.

### Concept 7: Multi-Agent Observability

When you have eight agents making 160+ tool calls in under a minute, you cannot rely on watching terminal output. Observability becomes a hard requirement, not a nice-to-have.

IndyDevDan's open-source observability system ([github.com/disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)) captures:
- Session start and end hooks for every agent
- Every tool call, with timing and results
- Task creation and status updates
- "Swim lanes" that let you isolate a single agent's activity from the fleet
- Searchable tool types across all agents

The system uses Claude Code hooks (the same hooks covered in Module 04) to capture events automatically, requiring no changes to your prompts or agent configurations. The key insight is that without observability, you cannot improve your multi-agent systems -- you are flying blind, unable to diagnose coordination failures, identify bottleneck agents, or optimize team compositions.

### Concept 8: Context Engineering Through Delegation

A subtle but important insight from IndyDevDan's demonstration: the primary orchestrating agent used only 31% of its context window while coordinating eight sub-agents. Delegation is not just a way to parallelize work -- it is a context engineering strategy.

By offloading detailed work to team members, the lead agent preserves its context for coordination, decision-making, and synthesis. Each team member gets a fresh context window for their specific task, avoiding the degradation that comes from stuffing too much information into a single context. This connects directly to the context engineering principles in Module 02 (see also: [Module 02: Prompting & Workflows](../02-prompting-and-workflows/README.md)) -- the same discipline of curating what goes into the context window, applied at the team level rather than the prompt level.

The corollary is that deleting teams when work is done (TeamDelete) forces a clean context reset between phases. This is not cleanup -- it is a deliberate quality practice that prevents context contamination between unrelated work streams.

## Patterns & Practices

### Pattern 1: Functional Team for Complex Builds

- **When to use**: Building a multi-layered application from scratch (frontend + backend + database + infrastructure) or any project where different areas of expertise must coordinate at interface boundaries.
- **How it works**: Define 3-5 specialized roles (e.g., UI designer, backend developer, database expert, technical architect, devil's advocate). Specify the model for each (typically Opus for complex work). The team lead creates a shared task list, spawns teammates, and coordinates work through the shared task list and peer-to-peer messaging.
- **Example**: Van Zyl builds "Claude Fit" (a fitness tracker) with five Opus agents. The team lead creates the task list first, then spawns specialists. The UI designer receives a mid-execution skill injection. The devil's advocate challenges architectural decisions in real time. Result: a fully functional application with coordinated frontend/backend/database layers.
- **Source**: [#014: Leon van Zyl](../../sources/014-leon-van-zyl-agent-teams.md)

### Pattern 2: Parallel Replication for Independent Workloads

- **When to use**: Processing multiple independent codebases, applications, or work units where each unit requires the same type of work but on different inputs.
- **How it works**: Create a team sized to your throughput needs (typically 4 agents per team). Assign each agent to one independent workload. Run multiple teams sequentially if workloads exceed team size. Use Tmux for visualization and observability hooks for tracking.
- **Example**: IndyDevDan processes eight full-stack applications using two sequential teams of four Opus agents each. Team 1 handles apps 1-4, Team 2 handles apps 5-8. Each agent independently sets up E2B sandboxes, uploads code, installs dependencies, and boots the application. 6 of 8 succeed on first pass; a third ad hoc team addresses the 2 failures.
- **Source**: [#010: IndyDevDan](../../sources/010-indydevdan-multi-agent-orchestration.md)

### Pattern 3: Exploratory Team for Debugging and Analysis

- **When to use**: Investigating a complex bug, performing a comprehensive code review, or analyzing a problem that benefits from multiple competing hypotheses.
- **How it works**: Create a team where each member investigates a different theory or examines a different subsystem. Members actively try to disprove each other's hypotheses, reducing anchoring bias. The shared task list ensures no one duplicates effort.
- **Example**: Anthropic recommends assigning distinct team members to different areas of the codebase for parallel review coverage -- security, performance, and test coverage specialists working simultaneously. For debugging, multiple teammates investigate different theories and share findings in real time.
- **Source**: [#004: Bart Slodyczka](../../sources/004-bart-slodyczka-agent-teams.md) (referencing Anthropic's recommended use cases)

### Pattern 4: Tiered Model Selection

- **When to use**: When cost matters and not all team tasks require the most capable model.
- **How it works**: Use Opus for the team lead and for complex, judgment-heavy tasks (architecture, review, the devil's advocate role). Use Haiku for high-volume, lower-complexity tasks (summarization, exploration, boilerplate generation). The prompt specifies the model for each team member independently.
- **Example**: IndyDevDan's first demo uses eight Haiku agents for codebase summarization (a read-heavy, lower-complexity task) while his second demo uses four Opus agents for application deployment (requiring judgment and troubleshooting). The model choice matches the cognitive demands of each task.
- **Source**: [#010: IndyDevDan](../../sources/010-indydevdan-multi-agent-orchestration.md)

## Common Pitfalls

- **Using teams for simple tasks**: Agent teams add coordination overhead (shared task lists, peer messaging, multiple context windows) that is only justified for complex, interdependent work. For isolated one-off tasks -- file exploration, targeted code changes, focused refactoring -- sub-agents are faster, cheaper, and simpler. As Van Zyl advises: "If you just want to do like a once-off task, you should definitely use sub agents instead."

- **Underestimating token costs**: A 5-person agent team uses roughly 5x the tokens of a single agent. This is not a hidden cost -- it is a direct consequence of each teammate running as a full Claude Code instance. Before creating a team, ask whether the quality and feature depth improvement justifies the cost multiplier. For exploratory or experimental work, start with a single agent and escalate to a team only if you hit the complexity ceiling.

- **No observability**: Running multiple agents without visibility into their activity is flying blind. You cannot diagnose coordination failures, identify agents that are stuck or duplicating work, or improve your team compositions if you do not know what happened. Invest in observability hooks before scaling to large teams.

- **Skipping team cleanup**: Failing to delete teams (TeamDelete) after work completes leaves stale context that can contaminate subsequent work. The delete is not optional cleanup -- it is a deliberate context reset that maintains quality across multi-step workflows.

- **Expecting speed improvements**: Bart Slodyczka's comparison ([#004](../../sources/004-bart-slodyczka-agent-teams.md)) shows that build times between single-agent and team approaches are comparable. Teams provide depth, not speed. If your primary goal is faster execution, teams may not deliver the improvement you expect.

- **Ignoring initial bugs**: Team output may require refinement fixes that single-agent output does not. In Bart's experiment, the agent team's task manager needed a JavaScript fix before buttons worked, while the single-agent version worked immediately. Budget time for integration testing and quick fixes after team builds.

- **No session resumption**: Agent teams do not survive session interruptions. The `/resume` and `/rewind` commands do not restore teammates. If your terminal closes or your connection drops, the team state is lost. For long-running work, use the observability system to track progress so you can reconstruct state if needed.

## Hands-On Exercises

1. **Sub-agent vs. team comparison**: Take a moderately complex project (a CRUD application with frontend, backend, and database) and build it twice -- once with sub-agents and once with an agent team. Compare the results on feature depth, code quality, coordination quality at interface boundaries, total token usage, and time to working output. Document which approach produced better results and why.

2. **Role design experiment**: Create the same project with three different team compositions: (a) 3 agents with broad roles, (b) 5 agents with narrow specializations, (c) 4 specialists plus a devil's advocate. Compare outputs to understand how role granularity affects team performance and coordination overhead.

3. **Tmux multi-agent setup**: Configure a Tmux session with split panes, enable agent teams, and run a team of 4 agents on a multi-faceted task. Practice navigating between agents using Shift+Arrow keys, interrupting and redirecting individual agents, and injecting skill instructions mid-execution. The goal is fluency with the interaction model, not the output quality.

4. **Observability integration**: Set up IndyDevDan's multi-agent observability system ([github.com/disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)). Run a team workflow and then review the captured data: tool call counts, session timelines, agent swim lanes. Identify which agent consumed the most context, which made the most tool calls, and whether any agents duplicated work.

5. **Context budget analysis**: Run a team of 4-8 agents and monitor the lead agent's context window usage. Verify that delegation keeps the lead's context consumption low (IndyDevDan observed 31% usage while orchestrating 8 agents). Experiment with different delegation strategies to find the balance between lead oversight and context preservation.

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [004: Claude Code's New Agent Teams Are Insane](../../sources/004-bart-slodyczka-agent-teams.md) | Bart Slodyczka | Single agent vs. team comparison, setup guide, team architecture, known limitations |
| [010: Claude Code Multi-Agent Orchestration](../../sources/010-indydevdan-multi-agent-orchestration.md) | IndyDevDan | Opus 4.6 orchestration at scale, Tmux, E2B sandboxes, observability, Core Four framework |
| [014: I Gave Opus 4.6 an Entire Dev Team](../../sources/014-leon-van-zyl-agent-teams.md) | Leon van Zyl | Sub-agents vs. teams architecture, devil's advocate pattern, individual agent interaction, skills composition |

## Further Reading

- [Claude Code Agent Teams documentation](https://docs.anthropic.com/en/docs/claude-code) -- Official Anthropic documentation for the experimental agent teams feature
- [IndyDevDan's multi-agent observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) -- Open-source observability hooks for tracking multi-agent workflows
- [E2B agent sandboxes](https://e2b.dev) -- Cloud-based sandboxed environments for running agents safely at scale
- [Module 04: Agentic Patterns](../04-agentic-patterns/README.md) -- Sub-agents, builder/validator, and the foundational task system that teams build upon
- [Module 02: Prompting & Workflows](../02-prompting-and-workflows/README.md) -- Context engineering principles that apply at the team level through delegation
