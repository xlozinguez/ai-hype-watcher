# Synthesize Source — Reference Material

## Tag Taxonomy

Established tags used across source notes. Prefer existing tags; create new ones only when no existing tag fits.

### Tool & Platform Tags
- `claude-code` — Claude Code CLI tool features and usage
- `chatgpt` — ChatGPT/OpenAI tool features
- `cursor` — Cursor IDE features
- `mcp` — Model Context Protocol
- `skills` — Claude Code skills system

### Pattern & Practice Tags
- `agent-teams` — Multi-agent team coordination
- `agentic-coding` — Autonomous AI coding workflows
- `builder-validator` — Builder/validator agent pattern
- `context-engineering` — Context window management and optimization
- `meta-prompts` — Reusable prompt templates and meta-prompting
- `multi-agent` — Multi-agent orchestration patterns
- `prompt-engineering` — Prompt design and optimization
- `specification` — Spec-first development workflows
- `task-system` — Claude Code task management tools
- `validation` — Output validation and cross-model verification
- `vibe-coding` — Vibe coding phenomenon and practices

### Domain Tags
- `ai-economics` — AI infrastructure costs, compute economics
- `ai-hype` — Bubble dynamics, critical perspective on AI industry
- `ai-landscape` — Broad AI industry overview and trends
- `ai-safety` — Safety research, constitutional AI, alignment
- `ai-sdlc` — AI-driven software development lifecycle
- `capability-overhang` — Gap between AI capabilities and adoption
- `enterprise-ai` — Enterprise AI adoption and deployment
- `infrastructure` — Compute infrastructure, DRAM, GPUs, data centers
- `revenue-per-employee` — AI-native company economics
- `security` — Skills security, supply chain attacks, agent safety
- `skills-ecosystem` — Skills marketplaces, discovery, vetting

### Creator Tags (use sparingly, only when the creator's perspective is the main value)
- `anthropic` — Anthropic company strategy and philosophy
- `openai` — OpenAI company strategy and releases

## Curriculum Module Mappings

| Module | Key Topics | Typical Tags |
|--------|-----------|--------------|
| `01-foundations` | AI landscape, capability overhang, hype vs reality, model releases | `ai-landscape`, `ai-hype`, `capability-overhang` |
| `02-prompting-and-workflows` | Prompt engineering, sticky workflows, spec-first, validation | `prompt-engineering`, `specification`, `validation`, `vibe-coding` |
| `03-claude-code-essentials` | Setup, CLAUDE.md, skills system, context discipline | `claude-code`, `skills`, `context-engineering` |
| `04-agentic-patterns` | Subagents, builder/validator, meta-prompts, hooks, task system | `agentic-coding`, `builder-validator`, `meta-prompts`, `task-system` |
| `05-team-orchestration` | Agent teams, multi-agent coordination, tmux/sandboxes, observability | `agent-teams`, `multi-agent` |
| `06-strategy-and-economics` | AI-driven SDLC, infra economics, security, adoption strategy | `ai-economics`, `ai-sdlc`, `security`, `enterprise-ai`, `infrastructure` |

## Filename Conventions

- Creator slug: lowercase, hyphenated, abbreviated if long
  - "IndyDevDan" → `indydevdan`
  - "Nate B Jones" → `nate-b-jones`
  - "The PrimeTime" / "ThePrimeagen" → `primetime` or `primeagen`
  - "Internet of Bugs" → `internet-of-bugs`
  - "Leon van Zyl" → `leon-van-zyl`
  - "Ali H. Salem" → `ali-salem`
  - "Bart Slodyczka" → `bart-slodyczka`
  - "CircleCI" → `circleci`
  - "Matt Shumer" → `matt-shumer`

- Topic slug: 2-4 words capturing the main topic, lowercase, hyphenated
  - Good: `task-system`, `agent-teams`, `ai-bubble`, `skills-security`
  - Bad: `the-new-video-about-coding-with-ai-tools`
