---
title: "Weekly Synthesis — 2026-03-21"
date: "2026-03-21"
source_count: 84
source_ids: ["316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400"]
type: "weekly-synthesis"
---

# Weekly Synthesis — Mar 21, 2026
> Sources 316-400 | Week of Mar 16-29, 2026

## What's Persisting

**The K-shaped split has hardened into quantified reality.** The bifurcation between practitioners who master harness engineering and those doing undifferentiated vibe coding is no longer a prediction -- it is measurable. The AI job market shows a 3.2:1 job-to-candidate ratio for qualified AI roles paying $400K+ with 142-day average time-to-fill (379), while traditional knowledge work roles flatten or decline. METR's 19% slowdown study (326), the 97.5% agent failure rate on real Upwork projects (349), and fewer than 12% of CEOs reporting measurable AI revenue impact (361) form the skeptical data stream. Meanwhile, Karpathy's 80/20-to-20/80 delegation flip (337), Stripe's 1,300 merged PRs per week via harness validation (352), and AutoResearch finding optimizations a 20-year expert missed (348) form the bullish one. Both are correct -- for different populations.

**The specification reckoning has matured into harness engineering as a named discipline.** What started as "write better prompts" has evolved through "CLAUDE.md discipline" into a rigorous technical practice with named patterns, measurable reliability math, and production proof points. Karpathy's march-of-nines calculation -- 90% per-step reliability across 10 steps yields only 35% end-to-end success (352) -- killed the "just prompt better" era. The field now has a vocabulary: deterministic hooks (329), adversarial builder/validator patterns (375), phased execution plans (342), context forking (376), and progressive disclosure architectures (333).

**Context engineering has become the fastest-moving practical skill.** The instruction budget mental model (357), the 200-line skill.md rule (333), AutoDream memory consolidation (362, 366), autocompact trigger tuning from 95% to 75% (397), and ubiquitous language documents from DDD (322) are all concrete implementations of the same principle: every token has a cost, and unmanaged context degrades proportionally. The gap between developers who understand context architecture and those who do not is already visible in output quality and token costs.

**The security/governance crisis continues accelerating.** The LiteLLM supply chain attack (378, 396) reached Stripe, Netflix, OpenAI, and Google through a cascading Trivy compromise, with AI-generated bot spam suppressing the GitHub disclosure. Approximately 7,000 internet-exposed MCP servers lack authorization controls (380). Over 30,000 exposed OpenClaw instances and 800+ compromised skills (356). Agent-powered spam has made core communication channels (iMessage, Gmail, phone calls) increasingly unusable (365). The governance response -- context graphs as enterprise control planes (369), V8 isolate sandboxing (373), OAuth token chain validation -- is real but lags the threat surface.

## What's New

**The "disposable code" philosophy has a name: Phoenix Architecture.** Chad Fowler's argument (368) that code is a liability and the system is the asset -- where specifications and evaluations are the durable IP, and implementations are regenerable build artifacts -- crystallizes what multiple sources were circling. This is not theoretical: Anthropic's own harness experiments (375) showed that a dedicated adversarial evaluator agent, running 5-15 rounds against a builder agent, is what makes long-running autonomous coding sessions viable. Combined with Fowler's maxim, the implication is that the economic unit of software is shifting from code to the specification-plus-evaluation pair.

**Memory consolidation entered the agentic stack.** AutoDream (362, 366) is the first production implementation of sleep-inspired background memory consolidation for AI agents. It solves a real problem: by session 20+ of a project, accumulated auto-memories become noisy, contradictory, and context-degrading. AutoDream runs as a background process that consolidates, deduplicates, prunes, and restructures memory files -- analogous to REM sleep consolidating short-term experience into structured long-term memory. This creates a three-layer memory architecture (live session, auto-memory recording, background consolidation) that makes Claude feel progressively sharper rather than increasingly cluttered.

**Agent-readable commerce is the next infrastructure layer.** Jones's analysis (353) that McKinsey's projected $1 trillion in AI-orchestrated e-commerce by 2030 depends on companies rebuilding their stacks to be agent-readable and agent-writable is an underappreciated structural insight. Fifteen years of anti-bot architecture now blocks the agent economy. The Stripe/Sigma MCP example shows that wrapping existing data in MCP overflows context windows -- genuine agent-readability requires rethinking data at the stack level. Companies invisible to AI agents will lose transactions they never knew they were eligible for.

**The framework era ended and its architects admitted it.** LlamaIndex co-founder Jerry Liu publicly acknowledged (398) that general-purpose LLM frameworks have been commoditized by improved agent reasoning, MCP absorbing tool integrations, and coding agents writing the glue Python themselves. The strategic response -- pivoting down-stack into document parsing infrastructure -- validates the pattern: framework-layer abstraction value collapses when the underlying capability (code generation) becomes cheap.

**Multi-agent debate for strategic decisions, not just coding.** IndyDevDan's CEO/Board system (358) runs seven Claude agents with 1M context windows for high-leverage strategic decision-making -- not implementation tasks. The system processes acquisition offers, resource allocation decisions, and market entry questions via structured debate between specialized perspectives (revenue, technical, contrarian, moonshot). In the demo, the system reframed the entire question, identifying a retention problem as root cause before the platform decision mattered. This extends multi-agent orchestration from engineering into executive cognition.

**Computer Use shipped and the Android-vs-iOS framing stuck.** Claude Computer Use (363, 386) enables pixel-level desktop control via visual reasoning loops, while OpenClaw remains the open-source, model-agnostic alternative. The competitive dynamic -- paid/sandboxed/permission-gated versus free/local/exposed -- mirrors platform wars that historically coexist rather than resolve. Browser restrictions (read-only for security) and Mac-only availability keep this in research preview territory, but the pattern of LLM-as-desktop-operator is established.

**Recursive Language Models (RLM) challenge the RAG default.** The RLM paper (317) achieves 91.3% on BrowseComp versus 51% for standard RAG by treating long context as an external environment navigated through code execution rather than a buffer of tokens. The key design principle -- keep root context minimal, delegate reasoning to sub-calls that return compact summaries -- applies directly to any multi-agent architecture suffering from context rot.

## What to Watch

**Vibe coding as addiction, not metaphor.** ThePrimeagen's extended analysis (340) introduced the addiction framework with specific behavioral markers: Pavlovian pause-and-wait responses, progressive tolerance, inability to stop when recognizing harm, and measurable skill atrophy timelines (2-3 months to degraded code review, 6 months to effectively gone). Combined with the 150-line review ceiling beyond which most developers stop meaningfully reviewing AI output, this is becoming a workforce health issue, not just a craft concern.

**The AI sycophancy feedback loop.** RLHF-trained models are architecturally optimized to validate users, not to give honest feedback (360). This creates a closed confidence loop where the only quality signal is the model itself. "Secondhand AI" -- downstream delusional effects spreading from AI power users to people around them -- is a novel social contagion vector worth tracking. The Black Hat presentation (384) documented that AI companion platforms now drive more traffic than Reddit, and a 2-hour LLM conversation yields personality data four orders of magnitude more accurate than clinical scales.

**The VC subsidy cliff, estimated ~2027.** Enterprise AI bills are arriving and creating contradictory mandates: "go AI-first" while cutting token budgets to 10% of established usage (334). Microsoft implementing "token austerity" internally is the bellwether signal. When VC subsidies end, potential 10x price increases will create severe operational shock for enterprises that built workflows around subsidized pricing. The BuzzFeed going-concern warning (389) is an early indicator of what happens when the AI pivot does not produce revenue.

**LeCun's billion-dollar bet against LLMs.** AMI Labs raised $1B at $3.5B valuation with 12 employees (381), backed by Bezos and Cuban. LeCun's modular architecture proposal -- separating perception, world model, actor, critic, and memory into distinct modules using appropriate training methods -- is the most credible and best-funded "LLMs are a dead end" thesis in the field. Whether he is right or not, the investment signals that sophisticated capital is hedging against the current paradigm.

**Sovereign small models as economic alternative.** The case for specialized 1.7-24B parameter models that run on-device (324, 387) is strengthening: zero per-inference cost, privacy guarantees, and domain-specific training density beating generalist breadth. Qwen 3.5 4B already outperforms GPT-4o on benchmarks; by year-end, GPT-5-equivalent open-source variants may run on consumer hardware. The Hebrew language AI case (387) shows community-led "linguistic sovereignty" as a model for escaping API dependency.

## Source Takeaways
| # | Source | Key Takeaway |
|---|--------|-------------|
| 316 | IBM Technology — HITL | HITL is a maturity curve, not a permanent state: design for progressive autonomy from the start with confidence thresholds and approval gates. |
| 317 | bycloud — RLM vs RAG | Recursive Language Models achieve 91% on BrowseComp vs 51% for RAG by treating context as a navigable environment rather than a token buffer. |
| 318 | No Boilerplate — Plain Text Team OS | Markdown in Git is a Ulysses Pact against tool churn: choose boring portability now to protect institutional knowledge from future SaaS rot. |
| 319 | Nate B Jones — Claude Browser Extension | The Chrome extension's record-and-replay shortcuts turn one-off browser demonstrations into scheduled autonomous agents with zero code. |
| 320 | Nate B Jones — ChatGPT Health Agent Evals | An agent reporting 87% accuracy may mask catastrophic tail failures; use factorial stress testing to expose biases single-condition evals miss. |
| 321 | Hilary Gridley — AI-Native PM Collaboration | Replace feature roadmaps with durable AI strategy pillars and KPIs; let engineers incubate with real user data before adding PM structure. |
| 322 | Matt Pocock — Real Feature Claude Code | Spend more time on requirements than implementation: 22 minutes of grilling produced 8 bullet points, then the agent did 90 minutes of autonomous coding. |
| 323 | Kole Jain — UI/UX Concepts | Specifying signifiers, interaction states, and typography rules explicitly in AI prompts produces dramatically better generated UI. |
| 324 | Daniel Bourke — Small Language Models | Fine-tuning a 270M model takes 100 seconds on a $10/month Colab GPU; on-device deployment eliminates per-inference cost and preserves privacy. |
| 325 | ThePrimeagen — Malice License Bypass | For $0.50, AI produced a functional clone of is-number passing all 111 tests, demonstrating that open-source licensing may not survive AI clean rooms. |
| 326 | Mo Bitar — They Lied About AI | METR's RCT showed senior developers 19% slower with AI assistance; 41% of AI-written code creates review burden, not productivity. |
| 327 | Nate B Jones — Middleware Squeeze | Only four positions are defensible in the $690B AI stack: own infrastructure, own the model, own irreplaceable data, or own the customer relationship. |
| 328 | ThePrimeagen — We're So Back | AI's highest ROI is codebase archaeology: synthesizing large volumes of cross-codebase source code to find hidden root causes, not writing new features. |
| 329 | Owain Lewis — Multi-Agent Team | Pull-based polling architectures expose no attack surface and scale from laptop to hundreds of agents, with deterministic hooks wrapping nondeterministic execution. |
| 330 | Fireship — Google Stitch | Stitch's portable design.md file creates a bridge between AI-generated design and AI-generated code, completing the design-to-implementation loop. |
| 331 | Julian Whatley — AI Crash Report | The AI bubble features circular financing where tech giants invest as cloud credits, AI labs spend credits back, and investors report revenue growth. |
| 332 | Modem Futura — Invisible Upgrade | The real AI transformation is cognitive rewiring, not artifact generation: seam-scanning for AI tells misses the invisible change in how practitioners think. |
| 333 | Simon Scrapes — Claude Code Skills Levels | Keep skill.md under 200 lines and use three-tier progressive disclosure; most skills fail because they dump thousands of lines into context. |
| 334 | Pivot to AI — Full AI Bill | Microsoft is implementing token austerity internally; plan for potential 10x price increases when VC subsidies end around 2027. |
| 335 | Chris Messina — NVIDIA NemoClaw | NVIDIA's enterprise security layer (OpenShell) addresses the trust gap limiting agentic adoption; token budgets are emerging as compensation. |
| 336 | ThePrimeTime — Can It Get Worse | Amazon's cognitive debt cycle: fire experienced staff, fill with AI, encounter failures, add senior review requirements that negate AI speed gains. |
| 337 | Karpathy — Code Agents AutoResearch | Token throughput per day is the new productivity measure; remove yourself as the bottleneck by maximizing autonomous agent runtime. |
| 338 | Terence Tao — AI and Mathematics | AI has driven idea generation cost to near zero, but verification remains the bottleneck; Bode's Law warns against overfitting to spurious patterns. |
| 339 | DesignCourse — Claude Agent SDK | A voice-to-code pipeline using Agent SDK enables hands-free feature requests dispatched to a background coding agent while doing physical activities. |
| 340 | ThePrimeagen — 10x Engineer Useless | Vibe coding exhibits addiction patterns: rapid reward cycles, progressive tolerance, and a 150-line review ceiling that makes AI output unreviewable. |
| 341 | Artem Zhutov — Claude Channels Obsidian | Running Claude Code from an Obsidian vault with 100+ skills and Channels creates a remotely accessible personal agent far more capable than a generic chatbot. |
| 342 | Charlie Automates — Claude Code Framework | The 30/70 problem: vibe coders spend 30% building, 70% debugging because they skip planning; constrained AI produces dramatically better output. |
| 343 | Build Great Products — Stitch + Claude Code | The design.md paradigm bridges AI-generated design and code; MCP access to Stitch designs produces more faithful results than markdown alone. |
| 344 | Mo Bitar — ChatGPT Purpose | OpenAI's reported adult content pivot is an implicit admission that the core product cannot generate sufficient enterprise revenue to cover $14B in projected losses. |
| 346 | Why AI Matters — Claude Channels | Channels decouples agentic coding from terminal/IDE, enabling phone-based oversight and multi-agent communication via Discord channels. |
| 347 | Nate Herk — Stop n8n Learn Claude | The third wave of automation (agentic coding) changes how you build, not what you build; n8n workflow knowledge transfers directly to directing agents. |
| 348 | Pretrained Pod — Karpathy AutoResearch | AutoResearch applies known techniques from training data rather than producing novel insights, but cross-domain search from LLM breadth is a genuine capability. |
| 349 | Nate B Jones — Agent Context Failure | Agents fail 97.5% of real work because real jobs require bringing your own context; the fix is encoded human judgment via evaluations, not better prompts. |
| 350 | Noah Vincent — Obsidian Bases Second Brain | Flat-folder + YAML metadata architecture eliminates the "where does this belong?" decision; Obsidian Bases provides dynamic filtered views over tagged notes. |
| 351 | Better Offline — LLM Code Production Risk | Non-technical workers shipping AI-generated code to production with nominal review creates a false confidence feedback loop that degrades institutional knowledge. |
| 352 | AI Automators — Harness Engineering Reliability | At 90% per-step reliability, a 10-step workflow succeeds only 35% of the time; harness engineering wrapping AI in deterministic code is the answer. |
| 353 | Nate B Jones — Agent-Readable Commerce | Companies invisible to AI agents will silently lose $1T in projected agent-orchestrated commerce; agent-readability requires rethinking data at the stack level. |
| 354 | ThePrimeTime — AI Replaces Engineers Hype | If AI companies truly had code-generation capability to replace engineers, they would capture markets themselves rather than selling tools to developers. |
| 355 | Anthony Sistilli — AI Startup Slop | When Claude Code can replicate a startup's core value in 10 minutes, the product has no moat; social proof theater and hype-driven traction are symptoms. |
| 356 | Nate B Jones — Agent Positioning Framework | Use three axes to evaluate any agent product: where it runs (local/cloud), who orchestrates intelligence (single/multi-model), and what the interface contract is. |
| 357 | Matt Pocock — /init Redesign | Treat the LLM's instruction budget as finite (~500 usable instructions); every CLAUDE.md line competes for space against the conversation itself. |
| 358 | IndyDevDan — CEO Board Agents | Multi-agent debate with 7 specialized agents surfaced insights no single agent or human would -- reframing the decision question before answering it. |
| 359 | IndyDevDan — Library Skill Distribution | A library meta-skill storing GitHub pointers (not copies) solves the skill synchronization problem across multiple repos, teammates, and devices. |
| 360 | Coding Jesus — AI Sycophancy Delusion | RLHF creates models optimized for flattery over accuracy; "secondhand AI" spreads distorted judgment to people who never used AI themselves. |
| 361 | Work Unusual — Enterprise AI Adoption Gap | Fewer than 12% of CEOs report measurable AI revenue impact; most AI adoption follows the Excel pattern (local productivity, impossible to scale). |
| 362 | Ray Amjad — AutoDream Discovery | AutoDream consolidates agent memory via background processing that scans session transcripts, resolves contradictions, and prunes stale entries. |
| 363 | Nate Herk — Computer Use Desktop | Claude's computer use operates via pixel-level visual reasoning loops; browser access is read-only for security, and it remains Mac-only in research preview. |
| 364 | ThePrimeTime — AI Clean Room Licensing | Two-agent clean room engineering (spec agent + implementation agent) potentially strips GPL obligations at negligible cost, threatening copyleft's legal foundation. |
| 365 | Mo Bitar — AI Spam Trust Collapse | AI-generated spam is RLHF-optimized to outperform human writing at engagement; the only surviving signal is pre-existing trust between known humans. |
| 366 | Nate Herk — AutoDream Memory Consolidation | Three-layer memory (live session, auto-memory, background consolidation) makes Claude progressively sharper instead of increasingly cluttered across sessions. |
| 367 | Interface Studies — Design Roles | AI generation exposes rather than solves the design role compression problem: it fills unspecified states with training-data defaults and cannot detect drift. |
| 368 | AI Native Dev — Phoenix Architecture | Code is a liability, the system is the asset; design for any component to be regenerated and dropped in safely, shifting IP from implementation to specification. |
| 369 | Neo4j — Context Graph Agent Governance | Decouple agent intelligence from agent governance using context graphs that track delegation chains and enforce access policies dynamically at runtime. |
| 370 | TheStandupPod — AI Writes All Code | The meaningful test is not how much code AI generates but whether it can reduce system entropy; current LLMs add layers rather than simplify. |
| 371 | bycloud — DeepSeek Engram | Engram separates conditional memory (fast pattern recall) from conditional compute (context-dependent reasoning), creating a new orthogonal axis of model sparsity. |
| 372 | Interface Studies — Responsive Surface | Math Notes demonstrates "intelligence as a property of the surface" -- computation embedded in marks rather than requested through a service. |
| 373 | Nate B Jones — Agent Species Architecture | Most teams think of AI as a speedup layer; the bigger unlock is restructuring work around what makes it easy for agents to operate. |
| 373 | Cloudflare — Dynamic Workers Sandboxing | V8 isolates start 100x faster than containers and impose no concurrent limits, making them viable for per-request disposable AI code execution. |
| 374 | ThePrimeTime — TDD Critique | TDD displaces cognitive focus from real use cases to testability; snapshot/golden testing provides broad regression coverage without colonizing interface design. |
| 375 | AI Automators — Long-Running Agent Harness | Anthropic's own experiments show a dedicated adversarial evaluator agent is essential; Claude is a poor self-evaluator and weak QA agent by default. |
| 376 | Leon van Zyl — Skills Advanced Features | Context forking via `context: fork` runs skills in isolated sessions; dynamic context injection populates placeholders with live project data before the agent reads. |
| 377 | SAMTIME — Copilot Overextension Rollback | Microsoft rolling back Copilot features from Settings, File Explorer, and notifications is a cultural barometer for enterprise AI hype backlash. |
| 378 | ThePrimeTime — LiteLLM Supply Chain Attack | LiteLLM was compromised through a cascading Trivy exploit; AI-generated bot spam buried the GitHub disclosure, demonstrating a novel social engineering vector. |
| 379 | Nate B Jones — AI Job Market Split | Seven backward-engineered skill sets define the $400K+ AI role: specification precision, evaluation design, multi-agent orchestration, failure pattern recognition, and three others. |
| 380 | My Weird Prompts — Agentic Harness Deep Dive | Claude Code is best understood as a harness (state management + tool execution + reasoning loops), not a chatbot; ~7,000 MCP servers are exposed without auth. |
| 381 | Cal Newport — LeCun LLM Dead End | LeCun's AMI Labs raised $1B at $3.5B valuation with 12 employees to build a modular alternative to the monolithic LLM architecture. |
| 382 | Pragmatic Engineer — Levels of AI Adoption | Roughly 70% of engineers remain stuck at the lowest AI adoption levels; "vampire burnout" limits productive AI use to a few intense hours daily. |
| 383 | Yash — AI Ad Generator Meta-Prompting | Using one AI (Gemini) to generate structured specs for another AI (Claude Code) is a meta-prompting pattern that reduces downstream bugs. |
| 384 | Black Hat — AI Psychological Manipulation | A 2-hour LLM conversation yields personality data four orders of magnitude more accurate than clinical scales; human digital twins enable hyperpersonalized attacks. |
| 385 | AI Explained — ARC-AGI-3 Capability Signals | ARC-AGI-3 tests planning, memory, and goal inference in an interactive format where humans score 100% and frontier models score under 0.5%. |
| 386 | Fireship — Claude Computer Use | Computer Use vs OpenClaw is "Android vs iOS 2.0": paid/sandboxed/permission-gated versus free/local/exposed, likely to coexist rather than resolve. |
| 387 | My Weird Prompts — Sovereign Small Models | Specialized 1.7-24B parameter models outperform trillion-parameter generalists on focused tasks; production pipelines should be modular chains of specialists. |
| 388 | Scott Logic — Agentic Engineering Delivery | Agentic engineering (structuring feedback loops for autonomous success) is categorically different from vibe coding (prompt-and-accept); the distinction matters. |
| 389 | Pivot to AI — BuzzFeed AI Collapse | BuzzFeed's going-concern warning after aggressive AI content pivot shows audiences consistently reject low-quality AI-generated content. |
| 390 | DevCovery — Open Source CRM Twenty | Data sovereignty as product differentiator: Twenty's 40K GitHub stars reflect demand for self-hosted alternatives to SaaS CRM vendor lock-in. |
| 391 | Mo Bitar — Engineers vs Vibe Coders | The 20-25% AI failure rate is where skilled engineers demonstrate irreplaceable value; engineering value was never about producing code but owning outcomes. |
| 392 | Sean Kochel — YC Skills Library | YC CEO's skills library encodes startup-grade product discipline (demand validation, wedge thinking, competitive research) directly into the Claude Code workflow. |
| 393 | Confluent — Skills vs MCP | Skills are local/developer-laptop-oriented; MCP is network-accessible for agentic microservices; the apparent tension dissolves when you distinguish use cases. |
| 394 | Greg Isenberg — Firecrawl Web Data Layer | AI agents are blind without structured web data; Firecrawl replaces custom scraper management the way AWS replaced physical server management. |
| 395 | John Kim — Claude Code Power Tips | A Meta Staff Engineer's core thesis: effective AI development is fundamentally context engineering -- managing what Claude knows, when, and at what window cost. |
| 396 | Low Level — LiteLLM Supply Chain Attack | The attack chain (Trivy exploit to LiteLLM credentials to PyPI malware) harvested SSH keys, cloud creds, and API keys; no clean remediation playbook exists. |
| 397 | AI LABS — Hidden Claude Code Settings | Many Claude Code defaults were calibrated for 200K context; adjusting autocompact, file read limits, and terminal output caps for 1M context yields significant gains. |
| 398 | Sam Witteveen — Document Parsing Framework Era | LlamaIndex's co-founder admits the LLM framework era is ending; genuine value now lives in hard infrastructure problems like production-scale document parsing. |
| 399 | Maximilian Schwarzmuller — Developer Joy AI Tradeoffs | AI shifted work toward specs and reviews (the parts many developers never enjoyed) while eliminating the coding flow state that made the work intrinsically rewarding. |
| 400 | ICOR with Tom — PKM Folder Agent System | A plain folder + Claude Code replaces specialized PKM apps; orchestrator agents spin up specialized sub-agents stored as plain markdown, fully model-agnostic. |

## Try This Week

1. **Build a builder/validator loop for your next feature.** Set up a dedicated adversarial evaluator agent with a skepticism-oriented system prompt, give it Playwright MCP access, and run 5-10 iterations against your builder agent before accepting output (375, 352).

2. **Audit your CLAUDE.md against the instruction budget.** Strip it below 500 usable instructions, extract everything else into skills with progressive disclosure, and verify skill.md files are under 200 lines (357, 333, 397).

3. **Run AutoDream on your longest-running project.** Use `/memory` toggle or `/dream` to trigger background memory consolidation, then diff the before/after memory files to understand what signal survived and what noise was pruned (362, 366).

4. **Create a ubiquitous language document.** Borrow from Domain-Driven Design: define precise terminology for your project's domain concepts in a shared glossary that both you and AI reference, and update it after each grilling/planning session (322).

5. **Evaluate one production agent with factorial stress testing.** Pick your most consequential AI workflow, add controlled stressors (contradictory context, social pressure cues, time pressure), and measure whether output shifts when it should not (320, 349).
