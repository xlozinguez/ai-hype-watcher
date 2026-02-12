# Module 04: Agentic Patterns

> Learn the architectural patterns that make AI agents reliable -- builder/validator, task systems, meta-prompts, lifecycle hooks, and the long-horizon strategies that keep agents coherent over extended work sessions.

## Overview

The transition from "AI assists the developer" to "AI leads, developer reviews and steers" is not a theoretical prediction -- it is the current daily workflow of power users who have adapted to models like Claude Opus 4.6. But autonomous agents that implement substantial features, refactor across files, and run for hours do not succeed by accident. They succeed because of architectural patterns that provide structure, safety, and quality assurance around what is fundamentally a probabilistic system.

This module covers those patterns. The builder/validator pattern separates implementation from review, mirroring proven engineering practices. The task system provides dependency-aware coordination across multiple agents. Meta-prompts encode organizational standards into reusable workflows. Lifecycle hooks add deterministic control over agent behavior at critical moments. And long-horizon strategies -- compaction, memory, and agent decomposition -- keep agents coherent as context windows fill up over extended sessions.

These patterns are not theoretical constructs. They come from working engineers who have pushed AI-assisted development past the "ask a question, get an answer" stage into sustained autonomous work. The capability is here; the challenge is building the scaffolding that makes it reliable. As IndyDevDan puts it: "The task system is on by default if you write a large enough prompt, but building out a meta prompt is more valuable." The difference between ad hoc agent usage and disciplined agentic engineering is precisely the patterns covered in this module.

## Prerequisites

- [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md) -- Skills system, context management, and Claude Code configuration

## Core Concepts

### Concept 1: The Workflow Inversion -- From "AI Assists" to "AI Leads"

As Nate B Jones describes in [#016], Claude Opus 4.6 crossed a qualitative threshold that changed the fundamental workflow dynamic. With earlier models, the developer drove the process and the AI filled in gaps -- autocomplete, boilerplate generation, answering questions. With Opus 4.6, the model can take the lead on substantial implementation tasks: designing the approach, making architectural decisions across files, implementing the solution, and explaining what it did. The developer's role shifts to specification, review, and course correction.

Two specific capability improvements underpin this shift. First, sustained reasoning over longer task horizons -- complex multi-file refactors that would cause earlier models to contradict themselves or forget context now complete reliably. Second, a significant drop in hallucination rate, enough that the developer can trust the model's output as a starting point rather than treating every line with suspicion. As Jones notes, trust is the prerequisite for delegation, and Opus 4.6 has crossed that trust threshold for many practical tasks.

This inversion is not universal. High-risk production code still demands close supervision. And the errors models make are conceptual, not syntactic -- similar to what a hasty junior developer would produce. As Nate B Jones documents in [#008], these are "supervision problems, not capability problems." The patterns in this module exist to provide that supervision at scale.

### Concept 2: The Claude Code Task System

The Claude Code Task System, introduced by Anthropic in late January 2026, provides native infrastructure for structured multi-agent coordination. As IndyDevDan explains in [#001], the task system enables teams of agents to communicate toward shared goals through four core tools:

- **TaskCreate**: Define a new task with description, objectives, and dependency relationships
- **TaskUpdate**: Modify task status, add notes, or update completion criteria
- **TaskList**: View all tasks and their current states
- **TaskGet**: Retrieve detailed information about a specific task

Key architectural properties:

- **Dependency graphs**: Tasks can block other tasks, forming directed acyclic graphs (DAGs). When a task completes, anything blocked by it automatically unblocks and the next wave kicks off.
- **Persistent state**: Tasks are written to the local filesystem (`~/.claude/tasks/`), following a UNIX-philosophy approach to state management.
- **Cross-session coordination**: Multiple Claude Code instances can share and coordinate on the same task list.
- **Isolated context**: Each spawned sub-agent gets its own fresh 200K token context window, completely isolated from the main conversation.

The critical insight from [#008] is that dependencies should be structural, not cognitive. Without externalized dependencies, the agent has to hold the entire plan in working memory, and the plan degrades as the context window fills up. When you externalize the dependencies as a task sheet, the graph does not forget and does not drift.

> "The task system is on by default if you write a large enough prompt, but building out a meta prompt is more valuable." -- IndyDevDan ([#001])

### Concept 3: The Builder/Validator Pattern

The builder/validator pattern, detailed by IndyDevDan in [#001], is a two-agent pairing designed for increasing trust in delivered work:

- **Builder Agent** (`builder.md`): Has full tool access (Bash, Edit, Write, Read, etc.) and is responsible for implementing code changes, running builds, and executing tasks. The builder does the actual work.
- **Validator Agent** (`validator.md`): Has **read-only access** and is responsible for reviewing the builder's work, verifying completion quality, checking for correctness, and ensuring the task meets its acceptance criteria. The validator cannot modify code -- it can only inspect and report.

This pattern mirrors real-world engineering practices (code review, QA) but automates them within the agent orchestration framework. For each task in a plan, a builder and validator pair are assigned (e.g., `session_end_builder` and `session_end_validator`), creating a structured quality gate at each step.

The architectural significance goes beyond simple verification. The validator's read-only constraint is enforced through tool permissions, not through prompting. This is deterministic control -- the validator physically cannot modify code, regardless of what instructions it receives. This distinction between "asked not to" and "cannot" is fundamental to building trustworthy agentic systems.

### Concept 4: Meta-Prompts and Reusable Workflows

Building reusable meta-prompts -- prompts that generate other prompts -- is presented in [#001] as one of the most valuable patterns in agentic engineering. Meta-prompts encode engineering best practices and enable deployment of consistent, highly vetted workflows that can be used repeatedly across projects.

IndyDevDan's `/plan_w_team` command from the `claude-code-hooks-mastery` repository exemplifies this pattern. It operates as a team lead that produces a structured plan including:

- Task descriptions and objectives
- Relevant files to be modified
- Step-by-step tasks with explicit dependency chains
- Team member assignments (builder/validator pairs)
- Validation criteria for each task

The meta-prompt does not build, write code, or deploy agents directly. Its sole output is a plan document. This separation of planning from execution is deliberate -- it creates a review point where a human can inspect and adjust the plan before committing agent compute to executing it.

The companion repository also includes a meta-agent (`meta-agent.md`) -- a specialized sub-agent that generates new sub-agents from descriptions. This is what IndyDevDan calls "building the thing that builds the thing":

> "Figure out how to scale it up. Build the thing that builds the thing." -- IndyDevDan ([#001])

### Concept 5: Lifecycle Hooks for Deterministic Control

IndyDevDan's `claude-code-hooks-mastery` repository ([#001]) implements all 13 Claude Code lifecycle hooks, providing deterministic control points over agent behavior:

| Hook | When It Fires | Can Block? |
|------|---------------|------------|
| UserPromptSubmit | Before Claude sees user input | Yes |
| PreToolUse | Before tool execution | Yes |
| PostToolUse | After successful tool completion | No |
| PostToolUseFailure | When tools fail | No |
| Notification | When Claude sends alerts | No |
| Stop | When Claude finishes responding | Yes |
| SubagentStart | When subagents spawn | No |
| SubagentStop | When subagents complete | Yes |
| PreCompact | Before session compaction | No |
| SessionStart | On session startup/resume | No |
| SessionEnd | On session exit/error | No |
| PermissionRequest | Permission dialogs appear | No |
| Setup | Repository initialization | No |

The key hooks for agentic workflows:

- **PreToolUse** blocks dangerous commands (e.g., `rm -rf`) and sensitive file access (`.env`, secrets) -- deterministic safety that does not rely on the LLM's judgment
- **PostToolUse** logs all agent actions as JSON for observability -- every tool call becomes an auditable record
- **SubagentStop** can block subagent completion if validation fails -- enforcement at the orchestration layer
- **UserPromptSubmit** validates and enhances prompts before Claude processes them -- input sanitization for the agent

Each hook is a standalone Python script with embedded dependencies (UV single-file scripts). Exit code 0 means success; exit code 2 means critical error (blocks execution for blocking hooks). All hook events are logged as JSON for auditability.

The fundamental principle: do not rely solely on LLM judgment for safety and quality. Use lifecycle hooks for deterministic control at every critical point in the agent's execution.

### Concept 6: Long-Horizon Strategies -- Compaction, Memory, and Agent Decomposition

For agents that run for extended periods -- hours or days of autonomous work -- context window exhaustion is the primary failure mode. Tim Berglund ([#011]) describes three strategies for managing this:

**Compaction**: Use an LLM call to summarize large resources or conversation history into condensed versions. LLMs are excellent at summarization -- a 50,000-token document can often be compressed to 500 words without losing decision-relevant information. Both Anthropic and OpenAI shipped native context compaction in late 2025, as documented in [#008], allowing models to summarize their own work as sessions extend.

**Memory**: A key-value store local to the agent where intermediate results, structured data, or lengthy outputs can be parked and retrieved on demand rather than persisted in the context window across every call. This follows the same principle as skills: not everything needs to be in context all the time.

**Agent decomposition**: Split complex agents into composed sub-agents. If your agent has a complex document-search workflow, that should be its own agent. The parent agent can ask the sub-agent for a concise summary rather than carrying the full search context. As Berglund notes, this mirrors microservice decomposition -- agents naturally evolve from monoliths to composed systems.

These strategies connect directly to Berglund's "60-70% rule": research consistently shows that filling a context window to 100% capacity does not give the best results. Performance peaks at roughly 60-70% of window capacity. Long-horizon strategies exist to maintain that headroom even as work accumulates.

> "More isn't always better. Somewhere in the 60 to 70% of the capacity of the context window is probably where you get your best results." -- Tim Berglund ([#011])

### Concept 7: Ralph and the Power of Simple Loops

One of the most influential agentic patterns emerged not from a research lab but from a bash script. As Nate B Jones documents in [#008], Jeffrey Huntley wrote a bash script called Ralph that runs Claude Code in a loop, using git commits and files as memory between iterations. When the context window fills up, a fresh agent picks up where the last one left off.

The technique is "embarrassingly simple" -- while the AI industry was building elaborate multi-agent frameworks, Huntley discovered that a loop that keeps running until tests pass is more reliable than carefully choreographed agent handoffs. VentureBeat called it "the biggest name in AI right now."

Ralph embodies a key principle of power user patterns from [#008]: **accept imperfection and iterate**. The AI will produce broken code, so you make it retry until it fixes it. It never gets tired. This requires abandoning the expectation that AI should get things right the first time.

Anthropic's native Task System can be understood as the productized version of what Ralph demonstrated as a prototype: persistent agent coordination with context isolation across sessions.

### Concept 8: The Bottleneck Shift -- From Writing to Evaluating

As Jacob Schmitt from CircleCI argues in [#018], when AI accelerates code generation by an order of magnitude, the constraint moves from writing code to evaluating it. Decision-making -- not implementation -- becomes the bottleneck. This has cascading implications for agentic patterns:

- **Infrastructure must validate at machine speed**: If your CI/CD pipeline takes 30 minutes to validate a change, it does not matter that AI generated the change in 30 seconds. Fast builds, continuous testing, and real-time failure signals are prerequisites for realizing AI's productivity gains.
- **Code review processes need redesign**: Review processes designed for human-paced output cannot absorb AI-paced input. Tiered review -- automated validation for routine changes, human review reserved for architectural and high-risk decisions -- becomes essential.
- **Engineering roles shift**: Senior engineers move from implementation toward architecture, review, and judgment. As Schmitt puts it: "What it means to be a senior engineer fundamentally changes when machines handle execution."

Multiple sources converge on this point. Nate B Jones ([#008]) cites Maggie Appleton: "When agents write the code, design becomes the bottleneck." The capability overhang is not about whether AI can do the work -- it can. The overhang is in the human systems (review, validation, deployment) that have not yet adapted to AI-paced output.

> "When AI can generate ten solutions quickly, the valuable skill becomes choosing the right one for your context." -- Jacob Schmitt ([#018])

## Patterns & Practices

### Pattern 1: Builder/Validator Task Execution

- **When to use**: Any implementation task where you want structured quality assurance without manual review of every line.
- **How it works**: Create a task with the task system. Assign a builder agent (full tool access) to implement the change. Assign a validator agent (read-only access) to verify correctness against acceptance criteria. The validator's inability to modify code is enforced by tool permissions, not by prompting.
- **Example**: From IndyDevDan's [#001] -- the `/plan_w_team` command generates a plan with explicit builder/validator pairs for each task: `session_end_builder` implements session cleanup logic, `session_end_validator` reviews it read-only against the specified criteria.
- **Source**: [#001]

### Pattern 2: Dependency-Aware Task Decomposition

- **When to use**: Complex features that span multiple files, services, or concerns and have natural ordering constraints.
- **How it works**: Decompose the feature into tasks with explicit dependency relationships forming a DAG. Independent tasks run in parallel. Dependent tasks wait for their blockers to complete. The task system manages sequencing automatically.
- **Example**: A full-stack feature might decompose into: database migration (no dependencies) -> API endpoint (depends on migration) -> frontend component (depends on API) -> integration test (depends on all). The migration and any independent setup tasks run in parallel; the API work begins only when its dependencies resolve.
- **Source**: [#001], [#008]

### Pattern 3: Skill-Augmented Agent Teams

- **When to use**: When different sub-agents in a task system need different specialized capabilities.
- **How it works**: Skills load on demand per-agent based on the task context (see [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md)). A front-end builder agent automatically activates design and accessibility skills. A backend builder activates database and API skills. Each agent gets the specialized knowledge it needs without bloating other agents' contexts.
- **Example**: IndyDevDan ([#015]) describes skill composition patterns that emerge naturally from auto-activation: sequential chaining (one skill's output feeds another's input), parallel activation (multiple skills for different aspects of the same prompt), and nested composition (a higher-level skill orchestrating lower-level ones).
- **Source**: [#015], [#001]

### Pattern 4: The Autonomous Loop Pattern (Ralph-Style)

- **When to use**: Tasks with clear success criteria (tests pass, build succeeds, linting clean) where iterative retry is acceptable.
- **How it works**: Run the agent in a loop. On each iteration, the agent attempts the task. If success criteria are not met, a fresh agent instance picks up where the last left off, using git commits or files as persistent state between iterations. The loop continues until success criteria are met or a maximum iteration count is reached.
- **Example**: Ralph ([#008]) -- a bash loop that runs Claude Code persistently, using git commits as memory. When the context window fills up, a new agent picks up the work. The agent keeps running until tests pass.
- **Source**: [#008]

### Pattern 5: Tiered Review for AI-Paced Output

- **When to use**: When your engineering team generates more code through AI assistance than your review pipeline can absorb.
- **How it works**: Automate validation of routine concerns (linting, type checking, test coverage, security scanning) so they never reach human reviewers. Fast-path low-risk changes (documentation, test additions, simple refactors) with lighter review. Reserve thorough human review for high-risk changes (architecture, security boundaries, data models). Use lifecycle hooks to enforce the tiers automatically.
- **Example**: CircleCI ([#018]) recommends connecting AI tools to delivery pipelines via MCP so that generated code flows through automated validation before human eyes see it. The validator agent pattern from [#001] automates the first tier within the agent system itself.
- **Source**: [#018], [#001]

### Pattern 6: Context Window Preservation through Agent Decomposition

- **When to use**: Any agent workflow that runs long enough to risk context window exhaustion (typically beyond 15-20 iterative tool calls).
- **How it works**: Identify sub-workflows that are self-contained reasoning tasks. Extract them into sub-agents with their own context windows. The parent agent receives a concise summary from each sub-agent rather than accumulating the full reasoning history. Apply compaction to the parent agent's context when intermediate details are no longer needed.
- **Example**: Tim Berglund ([#011]) describes the pattern directly: "If your agent has a complex document-search workflow, that's its own agent. The parent agent can ask the sub-agent for a concise summary rather than carrying the full search context."
- **Source**: [#011], [#008]

### Pattern 7: Policy-Driven Agent Supervision

- **When to use**: When multiple engineers or teams use AI agents across codebases with different risk profiles.
- **How it works**: Define explicit agent-coding policies per codebase or risk tier. High-risk production code: agent runs in supervised mode with human approval for writes. Green-field prototypes: agent runs autonomously with only test-based validation. The policy is encoded in lifecycle hooks, CLAUDE.md, and team conventions -- not left to individual judgment.
- **Example**: Nate B Jones ([#008]) recommends that technical leaders "define agent-coding expectations per codebase based on risk profile. High-risk production code requires watching the agent in an IDE and writing careful evals. Green-field prototypes allow stepping back."
- **Source**: [#008]

## Common Pitfalls

- **Relying on automatic task system activation instead of deliberate meta-prompts**: The task system activates automatically for large, complex prompts, but automatic activation lacks the organizational context and standards baked into a well-crafted meta-prompt. Deliberate meta-prompts enforce specific patterns (builder/validator pairs, dependency structures, validation criteria) and produce more consistent results.

- **Spawning sub-agents without dependency awareness**: Ad hoc sub-agent calls without task system coordination lead to race conditions, duplicated work, and agents that overwrite each other's changes. Use the task system's dependency DAG to ensure proper sequencing.

- **Trusting LLM judgment for safety instead of deterministic hooks**: The agent might usually avoid destructive commands, but "usually" is not a safety guarantee. Use PreToolUse hooks to block dangerous operations deterministically. The opening demonstration in IndyDevDan's [#001] video -- Claude Code attempting `rm -rf` and being blocked by a hook -- illustrates why this matters.

- **Ignoring context window growth in long-running agents**: Agents that iterate extensively accumulate assistant messages and tool call records that fill the context window. Without compaction or agent decomposition, performance degrades as the window fills. Monitor context usage and apply long-horizon strategies proactively, not reactively.

- **Rubber-stamping AI output to maintain velocity**: As CircleCI's Schmitt warns ([#018]), when review cannot keep pace with generation, teams are tempted to approve AI-generated code without adequate review. This trades speed for reliability. The builder/validator pattern and tiered review processes exist precisely to avoid this trap.

- **Treating all codebases with the same supervision level**: A prototype and a payment processing service should not have the same agent autonomy level. Without explicit policy, agent supervision becomes a free-for-all with inconsistent quality. Define policies per risk tier.

- **Building monolithic skills instead of composable ones**: As IndyDevDan notes in [#015], prefer skill composition (sequential chaining, parallel activation) over building monolithic skills that try to do everything. Smaller, focused skills are easier to test, reuse, and combine.

## Hands-On Exercises

1. **Build a builder/validator workflow**: Create a task that implements a simple feature (e.g., add a new API endpoint). Define a builder agent with full tool access and a validator agent with read-only access. Execute the task and observe how the validator reviews the builder's work. Evaluate whether the validator catches intentionally introduced issues.

2. **Design a dependency DAG**: Take a moderately complex feature (3-5 components) and decompose it into tasks with explicit dependencies. Draw the DAG on paper first, then implement it using TaskCreate with dependency relationships. Run the task system and verify that tasks execute in the correct order.

3. **Implement a safety hook**: Write a PreToolUse hook that blocks a specific dangerous pattern (e.g., writes to production configuration files, destructive shell commands). Test that the hook correctly blocks the operation. Then write a PostToolUse hook that logs all tool calls to a JSON file for auditability.

4. **Practice the autonomous loop**: Set up a simple project with a failing test. Run Claude Code in a loop (manually or scripted) that attempts to make the test pass. Observe how the agent adapts across iterations. Note where context window limits are reached and how a fresh agent picks up the work.

5. **Stress-test context management**: Start a long Claude Code session with an intentionally complex task. Monitor how context usage grows. Apply compaction at different points and observe the effect on response quality. Try agent decomposition for a sub-workflow and compare the result with keeping everything in one context.

6. **Write a meta-prompt**: Create a reusable meta-prompt for a workflow your team repeats (e.g., adding a new microservice, migrating a database schema). The meta-prompt should generate a structured plan with tasks, dependencies, and builder/validator assignments. Test it across two different instances of the workflow to verify consistency.

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [001: Claude Code Task System](../../sources/001-indydevdan-claude-code-task-system.md) | IndyDevDan | Task system, builder/validator, meta-prompts, lifecycle hooks, the "Big Three" framework |
| [008: The Capability Overhang](../../sources/008-nate-b-jones-phase-transition.md) | Nate B Jones | Ralph, capability overhang, power user patterns, parallel agents, agent supervision policy |
| [011: Prompt Engineering is dead](../../sources/011-confluent-developer-context-engineering.md) | Tim Berglund (Confluent) | Six components of context, compaction, memory, agent decomposition, the 60-70% rule |
| [015: I finally CRACKED Claude Agent Skills](../../sources/015-indydevdan-skills-engineering.md) | IndyDevDan | Skill composition patterns, chaining, context budget management |
| [016: The Biggest AI Jump](../../sources/016-nate-b-jones-opus-46-jump.md) | Nate B Jones | Opus 4.6 capability leap, workflow inversion from "AI assists" to "AI leads" |
| [018: The New AI-Driven SDLC](../../sources/018-circleci-ai-sdlc.md) | CircleCI (Jacob Schmitt) | Bottleneck shift from writing to evaluating, SDLC as network, infrastructure as enabler |

## Further Reading

- [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) -- IndyDevDan's companion repository with all 13 hook implementations, meta-prompt examples, builder/validator agent definitions, and the `/plan_w_team` workflow
- [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) -- Real-time monitoring for Claude Code agents through hook event tracking
- [claude-code-damage-control](https://github.com/disler/claude-code-damage-control) -- Safety-focused hooks for preventing destructive agent actions
- [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md) -- Skills system fundamentals that underpin skill-augmented agent teams
- [Module 05: Team Orchestration](../05-team-orchestration/README.md) -- Scaling these patterns to multi-agent teams and organizational workflows
- [Module 06: Strategy & Economics](../06-strategy-and-economics/README.md) -- The SDLC transformation and organizational implications of agentic patterns
