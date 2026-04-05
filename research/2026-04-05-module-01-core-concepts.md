---
type: research-validation
date: 2026-04-05
module: 01-foundations
section: all (core-concepts, patterns, pitfalls, exercises)
concepts_reviewed: 55
confirmed: 30
evolved: 8
needs_update: 5
emerging_insufficient: 12
---

# Research: Module 01 Foundations — Full Validation

> Validated on 2026-04-05. 55 concepts reviewed across all 4 sections (36 core concepts, 5 patterns, 9 pitfalls, 5 exercises), drawing on 430+ source notes and external evidence.

## Summary

Module 01 is the largest and most heavily referenced module in the curriculum. Its core thesis -- that AI capabilities are advancing rapidly while adoption lags, creating both opportunity and hype risk -- remains fundamentally sound. However, several concepts have evolved significantly since their initial framing, and a handful need targeted updates to reflect Q1 2026 developments.

**What is solid:** The capability overhang (c2), enterprise reality check (c11), vibe coding pitfall (pit6), and agent failure rate (c11a3) concepts are the strongest in the module -- well-supported by dozens of sources across many creators, with external evidence confirming their continued relevance. The skeptical/bubble thesis concepts (c6, c13, c14b) are well-constructed and increasingly validated by real market data.

**What has evolved:** The METR doubling rate (c3) has new data points. The bubble thesis (c6) has shifted from theoretical pattern-matching to concrete financial distress signals (OpenAI $14B projected 2026 losses, Bill Gurley's public warnings). The Mythos/model landscape concept (c11d) has a major update: the Mythos leak is now confirmed by Anthropic and Fortune, not speculative. Inference-time compute scaling (c12a) has become the dominant paradigm shift, not an emerging one. LeCun's departure from Meta to found AMI Labs with $1B in funding materially strengthens the "LLM dead end" structural critique (c6 addendum via #381).

**What needs attention:** Many concepts show 0 strength in the dashboard despite rich source citations in the curriculum text itself -- this is a dashboard keyword-matching limitation, not a content problem. The 38 "emerging" classifications overstate the fragility of concepts that are actually well-supported by inline citations. The most urgent content updates are to c3 (METR data), c6 (bubble financial data), c11d (Mythos confirmation), and c12a (inference scaling maturity).

**Structural observation:** Module 01 has grown to 36 core concepts, making it the largest single module. Some concepts (c11a2, c11a3, c11a4, c11b, c11c, c11d, c11e) are nested sub-concepts of c11 (Enterprise Reality Check) that could benefit from reorganization into a clearer hierarchy. The numbering scheme (c12d, c14c, etc.) suggests organic growth that may benefit from a structural review.

---

## Confirmed Evergreen (13 dashboard + 17 content-confirmed = 30)

The following concepts are well-supported and require no content changes. I am grouping them by theme rather than listing each individually.

### Capability & Landscape Cluster (c2, c4, c8, c12d, c11d)

- **c2: The Capability Overhang** -- Strength 84.0, 56 sources, 42 creators, last supported 2026-04-02. The module's anchor concept. External evidence confirms: only 13% of workers use AI daily (NBER 2026), matching the curriculum's framing of the gap between frontier capability and typical usage. **Status: Rock-solid.**

- **c4: The February 2026 Model Releases** -- Dashboard shows 0 strength (keyword mismatch), but the curriculum text cites sources #003, #016, #104, #143, #161 directly. The Opus 4.6 vs GPT-5.3 comparison and the "Great Convergence" thesis remain accurate. Sonnet closing the gap on Opus (source #104) is confirmed by current benchmark data. **Status: Confirmed, dashboard artifact.**

- **c8: Open-Source Frontier Models and Local Inference** -- Strength 9.0, 6 sources. The open-source landscape continues to expand (GLM 5.1, Kimi K2.5, DeepSeek). LeCun's AMI Labs departure from Meta and $1B raise further validates the importance of alternative architectures. **Status: Confirmed.**

- **c12d: The Chat-to-Code Capability Spectrum** -- Strength 10.5, 7 sources. Claude Co-work's positioning between Chat and Code remains accurate. **Status: Confirmed.**

- **c11d: Model Landscape Accelerates** -- Strength 12.0, 8 sources. See "Evolved" section below for the Mythos update.

### Enterprise Reality Cluster (c11, c11a3, c11a4, c11c)

- **c11: The Enterprise Reality Check** -- Strength 118.5, 79 sources, 55 creators. The strongest concept in the entire curriculum. External evidence strengthens it further: Forrester's Copilot reality check shows 3.3% paid adoption, a -24.1 accuracy NPS, and a 60-point gap between forced and voluntary adoption. The NBER finding that 90% of firms report no AI productivity impact despite executives projecting gains is devastating confirmation. **Status: Rock-solid, increasingly validated.**

- **c11a3: 97.5% Agent Failure Rate** -- Strength 16.5, 11 sources. External evidence: the new APEX-Agents benchmark shows 75% failure on complex workplace tasks; agents succeed on only 24% of professional tasks. Gartner projects 40%+ of agentic AI projects will be canceled or fail to reach production by 2027. The curriculum's 97.5% figure (from real freelance projects) sits at the pessimistic end of a range that external benchmarks broadly confirm. **Status: Confirmed; consider noting the range (75-97.5%) depending on task structure.**

- **c11a4: LLM Code Production Risk** -- Strength 13.5, 9 sources. The Meta SEV-1 and Amazon Q incidents cited remain the best-documented cases. No contradicting evidence found. **Status: Confirmed.**

- **c11c: Design Process Disruption** -- Strength 5.2, 4 sources. Jenny Wen's observations about engineering velocity forcing design adaptation remain current. **Status: Confirmed.**

### Skepticism Cluster (c6, c10, c13, c14b, c17)

- **c6: The Bubble Thesis** -- Dashboard shows 0 strength (keyword mismatch), but this is one of the most heavily cited concepts in the module, referencing sources #007, #037, #077, #085, #089, #096, #097, #144, #147, #151, #188, #218, #355, #381 and more. Internal grep finds 30+ source files discussing bubble/correction dynamics. See "Evolved" section for specific updates needed.

- **c10: The AI Reporting Problem** -- Strength 1.0 (dashboard undercount). Cal Newport's two-question test and taxonomy of bad AI reporting remains the gold standard framework. No contradictions. **Status: Confirmed.**

- **c13: The SaaSpocalypse** -- Dashboard 1.0 strength, but well-supported by #039, #065, #207 inline. The SaaS market has partially recovered from the initial panic, confirming Gerard's "market overreaction" framing. **Status: Confirmed.**

- **c14b: The Demo-to-Production Gap** -- Strength 2.0. The Cursor browser debunking (#054), compiler debunking (#073, #107), and Cloudflare VNext scrutiny (#199) form a strong pattern. External evidence continues to confirm: Copilot feature rollbacks, agent benchmark failures. **Status: Confirmed, strengthening pattern.**

- **c17: Verifying AI Industry Claims** -- Dashboard 0 strength, but well-supported by inline citations. The Java Brains Cursor case study remains the best teaching example. **Status: Confirmed, dashboard artifact.**

### Pattern & Practice Cluster (p1, p2, pit2, pit6, ex1)

- **p1: Calibrating Your AI Mental Model** -- Strength 7.0. The three-filter model (measured data, adoption gap, economic sustainability) remains applicable. **Status: Confirmed.**

- **p2: Tracking the Capability Frontier** -- Strength 84.0. METR + SWE-bench + practitioner reports. See c3 Evolved section for data updates. **Status: Confirmed framework, data needs refresh.**

- **pit2: "I tried ChatGPT once"** -- Strength 5.2. The power-user gap persists; external data confirms only 13% daily usage. **Status: Confirmed.**

- **pit6: Vibe coding trap** -- Strength 96.0, 64 sources, 45 creators. The module's second-strongest concept. Every new incident (Amazon Q outages, Meta SEV-1) reinforces this. **Status: Rock-solid.**

- **ex1: Map your capability overhang** -- Strength 84.0. The exercise remains well-designed and supported. **Status: Confirmed.**

### Additional Confirmed (brief notes)

| ID | Title | Note |
|----|-------|------|
| c1 | December 2025 Phase Transition | Dashboard 0 but well-cited inline (#008, #019). Historical framing, inherently stable. |
| c5 | Horizontal/Temporal Collapse | Dashboard 0 but cited via #012. Framework remains valid. |
| c9 | Demand Signal | 1 source. Narrow but accurate. |
| c11b | Implementation Cost as Feature | Dashboard 0 but well-cited (#201, #202). Jevons paradox framing confirmed by continued AI-driven software expansion. |
| c12 | Interface Flattening | 1 source (#038). The responsive surface addendum (#372) provides a useful counterpoint. |
| c14 | White-Collar Inversion | Dashboard 0 but well-cited (#050). Harris's inversion thesis continues to be confirmed by hiring data. |
| c14c | CS Beyond AI | 1 source. Grounding perspective remains valid and evergreen by nature. |
| c15 | Context Rot Two-Dimensional | Strength 2.2. The core claim (context rot = length * complexity) is confirmed by ongoing long-context research (#295, #307). |
| c16 | Assistant Axis / Persona Drift | Dashboard 0. Single-source (#049) but the research is peer-reviewed Anthropic work. Inherently stable. |
| pit3 | Dismissing bubble because tech is real | Dashboard 0. This is a logical/pedagogical framing, not an empirical claim. Inherently stable. |
| pit4 | Extrapolating exponentials | Dashboard 0. Pedagogical framing. Gary Marcus's "trillion-pound baby" analogy remains apt. |

---

## Evolved (8)

These concepts remain valid but need nuance or data updates to reflect Q1 2026 developments.

### c3: The Accelerating Doubling Rate
- **Status**: Evolved
- **Original claim**: METR task duration doubles every 7 months, recently compressing to 4 months. As of early 2026, models handle ~5 hours of human expert effort.
- **Current state**: METR's March 2026 correction of a regularization error adjusted some measurements. The latest data shows frontier agents (including GPT-5.2) handling tasks requiring 14+ hours of human effort at the 50% reliability threshold. The 7-month doubling trend has held since 2019 across 6 years of data. However, the curriculum's "compressing to every 4 months" claim may have been premature -- METR's own researchers note the trend "may have accelerated in 2024" but present 7 months as the central estimate.
- **Evidence**: [METR Time Horizons (Epoch AI)](https://epoch.ai/benchmarks/metr-time-horizons/), [METR official](https://metr.org/time-horizons/)
- **Recommended update**: Update the "~5 hours" figure to "14+ hours at 50% reliability" and soften the "compressing to 4 months" claim to "the 7-month doubling has held consistently, with possible acceleration." Add the March 2026 regularization correction as a data quality note.

### c6: The Bubble Thesis -- A Necessary Counterweight
- **Status**: Evolved
- **Original claim**: Historical pattern-matching (Super Bowl ads, dot-com parallels) with strong counter-arguments (big-tech balance sheets, real adoption).
- **Current state**: The thesis has moved from pattern-matching to concrete financial distress signals. Key updates since the curriculum was written:
  - **OpenAI financials**: $25B annualized revenue (Feb 2026) against projected $14B losses in 2026, $44B cumulative losses through 2028, carrying ~$100B in debt. Burn rate at 57%. Contrast with Anthropic dropping to 9% burn by 2027.
  - **Bill Gurley's public warning**: Benchmark's Bill Gurley publicly stated in March 2026 that the AI bubble is "about to burst" and a reset is coming -- significant because Gurley is not a perma-bear but a top-tier VC.
  - **NBER study (Feb 2026)**: 90% of firms report no AI impact on productivity, yet executives project productivity gains -- the exact pattern of "say-do gap" the curriculum identifies.
  - **LeCun's departure**: Yann LeCun left Meta to found AMI Labs with $1.03B (largest European seed round), explicitly arguing LLMs are a "dead end" -- this is now backed by real capital allocation, not just academic critique.
  - **24/7 Wall St. (March 2026)**: "Is This What the Start of an AI Bubble Bust Looks Like?" -- mainstream financial media asking the question directly.
- **Evidence**: [Fortune: Bill Gurley AI bubble](https://fortune.com/2026/03/17/is-ai-bubble-bill-gurley-run-out-of-money/), [OpenAI $14B losses](https://www.rdworldonline.com/facing-14b-losses-in-2026-openai-is-now-seeking-100b-in-funding-but-can-it-ever-turn-a-profit/), [24/7 Wall St.](https://247wallst.com/investing/2026/03/30/is-this-what-the-start-of-an-ai-bubble-bust-looks-like/), [Al Jazeera: OpenAI fundraising slowdown](https://www.aljazeera.com/economy/2026/3/7/openais-fund-raising-boom-slows-amid-mounting-debt)
- **Recommended update**: Add a "Q1 2026 update" paragraph noting the shift from theoretical pattern-matching to concrete distress signals. Include OpenAI's updated financials ($25B revenue / $14B projected loss / $100B debt), the Gurley warning, and the NBER 90% no-impact finding. Update the LeCun/Newport section (#381) to note AMI Labs and the $1B raise. The curriculum's existing framing ("three data points don't guarantee a fourth") remains appropriately cautious -- the update should strengthen the evidence without changing the balanced tone.

### c11d: Model Landscape Accelerates -- Mythos, ARC-AGI 3, and Engram
- **Status**: Evolved
- **Original claim**: Reports on a "leaked Anthropic model tier called Claude Mythos" with early Fortune reporting on capabilities.
- **Current state**: Mythos is no longer speculative. On March 26, 2026, Fortune broke confirmed coverage of the leak: nearly 3,000 unpublished assets from a misconfigured CMS, including details of a 10-trillion-parameter model above Opus tier (internally codenamed "Capybara"). Anthropic spokesperson confirmed it represents "a step change" in capabilities. The model is in internal beta, not publicly released. Internal documents flag significant cybersecurity risks (the model can rapidly find and exploit software vulnerabilities). The leak itself -- a misconfigured public data lake -- is ironic given Anthropic's safety positioning.
- **Evidence**: [Fortune: Anthropic Mythos confirmed](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/), [Euronews: cybersecurity risks](https://www.euronews.com/next/2026/03/30/what-is-anthropics-mythos-the-leaked-ai-model-that-poses-unprecedented-cybersecurity-risks)
- **Recommended update**: Upgrade the Mythos discussion from "leaked/reported" to "confirmed by Anthropic." Add the 10T parameter count, the cybersecurity risk disclosure, and the irony of the leak mechanism given Anthropic's safety brand. Note that the model remains in internal beta as of April 2026.

### c12a: Inference-Time Compute Scaling as a New Paradigm
- **Status**: Evolved
- **Original claim**: Frames inference-time scaling as an emerging paradigm shift, primarily through the lens of Gemini 3 Deep Think and the 100x compute reduction.
- **Current state**: Inference-time scaling is no longer "emerging" -- it is the dominant paradigm shift in AI research as of Q1 2026. External evidence: inference demand is projected to exceed training demand by 118x in 2026 (up from the curriculum's implicit framing as roughly equal). By 2030, inference could claim 75% of total AI compute. DeepSeek-R1 proved the approach at scale. Monte Carlo Tree Search (MCTS) with step-level evaluation has become the leading technique. Sebastian Raschka's comprehensive taxonomy identifies multiple categories of inference-time scaling. The paradigm has moved from "the next frontier" to "the current frontier."
- **Evidence**: [Sebastian Raschka: Categories of Inference-Time Scaling](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling), [AI Barcelona: The Inference-Time Revolution](https://www.aibarcelona.org/2026/01/post-chinchilla-era-inference-time-scaling.html), [Introl: Inference-Time Scaling Research](https://introl.com/blog/inference-time-scaling-research-reasoning-models-december-2025)
- **Recommended update**: Reclassify from "emerging paradigm" to "current dominant paradigm." Add the 118x inference-to-training demand ratio. Note DeepSeek-R1 as a second major proof point alongside Deep Think. The curriculum's Althia example remains excellent -- add that the generate-verify-revise pattern it describes has become the standard architecture for inference-time scaling systems.

### c14a: The Specification Bottleneck and J-Curve Adoption
- **Status**: Evolved
- **Original claim**: The bottleneck shifted from production to specification. J-curve adoption pattern with initial productivity dip.
- **Current state**: Internal grep finds 19 source files discussing spec-driven development, and 13 discussing maturity levels -- far more support than the dashboard's 0 strength suggests. The concept has been strongly reinforced by recent sources: IBM's spec-driven development tutorial (#214), Martin Fowler's spec-as-library experiment (#071), Dex Horthy's no-vibes methodology (#118). The J-curve pattern is now confirmed by NBER data (Feb 2026): 90% of firms report no productivity impact, matching the "trough" prediction. AWS launching Cairo to force testable specifications before code generation is a powerful industry validation.
- **Evidence**: Internal sources #076, #118, #214, #071, #456; NBER study (Feb 2026)
- **Recommended update**: This concept is actually much stronger than "emerging" -- it should be reclassified as established or evergreen based on the volume of supporting sources. The J-curve evidence from NBER is the strongest external validation available. Add a note that AWS Cairo represents an industry-level endorsement of the specification-first thesis.

### p5: The Maturity Self-Assessment
- **Status**: Evolved
- **Original claim**: Van Eyck's 5-level maturity ladder (Chat -> Mid-Loop -> In-the-Loop -> On-the-Loop -> Multi-Agent).
- **Current state**: The 5-level framework has been independently reinforced by Jones's 5-level AI coding framework (#108), The Pragmatic Engineer's tiered enterprise adoption framework (#382), and Karpathy's "loopy era" framing (#337). The framework is sound but the specific level descriptions may need updating: "Multi-Agent" (level 5) is no longer cutting-edge as of early 2026 -- it is increasingly practiced. A potential level 6 (autonomous agent fleets operating across organizational boundaries) may be emerging.
- **Evidence**: Internal sources #024, #108, #382, #337
- **Recommended update**: Note convergence across multiple independent frameworks. Consider whether the top level needs updating to reflect the state of the art as of mid-2026.

### ex4: Evaluate the Bubble Signals
- **Status**: Evolved
- **Original claim**: Asks students to research what happened to Super Bowl LX AI advertisers and whether Brown's parallels held.
- **Current state**: The exercise now has dramatically more material to work with. The Gurley warning, NBER 90% no-impact study, OpenAI debt spiral, and mainstream financial media questioning all provide rich evaluation material. The exercise should be updated to include these as evaluation inputs alongside the original Super Bowl ad data.
- **Evidence**: See c6 evolution above.
- **Recommended update**: Add a bullet asking students to evaluate OpenAI's financial trajectory and the NBER 90% finding as additional bubble signals. This makes the exercise richer without changing its pedagogical intent.

### ex5: Calculate Your Personal METR
- **Status**: Evolved
- **Original claim**: Compare against ~5-hour METR benchmark.
- **Current state**: The benchmark has moved to 14+ hours. The exercise framing remains excellent but the comparison target needs updating.
- **Evidence**: METR March 2026 data.
- **Recommended update**: Update "~5-hour METR benchmark" to "~14-hour METR benchmark (as of March 2026)."

---

## Needs Update (5)

These concepts have specific issues that should be addressed.

### c4a: The AI Maturity Plateau and Diminishing Hype Response
- **Status**: Needs update
- **Issue**: The concept frames the maturity plateau as a recently observed phenomenon. Since its writing, the plateau dynamic has intensified and become more complex. The Mythos leak (a qualitatively discontinuous model) tests whether the plateau thesis holds when a genuinely novel capability tier appears. If Mythos delivers on its leaked benchmarks, it could either break the plateau or confirm it (if reaction is muted). The concept should acknowledge this test case.
- **Evidence**: Fortune Mythos coverage (March 2026), ARC-AGI 3 sub-1% AI performance
- **Recommended action**: Add a forward-looking paragraph noting that Mythos represents a natural test of the plateau thesis. If a 10T-parameter model with confirmed "step change" capabilities generates a muted response, the plateau thesis is strongly confirmed. If it reignites the hype cycle, the thesis needs qualification.

### c7: The AI Maturity Ladder and Developer Identity Crisis
- **Status**: Needs update (concept not visible in README)
- **Issue**: This concept appears in the dashboard data (c7, emerging, strength 0) but I cannot find it as a standalone section in the README. The closest content is distributed across Concept 4b (agentic fever), pitfall 9 (emotional dimension), and source #022 (Traversy Media forced adoption). The developer identity crisis theme is well-covered thematically but lacks a consolidated section matching the c7 dashboard entry.
- **Evidence**: Dashboard data mismatch with curriculum content
- **Recommended action**: Either (a) add a consolidated c7 section synthesizing the identity crisis content from #022, #252, #311, #399, or (b) remove c7 from the dashboard data if it is intentionally distributed across other concepts. The current state creates a phantom concept that appears unsupported.

### pit1: Anchoring on Stale Mental Models
- **Status**: Needs update
- **Issue**: The pitfall references December 2025 as the anchor point ("If you have not revisited your AI assumptions since before December 2025..."). As of April 2026, this framing is itself becoming stale. The relevant anchor events now include the February 2026 model releases, the March 2026 Mythos leak, the METR 14-hour milestone, and the NBER productivity study. The pitfall should be generalized to "regularly" rather than anchored to a specific date that will continue aging.
- **Evidence**: Passage of time
- **Recommended action**: Replace "since before December 2025" with a more durable framing like "within the past 3-6 months" or add "or the February 2026 model releases" to keep it current. The underlying principle is evergreen; the specific date reference is not.

### pit7: Taking AI Demo Claims at Face Value
- **Status**: Needs update
- **Issue**: References only the Cursor FastRender browser case study. Since writing, multiple additional high-profile demo debunkings have occurred (Cloudflare VNext 13% test coverage, compiler "from scratch" with 37 years of test suites, Copilot feature rollbacks, the Erdos math "solutions" that were already in the literature). The pitfall should be strengthened with 1-2 additional examples to demonstrate this is a systemic pattern, not an isolated incident.
- **Evidence**: Sources #107, #199, #377, #408
- **Recommended action**: Add the compiler test suite dependency (#107) and the Erdos already-solved-problems case (#408) as additional examples. These are the strongest because they show the pattern operating at different scales (product marketing vs. research claims).

### pit8: Accepting AI Reporting at Face Value
- **Status**: Needs update
- **Issue**: References only Newport's framework (#034). The Mo Bitar circular validation loop thesis (#416) -- where AI companies make claims, media amplifies, markets react, and the reaction is cited as evidence -- is a powerful extension that deserves inclusion. It describes a failure mode that Newport's two-question test would catch but that the current pitfall does not explicitly name.
- **Evidence**: Source #416
- **Recommended action**: Add a sentence describing the circular validation loop as a specific pattern to watch for, alongside Newport's three reporting failures. This makes the pitfall more actionable.

---

## Emerging -- Needs More Support (12)

These concepts have limited source support and should be monitored for reinforcement or considered for consolidation.

### c4b: Agentic Fever (strength 1.0, 1 source, 1 creator)
- **Status**: Emerging, single-source concept
- **Current support**: Only source #252 (Matteo Cassese). However, the concept is thematically reinforced by #025 (AI burnout trap), #399 (developer joy tradeoffs), #216 (internal locus of control), and #311 (identity crisis).
- **Recommendation**: Monitor for additional creator coverage. Consider consolidating with the developer identity crisis theme (c7). The concept is pedagogically valuable as a counterweight to acceleration pressure.

### c9: The Demand Signal (strength 1.0, 1 source)
- **Status**: Emerging, narrow scope
- **Current support**: Single source. The OpenClaw demand data (250K+ GitHub stars) is striking but the concept could be broadened.
- **Recommendation**: Consider merging with c12e (Virtual Employee Adoption Pattern) since both address what users actually want from AI agents.

### c11a2: Karpathy "Loopy Era" (strength 1.0, 1 source)
- **Status**: Emerging but important
- **Current support**: 1 source (#337) plus the AutoResearch release (#348). Karpathy's authority gives this outsized weight despite limited source count.
- **Recommendation**: Watch for reinforcement. The "loopy era" framing is increasingly adopted in the practitioner community. The connection to inference-time scaling (c12a) should be made explicit -- they describe the same paradigm from different angles.

### c12b: "Future Overhyped, Present Underhyped" (strength 0, 1 source)
- **Status**: Emerging, single-source but valuable framework
- **Current support**: Only source #061 (Tim Fairley, construction). The framework is excellent but narrowly supported.
- **Recommendation**: Keep as-is. The construction industry lens is unique and the AI sweet spot framework (clear inputs/outputs, definable rules, human-verifiable, limited hallucination risk) is genuinely useful. Watch for similar frameworks from other industries.

### c12c: Tool Era vs. Agentic Era (strength 1.0)
- **Status**: Emerging
- **Current support**: Griffonomics #065. The "tool era to agentic era" framing is broadly used but this specific concept's grounding is narrow.
- **Recommendation**: Consider consolidating with the capability overhang (c2) or the maturity ladder (p5), which cover overlapping territory.

### c12e: "Virtual Employee" Adoption Pattern (strength 0)
- **Status**: Emerging, single-source
- **Current support**: Only source #058 (Krakowski). The "employee metaphor" framing is common in the agent space.
- **Recommendation**: Merge with c9 (Demand Signal) or consolidate into the enterprise reality check (c11) as a sub-observation about adoption framing.

### c13a: AI Scare Trade (strength 0)
- **Status**: Emerging but well-supported in text
- **Current support**: Dashboard shows 0 but the curriculum text cites #110 directly. Jones's "autoimmune disorder" metaphor is a strong framework.
- **Recommendation**: Dashboard keyword issue. The concept is well-constructed and has been validated by continued market volatility through Q1 2026. No content change needed; dashboard indexing should be improved.

### c14d: Technical Vocabulary Scaffold (strength 0)
- **Status**: Emerging, reference content
- **Current support**: Only source #031 (ByteByteAI). This is a glossary/primer concept.
- **Recommendation**: This serves a different pedagogical function (reference) than the analytical concepts around it. Consider moving to a "Prerequisites" or "Reference" section rather than treating it as a core concept.

### p3: Bicycle Rule (strength 0)
- **Status**: Emerging, single-metaphor
- **Current support**: Only source #012. The metaphor is memorable but narrow.
- **Recommendation**: Keep as pattern. The underlying principle (momentum over caution) is reinforced by multiple acceleration-thesis sources. No change needed.

### p4: Meta-Cognitive Evaluation Frameworks (strength 0)
- **Status**: Emerging, single-source
- **Current support**: Only source #100 (Justin Sung). The six meta-models are well-constructed.
- **Recommendation**: Monitor for reinforcement. This pattern is more general than AI-specific, which may explain limited AI-source support. It remains pedagogically valuable.

### pit5: Waiting for Stability (strength 0)
- **Status**: Emerging, pedagogical framing
- **Current support**: Derived from Jones's bicycle rule and general acceleration thesis.
- **Recommendation**: This is the pitfall counterpart to pattern p3. Both stand or fall together. No change needed.

### pit9: Emotional Dimension (strength 0)
- **Status**: Emerging, under-supported given its importance
- **Current support**: Primarily #022 (Traversy), with thematic support from #252, #399, #311.
- **Recommendation**: This pitfall addresses a real and under-discussed issue. Consider strengthening with explicit citations to the burnout research (#025), identity crisis sources (#311, #399), and agentic fever (#252).

---

## Dashboard Data Quality Notes

The dashboard strength formula appears to rely on keyword matching between concept titles and source content. This produces significant undercounting for concepts whose titles use distinctive vocabulary not commonly repeated in source text:

- **"Phase Transition"** (c1): 0 strength despite being the framing concept for the module's central thesis
- **"Bubble Thesis"** (c6): 0 strength despite 30+ sources discussing bubble dynamics
- **"White-Collar Inversion"** (c14): 0 strength despite being cited in 5+ sources
- **"Specification Bottleneck"** (c14a): 0 strength despite 19 files containing "spec-driven/spec-first"

**Recommendation**: Consider adding alias keywords to the dashboard formula (e.g., "bubble" as alias for "Bubble Thesis," "spec-driven" as alias for "Specification Bottleneck"). The current formula significantly underestimates the health of Module 01.

---

## Top 3 Urgent Updates

1. **c3 / ex5: METR data refresh** -- The "~5 hours" figure is outdated; current data shows 14+ hours. This is a factual claim that can be corrected quickly.
2. **c6: Bubble thesis financial data** -- OpenAI $14B projected loss, Gurley warning, NBER 90% no-impact study. The evidence base has shifted from pattern-matching to concrete financial signals.
3. **c11d: Mythos confirmation** -- Upgrade from "leaked/reported" to "confirmed by Anthropic." Include 10T parameter count and cybersecurity risk disclosure.

## Top 3 Strongest Concepts

1. **c11: Enterprise Reality Check** -- 118.5 strength, 79 sources, 55 creators. Externally validated by Forrester, NBER, and Fortune.
2. **pit6: Vibe Coding Trap** -- 96.0 strength, 64 sources, 45 creators. Reinforced by every new AI code incident.
3. **c2: Capability Overhang** -- 84.0 strength, 56 sources, 42 creators. The module's anchor concept, confirmed by 13% daily usage data.

## Module Health Summary

| Metric | Count | Percentage |
|--------|-------|-----------|
| Confirmed | 30 | 55% |
| Evolved (needs nuance/data update) | 8 | 15% |
| Needs Update (specific fix required) | 5 | 9% |
| Emerging (insufficient support) | 12 | 22% |

**Overall health: Strong.** The module's core analytical framework is sound and increasingly validated by external evidence. The primary risk is not conceptual staleness but structural bloat -- 36 core concepts with deep nesting (c11a2, c11a3, c11a4...) makes the module difficult to navigate. A structural reorganization pass would improve accessibility without changing content validity.
