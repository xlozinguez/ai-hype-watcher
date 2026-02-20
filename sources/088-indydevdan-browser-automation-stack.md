---
source_id: "088"
title: "My 4-Layer Agentic Browser Automation Stack (Skill, Subagent, Prompt, ????)"
creator: "IndyDevDan"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=efctPj6bjCY"
date: "2026-02-16"
duration: "27:16"
type: "video"
tags: ["skills", "agentic-coding", "multi-agent", "claude-code"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 088: My 4-Layer Agentic Browser Automation Stack (Skill, Subagent, Prompt, ????)

> **Creator**: IndyDevDan | **Platform**: YouTube | **Date**: 2026-02-16 | **Duration**: 27:16

## Summary

IndyDevDan presents "Bowser," a four-layer architecture for agentic browser automation and UI testing built on Claude Code. The layers — Skills (capability), Subagents (scale), Commands/Prompts (orchestration), and Justfiles (reusability) — form a composable stack that solves entire classes of problems rather than individual tasks. The video demonstrates two concrete use cases: automated Amazon shopping via Claude's `--chrome` flag and parallel agentic UI testing via the Playwright CLI.

The core insight is that skills alone are insufficient — the real power comes from layering specialized subagents on top of skills, orchestrating them through custom commands that meta-prompt how subagents should operate, and wrapping everything in a task runner (Just) for repeatable invocation. Dan argues this layered approach is what separates "vibe coders" who don't understand their agents from "agentic engineers" who know their agents so well they don't have to look.

## Key Concepts

### The Four-Layer Architecture

**Layer 1 — Skills (Capability)**: Foundational tools like a Playwright browser skill (headless, parallel sessions, persistent profiles) and a Claude browser skill (using the `--chrome` flag). Skills are the raw capability — they define what an agent can do. **Layer 2 — Subagents (Scale)**: Specialized agents that wrap a skill with a concrete workflow. The Browser QA agent, for example, parses user stories into steps, creates output directories, takes screenshots at each step, and reports pass/fail. Subagents are where you start to specialize and scale. **Layer 3 — Commands/Prompts (Orchestration)**: Custom slash commands like `/ui-review` that spawn agent teams, distribute user stories across parallel subagents, and collect results. This is the meta-prompting layer — teaching the orchestrator agent how to prompt subagents. **Layer 4 — Justfiles (Reusability)**: A task runner (`just`) that provides a single entry point for all agentic workflows with configurable parameters. This lets you, your team, and other agents quickly discover and invoke any workflow.

### CLI Over MCP for Token Efficiency

Dan explicitly recommends using CLIs (like the Playwright CLI) over MCP servers for browser automation. MCP servers consume more tokens and force you into their opinionated workflow. CLIs give you the freedom to build your own opinionated layer on top, with better token efficiency. This is a practical architectural choice: build skills on CLIs, then layer your own structure above.

### Higher-Order Prompts (HOPs)

Dan introduces the concept of a "Higher-Order Prompt" — a prompt that takes another prompt as a parameter, analogous to a higher-order function. The `/automate` command wraps any browser workflow prompt in consistent setup/teardown, output directory creation, and logging. The varying part (the specific steps) goes in the lower-order prompt, while the invariant structure (save to directory, follow safety protocols, report results) stays in the HOP. This pattern enables reusable orchestration without duplicating boilerplate.

### Agentic UI Testing vs. Traditional Testing

Agentic UI testing operates on applications the way a user would — no test configuration, no Jest/Vitest setup, no DOM selectors. You write user stories in plain language with a URL and steps; agents validate against the live page. Each agent takes screenshots along the way, creating a visual audit trail of success and failure. The tradeoff is non-determinism, but Dan argues the best agentic engineers will use a combination of deterministic and agentic testing, leaning toward agentic as agent orchestration matures.

### Don't Outsource Learning

Dan warns against relying entirely on community plugins and pre-built skills. If you can't look at a library, pull it into a skill, scale it with subagents, and orchestrate it with a prompt, you'll be permanently limited. Prompt injections are a real security risk when running other people's prompts. The layered approach teaches you how agents work at every level, which is essential as agent orchestration becomes the primary paradigm.

## Practical Takeaways

- **Solve classes of problems, not individual tasks**: Template your engineering into a repeatable, opinionated solution that can be deployed across codebases
- **Layer your agentics**: Skills provide capability; subagents provide scale; commands provide orchestration; task runners provide reusability. Each layer adds value
- **Prefer CLIs over MCP servers**: CLIs are more token-efficient and give you freedom to build opinionated workflows on top
- **Use Higher-Order Prompts for reusable orchestration**: Put invariant workflow structure in a HOP, pass the varying workflow as a parameter
- **Screenshot every step in agentic testing**: This creates an audit trail that helps debug failures and builds trust in agent-driven QA

## Hands-On Findings

### What Worked
- **Four-layer architecture is real and well-executed**: The code matches the video's claims. Skills (`.claude/skills/`), agents (`.claude/agents/`), commands (`.claude/commands/`), and justfile recipes compose exactly as described. Each layer is independently testable.
- **Agents are genuinely thin**: `playwright-bowser-agent.md` is ~20 lines. `bowser-qa-agent.md` adds structured reporting (~120 lines) but stays focused. No bloat.
- **YAML user stories work as advertised**: `hackernews.yaml` defines stories with name, URL, and workflow in plain language. The `/ui-review` command discovers and fans them out to parallel agents.
- **Higher-Order Prompt pattern is clean**: `hop-automate.md` resolves skill/mode/vision from keyword detection, then delegates to workflow-specific commands. Genuinely reusable.
- **README is accurate**: Directory structure, architecture diagram, comparison table, and usage examples all match the actual codebase. README-vs-reality gap is near zero.
- **Dual-skill approach is well-designed**: Chrome skill (observable, personal browser) vs. Playwright skill (headless, parallel, isolated) serve genuinely different use cases with clear decision criteria documented.

### What Didn't
- **Every justfile recipe uses `--dangerously-skip-permissions`**: This is a non-negotiable requirement for the system to function. Agents need `Bash` access to run `playwright-cli`, and Claude Code's permission model has no way to scope Bash to specific commands. This means agents can execute arbitrary shell commands with zero user confirmation.
- **No tests**: Zero test files in the repository. QA agent validates external sites, but there are no tests for Bowser itself.
- **No CI/CD**: No GitHub Actions, no linting, no type checking, no automated quality gates.
- **No lockfile or dependency manifest**: Dependencies (`playwright-cli`, `just`) are installed globally via npm/brew. No `package.json`, no lockfile, no version pinning.
- **Plain-text credential storage**: `.env` with `ANTHROPIC_API_KEY` in plain text. `.gitignore` covers `.env` (good), but persistent browser profiles store cookies/localStorage without encryption.
- **Playwright sessions persist across contexts**: Named sessions retain cookies and state. A previously visited malicious site could persist hostile content in a session that gets reused.

### Architecture Verification

| Claim (from source note) | Verified? | Evidence |
|---|---|---|
| Four-layer architecture composes as described | Yes | Skills in `.claude/skills/`, agents in `.claude/agents/`, commands in `.claude/commands/`, justfile at root. Each layer delegates down. |
| CLI is more token-efficient than MCP | Partial | Playwright skill uses `Bash` tool only (no MCP schemas in context). Chrome skill uses `mcp__claude_in_chrome__*` tools. Cannot measure token difference without running both on identical tasks. |
| Parallel subagent sessions work without collision | Yes (by design) | Playwright CLI uses `-s=<name>` for named sessions with isolated browser profiles. Each agent gets its own session name. |
| HOP pattern is genuinely reusable | Yes | `hop-automate.md` works with any workflow in `.claude/commands/bowser/`. Adding a new workflow is: drop a `.md` file, done. |
| Agents are thin wrappers | Yes | `playwright-bowser-agent.md`: 20 lines. `claude-bowser-agent.md`: 29 lines. QA agent is larger (~120 lines) due to structured reporting, but still focused. |

### Security Assessment

**Overall: Below baseline.** Falls within the 36% of vulnerable agent skills (source #017).

- **Critical**: `--dangerously-skip-permissions` on every recipe. Agents have unrestricted Bash access. No permission scoping.
- **Critical**: Playwright skill has `allowed-tools: Bash` with no command-level restriction. Any agent using this skill can run arbitrary shell commands.
- **High**: YAML user stories contain freeform text that flows directly into agent prompts. No schema validation, no input sanitization.
- **High**: URL navigation exposes page content to agent context via `snapshot`. Malicious page content enters the agent's prompt.
- **Medium**: `.env` plain text with API key. Mitigated by `.gitignore` but no encryption.
- **Medium**: Named sessions persist cookies/localStorage. No session cleanup on completion is enforced (agents are instructed to close, but it's not guaranteed).
- **Low**: `PLAYWRIGHT_MCP_ALLOWED_ORIGINS` explicitly documented as "NOT a security boundary" (transparency is good, but the limitation remains).
- **Info**: No network egress controls. Agents can make arbitrary HTTP requests via the browser.

**Calibration**: This security posture is typical for demo/prototype agentic code, but inadequate for any environment with production credentials or team deployment.

### Newport's Two-Question Test

1. **"What technical breakthrough?"** Not a technical breakthrough. Bowser composes existing Claude Code primitives (skills, agents, commands, justfiles) in a well-designed pattern. The innovation is architectural: the four-layer composable stack, the HOP pattern, and the dual-skill approach. No new algorithms or capabilities.
2. **"What measurable implications?"** Reduction in QA setup time (zero-config agentic testing vs. traditional test infrastructure). Parallel agent testing across user stories. Visual audit trail via screenshots. But: non-deterministic results with no regression baseline, no CI/CD integration path, and `--dangerously-skip-permissions` required for any execution.

### Three-Filter Calibration

1. **Measured data**: Architecture claims verified. No performance benchmarks, no token usage measurements, no reliability statistics. Demo-quality evidence only.
2. **Adoption gap**: Significant. Requires `just` (brew install), `playwright-cli` (npm -g), Claude Code, and `--dangerously-skip-permissions` trust. No onboarding path for teams. Single-developer workflow.
3. **Economic sustainability**: Token costs unknown but potentially high (opus model on every recipe, parallel agent spawning, full page snapshots in context). No cost tracking or budget controls.

## Notable Quotes

> "Code is fully commoditized. Anyone can generate code. That is not an advantage anymore. What is an advantage is your specific solution to the problem you're solving." — IndyDevDan ([05:22](https://www.youtube.com/watch?v=efctPj6bjCY&t=322))

> "Agentic engineers know what their agents are doing, and they know it so well, they don't have to look. Vibe coders don't know, and they don't look." — IndyDevDan ([26:21](https://www.youtube.com/watch?v=efctPj6bjCY&t=1581))

> "There are entire classes of problems that you don't need to solve anymore if you teach your agents to solve that problem." — IndyDevDan ([23:09](https://www.youtube.com/watch?v=efctPj6bjCY&t=1389))

> "Specialization combined with scale and agent orchestration is where the big nugget of gold is right now in the age of agents." — IndyDevDan ([26:58](https://www.youtube.com/watch?v=efctPj6bjCY&t=1618))

## Related Sources

- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) — Dan's earlier skills-focused video; this video extends that foundation with subagent and orchestration layers
- [010: Claude Code Multi-Agent Orchestration with Opus 4.6](010-indydevdan-multi-agent-orchestration.md) — The agent orchestration features Dan references and builds upon here
- [064: One Prompt Every AGENTIC Codebase Should Have](064-indydevdan-agentic-prompt.md) — Dan's prompt engineering patterns that underpin the command/orchestration layer
- [030: Playwright CLI vs MCP](030-playwright-cli-vs-mcp.md) — The CLI vs. MCP comparison that informed Dan's architectural choice for browser automation
- [062: Every Level of Claude Code Explained](062-simon-scrapes-claude-code-levels.md) — Simon Scrapes' layered breakdown of Claude Code features that complements Dan's layered architecture
- [017: Be Careful w/ Skills](017-primeagen-skills-security.md) — The security concerns Dan alludes to regarding prompt injections from community plugins

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system, CLI tooling preferences, and the Playwright CLI integration Dan builds on
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Subagent orchestration, meta-prompting, Higher-Order Prompts, and the four-layer architecture as a reusable pattern
