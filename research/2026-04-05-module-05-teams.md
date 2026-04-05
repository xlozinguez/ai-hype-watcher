---
type: research-validation
date: 2026-04-05
module: 05-team-orchestration
section: all (core-concepts, patterns, pitfalls, exercises)
concepts_reviewed: 47
confirmed: 20
evolved: 7
needs_update: 4
emerging_insufficient: 16
---

# Research: Module 05 Team Orchestration — Full Validation

> Validated on 2026-04-05. 47 concepts reviewed across 80+ sources. All sections covered: core concepts (53 items), patterns (6), pitfalls (22), exercises (5).

## Summary

Module 05 is the largest and most actively growing module in the curriculum. Its **evergreen core is strong** -- the foundational architecture (sub-agents vs. agent teams, observability, context engineering through delegation, empirical measurement) is well-supported by 60-80+ sources each with high creator diversity and recent citations through April 2026. Anthropic's official documentation confirms the shared task list, peer-to-peer messaging, and team architecture as described.

However, **the dashboard strength scores are misleading for many concepts**. Seven core concepts (C2, C3, C4, C9, C10, C12, C13) and many patterns/pitfalls show 0 support and "emerging" classification despite having 3-17 matching source files in internal search. This appears to be a keyword-matching gap in the strength formula rather than a genuine support deficit. These concepts are well-supported by their cited sources and confirmed by external evidence.

**Key evolution areas**: (1) Tiered model selection per teammate is NOT yet supported in official agent teams -- the curriculum's claim needs nuance; (2) Coordinator mode has been extensively analyzed via the source code leak and is confirmed as a real internal pattern; (3) Harness engineering has emerged as a recognized discipline with Martin Fowler coverage and an arxiv paper; (4) Git worktrees are confirmed as the standard isolation mechanism but need a note about runtime isolation gaps (ports, databases, caches).

**Top risks**: The module's growth to 53 concepts in core-concepts alone risks information overload. Several concepts (C14-C53) were added from recent sources and may benefit from consolidation.

## Confirmed Evergreen (20)

### C1: Sub-Agents vs. Agent Teams -- Two Architectures for Parallel Work
- **Status**: Confirmed
- **Support**: 62 sources, 48 creators, latest 2026-04-02 (strength: 93.0)
- **Evidence**: Anthropic's official documentation at [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) confirms the exact architecture described: shared task list, peer-to-peer messaging, independent context windows. The comparison table in the curriculum matches the official docs. Simon Scrapes' 2/6/8 heuristic and Van Zyl's room analogy remain accurate and widely referenced.

### C6: Infrastructure for Multi-Agent Execution
- **Status**: Confirmed
- **Support**: 80 sources, 63 creators, latest 2026-04-02 (strength: 120.0)
- **Evidence**: Official docs confirm tmux/iTerm2 for split-pane mode, in-process mode as default, and the `teammateMode` setting. E2B sandboxes, dedicated devices (Mac Mini pattern from IndyDevDan), and Q1 2026 features (Remote Control, Dispatch, Channels) all externally confirmed.

### C7: Multi-Agent Observability
- **Status**: Confirmed
- **Support**: 82 sources, 63 creators, latest 2026-04-02 (strength: 123.0)
- **Evidence**: Official docs now include `TeammateIdle`, `TaskCreated`, and `TaskCompleted` hooks as enforcement mechanisms for quality gates. IndyDevDan's observability system is still referenced in the community. Martin Fowler's harness engineering article confirms observability as foundational: "our most difficult challenges now center on designing environments, feedback loops, and control systems."

### C8: Context Engineering Through Delegation
- **Status**: Confirmed
- **Support**: 33 sources, 27 creators, latest 2026-04-01 (strength: 49.5)
- **Evidence**: The delegation-as-context-strategy framing is reinforced by LangChain's four-category context engineering taxonomy (#285) and the official docs confirming each teammate gets its own context window. The 31% orchestrator context usage figure from IndyDevDan remains a useful reference point.

### C11: Empirical Multi-Agent Measurement
- **Status**: Confirmed
- **Support**: 80 sources, 63 creators, latest 2026-04-02 (strength: 120.0)
- **Evidence**: Google Research's "Towards a Science of Scaling Agent Systems" paper has been extensively cited externally. [InfoQ coverage](https://www.infoq.com/news/2026/02/google-agent-scaling-principles/) and [Towards Data Science analysis](https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/) confirm: independent multi-agent systems amplify errors by 17.2x; centralized systems contain this to 4.4x. The coordination collapse finding at 5-10 agents is replicated across 180 experiments spanning three LLM families.

### C12a: Non-Technical Multi-Agent Patterns
- **Status**: Confirmed
- **Support**: 81 sources, 63 creators, latest 2026-04-02 (strength: 121.5)
- **Evidence**: The Krakowski/OpenClaw pattern continues to be referenced as the canonical example of non-developer multi-agent adoption.

### C5: Individual Agent Autonomy and Human Interaction
- **Status**: Confirmed
- **Support**: 2 sources, 2 creators, latest 2026-03-02 (strength: 2.2)
- **Evidence**: Official docs confirm: Shift+Down to cycle teammates, Escape to interrupt, in-process and split-pane modes. The granular control pattern (pause one agent, redirect, inject skills) is operational as described.

### Pit4: Skipping team cleanup
- **Status**: Confirmed (strength: 9.0, evergreen)
- **Evidence**: Official docs explicitly warn: "Always use the lead to clean up. Teammates should not run cleanup."

### Pit5: Using branches instead of worktrees
- **Status**: Confirmed (strength: 9.0, evergreen)
- **Evidence**: Multiple external sources confirm git worktrees as the standard isolation mechanism. Anthropic's 78% multi-file edit rate in Q1 2026 makes this more critical than ever.

### Pit13: Neglecting codebase readiness
- **Status**: Confirmed (strength: 120.0, evergreen)
- **Evidence**: Martin Fowler's harness engineering article and Eric's Stanford course both confirm: agent teams amplify codebase quality problems.

### Pit16: Confusing agent species
- **Status**: Confirmed (strength: 123.0, evergreen)
- **Evidence**: Jones's four-species taxonomy is externally validated and widely cited.

### P5: Adversarial Research Teams
- **Status**: Confirmed (strength: 75.0, evergreen)
- **Evidence**: Official docs now include "Investigating with competing hypotheses" as a first-class use case example, validating the pattern.

### P6: Baseline-First Multi-Agent Evaluation
- **Status**: Confirmed (strength: 120.0, evergreen)
- **Evidence**: Google Research paper and multiple external analyses confirm: always establish single-agent baseline before multi-agent deployment.

### Ex1: Sub-agent vs. team comparison
- **Status**: Confirmed (strength: 7.0, evergreen)
- **Evidence**: Remains a valid pedagogical exercise. Official docs provide clear comparison criteria.

### Ex3: Tmux multi-agent setup
- **Status**: Confirmed (strength: 120.0, evergreen)
- **Evidence**: Official docs confirm tmux as primary split-pane tool with detailed setup instructions.

### Ex5: Context budget analysis
- **Status**: Confirmed (strength: 54.0, evergreen)
- **Evidence**: The delegation-preserves-context principle is well-established across sources.

### Pit1: Using teams for simple tasks
- **Status**: Confirmed (strength: 2.2, established)
- **Evidence**: Official docs state: "Agent teams add coordination overhead and use significantly more tokens than a single session."

### Pit15: Relying on prompts alone for multi-step reliability
- **Status**: Confirmed (strength: 3.6, established)
- **Evidence**: Karpathy's "march of nines" framing now widely cited. Martin Fowler article and arxiv paper [2603.05344] both confirm harness engineering as the discipline addressing this.

### Pit22: Skipping single-agent reliability before scaling
- **Status**: Confirmed (strength: 3.6, established)
- **Evidence**: Horthy's scaling sequence confirmed by external sources and community consensus.

### Pit18: Designing skills for human callers when agents are primary users
- **Status**: Confirmed (strength: 4.4, established)
- **Evidence**: Cross-platform skill convergence (Anthropic, Microsoft, OpenAI) validates agent-first design requirement.

## Evolved (7)

### C9: Agent Isolation with Git Worktrees
- **Status**: Evolved
- **Original claim**: Git worktrees provide filesystem isolation; `claude --worktree` simplifies setup; worktrees branch from current branch (Pocock gotcha).
- **Current state**: The core claim remains accurate, but external evidence reveals an important gap: **git worktrees provide filesystem isolation but NOT runtime isolation**. As [Penligent](https://www.penligent.ai/hackinglabs/git-worktrees-need-runtime-isolation-for-parallel-ai-agent-development/) documents, worktrees do not isolate ports, databases, caches, secrets, or test state. One task's runtime can trample another task's resources. Additionally, Anthropic data shows worktree creation in a 20-minute session with a ~2GB codebase used 9.82 GB of disk space, making disk usage a practical concern at scale. Official docs now include a [dedicated worktree section](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees).
- **Internal support**: 17 sources reference worktrees including #137, #021, #027, #101, #220, #329
- **Recommended update**: Add a paragraph noting that worktrees solve filesystem isolation but not runtime isolation (ports, databases, caches). For full isolation, combine worktrees with container-based sandboxing (E2B, Docker) or dedicated devices.

### C12: The Three Modes Mental Model (Default / Sub-Agent / Teams)
- **Status**: Evolved
- **Original claim**: Three modes (default, sub-agent, agent teams) represent the session architecture progression. From Bart Slodyczka #067.
- **Current state**: The three-mode framework remains valid as a pedagogical model, but the official docs now introduce a fourth operational dimension: **display modes** (in-process vs. split-pane) that are orthogonal to the session architecture. Additionally, the official docs describe a subtler graduation path: subagents for focused tasks where only the result matters, agent teams for complex work requiring discussion and collaboration. The boundary is not about scale but about whether workers need to communicate. The curriculum's framing of "managing finite context windows" as the primary driver is accurate but incomplete -- the communication topology is equally important.
- **Internal support**: 3 sources match (#067, #135, #230)
- **Recommended update**: Note the in-process vs. split-pane display mode distinction as a separate operational axis. Emphasize the communication-need criterion (do workers need to talk to each other?) alongside the context management framing.

### Pattern 4: Tiered Model Selection
- **Status**: Evolved -- partially incorrect
- **Original claim**: "The team leader can specify cheaper models (e.g., Sonnet) for simpler tasks while reserving Opus for complex reasoning, optimizing cost without sacrificing quality where it matters." (From C12, Bart's walkthrough, and IndyDevDan's demo.)
- **Current state**: **Tiered model selection per teammate is NOT officially supported in Agent Teams as of April 2026.** The official docs confirm you can specify a model when spawning teammates ("Use Sonnet for each teammate"), but this applies uniformly -- you cannot mix Opus and Sonnet within the same team through the native agent teams feature. The curriculum's claim about IndyDevDan using "eight Haiku agents for summarization" and "four Opus agents for deployment" involved separate team sessions, not mixed models within one team. Per-teammate model selection is an actively requested community feature.
- **Internal support**: 1 source, 1 creator (strength: 1.0, emerging)
- **Evidence**: [Official docs](https://code.claude.com/docs/en/agent-teams), [community discussion](https://www.morphllm.com/claude-code-agent-teams)
- **Recommended update**: Clarify that tiered model selection currently works across separate team sessions (cheap models for one team, expensive for another) but not within a single team. The workaround is spawning separate processes with --model flags, losing shared task coordination. Note this as an expected future feature.

### C39: Harness Engineering for Multi-Agent Reliability
- **Status**: Evolved -- expanded significantly
- **Original claim**: Harness engineering wraps AI models in deterministic scaffolding; planner-generator-evaluator three-agent architecture; simplify as models improve.
- **Current state**: Harness engineering has matured from a community concept into a recognized discipline. [Martin Fowler's article](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) provides a canonical treatment: Agent = Model + Harness, with feedforward (guides) and feedback (sensors) controls. An [arxiv paper (2603.05344)](https://arxiv.org/abs/2603.05344) formalizes the scaffolding/harness/context engineering taxonomy. OpenAI revealed their internal product (1M+ lines) uses zero human-written code under harness engineering. Stripe's approach uses pre-push linter hooks with architectural blueprints. Teams report 2-5x reliability gains. The curriculum's treatment is accurate but now understates the maturity and formalization of the field.
- **Evidence**: [Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html), [arxiv 2603.05344](https://arxiv.org/abs/2603.05344), [agent-engineering.dev](https://www.agent-engineering.dev/article/harness-engineering-in-2026-the-discipline-that-makes-ai-agents-production-ready)
- **Recommended update**: Add references to the Fowler article and arxiv paper. Note that harness engineering is now a recognized discipline with formal taxonomy, not just a community practice. Consider noting the feedforward/feedback distinction as a useful framework.

### C50: Coordinator Mode
- **Status**: Evolved -- confirmed and elaborated
- **Original claim**: Feature-flagged coordinator mode from the Claude Code source leak; four phases (research, synthesis, implementation, verification); anti-rubber-stamping prompt engineering.
- **Current state**: Multiple external analyses of the leak confirm coordinator mode as a real, significant internal pattern. [Jock.pl analysis](https://thoughts.jock.pl/p/claude-code-source-leak-what-to-learn-ai-agents-2026) and [cloudmagazin.com](https://www.cloudmagazin.com/en/2026/04/01/claude-source-code-leak-reveals-ai-agent-architecture/) detail the asymmetric tool partitioning (coordinator retains only worker lifecycle tools, no filesystem access) and the star communication topology (workers cannot message each other; all inter-worker communication routes through coordinator). The curriculum's description is accurate but could note the communication topology constraint, which prevents coordination deadlocks.
- **Evidence**: [Jock.pl leak analysis](https://thoughts.jock.pl/p/claude-code-source-leak-what-to-learn-ai-agents-2026), [MindStudio analysis](https://www.mindstudio.ai/blog/claude-code-source-code-leak-unshipped-features), [DeepWiki](https://deepwiki.com/lucas-flatwhite/claude-code-system-prompts/3-multi-agent-orchestration)
- **Recommended update**: Add note about the star communication topology (workers cannot message each other directly) and the asymmetric tool partitioning as a structural inversion of the normal tool graph. This is a deliberate design choice, not a limitation.

### C14: Swarm Anti-Patterns (PACT Framework)
- **Status**: Evolved -- PACT now has public artifacts
- **Original claim**: McEntire's PACT framework; organizational dysfunction is substrate-independent; single agent scored 28/28 vs. Organizational Swarm at 0/28.
- **Current state**: McEntire has published PACT as a public framework at [jmcentire.github.io/pact](https://jmcentire.github.io/pact/) with a [GitHub repo](https://github.com/jmcentire/pact). The framework is now actionable, not just a research finding. The core claims (contracts before code, tests as law) remain valid and are reinforced by the Google Research scaling paper's finding that coordination collapse is architecture-dependent.
- **Recommended update**: Add links to the public PACT framework and GitHub repo. Note that the framework is now usable, not just a theoretical finding.

### C11 supplement: Coordination Collapse Evidence
- **Status**: Evolved -- stronger evidence
- **Original claim**: Coordination collapse is predictable beyond 5-7 agents; single-agent performance is a task difficulty proxy.
- **Current state**: New external research strengthens this significantly. [Silo-Bench (arxiv 2603.01045)](https://arxiv.org/html/2603.01045) shows agents "systematically fail to synthesize distributed state into correct answers" even when they successfully form task-appropriate coordination topologies. The [Towards Data Science "17x Error Trap"](https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/) analysis adds a critical nuance: on parallelizable tasks, centralized coordination improved performance by 80.9%, but on sequential tasks, every multi-agent variant degraded performance by 39-70%. This task-type dependency should be noted.
- **Recommended update**: Add the parallelizable-vs-sequential task distinction. Multi-agent systems help with parallelizable work but actively hurt sequential reasoning tasks.

## Needs Update (4)

### C2: The Shared Task List as Coordination Layer
- **Status**: Needs update (dashboard shows strength 0, classification "emerging" -- but this is a scoring artifact)
- **Issue**: The dashboard reports 0 support, but grep finds 14 sources referencing the shared task list concept. The concept is well-supported by #010, #014, #020, #051, #067, #444 and confirmed by official Anthropic documentation. The official docs now provide additional detail: tasks have three states (pending, in_progress, completed), tasks can have dependencies (blockedBy), task claiming uses file locking for race condition prevention, and tasks/teams are stored locally at `~/.claude/teams/{team-name}/config.json` and `~/.claude/tasks/{team-name}/`. The `TeammateIdle`, `TaskCreated`, and `TaskCompleted` hooks provide enforcement points.
- **Evidence**: [Official docs](https://code.claude.com/docs/en/agent-teams), 14 internal sources
- **Recommended action**: Update to include the three task states, dependency mechanism, file locking for race conditions, local storage paths, and hooks-based enforcement. Reclassify strength score -- this is evergreen, not emerging.

### C3: Team Composition and Role Design
- **Status**: Needs update (dashboard shows strength 0 -- scoring artifact)
- **Issue**: 6 internal sources match (#014, #102, #250, #426, #383, #028). The concept is well-cited. The official docs now add practical guidance missing from the curriculum: "Start with 3-5 teammates for most workflows," "5-6 tasks per teammate keeps everyone productive," and "Three focused teammates often outperform five scattered ones." The docs also introduce **subagent definitions** for teammates -- reusable role definitions with tools allowlists and model settings that can be defined once and referenced by name.
- **Evidence**: [Official docs](https://code.claude.com/docs/en/agent-teams), 6 internal sources
- **Recommended action**: Add the 3-5 teammate recommendation, 5-6 tasks per teammate heuristic, and subagent definitions as reusable role templates. Reclassify strength score.

### Pit6: Expecting speed improvements
- **Status**: Needs update
- **Issue**: Dashboard shows strength 0, but the claim itself may need nuance. While Bart's 2026-02 comparison showed comparable build times, the official docs state agent teams "work best when teammates can operate independently" -- implying speed gains are possible for parallelizable work. The coordination collapse research confirms: on parallelizable tasks, centralized multi-agent coordination improved performance by 80.9%. The pitfall should be reframed from "teams don't provide speed" to "teams provide speed only for genuinely parallelizable work; sequential or interdependent tasks see no speed gain."
- **Evidence**: Google Research scaling paper, official docs
- **Recommended action**: Reframe as "Expecting speed improvements from interdependent work" and note that parallelizable work can see genuine speed gains.

### Pit11: No session resumption
- **Status**: Needs update
- **Issue**: The official docs confirm this limitation but add important nuance: "/resume and /rewind do not restore **in-process** teammates" (emphasis added -- the limitation is specifically about in-process mode). The docs recommend: "After resuming a session, the lead may attempt to message teammates that no longer exist. If this happens, tell the lead to spawn new teammates." This is more actionable than the current pitfall text.
- **Evidence**: [Official docs limitations section](https://code.claude.com/docs/en/agent-teams#limitations)
- **Recommended action**: Update to specify in-process mode limitation, add the workaround (tell lead to spawn new teammates), and note the full list of official limitations: one team per session, no nested teams, lead is fixed, permissions set at spawn.

## Emerging -- Needs More Support (16)

### C4: The Devil's Advocate Pattern
- **Status**: Emerging, but understated support
- **Current support**: Dashboard shows 0 sources, but 4 internal sources match (#014, #021, #109, #265). Official docs include "Investigating with competing hypotheses" as a first-class use case with explicit adversarial framing: "each one's job is not only to investigate its own theory but to challenge the others'."
- **Recommendation**: Reclassify as established. The concept is confirmed by both internal sources and official documentation.

### C10: Fleet Orchestration with Gas Town
- **Status**: Emerging, limited validation
- **Current support**: 1 source (#024, Jo Van Eyck). Gas Town itself has limited external presence.
- **Recommendation**: Watch for reinforcement. The fleet orchestration concept is valid but the specific Gas Town tool may not gain wide adoption. Consider merging the fleet orchestration concept with C31 (Dedicated Agent Devices) and C44 (Heartbeat-Based Persistent Agent Companies) as different implementations of the same pattern.

### C13: The Integrator Removal Antipattern
- **Status**: Emerging, but the principle is strong
- **Current support**: 1 source (#054, Java Brains). The specific Cursor FastRender case study is well-documented but singular.
- **Recommendation**: The antipattern principle (don't remove quality gates for throughput) is validated by Anthropic's own harness research (#375) and the coordinator mode's mandatory separate verification. Consider strengthening by linking to these additional evidence points.

### P1: Functional Team for Complex Builds
- **Status**: Emerging (0 support)
- **Current support**: Well-described in #014 (Van Zyl). Official docs confirm the pattern with their "New modules or features" use case.
- **Recommendation**: Reclassify based on official docs confirmation.

### P2: Parallel Replication for Independent Workloads
- **Status**: Emerging (0 support)
- **Current support**: Well-described in #010 (IndyDevDan). Pattern is standard in the community.
- **Recommendation**: Reclassify based on widespread community adoption.

### P3: Exploratory Team for Debugging and Analysis
- **Status**: Emerging (0 support)
- **Current support**: Now a first-class example in official Anthropic docs ("Run a parallel code review," "Investigate with competing hypotheses").
- **Recommendation**: Reclassify as established -- Anthropic has canonized this pattern.

### Pit2: Underestimating token costs
- **Status**: Emerging (0 support) but universally acknowledged
- **Current support**: Official docs warn: "Token costs scale linearly: each teammate has its own context window." Turing College (#196) provides concrete $7-8/task data.
- **Recommendation**: Reclassify. This is practical knowledge confirmed by official documentation.

### Pit3: No observability
- **Status**: Emerging (0 support) but foundational principle
- **Recommendation**: Link to C7 (which has 123.0 strength) -- this pitfall is the inverse of a well-established concept.

### Pit7-Pit10: Various pitfalls at 0 support
- **Status**: Emerging but well-reasoned from cited sources
- **Recommendation**: These pitfalls derive logically from well-established concepts. Pit7 (removing quality gates) is the inverse of C13 and C50. Pit8 (scaling without measuring) is the inverse of C11. Pit9 (confusing scale with quality) cites the Anthropic compiler experiment. Pit10 (ignoring initial bugs) cites Bart's comparison. All are valid but need their inverse concept strengths credited.

### Ex2: Role design experiment
- **Status**: Emerging (1 source, strength 1.0)
- **Recommendation**: Valid exercise but could reference the official docs' 3-5 teammate and 5-6 tasks/teammate heuristics as evaluation criteria.

### Ex4: Observability integration
- **Status**: Emerging (0 support)
- **Recommendation**: Valid exercise. Could be updated to reference the official hooks (`TeammateIdle`, `TaskCreated`, `TaskCompleted`) alongside IndyDevDan's custom observability system.

### Pit12: Launching many agents simultaneously instead of incrementally
- **Status**: Emerging (1 source, strength 1.0)
- **Current support**: Eric #178 is the primary source. Official docs now recommend "Start with 3-5 teammates" which partially validates. The Google Research scaling paper strongly reinforces.
- **Recommendation**: Strengthen by linking to official docs team size guidance and external scaling research.

### Pit19: Scaling agents without durability infrastructure
- **Status**: Emerging (1 source, strength 1.0, last supported 2026-02-15)
- **Recommendation**: The Bantilan source (#468) is strong and the concept is important for production teams. Watch for additional evidence as more teams deploy persistent agent fleets.

### Pit20: Managing terminals instead of managing goals
- **Status**: Emerging (0 support)
- **Recommendation**: Well-argued in #473 (Simon Scrapes). The goal-first vs. session-first framing is valid but needs community adoption evidence.

### Pit21: Letting agents verify their own work
- **Status**: Emerging (1 source, strength 1.0)
- **Recommendation**: Strongly reinforced by coordinator mode (C50) which architecturally separates implementation from verification. Should be reclassified once C50's evidence is cross-linked.

## Module Health Summary

| Category | Count | Percentage |
|----------|-------|------------|
| Confirmed Evergreen | 20 | 43% |
| Evolved | 7 | 15% |
| Needs Update | 4 | 8% |
| Emerging (insufficient support) | 16 | 34% |

**Overall health**: 58% confirmed or evolved (solid foundation), 8% needs update (minor corrections), 34% emerging (many are dashboard scoring artifacts rather than genuine evidence gaps).

### Top 3 Urgent Updates

1. **Pattern 4 / C12 (Tiered Model Selection)**: The curriculum implies per-teammate model mixing within a single team, which is not supported. This could mislead practitioners into expecting functionality that does not exist.
2. **C2 (Shared Task List)**: Well-supported concept incorrectly scored as emerging. Official docs provide rich detail (three states, dependencies, file locking, hooks) that should be incorporated.
3. **C9 (Git Worktrees)**: The runtime isolation gap (ports, databases, caches) is a practical concern that practitioners will encounter. Adding this caveat prevents frustration.

### Top 3 Strongest Concepts

1. **C7: Multi-Agent Observability** (strength: 123.0) -- 82 sources, 63 creators, universally acknowledged as essential
2. **C12a: Non-Technical Multi-Agent Patterns** (strength: 121.5) -- Broad adoption evidence across technical and non-technical users
3. **C6: Infrastructure for Multi-Agent Execution** (strength: 120.0) -- Confirmed by official docs with detailed setup instructions

### Dashboard Scoring Recommendation

The strength formula appears to miss keyword matches for concepts whose titles use domain-specific terms (e.g., "shared task list," "devil's advocate," "integrator removal") that sources reference with different phrasing. Consider expanding keyword matching or implementing semantic similarity for concept-source matching. At least 7 concepts classified as "emerging" with 0 support have 3-17 matching sources in manual grep searches.

## External Sources Consulted

- [Anthropic Agent Teams Docs](https://code.claude.com/docs/en/agent-teams)
- [Martin Fowler: Harness Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)
- [Google Research: Towards a Science of Scaling Agent Systems](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- [Penligent: Git Worktrees Need Runtime Isolation](https://www.penligent.ai/hackinglabs/git-worktrees-need-runtime-isolation-for-parallel-ai-agent-development/)
- [TDS: The 17x Error Trap of Bag of Agents](https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/)
- [Silo-Bench: Evaluating Distributed Coordination (arxiv 2603.01045)](https://arxiv.org/html/2603.01045)
- [Building AI Coding Agents for the Terminal (arxiv 2603.05344)](https://arxiv.org/abs/2603.05344)
- [PACT Framework (jmcentire.github.io/pact)](https://jmcentire.github.io/pact/)
- [Jock.pl: Claude Code Source Leak Analysis](https://thoughts.jock.pl/p/claude-code-source-leak-what-to-learn-ai-agents-2026)
- [InfoQ: Google Agent Scaling Principles](https://www.infoq.com/news/2026/02/google-agent-scaling-principles/)
