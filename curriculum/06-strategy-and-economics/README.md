# Module 06: Strategy & Economics

> Navigate the business reality of AI adoption -- infrastructure constraints, industry economics, the reshaping of the software development lifecycle, security risks in the tooling ecosystem, career strategy, and the difference between hype and substance.

## Overview

AI tools do not exist in a vacuum. Every prompt you send, every agent you spawn, every team you orchestrate runs on physical infrastructure with real costs, real constraints, and real competitive dynamics. This module steps back from the technical "how" of AI-assisted development to examine the strategic "why" and "whether": Why is inference compute physically constrained with no relief before 2028? How is the software development lifecycle being restructured when code generation outpaces code review? What are the security risks emerging in the skills ecosystem? Is the AI industry in a bubble, and does it matter for practitioners?

The seven sources tagged to this module span an unusually wide range of perspectives -- from Nate B Jones's infrastructure crisis analysis to Carl Brown's bubble skepticism, from CircleCI's enterprise SDLC framework to ThePrimeagen's security warnings. The deliberate inclusion of contradictory viewpoints is the point. The goal is not to sell AI adoption but to equip you with the economic and strategic context to make informed decisions about where, when, and how aggressively to invest your time and resources.

This module is independent of the technical learning path. It can be taken alongside any other module, and its content becomes more relevant as your technical capabilities grow -- because the more capable you become with AI tools, the more important it is to understand the economic and strategic landscape those tools operate within.

## Prerequisites

None -- this module can be taken alongside any other module in the curriculum.

## Core Concepts

### Concept 1: The Infrastructure Crisis -- Physical Constraints on AI Compute

The most underappreciated fact about the AI landscape: the world built an economy that runs on AI inference, and now there is not enough compute to run that economy. As Nate B Jones details in his infrastructure analysis ([#009](../../sources/009-nate-b-jones-infrastructure-crisis.md)), this is not a prediction but an observation of current conditions across every layer of the hardware stack.

**Token consumption is growing exponentially.** A knowledge worker using AI aggressively today consumes roughly 1 billion tokens per year. Agentic systems -- which do not have natural rate limits and can consume billions of tokens per day -- push projections to 10-100 billion tokens per worker annually within 18 months. At enterprise scale (10,000 workers at 100B tokens each), the compute bill hits $2 billion per year, assuming stable pricing and available capacity -- neither of which holds.

**Memory is the binding constraint.** AI inference is memory-bound. Server DRAM prices have risen at least 50% through 2025, with projections of another 55-60% quarter-over-quarter increase in early 2026. The three companies controlling 95% of global memory production (Samsung, SK Hynix, Micron) are all reallocating from consumer to enterprise/AI segments. High-bandwidth memory (HBM) is fully allocated to Nvidia, AMD, and hyperscalers. A new DRAM fab costs approximately $20 billion and takes 3-4 years to construct and ramp -- decisions made today will not yield chips until around 2030.

**Semiconductor fabrication has no surge capacity.** TSMC manufactures the world's most advanced AI chips. Their 5nm, 4nm, and 3nm nodes are fully allocated. Nvidia is their largest customer. TSMC's Arizona fab will not reach full production until 2028. Intel's 18A process is unproven at scale. Essentially all advanced AI chip production runs through TSMC in Taiwan with no alternative and no ability to ramp quickly.

**GPUs are sold out.** Nvidia holds roughly 80% market share. H100 and Blackwell GPUs have lead times exceeding 6 months. Hyperscalers have locked up allocation through multi-year, multi-billion-dollar purchase agreements. Enterprise buyers get whatever remains.

> "We built an economy that runs on AI and now there isn't enough compute to run that economy." -- Nate B Jones

### Concept 2: Hyperscalers as Competitors, Not Partners

A critical strategic insight from Jones's analysis ([#009](../../sources/009-nate-b-jones-infrastructure-crisis.md)): AWS, Azure, and Google Cloud are not neutral infrastructure providers. They are AI product companies that happen to sell infrastructure. Google uses its compute for Gemini, Microsoft for Copilot, Amazon for its AWS AI services.

When compute is abundant, this conflict is manageable. When compute is scarce, it becomes zero-sum. Every GPU allocated to an enterprise customer is a GPU unavailable for the hyperscaler's own products. API pricing has fallen over the past two years, but rate limits have tightened. Enterprise customers report increasing difficulty securing allocation commitments for high-volume deployments.

The practical implication: diversify your compute dependencies. Build routing layers that abstract your infrastructure so switching providers is trivial. Treat your cloud provider as a vendor, not a partner, and maintain the optionality to move when incentives diverge.

### Concept 3: Efficiency as Competitive Advantage

When supply is constrained, efficiency becomes a force multiplier. As Jones argues: "The enterprises that can unlock efficiency effectively have given themselves 10x more capacity."

This applies at every level:
- **Prompt optimization**: Fewer tokens per request means more requests per dollar
- **Caching**: Avoid recomputing what you have already computed
- **Model routing**: Use the smallest capable model for each task (Haiku for summarization, Opus for architecture)
- **Retrieval-augmented generation (RAG)**: Inject relevant context rather than feeding entire documents
- **Quantization**: Run smaller model variants where precision is not critical

The same principle operates at the company level. As Nate B Jones documents in his analysis of Anthropic's strategy ([#002](../../sources/002-nate-b-jones-anthropic-ceo-philosophy.md)), Anthropic's competitive advantage comes not from having the most compute but from delivering the most capability per dollar of compute. Dario Amodei has emphasized that "a prominent part of Anthropic's culture has been 'do more with less,' always trying to maintain a situation where with less computational resources, we can do the same or better than someone with many more." This philosophy -- higher-quality training data, post-training techniques, algorithmic efficiency over brute-force scaling -- has driven Anthropic to 40% of enterprise LLM spending despite being outspent on infrastructure by competitors.

### Concept 4: Safety as Competitive Moat

The conventional assumption is that safety constrains commercial success -- that prioritizing responsible development means sacrificing speed and market share. Anthropic's trajectory disproves this.

As Jones documents ([#002](../../sources/002-nate-b-jones-anthropic-ceo-philosophy.md)), Anthropic's revenue has grown 100x since 2022: $10M (2022) to $100M (2023) to $1B (2024) to $9B+ annualized (2025). Their enterprise market position is dominant: 40% of enterprise LLM spending (surpassing OpenAI's 27%), 85% of revenue from business customers (versus OpenAI's consumer-heavy 60%+ from individual subscriptions), and API growth 5x faster than OpenAI.

The mechanism is straightforward: enterprises deploying AI in production environments -- regulated industries, sensitive data, customer-facing applications -- need vendors they can trust. Constitutional AI (embedding safety principles into model architecture during training), the Responsible Scaling Policy, and investment in mechanistic interpretability are not marketing -- they are the exact qualities enterprise buyers prioritize. Safety research improved model quality, enterprise trust translated to revenue, efficiency gains compounded, and the safety-focused mission attracted top research talent.

> "A prominent part of Anthropic's culture has been 'do more with less,' always trying to maintain a situation where with less computational resources, we can do the same or better than someone with many more." -- Dario Amodei

### Concept 5: The Bottleneck Shift -- From Writing Code to Evaluating It

The AI-driven SDLC does not just make the old process faster. It changes what the bottleneck is. As Jacob Schmitt argues in CircleCI's analysis ([#018](../../sources/018-circleci-ai-sdlc.md)): "When AI can generate ten solutions quickly, the valuable skill becomes choosing the right one for your context."

The traditional SDLC was a linear pipeline: plan, design, build, test, deploy, maintain. AI breaks this linearity. Planning generates prototype code. Design produces production-ready assets. Testing runs continuously. Deployment and maintenance feed insights back in real time. The result is not a faster pipeline but a fundamentally different topology -- an interconnected network where stages overlap and progress concurrently.

But the critical insight is about the capacity mismatch this creates. Code generation has accelerated by an order of magnitude. Code review remains a manual, human-paced activity. Teams that do not address this mismatch end up either rubber-stamping AI output (accepting risk) or creating massive review backlogs (losing the speed advantage).

The prescription is infrastructure-level: compress the validation loop to match generation velocity. Continuous testing during development, rapid builds, real-time failure signals, and automated validation of routine changes become prerequisites -- not nice-to-haves -- for realizing AI's productivity gains. If your CI/CD pipeline takes 30 minutes to validate a change, it does not matter that AI generated the change in 30 seconds.

> "What it means to be a senior engineer fundamentally changes when machines handle execution." -- Jacob Schmitt

See also: [Module 04: Agentic Patterns](../04-agentic-patterns/README.md) for the agentic coding workflows that drive this SDLC transformation.

### Concept 6: The Skills Ecosystem Security Problem

The convenience of the emerging skills ecosystem comes with real and underappreciated supply chain risks. As ThePrimeagen documents ([#017](../../sources/017-primeagen-skills-security.md)), research shows that 36% of publicly available agent skills contain security vulnerabilities. This is not a theoretical concern -- it is a measured baseline of the current ecosystem.

The most novel attack vector is **hallucination squatting**: AI models frequently hallucinate plausible-sounding package and skill names. Attackers monitor these hallucinations and preemptively register the nonexistent names in skill marketplaces with malicious payloads. When a developer follows the AI's recommendation to install the hallucinated skill, or when an agent autonomously attempts to install it, the attacker's code executes with full user-level permissions.

This is particularly dangerous because: the AI itself recommends the skill (lending false authority), installation often happens with minimal human review, and skills run with the same permissions as the user -- no sandbox, no capability restriction. A malicious skill can read files, access credentials, make network requests, and exfiltrate data.

The skills ecosystem is young, and security practices are immature. The current state privileges convenience heavily over security. Until better vetting, sandboxing, and provenance tracking exist, treat every skill installation with the same caution you would give to running an unknown script with `curl | bash`.

See also: [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md) for the skills system mechanics and trust model.

### Concept 7: The Horizontal and Temporal Collapse of Knowledge Work

Nate B Jones argues ([#012](../../sources/012-nate-b-jones-career-collapse.md)) that AI is collapsing professional futures along two dimensions simultaneously.

**The horizontal collapse**: Formerly distinct career paths -- engineering, product management, marketing, finance, design, operations -- are converging into a single meta-competency: orchestrating AI agents to get work done. Jones frames it starkly: "What used to be 50 different specializations is going to converge into variations on a single theme. Humans directing AI with good knowledge and good software-shaped intent toward an outcome." Domain expertise does not disappear, but it shifts from differentiator to table stakes -- it only matters if you can channel it through AI-driven workflows.

**The temporal collapse**: Traditional career planning assumed skills appreciated over time -- learn something, apply it for years, get promoted. In the AI era, expertise depreciates unless continuously updated, and the depreciation rate is accelerating. The SWE-bench benchmark went from 4% to roughly 95% saturation in two years. Career planning based on five-year horizons is, in Jones's words, "catastrophically wrong."

Jones introduces the concept of "software-shaped intent" -- the ability to think about problems the way software processes them, even if your job has nothing to do with building software. When directing AI agents, you need to understand where the agent's toolset is, where its memory lives, and what interfaces it can read and write. This makes the software engineering mental model universal.

> "The half-life of any given piece of specific AI knowledge is short and it's getting shorter. The half-life of the learning habit around AI is getting longer and more durable." -- Nate B Jones

### Concept 8: The Accelerating Capability Curve

Matt Shumer provides the quantitative backbone for the urgency arguments ([#019](../../sources/019-matt-shumer-something-big.md)). METR data shows AI task completion capacity -- measured by how long a model can work autonomously before needing human intervention -- has been doubling every 7 months, and that rate is compressing to every 4 months. The current capability is roughly 5 hours of autonomous expert-level work. Extrapolating even conservatively, autonomous multi-day work is a near-term reality.

The self-improvement loop compounds this: GPT-5.3 Codex was "instrumental in creating itself," and Anthropic's CEO says AI writes "much of the code" at Anthropic. Each generation of AI helps build the next generation faster, creating a feedback loop where linear progress becomes exponential acceleration.

Multiple creators ([#012](../../sources/012-nate-b-jones-career-collapse.md), [#019](../../sources/019-matt-shumer-something-big.md)) converge on the same conclusion: there is a brief window -- possibly months, not years -- where individuals who aggressively adopt AI tools gain a significant competitive edge. This window closes as adoption becomes universal.

> "I am no longer needed for the actual technical work of my job." -- Matt Shumer

### Concept 9: The Bubble Question -- Hype vs. Substance

Not every voice in the conversation is bullish. Carl Brown (Internet of Bugs) provides the essential skeptical counterpoint ([#007](../../sources/007-internet-of-bugs-ai-bubble.md)), drawing a direct line from the "Dot-Com Super Bowl" of 2000 through the "Crypto Bowl" of 2022 to Super Bowl LX in 2026, where AI companies accounted for 23% of all ads.

The structural parallels across bubble cycles are striking:
- **Valuation metrics divorced from reality**: Dot-coms measured "eyeballs," crypto measured "total value locked," AI measures model parameters and benchmark scores. None correspond directly to revenue or profit.
- **Massive capital burn**: OpenAI reportedly loses $13.5 billion on $4.3 billion in revenue. JPMorgan estimates the AI sector would need $650 billion in annual revenue to justify current valuations.
- **Same actors, different stage**: The ai.com Super Bowl ad was launched by Crypto.com's CEO, making the crypto-to-AI pipeline explicit.
- **58% of global VC funding** went to AI startups in early 2025, representing extreme sector concentration.

However, Brown acknowledges important counter-arguments. Unlike the dot-com era, major AI investors (Microsoft, Alphabet, Amazon) have among the strongest balance sheets and highest free cash flow in the market. Real enterprises are deploying AI for real tasks. The infrastructure being built may retain long-term value even if a bubble pops, just as the fiber optic cables and data centers that survived the dot-com crash became the foundation for the next wave.

The balanced takeaway: the technology is real and the productivity gains are measurable, but the valuations may not be sustainable. An AI correction might destroy speculative startups while preserving the underlying technology for more sustainable use. Individual practitioners benefit from the technology regardless of what happens to AI company stock prices -- but organizations should be cautious about building dependencies on vendors whose business models may be unviable at current burn rates.

### Concept 10: The Capital Commitment -- Follow the Money

Multiple sources ([#009](../../sources/009-nate-b-jones-infrastructure-crisis.md), [#012](../../sources/012-nate-b-jones-career-collapse.md)) emphasize the sheer scale of capital flowing into AI. Big tech's combined AI capital expenditure was close to half a trillion dollars in 2025, projected to exceed that in 2026, with the big five (Amazon, Microsoft, Google, Meta, Oracle) planning to add at least two trillion dollars in AI-related assets over four years. Jones calls it "the biggest capex project in human history."

This scale of commitment removes ambiguity about direction. The infrastructure is being built whether individuals participate or not. The question is not whether AI will reshape knowledge work, but how fast and how completely. This framing transforms the decision from "should I learn AI tools?" to "how quickly must I adapt to remain relevant?"

At the same time, Notion has publicly disclosed that AI costs now consume 10 percentage points of what was previously a 90% gross margin business. If inference costs double, many AI-native business models become unviable. Companies most at risk are those in the middle: too dependent on AI to abandon it, not large enough to secure dedicated compute allocation, competing in markets where pass-through cost increases are difficult to sustain.

## Patterns & Practices

### Pattern 1: The Routing Layer Strategy

- **When to use**: Any organization with significant AI compute consumption that depends on cloud providers for inference.
- **How it works**: Build an intelligence layer between your applications and your compute providers. The layer decides where workloads run, optimizes for cost, manages capacity across providers, and preserves the optionality to switch when one provider's pricing or availability becomes unfavorable. This is a strategic capability that should not be outsourced.
- **Example**: An enterprise running mixed workloads routes summarization tasks to the cheapest available model, reserves Opus-tier capacity for architecture and judgment tasks, and automatically fails over between providers when rate limits are hit.
- **Source**: [#009: Infrastructure Crisis](../../sources/009-nate-b-jones-infrastructure-crisis.md)

### Pattern 2: Tiered Review for AI-Generated Code

- **When to use**: When AI code generation volume exceeds your team's review capacity.
- **How it works**: Automate validation of routine changes (formatting, dependency updates, straightforward implementations). Fast-path low-risk changes with automated test gates. Reserve human review for high-risk changes (security, architecture, data model modifications). Use CI/CD infrastructure that validates at machine speed.
- **Example**: AI generates a feature implementation. Automated tests, linting, and type checking validate correctness. A model-based review flags potential issues. Only changes touching security boundaries, database schemas, or architectural patterns require human review.
- **Source**: [#018: The AI-Driven SDLC](../../sources/018-circleci-ai-sdlc.md)

### Pattern 3: Continuous Capability Assessment

- **When to use**: When making career or organizational strategy decisions about AI adoption.
- **How it works**: Track the METR autonomous task completion metric (current: ~5 hours of expert-level work, doubling every 4-7 months). For each role or function, estimate the average task duration. When the autonomous capability crosses that threshold, the role's execution component becomes automatable. Focus career development on the judgment and relationship components that persist beyond the crossing point.
- **Example**: If your role involves 2-hour analysis tasks, and autonomous capability is currently at 5 hours and doubling, you are already within the automation window. If your role involves multi-day strategic projects requiring stakeholder relationships, you have more runway -- but the window is still closing.
- **Source**: [#019: Something Big Is Happening](../../sources/019-matt-shumer-something-big.md), [#012: Career Collapse](../../sources/012-nate-b-jones-career-collapse.md)

### Pattern 4: Security-First Skill Adoption

- **When to use**: Every time you install a third-party skill or agent extension.
- **How it works**: Read the skill's source code before installation. Verify the author's identity and reputation. Check whether the skill name was recommended by an AI (hallucination squatting risk). Run skills in isolated environments for sensitive work. Prefer skills from known, trusted sources with visible audit histories. Monitor the ecosystem for security improvements, but do not assume current practices are adequate.
- **Example**: An AI suggests installing "awesome-deploy-skill" from a marketplace. Before installing, you search for the skill's repository, verify it has a real author with a history of contributions, read the source code to confirm it only accesses what it claims to, and run it first in a sandboxed environment.
- **Source**: [#017: Be Careful w/ Skills](../../sources/017-primeagen-skills-security.md)

### Pattern 5: The "Do More With Less" Efficiency Stack

- **When to use**: When inference costs are a meaningful line item or when you are hitting rate limits.
- **How it works**: Layer efficiency optimizations: (1) prompt engineering to reduce token count per request, (2) caching to avoid redundant computation, (3) model routing to use the cheapest capable model per task, (4) RAG to inject targeted context instead of large documents, (5) quantization for latency-sensitive but precision-tolerant tasks. Each layer compounds -- 50% fewer tokens per request combined with routing 60% of requests to a cheaper model yields 80% cost reduction.
- **Example**: Anthropic's own strategy -- higher-quality training data and post-training techniques instead of raw compute scaling -- demonstrates this at the model-development level. At the application level, the same principles apply to every API call.
- **Source**: [#002: Anthropic CEO Philosophy](../../sources/002-nate-b-jones-anthropic-ceo-philosophy.md), [#009: Infrastructure Crisis](../../sources/009-nate-b-jones-infrastructure-crisis.md)

## Common Pitfalls

- **Planning for linear growth in a nonlinear environment**: Traditional IT planning assumes predictable demand, stable technology, and available supply. None of these hold for AI infrastructure. An enterprise that purchases hardware on a 4-year depreciation schedule may find it obsolete in 2 years because per-worker consumption has grown 10x. Plan for 10-100x your current token consumption, not 2-3x.

- **Treating cloud providers as neutral partners**: Your hyperscaler is also your competitor. When compute is scarce, their strategic AI products get priority over your enterprise allocation. Maintain provider optionality through routing layers and avoid contractual lock-in that prevents switching.

- **Rubber-stamping AI output**: When code review cannot keep pace with code generation, teams either rubber-stamp (accepting risk) or create backlogs (losing speed). Neither is acceptable. Invest in automated validation infrastructure that compresses the review loop to match generation velocity.

- **Ignoring skills security**: The 36% vulnerability rate in public skills is a snapshot of an immature ecosystem. Installing skills without reading source code, verifying authors, and understanding the permission model is equivalent to running `curl | bash` from an untrusted URL. The convenience is real; so is the risk.

- **Waiting for stability before adopting**: Multiple sources ([#012](../../sources/012-nate-b-jones-career-collapse.md), [#019](../../sources/019-matt-shumer-something-big.md)) converge on the same message: there is no stable state to wait for. The bicycle metaphor from Jones is apt -- going slower makes balancing harder, not easier. Forward momentum builds fluency; caution builds stagnation.

- **Mistaking bubble dynamics for technology failure**: Even if AI valuations are in a bubble (and Brown's analysis in [#007](../../sources/007-internet-of-bugs-ai-bubble.md) makes a compelling case), the underlying technology and productivity gains are real. The dot-com crash destroyed companies but left behind the infrastructure that powered the next two decades of internet growth. The correct response to bubble risk is financial prudence, not technology avoidance.

- **Focusing career development on execution over judgment**: Roles defined by executing well-scoped cognitive tasks are the most vulnerable to automation. The roles that persist emphasize relationship trust, physical presence, licensed accountability, and strategic judgment. Invest in the judgment layer, not the execution layer.

## Hands-On Exercises

1. **Token cost modeling**: Calculate your current monthly AI token consumption across all tools and services. Then model what happens at 10x and 100x that consumption as agentic workflows scale. Identify which provider contracts, rate limits, or budget constraints would break first, and design a mitigation strategy.

2. **SDLC bottleneck audit**: Map your team's current development workflow from code generation through deployment. Identify where AI has accelerated a step and where the next step downstream cannot absorb the increased velocity. Design one infrastructure improvement that would compress the slowest validation step.

3. **Skill security audit**: Pick 3 third-party skills from a public marketplace. For each, read the source code, identify what permissions it requires, assess whether those permissions are justified by its stated function, and check whether the skill name appears in AI hallucination logs. Document your findings and your install/reject decision for each.

4. **Bubble indicator tracking**: Using Brown's framework, identify 3 current signals that support the bubble thesis and 3 that contradict it. For each signal, identify what data point would change your assessment. The goal is calibrating your own judgment, not reaching a predetermined conclusion.

5. **Career capability mapping**: List the 10 tasks that consume most of your working time. For each, estimate (a) the current METR autonomous capability threshold relative to that task, (b) how many months until autonomous capability likely crosses that threshold, and (c) what judgment or relationship component of the task would persist. Use this to identify your highest-priority areas for career development.

6. **Enterprise AI strategy brief**: Write a 1-page strategy document for a hypothetical CTO addressing: current compute constraints and their timeline, recommended provider diversification approach, infrastructure investments needed to capture AI productivity gains, and the security posture required for the skills ecosystem. Synthesize across all seven sources in this module.

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [002: Anthropic's CEO Bet the Company on This Philosophy](../../sources/002-nate-b-jones-anthropic-ceo-philosophy.md) | Nate B Jones | Safety-as-strategy, enterprise market dominance, "do more with less," revenue trajectory |
| [007: Super Bowl Commercial Bubble Curse](../../sources/007-internet-of-bugs-ai-bubble.md) | Carl Brown (Internet of Bugs) | Bubble indicators, dot-com/crypto parallels, counter-arguments, valuation analysis |
| [009: The 36-Month AI Infrastructure Crisis](../../sources/009-nate-b-jones-infrastructure-crisis.md) | Nate B Jones | Compute constraints, DRAM/HBM economics, GPU allocation, hyperscaler dynamics, CTO strategies |
| [012: Domain Expertise Won't Save You](../../sources/012-nate-b-jones-career-collapse.md) | Nate B Jones | Horizontal/temporal collapse, software-shaped intent, bicycle metaphor, capex trends |
| [017: Be Careful w/ Skills](../../sources/017-primeagen-skills-security.md) | ThePrimeagen | Skills security, hallucination squatting, 36% vulnerability rate, supply chain risks |
| [018: The New AI-Driven SDLC](../../sources/018-circleci-ai-sdlc.md) | CircleCI (Jacob Schmitt) | SDLC as network, bottleneck shift, MCP integration, engineering role redefinition |
| [019: Something Big Is Happening](../../sources/019-matt-shumer-something-big.md) | Matt Shumer | METR doubling rates, self-improvement loop, capability trajectory, career window |

## Further Reading

- [METR AI task completion tracking](https://metr.org/) -- The autonomous task duration metric referenced by Shumer; the single most informative data point for calibrating AI capability timelines
- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) -- The formalized framework for Anthropic's safety-first approach
- [Dario Amodei, "The Adolescence of Technology" (January 2026)](https://darioamodei.com/the-adolescence-of-technology) -- 20,000-word essay on AI risk categories, governance, and the 50% entry-level job displacement prediction
- [Module 01: Foundations](../01-foundations/README.md) -- AI landscape overview, capability overhang, and the historical context for understanding hype cycles
- [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md) -- Skills system mechanics and trust model, the technical foundation for the security discussion
- [Module 04: Agentic Patterns](../04-agentic-patterns/README.md) -- The agentic coding workflows driving the SDLC transformation
