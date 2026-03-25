---
source_id: "359"
title: "The Library Meta-Skill: How I Distribute PRIVATE Skills, Agents and Prompts"
creator: "IndyDevDan"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=_vpNQ6IwP9w"
date: "2026-03-16"
duration: "26:32"
type: "video"
tags: ["skills", "claude-code", "multi-agent", "agent-teams", "agentic-coding", "security", "meta-prompts"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 359: The Library Meta-Skill: How I Distribute PRIVATE Skills, Agents and Prompts

> **Creator**: IndyDevDan | **Platform**: YouTube | **Date**: 2026-03-16 | **Duration**: 26:32

# The Library Meta-Skill: Distributing Private Skills, Agents, and Prompts

## Summary

IndyDevDan presents a scalable solution to a real problem that emerges when engineers graduate from one or two codebases to ten or more: private agentic assets (skills, agents, prompts) proliferate, go out of sync, get duplicated, and become hard to coordinate across teams and devices. The proposed solution is a "library" meta-skill — a single YAML-based reference file that stores pointers to GitHub repositories or local file paths rather than duplicating the assets themselves. This functions analogously to a `package.json` or `pyproject.toml` — a lightweight manifest that agents and engineers can use to pull in the correct, current version of any agentic asset on demand.

The workflow follows four stages: **build** (create prompts, skills, and agents inside the value-generating repo), **catalog** (add references to the library YAML via `library.add`), **distribute** (use `library.use` to install assets into any new environment), and **sync** (pull the latest versions of referenced repos). Critically, this is framed as an agent-first, codeless skill — there is no custom application code backing it, just a YAML file and a Claude Code skill that interprets natural language commands against it. This approach also enables private distribution, which Dan emphasizes as essential for engineers building specialized, proprietary agentic tooling.

The video also gestures at a broader architectural philosophy: treating skills, agents, and prompts as distinct primitives with different purposes (raw capabilities, scale/parallelism, and orchestration respectively) rather than over-engineering everything into monolithic skills. The library pattern is positioned as the coordination layer on top of this primitive stack, enabling consistent deployment across personal devices, Mac Mini agents, cloud sandboxes, and team members.

---

## Key Concepts

### The Library Meta-Skill

A "meta-skill" is a skill that unlocks access to other skills, agents, and prompts. The library is implemented as a single YAML file containing references (GitHub URLs or local file paths) to agentic assets — nothing is stored directly in the library itself. This keeps the manifest lightweight and ensures that the authoritative source of truth for each asset remains in its original repository. The library skill exposes a small API: `add`, `use`, `push`, `list`, `search`, and `sync`.

### Reference-Based Distribution (Not Copy-Based)

The core architectural insight is that copying assets across codebases is the root cause of drift and duplication. Instead, the library stores *pointers* to assets. When an engineer or agent runs `library.use`, it clones or pulls from the referenced repo and installs the asset locally. This mirrors the dependency management model used by package managers — you declare what you need, and the tooling fetches the canonical version. The `sync` command specifically re-pulls all referenced repositories to ensure nothing is stale.

### Private Agentic Distribution

Dan emphasizes that high-value, specialized agentic tooling should be kept in private repositories. The library pattern supports this natively: the YAML file simply points to private GitHub repos. Access control is handled by standard Git credentials. This is a direct counter to the assumption (common among "vibe coders," per Dan) that all useful agentic tooling is public — proprietary skills and agents represent real competitive value and should be treated accordingly.

### The Agentic Primitive Stack

Dan articulates a layered model for thinking about agentic engineering:
- **Skills** — raw, reusable capabilities (lowest level)
- **Agents** — enable scale and parallelism
- **Prompts** — single-file orchestrators that coordinate skills and agents
- **Just files / commands** — optional top layer for task automation

A common mistake is over-building skills when the right tool is a lightweight prompt or agent. The library coordinates all three levels rather than forcing everything into the skill primitive.

### Agent-First, Codeless Architecture

The library is explicitly a skill with no backing application code — it is purely a Claude Code skill interpreting natural language commands against a YAML file. Dan frames this as a preview of a broader trend: pure agentic solutions that need no bespoke software, relying instead on the agent's ability to interpret structured data and execute git/file operations. This makes the system immediately portable to any environment where Claude Code (or a compatible agent) can run.

---

## Practical Takeaways

- **Treat your YAML library file like a `package.json`** — commit it to its own repo, share it with teammates and agents, and let it be the single source of truth for which agentic assets belong in any given environment. Never share assets by copying files directly.

- **Keep high-value skills, agents, and prompts in private GitHub repos** — use standard Git access controls for distribution rather than building a separate access management system. The library pattern plugs directly into existing Git infrastructure.

- **Separate the asset-building workflow from the distribution workflow** — build and iterate on skills inside the value-generating repo, then catalog them into the library. This prevents the library from becoming a development environment and keeps the catalog clean.

- **Use `library.sync` as part of any new environment setup** — whether spinning up a new device, onboarding a team member, or provisioning a cloud sandbox agent, a single sync command should bring the environment to the correct state for all agentic assets.

- **Match the primitive to the problem** — avoid over-engineering single-purpose logic into skills when a simple prompt file would suffice. Reserve skills for reusable, cross-repo capabilities; use prompts for orchestration and one-off workflows.

---

## Notable Quotes

> "We have endless skills everywhere. They're out of sync. They're duplicated and they're hard to coordinate across your engineering team."

> "Your top-notch skills, agents, and prompts should absolutely be private. I know a lot of vibe coders, you think that everything is just out there in the public. Trust me, it's not."

> "There is no code associated with this... I'm predicting we're going to see a lot of pure agentic solutions as we move through this year."

---
