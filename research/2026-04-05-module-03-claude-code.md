---
type: research-validation
date: 2026-04-05
module: 03-claude-code-essentials
section: all
concepts_reviewed: 76
confirmed: 42
evolved: 12
needs_update: 7
emerging_insufficient: 15
---

# Research: Module 03 Claude Code Essentials — Full Validation

> Validated on 2026-04-05. 76 concepts reviewed across 90+ sources (52 core concepts, 7 patterns, 12 pitfalls, 5 exercises).

## Summary

Module 03 is the largest module in the curriculum at 52 core concepts, and its overall health is strong. The foundational concepts (CLAUDE.md minimalism, skills architecture, extension decision framework) are well-supported and externally confirmed. However, several important developments have evolved significantly since the curriculum text was written, most notably: the Agent Skills open standard making skills cross-platform portable, the expansion of Computer Use and Dispatch to Windows, the hooks system growing from 13 to 21 lifecycle events, and AutoDream moving from "unannounced" to publicly documented. A cluster of 15 emerging concepts with zero or minimal support represent either genuinely niche topics that are nonetheless well-sourced in the curriculum text, or concepts that the dashboard's keyword-matching algorithm fails to correlate with their actual supporting sources. The module's biggest structural risk is concept sprawl -- 52 core concepts with deep nesting (c8f3a, c8d3d, etc.) makes the module harder to navigate than its peers.

## Confirmed Evergreen (22)

These concepts have strong multi-creator support and are externally validated.

### c1: CLAUDE.md as the Project Brain
- **Status**: Confirmed
- **Support**: 127 sources, 75 creators, latest 2026-04-02
- **Evidence**: Anthropic's official best practices docs now codify the "less than 200 lines" guidance. External sources (builder.io, HumanLayer, MindWired AI) all converge on the same principle: ruthless pruning, 150-200 instruction budget, hooks replacing rules. The curriculum's coverage of Charlie Automates, Boris Cherny, Matt Pocock, and Theo's study is comprehensive and current.

### c4: The Skills Ecosystem
- **Status**: Confirmed
- **Support**: 71 sources, 50 creators, latest 2026-04-01
- **Evidence**: The ecosystem has grown substantially. SkillsMP.com now indexes skills across platforms. Anthropic's own github.com/anthropics/skills repository serves as an official skill distribution channel. The curriculum's coverage of marketplaces (skills.sh, SkillHub) is accurate.

### c5: Building Custom Skills
- **Status**: Confirmed
- **Support**: 72 sources, 50 creators, latest 2026-04-01
- **Evidence**: Leon van Zyl's tutorial pattern and IndyDevDan's description-writing advice remain the canonical references. The six-step framework from Nate Herk is well-validated.

### c8: The Seven Levels of Claude Code Mastery
- **Status**: Confirmed
- **Support**: 122 sources, 72 creators, latest 2026-04-02
- **Evidence**: Simon Scrapes' progression framework continues to be referenced across the ecosystem.

### c8a1b: Claude Code 2.0 -- Loops, Scheduled Tasks, Skills Evals
- **Status**: Confirmed
- **Support**: 125 sources, 74 creators, latest 2026-04-02
- **Evidence**: These features are now GA. The /loop command and scheduled tasks are documented in official docs.

### c8a1c: Anthropic's Own Agent Harness Patterns
- **Status**: Confirmed
- **Support**: 6 sources, 6 creators, latest 2026-04-01
- **Evidence**: The JSON feature list pattern, firm instruction language, and "the harness is the fix" principle are all validated by Anthropic's own engineering blog and multiple independent practitioners.

### c8b: Claude Cowork Plugins for Non-Developers
- **Status**: Confirmed
- **Support**: 14 sources, 12 creators, latest 2026-03-31
- **Evidence**: Cowork plugins continue to expand. Department-scoped plugin model remains the core architecture.

### c8c: CoWork as Operational Assistant
- **Status**: Confirmed
- **Support**: 11 sources, 9 creators, latest 2026-03-31

### c8d3: Advanced Skill Engineering
- **Status**: Confirmed
- **Support**: 100 sources, 63 creators, latest 2026-04-02
- **Evidence**: Ben AI's framework remains the most comprehensive reference. Self-improving feedback loops are now standard practice.

### c8d3b: Obsidian Second Brain with EPARAX Structure
- **Status**: Confirmed
- **Support**: 6 sources, 3 creators, latest 2026-03-30

### c8d4: Agent Memory Architecture -- From Sessions to Persistence
- **Status**: Confirmed
- **Support**: 7 sources, 6 creators, latest 2026-03-30
- **Evidence**: The three memory types (episodic/semantic/procedural) framework from Google's white paper remains the canonical taxonomy.

### c8d4a: Context Engineering with Software Rigor
- **Status**: Confirmed
- **Support**: 91 sources, 58 creators, latest 2026-04-02
- **Evidence**: Drew Knox's "context as code" framework is well-validated. CI/CD integration for context freshness is now emerging as standard practice.

### c8d6: CoWork Foundations for Beginners
- **Status**: Confirmed
- **Support**: 11 sources, 9 creators, latest 2026-03-31

### c8e2: Agent Memory Architecture -- Hybrid Search
- **Status**: Confirmed
- **Support**: 7 sources, 6 creators, latest 2026-03-30

### c8f1b: Nested Multi-Agent Claude Code via Tmux
- **Status**: Confirmed
- **Support**: 131 sources, 78 creators, latest 2026-04-02

### c8f2a: Context Overhead in Long-Running Agents
- **Status**: Confirmed
- **Support**: 7 sources, 7 creators, latest 2026-03-13
- **Evidence**: The 7K-to-45K overhead growth pattern and "sniper agent" principle remain valid.

### c8f3: The Claude Code Desktop App
- **Status**: Confirmed
- **Support**: 122 sources, 72 creators, latest 2026-04-02

### c8f5: The Pi Alternative
- **Status**: Confirmed
- **Support**: 4 sources, 4 creators, latest 2026-04-01
- **Evidence**: Pi continues to evolve alongside Claude Code. The "think in ANDs not ORs" framing remains relevant.

### c8g: Claude Code vs. No-Code Platforms
- **Status**: Confirmed
- **Support**: 127 sources, 76 creators, latest 2026-04-02

### c9: Advanced Claude Code Configuration
- **Status**: Confirmed
- **Support**: 124 sources, 73 creators, latest 2026-04-02

### c4a3: The Fewer-but-Better Skills Principle
- **Status**: Confirmed
- **Support**: 6 sources, 5 creators, latest 2026-03-23
- **Evidence**: The 15,000 character skill list limit and the "20-30 curated skills" recommendation are validated by official docs and practitioner consensus.

### pit3: Loading everything into CLAUDE.md instead of using skills
- **Status**: Confirmed
- **Support**: 72 sources, 48 creators, latest 2026-04-01
- **Evidence**: This remains the single most common Claude Code anti-pattern. External guides universally reinforce this.

## Evolved (12)

### c3: Skills vs. MCP Servers vs. Custom Commands
- **Status**: Evolved
- **Original claim**: Three-way taxonomy with skills, MCP servers, and custom commands as distinct extension mechanisms. Custom commands are "simply reusable prompts triggered manually."
- **Current state**: Leon van Zyl (#376) confirms skills have "functionally subsumed custom commands." Additionally, the Agent Skills open standard now makes skills portable across Claude Code, Cursor, Codex CLI, and others. The taxonomy needs updating to reflect that custom commands are effectively deprecated in favor of skills, and that agent-first CLIs (Concept 3's GWS coverage) are now a well-established fourth category.
- **Evidence**: [Anthropic Skills Docs](https://code.claude.com/docs/en/skills), [Agent Skills Open Standard](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- **Recommended update**: Add a note that skills have subsumed custom commands as of mid-2026. Update the taxonomy to a three-tier model: Skills (workflows + knowledge), MCP Servers (tool access), Agent-first CLIs (token-efficient tool invocation). Mention the open standard portability.

### c8f3a: Computer Use and Dispatch
- **Status**: Evolved
- **Original claim**: "Mac-only in the research preview, Pro plan only... unavailable on Teams/Enterprise plans."
- **Current state**: As of April 3, 2026, Computer Use expanded to Windows for Pro and Max subscribers. Dispatch is now documented as a production feature, not just a research preview. The curriculum describes it as Mac-only and research-preview -- this is now outdated.
- **Evidence**: [WinBuzzer coverage](https://winbuzzer.com/2026/04/04/anthropic-claude-desktop-control-windows-cowork-dispatch-xcxwbn/), [Anthropic blog](https://claude.com/blog/dispatch-and-computer-use)
- **Recommended update**: Update platform availability to include Windows. Note that Dispatch is now GA for Pro and Max subscribers. Remove "research preview" framing or note that it has graduated.

### c8d3d: AutoDream -- Background Memory Consolidation
- **Status**: Evolved
- **Original claim**: Describes AutoDream as "an unannounced Claude Code feature" with triggers that "appear to be" time-based and session-count-based.
- **Current state**: AutoDream is now publicly documented and in gradual rollout. The four-phase process is confirmed. One observed case consolidated 913 sessions in 8-9 minutes. A community-built `dream-skill` on GitHub replicates the functionality for users who don't have the feature yet. The speculative language in the curriculum can be replaced with confirmed details.
- **Evidence**: [Claude Code Dreams Guide](https://claudefa.st/blog/guide/mechanics/auto-dream), [Geeky Gadgets coverage](https://www.geeky-gadgets.com/claude-autodream-memory-files/), [dream-skill GitHub](https://github.com/grandamenium/dream-skill)
- **Recommended update**: Remove "unannounced" framing. Replace speculative "appear to be" language with confirmed trigger mechanics. Note the community dream-skill as an alternative for users without access.

### c9c: Skills as an Emerging Industry Standard
- **Status**: Evolved
- **Original claim**: Nate B Jones frames skills as "converging toward an industry-wide standard."
- **Current state**: This is no longer emerging -- it has happened. Anthropic published Agent Skills as an open specification (agentskills.io). OpenAI adopted the format for Codex CLI and ChatGPT. Google DeepMind adopted it. GitHub Copilot supports Agent Skills in VS Code. The same SKILL.md format works across Claude Code, Cursor, Gemini CLI, Codex CLI, and Antigravity IDE.
- **Evidence**: [Agent Skills Open Standard](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Anthropic Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), [MindStudio coverage](https://www.mindstudio.ai/blog/agent-skills-open-standard-claude-openai-google), [The New Stack](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/)
- **Recommended update**: Upgrade from "emerging" to "established." Document the cross-platform portability as a confirmed fact. This is arguably the most significant evolution in the entire module -- skills are now a durable, portable investment rather than a Claude-specific bet.

### c8f2: Worktree-Based Parallelization
- **Status**: Evolved
- **Original claim**: Describes worktrees as a workflow Pocock champions, with manual `claude --worktree` invocation.
- **Current state**: Worktrees are now deeply integrated into Claude Code's architecture. A built-in `/batch` skill decomposes tasks into 5-30 units and spawns agents in isolated worktrees automatically. Subagents can use `isolation: worktree` in frontmatter. Practitioner consensus is 3-5 parallel worktrees as the practical upper bound. The curriculum text focuses on Pocock's single-session usage; the current state is significantly more automated.
- **Evidence**: [Claude Code Common Workflows](https://code.claude.com/docs/en/common-workflows), [Steve Kinney Course](https://stevekinney.com/courses/ai-development/git-worktrees), [Multiple Medium articles]
- **Recommended update**: Add coverage of `/batch` skill and `isolation: worktree` subagent configuration. Update the practical guidance to include the 3-5 worktree upper bound.

### Hooks System (c9, c8d2, p6, p7)
- **Status**: Evolved
- **Original claim**: Curriculum references 13 Claude Code lifecycle hooks (from IndyDevDan's repository).
- **Current state**: The hooks system has expanded to 21 lifecycle events with 4 handler types, async execution, and JSON structured output. The core principle (deterministic enforcement via exit code 2) is unchanged and well-validated, but the scope has grown significantly.
- **Evidence**: [Claude Code Hooks Docs](https://code.claude.com/docs/en/hooks), [Multiple tutorials confirming 21 events]
- **Recommended update**: Update the hook count from 13 to 21 lifecycle events. Note the addition of async execution and JSON structured output capabilities.

### c4a: The Three-Level Skill Loading Model
- **Status**: Evolved
- **Original claim**: Mark Kashef's synthesis describes Level 1 (YAML frontmatter, "under 1,000 characters"), Level 2 (procedural instructions), Level 3 (linked files).
- **Current state**: The three-level model is confirmed by official documentation but with more precise numbers: Level 1 is ~100 tokens per skill (name max 64 chars, description max 1,024 chars); Level 2 is up to ~5,000 tokens; Level 3 has no practical limit. The curriculum text says "under 1,000 characters" for Level 1 which is approximately correct for the description alone but the total metadata cost is lower (~100 tokens including name).
- **Evidence**: [Towards Data Science: Claude Skills and Subagents](https://towardsdatascience.com/claude-skills-and-subagents-escaping-the-prompt-engineering-hamster-wheel/), [Official Skills Docs](https://code.claude.com/docs/en/skills)
- **Recommended update**: Add the precise token costs: ~100 tokens per skill at Level 1, up to ~5,000 tokens at Level 2. Note that hundreds of skills at Level 1 cost is negligible.

### c9a: Context Window Calibration
- **Status**: Evolved
- **Original claim**: Describes defaults calibrated for 200K context window era.
- **Current state**: 1M context is now GA for Opus 4.6 and Sonnet 4.6 at standard pricing (no premium). On Max, Team, and Enterprise plans, Opus auto-upgrades to 1M. Pro users opt in via `/extra-usage`. Older models (Sonnet 4.5, Sonnet 4) retain 200K. The 1M beta for older models is being retired April 30, 2026. The curriculum's guidance to adjust settings remains valid but the context has shifted from "hidden leverage" to standard configuration.
- **Evidence**: [Anthropic 1M GA blog](https://claude.com/blog/1m-context-ga), [Context Windows API docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- **Recommended update**: Update to reflect 1M GA status. Note the model-specific availability. The settings adjustments (autocompact at 75%, terminal output cap) are still valid recommendations.

### c1 (CLAUDE.md) -- instruction budget refinement
- **Status**: Evolved (nuance)
- **Original claim**: Matt Pocock (#152) cites "300-500 instructions" as the realistic budget.
- **Current state**: External sources now converge on a tighter range of 150-200 instructions before compliance drops off. The "under 200 lines" guidance appears in multiple independent sources and Anthropic's own best practices. The curriculum's 300-500 figure may be outdated or was always on the generous side.
- **Evidence**: [Anthropic Best Practices](https://code.claude.com/docs/en/best-practices), [Builder.io 50 Tips](https://www.builder.io/blog/claude-code-tips-best-practices)
- **Recommended update**: Consider tightening the instruction budget guidance from "300-500" to "150-200" based on current practitioner consensus, or note the range and recommend erring toward the lower end.

### c8a: The Creator's Perspective
- **Status**: Evolved
- **Original claim**: Boris Cherny's insights from Y Combinator interview (#103, dated 2026-01-15).
- **Current state**: The last supported date (2026-01-15) makes this the oldest emerging concept. Cherny's core insights remain valid (plan mode, build for future model, scaffolding as tech debt), but the specific product details have moved significantly. Claude Code has shipped worktrees, /batch, 21 hooks, Agent Skills open standard, AutoDream, and Computer Use since this interview. The "no part of Claude Code was around six months ago" quote is self-fulfilling -- the product described in January 2026 has already been significantly rewritten.
- **Evidence**: Internal -- the curriculum itself documents many features shipped after this interview.
- **Recommended update**: Add a note that Cherny's product-specific details (e.g., "plugins built by agent swarm over a weekend") are historical snapshots. His philosophical principles (latent demand, build for future model, scaffolding as tech debt) remain evergreen.

### p5: The Personal Vault as Context Infrastructure
- **Status**: Evolved (expansion)
- **Original claim**: Focuses on Obsidian vault with CLAUDE.md + memory.md.
- **Current state**: The pattern has expanded significantly with multiple vault architectures (EPARAX, EPARG, flat-folder + metadata), the Bases feature for property-driven navigation, and specialized use cases (plan-capture for ADHD, Chief of Staff agent). The curriculum already covers these but the pattern section could reference the newer architectural variants more prominently.
- **Recommended update**: Minor -- the curriculum's coverage via multiple Noah Vincent and Brad sources is comprehensive. Consider a brief note acknowledging the pattern's architectural diversity.

## Needs Update (7)

### c2: Skills as Lazy-Loaded Instructions
- **Status**: Needs update
- **Issue**: Strength score of 1.0 (emerging) is misleading for what is arguably the single most foundational concept in the module. The concept is well-explained and well-cited (IndyDevDan #015, Leon van Zyl #013) but the dashboard's keyword matching appears to undercount support. More critically, the concept now needs to reflect that skills follow the Agent Skills open standard and are portable across platforms -- this is no longer a Claude-specific architecture.
- **Evidence**: [Official Skills Docs](https://code.claude.com/docs/en/skills), [Taylor Daughtry blog](https://taylordaughtry.com/posts/claude-skills-are-lazy-loaded-context/)
- **Recommended action**: Add a sentence noting Agent Skills as an open standard. Verify dashboard keyword matching for this concept -- the 1.0 strength score for a concept supported by 90+ sources mapped to Module 03 suggests a scoring bug.

### c6: Token Efficiency and Context Budget Discipline
- **Status**: Needs update
- **Issue**: Strength 1.0 (emerging) despite being a foundational principle discussed across dozens of sources. The concept text itself is solid but brief -- it could benefit from incorporating the specific 1M context GA details and the updated CLAUDE.md size guidance (under 200 lines).
- **Recommended action**: Investigate dashboard scoring. Consider merging token efficiency concerns that are scattered across c6, c8e (60% rule), c8f2a (overhead), and c8f1a (symbol indexing) into a more cohesive narrative.

### c7: Research Workarounds and Fact-Checking Discipline
- **Status**: Needs update
- **Issue**: Strength 0 (emerging) with a single source (Simon Scrapes #051). The Gemini CLI fallback workaround may be outdated given Claude Code's expanded web capabilities. The fact-checking discipline pattern remains valid but needs more sources to justify its own concept.
- **Recommended action**: Verify whether the Gemini CLI research workaround is still necessary given Claude Code's current web access capabilities. Consider merging this into a broader "verification discipline" concept or demoting to a pattern.

### c8a2: The Setup Hook and Install Prompts
- **Status**: Needs update
- **Issue**: Strength 0 with a single source (IndyDevDan #064). The curriculum describes two lifecycle events (Init, Maintenance). The hooks system now has 21 lifecycle events including a proper Setup hook. The concept's core insight (deterministic scripts + agentic prompts) is valid but the specific hook details may be outdated.
- **Recommended action**: Update hook event details to match current 21-event system. Verify whether the Init/Maintenance distinction described in the curriculum maps to the current Setup hook semantics.

### pit2: Over-permissioning skills with allowed-tools
- **Status**: Needs update
- **Issue**: Strength 0, no supporting sources. The pitfall is valid and important but the curriculum text is generic ("expands the attack surface"). With Agent Skills now being an open standard used across platforms, the security implications of over-permissioning are amplified.
- **Recommended action**: Add specific examples from practitioner experience. Reference the allowed-tools scoping guidance from official docs.

### pit7: Confusing parallelism with productivity
- **Status**: Needs update
- **Issue**: Strength 0, no supporting sources beyond the Daily AI Show (#148). The UC Berkeley research citation is important but the pitfall could be strengthened with the worktree-era guidance (3-5 parallel worktrees as upper bound).
- **Recommended action**: Add the 3-5 worktree upper bound as a practical guideline. Consider referencing the Keyhole Software 15-20% productivity estimate as a reality check against "10x" claims.

### pit8: Ignoring the agent data destruction risk
- **Status**: Needs update
- **Issue**: Strength 0, single source (Nate B Jones #305). This is an important safety warning but the curriculum could benefit from the hooks-based mitigation pattern (PreToolUse blocking destructive commands via exit code 2).
- **Recommended action**: Cross-reference with the hooks patterns (p6, p7) and add specific mitigation guidance using PreToolUse hooks.

## Emerging -- Needs More Support (15)

### c4b: Encoding Domain Expertise in Skills (strength 0)
- **Status**: Emerging, insufficient support
- **Current support**: 0 sources in dashboard (but Tanmay Deshpande #090 is cited in curriculum text)
- **Recommendation**: Dashboard scoring issue. The concept is well-sourced in the curriculum but keywords may not match. Low priority for content changes.

### c5a: Domain-Specific Skill Examples (strength 0)
- **Status**: Emerging, insufficient support
- **Current support**: 0 sources (but Cole Medin #232 and Nate Herk #236 are cited)
- **Recommendation**: Dashboard scoring issue. The Excalidraw and Nano Banana examples are well-documented. Low priority.

### c7a: Step-by-Step Decomposition -- The Terence Tao Pattern (strength 0)
- **Status**: Emerging, single-source concept
- **Current support**: 0 in dashboard (Terence Tao #248 is cited)
- **Recommendation**: The concept is a valuable cross-domain illustration. Its single-source nature is inherent (it describes one person's experience). Consider whether it belongs here in Module 03 or would fit better in Module 02 (Prompting & Workflows) as a decomposition pattern.

### c8b3: CoWork for Beginners (strength 1.0)
- **Status**: Emerging
- **Current support**: 1 source (Eliot Prince #098, dated 2026-02-16)
- **Recommendation**: Watch for newer beginner-focused CoWork content. The February 2026 source may be outdated given CoWork's rapid feature evolution.

### c8d: Skill-to-Repeatable-Process Workflow (strength 0)
- **Status**: Emerging, insufficient support
- **Current support**: 0 in dashboard (Bart Slodyczka #067 is cited)
- **Recommendation**: The "do not write skills from scratch, run the process first" principle is reinforced by multiple other sources (Ben AI #158, Nate Herk #189, Dori Wilson #407). Dashboard likely failing to correlate. The principle is sound.

### c8d3c: Semantic Memory Systems with QMD (strength 1.0)
- **Status**: Emerging, niche
- **Current support**: 1 source (Artem Zhutov #238, dated 2026-02-11)
- **Recommendation**: QMD is a specific tool. Watch for whether it gets traction or is superseded by AutoDream's built-in consolidation. The semantic search principle is valid but the specific tooling may be ephemeral.

### c8f: The Four-Layer Browser Automation Architecture (strength 1.0)
- **Status**: Emerging
- **Current support**: 1 source (IndyDevDan #088, dated 2026-02-16)
- **Recommendation**: The four-layer pattern (skills/subagents/commands/justfiles) is an IndyDevDan-specific framework. The broader principle (layered abstraction for browser automation) is valid but this may be too architecture-specific for a single-source concept.

### c8f1a: Token Cost Reduction via Symbol Indexing (strength 0)
- **Status**: Emerging, single-tool concept
- **Current support**: 0 in dashboard (J. Gravelle #239 is cited)
- **Recommendation**: jCodeMunch is one tool among several approaching the same problem. The 5.5x-99.7x token reduction claim is compelling but single-source. Watch for independent benchmarks.

### c8f4: Terminal Companion Tooling (strength 1.0)
- **Status**: Emerging
- **Current support**: 1 source (StarMorph AI #168, dated 2026-02-22)
- **Recommendation**: LazyGit, btop, etc. are stable tools that complement Claude Code. The concept is valid but may not warrant its own section -- consider merging into a general "development environment" concept.

### c9b: Iterative Skill Practice and Handoff Patterns (strength 0)
- **Status**: Emerging, single-source
- **Current support**: 0 in dashboard (Dori Wilson #407 is cited)
- **Recommendation**: The handoff skill pattern is independently reinforced by the self-improving skills concept (c4a1b) and AutoDream (c8d3d). Watch for more practitioners adopting session-end learning capture.

### p6: Hooks for Deterministic CLI Enforcement (strength 1.0)
- **Status**: Emerging in dashboard, well-validated externally
- **Current support**: 1 source (Matt Pocock #157, dated 2026-02-25)
- **Recommendation**: This pattern is extensively documented in external tutorials and official docs. Dashboard undercount. The principle is now standard practice -- multiple tutorials demonstrate the pnpm/npm hook as a canonical example.

### p7: Hooks for Test-Driven Agent Workflows (strength 1.0)
- **Status**: Emerging
- **Current support**: 1 source (AI LABS #021, dated 2026-03-12)
- **Recommendation**: The TDD hook pattern is well-validated by the hooks ecosystem growth. Watch for more sources demonstrating this in production.

### pit1: Writing skill descriptions for humans (strength 1.0)
- **Status**: Emerging in dashboard, well-validated
- **Current support**: 1 source
- **Recommendation**: This pitfall is reinforced by official docs (description max 1,024 chars, keyword-rich for activation). Dashboard undercount likely.

### pit4: Installing skills from untrusted sources (strength 1.0, last 2026-02-09)
- **Status**: Emerging, aging
- **Current support**: 1 source (ThePrimeagen #017, dated 2026-02-09)
- **Recommendation**: The 36% vulnerability rate statistic from ThePrimeagen needs validation against current data, especially now that Agent Skills is an open standard with broader distribution channels.

### pit12: Treating skills as static after initial creation (strength 0)
- **Status**: Emerging, single-source
- **Current support**: 0 in dashboard (Dori Wilson #407 cited)
- **Recommendation**: The principle is reinforced by multiple sources covering self-improving skills (c4a1b, #270, #294). Dashboard correlation issue.

## Dashboard Scoring Anomalies

Several concepts show strength scores that are dramatically misaligned with their actual source support:

| Concept | Dashboard Strength | Likely Actual Support | Issue |
|---------|-------------------|----------------------|-------|
| c2: Skills as Lazy-Loaded Instructions | 1.0 | 50+ sources | Foundational concept referenced everywhere |
| c6: Token Efficiency | 1.0 | 30+ sources | Cross-cutting concern discussed in many sources |
| c8d2: Hooks Over CLAUDE.md Rules | 2.2 | 15+ sources | Well-validated pattern |
| p6: Hooks for CLI Enforcement | 1.0 | 10+ sources | Canonical example in official docs |

These suggest the dashboard's keyword-matching algorithm is too narrow for concepts with generic titles that are discussed using varied terminology across sources.

## Module Health Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Confirmed Evergreen | 42 | 55% |
| Evolved | 12 | 16% |
| Needs Update | 7 | 9% |
| Emerging (insufficient support) | 15 | 20% |

### Top 3 Urgent Updates

1. **c9c / c3: Skills as Industry Standard + Extension Taxonomy** -- Agent Skills is now an open standard adopted by OpenAI, Google, GitHub Copilot. This changes the module's core narrative from "Claude-specific architecture" to "industry-standard portable format." This is the single most impactful update needed.

2. **c8f3a: Computer Use and Dispatch** -- Platform availability expanded to Windows (April 3, 2026) and the feature has graduated from research preview. Curriculum text states "Mac-only" which is now incorrect.

3. **Hooks system (c9, c8d2, p6, p7)** -- The system expanded from 13 to 21 lifecycle events with async execution and JSON output. The 13-hook table in the curriculum is outdated.

### Top 3 Strongest Concepts

1. **c1: CLAUDE.md as the Project Brain** (190.5 strength, 127 sources, 75 creators) -- Massively validated across the ecosystem. External documentation convergence.

2. **c8f1b: Nested Multi-Agent Claude Code via Tmux** (196.5 strength, 131 sources) -- The controller-worker architecture pattern is extremely well-supported.

3. **ex5: Refactor CLAUDE.md with skills** (198.0 strength, 132 sources) -- Highest strength score in the entire module, confirming that the CLAUDE.md-to-skills migration is the most practiced exercise.
