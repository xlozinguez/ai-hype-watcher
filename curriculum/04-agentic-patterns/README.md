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

Agrici Daniel's "Cloudy Ads" skill ([#043](../../sources/043-agrici-daniel-claude-ad-agency.md)) demonstrates a single-agent variant of the builder/validator pattern applied outside software development. When asked to generate a PDF report, the agent self-orchestrates a multi-step workflow: designing an HTML report with charts, writing a Python script for PDF conversion, generating the output, self-reviewing for formatting issues, and fixing problems without human intervention. The agent acts as both builder and reviewer of its own output within the same session. This is less rigorous than the two-agent builder/validator (no tool permission enforcement), but it demonstrates that the review-after-build pattern is valuable even when collapsed into a single agent -- particularly for non-code outputs where the review criteria are visual rather than functional.

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

Damian Galarza ([#099](../../sources/099-damian-galarza-agent-memory-search.md)) provides a detailed technical breakdown of how production agent memory systems actually work, using OpenClaw's implementation as a case study. The key architectural insight is that **no single search approach is sufficient** for agent memory retrieval. Keyword search (grep, BM25) excels at exact matches -- error codes, function names -- but misses semantic relationships. Semantic search (embeddings, vector databases) finds conceptually related content but fails on literal string matching. OpenClaw combines both via **weighted score fusion** (70% vector, 30% keyword), then optionally reranks results using an LLM for nuanced relevance judgment.

The **search-then-get two-tool pattern** is particularly important for context management: `memory_search` returns lightweight previews (file path, line numbers, relevance score, 700-character snippet), and `memory_get` retrieves specific sections by path and line range. This mirrors how humans search -- scan results for relevance, then read only what matters -- and prevents loading entire files into the context window. The pattern keeps token usage efficient and directly supports the 60-70% context headroom principle.

Additional implementation details from Galarza's analysis: chunking with overlap (400-token chunks with 80-token overlap) ensures ideas split across boundaries remain discoverable; embedding caches keyed by provider and model prevent redundant API calls; and a 4x candidate multiplier (requesting 24 candidates when 6 are needed) gives the fusion step more material to work with. Notably, the Claude Code team started with a vector database but found that grep-based agentic search actually performed better and was easier to maintain -- a counter-intuitive finding that reinforces the "start simple" principle.

**Agent decomposition**: Split complex agents into composed sub-agents. If your agent has a complex document-search workflow, that should be its own agent. The parent agent can ask the sub-agent for a concise summary rather than carrying the full search context. As Berglund notes, this mirrors microservice decomposition -- agents naturally evolve from monoliths to composed systems.

These strategies connect directly to Berglund's "60-70% rule": research consistently shows that filling a context window to 100% capacity does not give the best results. Performance peaks at roughly 60-70% of window capacity. Long-horizon strategies exist to maintain that headroom even as work accumulates.

> "More isn't always better. Somewhere in the 60 to 70% of the capacity of the context window is probably where you get your best results." -- Tim Berglund ([#011])

### Concept 7: Ralph and the Power of Simple Loops

One of the most influential agentic patterns emerged not from a research lab but from a bash script. As Nate B Jones documents in [#008], Jeffrey Huntley wrote a bash script called Ralph that runs Claude Code in a loop, using git commits and files as memory between iterations. When the context window fills up, a fresh agent picks up where the last one left off.

The technique is "embarrassingly simple" -- while the AI industry was building elaborate multi-agent frameworks, Huntley discovered that a loop that keeps running until tests pass is more reliable than carefully choreographed agent handoffs. VentureBeat called it "the biggest name in AI right now."

Jo Van Eyck ([#024]) provides a more detailed framework for understanding the Ralph Wiggum loop: it is fundamentally a while loop around a coding agent where the halting condition is deterministic verification -- compilation succeeds, tests pass, linting is clean. The key insight: "We do not need AGI, we do not need super smart models, we just need persistence" ([4:29](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=269)). The agent will confidently report "all done, all tests pass" when the code doesn't even compile. The Ralph loop's value is precisely that it replaces agent self-assessment with actual execution of compilation and test suites.

The Ralph Wiggum loop also connects to Van Eyck's "autonomy slider" concept -- it enables the shift from In-the-Loop (babysitting the agent through each step) to On-the-Loop (fire-and-forget with quality gates). You prepare a package of work, hand it to an agent, and only return when deterministic verification confirms completion. This shift requires trust in the quality gates, not trust in the agent's self-assessment.

Ralph embodies a key principle of power user patterns from [#008]: **accept imperfection and iterate**. The AI will produce broken code, so you make it retry until it fixes it. It never gets tired. This requires abandoning the expectation that AI should get things right the first time.

Anthropic's native Task System can be understood as the productized version of what Ralph demonstrated as a prototype: persistent agent coordination with context isolation across sessions.

### Concept 8: The Bottleneck Shift -- From Writing to Evaluating

As Jacob Schmitt from CircleCI argues in [#018], when AI accelerates code generation by an order of magnitude, the constraint moves from writing code to evaluating it. Decision-making -- not implementation -- becomes the bottleneck. This has cascading implications for agentic patterns:

- **Infrastructure must validate at machine speed**: If your CI/CD pipeline takes 30 minutes to validate a change, it does not matter that AI generated the change in 30 seconds. Fast builds, continuous testing, and real-time failure signals are prerequisites for realizing AI's productivity gains.
- **Code review processes need redesign**: Review processes designed for human-paced output cannot absorb AI-paced input. Tiered review -- automated validation for routine changes, human review reserved for architectural and high-risk decisions -- becomes essential.
- **Engineering roles shift**: Senior engineers move from implementation toward architecture, review, and judgment. As Schmitt puts it: "What it means to be a senior engineer fundamentally changes when machines handle execution."

Multiple sources converge on this point. Nate B Jones ([#008]) cites Maggie Appleton: "When agents write the code, design becomes the bottleneck." The capability overhang is not about whether AI can do the work -- it can. The overhang is in the human systems (review, validation, deployment) that have not yet adapted to AI-paced output.

> "When AI can generate ten solutions quickly, the valuable skill becomes choosing the right one for your context." -- Jacob Schmitt ([#018])

### Concept 9: Persistent Task Management with Beats

Jo Van Eyck ([#024]) introduces Beats -- a persistent memory and task management system for coding agents, created by Steve Yaggi. Think of it as "a Trello board for your coding agents." Plans are broken into subtasks with identified dependencies and blocking relationships, persisted outside the context window as a git repository with JSON files.

The architecture solves a fundamental problem: when task state lives in the context window, it degrades as sessions extend (what Van Eyck calls "context rot"). By externalizing task state, Beats enables agents to look at the next task, update completion state, and reason about parallel versus sequential work without holding the entire plan in working memory.

Key properties of Beats:

- **Git-backed persistence**: Task state is stored as JSON files in a git repository, completely outside the agent's context window
- **Dependency-aware sequencing**: Agents can query which tasks are ready to work on based on completion state and blocking relationships
- **Cross-session continuity**: When a new agent picks up work, it reads the current state from disk rather than reconstructing it from conversation history
- **Parallel execution support**: Multiple agents can work on independent tasks simultaneously, coordinating through the shared task repository

Claude Code's improved plan mode (introduced in late 2025/early 2026) follows the same pattern -- a series of JSON files on disk that persist task state outside the context window. As Van Eyck notes, this is "very Beats-like." The principle extends in Module 05's Gas Town pattern, which adds fleet orchestration on top of Beats-style persistent task management.

The connection to the Ralph Wiggum loop (Concept 7) is direct: Beats provides the persistent state that enables long-running autonomous loops to survive context window resets. Each agent iteration reads the current task state, makes progress, updates the state, and terminates. The next iteration picks up seamlessly.

### Concept 10: Continuous Agentic Pressure -- Agents as Always-On Infrastructure

Eddie Aftandilian ([#069](../../sources/069-eddie-aftandilian-agentic-workflows.md)) describes a maturity shift from AI-as-tool to AI-as-infrastructure. GitHub deployed over 100 specialized agentic workflows on their own repository, and the key finding was that the real leverage wasn't in automating discrete tasks (issue triage, routine fixes) but in applying **continuous pressure** to areas of the codebase that are never really "done": code quality, test coverage, performance, dependency usage.

The operational difference is fundamental: improvement stops being event-driven. It doesn't depend on someone prioritizing a tech-debt ticket or deciding to run a cleanup sprint. It just keeps happening in the background, with humans in the loop for review. Agents regularly propose structural refactors, analyze dependency patterns, open PRs for test coverage gaps, and keep documentation synchronized with code changes.

This extends the agentic patterns in this module from session-scoped to repository-scoped. The Ralph loop (Concept 7) runs until tests pass and then stops. Continuous agentic pressure never stops -- it's a permanent layer of the development infrastructure. GitHub's approach uses many small, specialized workflows rather than one monolithic agent, with categories including:

- **Analysis agents**: Read-only monitoring of metrics, health, and patterns
- **Improvement agents**: Proactively propose changes via PRs
- **Meta agents**: Monitor and improve other workflows' performance
- **Documentation agents**: Keep docs synchronized with code changes

The security implication is significant: always-on agents have a larger blast radius than on-demand tools. GitHub enforces read-only permissions by default, sandboxed execution, and sanitized outputs. Start with read-only analysis agents to build trust before granting write access.

> "I think some form of continuous AI is going to become a normal part of how serious software projects operate." -- Eddie Aftandilian ([#069])

### Concept 11: Delegation vs. Coordination -- Two Agent Philosophies

Nate B Jones ([#086](../../sources/086-nate-b-jones-codex-vs-claude.md)) identifies a fundamental philosophical divergence in agent architecture, crystallized by the near-simultaneous release of OpenAI's Codex and Anthropic's Claude. Codex bets on **autonomous correctness through delegation** -- hand it off, walk away. Its three-layer architecture (orchestrator, executors, recovery layer) is designed to produce trustworthy output without human review. Claude bets on **integration and coordination** -- plugging into existing tools via MCP, coordinating agent teams with peer-to-peer communication, and extending beyond code into all knowledge work.

Jones offers a three-question decision framework for choosing the right approach: (1) Can you tolerate errors, or is correctness non-negotiable? (2) Does the task live in one environment or span multiple tools? (3) Is the work independent or interdependent? Five separate contract reviews suit delegation in parallel; a product launch where press release, landing page, and email sequence must align suits coordination.

The strategic implication: Codex's bet strengthens if individual agent capability grows fast enough to make coordination unnecessary. Claude's bet strengthens if real work stays fundamentally interdependent and the most valuable problems can never be cleanly decomposed. The MCP network effect compounds for Claude: every new integration makes the system more useful. Most teams will need both capabilities -- the durable meta-skill is rapidly assessing which problems are delegation-shaped and which are coordination-shaped.

> "The gap between the releases might be tiny -- 20 minutes. But the gap around what these companies think agents can do could not be wider." -- Nate B Jones ([#086])

### Concept 12: The Four-Layer Agentic Architecture

IndyDevDan ([#088](../../sources/088-indydevdan-browser-automation-stack.md)) presents "Bowser," a four-layer architecture that demonstrates how to compose agentic capabilities into a reusable stack that solves entire classes of problems rather than individual tasks:

**Layer 1 -- Skills (Capability)**: Foundational tools like a Playwright browser skill or a Claude browser skill. Skills define what an agent can do -- the raw capability.

**Layer 2 -- Subagents (Scale)**: Specialized agents that wrap a skill with a concrete workflow. A Browser QA agent, for example, parses user stories into steps, creates output directories, takes screenshots at each step, and reports pass/fail. Subagents are where specialization and scale begin.

**Layer 3 -- Commands/Prompts (Orchestration)**: Custom slash commands that spawn agent teams, distribute work across parallel subagents, and collect results. This is the meta-prompting layer -- teaching the orchestrator agent how to prompt subagents. Dan introduces the concept of a **Higher-Order Prompt (HOP)** -- a prompt that takes another prompt as a parameter, analogous to a higher-order function. The invariant workflow structure lives in the HOP; the varying task-specific steps are passed as parameters.

**Layer 4 -- Justfiles (Reusability)**: A task runner that provides a single entry point for all agentic workflows with configurable parameters, letting teams and other agents discover and invoke any workflow.

This layered approach is what separates "vibe coders" from "agentic engineers." As Dan puts it: "Agentic engineers know what their agents are doing, and they know it so well, they don't have to look. Vibe coders don't know, and they don't look."

### Concept 13: Skill Design Patterns for Agent Systems

Mark Kashef ([#079](../../sources/079-mark-kashef-claude-skills-guide.md)) synthesizes Anthropic's official 33-page skills guide into five design patterns that directly support agentic workflows:

1. **Sequential workflow** -- Linear steps with rollback on failure (e.g., authentication flow)
2. **Multi-MCP coordination** -- Orchestrating multiple MCPs in phases (e.g., Figma to Drive to Linear to Slack)
3. **Iterative refinement** -- Generate, audit, refine cycles until a quality threshold is met
4. **Conditional branching** -- Same input routed differently based on context
5. **Domain-specific intelligence** -- Enterprise patterns with embedded business rules and compliance checks

Skills operate on a three-level loading model that manages context efficiently: Level 1 (YAML front matter, always loaded, under 1,000 characters), Level 2 (procedural instructions, loaded on match), Level 3 (linked files, loaded on execution). This progressive loading preserves context window space -- critical for agents running multiple skills simultaneously.

The iterative skill creation pattern demonstrated by Jack Roberts ([#083](../../sources/083-jack-roberts-cowork-use-cases.md)) provides a practical on-ramp: start by having the agent perform a task manually through conversation, refine the output through feedback, then enshrine the refined process as a reusable skill for autonomous execution.

Tanmay Deshpande ([#090](../../sources/090-tanmay-deshpande-claude-skill-tradeoffs.md)) demonstrates a compelling application of the **domain-specific intelligence** pattern: a Claude Code skill that encodes a complete architecture trade-off analysis framework into a single invocation. The skill takes a one-paragraph scenario description and produces a comprehensive architecture decision record -- weighted scoring across architecture characteristics, Roger Martin's "What Would Have to Be True" strategic framework, second-order effects analysis (Conway's Law implications, discipline tax), risk profiles, and a phased implementation roadmap. This illustrates how skills can encode multi-step analytical frameworks from management and architecture literature, turning complex decision-making processes into repeatable, documented workflows. As Deshpande puts it: "The most senior person in the room wins and nobody documents why" -- the skill addresses both the documentation gap and the consistency problem in architecture decisions.

### Concept 14: CLI Over MCP for Token Efficiency

The Playwright team ([#030](../../sources/030-playwright-cli-vs-mcp.md)) introduces a file-mediated architecture that dramatically reduces token consumption for browser automation. The same task consumed 114,000 tokens via MCP versus 26,800 tokens via CLI -- a 4.3x reduction. The architectural difference: MCP returns all browser output directly to the LLM's context window, while CLI writes outputs to disk files and lets the agent decide what to read into context.

IndyDevDan ([#088](../../sources/088-indydevdan-browser-automation-stack.md)) reinforces this choice, explicitly recommending CLIs over MCP servers for browser automation. MCP servers consume more tokens and force you into their opinionated workflow; CLIs give you freedom to build your own opinionated layer on top. The practical guidance: build skills on CLIs, then layer your own structure above.

Peter Steinberger, creator of OpenClaw ([#094](../../sources/094-y-combinator-openclaw-viral-agent.md)), provides additional evidence for the CLI-first thesis. He deliberately avoided building MCP support into OpenClaw -- the fastest-growing open-source project in GitHub history -- and instead created **makeporter**, a tool that converts any MCP into a CLI on the fly. His reasoning: CLIs are what humans naturally use, bots are good at Unix, CLIs scale better, and you do not need to restart the agent to add new tools (unlike Claude Code or Codex with MCP). Steinberger views MCP as unnecessary complexity "invented for bots" rather than building on what already works. The fact that OpenClaw reached 160,000+ stars without any MCP support is a strong empirical signal that CLIs are sufficient for even the most ambitious agent projects.

This applies broadly beyond browser automation. Any tool interaction where the agent does not need to reason about every piece of output benefits from the file-mediated pattern. Write output to disk, read selectively into context -- a lazy-loading pattern that preserves context budget for decisions that actually require intelligence.

### Concept 15: Git Worktrees as Agent Infrastructure

Joshua Morony ([#027](../../sources/027-joshua-morony-git-worktree.md)) makes the case that `git worktree` has become essential infrastructure for agentic coding. When AI agents execute multi-phase tasks autonomously for 15-60 minutes, they occupy the filesystem. The developer cannot safely work in the same codebase while agents make edits on the same branch.

Worktrees solve this by creating separate filesystem checkouts that share the same git history. Each agent gets its own working directory, completely isolated from others. Morony integrates worktree creation directly into his agentic pipeline: each new work track automatically creates a dedicated worktree and branch, isolating agent work from the developer's main working directory.

Matt Pocock ([#137](../../sources/137-matt-pocock-worktree-workflow.md)) takes this further with Claude Code's native `claude --worktree` command, which automatically creates a worktree at `.claude/worktrees/` with a randomly generated name. The agent's lifecycle is scoped to the worktree -- on exit, the user chooses to keep or remove it. Pocock identifies a significant gotcha: worktrees branch from the current branch (typically main), so agents may accidentally push commits to main unless explicitly told to push to a named branch. His recommendation: use worktrees for every Claude session, always push to a named branch, and protect your main branch. Subagents also support worktrees, enabling orchestrated parallel workflows where each subagent owns its own branch and produces a PR back to main. As Pocock puts it: "I'm not sure why you wouldn't want to use git work trees like every single time you use Claude."

See also: [Module 05: Team Orchestration](../05-team-orchestration/README.md) for expanded coverage of worktrees in multi-agent setups.

### Concept 16: WebMCP -- Structured Agent-Web Interaction

Sam Witteveen ([#046](../../sources/046-sam-witteveen-webmcp.md)) breaks down WebMCP, a new standard jointly developed by Google and Microsoft that replaces the two fundamentally inefficient methods agents currently use to interact with websites: screenshot-based interaction (consuming thousands of tokens per image) and DOM/HTML parsing (translating raw markup into actionable information). WebMCP allows websites to expose structured tools directly to AI agents through the browser, turning each web page into what is effectively an MCP server.

The architecture rests on three pillars: **Context** (data agents need, including content not currently visible), **Capabilities** (actions agents can take on the user's behalf), and **Coordination** (handoff between user and agent when ambiguity arises). Two complementary APIs are provided: a **Declarative API** that annotates existing HTML forms (making well-structured forms approximately 80% agent-ready with minimal work) and an **Imperative API** for complex JavaScript-driven interactions.

For agent builders, WebMCP replaces what could be dozens of screenshot-and-click interactions with a single structured tool call, dramatically reducing token costs and improving reliability. This is available now behind a flag in Chrome with broader rollout expected in early-to-mid 2026.

### Concept 17: The Generate-Verify-Revise Pattern

Google DeepMind's Althia research agent ([#060](../../sources/060-prompt-engineering-100x-breakthrough.md)) formalizes a three-part agentic loop that outperforms raw model inference at every compute scale:

1. **Generator**: Takes a research task and proposes a candidate solution
2. **Verifier**: A separate natural-language mechanism that probes the logic for gaps and hallucinations (not surface-level plausibility checks)
3. **Reviser**: Patches minor issues or triggers a complete restart back to the generator if critically flawed

Althia achieved 91.9% on Advanced Proof Bench (previous record: 65.7%), and on the 29 of 30 problems where it returned a solution, conditional accuracy was 98.3%. Two features distinguish it from simpler loops: it uses web search to ground citations in real literature (addressing hallucinated citations), and it can explicitly admit when it cannot solve a problem rather than hallucinating a confident answer.

The meta-lesson reinforced across the release: **the orchestration layer around the model is where the real capability gains come from**. Poetic's agentic harness on Gemini 3 Pro beat earlier Deep Think at lower cost. Tool selection alone can yield 5-8% improvements -- gains not typically achievable with a model generation upgrade. This validates investing in harness design (generate-verify-revise loops, tool access, orchestration logic) rather than waiting for the next model release.

### Concept 18: Deterministic Scripts + Agentic Prompts as Architectural Pattern

IndyDevDan ([#064](../../sources/064-indydevdan-agentic-prompt.md)) introduces a pattern applicable beyond codebase setup: combining deterministic code execution with agentic intelligence. The pattern structure is:

1. Run deterministic steps first (scripts with predictable execution)
2. Log everything from the deterministic execution
3. Let an agentic prompt read the logs, validate results, and handle exceptions
4. For interactive workflows, the agent asks human-in-the-loop questions for decisions that require judgment

This pattern directly addresses the trust problem in agentic systems. As IndyDevDan frames it: "Agents when combined with code beats either alone." Deterministic hooks provide the reliability floor; agentic prompts provide the intelligence ceiling. The combination is strictly better than either approach in isolation.

The encoding of common failure modes into the prompt creates a positive feedback loop: every time a new failure is discovered, it gets encoded as a problem/solution pair, making the agent progressively better at handling issues without human intervention. This turns prompts into evolving knowledge bases -- "living documents that execute."

### Concept 19: REPL + Recursion as a Reasoning Primitive

Brainqub3's analysis of the Recursive Language Models paper ([#048](../../sources/048-brainqub3-recursive-language-models.md)) introduces a deceptively simple agentic pattern for reasoning over complex, high-context documents. Instead of placing documents in the context window, the system assigns them to variables in a Python REPL. The model then operates through four primitives: **Read** (inspect the data object), **Evaluate** (run programmatic functions), **Print** (return results), and **Loop** (continue until solved). A recursive layer allows the orchestrating model to hand off sub-tasks to smaller models that focus on specific portions of the data.

This pattern is particularly powerful for documents that are dependency graphs rather than linear text -- legal contracts, codebases, and policy documents with dense internal cross-references. Prior approaches (context stuffing, summarization, and RAG) break down when task complexity is high. The REPL + recursion approach enables intelligent search over the document graph rather than brute-force context consumption.

The practical guidance: match the approach to the complexity. RLMs shine when tasks involve both long context and high complexity. For short context or simple retrieval, a direct LLM call often outperforms the overhead. Implement guardrails for recursion -- the paper limits recursion to one layer deep and uses synchronous workflows to prevent runaway costs.

### Concept 20: Scaffolding as Temporary Tech Debt -- Build for the Future Model

Boris Cherny, Claude Code's creator ([#103](../../sources/103-y-combinator-boris-cherny-claude-code.md)), articulates a core product philosophy with direct implications for agentic pattern design: **do not optimize for current model capabilities -- build for the model six months from now**. All product scaffolding -- code written to compensate for model limitations -- provides 10-20% performance gains but gets "wiped out with the next model." The Bitter Lesson (Sutton) hangs framed on the Claude Code team's wall: never bet against the model.

This principle extends to agentic patterns. CLAUDE.md itself is scaffolding; Cherny recommends deleting it and starting fresh with each model upgrade, adding back instructions only when the model demonstrably goes off track. Anthropic's own CLAUDE.md is only two lines long. Plan mode -- one of Claude Code's most used features -- "all it does is it adds one sentence to the prompt that's like please don't code." The simpler the scaffolding, the more durable it is across model generations.

The practical implication for agentic engineers: invest in patterns that leverage improving model capabilities (task decomposition, deterministic verification, context isolation) rather than patterns that compensate for model weaknesses (elaborate prompt engineering, excessive guardrails). The former compound in value as models improve; the latter become unnecessary overhead.

> "There is no part of Claude Code that was around six months ago. It's just constantly rewritten." -- Boris Cherny ([#103])

### Concept 21: The Five Levels of Agentic Maturity

Nate B Jones ([#108](../../sources/108-nate-b-jones-five-levels-ai-coding.md)) presents Dan Shapiro's five-level framework for AI coding maturity, which maps directly onto the agentic patterns in this module:

- **Level 0 -- Spicy Autocomplete**: AI fills in code suggestions. No agentic behavior.
- **Level 1 -- Coding Intern**: AI handles isolated tasks with close supervision.
- **Level 2 -- Junior Developer**: AI implements features with moderate oversight. Most self-described "AI-native" developers plateau here.
- **Level 3 -- Developer as Manager**: The developer directs agents rather than writing code. This requires the builder/validator pattern (Concept 3), task systems (Concept 2), and lifecycle hooks (Concept 5).
- **Level 4 -- Developer as Product Manager**: The bottleneck shifts entirely to specification quality. The patterns from this module become infrastructure that runs without direct supervision.
- **Level 5 -- Dark Factory**: No human-written or human-reviewed code. StrongDM operates at this level with three engineers shipping production software, using external "scenarios" as holdout sets and digital twin environments for validation.

The J-curve insight is critical: when AI tools are bolted onto existing workflows without redesigning those workflows, productivity *dips* before it rises. The METR study measured a 19% slowdown for experienced developers. Organizations seeing 25-30%+ gains are the ones that redesigned end-to-end -- which means adopting the patterns in this module, not just the tools.

> "The bottleneck has moved from implementation speed to spec quality. And spec quality is a function of how deeply you understand the system, your customer, and your problem." -- Nate B Jones ([#108])

### Concept 22: Skills as Workflow Automation in the Human-in-the-Loop Sweet Spot

Ben AI ([#105](../../sources/105-ben-ai-cowork-guide.md)) identifies a gap that skills fill between fully automated pipelines and ad-hoc LLM conversations. Many day-to-day tasks are too context-dependent and iterative for rigid automation (n8n, Make.com workflows) but too repetitive for one-off conversations. Skills encode the process while keeping the human in the loop for decisions -- choosing from suggestions, approving steps, iterating on outputs.

The practical workflow: walk through a task manually with Claude once, refine through feedback, then save it as a repeatable skill. Unlike projects or custom GPTs where context is locked to one configuration, multiple skills can be invoked within a single context window, enabling complex multi-step workflows. This extends the skill composition patterns from IndyDevDan ([#015]) into non-developer workflows -- content creation, ad copy, newsletters, and operational tasks.

The key differentiator from the four-layer stack (Concept 12): Concept 12 targets developers building reusable agentic infrastructure. The human-in-the-loop skill pattern targets anyone who does repeatable knowledge work and can describe their process in plain language.

### Concept 23: The Heartbeat Pattern for Persistent Autonomous Agents

Stephen G. Pope ([#142](../../sources/142-stephen-pope-free-openclaw.md)) demonstrates "Popebot," an open-source agent framework that introduces the **heartbeat pattern** -- a configurable cron job that runs agent instructions on a regular interval (e.g., every 10-30 minutes). This enables persistent autonomous operation for tasks like email checking, research monitoring, API polling, or self-improvement reviews without requiring a continuously running agent session.

The architectural innovation is using **GitHub as both version control and orchestration layer**. All agent modifications are tracked as git commits, changes can require human approval via pull requests, and the agent's "swarm" of jobs runs as GitHub Actions workflows with built-in logging and auditability. Path-based auto-merge rules let operators control which changes the agent can make autonomously versus which require review. This provides a transparent, auditable alternative to opaque agent execution -- as Pope notes: "We're not just setting up an agent that's able to modify itself with no transparency."

The zero-cost stack (Ollama for local inference, Docker for sandboxing, GitHub Actions for orchestration with 2,000 free hours) makes the pattern accessible without API fees or dedicated hardware. This extends the Ralph Wiggum loop (Concept 7) from "run until tests pass" to "run continuously on a schedule," bridging the gap between session-scoped agents and the always-on infrastructure described by Aftandilian (Concept 10).

### Concept 24: AI-Friendly Codebase Architecture -- Deep Modules as Agent Infrastructure

Matt Pocock ([#164](../../sources/164-matt-pocock-codebase-ai-ready.md)) argues that codebase design is the single biggest influence on AI coding output -- more than prompts, more than CLAUDE.md files. The core insight: AI agents have no memory of your codebase. Every session is like onboarding a new developer. This reframes codebase quality as an onboarding problem.

Drawing from John Ousterhout's "A Philosophy of Software Design," Pocock advocates for **deep modules** -- large chunks of implementation behind simple interfaces. When each module lives in its own folder with a clear public API, agents can progressively discover the codebase: read the interface first, understand what a module does, and only dive into implementation when needed. Shallow, highly interconnected modules force agents to load excessive context just to understand relationships.

The **graybox module** pattern extends this: developers design interfaces and write tests that lock down behavior, while AI manages internal implementation. As long as tests pass, the internals are delegated. This creates a natural seam between human judgment (interface design, acceptance criteria) and AI execution (implementation), directly supporting the builder/validator pattern (Concept 3) at the codebase architecture level.

This connects to the broader principle that infrastructure investment in AI-readiness compounds over time. As Pocock puts it: "We need to stop thinking about AI as this superpowered developer and understand that it's got some weird limitations. It's a new starter in your codebase."

### Concept 25: The Always-On Competing Agent Pattern

Mitchell Hashimoto ([#165](../../sources/165-pragmatic-engineer-hashimoto-ai-coding.md)), creator of Terraform and Ghostty, describes a workflow principle that extends the continuous agentic pressure concept (Concept 10) to individual developer practice: **always have an agent running**. If you are coding, an agent is planning. If an agent is coding, you are reviewing. This creates a continuous human-AI parallel workflow where neither party is idle.

For harder tasks, Hashimoto runs two agents in competition -- Claude and Codex on the same problem -- then compares outputs. He caps at two competing agents because cleanup overhead becomes counterproductive beyond that point. This "competitive agent" pattern provides a lightweight alternative to full adversarial verification (Pattern 8) for individual practitioners.

Hashimoto's **effort-for-effort review philosophy** also provides a practical framework for calibrating agent output review: match review intensity to stakes. For production systems (Ghostty), review everything. For throwaway projects (a family wedding website), ship if it renders correctly. This nuances the anti-rubber-stamping pitfall -- the goal is not universal deep review but context-appropriate review.

### Concept 26: The Instruction Budget and Deterministic Feedback Loops

Matt Pocock ([#157](../../sources/157-matt-pocock-hooks-cli-enforcement.md)) crystallizes a principle implicit in earlier hook discussions (Concept 5): CLAUDE.md instructions are probabilistic -- they consume context tokens and only reduce the probability of unwanted behavior. Hooks are deterministic -- they block or transform behavior with zero context cost. This distinction has a quantitative dimension: LLMs have an effective instruction budget of roughly 500 instructions before compliance degrades. Every irrelevant instruction in CLAUDE.md competes for this budget.

The practical workflow: identify CLAUDE.md rules that enforce deterministic behavior (CLI preferences, command blockers, file access restrictions), convert them into pre-tool-use hooks, and remove them from CLAUDE.md to free instruction budget for complex reasoning guidance. DIY Smart Code ([#154](../../sources/154-diy-smart-code-claude-code-features.md)) provides a complementary five-feature decision matrix for where to put configuration: CLAUDE.md for always-on rules, skills for on-demand expertise, subagents for isolated context, hooks for event-driven automation, and MCP for external tools.

Ben AI ([#158](../../sources/158-ben-ai-skill-engineering.md)) extends the skill design patterns (Concept 13) with a structured engineering framework: define triggers, set objectives, specify tool/MCP usage, lay out step-by-step processes with human-in-the-loop checkpoints, add rules for edge cases, and enable progressive self-improvement. The most significant addition is **self-improving skills** -- instructing skills to save approved outputs as examples and update rules based on user corrections, creating a positive feedback loop that makes skills progressively better with use.

### Concept 27: The Do-Make-Know Framework for Progressive Agent Autonomy

Dylan Davis ([#177](../../sources/177-dylan-davis-claude-cowork-system.md)) presents a three-level framework for moving from ad-hoc AI assistance to fully autonomous, memory-enhanced workflows:

- **Do** (single task execution): Give the agent a single task (rename files, format a document). This is the entry point.
- **Make** (multi-system orchestration): Drop a single input (e.g., a meeting transcript) and have the AI orchestrate across multiple systems (Gmail, calendar, CRM) to produce finished deliverables. This level uses sub-agents for parallelization.
- **Know** (compounding memory): Add a persistent memory file that accumulates insights across sessions -- client preferences, recurring themes, key decisions -- transforming the AI from a disposable tool into a reusable asset that compounds in value.

Two operational patterns from Davis are particularly useful for long-running agents. First, **changelog files**: have the agent log every action to a changelog.txt so it can resume correctly after context compaction without redoing work. This is a lightweight alternative to the search-then-get pattern (Concept 6) for session-scoped work. Second, **append-only memory**: never remove previous entries from the memory file; structure entries with communication preferences, themes, and decisions so the agent can pick up recurring engagement context.

The framework connects directly to the long-horizon strategies in Concept 6: the Do level operates within a single context window, Make uses sub-agent decomposition for parallelism, and Know implements the memory pattern with markdown files -- validating the simplicity principle from Galarza's analysis ([#099], [#182]).

### Concept 28: Sniper Agents vs. Generalist Agents -- Context Budget as Design Constraint

Agentic Lab ([#179](../../sources/179-agentic-lab-openclaw-architecture.md)) quantifies the context rot problem in generalist agent architectures and argues for purpose-built alternatives. Using OpenClaw as a case study, Roman demonstrates that a generalist agent starts with approximately 7,000 tokens of fixed overhead on day one -- impressively low. But after a month of daily use, memory files grow, skills accumulate, and session summaries pile up, reaching approximately 45,000 tokens of fixed overhead. After six months, the number can reach tens of thousands more. Research on context rot shows this causes 40-90% performance degradation and approximately $0.52 extra per message.

By contrast, a single-purpose "sniper agent" -- an email agent, for example -- needs only approximately 1,400 tokens of fixed context. This is a 30x reduction in overhead, with proportional improvements in performance and cost.

The architectural insight: every agent harness can be understood through four questions: (1) What triggers the agent? (heartbeats, cron jobs, webhooks), (2) What gets injected into context on every turn? (system prompt, conversation history, tool schemas), (3) What tools can the agent call? (memory retrieval, computer control, skills/plugins), and (4) What does the agent output or write? (messages, files, memory updates). This framework applies to designing any custom agent.

The prescription aligns with Berglund's 60-70% rule (Concept 6): build purpose-specific agents with minimal context overhead rather than generalists that accumulate context rot. The four-category framework provides a practical design checklist for any agent architecture.

### Concept 29: Agent Management as Human Management

Mihail Eric ([#178](../../sources/178-eo-multi-agent-orchestration.md)), who leads AI at a startup and teaches Stanford's first AI-across-the-SDLC course, argues that orchestrating multiple agents is fundamentally a management skill -- the same context-switching and task isolation abilities that make good human managers translate directly to multi-agent coordination. People who have managed human developers tend to be the best at managing agent teams because they already have these skills.

Eric provides a grounded counterpoint to the "run 10 agents at once" hype, advocating for **incremental agent addition**: start with one agent doing a complex task well, then add a second agent on an isolated change, then a third on another independent task. Only scale up when you are confident each agent is performing reliably. The key is ensuring tasks are truly independent -- task B should not depend on task A.

The error compounding risk is significant: "Agents can compound errors very quickly. If an agent has one misunderstanding in code, and then it sees that misunderstanding it created in step 1, it can double down and create another error in step 2." This reinforces the case for agent-friendly codebases (Concept 24) -- comprehensive test coverage, consistent design patterns, accurate documentation, and proper linting are prerequisites, not optional extras.

### Concept 30: Markdown-Based Agent Memory -- Three Questions That Define Any Memory System

Damian Galarza ([#182](../../sources/182-damian-galarza-agent-memory.md)) breaks down how AI agents achieve persistent memory despite being inherently stateless, building on his earlier memory search analysis ([#099]). The architecture has two layers: session memory (conversation history, subject to compaction) and long-term memory (what survives between sessions).

Drawing on Google's November 2025 white paper on context engineering, Galarza categorizes memory into three types: **episodic** (what happened in past interactions), **semantic** (facts and user preferences), and **procedural** (workflows and learned routines). An effective memory system must filter what is worth remembering, consolidate duplicate or contradictory entries, and overwrite outdated information.

Using OpenClaw as a case study, Galarza shows the entire memory system is built on markdown files rather than vector databases -- validating the "start simple" principle from Concept 6. Four mechanisms trigger reads and writes at the right moments: bootstrap loading at session start, pre-compaction flush (a write-ahead log pattern borrowed from database design that converts a destructive operation into a checkpoint), session snapshot on reset, and direct user instruction.

The practical guidance is concise: "You don't need a complex setup to give an agent memory. You just need clear instructions to three questions. What's worth remembering? Where does it go? And when does it get written?" Claude Code's own memory feature uses the same markdown-based approach.

### Concept 31: The Agentic Trap -- Over-Optimization as a Failure Mode

Peter Steinberger ([#162](../../sources/162-openai-openclaw-steinberger.md)) identifies a common failure mode he calls "the agentic trap": developers get stuck between their first touchpoint with AI tools and becoming truly productive because they obsessively optimize their setup rather than building. The optimization feels productive but is not.

Steinberger's counter-approach is radically simple: 10 parallel git checkouts (not even worktrees), conversational prompting, and the habit of always asking "do you have any questions?" to surface the model's assumptions before it starts building. He ships code he does not read because most code is "boring" data transformation, focusing his attention on architecture and performance-critical paths.

The emergent problem-solving capability of agents is illustrated by Steinberger's voice message story: OpenClaw received a WhatsApp voice message it was never designed to handle. The model identified the file as Opus codec by inspecting the file header, used FFmpeg to convert it, found an OpenAI API key in the environment, used cURL to call the Whisper API for transcription, and replied with the text. This demonstrates that agents with tool access exhibit problem-solving behavior that transcends their explicit programming -- reinforcing the generate-verify-revise principle (Concept 17) at a micro level.

Steinberger also reframes open-source contributions as "prompt requests" -- the intent behind a PR matters more than the code itself. This aligns with the broader shift from evaluating code to evaluating specifications (Concept 8).

> "The agentic trap... a lot of people get stuck in there trying to super optimize their setup. It doesn't really make you more productive, but it feels like you're more productive." -- Peter Steinberger ([#162])

### Concept 32: Scheduled Tasks and Plugin Bundles as Agent Capabilities

Eliot Prince ([#183](../../sources/183-eliot-prince-cowork-scheduled-tasks.md)) demonstrates scheduled tasks in Claude Cowork -- automated prompts that run on a configurable schedule (hourly, daily, weekly) as long as the computer is on. This bridges the gap between session-scoped agents and the heartbeat pattern (Concept 23): scheduled tasks are simpler to configure but require the machine to remain active, while the heartbeat pattern via GitHub Actions runs independently of the user's hardware.

Plugins bundle multiple skills and connectors into department-like AI employees (finance, marketing, customer support), extending the skill composition patterns from Concept 13. Rather than configuring individual skills, plugins package related tools into functional roles -- a higher-level abstraction that simplifies adoption for non-technical users while maintaining the composability principles of the four-layer stack (Concept 12).

### Concept 33: Agent Harness Customization -- Opinionated vs. Minimal Design

IndyDevDan ([#146](../../sources/146-indydevdan-pi-coding-agent.md)) presents Pi, an open-source agentic coding tool, as a case study in the fundamental design tension between opinionated and minimal agent harnesses. Claude Code ships with a 10,000-token system prompt, five safety modes, and polished defaults. Pi takes the opposite approach: a 200-token system prompt, no safety modes, and just four tools (read, write, edit, bash). The philosophy is "if I don't need it, it won't be built."

The key insight is that **the agent harness matters as much as the model**. Dan demonstrates a "till done" extension that forces the agent to create and complete task items before executing work, blocks tool calls until a task list exists, and requires engineer approval to clear tasks. This deterministic workflow enforcement extracts reliable results even from cheaper models like Haiku -- compensating for model limitations through harness design rather than model selection.

Pi's extension system enables **stackable customization**: composable TypeScript files that hook into the agent lifecycle for custom UI, tool counters, sub-agent support, and task management. This composable approach -- stacking capabilities in isolation, then combining for specific workflows -- reinforces the principle from Concept 12 (the four-layer stack) that agentic engineering is about building reusable, composable layers rather than monolithic tools.

The practical recommendation is hedging: use Claude Code (80% of the time) for its excellent defaults and enterprise features, but maintain fluency with open-source alternatives like Pi for deep customization, model flexibility, and experimental workflows. As Dan frames the progression: base agent, improved agent, context engineering, customized agents, orchestrator agent -- each level builds on the last. "Knowing what your agent is doing is engineering. Not knowing is vibe coding."

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
- **How it works**: Skills load on demand per-agent based on the task context (see [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md)). A front-end builder agent automatically activates design and accessibility skills. A backend builder activates database and API skills. Each agent gets the specialized knowledge it needs without bloating other agents' contexts. Mark Kashef's five design patterns ([#079]) provide a taxonomy for structuring these skills: sequential workflow, multi-MCP coordination, iterative refinement, conditional branching, and domain-specific intelligence.
- **Example**: IndyDevDan ([#015]) describes skill composition patterns that emerge naturally from auto-activation: sequential chaining (one skill's output feeds another's input), parallel activation (multiple skills for different aspects of the same prompt), and nested composition (a higher-level skill orchestrating lower-level ones).
- **Source**: [#015], [#001], [#079]

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

### Pattern 8: Adversarial Verification Agents

- **When to use**: When you need higher confidence in research, analysis, or implementation quality and cannot rely solely on deterministic testing.
- **How it works**: Spawn adversarial agent pairs where one agent performs research or implementation and a second agent actively tries to find flaws, challenge assumptions, or identify gaps. Unlike the builder/validator pattern (which is sequential), adversarial agents can run concurrently. This is particularly effective for research tasks where confirmation bias is a risk.
- **Example**: AI LABS ([#021]) demonstrates spawning adversarial agent pairs for research validation. After the primary agent completes research, an adversarial agent receives the same prompt with instructions to challenge conclusions and identify missing information. AI LABS also uses "predictive failure analysis" as a post-testing quality gate -- after tests pass, a separate agent analyzes the code for potential failure modes that tests might not cover.
- **Source**: [#021]

### Pattern 9: The Four-Layer Stack Pattern

- **When to use**: When you need to solve a class of problems (e.g., browser automation, UI testing, content generation) repeatedly across projects.
- **How it works**: Build four composable layers: Skills (raw capability), Subagents (specialized workflow wrapping the skill), Commands (orchestration via Higher-Order Prompts), and Justfiles (reusable invocation). Each layer adds value without duplicating the one below. The HOP pattern keeps invariant structure in the orchestration layer while varying the task-specific steps.
- **Example**: IndyDevDan's Bowser ([#088]) -- a Playwright browser skill (Layer 1) wrapped by a Browser QA subagent (Layer 2), orchestrated by a `/ui-review` command that distributes user stories across parallel subagents (Layer 3), invocable via `just ui-review` (Layer 4).
- **Source**: [#088]

## Common Pitfalls

- **Relying on automatic task system activation instead of deliberate meta-prompts**: The task system activates automatically for large, complex prompts, but automatic activation lacks the organizational context and standards baked into a well-crafted meta-prompt. Deliberate meta-prompts enforce specific patterns (builder/validator pairs, dependency structures, validation criteria) and produce more consistent results.

- **Spawning sub-agents without dependency awareness**: Ad hoc sub-agent calls without task system coordination lead to race conditions, duplicated work, and agents that overwrite each other's changes. Use the task system's dependency DAG to ensure proper sequencing.

- **Trusting LLM judgment for safety instead of deterministic hooks**: The agent might usually avoid destructive commands, but "usually" is not a safety guarantee. Use PreToolUse hooks to block dangerous operations deterministically. The opening demonstration in IndyDevDan's [#001] video -- Claude Code attempting `rm -rf` and being blocked by a hook -- illustrates why this matters.

- **Ignoring context window growth in long-running agents**: Agents that iterate extensively accumulate assistant messages and tool call records that fill the context window. Without compaction or agent decomposition, performance degrades as the window fills. Monitor context usage and apply long-horizon strategies proactively, not reactively.

- **Rubber-stamping AI output to maintain velocity**: As CircleCI's Schmitt warns ([#018]), when review cannot keep pace with generation, teams are tempted to approve AI-generated code without adequate review. This trades speed for reliability. The builder/validator pattern and tiered review processes exist precisely to avoid this trap.

- **Treating all codebases with the same supervision level**: A prototype and a payment processing service should not have the same agent autonomy level. Without explicit policy, agent supervision becomes a free-for-all with inconsistent quality. Define policies per risk tier.

- **Building monolithic skills instead of composable ones**: As IndyDevDan notes in [#015], prefer skill composition (sequential chaining, parallel activation) over building monolithic skills that try to do everything. Smaller, focused skills are easier to test, reuse, and combine. The four-layer architecture ([#088]) demonstrates how composable skills scale into reusable stacks.

- **Jumping to agent teams when sub-agents suffice**: Simon Scrapes ([#051](../../sources/051-simon-scrapes-claude-code-tips.md)) recommends a clear graduation model: start with single agents, graduate to sub-agents for delegation, then reach for agent teams only when genuine cross-collaboration is required. Agent teams add token cost (~5x) and coordination overhead. The additional complexity is overkill for simple delegation tasks.

- **Running autonomous loops without deterministic halting conditions**: Van Eyck ([#024]) warns that agents will confidently report "all done, all tests pass" when the code doesn't even compile. The Ralph Wiggum loop's value is precisely that it replaces agent self-assessment with deterministic verification (actual compilation, actual test execution). Without this, autonomous loops produce false-positive completion signals and waste compute on work that never had a chance of succeeding.

- **Neglecting the agent security surface**: IBM's zero trust framework for agentic AI ([#057](../../sources/057-ibm-zero-trust-ai-agents.md)) identifies six attack vectors specific to agent architectures: prompt injection, policy/model poisoning, interface interception (including MCP calls), tool/API compromise, credential theft, and privilege escalation. The "assume breach" mindset -- designing every control assuming the agent or its environment is already compromised -- becomes critical when autonomous agents have elevated privileges and can take real-world actions. Key mitigations: never embed credentials in agent code (use just-in-time credential vaults), maintain a vetted tool registry for all MCP tools and APIs, deploy AI firewalls at agent boundaries for input/output inspection, and log everything immutably for post-incident forensics.

- **Expecting AI-generated codebases to remain maintainable at scale**: Tom Delalande ([#073](../../sources/073-tom-delalande-claude-agents-useless.md)) documents how Anthropic's own C compiler project reached a point where Claude could not make changes without breaking existing functionality. AI-generated codebases can exceed the model's own ability to modify them -- a critical concern for long-lived projects that depend on autonomous agent maintenance.

- **Using MCP when CLI would be more efficient**: The Playwright team ([#030]) demonstrated a 4.3x token reduction using CLI over MCP for the same browser automation task. Default to CLI-based tools for coding agents; reserve MCP for custom agentic loops where the standardized protocol matters.

- **Granting agents destructive permissions on external systems**: ThePrimeTime ([#163](../../sources/163-primetime-openclaw-inbox.md)) documents an incident where Meta's head of AI safety had her email inbox bulk-deleted by an agent that could not be interrupted mid-execution. The agent interpreted "clean up my inbox" as authorization for bulk deletion, and repeated "stop" commands were queued rather than processed. The lesson: never give agents unsupervised destructive access to external systems (email, calendars, databases). Prefer reversible operations (archiving, moving) over irreversible ones (deletion), require per-action approval for destructive operations, and ensure you can kill the agent process at the OS level when interrupt commands are being queued.

- **Ignoring codebase architecture as an agent constraint**: Pocock ([#164](../../sources/164-matt-pocock-codebase-ai-ready.md)) argues that codebase design influences AI output more than prompts or agent configuration. Shallow, interconnected modules force agents to load excessive context. Investing in deep modules with simple interfaces, clear directory structures, and comprehensive tests makes the codebase navigable for agents that have no memory of prior sessions.

- **Running too many concurrent agents as a human operator**: The Daily AI Show ([#148](../../sources/148-daily-ai-show-memory-hacks-burnout.md)) surfaces research showing that AI tools intensify work rather than reduce it, and that managing multiple agent instances creates an interrupt-driven workflow that degrades human cognitive quality. Each agent interruption erodes flow and focus. Limit concurrent agent instances to what you can meaningfully oversee rather than maximizing parallelism.

- **Scaling agents before ensuring codebase readiness**: Mihail Eric ([#178](../../sources/178-eo-multi-agent-orchestration.md)) emphasizes that agents can only operate reliably on "explicitly defined contracts of software." Without comprehensive test coverage, consistent design patterns, accurate documentation, and proper linting, agents compound errors -- one misunderstanding in step 1 gets magnified in step 2. Invest in codebase fundamentals before scaling agent count.

- **Building generalist agents when specialists would perform better**: Agentic Lab ([#179](../../sources/179-agentic-lab-openclaw-architecture.md)) quantifies the penalty: a generalist agent with 45,000+ tokens of fixed overhead experiences 40-90% performance degradation compared to a purpose-built agent with 1,400 tokens. Build single-purpose "sniper agents" for specific tasks rather than one agent that does everything poorly.

- **Falling into the agentic trap**: Peter Steinberger ([#162](../../sources/162-openai-openclaw-steinberger.md)) identifies a common failure mode where developers obsessively optimize their AI tooling setup instead of building. The optimization feels productive but is not. The counter-approach: start building with radically simple setups and let complexity emerge from real needs.

## Hands-On Exercises

1. **Build a builder/validator workflow**: Create a task that implements a simple feature (e.g., add a new API endpoint). Define a builder agent with full tool access and a validator agent with read-only access. Execute the task and observe how the validator reviews the builder's work. Evaluate whether the validator catches intentionally introduced issues.

2. **Design a dependency DAG**: Take a moderately complex feature (3-5 components) and decompose it into tasks with explicit dependencies. Draw the DAG on paper first, then implement it using TaskCreate with dependency relationships. Run the task system and verify that tasks execute in the correct order.

3. **Implement a safety hook**: Write a PreToolUse hook that blocks a specific dangerous pattern (e.g., writes to production configuration files, destructive shell commands). Test that the hook correctly blocks the operation. Then write a PostToolUse hook that logs all tool calls to a JSON file for auditability.

4. **Practice the autonomous loop**: Set up a simple project with a failing test. Run Claude Code in a loop (manually or scripted) that attempts to make the test pass. Observe how the agent adapts across iterations. Note where context window limits are reached and how a fresh agent picks up the work.

5. **Stress-test context management**: Start a long Claude Code session with an intentionally complex task. Monitor how context usage grows. Apply compaction at different points and observe the effect on response quality. Try agent decomposition for a sub-workflow and compare the result with keeping everything in one context.

6. **Write a meta-prompt**: Create a reusable meta-prompt for a workflow your team repeats (e.g., adding a new microservice, migrating a database schema). The meta-prompt should generate a structured plan with tasks, dependencies, and builder/validator assignments. Test it across two different instances of the workflow to verify consistency.

7. **Build a four-layer stack**: Following the Bowser pattern ([#088]), create a skill for a repeatable task, wrap it in a subagent with a concrete workflow, write a command that orchestrates parallel subagent execution, and wrap everything in a Justfile entry. Test the full stack end-to-end.

8. **Compare CLI vs MCP token usage**: Run the same browser automation task using both the Playwright CLI and MCP server. Compare token consumption, execution time, and output quality. Use this to calibrate your default tool choice for agent workflows.

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [001: Claude Code Task System](../../sources/001-indydevdan-claude-code-task-system.md) | IndyDevDan | Task system, builder/validator, meta-prompts, lifecycle hooks, the "Big Three" framework |
| [008: The Capability Overhang](../../sources/008-nate-b-jones-phase-transition.md) | Nate B Jones | Ralph, capability overhang, power user patterns, parallel agents, agent supervision policy |
| [011: Prompt Engineering is dead](../../sources/011-confluent-developer-context-engineering.md) | Tim Berglund (Confluent) | Six components of context, compaction, memory, agent decomposition, the 60-70% rule |
| [015: I finally CRACKED Claude Agent Skills](../../sources/015-indydevdan-skills-engineering.md) | IndyDevDan | Skill composition patterns, chaining, context budget management |
| [016: The Biggest AI Jump](../../sources/016-nate-b-jones-opus-46-jump.md) | Nate B Jones | Opus 4.6 capability leap, workflow inversion from "AI assists" to "AI leads" |
| [018: The New AI-Driven SDLC](../../sources/018-circleci-ai-sdlc.md) | CircleCI (Jacob Schmitt) | Bottleneck shift from writing to evaluating, SDLC as network, infrastructure as enabler |
| [020: How & When to Use Claude Code Agent Teams](../../sources/020-simon-scrapes-agent-teams.md) | Simon Scrapes | Context rot, hub-spoke vs mesh topology, complexity heuristic |
| [021: Claude's Best Release Yet + 10 Tricks](../../sources/021-ai-labs-claude-code-tricks.md) | AI LABS | Adversarial agent pairs, predictive failure analysis, hooks for TDD enforcement, user stories for BDD |
| [024: Agentic coding in 2026](../../sources/024-jo-van-eyck-agentic-coding-2026.md) | Jo Van Eyck | Ralph Wiggum loop deep dive, Beats persistent task management, autonomy slider, deterministic verification |
| [026: 10 Claude Code tips](../../sources/026-no-code-mba-claude-code-tips.md) | No Code MBA | Sub-agents as isolated workers, skills vs sub-agents distinction, plan mode for deliberate development |
| [027: Devs can no longer avoid learning Git worktree](../../sources/027-joshua-morony-git-worktree.md) | Joshua Morony | Git worktrees as essential agent infrastructure, file system contention, automated worktree pipelines |
| [030: Playwright CLI vs MCP](../../sources/030-playwright-cli-vs-mcp.md) | Playwright | CLI vs MCP token efficiency (4.3x reduction), file-mediated context control, capability surface trade-offs |
| [043: Claude Code just replaced your ad agency](../../sources/043-agrici-daniel-claude-ad-agency.md) | Agrici Daniel | Autonomous multi-step tool orchestration within a skill, self-review and self-correction pattern |
| [046: The Rise of WebMCP](../../sources/046-sam-witteveen-webmcp.md) | Sam Witteveen | WebMCP structured agent-web interaction, declarative vs imperative APIs |
| [048: Before You Build Another Agent, Understand This MIT Paper](../../sources/048-brainqub3-recursive-language-models.md) | Brainqub3 | REPL + recursion as reasoning primitive, documents as dependency graphs, recursive delegation |
| [051: You're using Claude Code Wrong](../../sources/051-simon-scrapes-claude-code-tips.md) | Simon Scrapes | Agent teams vs sub-agents graduation model, hooks as zero-token checks |
| [057: Securing AI Agents with Zero Trust](../../sources/057-ibm-zero-trust-ai-agents.md) | IBM Technology | Six agent attack vectors, assume-breach for agents, just-in-time credentials, tool registry |
| [060: The 100x AI Breakthrough No One is Talking About](../../sources/060-prompt-engineering-100x-breakthrough.md) | Prompt Engineering | Generate-verify-revise pattern (Althia), agent layer as capability multiplier |
| [062: Every Level of Claude Code Explained](../../sources/062-simon-scrapes-claude-code-levels.md) | Simon Scrapes | GSD planning framework, context rot mitigation, RAWL autonomous loops, seven-level progression |
| [064: One Prompt Every AGENTIC Codebase Should Have](../../sources/064-indydevdan-agentic-prompt.md) | IndyDevDan | Deterministic + agentic pattern, setup hooks, justfile as launchpad, encoding failure modes |
| [068: The Organizational Physics of Multi-Agent Systems](../../sources/068-jeremy-mcentire-multi-agent-physics.md) | Jeremy McEntire | PACT framework, organizational dysfunction is substrate-independent, single agent outperforms swarms |
| [069: How GitHub Uses AI Agents](../../sources/069-eddie-aftandilian-agentic-workflows.md) | Eddie Aftandilian | Continuous agentic pressure, 100+ specialized workflows, agents as always-on infrastructure |
| [073: Claude Code Agents Are Completely Useless](../../sources/073-tom-delalande-claude-agents-useless.md) | Tom Delalande | Gap between demo and reproduction, hidden cost accounting, unmaintainability at scale |
| [079: Anthropic's Full Claude Skills Guide](../../sources/079-mark-kashef-claude-skills-guide.md) | Mark Kashef | Three-level skill loading, five design patterns, YAML front matter best practices, skill testing |
| [083: 5 INSANE Claude CoWork use cases](../../sources/083-jack-roberts-cowork-use-cases.md) | Jack Roberts | Iterative skill creation from manual workflows, multi-connector MCP chaining, browser automation |
| [086: The 12-Point Gap Between Codex and Claude](../../sources/086-nate-b-jones-codex-vs-claude.md) | Nate B Jones | Delegation vs coordination philosophies, three-question decision framework, convergence with echoes |
| [088: My 4-Layer Agentic Browser Automation Stack](../../sources/088-indydevdan-browser-automation-stack.md) | IndyDevDan | Four-layer architecture (Skills/Subagents/Commands/Justfiles), Higher-Order Prompts, CLI over MCP |
| [090: I built Claude Skill for trade off analysis](../../sources/090-tanmay-deshpande-claude-skill-tradeoffs.md) | Tanmay Deshpande | Domain-specific skill encoding, architecture decision automation, multi-step analytical frameworks |
| [094: OpenClaw Creator Explains How He Built The Viral Agent](../../sources/094-y-combinator-openclaw-viral-agent.md) | Y Combinator / Peter Steinberger | CLI-first agent tooling (makeporter), MCP avoidance, emergent agent problem-solving, local-first architecture |
| [099: How AI Agents Search Their Memory](../../sources/099-damian-galarza-agent-memory-search.md) | Damian Galarza | Hybrid memory search (keyword + semantic), weighted score fusion, search-then-get pattern, chunking with overlap |
| [101: I Built a Self-Improving Agent Swarm](../../sources/101-jaymin-west-self-improving-swarm.md) | Jaymin West | Coordinator-lead-builder hierarchy, forced delegation, self-improving agent tooling, git worktree isolation |
| [103: Inside Claude Code With Its Creator Boris Cherny](../../sources/103-y-combinator-boris-cherny-claude-code.md) | Y Combinator / Boris Cherny | Scaffolding as temporary tech debt, build for future model, CLAUDE.md minimalism, plan mode mechanics |
| [105: How to Use Claude Cowork Better Than 99% of People](../../sources/105-ben-ai-cowork-guide.md) | Ben AI | Skills as workflow automation, human-in-the-loop sweet spot, skill chaining in single context |
| [108: The 5 Levels of AI Coding](../../sources/108-nate-b-jones-five-levels-ai-coding.md) | Nate B Jones | Five-level maturity framework, dark factory architecture, J-curve adoption, specification as bottleneck |
| [113: I was an AI skeptic. Then I tried plan mode](../../sources/113-matt-pocock-plan-mode.md) | Matt Pocock | Plan-execute-test-commit loop, plan mode as context loading, concise plans via CLAUDE.md |
| [115: Ship working code while you sleep with the Ralph Wiggum technique](../../sources/115-matt-pocock-ralph-wiggum-technique.md) | Matt Pocock | Ralph as bash loop, PRD as desired state, progress.txt as sprint memory, task sizing |
| [116: LIVE: Chat with AI Coding Wizard Dex Horthy](../../sources/116-matt-pocock-dex-horthy-interview.md) | Matt Pocock / Dex Horthy | Smart zone vs dumb zone, quadratic attention scaling, Ralph as control loop, tracer bullet task sizing |
| [118: No Vibes Allowed: Solving Hard Problems in Complex Codebases](../../sources/118-dex-horthy-no-vibes-complex-codebases.md) | Dex Horthy | Research-Plan-Implement workflow, intentional compaction, dumb zone at 40% context, sub-agents for context control |
| [119: $1,000 a Day in AI Costs. Three Engineers. No Writing Code.](../../sources/119-nate-b-jones-ai-costs-dark-factory.md) | Nate B Jones | Token as unit of computing, Jevons' paradox applied to AI, three developer career tracks, token economics as core competency |
| [120: How to Make the Best of AI Programming Assistants](../../sources/120-dave-farley-ai-programming-assistants.md) | Dave Farley | Nyquist-Shannon theorem applied to AI coding, CI as sampling strategy, production-feedback gap |
| [124: Skills.sh Just Launched. It's Already a Massive Security Risk](../../sources/124-kathy-zant-skills-sh-security.md) | Kathy Zant | Skills marketplace supply-chain risks, prompt injection via alt text, "find skills" meta-danger, WordPress security parallels |
| [126: How I use Claude Code for real engineering](../../sources/126-matt-pocock-claude-code-engineering.md) | Matt Pocock | Plan mode first workflow, multi-phase planning, GitHub issues as external memory, context chaining |
| [127: 50 days with OpenClaw](../../sources/127-velvetshark-openclaw-50-days.md) | VelvetShark | Markdown-first architecture, context separation via channels, multi-model routing, long-term agent adoption reality |
| [128: The $285B Sell-Off Was Just the Beginning](../../sources/128-nate-b-jones-285b-selloff.md) | Nate B Jones | Agent web fork, agent wallets and commerce, agent-readable content, infrastructure primitives convergence |
| [129: One Claude Code Agent? That's Your First Mistake](../../sources/129-leon-van-zyl-multi-agent-claude.md) | Leon van Zyl | Git worktrees for parallel AI development, parallel experimentation workflow, side-by-side model comparison |
| [134: Google DeepMind's Experimental Platform for Humans and LLM Agents](../../sources/134-prolific-deepmind-agent-platform.md) | Prolific / Google DeepMind | Deliberate Lab for human-AI group research, mirror vs mask duality, LLM agent negotiation strategies |
| [135: His Claude Code Workflow Is Insane](../../sources/135-john-kim-claude-code-workflow.md) | John Kim | Boris Cherny's 13-tip workflow, parallel instance management, shared CLAUDE.md, custom sub-agents for post-processing |
| [136: Head of Claude Code: What happens after coding is solved](../../sources/136-lennys-podcast-boris-cherny-after-coding.md) | Lenny's Podcast / Boris Cherny | Coding as solved problem, printing-press analogy, latent demand, bitter lesson applied to AI products |
| [137: I'm using claude --worktree for everything now](../../sources/137-matt-pocock-worktree-workflow.md) | Matt Pocock | Native `claude --worktree` integration, branch naming gotcha, worktree-scoped agent lifecycle, free parallelization |
| [142: I Built a FREE OpenClaw](../../sources/142-stephen-pope-free-openclaw.md) | Stephen G. Pope | Heartbeat pattern, GitHub-as-orchestration, zero-cost agent stack, Docker-based security and scalability |
| [146: The Pi Coding Agent](../../sources/146-indydevdan-pi-coding-agent.md) | IndyDevDan | Opinionated vs minimal agent harness, "till done" pattern, stackable extensions, meta-agents building agents |
| [148: Claude Code Memory Hacks and AI Burnout](../../sources/148-daily-ai-show-memory-hacks-burnout.md) | The Daily AI Show | Context rot from micro-task fixation, AI work intensification research, cognitive overload from multi-agent workflows |
| [149: Stop Using Claude Code Without This Tool](../../sources/149-leon-van-zyl-n8n-claude-code.md) | Leon van Zyl | N8N as MCP server for Claude Code, webhook-based completion notifications, prototype-to-production pipeline |
| [154: Why Most Developers Are Using Claude Code Wrong](../../sources/154-diy-smart-code-claude-code-features.md) | DIY Smart Code | Five-feature decision matrix (CLAUDE.md/skills/subagents/hooks/MCP), context window cost hierarchy |
| [157: How to actually force Claude Code to use the right CLI](../../sources/157-matt-pocock-hooks-cli-enforcement.md) | Matt Pocock | Deterministic vs probabilistic enforcement, instruction budget as finite resource, hook-based workflow |
| [158: How to build Claude Skills Better than 99% of People](../../sources/158-ben-ai-skill-engineering.md) | Ben AI | Skill engineering framework, progressive disclosure, self-improving skills, reference file architecture |
| [160: Lecture 7: Agentic Coding](../../sources/160-missing-semester-agentic-coding.md) | Missing Semester (MIT) | LLM + agent harness architecture, test-driven agent development, context management as core skill |
| [163: OpenClaw Deletes Entire Inbox](../../sources/163-primetime-openclaw-inbox.md) | ThePrimeTime | Agent interrupt problem, destructive permissions on external systems, kill switch requirement |
| [164: Your codebase is NOT ready for AI](../../sources/164-matt-pocock-codebase-ai-ready.md) | Matt Pocock | Deep modules for AI navigation, graybox module pattern, AI as perpetual new starter |
| [165: Mitchell Hashimoto's new way of writing code](../../sources/165-pragmatic-engineer-hashimoto-ai-coding.md) | The Pragmatic Engineer / Mitchell Hashimoto | Always-on agent pattern, competing agents, effort-for-effort review, open source trust crisis from AI |
| [162: Peter Steinberger on Building OpenClaw](../../sources/162-openai-openclaw-steinberger.md) | OpenAI / Peter Steinberger | The agentic trap, prompt requests, emergent agent problem-solving, cross-model workflows |
| [169: Claude Code Just Became a Full IDE](../../sources/169-leon-van-zyl-claude-desktop-app.md) | Leon van Zyl | Desktop app as development environment, parallel local and cloud agents, auto-verify with screenshots |
| [174: Using Obsidian and Claude Code as a Personal Thinking Partner](../../sources/174-greg-isenberg-obsidian-claude-code.md) | Greg Isenberg / Vinh Nguyen | Personal vault as agent context, strict read-only separation, custom slash commands for vault interaction |
| [177: Three-Level Framework for Claude Co-Work Automation](../../sources/177-dylan-davis-claude-cowork-system.md) | Dylan Davis | Do/Make/Know progressive autonomy, changelog files, append-only memory, sub-agent parallelization |
| [178: Multi-Agent Orchestration for AI-Native Engineers](../../sources/178-eo-multi-agent-orchestration.md) | EO / Mihail Eric | Incremental agent addition, agent management as human management, agent-friendly codebases, error compounding |
| [179: OpenClaw Agent Architecture Explained](../../sources/179-agentic-lab-openclaw-architecture.md) | Agentic Lab | Sniper agents vs generalists, four-category agent framework, context rot quantification (40-90%), heartbeat/cron triggers |
| [182: How AI Agent Memory Systems Work](../../sources/182-damian-galarza-agent-memory.md) | Damian Galarza | Three memory types (episodic/semantic/procedural), pre-compaction flush, markdown-based memory, write-ahead log pattern |
| [183: Claude Cowork Scheduled Tasks and Video Editing](../../sources/183-eliot-prince-cowork-scheduled-tasks.md) | Eliot Prince | Scheduled tasks as lightweight automation, plugins as role bundles, Customize tab consolidation |

## Further Reading

- [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) -- IndyDevDan's companion repository with all 13 hook implementations, meta-prompt examples, builder/validator agent definitions, and the `/plan_w_team` workflow
- [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) -- Real-time monitoring for Claude Code agents through hook event tracking
- [claude-code-damage-control](https://github.com/disler/claude-code-damage-control) -- Safety-focused hooks for preventing destructive agent actions
- [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md) -- Skills system fundamentals that underpin skill-augmented agent teams
- [Module 05: Team Orchestration](../05-team-orchestration/README.md) -- Scaling these patterns to multi-agent teams and organizational workflows
- [Module 06: Strategy & Economics](../06-strategy-and-economics/README.md) -- The SDLC transformation and organizational implications of agentic patterns
