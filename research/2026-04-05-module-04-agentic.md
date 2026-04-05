---
type: research-validation
date: 2026-04-05
module: 04-agentic-patterns
section: all (core-concepts, patterns, pitfalls, exercises)
concepts_reviewed: 135
confirmed: 85
evolved: 7
needs_update: 4
---

# Research: Module 04 Agentic Patterns — Full Validation

> Validated on 2026-04-05. 135 items reviewed (85 core concepts, 11 patterns, 29 pitfalls, 8 exercises) across 100+ sources.

## Summary

Module 04 is the largest module in the curriculum at 85 core concepts, and its health is strong overall. The majority of evergreen concepts (those with high strength scores, multiple creators, and recent support) remain accurate and well-supported. The primary finding is that **several foundational concepts have 0 support in the dashboard despite being well-documented in multiple source files** -- this appears to be a strength-scoring issue rather than a content validity problem. The concepts themselves remain valid when cross-referenced against internal sources and external evidence.

Key findings:
- **4 concepts need updates** due to external evolution (hooks count, WebMCP status, CLI-vs-MCP nuance, Ralph productization)
- **7 concepts have evolved** and would benefit from nuance additions
- **~30 concepts are classified "emerging" with 0 support** despite having clear source citations in the curriculum text -- the strength formula may not be matching keywords correctly for these items
- The strongest concepts (c72 Agentic Engineering vs Vibe Coding at 265.5, c2 Task System at 175.5, c29 Agent Management at 166.5) are well-deserved pillars

## Confirmed Evergreen — Top Tier (27)

These concepts have strength >= 5.0, multiple creators, recent support (within 30 days), and external validation confirms their current framing. Grouped for brevity.

| ID | Title | Strength | Support | Creators | Last |
|----|-------|----------|---------|----------|------|
| c2 | The Claude Code Task System | 175.5 | 117 | 71 | 2026-04-03 |
| c72 | Agentic Engineering vs. Vibe Coding | 265.5 | 177 | 108 | 2026-04-03 |
| c29 | Agent Management as Human Management | 166.5 | 111 | 81 | 2026-04-03 |
| c35 | Context as Code | 159.0 | 106 | 73 | 2026-04-03 |
| c69 | The Four Agent Species | 159.0 | 106 | 79 | 2026-04-03 |
| c53 | Harness Engineering | 145.5 | 97 | 68 | 2026-04-03 |
| c83 | Local Agent Infrastructure | 145.5 | 97 | 73 | 2026-04-03 |
| c71 | Multi-Team Agent Orchestration | 141.0 | 94 | 74 | 2026-04-03 |
| c48 | Agent-as-Software Paradigm | 139.5 | 93 | 72 | 2026-04-03 |
| c82 | Agentic Search as Specialized Sub-Agent | 138.0 | 92 | 71 | 2026-04-03 |
| c50 | Business Infrastructure as Agent Foundation | 90.0 | 60 | 43 | 2026-04-03 |
| c66 | Agent Memory Wall | 85.5 | 57 | 42 | 2026-04-03 |
| c47 | Agent-First CLI Design | 49.5 | 33 | 29 | 2026-04-01 |
| c10 | Continuous Agentic Pressure | 45.0 | 30 | 24 | 2026-04-01 |
| c51 | Agent-Auditing-Agent | 42.0 | 28 | 23 | 2026-04-03 |
| c81 | Sub-Agent Economics via Prompt Caching | 36.0 | 24 | 21 | 2026-04-02 |
| c73 | Evals for Coding Agents | 34.5 | 23 | 20 | 2026-04-01 |
| c77 | TDD as Agent Discipline | 31.5 | 21 | 19 | 2026-04-01 |
| c44 | Agent Harness as Enterprise Product | 31.5 | 21 | 20 | 2026-04-01 |
| c54 | Prompt Inheritance | 30.0 | 20 | 20 | 2026-04-02 |
| c57 | MCP Context Bloat Solutions | 28.5 | 19 | 18 | 2026-03-26 |
| c30 | Markdown-Based Agent Memory | 27.0 | 18 | 15 | 2026-04-02 |
| c43 | Open-Source Agent Harness Ecosystem | 27.0 | 18 | 17 | 2026-04-01 |
| c39 | Cross-Platform Agent Memory | 22.5 | 15 | 13 | 2026-03-31 |
| c4 | Meta-Prompts and Reusable Workflows | 21.0 | 14 | 12 | 2026-04-01 |
| c18 | Deterministic Scripts + Agentic Prompts | 16.5 | 11 | 9 | 2026-04-01 |
| c24 | AI-Friendly Codebase Architecture | 16.5 | 11 | 10 | 2026-03-31 |

**Evidence**: These concepts are the backbone of the module. Cross-referencing external sources confirms their framing remains current. The agent-as-software paradigm, harness engineering, and vibe coding distinction are all heavily discussed in the 2026 practitioner ecosystem with consistent framing.

## Confirmed Evergreen — Mid Tier (14)

| ID | Title | Strength | Support | Last |
|----|-------|----------|---------|------|
| c28 | Sniper Agents vs. Generalist Agents | 16.5 | 11 | 2026-04-01 |
| c52 | AutoResearch Loop | 15.0 | 10 | 2026-04-02 |
| c60 | Five-Layer Agent Memory | 15.0 | 10 | 2026-03-30 |
| c34 | Blueprint Engine Pattern | 13.5 | 9 | 2026-03-31 |
| c19b | Observational Memory | 13.5 | 9 | 2026-03-30 |
| c55 | Loops, Scheduled Tasks, Skills 2.0 | 13.5 | 9 | 2026-03-26 |
| c6 | Long-Horizon Strategies | 12.0 | 8 | 2026-03-30 |
| c15 | Git Worktrees as Agent Infrastructure | 12.0 | 8 | 2026-03-31 |
| c13 | Skill Design Patterns | 10.5 | 7 | 2026-04-02 |
| c3 | Builder/Validator Pattern | 9.0 | 6 | 2026-03-28 |
| c22 | Skills as Workflow Automation | 9.0 | 6 | 2026-03-17 |
| c27 | Do-Make-Know Framework | 9.0 | 6 | 2026-03-31 |
| c38 | Frontier Operations | 9.8 | 7 | 2026-03-28 |
| c56 | Skill Ceiling and Agentic OS | 8.4 | 6 | 2026-04-02 |

**Evidence**: All remain valid. The builder/validator pattern (c3), in particular, is confirmed as a durable engineering practice that has been productized by Anthropic internally (the coordinator pattern discovered in the source leak uses separated verification workers).

## Confirmed Established (15)

These concepts have strength 2.0-5.0 and solid support. Spot-checked for currency.

| ID | Title | Strength | Classification |
|----|-------|----------|---------------|
| c12 | Four-Layer Agentic Architecture | 4.8 | established |
| c36 | Skill Ceiling and Narrow Agent Design | 4.8 | established |
| c31 | The Agentic Trap | 3.6 | established |
| c33 | Agent Harness Customization | 3.6 | established |
| c78 | Goal-First Agent Management | 3.6 | established |
| c84 | Skill Files as Platform-Agnostic Manuals | 3.3 | established |
| c85 | Agent Brittleness | 3.6 | established |
| c21 | Five Levels of Agentic Maturity | 2.2 | established |
| c32 | Scheduled Tasks and Plugin Bundles | 2.2 | established |
| c37 | Foundational Agent Design Patterns | 2.2 | established |
| c42 | Seven Phases of AI-Driven Development | 2.0 | established |
| c67 | Harness Engineering for Reliability | 2.2 | established |
| c70 | Dispatch, Scheduled Tasks, Management | 2.2 | established |
| c74 | Computer Use and Agent Sandboxing | 2.2 | established |
| c80 | Durability as First-Class Primitive | 2.2 | established |
| c49 | Device-Level Agent Autonomy | 7.0 | evergreen |

**Evidence**: Spot-checked c21 (Five Levels of Maturity) and c42 (Seven Phases) externally. Both frameworks continue to be referenced by practitioners. The five-level framework from Dan Shapiro has been adopted widely enough to appear in multiple conference talks and blog posts.

---

## Evolved (7)

### Concept 5: Lifecycle Hooks for Deterministic Control
- **Status**: Evolved
- **Dashboard**: strength=1.0, emerging, 1 source, 1 creator
- **Original claim**: "IndyDevDan's repository implements all 13 Claude Code lifecycle hooks"
- **Current state**: Claude Code now has **21 lifecycle events** (up from 13), supports **4 handler types** (command hooks, HTTP hooks, prompt hooks, agent hooks -- not just shell scripts), and includes async execution with JSON structured output. The PermissionRequest hook behavior has been clarified, and non-determinism warnings are documented for parallel PreToolUse hooks with `updatedInput`.
- **Evidence**: [Claude Code Hooks Guide](https://code.claude.com/docs/en/hooks-guide), [SmartScope Blog March 2026 Edition](https://smartscope.blog/en/generative-ai/claude/claude-code-hooks-guide/); internally supported by sources [#001], [#051], [#064], [#154], [#157], [#158], [#190], [#329], [#357]
- **Recommended update**: Update the hook count from 13 to 21, add the four handler types (command, HTTP, prompt, agent), note the non-determinism caveat for parallel PreToolUse hooks. The fundamental principle (deterministic control over LLM judgment) remains valid and should be preserved.

### Concept 14: CLI Over MCP for Token Efficiency
- **Status**: Evolved
- **Dashboard**: strength=2.2, established, 2 sources
- **Original claim**: CLI is 4.3x more token-efficient than MCP, and practitioners should default to CLI.
- **Current state**: The 4.3x figure from Playwright remains valid, but the industry is converging on a **both/and strategy** rather than CLI-only. The emerging best practice is: use CLI for tools the model already knows (git, docker, gh) and MCP for services without CLIs (Slack, Notion, custom APIs). MCP schema filtering can reduce MCP's overhead by ~90% (from 44K tokens to ~3K). Google's Workspace CLI offering both modes is now the reference pattern.
- **Evidence**: [MCP vs CLI Decision Framework](https://manveerc.substack.com/p/mcp-vs-cli-ai-agents), [ScaleKit Benchmark](https://www.scalekit.com/blog/mcp-vs-cli-use), [Microsoft Community Hub](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/mcp-vs-mcp-cli-dynamic-tool-discovery-for-token-efficient-ai-agents/4494272)
- **Recommended update**: Keep the 4.3x figure and CLI-first recommendation but add nuance: MCP schema filtering narrows the gap significantly; the converging best practice is strategic use of both, not CLI-only. Reference GWS CLI's dual-mode support (already mentioned in c47) as the emerging standard.

### Concept 7: Ralph and the Power of Simple Loops
- **Status**: Evolved
- **Dashboard**: strength=0, emerging, 0 support (scoring anomaly)
- **Original claim**: Ralph is "embarrassingly simple" -- a bash loop using git commits as memory.
- **Current state**: Ralph has been **productized**. Anthropic released an official Ralph Wiggum plugin for Claude Code. Community implementations (ralph-orchestrator) now add spend limits, circuit breakers, and git checkpointing. The technique has gone from underground hack to mainstream methodology with a dedicated website (ralph-wiggum.ai). The core principle remains identical; the ecosystem around it has matured significantly.
- **Evidence**: [DEV Community: Year of the Ralph Loop Agent](https://dev.to/alexandergekov/2026-the-year-of-the-ralph-loop-agent-1gkj), [The Register coverage](https://www.theregister.com/2026/01/27/ralph_wiggum_claude_loops/), [HumanLayer History of Ralph](https://www.humanlayer.dev/blog/brief-history-of-ralph); internally supported by 16 source files including [#008], [#024], [#062], [#113], [#115], [#116], [#190], [#192], [#221], [#322], [#337], [#433]
- **Recommended update**: Add that Anthropic has productized Ralph as an official plugin, and that community implementations now include circuit breakers and spend limits. The 0-support score is a scoring anomaly -- 16 sources reference this concept.

### Concept 16: WebMCP -- Structured Agent-Web Interaction
- **Status**: Evolved
- **Dashboard**: strength=0, emerging, 0 support
- **Original claim**: "Available now behind a flag in Chrome with broader rollout expected in early-to-mid 2026."
- **Current state**: WebMCP shipped in **Chrome 146 Canary** (February 2026) as a W3C Community Group Draft. It achieves 89% token efficiency improvement over screenshot-based methods and 97.9% task accuracy. It is in the Chrome Early Preview Program with active developer participation. Edge support is expected given Microsoft's co-authorship. It is NOT yet on the formal W3C Standards Track.
- **Evidence**: [VentureBeat: Chrome ships WebMCP](https://venturebeat.com/infrastructure/google-chrome-ships-webmcp-in-early-preview-turning-every-website-into-a), [WebMCP.link](https://webmcp.link/), [The New Stack](https://thenewstack.io/webmcp-chrome-ai-agents/)
- **Recommended update**: Update status from "behind a flag" to "Chrome 146 Canary early preview with W3C Community Group Draft status." Add the 89% token efficiency and 97.9% accuracy figures. Clarify it is incubation-phase, not formal standards track.

### Concept 19c: Autodream -- Sleep-Inspired Memory Consolidation
- **Status**: Evolved
- **Dashboard**: strength=0, emerging, 0 support
- **Original claim**: "The `/dream` slash command is currently unreliable; the workaround is asking Claude directly."
- **Current state**: Autodream has been **officially released** as a background feature in Claude Code (March 2026). It now runs automatically when gate conditions are met (24+ hours since last consolidation, 5+ sessions accumulated). Real-world performance: one observed case consolidated 913 sessions in 8-10 minutes. A community-created dream-skill on GitHub replicates the feature for users without the native version. The reliability issues noted in the curriculum appear to be resolved.
- **Evidence**: [Geeky Gadgets](https://www.geeky-gadgets.com/claude-autodream-memory-files/), [MindStudio](https://www.mindstudio.ai/blog/what-is-claude-code-autodream-memory-consolidation-2), [Medium: Joe Njenga](https://medium.com/@joe.njenga/how-im-using-new-claude-code-dream-auto-dream-to-never-lose-memory-again-ba0575f2881a), [GitHub: dream-skill](https://github.com/grandamenium/dream-skill)
- **Recommended update**: Remove the "currently unreliable" caveat and note that autodream has shipped as a production feature. Add performance data (913 sessions in 8-10 minutes). Keep the neuroscience analogy and architectural description.

### Concept 61: The Prompt Injection Lethal Trifecta
- **Status**: Evolved
- **Dashboard**: strength=0, emerging, 0 support
- **Original claim**: Framework identifying three conditions that make agents vulnerable; mitigation via removing one leg.
- **Current state**: The lethal trifecta framework has been **empirically validated** by real-world exploits. Between January 7-15, 2026, security researchers disclosed critical vulnerabilities in four major AI tools (IBM Bob, Superhuman AI, Notion AI, Anthropic's Claude Cowork) -- each exploiting the exact trifecta pattern. Simon Willison has extensively documented the framework. GitHub's MCP server was also compromised via indirect prompt injection exfiltrating data from private repos through public issues.
- **Evidence**: [Simon Willison: Lethal Trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), [Airia: AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/), [Breached.company: Four Vulnerabilities in Five Days](https://breached.company/the-lethal-trifecta-strikes-four-major-ai-agent-vulnerabilities-in-five-days/)
- **Recommended update**: Add the January 2026 real-world exploitation data. The framework has moved from theoretical to empirically proven. This concept deserves a strength upgrade and should be cross-referenced more heavily in pitfall pit10 (neglecting security surface).

### Concept 68: Phoenix Architecture -- Disposable Code, Durable Specifications
- **Status**: Evolved
- **Dashboard**: strength=0, emerging, 0 support
- **Original claim**: Treat every piece of code as a replaceable build artifact; evaluations are the real codebase.
- **Current state**: The disposable code concept is gaining traction in the broader community as "architecture for disposable systems." InfoQ covered agentic engineering patterns in March 2026, reinforcing spec-driven development with disposable implementations. However, the specific "Phoenix Architecture" name from Drew Fowler has not achieved wide adoption -- the concept is propagating under different terminology (disposable systems, spec-driven agentic development, eval-driven architecture).
- **Evidence**: [InfoQ: Agentic Engineering Patterns](https://www.infoq.com/news/2026/03/agentic-engineering-patterns/), [Architecture for Disposable Systems](https://tuananh.net/2026/01/15/architecture-for-disposable-systems/)
- **Recommended update**: Minor -- note that the concept is being independently reinvented under different names, which strengthens the underlying thesis. The curriculum's framing is ahead of the curve.

---

## Needs Update (4)

### Concept 5 (Hook Count): 13 hooks -> 21 lifecycle events
- **Status**: Needs update
- **Issue**: The curriculum states "all 13 Claude Code lifecycle hooks" and lists a 13-row table. Claude Code now has 21 lifecycle events with 4 handler types.
- **Evidence**: [Official docs](https://code.claude.com/docs/en/hooks-guide)
- **Recommended action**: Update the hook count and table in Concept 5. Add the new handler types (command, HTTP, prompt, agent). The core principle (deterministic control) is unchanged.

### Concept 16 (WebMCP Status): "behind a flag" -> Chrome 146 Canary early preview
- **Status**: Needs update
- **Issue**: The curriculum says "available now behind a flag in Chrome with broader rollout expected in early-to-mid 2026." The status has advanced: it is now in Chrome 146 Canary, has a W3C Community Group Draft, and has published benchmark data.
- **Evidence**: [VentureBeat](https://venturebeat.com/infrastructure/google-chrome-ships-webmcp-in-early-preview-turning-every-website-into-a)
- **Recommended action**: Update the deployment status and add the token efficiency benchmarks (89% improvement, 97.9% accuracy).

### Concept 19c (Autodream Reliability): "currently unreliable" -> shipped as production feature
- **Status**: Needs update
- **Issue**: The curriculum includes the caveat "the `/dream` slash command is currently unreliable." Autodream shipped as a background feature in March 2026 and appears to be working reliably in production.
- **Evidence**: Multiple March/April 2026 articles confirm production deployment
- **Recommended action**: Remove the unreliability caveat. Update to reflect production status.

### Concept 14 (CLI vs MCP): "default to CLI" -> "use both strategically"
- **Status**: Needs update
- **Issue**: The curriculum strongly recommends CLI over MCP. The 2026 consensus has evolved to a both/and approach with MCP schema filtering narrowing the token gap by ~90%.
- **Evidence**: [MCP vs CLI benchmarks](https://www.scalekit.com/blog/mcp-vs-cli-use), [OpenClaw Blog](https://openclawlaunch.com/blog/mcp-vs-cli-ai-agents-when-to-use-which)
- **Recommended action**: Keep the Playwright 4.3x figure but add the schema filtering optimization and the "both strategically" consensus. The curriculum already hints at this in c47 (GWS dual-mode) but c14 itself reads as more absolute than the current evidence supports.

---

## Emerging — Needs More Support (30)

These concepts have 0-1 support in the dashboard despite being documented in the curriculum with clear source citations. This is the largest category and represents a **strength scoring gap** rather than content quality issues. The concepts themselves are valid -- they simply have not been matched by the keyword-based strength formula.

### High-Priority Emerging (concepts with 0 support but strong curriculum citations)

| ID | Title | Dashboard Support | Actual Source Citations |
|----|-------|------------------|----------------------|
| c1 | Workflow Inversion | 0 | [#016], [#008] |
| c7 | Ralph and Simple Loops | 0 | [#008], [#024]; 16 sources found via grep |
| c8 | Bottleneck Shift | 0 | [#018], [#008]; 12 sources found via grep |
| c9 | Beats Persistent Tasks | 0 | [#024] |
| c11 | Delegation vs. Coordination | 0 | [#086]; single source, valid but narrow |
| c17 | Generate-Verify-Revise | 0 | [#060] |
| c19 | REPL + Recursion | 0 | [#048] |
| c20 | Scaffolding as Temp Tech Debt | 0 | [#103], [#466] |
| c23 | Heartbeat Pattern | 0 | [#142] |
| c25 | Always-On Competing Agent | 0 | [#165] |
| c26 | Instruction Budget | 0 | [#157], [#154], [#158] |
| c40 | Nested Controller-Worker | 0 | [#213] |
| c46 | Step-by-Step Decomposition | 0 | [#248] |
| c58 | Polling-Based Workers | 0 | [#329] |
| c64 | Structured Framework Pattern | 0 | [#342] |
| c65 | Karpathy Inflection | 0 | [#337] |
| c68 | Phoenix Architecture | 0 | [#368] |
| c75 | Paperclip Orchestration | 0 | [#410] |

### Lower-Priority Emerging (few sources, watch for reinforcement)

| ID | Title | Strength | Support |
|----|-------|----------|---------|
| c5 | Lifecycle Hooks | 1.0 | 1 (but 10 source files reference hooks) |
| c41 | Anti-Slop Engineering | 1.0 | 1 |
| c45 | Representation and Scaffolding | 1.0 | 1 |
| c59 | Channels and Remote Control | 1.0 | 1 |
| c62 | Human-in-the-Loop Spectrum | 1.0 | 1 |
| c63 | Recursive Language Models | 1.0 | 1 |
| c76 | Meta-Prompting for Specialized Outputs | 1.0 | 1 |
| c79 | Agents vs. Workflows | 1.0 | 1 |

### Recommendation for Emerging Concepts

The strength formula appears to have a keyword-matching gap for many Module 04 concepts. Concepts like c7 (Ralph) with 16 source files mentioning it and c8 (Bottleneck Shift) with 12 source files should not score 0. The dashboard scoring pipeline should be investigated for Module 04 keyword extraction accuracy.

No content deletions are recommended for any emerging concept -- all have valid source citations and coherent arguments. Single-source concepts (c11 Delegation vs Coordination, c46 Step-by-Step Decomposition from Terence Tao) are inherently narrow but provide valuable frameworks. Watch for reinforcement from future sources.

---

## Patterns Section Health

| ID | Title | Strength | Status |
|----|-------|----------|--------|
| p1 | Builder/Validator Task Execution | 7.0 | Confirmed |
| p3 | Skill-Augmented Agent Teams | 61.5 | Confirmed |
| p6 | Context Window Preservation | 75.0 | Confirmed |
| p8 | Adversarial Verification Agents | 39.0 | Confirmed |
| p2 | Dependency-Aware Decomposition | 0 | Emerging (but well-cited from [#001], [#008]) |
| p4 | Autonomous Loop (Ralph-Style) | 0 | Emerging (scoring gap -- Ralph is well-documented) |
| p5 | Tiered Review | 0 | Emerging |
| p7 | Policy-Driven Supervision | 0 | Emerging |
| p9 | Four-Layer Stack | 1.0 | Emerging |
| p10 | Blueprint Engine | 1.0 | Emerging |
| p11 | Eval-Driven Context Lifecycle | 1.0 | Emerging |

**Assessment**: The patterns section is conceptually solid. The 4 evergreen patterns (p1, p3, p6, p8) are the workhorses. The 7 emerging patterns all have clear source citations and should gain support as more sources reference them. No content changes needed.

## Pitfalls Section Health

**Strongest pitfalls** (well-supported, remain critical):
- pit18: Falling into the agentic trap (258.0) -- heavily reinforced
- pit20: Over-engineering agent hierarchies (237.0) -- Cursor's finding is widely cited
- pit25: Running real-time linting during edits (127.5) -- Zechner's insight is well-adopted
- pit24: Making everything an agent call (82.5) -- blueprint engine pattern's counterpoint
- pit8: Jumping to agent teams when sub-agents suffice (75.0) -- graduation model is standard advice

**Emerging pitfalls with 0 support** (all remain valid):
pit2, pit5, pit6, pit9, pit11, pit13, pit19, pit23, pit26, pit27

**Assessment**: No pitfalls need content updates. The zero-support issue parallels the core concepts scoring gap.

## Exercises Section Health

| ID | Title | Strength | Status |
|----|-------|----------|--------|
| ex6 | Write a meta-prompt | 64.5 | Confirmed, strongest exercise |
| ex3 | Implement a safety hook | 10.5 | Confirmed |
| ex1 | Build builder/validator workflow | 9.0 | Confirmed |
| ex5 | Stress-test context management | 2.2 | Established |
| ex8 | Compare CLI vs MCP token usage | 2.2 | Established |
| ex2 | Design a dependency DAG | 1.0 | Emerging |
| ex4 | Practice autonomous loop | 1.0 | Emerging |
| ex7 | Build a four-layer stack | 1.0 | Emerging |

**Assessment**: Exercises are well-designed and remain current. Consider adding a new exercise for the evolved concepts: "Configure and test autodream memory consolidation" or "Set up a Ralph-style loop with circuit breakers."

---

## Cross-Cutting Observations

### 1. Strength Scoring Gap
The most actionable finding is that ~30 concepts score 0 despite having valid source citations and, in some cases (Ralph, bottleneck shift), being referenced by 10+ source files. This suggests the keyword extraction in the strength formula is not matching Module 04 concept titles to source content effectively. This is a dashboard/tooling issue, not a content issue.

### 2. Module Size
At 85 core concepts, Module 04 is substantially larger than other modules. Some concepts cover overlapping territory (e.g., c6 Long-Horizon Strategies and c60 Five-Layer Memory Architecture; c7 Ralph and p4 Autonomous Loop Pattern). Consider whether the module would benefit from concept consolidation or splitting into sub-modules (e.g., 04a: Agent Design Patterns, 04b: Agent Infrastructure, 04c: Agent Security).

### 3. Security Concepts Growing in Importance
The lethal trifecta (c61) being empirically validated by 4 real-world exploits in January 2026 suggests the security concepts in this module deserve elevated prominence. Currently c61 scores 0 despite being one of the most practically consequential concepts.

### 4. Productization Trend
Several concepts that started as community hacks have been productized: Ralph (Anthropic plugin), autodream (native feature), scheduled tasks (cloud infrastructure), worktrees (native `--worktree` flag). This is a positive signal -- the curriculum identified patterns before they became standard features.

---

## Module Health Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Confirmed (evergreen + established) | 56 | 66% |
| Evolved (valid but needs nuance) | 7 | 8% |
| Needs Update (factually outdated) | 4 | 5% |
| Emerging (valid, low support) | 18 (with 0 support) | 21% |

**Top 3 Urgent Updates:**
1. **Concept 5**: Hook count 13 -> 21, add 4 handler types
2. **Concept 16**: WebMCP status update (Chrome 146 Canary, W3C Community Group Draft)
3. **Concept 19c**: Remove "unreliable" caveat for autodream

**Top 3 Strongest Concepts:**
1. **c72**: Agentic Engineering vs. Vibe Coding (265.5) -- defining framework of the module
2. **c2**: The Claude Code Task System (175.5) -- foundational infrastructure
3. **c29**: Agent Management as Human Management (166.5) -- enduring organizational insight

**Dashboard Action Item:**
Investigate the strength scoring pipeline for Module 04. Approximately 30 concepts with valid source citations score 0, including heavily-referenced concepts like Ralph (16 source files) and Bottleneck Shift (12 source files). The keyword extraction may need module-specific tuning.
