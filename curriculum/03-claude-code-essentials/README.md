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

Charlie Automates ([#040](../../sources/040-charlie-automates-claudemd-context.md)) quantifies the cost of ignoring this principle. A 733-line CLAUDE.md consumes 15-20% of the context window before any work begins. More importantly, irrelevant instructions do not sit passively in context -- they actively dilute the model's attention, degrading output quality across the entire conversation. As Charlie puts it: "They think the goal is to make Claude smarter, giving it more information, more context, more rules. It's not. Claude is already super intelligent. The goal is to make Claude more focused."

Simon Scrapes ([#051](../../sources/051-simon-scrapes-claude-code-tips.md)) independently arrives at the same principle with a memorable formulation: "Keep CLAUDE.md lean and point to where the detail lives. Don't dump the detail itself." His recommendation is to keep CLAUDE.md under 20-30 lines and use it as an index that points to skills and reference files that Claude loads on demand. This preserves a clean, scannable root configuration while keeping detailed context available when needed without eating into the token budget of every session.

Charlie introduces Carl (Context Augmentation Reinforcement Layer), a plugin that addresses this by splitting rules into domain-based groups (global, dev, content, clients, agents) and loading only the domains whose keywords match the current prompt. The same 734-line CLAUDE.md reduced to 28 rules for a content task and 23 rules for a dev task. Carl also provides star commands for manual style overrides (`*brief` for bullet-point-only output, `*dev` for code-over-explanation) and context brackets that automatically adjust verbosity as the context window fills -- from detailed responses when fresh, to concise at moderate usage, to code-only survival mode when depleted. Install with a single `npx carl-core` command.

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

Simon Scrapes ([#051](../../sources/051-simon-scrapes-claude-code-tips.md)) extends this taxonomy with a fourth category: **Plugins**. Plugins are the distribution layer -- a packaged collection of commands, skills, hooks, and agents that can be installed from a marketplace in two commands. He also clarifies that **hooks** are purely programmatic (zero LLM tokens) and run deterministic checks at defined lifecycle points, such as scanning output drafts for banned words. The four-part extensibility stack -- slash commands (user-triggered), skills (auto-invoked context), hooks (zero-token programmatic checks), and plugins (distributable packages) -- provides a clear mental model for which mechanism to use when.

> "MCP servers simply provide new tools to the agent... skills actually take up very little context." -- Leon van Zyl ([01:47](https://www.youtube.com/watch?v=vIUJ4Hd7be0&t=107))

### Concept 4: The Skills Ecosystem

Two main sources exist for discovering and installing skills, as Leon van Zyl covers in [#013]:

1. **Anthropic's built-in plugin marketplace**: Accessed directly within Claude Code. Contains Anthropic's officially curated skills.
2. **skills.sh (Vercel)**: An open marketplace for community-contributed skills. Notable entries include a "Find Skills" meta-skill for discovering other skills, a "Skill Creator" skill for building new skills, React best practices, front-end design, and browser automation.

The ecosystem also includes meta-skills -- skills that find or create other skills. The "Skill Creator" skill, for instance, bootstraps a well-structured `SKILL.md` from a natural language description of the desired capability, lowering the barrier to building custom skills.

IndyDevDan ([#015]) frames the ecosystem through both opportunity and responsibility. The marketplace model enables specialization: domain experts can encode their knowledge as skills that generalist engineers consume. But as the ecosystem grows, the question of trust becomes unavoidable -- a concern that ThePrimeagen takes head-on in [#017].

Agrici Daniel's "Cloudy Ads" skill ([#043](../../sources/043-agrici-daniel-claude-ad-agency.md)) demonstrates the ecosystem's reach beyond software development. This skill packages an entire paid advertising workflow -- covering Google Ads, Meta, YouTube, LinkedIn, TikTok, and Microsoft Ads with over 190 audit checks and industry-specific templates. Its knowledge base draws from approximately 2,500 websites on advertising best practices, encoded as markdown files that the agent reads on demand. The skill uses a progressive questioning pattern (broad parameters first, then targeted follow-ups after reading relevant skill files) and delegates to parallel sub-agents for execution. When asked to produce a PDF report, the agent self-orchestrates: writing a Python script for HTML-to-PDF conversion, generating charts, self-reviewing for formatting issues, and fixing them autonomously. This demonstrates that skills can encode entire professional domains -- not just developer workflows -- into reusable, extensible Claude Code capabilities. The skill also demonstrates budget-aware reasoning: at $1,000/month it recommends Meta only, ruling out LinkedIn (too expensive) and Google Search (wrong goal), illustrating how constraint-based reasoning distinguishes a useful skill from a generic prompt.

### Concept 4a: The Three-Level Skill Loading Model

Mark Kashef ([#079](../../sources/079-mark-kashef-claude-skills-guide.md)), synthesizing Anthropic's 33-page official skills guide, reveals a three-level loading model that explains how skills manage context efficiently. **Level 1** (YAML front matter) is always loaded in the system prompt -- it contains only the name, description, and trigger words (under 1,000 characters). **Level 2** (procedural instructions) loads when Claude Code determines the skill might match the current task. **Level 3** (linked files -- scripts, references, assets) loads only when the skill is actively being executed. This progressive loading is the architectural mechanism behind the "lazy-loaded" property.

Kashef uses an effective analogy: MCPs are the hands (tooling, connections to external services), while skills are the recipes (procedural knowledge of how to use those tools). Without skills, Claude Code "yolos" MCP server calls; with skills, it follows a crystallized procedure that was proven to work.

He also identifies five design patterns for skills: sequential workflow (linear steps with rollback), multi-MCP coordination (orchestrating multiple MCPs in phases), iterative refinement (generate-audit-refine cycles), conditional branching (routing based on context), and domain-specific intelligence (embedded business rules and compliance checks). The YAML front matter is the make-or-break layer: the description must answer what the skill does *and* when it should be invoked, with specific trigger words rather than vague descriptions.

### Concept 4b: Encoding Domain Expertise in Skills

Tanmay Deshpande ([#090](../../sources/090-tanmay-deshpande-claude-skill-tradeoffs.md)) demonstrates a compelling pattern for skills that goes beyond developer workflows: encoding complex analytical frameworks as reusable skill invocations. His architecture trade-off analysis skill takes a one-paragraph scenario description -- such as a fintech startup deciding between microservices extraction, a modular monolith refactor, or monolith optimization -- and produces a comprehensive architecture decision record. The output includes weighted scoring across architecture characteristics, Roger Martin's "What Would Have to Be True" strategic framework, second-order effects analysis (Conway's Law implications, discipline tax), risk profiles, and a phased implementation roadmap.

The key insight is that skills can encode domain expertise from management and architecture literature into automated workflows, making sophisticated analytical approaches accessible without requiring the user to know the frameworks by name. A junior architect running this skill gets exposure to frameworks they might not know to apply, leveling the analytical playing field. As Deshpande puts it: "Every architecture decision I have seen plays out the same way. Someone proposes microservices, someone else defends the monolith, 3 hours of whiteboarding later, the most senior person in the room wins and nobody documents why." The skill replaces that ad-hoc process with a structured, documented artifact that serves as a starting point for discussion rather than a final decision. This pattern generalizes: any complex decision-making process with consistent structure (trade-off analysis, risk assessment, technology selection, compliance checks) is a strong candidate for encoding as a Claude Code skill.

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

### Concept 7: Research Workarounds and Fact-Checking Discipline

Simon Scrapes ([#051](../../sources/051-simon-scrapes-claude-code-tips.md)) identifies two practical gaps in Claude Code's native capabilities and demonstrates workarounds.

**Research access limitations**: Claude Code cannot fetch from many sites (Reddit, paywalled content, some social platforms). A workaround installs the Gemini CLI as a fallback research tool via a custom skill that detects blocked-site requests and routes them through Gemini's broader web access. Additionally, the community-built "last 30 days" skill scans Reddit and X for recent discussions, synthesizes patterns, and generates ready-to-use prompts.

**Fact-checking as systematic workflow step**: Asking Claude to "double check every claim and statistic and make a table of what you could and couldn't verify, including the source" produces a verification matrix that catches hallucinated statistics before publication. In Simon's demo, 3 of 8 claims in generated content were flagged as unverifiable, with Claude recommending removal or softening. This transforms fact-checking from an afterthought into a final step in content workflows -- particularly valuable for non-code outputs where traditional test suites do not apply.

### Concept 8: The Seven Levels of Claude Code Mastery

Simon Scrapes ([#062](../../sources/062-simon-scrapes-claude-code-levels.md)) organizes Claude Code proficiency into a structured progression that maps the full capability surface, from basic prompting through fully autonomous pipelines:

1. **Prompting with Intent** -- Using plan mode (Shift+Tab) before execution; iterating on plans before touching code
2. **CLAUDE.md Personalization** -- Setting up project rules, brand voice, and guardrails via CLAUDE.md
3. **Slash Commands, Skills, and Hooks** -- Reusable prompts (commands), context-rich background knowledge (skills), and automatic post-action triggers (hooks)
4. **MCP Connections** -- Bridging Claude Code to external apps via Model Context Protocol servers
5. **Planning Frameworks (GSD)** -- Structured planning frameworks with plan-execute-verify loops and persistent state files to combat context rot
6. **Agent Teams** -- Running sub-agents for specialized tasks, either sequentially or in parallel across multiple terminals
7. **Fully Autonomous Pipelines** -- Using loop frameworks like RAWL that run Claude autonomously against a PRD with acceptance criteria

The key insight is that most users plateau at level two or three, never reaching the orchestration and automation tiers that unlock real leverage. Simon's mental model for the three main automation primitives is particularly clean: **Skills** = how Claude *thinks* (background context loaded automatically when relevant); **Hooks** = what happens *automatically after* Claude acts (mechanical checks requiring no LLM tokens); **Commands** = what you *manually trigger* (saved prompts with dynamic arguments).

Simon also surfaces the concept of **context rot** -- as the context window fills (approaching 95% capacity), Claude auto-compresses context into summaries, degrading output reliability. At around 10,000 tokens (~7,500 words), approximately 50% of context fidelity is lost. The GSD framework mitigates this by keeping context in individual phase-level files, and the RAWL loop addresses it by feeding state back into fresh context windows after each completed task.

### Concept 8a: The Setup Hook and Install Prompts

IndyDevDan ([#064](../../sources/064-indydevdan-agentic-prompt.md)) argues that every agentic codebase should have a standardized install/maintain prompt -- a natural language document that combines deterministic setup scripts with agentic intelligence for installation, onboarding, and maintenance. Claude Code's setup hook supports two lifecycle events:

- **Init**: Runs on first setup or with `--init` flag. Handles dependency installation, database initialization, one-time setup.
- **Maintenance**: Runs periodically for dependency updates, migrations, artifact cleanup, security checks.

The core architectural insight: **deterministic scripts + agentic prompts = best of both worlds**. Scripts provide predictable execution but cannot handle unexpected failures. Agents provide intelligence but lack reliability for known steps. The combination delivers predictable execution for known steps, intelligent oversight for validation and error resolution, and interactivity for configuration decisions requiring human input.

IndyDevDan also introduces the `just` command runner (justfile) as a launchpad for standardizing codebase interactions. The justfile encodes setup commands, agent invocations with specific CLI flags, and maintenance workflows -- eliminating the "look up the right flags" problem for both humans and agents. As he puts it: "You can tell how great an engineering team is by the time it takes for a new engineer to run the project locally."

The most powerful pattern is encoding common issues directly into the install prompt. Every time an installation issue recurs, it becomes a problem/solution pair in the prompt, making the agent progressively better at handling failures without human intervention. This creates what IndyDevDan calls "a living document that executes" -- unlike static READMEs that go stale, these prompts stay accurate because if they are wrong, the installation fails, forcing an update.

### Concept 8b: Claude Cowork Plugins for Non-Developers

Ben AI ([#063](../../sources/063-ben-ai-cowork-plugins.md)) documents Anthropic's plugins system for Claude Cowork -- the non-developer counterpart to Claude Code. Plugins bundle skills, connections (MCPs, built-in connectors, browser access, local files), and slash commands into department-specific packages. This architecture mirrors what exists in Claude Code but is packaged for non-developer accessibility.

Anthropic's design organizes plugins by business department -- sales, customer support, product management, legal, finance -- with each plugin scoping its connectors and skills to that function. This department-level scoping is intentional: it prevents cross-department data leakage while enabling focused capability.

Three plugin economies are emerging: (1) **Anthropic-built plugins** as open-source starters with organization-wide sharing coming soon; (2) **Third-party provider plugins** from SaaS companies and independent builders; (3) **Custom-built plugins** unique to each business's workflows. This echoes the app store pattern but for AI agent capabilities rather than standalone applications.

The broader significance: plugins position AI agents as a potentially superior interface to the fragmented SaaS landscape. When Anthropic launched plugins, companies like Salesforce, ServiceNow, and Adobe saw stock drops because plugins threaten to collapse the multi-tool workflow most knowledge workers endure into a single AI interface that accesses all tools through connections.

### Concept 8b2: CoWork for Beginners -- The Accessibility Layer

Eliot Prince ([#098](../../sources/098-eliot-prince-cowork-explained.md)) provides the most beginner-friendly introduction to Claude Cowork, framing it as "the hands" to Claude's "brain" -- the same underlying Claude Code architecture wrapped in a desktop interface that does not require coding knowledge. Prince walks through three progressively complex use cases: organizing screenshots with automatic renaming and folder creation, processing invoices into structured folders with a generated CSV tracker, and using the Chrome extension to browse authenticated web pages and generate analytics reports. His emphasis on folder-based permission sandboxing -- granting Cowork access to specific folders rather than broad directories -- provides a practical security boundary for non-technical users. Prince is honest about limitations: no memory across sessions, desktop-only operation, and token usage that can burn through credits quickly on heavier tasks. He also demonstrates the plugin/skills ecosystem and the ability to import Claude Projects into Cowork sessions. This complements Ben AI's plugin-focused coverage ([#063](../../sources/063-ben-ai-cowork-plugins.md)) and Brooke Wright's more advanced tutorial ([#066](../../sources/066-brooke-wright-cowork-tutorial.md)) by providing the entry-level onboarding path.

### Concept 8c: CoWork as Operational Assistant

Jack Roberts ([#083](../../sources/083-jack-roberts-cowork-use-cases.md)) demonstrates five progressively more powerful CoWork use cases aimed at non-technical business users: file management, browser automation, service connectors (Gmail, Calendar, Fireflies, Canva, Notion), skills creation, and plugins. His framing distinguishes CoWork from Code clearly: "Antigravity/Claude Code is hiring a developer to build you custom software. CoWork is hiring an assistant who uses your computer, your files, your logins and does the work for you."

The most valuable pattern Roberts demonstrates is iterative skill creation from manual workflows: (1) have Claude perform a task through conversation, iterating until output quality is satisfactory, (2) refine rules and style preferences through back-and-forth dialogue, (3) enshrine the entire process as a skill for autonomous future execution. He also demonstrates multi-connector MCP chaining -- pulling meeting action items from Fireflies via MCP, then creating a Notion document with those items. When API access isn't available, CoWork's browser automation acts as a universal fallback, navigating YouTube to scrape comments or editing Canva designs directly.

### Concept 8d: Skill-to-Repeatable-Process Workflow

Bart Slodyczka ([#067](../../sources/067-bart-slodyczka-agent-teams-course.md)) provides a practical workflow for converting ad hoc team processes into reusable Claude Code skills:

1. Run the full process manually with Claude Code first
2. Iterate until the process is refined
3. Prompt Claude to "turn whatever we just did into a skill" with configurable variables
4. Store the skill in the repository, invoke via `/skillname` in future sessions
5. Update the skill incrementally as the process evolves

This creates a positive feedback loop: each team session improves the skill definition for future teams. The key principle: **do not write skills from scratch** -- run the process first, then have Claude generate the skill from the actual workflow. This ensures the skill captures the real process rather than an idealized version of it.

### Concept 8e: Context Rot Awareness and the 60% Rule

Dylan Davis ([#084](../../sources/084-dylan-davis-context-rot-60-rule.md)) provides practical context rot countermeasures specifically relevant to Claude Code users. Context window performance follows a degradation curve: up to ~60% capacity, Claude maintains effective instruction-following; between 60-95%, performance degrades progressively; past 95%, Claude triggers automatic compaction that loses nuance. The practical rule: treat 60% of the context window as the effective working limit.

For Claude Code specifically, this means monitoring session length and proactively using `/compact` (see Concept 8, Level 1) before degradation begins. Davis's handoff strategy -- creating a structured summary covering what has been covered, key decisions, current status, and next steps -- translates directly to starting fresh Claude Code sessions with a well-crafted initial prompt that carries forward context from the previous session. This connects to the GSD framework (Concept 8, Level 5) and Simon Scrapes' context rot mitigation patterns.

### Concept 8e2: Agent Memory Architecture -- Hybrid Search and the Search-Then-Get Pattern

Damian Galarza ([#099](../../sources/099-damian-galarza-agent-memory-search.md)) provides a detailed technical breakdown of how AI agents search their memory, using OpenClaw's default memory system as a concrete implementation. The core architectural insight is that no single search approach is sufficient. Keyword search (grep, BM25) excels at exact matches -- error codes, function names, specific identifiers -- but misses semantic relationships. Semantic search (embeddings, vector databases) finds conceptually related content but fails on literal string matching. A counter-intuitive finding drives the analysis: the Claude Code team started with a vector database but found that grep-based agentic search actually performed better and was easier to maintain.

OpenClaw's solution combines both via weighted score fusion: 0.7 times the vector similarity score plus 0.3 times the BM25 text score. Both searches use a 4x candidate multiplier (requesting 24 candidates when 6 results are needed) to give the fusion step more to work with, and results are filtered by a minimum threshold of 0.35. Memory files are chunked into roughly 400 tokens with 80-token overlap between chunks, and an embedding cache prevents redundant API calls by hashing chunk text and caching embeddings keyed by provider and model.

The most practically relevant pattern is the **search-then-get** two-tool design: `memory_search` returns lightweight snippets (file path, line numbers, relevance score, 700-character preview), and `memory_get` retrieves specific sections by path and line range. This mirrors how humans search -- scan results for relevance, then read only what matters -- and prevents loading entire files into the context window. The system prompt describes `memory_search` as a "mandatory recall step" that agents must use before answering questions about prior work. This pattern connects directly to the context engineering principles in [Module 02](../02-prompting-and-workflows/README.md) and the 60% rule (Concept 8e): keeping token usage lean is not just about managing session length but also about how agents retrieve stored knowledge.

### Concept 8f: The Four-Layer Browser Automation Architecture

IndyDevDan ([#088](../../sources/088-indydevdan-browser-automation-stack.md)) presents "Bowser," a four-layer architecture for agentic browser automation and UI testing:

- **Layer 1 -- Skills (Capability)**: Foundational tools like a Playwright browser skill (headless, parallel sessions, persistent profiles) and Claude's `--chrome` flag. Skills define what an agent can do.
- **Layer 2 -- Subagents (Scale)**: Specialized agents wrapping a skill with a concrete workflow. The Browser QA agent parses user stories into steps, creates output directories, takes screenshots at each step, and reports pass/fail.
- **Layer 3 -- Commands/Prompts (Orchestration)**: Custom slash commands like `/ui-review` that spawn agent teams, distribute user stories across parallel subagents, and collect results. This is the meta-prompting layer.
- **Layer 4 -- Justfiles (Reusability)**: A task runner providing a single entry point for all agentic workflows with configurable parameters.

Dan explicitly recommends CLIs (like the Playwright CLI) over MCP servers for browser automation. MCP servers consume more tokens and force you into their opinionated workflow. CLIs give freedom to build opinionated layers on top with better token efficiency. He also introduces "Higher-Order Prompts" (HOPs) -- prompts that take another prompt as a parameter, analogous to higher-order functions -- enabling reusable orchestration without duplicating boilerplate.

### Concept 8g: Claude Code vs. No-Code Platforms

Simon Scrapes ([#078](../../sources/078-simon-scrapes-n8n-failing.md)) provides an honest comparison of n8n and Claude Code, arguing they are complementary rather than competitive. Claude Code with MCP connections now matches or exceeds n8n's drag-and-drop speed for building workflows. But n8n's execution history log provides visual debugging that Claude Code cannot match -- non-technical team members can click through workflow runs and inspect data at each node. The optimal architecture: Claude Code for infrastructure (backends, front-ends, databases, authentication) and n8n for core business automations that need visual transparency. The n8n MCP server and n8n skills let Claude Code build and edit n8n workflows, bridging both tools.

### Concept 9: Advanced Claude Code Configuration -- Hooks, MCP CLI, and Insights

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

- **Loading everything into CLAUDE.md instead of using skills**: A common pattern for new users is to pack every workflow, convention, and procedure into CLAUDE.md. This consumes context window space in every session, regardless of relevance. Charlie Automates ([#040](../../sources/040-charlie-automates-claudemd-context.md)) quantifies the damage: a 733-line CLAUDE.md eats 15-20% of context before you even send a message, and the irrelevant instructions actively dilute the model's attention. Move specialized workflows into skills or use a domain-based segmentation tool like Carl; keep CLAUDE.md focused on universal project context.

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
| [040: Stop Feeding Claude Your Entire CLAUDE.md](../../sources/040-charlie-automates-claudemd-context.md) | Charlie Automates | Monolithic CLAUDE.md as attention dilution, Carl plugin for domain-based rule segmentation, star commands, context brackets, focus over intelligence |
| [043: Claude Code just replaced your ad agency](../../sources/043-agrici-daniel-claude-ad-agency.md) | Agrici Daniel | Cloudy Ads skill for paid advertising, domain-expert skills as agency replacements, 190+ audit checks, progressive questioning, skills knowledge base at scale (2,500 sources), non-coding use case |
| [051: You're using Claude Code Wrong](../../sources/051-simon-scrapes-claude-code-tips.md) | Simon Scrapes | Extensibility stack disambiguation (commands vs skills vs hooks vs plugins), CLAUDE.md lean pointer pattern, Gemini CLI research fallback, fact-checking as workflow discipline |
| [062: Every Level of Claude Code Explained](../../sources/062-simon-scrapes-claude-code-levels.md) | Simon Scrapes | Seven levels of mastery, skills-commands-hooks mental model, context rot mitigation, GSD and RAWL frameworks, "don't dump" CLAUDE.md principle |
| [063: Claude Cowork Just Became 10x Better (Plugins Guide)](../../sources/063-ben-ai-cowork-plugins.md) | Ben AI | Plugin architecture (skills + connections + commands), department-scoped plugins, three plugin economies, AI as universal software interface |
| [064: One Prompt Every AGENTIC Codebase Should Have](../../sources/064-indydevdan-agentic-prompt.md) | IndyDevDan | Setup hook (init/maintenance), deterministic code + agentic prompts, justfile as launchpad, install prompt as living document, encoding common issues |
| [066: How to use Claude Cowork better than 99% of people](../../sources/066-brooke-wright-cowork-tutorial.md) | Brooke Wright | Co-work as bridge product, connectors and plugins as leverage layer, parallel task execution, safety patterns (deletion guardrails) |
| [067: Learn 90% Of Claude Code Agent Teams](../../sources/067-bart-slodyczka-agent-teams-course.md) | Bart Slodyczka | Three modes of Claude Code (default/sub-agent/teams), skill-from-process workflow, model selection for cost optimization, shared memory files |
| [020: How & When to Use Claude Code Agent Teams](../../sources/020-simon-scrapes-agent-teams.md) | Simon Scrapes | Agent teams vs. sub-agents, context rot as team motivation, shared task list collaboration, decision heuristics |
| [024: Agentic coding in 2026](../../sources/024-jo-van-eyck-agentic-coding-2026.md) | Jo Van Eyck | Maturity ladder, fading vs. evergreen skills, cost warnings for multi-agent, developer skills evolution |
| [026: 10 Claude Code tips I wish I knew from the start](../../sources/026-no-code-mba-claude-code-tips.md) | No Code MBA | Slash commands, /compact for context management, sub-agents, plan mode, security review command |
| [030: Playwright CLI vs MCP](../../sources/030-playwright-cli-vs-mcp.md) | Playwright | CLI vs. MCP token efficiency (4x gain), file-mediated context control, lazy-loading pattern for browser automation |
| [078: N8N is Failing Us...](../../sources/078-simon-scrapes-n8n-failing.md) | Simon Scrapes | Claude Code vs. n8n comparison, visual observability advantage, combined system architecture, MCP bridging |
| [079: Anthropic's Full Claude Skills Guide](../../sources/079-mark-kashef-claude-skills-guide.md) | Mark Kashef | Three-level loading model, MCPs as hands / skills as recipes, five design patterns, YAML front matter best practices, skill testing framework |
| [083: 5 INSANE Claude CoWork use cases](../../sources/083-jack-roberts-cowork-use-cases.md) | Jack Roberts | CoWork as operational assistant, iterative skill creation from manual workflows, multi-connector MCP chaining, browser automation as API bypass |
| [084: The 60% Rule Stops Context Rot](../../sources/084-dylan-davis-context-rot-60-rule.md) | Dylan Davis | 60% rule for context windows, four warning signs of context rot, handoff strategy, Claude-specific compaction behavior |
| [088: My 4-Layer Agentic Browser Automation Stack](../../sources/088-indydevdan-browser-automation-stack.md) | IndyDevDan | Four-layer architecture (skills/subagents/commands/justfiles), CLI over MCP for token efficiency, Higher-Order Prompts, agentic UI testing |
| [090: I built Claude Skill for trade off analysis](../../sources/090-tanmay-deshpande-claude-skill-tradeoffs.md) | Tanmay Deshpande | Architecture decision automation via skills, encoding domain expertise (Roger Martin, Conway's Law), documentation gap solution |
| [098: Claude COWORK Clearly Explained](../../sources/098-eliot-prince-cowork-explained.md) | Eliot Prince | Beginner-friendly Cowork walkthrough, folder-based permission sandboxing, progressive capability stack, plugin/connector ecosystem |
| [099: How AI Agents Search Their Memory](../../sources/099-damian-galarza-agent-memory-search.md) | Damian Galarza | Hybrid search (keyword + semantic), search-then-get two-tool pattern, grep vs vector DB finding, weighted score fusion, embedding cache |

## Further Reading

- [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) -- IndyDevDan's companion repository with meta-prompts, hooks, and agent configuration examples
- [skills.sh](https://skills.sh) -- Vercel's open marketplace for community-contributed Claude Code skills
- [Module 02: Prompting & Workflows](../02-prompting-and-workflows/README.md) -- Context engineering principles that explain why lazy-loaded skills are architecturally superior
- [Module 04: Agentic Patterns](../04-agentic-patterns/README.md) -- Skill composition and chaining as primitives in agentic workflows
