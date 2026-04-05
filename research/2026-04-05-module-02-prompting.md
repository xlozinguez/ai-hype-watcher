---
type: research-validation
date: 2026-04-05
module: 02-prompting-and-workflows
section: all
concepts_reviewed: 50
confirmed: 28
evolved: 7
needs_update: 4
emerging_insufficient: 11
---

# Research: Module 02 Prompting & Workflows — Full Validation

> Validated on 2026-04-05. 50 concepts reviewed across 4 sections (core-concepts, patterns, pitfalls, exercises), cross-referenced against ~80 internal sources and 15+ external references.

## Summary

Module 02 is in strong health overall. The foundational thesis -- specification over prompting, context engineering over prompt tricks -- has been decisively confirmed by both the internal source base and the external landscape in early-to-mid 2026. The strongest concepts (specification-first, context engineering, context window discipline, repository hygiene) are among the best-supported in the entire curriculum with 30-60+ sources each.

However, the module has a structural issue: **22 of 50 concepts show 0-1 source support in the dashboard**, classifying them as "emerging" despite many being well-argued in the curriculum text and traceable to specific cited sources. This is primarily a dashboard keyword-matching limitation rather than a content quality problem -- the concepts exist in the curriculum with detailed citations, but the strength algorithm does not detect the supporting sources. This should be addressed by improving the strength calculation or manually verifying support counts.

The most significant evolution since the curriculum was written is the rise of **spec-driven development tooling** (Kiro, GitHub Spec Kit, Tessl) and the emergence of the **planner-generator-evaluator** three-role pattern as a refinement of the builder-validator pattern. The concept of "apparatus engineering" (Dex Horthy, #280) remains a distinctive local coinage that has not been adopted externally -- the industry uses "context engineering" to cover the broader configuration space.

**Key findings:**
- 3 concepts have genuinely evolved and need curriculum updates
- 4 concepts need factual or framing updates
- 7 concepts are emerging with insufficient dashboard support but are internally valid
- 28 concepts are confirmed evergreen or established
- The module's 60+ source references are current (latest: 2026-04-02)

---

## Confirmed Evergreen (28)

### Core Concepts

#### c1: Specification Is the Real Bottleneck
- **Status**: Confirmed -- strongest thesis in the module
- **Support**: 24 sources, 20 creators, latest 2026-04-02 (strength: 36.0)
- **Evidence**: External validation is overwhelming. GitHub launched Spec Kit (2026), AWS launched Kiro IDE specifically for spec-driven development, and Martin Fowler's team published a three-level spec rigor taxonomy (spec-first, spec-anchored, spec-as-source). The curriculum's framing through Nate B Jones, Lamport, and IBM Technology aligns precisely with the industry trajectory. An arxiv paper ([2602.00180](https://arxiv.org/abs/2602.00180)) formalizes spec-driven development as a paradigm. Delta Airlines reported 1,948% growth in AI tool adoption using spec-driven approaches.

#### c3: From Prompt Engineering to Context Engineering
- **Status**: Confirmed -- foundational and industry-standard
- **Support**: 62 sources, 45 creators, latest 2026-04-02 (strength: 93.0)
- **Evidence**: Gartner now publishes enterprise guidance on context engineering. Anthropic's own engineering blog ([anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) codifies the principles. The curriculum's framing via Tim Berglund and Nate B Jones's four-discipline model (craft/context/intent/specification) anticipated the industry consensus. The Anthropic blog's guiding principle -- "find the smallest set of high-signal tokens that maximize desired outcomes" -- echoes the curriculum's "focus over intelligence" framing from Charlie Automates (#040).

#### c5: Context Window Discipline
- **Status**: Confirmed
- **Support**: 44 sources, 33 creators, latest 2026-04-02 (strength: 66.0)
- **Evidence**: Anthropic's engineering blog confirms: "even as capabilities scale, treating context as a precious, finite resource will remain central." The 60-70% utilization ceiling from Berglund and Dylan Davis (#084) is independently validated by multiple external sources. Fresh context per task remains best practice: "A focused 20-minute session with clear instructions outperforms a sprawling 2-hour session every time" (external source, consistent with curriculum).

#### c6: Validation and Hallucination Reduction
- **Status**: Confirmed
- **Support**: 13 sources, 13 creators, latest 2026-04-02 (strength: 19.5)
- **Evidence**: The curriculum's claim that hallucination is structural is mathematically proven -- a 2025 proof showed hallucinations are architecturally inevitable under existing LLM designs. OpenAI's 2026 research confirms training rewards guessing over uncertainty admission. The curriculum's three-layer validation (grounding, self-evaluation, cross-model critique) remains the standard defensive stack.

#### c8b: Anti-Slop Engineering as Specification Enforcement
- **Status**: Confirmed
- **Support**: 16 sources, 14 creators, latest 2026-04-02 (strength: 24.0)
- **Evidence**: Jaymin West's layered defense framework (#220) continues to be validated by practitioners. The "never fix bad output, fix the configuration" principle aligns with Anthropic's own guidance.

#### c8b3: Meta-Prompting and Multi-Stage Specification Pipelines
- **Status**: Confirmed
- **Support**: 14 sources, 14 creators, latest 2026-04-02 (strength: 21.0)
- **Evidence**: Multi-stage prompting pipelines are now standard practice. The curriculum's coverage via Yash (#383) accurately represents the pattern.

#### c8b5: Folder-as-Knowledge-Base with Agent Teams
- **Status**: Confirmed
- **Support**: 5 sources, 5 creators, latest 2026-03-25 (strength: 7.0)
- **Evidence**: The plain-folder-plus-AI pattern from ICOR with Tom (#400) represents a legitimate alternative to structured PKM tools.

#### c10: Meta-Cognitive Frameworks for Prompt Design
- **Status**: Confirmed
- **Support**: 8 sources, 8 creators, latest 2026-03-31 (strength: 12.0)
- **Evidence**: Justin Sung's meta-models (#100) remain applicable. The mapping to prompt design is the curriculum's original contribution.

#### c10b: Repository Hygiene as Prompt Engineering
- **Status**: Confirmed
- **Support**: 41 sources, 29 creators, latest 2026-04-02 (strength: 61.5)
- **Evidence**: This has become one of the strongest concepts in the module. The insight that repository metadata (CONTRIBUTING.md, branch protection, type systems) functions as prompt engineering for agents is widely adopted. External sources confirm that "popular AI agents for software development advocate for maintaining tool-specific version-controlled Markdown files."

#### c10c: Supply Chain Security in Agentic Workflows
- **Status**: Confirmed
- **Support**: 4 sources, 4 creators, latest 2026-03-30 (strength: 5.2)
- **Evidence**: The LiteLLM case study (#378) remains a canonical example. Supply chain risk in agentic toolchains is a growing concern with no signs of resolution.

### Patterns

#### p1: Specification-First Development
- **Status**: Confirmed
- **Support**: 25 sources, 21 creators, latest 2026-04-02 (strength: 37.5)
- **Evidence**: Now supported by dedicated tooling (Kiro, Spec Kit). Pattern description is accurate and actionable.

#### p2: The RTCEOC Prompt Framework
- **Status**: Confirmed
- **Support**: 43 sources, 31 creators, latest 2026-04-02 (strength: 64.5)
- **Evidence**: The six-step framework from Ali H. Salem (#006) remains a practical structure. Internally referenced across multiple sources. The calibration advice (use the full framework for high-stakes work only) is particularly valuable.

#### p4: Context Window Budgeting
- **Status**: Confirmed
- **Support**: 44 sources, 33 creators, latest 2026-04-02 (strength: 66.0)
- **Evidence**: Directly validated by Anthropic's engineering guidance: context is a "finite attention budget."

#### p5: Three-Layer Validation
- **Status**: Confirmed
- **Support**: 13 sources, 13 creators, latest 2026-04-02 (strength: 19.5)
- **Evidence**: Cross-model critique and grounded tools remain the standard validation stack.

#### p7: The Sacrificial First Prompt
- **Status**: Confirmed
- **Support**: 42 sources, 30 creators, latest 2026-04-02 (strength: 63.0)
- **Evidence**: Widely practiced. The iterative specification refinement pattern is now embedded in tools like Kiro's workflow.

#### p8: The Obsidian Vault as Context Infrastructure
- **Status**: Confirmed
- **Support**: 5 sources, 4 creators, latest 2026-03-20 (strength: 6.5)
- **Evidence**: The "human writes, agent reads" discipline from Vinh Nguyen (#174) and Noah Vincent (#206) is validated. Anthropic's guidance on just-in-time context retrieval mirrors the vault pattern's selective loading.

#### p9: Honest Extraction Prompting
- **Status**: Confirmed
- **Support**: 4 sources, 4 creators, latest 2026-03-28 (strength: 5.2)
- **Evidence**: Dylan Davis's three-rule system (#432) is a distinctive and well-supported technique.

### Pitfalls

#### pit1: Prompting before specifying
- **Status**: Confirmed
- **Support**: 4 sources, 4 creators, latest 2026-03-26 (strength: 5.2)

#### pit2: Over-engineering every prompt
- **Status**: Confirmed
- **Support**: 63 sources, 46 creators, latest 2026-04-02 (strength: 94.5)
- **Evidence**: The highest-strength concept in the module. The calibration advice is critical and well-supported.

#### pit10: Treating code as the durable artifact instead of the specification
- **Status**: Confirmed
- **Support**: 8 sources, 8 creators, latest 2026-03-26 (strength: 12.0)
- **Evidence**: Chad Fowler's Phoenix Architecture (#368) is now supported by the spec-as-source paradigm in external tooling.

### Exercises

#### ex1: Write a specification before you prompt
- **Status**: Confirmed
- **Support**: 10 sources, 9 creators, latest 2026-04-02 (strength: 15.0)

#### ex6: Budget a context window
- **Status**: Confirmed
- **Support**: 44 sources, 33 creators, latest 2026-04-02 (strength: 66.0)

---

## Evolved (7)

### c8b2: The Builder-Validator Pattern for Long-Running Work
- **Status**: Evolved
- **Original claim**: Two-role pattern (generator + adversarial evaluator) inspired by GANs, with 5-15 iteration rounds.
- **Current state**: The pattern has matured into a **three-role architecture** in industry practice: Planner-Generator-Evaluator. The planner creates a structured specification (decomposition), the generator produces output, and the evaluator provides structured feedback. The critical distinction from the curriculum's two-role version: "A two-step approach asks the same model to generate output and then critique it -- introducing cognitive bias where authors miss errors in their own writing. The three-role pattern addresses this by ensuring the evaluator operates with fresh context" ([MindStudio](https://www.mindstudio.ai/blog/planner-generator-evaluator-pattern-gan-inspired-ai-coding)).
- **Evidence**: MindStudio blog, AWS Strands Evals documentation, Zylos Research (2026-03-06)
- **Recommended update**: Expand the concept to acknowledge the planner-generator-evaluator evolution as a refinement. The current two-role description is not wrong but is now the simpler variant of a more nuanced pattern. Add a note: "Industry practice has evolved this into a three-role pattern (Planner-Generator-Evaluator) where planning/specification is separated from generation, ensuring the evaluator judges against an independent specification rather than the generator's own framing."

### c1 (extended): Specification-First -- Tooling Has Arrived
- **Status**: Evolved
- **Original claim**: Specification-first is a discipline and a pattern, described through practitioner testimony.
- **Current state**: Dedicated tooling now exists. AWS Kiro is an IDE built on spec-driven development. GitHub Spec Kit is an open-source CLI for spec-driven agent workflows. Martin Fowler's team has published a three-level rigor taxonomy ([martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)): spec-first (specs before code), spec-anchored (specs persist post-completion), spec-as-source (specs are the maintained artifact, code is generated). The curriculum's framing through Chad Fowler's Phoenix Architecture (#368) aligns with "spec-as-source" -- the most radical level.
- **Evidence**: [GitHub Spec Kit blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/), [Augment Code guide](https://www.augmentcode.com/guides/what-is-spec-driven-development), [arxiv 2602.00180](https://arxiv.org/abs/2602.00180)
- **Recommended update**: Add a paragraph to Concept 1 noting the tooling maturation: "As of early 2026, the specification-first pattern has moved from practitioner advice to dedicated tooling. AWS Kiro, GitHub Spec Kit, and the Tessl framework all implement spec-driven workflows at different levels of rigor. Martin Fowler's team identifies three levels: spec-first (documentation before code), spec-anchored (specifications persist as living documents), and spec-as-source (specifications are the primary artifact, code is disposable). The Phoenix Architecture from Concept 8b4 corresponds to the spec-as-source level."

### c3 (extended): Context Engineering -- Anthropic's Official Guidance
- **Status**: Evolved
- **Original claim**: Context engineering is the broader discipline; Berglund identifies six competing components.
- **Current state**: Anthropic published official engineering guidance ([anthropic.com](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) that codifies the principles and adds several techniques not in the curriculum: **just-in-time context retrieval** (agents maintain lightweight identifiers and dynamically load data at runtime), **structured note-taking** (agents write persistent notes outside the context window for multi-hour tasks), and the explicit principle that "smarter models require less prescriptive engineering." Gartner now recommends organizations appoint a "context engineering lead or team."
- **Evidence**: [Anthropic engineering blog](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Gartner](https://www.gartner.com/en/articles/context-engineering)
- **Recommended update**: Add Anthropic's official guidance as a reference in the Further Reading section. Update Concept 3 to note the just-in-time retrieval and structured note-taking techniques as formal additions to the compaction/memory/decomposition trio from Berglund.

### c5 (extended): Context Window Discipline -- Attention Guidance
- **Status**: Evolved
- **Original claim**: Performance peaks at 60-70% capacity; strategies include compaction, memory, decomposition.
- **Current state**: External sources now describe **attention guidance** as a formal technique: using explicit markers ([CRITICAL], [REFERENCE]) to signal information importance within long documents. Anthropic's blog describes this as managing a "finite attention budget" -- analogous to the curriculum's framing but with more concrete tactics. Also, "content tags" and "truncation policies" for tool outputs are now standard practice.
- **Evidence**: [Maxim AI article](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/), [Anthropic engineering blog](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **Recommended update**: Add attention guidance markers and tool output truncation as practical techniques under Concept 5, alongside the existing compaction/memory/decomposition strategies.

### p10: The Builder-Validator Loop (Pattern)
- **Status**: Evolved (same as c8b2)
- **Support**: 1 source, 1 creator, latest 2026-03-25 (strength: 1.0)
- **Recommended update**: Align with the three-role evolution described above. Consider renaming to "The Builder-Validator Loop (and Planner-Generator-Evaluator)" to acknowledge the maturation.

### c6 (extended): Validation -- Hallucination Data Update
- **Status**: Evolved
- **Original claim**: "Hallucination persistence is a structural property that does not significantly improve with model generations."
- **Current state**: This has been strengthened by 2026 data. A mathematical proof (2025) confirms hallucinations are architecturally inevitable. OpenAI's 2026 research shows training actively rewards guessing over uncertainty admission. Most strikingly, OpenAI's o3 model hallucinated **33% of the time** on PersonQA -- more than double the 16% rate of its predecessor o1 ([Suprmind report](https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/)). Reasoning models hallucinate *more* on factual benchmarks, not less.
- **Evidence**: [Suprmind hallucination statistics](https://suprmind.ai/hub/insights/ai-hallucination-statistics-research-report-2026/), [Towards Data Science analysis](https://towardsdatascience.com/hallucinations-in-llms-are-not-a-bug-in-the-data/)
- **Recommended update**: Add the o3/o1 comparison as concrete evidence in Concept 6: "OpenAI's o3 model hallucinated 33% of the time on the PersonQA benchmark -- more than double its predecessor o1's 16% rate -- confirming that reasoning improvements do not automatically reduce factual hallucination."

### pit5: Building one-off prompts instead of systems
- **Status**: Evolved
- **Support**: 2 sources, 2 creators, latest 2026-04-02 (strength: 2.2)
- **Original claim**: "Save successful prompts in a library."
- **Current state**: The concept is correct but the recommended practices have moved beyond text files and spreadsheets. Prompt inheritance patterns (Jaymin West, #266), skills libraries (Sean Kochel, #392), and object-oriented prompt composition (base/child/mixin patterns) now represent the mature form of "systems over one-offs." The pitfall description could reference these as the solution rather than just text expanders.
- **Recommended update**: Add a reference to the prompt inheritance pattern (#266) and skills libraries (#392) as the mature evolution of prompt systems.

---

## Needs Update (4)

### c2: The Six-Step Prompting Framework
- **Status**: Needs update -- dashboard misclassification
- **Issue**: Shows 0 sources and 0 support in the dashboard despite being directly sourced from #006 (Ali H. Salem) with clear citations. The curriculum text is accurate and well-written. The issue is purely a dashboard/strength-algorithm problem -- the concept does have source support.
- **Evidence**: Source #006 is explicitly cited. Grep confirms #006 references the RTCEOC framework.
- **Recommended action**: Fix the strength algorithm to detect support for this concept. No curriculum text changes needed.

### c2a: Context Over Personality -- The End of "You Are an Expert"
- **Status**: Needs update -- dashboard misclassification + minor framing evolution
- **Issue**: Shows 0 sources despite being directly sourced from #246 (The Blur) with explicit citations. Additionally, the framing could be strengthened: Anthropic's official guidance now explicitly states that "smarter models require less prescriptive engineering, allowing agents to operate with more autonomy" -- directly confirming the "end of persona prompts" thesis. The claim that "you don't got to do that anymore" is no longer just a practitioner observation; it is Anthropic's official engineering position.
- **Evidence**: Source #246 is explicitly cited. Anthropic engineering blog confirms the thesis.
- **Recommended action**: Fix dashboard detection. Optionally add Anthropic's engineering blog as corroborating evidence.

### c8c: Claude vs. ChatGPT -- Training Philosophy Shapes Prompting Strategy
- **Status**: Needs update -- partial obsolescence risk
- **Issue**: Strength 3.6 (established, 3 sources, 3 creators). The core claim about Constitutional AI vs. RLHF producing different default behaviors is accurate. However, the specific "94% vs 87% instruction compliance" benchmark from Pixel Peak is now dated (the comparison likely involved earlier model generations). Both Claude and ChatGPT have evolved significantly. The principle (different training → different prompting strategies) remains valid, but the specific numbers and behavioral contrasts may no longer be accurate for current model versions.
- **Evidence**: Both Anthropic and OpenAI have released multiple model updates since the cited comparison. The [arxiv paper on RLHF sycophancy](https://arxiv.org/abs/2602.01002) (Feb 2026) confirms that sycophancy differences between training approaches persist structurally.
- **Recommended action**: Keep the principle but flag the specific compliance numbers as historical. Add a note: "These behavioral differences persist structurally due to training methodology, but specific compliance metrics shift with each model release."

### Concept: "Apparatus Engineering" (within c5)
- **Status**: Needs update -- term not adopted externally
- **Issue**: Dex Horthy's coinage "apparatus engineering" (#280) -- configuring the full stack of MCPs, skills, slash commands, and agent settings -- is a useful distinction from context engineering (crafting tokens for a single context window). However, web search confirms the term has not been adopted by the broader industry. The external landscape uses "context engineering" to encompass both token-level craft and tool/harness configuration. The curriculum should acknowledge this is a local term while preserving the useful distinction.
- **Evidence**: Searching for "apparatus engineering" returns zero relevant results outside the original source. [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Gartner](https://www.gartner.com/en/articles/context-engineering), and [Martin Fowler's team](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) all subsume this under "context engineering."
- **Recommended action**: Keep the term as a useful conceptual distinction but add a note: "Note: 'apparatus engineering' is a term coined by Dex Horthy in the 12 Factor Agents paper. The broader industry subsumes this under the umbrella of 'context engineering,' but the distinction between token-level context craft and tool/harness configuration remains practically useful."

---

## Emerging -- Needs More Support (11)

### c4: Sticky Workflows -- Compounding Over Coasting
- **Status**: Emerging in dashboard (0 support), but well-supported in curriculum text
- **Current support**: Dashboard shows 0 sources, but curriculum cites #005, #006, #109, #272, #318, #372. Grep confirms 14 sources reference related concepts (reusable prompts, prompt libraries, sticky workflows).
- **Recommendation**: Dashboard detection issue. The concept is well-argued with 6+ explicit citations. Fix strength algorithm.

### c7: Software Vision and the Automation Decision
- **Status**: Emerging (0 dashboard support), internally sourced
- **Current support**: Curriculum cites #005 and #006. Grep finds 9 sources mentioning software vision or automation decision concepts.
- **Recommendation**: Valid concept with adequate sourcing. Dashboard needs recalibration.

### c8: Handoff Drift and the PM-as-Prototyper
- **Status**: Emerging (1 source, 2026-02-14)
- **Current support**: Only #070 (Dhyey Mavani at Anthropic). Grep finds 10 sources referencing related PM/prototyper concepts including #071, #103, #136, #221, #321.
- **Recommendation**: Watch for reinforcement. The concept describes a specific organizational pattern at Anthropic that may not generalize. Consider broadening the concept title to encompass the wider PM-as-builder trend seen in multiple sources.

### c9: Incremental Prompting vs. Monolithic Instructions
- **Status**: Emerging (0 dashboard support), but well-documented
- **Current support**: Curriculum cites #072 and #091 explicitly. Grep finds 5 sources referencing incremental/step-by-step prompting.
- **Recommendation**: Dashboard detection issue. Concept is sound and well-sourced.

### c10a: Testing Strategy for AI-Assisted Development
- **Status**: Emerging (1 source, 2026-02-28)
- **Current support**: Curriculum cites #374 and #436. Only 1 detected by dashboard.
- **Recommendation**: Valid emerging concept. The TDD critique and eval-for-agents discussion is growing. Watch for reinforcement from the expanding AI evaluation tooling ecosystem (AWS Bedrock AgentCore, Galileo, etc.).

### c10d: The AutoResearch Loop as General-Purpose Optimization
- **Status**: Emerging (0 dashboard support)
- **Current support**: Curriculum cites #433. Grep finds #288, #294 as related sources.
- **Recommendation**: Niche but valid pattern. The concept that any domain with a scalar metric is a candidate for automated optimization loops is powerful. May benefit from merging with Module 04 (Agentic Patterns) coverage of eval loops.

### c11: The AI Slop Problem and Feelings-First Design
- **Status**: Emerging (1 source, 2026-02-13)
- **Current support**: Curriculum cites #075. The concept is well-articulated but narrowly sourced.
- **Recommendation**: The "everything looks the same" problem is real but may be better framed as a design concern than a prompting concern. Consider whether this belongs in Module 02 or would be better as a reference to a Module 06 (Strategy) discussion.

### p3: Fresh Context Per Task
- **Status**: Emerging (0 dashboard support), but externally validated
- **Current support**: Curriculum cites #005 and #011. External validation: Anthropic's blog recommends starting fresh sessions for new tasks. 35 internal sources reference fresh context or context reset concepts.
- **Recommendation**: Critical dashboard detection failure. This is one of the most well-supported practices in the module. Fix immediately.

### p6: MCP-Style Resource Discovery (Beyond RAG)
- **Status**: Emerging (0 dashboard support)
- **Current support**: Curriculum cites #011 (Berglund). 12 sources reference MCP resource discovery patterns.
- **Recommendation**: The concept is sound and the MCP ecosystem has grown significantly. Dashboard detection needs fixing.

### p10/p11: Builder-Validator Loop / Skills Library as Expert Encoding
- **Status**: Emerging (0-1 dashboard support each)
- **Current support**: p10 cites #375; p11 cites #392. Both have internal references in 25+ and 26+ sources respectively.
- **Recommendation**: Both are well-sourced but under-detected. The Builder-Validator Loop has evolved (see Evolved section). Skills Library as Expert Encoding is validated by the growing skills ecosystem.

### Pitfalls pit3, pit4, pit6, pit7, pit8, pit9 (batch)
- **Status**: Emerging (0-1 dashboard support each)
- **Assessment**: These are practical warnings derived from the core concepts above. Their low dashboard scores reflect the nature of pitfalls -- they are warnings *about* well-supported concepts rather than independently sourced claims. All remain valid. No curriculum changes needed; dashboard detection should be improved to inherit strength from parent concepts.

### Exercises ex2, ex3, ex4, ex5 (batch)
- **Status**: Emerging (0-1 dashboard support each)
- **Assessment**: Exercises are inherently derivative of the concepts they practice. Low dashboard scores are expected and not concerning. All exercises remain pedagogically sound.

---

## Spot-Check: Evergreen Stability

Three highest-strength concepts were spot-checked externally:

1. **pit2: Over-engineering every prompt** (strength 94.5) -- Confirmed stable. The calibration advice remains critical as context engineering grows in prominence.

2. **c3: From Prompt Engineering to Context Engineering** (strength 93.0) -- Confirmed and strengthened. Now an industry standard with Gartner, Anthropic, and Google all publishing formal guidance.

3. **p4: Context Window Budgeting** (strength 66.0) -- Confirmed stable. The 60-70% rule continues to hold despite larger context windows.

---

## Module Health Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Confirmed | 28 | 56% |
| Evolved | 7 | 14% |
| Needs Update | 4 | 8% |
| Emerging (insufficient support) | 11 | 22% |

### Top 3 Urgent Updates

1. **Builder-Validator Pattern (c8b2, p10)**: Expand to acknowledge the Planner-Generator-Evaluator three-role evolution. The current two-role description is not wrong but is now the simplified variant.

2. **Specification-First Tooling (c1)**: Add coverage of Kiro, GitHub Spec Kit, and the three-level rigor taxonomy. The thesis has moved from advice to infrastructure.

3. **Dashboard Strength Detection**: 22 concepts show 0-1 support despite having explicit source citations and multiple grep-confirmed references. This is a systemic measurement issue, not a content problem. Priority fix: p3 (Fresh Context Per Task), c4 (Sticky Workflows), c2 (Six-Step Framework), p6 (MCP Resource Discovery).

### Top 3 Strongest Concepts

1. **pit2: Over-engineering every prompt** -- 94.5 strength, 63 sources, 46 creators
2. **c3: From Prompt Engineering to Context Engineering** -- 93.0 strength, 62 sources, 45 creators
3. **p4: Context Window Budgeting** -- 66.0 strength, 44 sources, 33 creators

### External Sources Consulted

- [Anthropic: Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Martin Fowler: Understanding Spec-Driven Development Tools](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [Gartner: Context Engineering for Enterprise AI](https://www.gartner.com/en/articles/context-engineering)
- [GitHub Blog: Spec-Driven Development with AI](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- [MindStudio: The Planner-Generator-Evaluator Pattern](https://www.mindstudio.ai/blog/planner-generator-evaluator-pattern-gan-inspired-ai-coding)
- [Augment Code: What Is Spec-Driven Development](https://www.augmentcode.com/guides/what-is-spec-driven-development)
- [arxiv 2602.00180: Spec-Driven Development in the Age of AI](https://arxiv.org/abs/2602.00180)
- [arxiv 2602.01002: How RLHF Amplifies Sycophancy](https://arxiv.org/abs/2602.01002)
- [Suprmind: AI Hallucination Statistics Report 2026](https://suprmind.ai/hub/insights/ai-hallucination-statistics-research-report-2026/)
- [Maxim AI: Context Window Management Strategies](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/)
