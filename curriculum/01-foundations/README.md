# Module 01: Foundations

> Understand the current AI landscape, the gap between capability and adoption, and how to separate genuine progress from hype.

## Overview

Something fundamental shifted in late 2025 and early 2026. Three frontier models released within six days in December 2025, two more launched within 20 minutes of each other on February 5, 2026, and the measured rate at which AI can work autonomously is accelerating. Whether you view this as the dawn of a new era or the peak of a speculative bubble depends on which data you weight -- and this module equips you to weight that data thoughtfully.

This module builds the mental models you need before touching any tools. It covers what the latest AI models can actually do (and where they fall short), the concept of the "capability overhang" -- the widening gap between what AI tools offer and how most people use them -- and the historical patterns that suggest caution even amid genuine progress. The goal is not to sell you on AI or scare you away from it, but to give you an informed framework for evaluating developments as they arrive.

Everything in subsequent modules -- prompt engineering, agentic coding, team orchestration -- rests on this foundation. If you misjudge the landscape, you will either over-invest in tools that disappoint or under-invest in a shift that leaves you behind. See also: [Module 06: Strategy and Economics](../06-strategy-and-economics/README.md) for the career and financial implications of the dynamics covered here.

## Prerequisites

None -- this is the starting module.

## Core Concepts

### Concept 1: The December 2025 Phase Transition

As Nate B Jones documents in "The Capability Overhang," something crossed a threshold in December 2025. Within six days, three frontier models landed: Google's Gemini 3 Pro, OpenAI's GPT 5.1/5.2 Codex Max, and Anthropic's Claude Opus 4.5. All three were explicitly optimized not for chat-style question-and-answer but for sustained autonomous work measured in hours or days. GPT's 5.1/5.2 class models are designed for continuous operation exceeding a full day. Claude Opus 4.5 introduced an effort parameter that lets developers dial reasoning up or down. Both OpenAI and Anthropic shipped context compaction techniques that allow models to summarize their own work as sessions extend, maintaining coherence over far longer time frames.

> "Something fundamental shifted in December 2025. The people closest to technology are calling it a phase transition, a threshold crossing, a break in the timeline." -- Nate B Jones

This was not a single breakthrough but a convergence: better models, longer autonomous work horizons, and orchestration patterns (like the viral "Ralph" bash loop) all arriving simultaneously. The result is a fundamentally new category of AI-assisted work that most knowledge workers have not yet encountered.

### Concept 2: The Capability Overhang

The most important concept in this module -- and arguably in the entire curriculum -- is the "capability overhang." OpenAI's own benchmark shows GPT 5.2 Pro reaches 74% preference over human experts on scoped knowledge work, yet most knowledge workers are still using AI at a ChatGPT 3.5/4 level: ask a question, get an answer, move on. They are not running agent loops overnight, not assigning hour-long tasks to AI, not managing fleets of parallel workers.

As Jones explains, this overhang is why discourse about AI feels so disconnected:

> "Someone running task loops is living in a different technical reality than someone who queries ChatGPT four or five times a day, even though they have access to the exact same underlying tools. One person sees acceleration happening all at once; the other sees incremental improvement and wonders why AI is such a big deal."

The overhang creates a temporary but significant arbitrage for those who learn to use these tools at their actual capability level. How long this window lasts is debatable -- Matt Shumer argues it may be months rather than years, while adoption curves for previous technologies suggest it could persist longer. Either way, understanding that the overhang exists is prerequisite to making rational decisions about investment of time and attention.

Nate B Jones extends this with a concrete enterprise example ([#044](../../sources/044-nate-b-jones-claude-excel-powerpoint.md)): Claude's integration into Excel and PowerPoint means the same Opus 4.6 intelligence powering headline coding benchmarks now lives inside the productivity tools that a billion-plus knowledge workers use daily. The overhang is not just in developer tools -- it is in the spreadsheets and slide decks that define most knowledge work. Crucially, these integrations improve silently: the upgrade from Opus 4.5 to 4.6 inside Excel happened overnight with no user action. As Jones puts it: "Your tools are getting smarter faster than you're updating your expectations of them." This "silent compounding intelligence" means the overhang is not static -- it widens automatically with every model upgrade.

### Concept 3: The Accelerating Doubling Rate

Matt Shumer, writing in "Something Big Is Happening," provides the most concrete metric for tracking AI capability growth. METR (an AI evaluation organization) measures how long a model can work autonomously before needing human intervention. This capacity has been doubling every 7 months, and the doubling rate itself is compressing -- recently to every 4 months. As of early 2026, models can handle tasks requiring roughly 5 hours of human expert effort.

The self-improvement loop amplifies this trajectory. OpenAI documented that GPT-5.3 Codex was "instrumental in creating itself." Dario Amodei described Anthropic engineers telling him "I don't write code anymore. I let the model write the code." AI is now meaningfully contributing to its own development, creating a feedback loop where each generation helps build the next generation faster.

This is not speculative futurism -- it is a measured trend with consistent data points. But measured trends can still be disrupted by practical constraints (compute costs, energy, data quality), and extrapolation from exponentials has a long history of producing overconfident predictions. The METR doubling rate is the best single metric to watch, but watch it with appropriate skepticism.

### Concept 4: The February 2026 Model Releases

On February 5, 2026, Anthropic's Claude Opus 4.6 and OpenAI's GPT-5.3 Codex launched within approximately 20 minutes of each other -- the closest head-to-head release window in AI model history. As ThePrimeagen (Michael Paulson) details in his comparison, both models represent significant capability jumps, but with different strengths:

- **Opus 4.6** leads on reasoning-heavy benchmarks (GPQA Diamond, MMLU Pro, OSWorld) and introduces adaptive thinking, a 1M-token context window, and agent teams. It excels at architectural thinking and dynamic modularity.
- **GPT-5.3 Codex** dominates speed-focused coding workloads (Terminal-Bench 2.0) and introduces interactive steering. It excels at streamlined, concise code generation.

The "Great Convergence" theme is notable: both companies addressed their historical weaknesses by borrowing from each other's playbook. Anthropic pitched depth ("plans more carefully, sustains agentic tasks for longer"), OpenAI pitched speed ("25% faster, interact in real time"). As the Every.to analysis put it: "Opus 4.6 wants to explore while Codex 5.3 wants to execute."

Jones, in his dedicated Opus 4.6 analysis, argues this release crosses a qualitative threshold where the model's behavior feels fundamentally different -- not a better tool, but a different category of collaborator. The workflow shift he describes is an inversion: from "AI assists the developer" to "AI leads, developer reviews and steers."

### Concept 5: The Horizontal and Temporal Collapse of Knowledge Work

Jones's "Career Collapse" analysis introduces two dimensions of disruption that operate simultaneously. The **horizontal collapse** compresses formerly distinct career paths -- engineer, product manager, marketer, analyst, designer -- into what he calls "variations on a single theme: humans directing AI with good knowledge and good software-shaped intent toward an outcome." Domain expertise does not disappear, but it shifts from being a differentiator to being table stakes.

The **temporal collapse** breaks the traditional career ladder. The assumption that skills appreciate steadily over years no longer holds when AI capability can replicate years of accumulated expertise in months. The SWE-bench benchmark went from 4% to roughly 95% saturation in two years, illustrating how quickly formerly scarce skills can be commoditized.

> "What used to be 50 different specializations is going to converge into variations on a single theme. Humans directing AI with good knowledge and good software-shaped intent toward an outcome." -- Nate B Jones ([4:03](https://www.youtube.com/watch?v=q6p-_W6_VoM&t=243))

This framework is not universally accepted. Shumer's analysis independently confirms the pattern with different data (the METR doubling rate, the 50% entry-level job prediction from Dario Amodei), while the skeptical perspective (covered below) questions whether these trends will continue or represent peak hype.

### Concept 6: The Bubble Thesis -- A Necessary Counterweight

Carl Brown, a veteran software developer and host of the Internet of Bugs YouTube channel, provides the essential skeptical perspective. In "Super Bowl Commercial Bubble Curse," he documents a historical pattern: when a tech sector becomes flush enough with cash to buy 20%+ of Super Bowl ad inventory, it may be near peak hype. The "Dot-Com Super Bowl" of 2000 (14 dot-com ads, most companies bankrupt within 2 years), the "Crypto Bowl" of 2022 (FTX collapsed within a year), and the "AI Bowl" of 2026 (15 out of 66 ads, 23%) follow the same structural pattern.

The parallels are specific and uncomfortable:
- **Valuation metrics divorced from reality**: Dot-coms measured "eyeballs," crypto measured "total value locked," AI measures model parameters and benchmark scores -- none correspond directly to revenue or profit.
- **Massive capital burn**: OpenAI reportedly loses $13.5 billion on $4.3 billion in revenue. JPMorgan estimates the AI sector would need $650 billion in annual revenue to justify current valuations.
- **Same actors, different stage**: The ai.com Super Bowl ad was launched by Crypto.com's CEO, making the crypto-to-AI pipeline explicit.

Brown also acknowledges important counter-arguments: unlike dot-com startups, the major AI investors (Microsoft, Alphabet, Amazon) have the strongest balance sheets in the market. Real enterprise adoption is occurring. The infrastructure being built retains long-term value even if a correction occurs. These differences suggest that survivors of any correction would likely be the large incumbents, not speculative startups -- but they do not eliminate the risk of a correction itself.

Data from early 2026 has intensified both the bull and bear signals. On the spending side, Amazon, Google, Microsoft, and Meta plan a combined **$660 billion** in AI infrastructure spending in 2026, up 60% from 2025. Google raised nearly $32 billion in debt in under 24 hours, including an ultra-rare **100-year sterling bond** that was 10x oversubscribed -- not out of financial necessity (Google has ~$80 billion in net cash) but as competitive signaling. ([#037](../../sources/037-prof-g-google-ai-arms-race.md), [01:00](https://www.youtube.com/watch?v=cJ803xOqP_k&t=60)) On the demand side, **more than 80% of Americans express concern about AI**, 75% say it could threaten humanity, and less than half have a favorable view. This sentiment is translating into political action: data center moratoriums, lawsuits, and 50+ regulation bills across multiple states. ([#037](../../sources/037-prof-g-google-ai-arms-race.md), [21:00](https://www.youtube.com/watch?v=cJ803xOqP_k&t=1260))

The competitive dynamics have also sharpened. Anthropic's Super Bowl ad -- which satirized AI-inserted advertising in ChatGPT -- is described by Galloway as a "seminal moment" comparable to Apple's 1984 ad. He applies his brand strategy framework: Anthropic's no-ads commitment is differentiated, relevant (people share intimate information with AI), and sustainable (OpenAI's revenue projections make reversing ads difficult). Galloway predicts Anthropic will surpass OpenAI in valuation within 12 months, driven by enterprise-first positioning versus OpenAI's consumer orientation. ([#036](../../sources/036-prof-g-ai-kill-software.md), [56:00](https://www.youtube.com/watch?v=ERAoSEC4skY&t=3360)) Whether this prediction holds, the Anthropic-OpenAI dynamic illustrates how quickly competitive positioning can shift in a market where trust and privacy are becoming core differentiators.

Three data points do not guarantee a fourth. But maintaining this skeptical frame alongside the acceleration narrative is what separates informed analysis from hype.

Safety discourse adds another dimension to the hype evaluation. ThePrimeTime ([#045](../../sources/045-primetime-altman-townhall-biosecurity.md)) highlights a troubling dynamic from an OpenAI town hall: Sam Altman openly stated that AI is going to be "a real problem for bioterrorism" and "a real problem for cybersecurity," then immediately positioned AI as the solution to those same problems. As Prime identifies, the entity creating the risk positioning itself as the indispensable fix mirrors a "create the problem, sell the solution" pattern that merits heightened scrutiny. Meanwhile, Novara Media ([#052](../../sources/052-novara-media-anthropic-safety-crisis.md)) examines the resignation of Mrinank Sharma from Anthropic's Safeguards Research Team, connecting it to a broader polycrisis thesis: AI systems with documented alignment problems (blackmailing engineers, resisting shutdown) are simultaneously being deployed to replace the professional services backbone of Western economies. Incentive analysis is essential -- AI companies benefit from hyping existential risk because it maintains salience and justifies valuations, while chip makers downplay risks to sell hardware globally. Resignations of well-compensated safety researchers (who have financial incentives to stay) are stronger signals about internal safety culture than corporate safety publications.

### Concept 7: The AI Maturity Ladder and the Developer Identity Crisis

Jo Van Eyck introduces a five-level AI-augmented coding maturity ladder that maps how developers should progressively adopt AI capabilities: Chat (web interface usage) → Mid-Loop Generation (IDE autocomplete) → In-the-Loop Agentic (supervised agent sessions) → On-the-Loop Agentic (autonomous agent execution with human verification) → Multi-Agent (orchestrated teams). Each level compounds on the previous, and Van Eyck emphasizes that most engineers should spend 2-3 months at In-the-Loop before advancing, building guard rails, understanding failure modes, and developing prompt/skill libraries.

This technical maturity progression intersects with a deeper emotional reality that Brad Traversy articulates with unusual candor. After initial excitement with AI tools like Cursor during a period of burnout, Traversy realized over months that "nothing you build with AI is 100% yours" ([2:31](https://www.youtube.com/watch?v=UaB0gWFwuEU&t=151)). His video "Developers are forced to use AI" speaks directly to a loss of builder satisfaction -- the traditional developer experience of starting with an empty IDE, physically typing every line, knowing the codebase intimately, and feeling genuine accomplishment when shipping. This emotional dimension is not just personal preference but structural: companies now mandate AI adoption for productivity regardless of code quality implications, creating what Traversy describes as an industry-wide forced adoption scenario.

Both creators converge on the architect metaphor as the psychological adaptation path for experienced developers. Traversy frames it explicitly: "You now want to look at yourself as the architect of your projects. The vision, the structure, the decisions are all still yours. You're just no longer the brick layer" ([5:38](https://www.youtube.com/watch?v=UaB0gWFwuEU&t=338)). Van Eyck arrives at the same conclusion through technical analysis, describing his personal evolution from "babysitting" agents to "preparing a package of work, giving it off to an agent, and only coming back when it's in a stage of high quality and guaranteed completion" ([13:19](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=799)).

Critically, both emphasize that this shift only works for developers with foundational coding knowledge. Traversy warns bluntly: "If you don't know how to code and you're vibe coding, you're nothing. You're someone that pushes buttons" ([5:38](https://www.youtube.com/watch?v=UaB0gWFwuEU&t=338)). Van Eyck advises: "Junior engineers please write some code. You need to build up a mental model of programming." The maturity ladder is not a path to skip learning to code -- it's a framework for experienced developers to adapt while maintaining competence.

Van Eyck also provides a skills evolution framework that complements the maturity ladder:

- **Fading skills**: Syntax knowledge, hand-coding in established codebases with existing patterns (though juniors must still practice these to build mental models)
- **Evergreen skills**: System design, architecture, work decomposition, judgment and taste, ownership and accountability
- **New skills**: Prompt engineering, context engineering, harness engineering (setting up agentic workflows), agentic workflow debugging

The joy shifts from "I built this" to "I shipped this" -- but as Traversy acknowledges, that reframing only succeeds if you understand what you shipped, which requires the foundational knowledge that comes from writing code by hand.

### Concept 8: Open-Source Frontier Models and Local Inference

The economics of AI-assisted development are typically discussed through the lens of cloud API costs, but a parallel track is emerging with open-source frontier models running on local hardware. xCreate's review of GLM-5 demonstrates capabilities that challenge assumptions about what requires cloud infrastructure.

GLM-5 is a 744B parameter model (up from 355B in GLM 4.7) with 40B active parameters, trained on 28.5 trillion tokens, and released under an MIT license -- meaning no restrictions on commercial use. On SWE-bench, it scores 73.3 vs Claude's 75.0, a gap that has narrowed substantially from earlier generations. The model runs on a Mac Studio with 512GB RAM at 16+ tokens/second using mixed quantization (4/6/9-bit), with approximately 100GB of headroom remaining for context window operations.

The key architectural innovation is multi-head latent attention (MLA), which reduces context memory usage by 33x compared to traditional multi-head attention. In xCreate's testing, the same prompt consumed over 10GB of memory with MHA but only 0.3GB with MLA. This efficiency unlocks batching on consumer hardware -- xCreate demonstrated 6 simultaneous inferences running at 30+ tokens/second combined throughput.

> "Using MHA the multi head attention and the context of this took over 10 gigabytes of memory. But then using MLA, which is multi head latent attention, this one only uses 0.3 GB." -- xCreate ([3:50](https://www.youtube.com/watch?v=3XCYruBYr-0&t=230))

The MIT licensing removes deployment friction entirely. Unlike models requiring attribution or commercial agreements, GLM-5 allows unrestricted use, eliminating legal overhead for business deployment.

This connects directly to Van Eyck's cost warning about multi-agent orchestration: "multiple hundreds of dollars" for serious experimentation with cloud-based Sonnet/Opus models. Local inference with open-source frontier models represents a fundamentally different cost structure -- capital expense on hardware rather than ongoing operational expense on API calls. For sustained multi-agent workflows, the economics may favor local deployment, particularly for small teams or solo developers who would otherwise pay out of pocket.

The performance gap between open-source and proprietary models is narrowing, the memory efficiency of new architectures makes consumer hardware viable, and the licensing removes barriers to commercial deployment. This does not eliminate cloud APIs -- latency, convenience, and cutting-edge capability still favor them for many use cases -- but it establishes local inference as a credible alternative rather than a hobbyist curiosity.

### Concept 9: The Demand Signal -- What Users Actually Want From AI

Two independent data sets from early 2026, examined together, reveal both what people want from AI and why companies cannot see it.

The first is behavioral. The OpenClaw project (formerly Claudebot/Moltbot) -- with 145,000+ GitHub stars and 3,000 community-built skills generating 50,000 monthly installs -- functions as what Jones calls a "revealed preference engine." Nobody filled out a survey; 160,000 developers voted with code. The top skill categories are email management (autonomous triage, not drafting), morning briefings (consolidated pulls from calendar, email, GitHub, Stripe), smart home integration, developer workflows (agents executing commits), and novel emergent capabilities like agents calling restaurants when online booking fails. The pattern across all categories is action, not conversation. ([#032](../../sources/032-nate-b-jones-openclaw.md), [4:00](https://www.youtube.com/watch?v=q-sClVMYY4w&t=240))

> "The community is not building better chatbots when they get the chance. They're building better employees, for lack of a better term." -- Nate B Jones ([7:00](https://www.youtube.com/watch?v=q-sClVMYY4w&t=420))

The second is sociological. Ethan Mollick reports that roughly 50% of American workers already use AI, reporting 3x productivity on tasks they apply it to -- but they are hiding this usage from their employers. Workers fear that revealing AI-driven efficiency gains will result in headcount cuts. The result is a massive gap between what companies think is happening with AI adoption and what is actually happening: corporate AI tools go underused while employees quietly use consumer AI products. ([#033](../../sources/033-prof-g-ethan-mollick-ai-wrong.md), [04:30](https://www.youtube.com/watch?v=-xNq_wJHsls&t=270))

> "About 50% of American workers use AI. They report three times productivity gains on the tasks they use AI for. They're just not giving that to companies. Because why would you? You're worried you'll get fired if AI shows you that you're more efficient." -- Ethan Mollick ([04:30](https://www.youtube.com/watch?v=-xNq_wJHsls&t=270))

These two signals are complementary. OpenClaw shows that when given unconstrained choice, people want digital employees that take action -- not smarter chatbots. Mollick shows that the adoption is already happening at scale but is invisible to employers because of misaligned incentives. Together they explain why enterprise AI strategies feel disconnected: companies are building chatbot interfaces for a workforce that secretly wants autonomous agents, and cannot see the demand because the demand is hiding from them.

Research published in Management Science adds nuance: when real stakes are involved, people consistently prefer a 70% human control / 30% agent delegation split -- choosing less competent human helpers over more competent AI helpers. Jones frames this not as irrationality but as a product requirement, and predicts the ratio will shift toward greater delegation as agent capabilities mature throughout 2026. ([#032](../../sources/032-nate-b-jones-openclaw.md), [13:00](https://www.youtube.com/watch?v=q-sClVMYY4w&t=780))

### Concept 10: The AI Reporting Problem

Before you can evaluate the AI landscape, you need a framework for evaluating AI reporting -- because most of it is unreliable. Cal Newport, speaking on the Better Offline podcast, identifies three distinct patterns of problematic AI journalism that distort public understanding of the technology. ([#034](../../sources/034-better-offline-cal-newport.md))

**Astonishment reporting** omits key facts and places loosely related claims adjacent to each other to manufacture a sense of inevitable disruption. **Vibe reporting** takes real events and spins them with AI-centric framing -- exemplified by Amazon's 16,000 layoffs being reported as AI-driven when the company itself attributed them to standard efficiency cycles. **Mining digital ick** involves taking any uncomfortable AI example and extrapolating it into a broader narrative of existential change. ([0:30](https://www.youtube.com/watch?v=85uXDLzuvdk&t=30), [10:00](https://www.youtube.com/watch?v=85uXDLzuvdk&t=600), [3:00](https://www.youtube.com/watch?v=85uXDLzuvdk&t=180))

Newport's core critique: reporters covering AI are like war correspondents who never leave the capital -- they respond to press conferences from generals without anyone embedded on the ground where the technology is actually being used. ([23:30](https://www.youtube.com/watch?v=85uXDLzuvdk&t=1410))

The antidote is Newport's **two-question test**. Every AI story should answer: (1) What specific technical breakthrough made this possible now? (2) What are the concrete, measurable implications? If a story cannot answer both, it is "mining emotions" rather than informing. ([44:30](https://www.youtube.com/watch?v=85uXDLzuvdk&t=2670))

> "What specific technical breakthrough made this possible now? And then what are the concrete implications?" -- Cal Newport ([45:00](https://www.youtube.com/watch?v=85uXDLzuvdk&t=2700))

Newport applies this framework to the "agents" hype, noting that many so-called AI agents involve no new AI technology -- they are essentially prompt chains calling LLMs in loops with tool-use plugins, a pattern that has existed since OpenAI's plugin system. When the two-question test yields no satisfying answer, the appropriate response is not to dismiss the claim but to demand better evidence before acting on it. This is a critical evaluation skill for the Foundations module: every concept, metric, and prediction in this curriculum should survive the two-question test.

### Concept 11: The Enterprise Reality Check

Three distinct insider perspectives from early 2026 -- an OpenAI product lead, a markets analyst, and an AI researcher -- converge on the same uncomfortable conclusion: the gap between the AI narrative and enterprise reality is wider than the industry acknowledges.

**The Silicon Valley bubble admission.** Sherwin Wu, who leads developer-facing products at OpenAI, is remarkably candid: "Silicon Valley just forgets that we live in a bubble." Despite 95% of OpenAI engineers using Codex and 100% of PRs being reviewed by Codex, Wu acknowledges that many companies outside the Valley have not meaningfully adopted AI yet. The gap between what frontier AI companies practice internally and what their enterprise customers actually do is enormous. ([#035](../../sources/035-lennys-podcast-openai-sherwin-wu.md), [38:30](https://www.youtube.com/watch?v=B26CwKm5C1k&t=2310))

**The panic-not-fundamentals diagnosis.** Scott Galloway analyzes the software stock selloff -- the software ETF (IGV) dropped 20% in a single month, with individual names like Shopify falling 14% and Adobe nearly 40% over the past year -- and argues this is panic selling, not a fundamental shift. He compares it to Google's 40% crash when ChatGPT launched, which preceded a 280% run-up. The core argument: enterprise switching costs (committee approvals, 6+ month replacement timelines, 100% remaining contract fees) make the "software is dead" narrative structurally overblown. AI will compress margins, not cause extinction. ([#036](../../sources/036-prof-g-ai-kill-software.md), [07:00](https://www.youtube.com/watch?v=ERAoSEC4skY&t=420))

**The efficiency-vs-expansion framing error.** Mollick identifies the critical mistake CEOs are making: treating AI purely as an efficiency play (headcount reduction) rather than as a capability expansion opportunity. If one person can do 40% more work, the instinct is to hire 40% fewer people. But the better move is to ask what new things become possible. "10 times more code doesn't mean we should have 90% less coders. Maybe that means we can do different things than we could do before." Companies succeeding with AI use a "leadership + lab + crowd" model: leadership sets direction, a dedicated team builds internal tooling, and the entire workforce experiments to discover use cases. ([#033](../../sources/033-prof-g-ethan-mollick-ai-wrong.md), [28:00](https://www.youtube.com/watch?v=-xNq_wJHsls&t=1680))

The convergence of these three perspectives is instructive. Wu (insider optimist) admits the adoption gap is real. Galloway (market analyst) says the market is overreacting to it. Mollick (researcher) identifies why companies that do adopt are still getting it wrong. Together they paint a picture of an industry where the technology works, the adoption lags, the market panics, and the companies that do adopt often misframe the opportunity. This is the enterprise reality as of early 2026 -- and it is substantially more nuanced than either "AI changes everything" or "AI is a bubble."

Jim Jensen of Traxxion.AI ([#053](../../sources/053-hr-com-ai-operational-traction-wfm.md)) provides a ground-level view from enterprise HCM that reinforces this nuance. Most enterprise AI projects remain stuck in experimentation mode because organizations frame AI agents as "cheaper humans" rather than rethinking work as decisions under constraints. Jensen advocates for "assistive intelligence" -- AI that surfaces trends and guides human decision-making but never assumes accountability -- and proposes a practical autonomy tier model: (1) Observe, (2) Recommend, (3) Execute within guardrails, (4) Escalate ambiguous cases to humans. The failure mode is when organizations skip tiers, deploying AI in full execution mode without the domain-appropriate guardrails. This tier model offers a concrete framework for the enterprise adoption gap: most organizations should start at "observe" and work up, rather than leaping to autonomous execution.

### Concept 12: The Interface Flattening Thesis

Interface Studies host Sal ([#038](../../sources/038-interface-studies-prompt-interface.md)) examines a structural shift in how humans interact with software: the collapse of visual GUIs into a single text input box. GUIs were built on the principle of "recognize, don't recall" -- buttons, menus, and icons made possible actions visible. But as software grew, settings sprawled, controls nested deeper, and recognition became visual overload. Language offered a shortcut: describe the outcome instead of navigating to the right menu.

> "When the cost of navigation becomes higher than the cost of description, people default to text." -- Sal, Interface Studies ([3:43](https://www.youtube.com/watch?v=ccT0jjd36I4&t=223))

Two paths are emerging from this shift. **Path 1: Specification through language** -- casual prompting works for simple tasks, but complex work demands precision, and what goes into the chat box starts looking less like conversation and more like code. "The syntax is conversational, but the mental model required is specification." **Path 2: Hybrid interfaces** -- Claude's artifacts panel, ChatGPT's canvas, Cursor's sidebars -- attempts to give users visual handles alongside the chat box, but many users default to the chat box anyway.

The deeper argument concerns cognitive consequences. The Einstellung effect -- a bias where learning one way to solve problems blocks alternatives -- means that as the prompt becomes the default tool, every problem starts looking like something that needs instructions. Exploration feels like failed planning. Ambiguity feels like inefficiency. Studies show that frequent AI tool use correlates with reduced critical thinking, with cognitive offloading as the mediating factor. This connects directly to the vibe coding risks (Concept 7) and the specification bottleneck in [Module 02](../02-prompting-and-workflows/README.md): the chat input has become the assumed starting point, and language turned out to be more demanding than expected.

### Concept 13: The SaaSpocalypse -- Market Overreaction as Hype Signal

David Gerard ([#039](../../sources/039-pivot-to-ai-saaspocalypse.md)) documents a sharp selloff in enterprise SaaS stocks triggered by Anthropic's Claude Co-work announcement -- a "research preview" that was enough to panic investors into 4-12% single-day drops for legal software companies, cascading into 20% declines across the broader SaaS sector. Gerard argues this was the bursting of a mini-bubble in already overvalued software companies, with AI as the trigger rather than the cause.

The episode reinforces and extends the bubble thesis (Concept 6). Stock traders, saturated with AI hype, extrapolated a narrow product announcement into an existential threat to entire sectors. Gerard's assessment of the underlying AI claims is blunt: AI agents "literally don't work" for the enterprise use cases investors are pricing in, and "you can't vibe code enterprise software if you have any requirement for accuracy or compliance." Yet the resentment toward rent-seeking enterprise software is real -- vendors who "don't even have to make the software very good, so they don't" have created customers who "want nothing more than to make these parasites go away." This resentment creates fertile ground for AI promises even when those promises cannot be delivered.

The SaaSpocalypse is useful as a case study in applying the calibration pattern (below): the trigger was a research preview, not a shipping product; the selloff reflected overvaluation, not AI capability; and the stocks were already recovering at time of reporting. Distinguishing trigger from cause is a core skill for navigating AI-adjacent market dynamics.

### Concept 14: The White-Collar Inversion

Sam Harris ([#050](../../sources/050-sam-harris-ai-economy-emergency.md)), reacting to Microsoft AI CEO Mustafa Suleyman's prediction that "most if not all professional tasks" will be fully automated within 12-18 months, identifies a deeply ironic inversion of historical automation patterns. Previous waves of technology displaced manual and blue-collar labor first. AI is doing the opposite -- it threatens lawyers, accountants, software engineers, and knowledge workers before it can replace plumbers, janitors, nurses, and massage therapists.

This inverts the traditional relationship between education investment and job security. A $200,000 college degree that once guaranteed access to high-status employment may now be a liability rather than an asset. Before full automation arrives, the practical effect is already reshaping hiring: every manager contemplating a new hire now asks "Is this even a job? Can someone already on staff use AI to do this?" The 21-year-old college graduate is the first casualty -- not because AI has replaced their future role, but because the question of whether to create the role at all has become unavoidable.

Harris's most striking framing: even the best-case scenario for AI -- genuine productivity abundance -- is itself an emergency. One person could spin up a thousand agents, start multiple companies in an hour, and run a law firm without associates or paralegals. "That's what success looks like. That's not one of the failure modes." The political question of how to share the resulting wealth is not optional -- it is existential.

### Concept 15: Context Rot Is Two-Dimensional

Brainqub3's analysis of the Recursive Language Models paper ([#048](../../sources/048-brainqub3-recursive-language-models.md)) introduces a crucial refinement to how we understand context window limitations. Context rot -- performance degradation as context grows -- is not simply a function of token count. It is the product of context length **and** task complexity. A model with a million-token window will deteriorate well before reaching capacity if the task requires multihop reasoning across internally self-referencing documents.

This reframes the "bigger context windows" narrative: bigger windows alone do not solve complex reasoning tasks. Complex documents like legal contracts and codebases should be modeled as dependency graphs rather than linear text. The paper's solution -- loading documents as variables in a Python REPL and letting the model programmatically search, slice, and recursively delegate sub-tasks -- demonstrates that code execution plus recursion can unlock reliable reasoning over documents orders of magnitude larger than advertised context windows. This connects directly to Module 02's context engineering principles and Module 04's agentic patterns.

### Concept 16: The Assistant Axis and Persona Drift

Anthropic-affiliated research ([#049](../../sources/049-two-minute-papers-assistant-axis.md)) identified a geometric direction in model activation space -- the "assistant axis" -- that encodes how closely a model adheres to its helpful-assistant persona. Models naturally drift away from this axis during extended conversations, certain topic areas, and in response to emotionally charged interactions, leading to bizarre, unsafe, or delusional outputs.

The practical implications are significant. Writing and philosophy discussions cause more persona drift than coding tasks. Emotionally vulnerable user behavior or questions about AI consciousness are particularly potent triggers. This may explain the common experience where AI responses degrade over long conversations -- and why starting a fresh chat often produces better results. The researchers developed "activation capping" -- analogous to lane-keep assist in cars -- that cut jailbreak success rates roughly in half while preserving capability. The finding that this axis is geometrically similar across different model families (Llama, Qwen, Gemma) suggests a universal structural property of instruction-tuned language models, with implications for transferable safety techniques.

### Concept 17: Verifying AI Industry Claims -- The Cursor Case Study

Java Brains ([#054](../../sources/054-java-brains-cursor-browser-hype.md)) provides a detailed case study in applying critical evaluation to AI industry claims. Cursor's blog post claimed hundreds of concurrent AI agents autonomously built a web browser "from scratch" in one week. Investigation revealed: the browser does not compile (32+ build errors, 88% CI failure rate), core functionality came from existing open-source libraries (undermining the "from scratch" claim), and the estimated cost of $8-16 million in API tokens produced non-functional code.

The most architecturally revealing detail: Cursor's agent system originally included an "integrator" agent responsible for quality control, but removed it because it was slowing throughput. This directly parallels the antipattern in human teams where managers optimize for velocity metrics by cutting code reviews. The result is predictable: impressive throughput numbers and broken software.

The video also surfaces a key principle: bounded, verifiable tasks (framework migrations, refactors with clear before/after states) are where multi-agent systems deliver real value. Open-ended architectural challenges requiring design judgment remain poorly suited for fully autonomous agents. When evaluating AI demos, always check whether the code compiles, has passing CI, and has been independently validated. As Java Brains notes: "The real capabilities of what AI does today is already impressive enough... we don't need this exaggeration."

## Patterns & Practices

### Pattern: Calibrating Your AI Mental Model

- **When to use**: When encountering any new AI capability claim, product launch, or benchmark result.
- **How it works**: Apply three filters sequentially: (1) What is the measured data? (Look for METR-style autonomous task duration, SWE-bench scores, or equivalent reproducible metrics -- not anecdotes or demos.) (2) What is the adoption gap? (How far is this ahead of how most people actually work?) (3) What is the economic sustainability? (Who is paying, how much, and is there a path to revenue?)
- **Example**: When Opus 4.6 launched, the measured data (80.8% SWE-bench Verified, 1M context window) was concrete. The adoption gap was enormous (most developers had not used Opus 4.5's agent features). The economic sustainability was unclear ($5/$25 per million tokens with uncertain enterprise uptake).
- **Source**: Synthesized from [#008](../../sources/008-nate-b-jones-phase-transition.md), [#007](../../sources/007-internet-of-bugs-ai-bubble.md), [#019](../../sources/019-matt-shumer-something-big.md)

### Pattern: Tracking the Capability Frontier

- **When to use**: To maintain an up-to-date understanding of what AI can actually do, rather than relying on impressions from months ago.
- **How it works**: Monitor three signals: (1) The METR autonomous task duration metric (the single most informative capability indicator). (2) SWE-bench trajectories for coding-specific capability. (3) Reports from practitioners who use frontier models daily, not occasional users or commentators (Jones and Shumer are examples of practitioners whose reports are grounded in daily use).
- **Example**: The SWE-bench trajectory went from 4% to ~95% saturation in two years. The METR autonomous task duration doubled from ~2.5 hours to ~5 hours in a single interval. Both metrics told the same story before the February 2026 releases confirmed it experientially.
- **Source**: [#019](../../sources/019-matt-shumer-something-big.md), [#012](../../sources/012-nate-b-jones-career-collapse.md)

### Pattern: The Bicycle Rule -- Forward Momentum Over Caution

- **When to use**: When deciding how aggressively to adopt new AI capabilities.
- **How it works**: Jones's bicycle metaphor: going slower on a bicycle makes balancing harder, not easier. Children instinctively try to go slowly for safety, but physics rewards speed -- forward momentum stabilizes the rider. Applied to AI adoption: cautiously waiting for maturity, integrating AI incrementally, or resisting engagement entirely all produce worse outcomes than leaning in aggressively. Fluency comes from daily practice, not occasional deep dives.
- **Example**: Engineers who adopted multi-agent workflows when they first became viable in December 2025 had three months of compounding practice by the time Opus 4.6 released. Those who waited to see if the tools "matured" had to start from scratch with a steeper learning curve.
- **Source**: [#012](../../sources/012-nate-b-jones-career-collapse.md)

### Pattern: The Maturity Self-Assessment

- **When to use**: When determining where to focus AI learning investment and which capabilities to adopt next.
- **How it works**: Map yourself to Van Eyck's 5-level maturity ladder. Master your current level before advancing to the next. Key indicators for each level: (1) Chat -- basic web interface usage, (2) Mid-Loop -- IDE autocomplete integration like Cursor or Copilot, (3) In-the-Loop -- supervised agent sessions where you watch execution and intervene (spend 2-3 months here building guard rails and understanding failure modes), (4) On-the-Loop -- agent works autonomously from specification to completion while you're away (requires test automation and verification infrastructure), (5) Multi-Agent -- orchestrated teams with shared task management (cutting edge as of early 2026). Start at the bottom, build compounding skills at each level, and resist the temptation to skip ahead.
- **Example**: A developer comfortable with Cursor autocomplete (level 2) who jumps directly to multi-agent orchestration (level 5) without spending time In-the-Loop will lack the debugging instincts and guard rail patterns needed to prevent costly mistakes. The maturity ladder forces sequential skill building.
- **Source**: [#024](../../sources/024-jo-van-eyck-agentic-coding-2026.md), [#022](../../sources/022-traversy-media-forced-ai.md)

## Common Pitfalls

- **Pitfall: Anchoring on stale mental models.** If you have not revisited your AI assumptions since before December 2025, you are operating on obsolete information. The phase transition that month was qualitative, not just quantitative. Avoid this by regularly testing frontier models on your actual work, not by reading about them.

- **Pitfall: Confusing "I tried ChatGPT once" with understanding the landscape.** The capability overhang means the gap between a casual user and a power user is enormous. Someone using free-tier ChatGPT for occasional questions is experiencing a fundamentally different product than someone running multi-agent task loops with Opus 4.6. Avoid this by investing in paid-tier access and sustained daily practice.

- **Pitfall: Dismissing the bubble thesis because the technology is real.** The dot-com crash destroyed companies, not the internet. Real underlying technology does not prevent speculative over-investment and painful corrections. The AI infrastructure will likely survive any correction; many AI startups may not. Avoid this by distinguishing between "AI is transformative" (likely true) and "current AI valuations are sustainable" (uncertain).

- **Pitfall: Extrapolating exponentials without constraint.** Doubling rates are real but not infinite. Compute costs, energy availability, data quality, and regulatory intervention all impose practical limits. The METR metric is the best signal, but even consistent doubling rates can decelerate. Avoid this by tracking actual data points rather than extrapolating curves.

- **Pitfall: Waiting for stability before engaging.** As Jones argues, there is no mature state to wait for. The technology landscape is a continuously steepening curve, and early adopters compound their advantage. The learning habit has a longer half-life than any specific piece of AI knowledge. Avoid this by building daily practice now, even if the specific tools change.

- **Pitfall: Skipping the learning curve with vibe coding.** Both Traversy and Van Eyck warn that beginners who jump straight to AI-generated code without learning to code manually will lack the mental models needed to be effective architects. Traversy's warning is blunt: "If you don't know how to code and you're vibe coding, you're nothing. You're someone that pushes buttons" ([5:38](https://www.youtube.com/watch?v=UaB0gWFwuEU&t=338)). Van Eyck advises junior engineers to write code by hand to build mental models of programming. The joy shifts from "I built this" to "I shipped this" -- but only if you understand what you shipped. DevForge ([#042](../../sources/042-devforge-vibe-coding-trap.md)) quantifies the lifecycle cost: AI writes code in 10 minutes, followed by 90 minutes debugging edge cases, an hour refactoring for architectural fit, and 3 hours fixing production issues -- often slower than writing with full understanding from the start. The underlying mechanism is Kernighan's Law applied to AI: if the model writes code beyond your understanding, you definitionally cannot debug it. This creates a trap where repeated reliance trains the brain to "ask AI first instead of thinking through problems," producing measurable skill atrophy within six months. Avoid this by mastering foundational coding skills before relying heavily on AI assistance, and by measuring real velocity across the full lifecycle rather than just initial implementation speed.

- **Pitfall: Taking AI demo claims at face value without verification.** Cursor's FastRender browser claim ([#054](../../sources/054-java-brains-cursor-browser-hype.md)) -- hundreds of agents building a browser "from scratch" -- collapsed under scrutiny: the code does not compile, core libraries were borrowed, and the $8-16M in token costs produced nothing functional. When a company publishes code, check whether it compiles, has passing CI, and has been independently validated before accepting claims. The most inflated version of the story is always the one that goes viral; rational assessments get buried.

- **Pitfall: Accepting AI reporting at face value.** Most mainstream AI coverage fails Newport's two-question test: it cannot identify the specific technical breakthrough or articulate concrete implications. Astonishment reporting, vibe reporting, and mining digital ick are the three dominant patterns ([#034](../../sources/034-better-offline-cal-newport.md)). Before forming opinions from an AI article, ask: "What technical breakthrough made this possible?" and "What are the concrete, measurable implications?" If neither is answered, the story is emotional content, not information. This applies equally to hype-driven and fear-driven coverage -- both can fail the test. Avoid this by building the two-question habit into your media consumption before sharing, acting on, or internalizing any AI claim.

- **Pitfall: Ignoring the emotional dimension of AI adoption.** Traversy's candid account reveals a real team morale risk. The loss of builder satisfaction is not just personal -- it reflects a structural change in what it means to be a developer. Leaders who dismiss this as resistance miss the underlying identity shift that needs to be addressed explicitly. The architect mindset can preserve some creative satisfaction, but only if acknowledged as a genuine psychological transition, not just a technical workflow change. Avoid this by recognizing that forced AI adoption changes what developers value about their work, and addressing that shift openly rather than treating it as mere resistance to change.

## Hands-On Exercises

1. **Map your capability overhang.** Spend 30 minutes using a frontier AI model (Claude Opus 4.6 or GPT-5.3 Codex, paid tier) on a real work task -- not a toy example. Then write down: What surprised you? What was the gap between this experience and your previous AI mental model? This exercise forces a personal confrontation with the overhang.

2. **Benchmark your current AI usage pattern.** Track how you use AI tools for one full work day. Count: How many interactions? What type (question-answer, task delegation, multi-step work)? What percentage of your work involves AI? Compare your pattern to the "power user" description from Source #008 (parallel agents, overnight task loops, specification-first workflow). Where is the gap?

3. **Apply the three-filter calibration model.** Pick one recent AI announcement or product launch. Research and write down: (a) What is the measured data (not the marketing claim)? (b) What is the adoption gap between this capability and how most people work? (c) What is the economic sustainability? Practice this filter on at least three different announcements to build the habit.

4. **Evaluate the bubble signals.** Read through the Super Bowl ad pattern from Source #007. Then research: What happened to the companies that advertised AI at Super Bowl LX? Are the structural parallels Brown identifies playing out, or have the counter-arguments (strong balance sheets, real enterprise adoption) held? This exercise builds the critical evaluation muscle that prevents both naive hype and naive skepticism.

5. **Calculate your personal METR.** How long can you currently delegate autonomous work to an AI tool before needing to intervene? Try giving an AI a task that should take 30 minutes of human effort, with clear success criteria, and time how long before it needs help. Compare to the ~5-hour METR benchmark. What would need to change in your workflow to extend your personal delegation horizon?

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [003: Opus 4.6 AND GPT-5.3 Same Day](../../sources/003-primetime-opus-46-chatgpt-53.md) | ThePrimeTime | Model comparison, benchmarks, the Great Convergence |
| [007: Super Bowl Commercial Bubble Curse](../../sources/007-internet-of-bugs-ai-bubble.md) | Carl Brown (Internet of Bugs) | Bubble dynamics, historical pattern, counter-arguments |
| [008: The Capability Overhang](../../sources/008-nate-b-jones-phase-transition.md) | Nate B Jones | Phase transition, capability overhang, power user patterns |
| [012: Career Collapse](../../sources/012-nate-b-jones-career-collapse.md) | Nate B Jones | Horizontal/temporal collapse, bicycle metaphor, compounding learning |
| [016: The Biggest AI Jump](../../sources/016-nate-b-jones-opus-46-jump.md) | Nate B Jones | Opus 4.6 qualitative leap, workflow inversion, temporal collapse |
| [019: Something Big Is Happening](../../sources/019-matt-shumer-something-big.md) | Matt Shumer | METR doubling rate, self-improvement loop, general-purpose disruption |
| [022: Developers are forced to use AI](../../sources/022-traversy-media-forced-ai.md) | Brad Traversy (Traversy Media) | Developer identity crisis, forced adoption, architect metaphor, builder satisfaction loss |
| [023: GLM-5 Local AI Review](../../sources/023-xcreate-glm5-review.md) | xCreate | Open-source frontier models, local inference, MLA memory optimization, MIT licensing |
| [024: Agentic coding in 2026](../../sources/024-jo-van-eyck-agentic-coding-2026.md) | Jo Van Eyck | Maturity ladder, fading vs evergreen skills, developer skills evolution |
| [032: OpenClaw Skills Marketplace](../../sources/032-nate-b-jones-openclaw.md) | Nate B Jones | Revealed preference engine, demand for digital employees, specification quality, 70/30 human-agent split |
| [033: Why CEOs Are Getting AI Wrong](../../sources/033-prof-g-ethan-mollick-ai-wrong.md) | Prof G / Ethan Mollick | Hidden adoption gap, efficiency vs capability expansion, three endgame scenarios, apprenticeship crisis |
| [034: Hater Season: Cal Newport on AI Reporting](../../sources/034-better-offline-cal-newport.md) | Better Offline / Cal Newport | Taxonomy of bad AI reporting, two-question test, pre-training plateau, vibe coding reality gap |
| [035: Engineers are becoming sorcerers](../../sources/035-lennys-podcast-openai-sherwin-wu.md) | Lenny's Podcast / Sherwin Wu | OpenAI internal practices (95% Codex), enterprise adoption gap, explosion of small companies |
| [036: Did AI Just Kill Software?](../../sources/036-prof-g-ai-kill-software.md) | Prof G Markets | Software selloff as panic, Anthropic Super Bowl ad, Anthropic vs OpenAI positioning |
| [037: Google Goes All-In on the AI Arms Race](../../sources/037-prof-g-google-ai-arms-race.md) | Prof G Markets | $660B AI capex arms race, 100-year bond, memory chip shortage, public backlash |
| [038: When the Interface Flattens Into a Prompt](../../sources/038-interface-studies-prompt-interface.md) | Interface Studies (Sal) | Interface flattening thesis, GUIs collapsing to prompts, cognitive consequences of text-first interaction, Einstellung effect |
| [039: SaaSpocalypse](../../sources/039-pivot-to-ai-saaspocalypse.md) | Pivot to AI (David Gerard) | SaaS investor panic from AI announcements, enterprise software as rent-seeking, vibe coding compliance ceiling |
| [042: Vibe Coding is a Trap](../../sources/042-devforge-vibe-coding-trap.md) | DevForge | Illusion of speed in AI coding, mental models as the real asset, Kernighan's Law applied to AI, skill atrophy risk |
| [044: Full Day of Analyst Work in 10 Minutes](../../sources/044-nate-b-jones-claude-excel-powerpoint.md) | Nate B Jones | Context layer thesis, silent compounding intelligence, execution premium collapse, capability overhang in productivity tools |
| [045: Sam Altman said what???](../../sources/045-primetime-altman-townhall-biosecurity.md) | ThePrimeTime | 100x cost reduction trajectory, LLM monoculture risk, biosecurity as AI risk vector, "problem and solution" paradox |
| [046: The Rise of WebMCP](../../sources/046-sam-witteveen-webmcp.md) | Sam Witteveen | WebMCP standard (Google/Microsoft), structured agent-web interaction, declarative vs imperative APIs |
| [047: OpenAI's AI Browser Is a Security Nightmare](../../sources/047-standuppod-ai-browser-security.md) | TheStandupPod | AI browser security paradox, prompt injection as intractable problem, hype vs shipped product quality |
| [048: Before You Build Another Agent, Understand This MIT Paper](../../sources/048-brainqub3-recursive-language-models.md) | Brainqub3 | Context rot as two-dimensional, documents as dependency graphs, REPL + recursion architecture, limits of RAG and context stuffing |
| [049: Anthropic Found Out Why AIs Go Insane](../../sources/049-two-minute-papers-assistant-axis.md) | Two Minute Papers | Assistant axis, persona drift in extended conversations, activation capping, universal geometry across model families |
| [050: We're Not Ready for What AI Is About to Do to the Economy](../../sources/050-sam-harris-ai-economy-emergency.md) | Sam Harris | White-collar inversion, entry-level hiring freeze, "success is the emergency," wealth concentration dynamics |
| [052: Claude Isn't Safe. This Anthropic Whistleblower Has the Proof.](../../sources/052-novara-media-anthropic-safety-crisis.md) | Novara Media | Safety-economy polycrisis, incentive distortion in safety discourse, geopolitical imperatives overriding safety, Eric Schmidt's red lines |
| [053: From AI Curiosity to Operational Traction](../../sources/053-hr-com-ai-operational-traction-wfm.md) | HR.com / Jim Jensen | Assistive intelligence over autonomy, redefining work as decisions not tasks, autonomy tiers for AI deployment, capability overhang in enterprise HCM |
| [054: The Cursor Situation](../../sources/054-java-brains-cursor-browser-hype.md) | Java Brains | FastRender browser debunking, integrator removal antipattern, bounded vs open-ended agent tasks, hype framing and trust erosion |

## Further Reading

- [METR Task Completion Benchmarks](https://metr.org/) -- The primary source for autonomous task duration metrics referenced throughout this module
- [SWE-bench Leaderboard](https://www.swebench.com/) -- Track the coding benchmark trajectory that illustrates capability acceleration
- [Module 02: Prompting & Workflows](../02-prompting-and-workflows/README.md) -- Once you understand the landscape, learn how to communicate effectively with these models
- [Module 06: Strategy and Economics](../06-strategy-and-economics/README.md) -- The career and financial implications of the dynamics covered here
