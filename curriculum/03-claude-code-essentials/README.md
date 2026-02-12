# Module 03: Claude Code Essentials

> Set up Claude Code effectively -- CLAUDE.md configuration, the skills system, and context management fundamentals.

## Overview

Claude Code is a CLI-based AI development environment that becomes dramatically more effective when configured deliberately. Out of the box, it is a capable coding assistant. With proper setup -- a well-structured CLAUDE.md file, a curated set of skills, and disciplined context management -- it becomes an extensible platform for AI-assisted engineering workflows.

This module covers three interconnected concerns. First, how to configure Claude Code's behavior through CLAUDE.md and project-level settings. Second, the skills system: what skills are architecturally, how they differ from MCP servers and custom commands, and how to find, install, and build them. Third, the security considerations that come with extending Claude Code through third-party skills -- a topic that the community is only beginning to take seriously.

The skills system is where most of the depth lies. As IndyDevDan frames it, skills are "lazy-loaded instructions" -- they only consume context window space when activated, making them the preferred extension mechanism for specialized capabilities. Understanding this architectural property, and knowing when to reach for a skill versus an MCP server versus a custom command, is one of the practical skills that separates effective Claude Code users from those who are merely using it.

## Prerequisites

- [Module 01: Foundations](../01-foundations/README.md) -- Understanding the AI landscape and model capabilities
- [Module 02: Prompting & Workflows](../02-prompting-and-workflows/README.md) -- Context engineering principles that underpin skills architecture

## Core Concepts

### Concept 1: CLAUDE.md as the Project Brain

CLAUDE.md is the primary configuration file that shapes Claude Code's behavior for a given project. It sits at the root of your repository and is loaded into the agent's context at the start of every session. It defines project conventions, architectural decisions, coding standards, and workflow preferences -- everything the agent needs to know about how you work and what you expect.

Because CLAUDE.md is always loaded, it occupies context window space in every session. This creates a design tension: you want enough information to guide Claude Code effectively, but every line in CLAUDE.md consumes tokens that could be used for the actual work. This tension is precisely what the skills system resolves -- by moving specialized workflow knowledge out of CLAUDE.md and into skills that load on demand.

Effective CLAUDE.md files focus on universal project context: directory structure, tech stack, testing conventions, naming patterns, and any non-obvious architectural decisions. Specialized workflows (image generation, deployment procedures, code review checklists) belong in skills, not in CLAUDE.md.

### Concept 2: Skills as Lazy-Loaded Instructions

The central architectural insight of the skills system, emphasized by both IndyDevDan ([#015]) and Leon van Zyl ([#013]), is that skills are "lazy-loaded instructions" that only occupy context window space when activated. This stands in direct contrast to MCP server tool definitions, which are always present in the agent's context and consume tokens whether or not they are used in a given session.

Every skill is anchored by a `SKILL.md` file with structured YAML frontmatter:

- **name**: Human-readable skill name for discovery
- **description**: What the skill does -- written for Claude Code's auto-activation system, not for human readers
- **allowed-tools**: Which Claude Code tools the skill is permitted to use (scoping the skill's capabilities)
- **argument-hint**: Guidance on what arguments the skill expects when invoked

The body of `SKILL.md` contains the actual instructions: step-by-step workflows, reference material, scripts, and domain knowledge. As IndyDevDan explains in [#015], this structure mirrors good API design -- a clear interface (frontmatter) backed by an implementation (body).

When a user asks Claude Code to perform a task, the agent reads the description fields of available skills to determine which ones are relevant. Only the relevant skills are loaded into the working context. This means you can have dozens of installed skills without paying a token cost for all of them in every session.

> "We can use skills to teach Claude Code how to do something that it couldn't do natively." -- Leon van Zyl ([00:55](https://www.youtube.com/watch?v=vIUJ4Hd7be0&t=55))

### Concept 3: Skills vs. MCP Servers vs. Custom Commands

The three extension mechanisms in Claude Code serve different purposes, and choosing the wrong one creates unnecessary friction or context bloat. Leon van Zyl ([#013]) provides the clearest taxonomy:

- **MCP Servers** provide new tools (browser control, database access, API integration). Tool definitions are always present in the agent's context, consuming tokens even when unused. Best for capabilities needed frequently across sessions. Think of them as always-imported libraries.

- **Skills** provide workflows, domain knowledge, and step-by-step instructions. Loaded on demand based on conversational context. Best for specialized capabilities used occasionally -- image generation, front-end design patterns, optimization techniques, deployment procedures. Think of them as modules imported on demand.

- **Custom Commands** are simply reusable prompts triggered manually. No auto-activation, no tool integration. Best for frequently repeated prompt patterns that do not need autonomous tool access.

As IndyDevDan puts it in [#015]: "If you would put it in a library that is always imported, use an MCP server. If you would put it in a module that is imported on demand, use a skill."

Skills and MCP tools can be combined: a skill might instruct the agent to use a particular MCP tool in a specific way, layering workflow knowledge on top of raw tool capabilities. This composition -- workflow instructions (skill) directing tool usage (MCP) -- is a common and effective pattern.

> "MCP servers simply provide new tools to the agent... skills actually take up very little context." -- Leon van Zyl ([01:47](https://www.youtube.com/watch?v=vIUJ4Hd7be0&t=107))

### Concept 4: The Skills Ecosystem

Two main sources exist for discovering and installing skills, as Leon van Zyl covers in [#013]:

1. **Anthropic's built-in plugin marketplace**: Accessed directly within Claude Code. Contains Anthropic's officially curated skills.
2. **skills.sh (Vercel)**: An open marketplace for community-contributed skills. Notable entries include a "Find Skills" meta-skill for discovering other skills, a "Skill Creator" skill for building new skills, React best practices, front-end design, and browser automation.

The ecosystem also includes meta-skills -- skills that find or create other skills. The "Skill Creator" skill, for instance, bootstraps a well-structured `SKILL.md` from a natural language description of the desired capability, lowering the barrier to building custom skills.

IndyDevDan ([#015]) frames the ecosystem through both opportunity and responsibility. The marketplace model enables specialization: domain experts can encode their knowledge as skills that generalist engineers consume. But as the ecosystem grows, the question of trust becomes unavoidable -- a concern that ThePrimeagen takes head-on in [#017].

### Concept 5: Building Custom Skills

Leon van Zyl ([#013]) demonstrates the full process of building a custom skill from scratch -- an image generation skill using Google's Nano Banana Pro model:

1. **Define the capability boundary**: Be specific. "Generate images" is too broad; "Generate images using a specific model via a Python script with API key from environment variables" is appropriately scoped.
2. **Write the SKILL.md frontmatter**: Name, description (written for the auto-activation system), allowed-tools, argument-hint.
3. **Write the instructions body**: Step-by-step instructions the agent follows, including error handling guidance, expected outputs, and validation steps.
4. **Include supporting resources**: Scripts, reference files, examples. These are loaded alongside the instructions when the skill activates.
5. **Handle secrets securely**: API keys go in `.env` files excluded from git, referenced through environment variables in supporting scripts.
6. **Test activation**: Verify that conversational prompts correctly trigger the skill and that the agent follows the instructions reliably.

IndyDevDan ([#015]) adds an important refinement to step 2: the quality of the description field is critical because it determines whether the auto-activation system correctly identifies when the skill should be loaded. Write descriptions for the machine, not for humans. Make them precise and keyword-rich.

### Concept 6: Token Efficiency and Context Budget Discipline

Skills are a tool for managing the context budget deliberately. As IndyDevDan argues in [#015], even with a million-token context window, discipline matters: keep the baseline lean, load specialized knowledge on demand, and treat context window space as a scarce resource even when it feels abundant. Skills are the engineering mechanism for this discipline -- they encode the principle that not everything needs to be in context all the time.

Leon van Zyl ([#013]) demonstrates this concretely: installed skills consume very little context because Claude Code only loads the minimum metadata needed for skill discovery (name, description, activation conditions). The full skill content -- which can include extensive instructions, reference material, and examples -- is only loaded when the agent decides the skill is relevant to the current task.

This connects directly to the context engineering principles covered in [Module 02: Prompting & Workflows](../02-prompting-and-workflows/README.md). See also: Tim Berglund's "60-70% rule" -- research shows that performance peaks at roughly 60-70% of context window capacity, meaning effective context engineering requires being selective enough to leave headroom. Skills are one of the primary mechanisms for achieving that selectivity.

### Concept 7: Advanced Claude Code Configuration -- Hooks, MCP CLI, and Insights

Beyond skills and CLAUDE.md, Claude Code supports several advanced configuration mechanisms that extend the platform's capabilities in sophisticated ways. As demonstrated in AI LABS ([#021]), these features enable deterministic control over agent behavior, more efficient context management, and structured knowledge accumulation across sessions.

**Hooks with exit code 2**: Claude Code hooks can return exit code 2 to block agent actions deterministically. This is more than logging or notification -- it is enforcement. AI LABS uses this to prevent agents from modifying test files, enforcing a test-driven development discipline where tests are written by humans (defining behavior) and implementation is written by agents (satisfying the tests). When a hook returns exit code 2, the agent's action is rejected and the agent must adjust its approach.

**MCP CLI mode**: An experimental feature that addresses a specific context management problem. When many MCP servers are installed, their combined tool schemas consume significant context window space in every session, whether or not those tools are used. MCP CLI mode presents MCP server tools as CLI commands rather than loading tool schemas into the agent's context. The agent invokes tools via command-line interface instead of carrying all tool definitions in the context window, reducing baseline token consumption.

**The `insights` command**: A structured documentation pattern for project-specific notes that persist across sessions. `/insights add` functions as a lightweight knowledge base for the project -- more dynamic than CLAUDE.md (which requires file edits to update), less structured than skills (which are designed for reusable workflows). Insights serve as a middle ground for capturing architectural decisions, gotchas, and context that emerge during development.

**Structured documentation in context**: A recurring theme in AI LABS is that agent output quality is directly proportional to the quality of structured context provided. Feed agents user stories, architecture decision records, and explicit requirements rather than vague instructions. The difference between "improve the authentication flow" and "implement OAuth2 refresh token rotation according to ADR-014" is measurable in both correctness and execution time.

## Patterns & Practices

### Pattern 1: Skill Composition and Chaining

- **When to use**: When a task spans multiple specialized capabilities that no single skill covers.
- **How it works**: Multiple skills activate for different aspects of the same task, or one skill's output feeds into another skill's input. The auto-activation mechanism handles this naturally -- the agent determines which skills are relevant and loads them as needed.
- **Example**: As Leon van Zyl demonstrates in [#013], a front-end design skill improves layout and aesthetics, an image generation skill creates a custom hero image, and an image optimization skill compresses it from 631KB to 56KB for web performance. The three skills chain sequentially without formal orchestration.
- **Source**: [#013], [#015]

### Pattern 2: The Extension Decision Framework

- **When to use**: When deciding how to add a new capability to your Claude Code setup.
- **How it works**: Apply this decision tree:
  - Is this capability needed in most sessions? Use an **MCP server**.
  - Is this a specialized workflow used occasionally, with rich instructions? Use a **skill**.
  - Is this a repeated prompt pattern with no tool integration? Use a **custom command**.
  - Does this skill need to orchestrate MCP tools in a specific way? **Combine** a skill (for workflow instructions) with an MCP server (for tool access).
- **Example**: File system access is an MCP server (always needed). Image generation is a skill (occasionally needed, instruction-heavy). A standard PR description template is a custom command (no tools, just a prompt pattern).
- **Source**: [#013], [#015]

### Pattern 3: Secure Skill Configuration

- **When to use**: When building skills that interact with external APIs or sensitive resources.
- **How it works**: Never hardcode secrets in skill markdown files. Use `.env` files excluded by `.gitignore` and reference secrets through environment variables in the skill's supporting scripts. Scope `allowed-tools` to the minimum set the skill needs -- a code review skill should not have Write access; an image generation skill does not need unrestricted Bash access.
- **Example**: Van Zyl's image generation skill ([#013]) stores the API key in a `.env` file and the Python script reads it from the environment, keeping secrets out of the skill's markdown and out of the git repository.
- **Source**: [#013], [#015]

### Pattern 4: Bootstrap with Meta-Skills

- **When to use**: When building a new custom skill and you want a well-structured starting point.
- **How it works**: Use the "Skill Creator" skill (available from skills.sh) to generate a properly structured `SKILL.md` from a natural language description. Then refine the generated output -- adjust the description for auto-activation precision, tighten `allowed-tools` scope, and add domain-specific instructions.
- **Example**: Instead of writing a skill from scratch, ask Claude Code to use the Skill Creator skill: "Create a skill that generates database migration files following our team's conventions." The meta-skill produces the scaffolding; you refine the domain knowledge.
- **Source**: [#013]

### Pattern 5: Hooks for Test-Driven Agent Workflows

- **When to use**: When you want agents to implement code but not modify your test suite.
- **How it works**: Create a PreToolUse hook that checks if the agent is about to write to test files. Return exit code 2 to block the write. This enforces a workflow where humans write tests (defining behavior) and agents write implementation (satisfying the tests). The deterministic enforcement via hooks is more reliable than prompting the agent not to touch tests -- the agent cannot bypass a hook that returns exit code 2.
- **Example**: AI LABS ([#021]) demonstrates a hook that intercepts Write and Edit operations on test files and blocks them with exit code 2. The agent must then implement code that passes the human-written tests, creating a natural TDD loop.
- **Source**: [#021]

## Common Pitfalls

- **Writing skill descriptions for humans instead of for the auto-activation system**: The description field in `SKILL.md` is what Claude Code reads to decide whether to activate a skill. Vague or conversational descriptions lead to unreliable activation. Make descriptions precise, keyword-rich, and focused on what the skill does and when it should be used.

- **Over-permissioning skills with allowed-tools**: Giving a skill access to every tool "just in case" expands the attack surface and increases the chance of unintended side effects. A code review skill that can Write files might accidentally modify the code it is supposed to be reviewing. Scope permissions to the minimum required.

- **Loading everything into CLAUDE.md instead of using skills**: A common pattern for new users is to pack every workflow, convention, and procedure into CLAUDE.md. This consumes context window space in every session, regardless of relevance. Move specialized workflows into skills; keep CLAUDE.md focused on universal project context.

- **Installing skills from untrusted sources without review**: As ThePrimeagen warns in [#017], 36% of publicly available agent skills contain security vulnerabilities. Skills execute with user-level permissions and can run arbitrary code. Treat skill installation with the same caution you would give to running an unknown script -- review the source code before installing.

- **Ignoring token cost of MCP servers**: When every capability is an MCP server, tool definitions accumulate in the context window and consume tokens in every session. If you notice your context filling up quickly, audit which MCP servers are loaded and consider converting occasionally-used ones to skills.

- **Loading too many MCP server tool schemas into context**: When many MCP servers are installed, their combined tool definitions consume significant context window space in every session. AI LABS ([#021]) recommends the experimental MCP CLI mode as a mitigation -- tools are invoked via CLI rather than loaded as schemas. Alternatively, audit which MCP servers are truly needed per-session and disable the rest. The cost is real: a dozen MCP servers might consume thousands of tokens before the agent even begins working on the actual task.

## Hands-On Exercises

1. **Audit your context window**: Start a Claude Code session and ask it to describe what is in its context. Count how many MCP tool definitions are loaded. Identify any that could be converted to on-demand skills based on usage frequency.

2. **Build a custom skill from scratch**: Choose a workflow you repeat regularly (generating test files, writing commit messages in a specific format, setting up a new API endpoint). Write a `SKILL.md` with proper frontmatter and step-by-step instructions. Test that it activates reliably from natural language prompts.

3. **Practice the extension decision framework**: Take five capabilities you currently use or want to add. For each one, decide whether it should be an MCP server, a skill, or a custom command. Write a sentence justifying each choice using the criteria from this module.

4. **Security review a third-party skill**: Find a skill on skills.sh that looks useful. Before installing it, read its full source code. Identify: what tools does it use? Does it make network requests? Does it access files outside the project directory? Does it handle secrets safely? Document your findings and decide whether to install it.

5. **Refactor CLAUDE.md with skills**: Take a long CLAUDE.md file (or create a deliberately bloated one) and extract three specialized sections into separate skills. Verify that the skills activate correctly when relevant and that CLAUDE.md is lighter as a result.

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [013: Stop Using Claude Code Without Skills](../../sources/013-leon-van-zyl-claude-code-skills.md) | Leon van Zyl | Hands-on skills tutorial, building custom skills, skill composition, MCP vs skills taxonomy |
| [015: I finally CRACKED Claude Agent Skills](../../sources/015-indydevdan-skills-engineering.md) | IndyDevDan | Skills architecture, lazy-loading, SKILL.md anatomy, skills.sh ecosystem, context budget management |
| [017: Be Careful w/ Skills](../../sources/017-primeagen-skills-security.md) | ThePrimeagen | Skills security, 36% vulnerability rate, hallucination squatting, supply chain risks |
| [021: Claude's Best Release Yet + 10 Tricks](../../sources/021-ai-labs-claude-code-tricks.md) | AI LABS | Hooks with exit code 2, MCP CLI mode, insights command, structured documentation, context engineering |

## Further Reading

- [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) -- IndyDevDan's companion repository with meta-prompts, hooks, and agent configuration examples
- [skills.sh](https://skills.sh) -- Vercel's open marketplace for community-contributed Claude Code skills
- [Module 02: Prompting & Workflows](../02-prompting-and-workflows/README.md) -- Context engineering principles that explain why lazy-loaded skills are architecturally superior
- [Module 04: Agentic Patterns](../04-agentic-patterns/README.md) -- Skill composition and chaining as primitives in agentic workflows
