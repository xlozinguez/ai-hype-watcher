# Module 02: Prompting & Workflows

> Master the shift from prompt engineering to context engineering, build sticky reusable workflows, and develop the specification skills that separate effective AI users from everyone else.

## Overview

If Module 01 established that AI tools are dramatically more capable than most people realize, this module addresses the next question: how do you actually communicate with them effectively? The answer has evolved rapidly. What began as "prompt engineering" -- the art of crafting the perfect instruction -- has broadened into "context engineering," a discipline concerned with managing everything that enters a model's context window. And underlying both is a more fundamental skill: specification, the ability to precisely define what you want before you start prompting at all.

This module synthesizes three complementary perspectives. Nate B Jones argues that specification -- not coding, not prompting -- is the skill that separates people who thrive with AI from those who produce incoherent output. Ali H. Salem provides a systematic framework for prompt construction, workflow stickiness, and hallucination reduction. Tim Berglund reframes the entire conversation by showing that the prompt itself is just one of six components competing for space in a context window, and that engineering the full context is what production-grade AI work demands.

Together, these perspectives form a progression: know what you want (specification), communicate it well (prompting), make it repeatable (sticky workflows), validate the output (verification), and manage the technical constraints (context engineering). This is the skill stack that Module 03 and beyond will assume you have.

## Prerequisites

- [Module 01: Foundations](../01-foundations/README.md) -- You need to understand the capability overhang and current model landscape before optimizing how you communicate with these models.

## Core Concepts

### Concept 1: Specification Is the Real Bottleneck

The most important idea in this module comes from Nate B Jones's analysis in "90% of People Fail at Vibe Coding":

> "The valuable skill isn't really coding anymore. It's specification."

When AI can implement your ideas in minutes, the constraining factor shifts to whether you can articulate what you actually want. Jones identifies two failure modes that plague AI users at every level:

**Failure Mode 1: Moving so fast you never stop to think.** When building is instant, the bottleneck shifts to knowing what you actually want. It is easy to start prompting before you have figured that out, generating piles of features that do not fit together. The build-test-iterate loop can feel intoxicating for its own sake, but without a clear specification, you are generating noise.

**Failure Mode 2: Confusing "works on my laptop" with "ready for users."** AI compresses the cost of *creating* software toward zero, but it does not compress the cost of *owning* software in production. Security researchers found roughly 10% of apps on popular vibe coding platforms have vulnerabilities (exposed databases, visible API keys). The happy path works; the edge cases do not.

The discipline Jones prescribes is deceptively simple: "Pause. Describe what you want really plainly before you start prompting. Know why you're building it. Even if it's just for fun -- what should it do, what success looks like." Experienced developers already do this instinctively -- they know how to break problems into pieces so each coded piece contributes to a coherent whole, and they ask the right questions (What happens when a user is not logged in? What if the database is slow?). The gap between a beginner and someone effective with AI is not coding ability but this specification intuition. As Jones notes, "It's a much smaller gap than learning to code from scratch and it will close faster with practice."

Interface Studies ([#038](../../sources/038-interface-studies-prompt-interface.md)) provides the deeper cognitive explanation for why specification is so demanding. As GUIs collapse into chat boxes, users discover that language is harder than it looks: "The syntax is conversational, but the mental model required is specification and we only have this input box for it." Two paths are emerging -- specification through increasingly structured language (JSON prompts, schemas, agent skills), or hybrid interfaces that patch visual controls back in. Both paths confirm that the chat input has become the assumed starting point for AI interaction, and that specification skill is the differentiator in both.

DevForge ([#042](../../sources/042-devforge-vibe-coding-trap.md)) adds a concrete lifecycle argument: the senior developer pattern is to understand the problem first, design the solution yourself, then optionally use AI to speed up implementation while reviewing critically. AI is used for boilerplate, exploration, and implementation acceleration -- but never for core logic the developer needs to understand. This "design before generating" discipline is the specification-first pattern applied at the code level.

NeuralNine ([#138](../../sources/138-neuralnine-coding-habit.md)) demonstrates this understand-first workflow in practice. His approach: manually experiment with the core technology (inference APIs, vector stores, embedding models), understand the logic, then feed reference files to Claude Code with instructions to scaffold the full application. As he puts it: "I told it look I know how to do this. Here are three files that I wrote... and build a FastAPI application around it." This preserves comprehension while leveraging AI for boilerplate -- the specification is not a document but a working reference implementation. NeuralNine also advocates for a daily goal-free coding habit (30-60 minutes) specifically to maintain foundational skills that differentiate developers in an era of vibe coding: "Having good linear algebra skills, it's just nice when you read papers... especially in an age where everyone is just vibe coding." This reinforces the principle that specification quality depends on deep understanding that only comes from hands-on practice.

Jones ([#108](../../sources/108-nate-b-jones-five-levels-ai-coding.md)) frames the specification bottleneck through Shapiro's five-level AI coding maturity model. At Level 4-5 ("developer as PM" and "dark factory"), the constraining resource shifts entirely from implementation speed to specification quality. Writing specs detailed enough for autonomous agents requires deep systems thinking, customer understanding, and domain expertise. For brownfield legacy systems, the first step is not deploying agents but reverse-engineering specifications from running code and institutional knowledge. As Jones puts it: "The bottleneck has moved from implementation speed to spec quality. And spec quality is a function of how deeply you understand the system, your customer, and your problem."

Martin Fowler's Deer Valley retreat ([#071](../../sources/071-martin-fowler-future-software-dev.md)) pushes the specification-first thesis to its logical extreme through Drew Breunig's "spec-as-library" experiment: a timestamp-to-phrase converter defined entirely as a 500-line markdown specification and 500-line YAML test suite, with no implementation code, successfully implemented across seven programming languages by LLMs. The provocation: "What does software engineering look like when coding is free?" If specifications become the primary software artifact — with test suites as verification and implementation generated on demand — then specification skill is not just important, it is the entire job. Laura Tacho's observation from the same retreat reinforces this: "Developer Experience and Agent Experience intersect completely" — clear documentation, modularity, and descriptive naming benefit both humans and LLMs equally. There is no separate "AI optimization" discipline; investing in specification quality is investing in AI effectiveness.

Mo Bitar ([#159](../../sources/159-mo-bitar-vibecoding-handwriting.md)) provides the sharpest counterpoint to the specification-first thesis: after two years of vibecoding with increasingly detailed specifications, he returned to writing code by hand. His argument is not that specification does not help but that it has a ceiling -- AI-generated code that passes all reviews and tests can still produce codebases that are "complete gibberish" when read end-to-end. The **diff-level illusion** (individual changes always look reasonable in isolation because they are designed to "fit into a hole") means that even rigorous spec-driven AI workflows can produce architecturally incoherent systems. The deception cycle he identifies (prompt, correct, get dopamine hit, conclude the AI "coded something") operates at every level of specification complexity. This does not negate the specification-first pattern but establishes an important boundary: specification quality determines the quality of individual outputs, but only human comprehension of the full codebase ensures architectural coherence.

### Concept 2: The Six-Step Prompting Framework

Ali H. Salem, in "4 AI Skills That Set You Apart," provides the most actionable prompting structure in the source material -- a six-step framework that works across ChatGPT, Claude, Gemini, and other models:

1. **Role** -- Define who the model is, who it is speaking to, and the tone. Without this, answers are generic and mismatched.
2. **Task** -- State the action and the success criteria. The model executes instead of guessing.
3. **Context** -- Provide the single source of truth: facts, documents, and background. When context is missing, models fill gaps with plausible guesses -- which is where hallucination begins.
4. **Examples** -- Show what good looks like (format, tone, depth). Without examples, outputs vary significantly even with the same prompt.
5. **Output** -- Specify the exact format, length, and structure. Without this, you get a correct but inconveniently formatted response that requires follow-up.
6. **Constraints** -- Set guardrails on what to avoid and what to prioritize so the model does not drift.

The critical insight from Salem is that you should *not* apply all six steps to every interaction. For simple, low-stakes tasks, a lighter approach is fine. The full framework is for high-stakes work where accuracy and format matter. The power comes from building reusable prompts that encode the framework (see Concept 4: Sticky Workflows) rather than constructing it from scratch each time.

### Concept 3: From Prompt Engineering to Context Engineering

Tim Berglund, in "Prompt Engineering is Dead," makes the case that prompt engineering -- while not irrelevant -- addresses only one of six components competing for space in a model's context window. The broader discipline is **context engineering**: managing everything that goes into the window.

An LLM is a stateless function. It remembers nothing between calls. Everything it needs must fit in the context window. For agentic applications that make iterative calls and use tools, this constraint becomes the central engineering challenge. Berglund identifies six components that occupy every context window:

1. **User message** -- The initial input (your prompt or instruction)
2. **System prompt** -- Personality, guardrails, behavioral instructions
3. **Tools** -- Descriptions and schemas of available tools
4. **Resources** -- Business-specific data the model was never trained on
5. **Assistant messages** -- History of the model's previous responses
6. **Tool calls and responses** -- Record of intermediate tool invocations and results

Items 1-4 are relatively static. Items 5-6 **grow as the agent runs**, eventually consuming the entire window. This is why long-running AI sessions degrade -- it is not the model getting "tired," it is the context filling up with accumulated history.

> "Prompt engineering was always a little bit ridiculous, but context is king." -- Tim Berglund

This reframing is essential for anyone moving beyond casual chat interactions. The system prompt matters, but so do tool descriptions, resource selection, conversation history management, and context window budgeting. Context engineering is where Module 02 connects to [Module 04: Agentic Patterns](../04-agentic-patterns/README.md), which covers the architectural solutions (agent decomposition, compaction, memory) for managing context at scale.

Jones ([#170](../../sources/170-nate-b-jones-four-prompting-disciplines.md)) extends this further by arguing that "prompting" has silently diverged into four distinct cumulative disciplines: (1) **prompt craft** (structuring clear instructions -- now table stakes), (2) **context engineering** (curating the optimal token set -- your 200-token prompt is 0.02% of what the model sees), (3) **intent engineering** (encoding organizational purpose and decision boundaries), and (4) **specification engineering** (writing documents that autonomous agents can execute against over hours or days without human intervention). The shift from synchronous to autonomous AI work breaks every assumption of conversational prompting: everything you relied on in conversation -- catching mistakes, providing missing context, course-correcting drift -- must be encoded before the agent starts. Jones identifies five learnable specification primitives: self-contained problem statements, acceptance criteria, constraint architecture (musts, must-nots, preferences, escalation triggers), decomposition into independently testable components, and evaluation design with known good outputs.

### Concept 4: Sticky Workflows -- Compounding Over Coasting

Multiple creators ([#005](../../sources/005-nate-b-jones-vibe-coding-readiness.md), [#006](../../sources/006-ali-salem-4-ai-skills.md)) emphasize that the difference between power users and everyone else is not talent but systems. As Salem puts it:

> "The absolute best users of AI aren't necessarily smarter or more experienced. They just have better systems."

Salem introduces the concept of "sticky AI workflows" -- systems that compound AI effectiveness over time and where going back to the old way feels painful. Three building blocks:

1. **Link documents to chats.** Copy the link to the AI chat you used and drop it into your working document. This eliminates the frustration of sifting through old conversations when you need to recreate something.

2. **Build systems to reuse successful prompts:**
   - **Text expanders** (e.g., Espanso) -- Assign a short code that expands into a full prompt. Your best prompts are always available instantly.
   - **Prompt library** -- Use Notion, a spreadsheet, or any accessible tool to keep your highest-performing prompts organized and reusable.

3. **Use Projects in your AI platform.** Both ChatGPT and Claude support "Projects" where every chat inherits the same instructions and files. You stop re-explaining the same background, get more consistent outputs, and can reuse context across multiple chats without information bleeding into unrelated work.

theMITmonk ([#109](../../sources/109-themitmonk-chatgpt-hacks.md)) formalizes this with the "ESP" framework for building persistent AI context: **Extract** (voice-mode interview to capture background, tone, strategy, blind spots), **Synthesize** (organize transcript into a structured summary for custom instructions), **Projects** (domain-separated workspaces with uploaded files and customized instructions). This transforms a stateless chat tool into a context-persistent system. The domain separation is critical: mixing consulting, personal, and health contexts in a single workspace causes context contamination and degraded output quality. Each project should have its own tailored instructions and reference materials.

The compounding dynamic is critical. A prompt you use once has linear value. A prompt you save, refine, and reuse compounds. A workflow that builds on previous outputs and feeds into the next task creates exponential leverage. Power users are not doing more work -- they are doing the same work with accumulated infrastructure.

### Concept 5: Context Window Discipline

Both Jones and Berglund converge on the same practical insight from different angles: AI tools degrade over long conversations, and the solution is disciplined context management.

Jones frames it from the user's perspective: "Instead of one long conversation that can meander, make sure that you have clear tasking for a particular job and you can define it precisely." Break work into small tasks, run each in a fresh context window, and maintain quality by not letting accumulated history pollute the model's reasoning.

Berglund provides the technical explanation: the context window has a practical capacity of roughly 60-70% of its stated size.

> "More isn't always better. Somewhere in the 60 to 70% of the capacity of the context window is probably where you get your best results." -- Tim Berglund

Research consistently shows that filling a context window to 100% does not give the best results. Performance peaks at 60-70%. This means effective context engineering is not just about fitting everything in -- it is about being selective enough to leave headroom for the model to reason.

For longer-running work, Berglund identifies three strategies that prevent context exhaustion:

- **Compaction**: Use an LLM call to summarize large resources or conversation history. A 50,000-token document can often be compressed to 500 words without losing decision-relevant information.
- **Memory**: A key-value store where intermediate results can be parked and retrieved on demand rather than persisted in the window across every call.
- **Agent decomposition**: Split complex work into composed sub-agents. The parent agent gets a concise summary rather than carrying the full context of every sub-task.

Charlie Automates ([#040](../../sources/040-charlie-automates-claudemd-context.md)) demonstrates these principles applied to CLAUDE.md configuration specifically. A 733-line CLAUDE.md can consume 15-20% of the context window before the user even sends a message. More critically, irrelevant instructions do not sit passively -- they actively dilute the model's attention, degrading output quality. The solution is domain-based rule segmentation: split rules into groups (global, dev, content, clients) and load only the domains whose keywords match the current prompt. In Charlie's demonstration, the same 734-line CLAUDE.md was reduced to 28 rules for a YouTube script task and 23 rules for a dev task. The closing insight reframes the goal: "They think the goal is to make Claude smarter, giving it more information, more context, more rules. It's not. Claude is already super intelligent. The goal is to make Claude more focused." This principle -- focus over intelligence -- is context engineering distilled to its essence.

Charlie also introduces context brackets for adaptive verbosity: as the context window fills, Claude automatically shifts from detailed responses (when fresh) to concise communication (at moderate usage) to code-only survival mode (when depleted). This addresses the common problem of verbose responses accelerating context exhaustion in long sessions.

Dylan Davis ([#084](../../sources/084-dylan-davis-context-rot-60-rule.md)) independently validates Berglund's 60-70% rule and provides a concrete mental model: imagine the AI's memory as a whiteboard that gets progressively cluttered. He identifies four warning signs of context rot: (1) instructions getting ignored -- the AI stops following formatting constraints set earlier, (2) self-contradiction -- the AI reverses positions without justification, (3) fact disappearance -- specific data points are hallucinated or dropped, (4) automatic compaction -- Claude's visible "organizing my thoughts" summarization, which loses nuance. His four tactical countermeasures -- handoff summaries to fresh conversations, strategic file management to minimize token waste, experimentation to build intuition about task complexity limits, and proactive in-thread summaries every 5-15 exchanges -- translate the abstract 60% rule into daily practice.

Matt Pocock ([#152](../../sources/152-matt-pocock-never-run-init.md)) adds a concrete framework for thinking about context cost. He breaks the agent's context window into four phases competing for space: system prompt (fixed, includes CLAUDE.md), exploration (discovering the codebase), implementation (writing code), and testing/debugging (feedback loops). Only the system prompt is non-flexible -- minimizing it maximizes available space for actual work. LLMs have a realistic instruction budget of 300-500 instructions, and every statement in CLAUDE.md counts against this budget regardless of relevance. The critical distinction: information that exists in source code (package.json scripts, file structure, imports) is trivially discoverable by the agent during exploration and should not be duplicated in CLAUDE.md. The only information worth putting in context files is what the agent genuinely cannot discover.

Theo ([#153](../../sources/153-theo-delete-claudemd.md)) provides empirical backing: a study ("Are Repository-Level Context Files Helpful for Coding Agents?") found that developer-provided context files only marginally improved performance (+4% average), while LLM-generated context files had a small negative effect (-3% average). Both increased costs by over 20%. Theo identifies the **pink elephant problem**: mentioning a technology in a context file -- even to say "don't use this" -- makes the model more likely to reach for it. His approach: use CLAUDE.md as a diagnostic tool to discover what agents struggle with in your codebase, then fix the codebase rather than adding more instructions.

Matt Pocock ([#164](../../sources/164-matt-pocock-codebase-ai-ready.md)) extends this insight to its logical conclusion: codebase design is the single biggest influence on AI coding output -- more than prompts, more than agent configuration files. Drawing from John Ousterhout's "A Philosophy of Software Design," he advocates for **deep modules** (large implementations behind simple interfaces) as "graybox modules" where humans design the interface and write tests while AI handles the internals. The key reframing: AI is a perpetual new starter with no memory of your codebase, so codebase quality is an onboarding problem. The same 20-year-old software practices that help human new starters -- clear boundaries, good tests, navigable structure -- are exactly what AI needs.

These strategies become the architectural foundation for the agentic patterns covered in [Module 04: Agentic Patterns](../04-agentic-patterns/README.md).

### Concept 6: Validation and Hallucination Reduction

Salem's validation framework provides three practical layers for reducing hallucination risk:

**Layer 1: Use tools with strong grounding.** NotebookLM is built around answering based on sources you provide, dramatically reducing hallucinations because the model is anchored in real material. Perplexity finds and cites online sources by default, making it easier to verify claims.

**Layer 2: Self-evaluation prompts.** Three techniques:
- Ask the AI to score its statements with a confidence level so you can focus cross-checking where it matters.
- Tell the AI to base answers only on documents you attach (stops the model from filling gaps with guesses).
- Explicitly give the AI permission to say "I don't know." Without this, models try to be "helpful" by filling gaps, which is exactly where hallucinations occur.

**Layer 3: Cross-model critique.** Create something in one model, then let a different model critique it. As Salem explains using a self-driving car analogy: redundant systems built on different architectures catch errors that single-system approaches miss. Different LLMs do not reason identically, so their disagreements reveal weaknesses.

> "You never fully get rid of hallucinations because LLMs are probabilistic in nature and no technique today can enforce causality." -- Ali H. Salem

theMITmonk ([#109](../../sources/109-themitmonk-chatgpt-hacks.md)) adds a complementary technique: adversarial prompting to counter AI's default agreeableness. Three approaches: magic triggers ("audit using first principles," "act as my fierce competitor"), shadow boxing (simulated debates between opposing personas within the same conversation), and blind spot checks ("based on what you know about me, what are the gaps in my reasoning?"). As he puts it: "Most people use ChatGPT for validation, but you should use it for violation." This pairs naturally with Salem's cross-model critique -- adversarial prompting within a single model, cross-model critique between models.

This honest framing is important. Validation reduces risk; it does not eliminate it. Building this understanding into your workflow prevents both over-trust (accepting everything uncritically) and over-skepticism (rejecting AI output entirely because it sometimes hallucinates).

### Concept 7: Software Vision and the Automation Decision

Jones introduces the concept of "software vision" -- analogous to *parkour vision*, the trained ability to see walls as runnable surfaces. Software vision means seeing problems as software-shaped, recognizing when a repetitive task could be automated, or when a messy process could be systematized.

> "The people who take to vibe coding aren't necessarily technical. They're people who already have software vision or develop it quickly."

Indicators you may already have it: you have built complicated spreadsheets, duct-taped together automations (N8N, Zapier, macros), or bent a tool to do something it was not designed for.

Salem complements this with a structured three-step process for deciding *what* to automate:

1. **Find candidates**: Break your day into individual tasks. Anything that is repeatable, digital, and where you can clearly describe what good looks like is a candidate.
2. **Check the pain threshold**: If the task is not annoying enough, you will not sustain the automation. Pain is the adoption signal.
3. **Start with your generalist AI, escalate to specialists**: Fit as many use cases as possible into one tool before adding complexity.

The discipline here is restraint. As Salem warns: "Using AI for everything actually makes you less effective." The goal is selective, high-leverage automation, not universal AI application.

### Concept 8: Handoff Drift and the PM-as-Prototyper

Dhyey Mavani ([#070](../../sources/070-dhyey-mavani-handoff-drift.md)) describes a concrete workflow change at Anthropic that eliminates what he calls **Handoff Drift** -- the progressive degradation of intent as a specification passes through multiple handoffs (PM writes spec, design interprets the spec, engineering interprets the design, each handoff adds a week and introduces drift). At Anthropic, product managers don't write PRDs. They use Claude Code to build the first version of the feature themselves, then ship an experiment. The whole company dogfoods it for weeks, and only then do they ship.

This is a concrete evolution of the specification-first pattern: the PM role expands from "specification writer" to "prototype builder." The skill is specification and intent communication, not programming. The prerequisite is an AI-friendly codebase (Tailwind instead of custom CSS, microservices architecture, reduced codebase size). If your experimentation cycle is 6 weeks and your competitor's is 3 days, they are running 13x more experiments per quarter. See also: [Module 06: Strategy and Economics](../06-strategy-and-economics/README.md) for the organizational implications.

### Concept 9: Incremental Prompting vs. Monolithic Instructions

Income stream surfers ([#072](../../sources/072-income-stream-surfers-antigravity-convex.md)) demonstrates a common failure mode and its antidote. Vibe coding fails when people dump a massive prompt and expect a working app. The solution: set up authentication, database, and backend incrementally -- each step verified before moving to the next. The creator proves that even weaker models (Gemini 3 Flash) can handle structured, step-by-step prompting. This echoes the specification-first philosophy at a more granular level: reduce the surface area that AI needs to handle at any one time, and verify each integration step before compounding complexity.

Greg Isenberg ([#091](../../sources/091-greg-isenberg-claude-code-directory.md)) demonstrates a practical application of incremental prompting in a data enrichment context. His guest Frey Chu walks through building a profitable online directory using Claude Code and the open-source Crawl4AI web scraper -- a seven-step process that starts with scraping 71,000 rows from Google Maps, then runs sequential enrichment passes: business verification (71K down to 20K), website crawling to identify actual businesses (20K down to 725), then separate passes for inventory, images (validated via Claude Vision at $30 for 700 listings), amenities, and service areas. Each pass requires its own prompt iteration and edge case handling. The key insight for this module: Chu explicitly uses a "game plan" prompt before burning tokens on any major step, asking Claude Code to outline its approach before executing. This maps directly to the specification-first pattern applied to data workflows rather than code generation -- and demonstrates that the incremental prompting approach scales to non-trivial real-world data processing tasks.

### Concept 10: Meta-Cognitive Frameworks for Prompt Design

Justin Sung ([#100](../../sources/100-justin-sung-top-1-percent-thinking.md)) provides six "meta models" -- mental frameworks that govern how you apply any framework, including prompting and specification. While not explicitly about AI, they map directly onto the challenges of prompt design and context engineering:

**Nonlinearity**: Most real-world problems involve multifactorial relationships. Linear thinking -- "if I prompt A, I get B" -- systematically misses variables. The remedy: map all factors before simplifying the prompt. This directly parallels context engineering -- oversimplifying a prompt strips out variables the model needs.

**Framing bias**: The way a problem is presented shapes how you think about it. If you can only see one framing, you are almost certainly missing the breakthrough perspective. This is the essence of prompt engineering: reframing a problem for the model rather than accepting the first framing that feels logical. The Toyota Andon cord example -- reframing "efficiency = never stopping the line" to "efficiency = constantly learning" -- illustrates how reframing can unlock entirely new solution spaces.

**Delayed discomfort**: Avoiding cognitive difficulty upfront does not eliminate it -- it shifts the cost (often amplified) to the future. This maps directly to the specification-first pattern: skipping thorough specification to start prompting immediately creates deferred rework that compounds. As Sung puts it: "The discomfort is there regardless. It's just do you pay that upfront or do you pay that later?"

These meta-cognitive principles apply at every level of AI interaction -- from crafting a single prompt to designing an entire agentic workflow. They explain why specification-first development works (it forces upfront cognitive investment) and why vibe coding often fails (it defers that investment to debugging time).

### Concept 11: The AI Slop Problem and Feelings-First Design

Greg Isenberg and designer Sariah ([#075](../../sources/075-greg-isenberg-ai-slop-design.md)) identify a new problem created by vibe coding's success: everything looks the same. Functional apps can now be scaffolded quickly, but the results are visually homogeneous -- the "what it does" is solved, but "how it makes you feel" is the differentiator. Nobody downloads yet another generic app.

Their solution is a design-first workflow that starts with emotional specifications before touching any visual tool: how should the app make users feel? These emotional specs become the filter for every subsequent design decision. The practical pipeline chains Claude (brand strategy and prompt generation) with Weavy AI (visual asset generation), Cosmos (mood boards), Figma (composition), and image models. A key insight: find one image you love and build the entire brand around it. This represents a specification-first pattern applied to design rather than code -- defining the outcome emotionally before using AI to generate assets.

## Patterns & Practices

### Pattern: Specification-First Development

- **When to use**: Before any AI-assisted building task, whether a one-line prompt or a multi-day project.
- **How it works**: Before you prompt, write a plain-language specification: (1) What should it do? (2) What does success look like? (3) What are the edge cases? (4) What does it NOT need to do? Only after answering these questions do you begin interacting with the AI.
- **Example**: Instead of prompting "build me a user dashboard," write: "A dashboard that shows the user's last 10 orders, with date, status, and total. Success: renders correctly with 0, 1, and 100+ orders. Does not need: filtering, export, or admin views." The second version produces dramatically better first-pass output.
- **Source**: [#005](../../sources/005-nate-b-jones-vibe-coding-readiness.md)

### Pattern: The RTCEOC Prompt Framework

- **When to use**: For high-stakes prompts where accuracy, format, and tone all matter.
- **How it works**: Construct the prompt using six sequential components: **R**ole, **T**ask, **C**ontext, **E**xamples, **O**utput, **C**onstraints. For lower-stakes work, use a subset (Task + Context is often enough). Build successful prompts into your reusable library.
- **Example**: "You are a senior backend engineer reviewing a pull request [Role]. Identify potential bugs, performance issues, and security concerns in the following code [Task]. This is a Rails 7 application using PostgreSQL and Sidekiq [Context]. Format your review as a numbered list with severity labels (Critical/Warning/Nitpick) [Output]. Do not suggest stylistic changes or formatting preferences [Constraints]."
- **Source**: [#006](../../sources/006-ali-salem-4-ai-skills.md)

### Pattern: Fresh Context Per Task

- **When to use**: Whenever an AI conversation starts degrading -- contradictions, forgotten context, declining quality.
- **How it works**: Rather than one long meandering conversation, break work into discrete tasks. Each task gets a fresh context window with a clear specification. For command-line tools like Claude Code, this means separate sessions. For chat interfaces, this means new conversations with the relevant context re-attached via Projects or document links.
- **Example**: Instead of one 2-hour conversation that builds a full feature, run five separate 20-minute sessions: "design the database schema," "implement the API endpoints," "write the frontend components," "write the tests," "review everything together." Each session starts clean.
- **Source**: [#005](../../sources/005-nate-b-jones-vibe-coding-readiness.md), [#011](../../sources/011-confluent-developer-context-engineering.md)

### Pattern: Context Window Budgeting

- **When to use**: When building any agentic application or long-running AI workflow.
- **How it works**: Map out how much context window space each component consumes: system prompt, tool descriptions, resources, conversation history, tool call records. Target 60-70% utilization as your operating ceiling. Monitor growth over agent iterations. When approaching the ceiling, apply compaction (summarize history), offload to memory (store intermediate results externally), or decompose into sub-agents.
- **Example**: A 200K-token context window has an effective budget of ~130K tokens. If your system prompt is 2K, tool descriptions are 8K, and initial resources are 20K, you have ~100K tokens for conversation history and tool calls before quality degrades. Plan accordingly.
- **Source**: [#011](../../sources/011-confluent-developer-context-engineering.md)

### Pattern: Three-Layer Validation

- **When to use**: Whenever AI output will be used for decisions, shared publicly, or committed to a codebase.
- **How it works**: Apply three validation layers: (1) Use grounded tools (NotebookLM for document-based Q&A, Perplexity for sourced research). (2) Add self-evaluation prompts (confidence scoring, source restriction, "say I don't know" permission). (3) Cross-check with a different model (create in Claude, critique in ChatGPT, or vice versa).
- **Example**: After generating a technical analysis in Claude, paste the output into ChatGPT with the prompt: "You are a skeptical reviewer. What claims in this analysis are weakest? What might be fabricated? What needs a citation?" Different model architectures catch different failure modes.
- **Source**: [#006](../../sources/006-ali-salem-4-ai-skills.md)

### Pattern: MCP-Style Resource Discovery (Beyond RAG)

- **When to use**: When building production agents that need access to business-specific data without bloating the context window.
- **How it works**: Instead of dumping all potentially relevant documents into context (naive RAG), expose resources as queryable endpoints with text descriptions and parameter schemas (MCP pattern). Include resource *descriptions* (not full content) in one LLM call. Let the LLM decide which resources it actually needs. Retrieve only those resources for the next call. Pass references (e.g., user IDs) instead of full objects, with tools available to fetch details on demand.
- **Example**: Rather than stuffing 50 Jira tickets into context, provide a tool description: "search_jira(query, project, status) -- Search Jira issues by JQL query. Returns issue key, title, and status." The model calls this tool only when it needs specific ticket information, keeping context lean.
- **Source**: [#011](../../sources/011-confluent-developer-context-engineering.md)

## Common Pitfalls

- **Pitfall: Prompting before specifying.** The most common failure mode. When the AI can build anything in minutes, the temptation is to start immediately and iterate. But iteration without direction produces incoherent output. Avoid this by writing your specification *before* opening the AI tool. Even a two-sentence description of "what it should do" and "what success looks like" dramatically improves results.

- **Pitfall: Over-engineering every prompt.** The six-step framework is for high-stakes work. Applying Role + Task + Context + Examples + Output + Constraints to a simple "summarize this email" request wastes time. Calibrate effort to task importance. Salem is explicit about this: build reusable prompts for recurring high-stakes tasks, and use lightweight prompts for everything else.

- **Pitfall: Treating the context window as unlimited.** A 1M-token context window sounds enormous until you account for system prompts, tool descriptions, resources, conversation history, and tool call records all competing for the same space. Performance peaks at 60-70% capacity. Filling it to 100% produces worse results, not better. Avoid this by budgeting context explicitly and applying compaction before the window fills.

- **Pitfall: Trusting AI output without validation.** Hallucinations are a structural property of probabilistic language models, not a bug that will be fixed in the next release. Even frontier models fabricate plausible-sounding information. Avoid this by layering validation: grounded tools, self-evaluation prompts, and cross-model critique. Never publish or commit AI-generated content without at least one validation pass.

- **Pitfall: Building one-off prompts instead of systems.** A brilliant prompt used once has linear value. The same prompt saved in a text expander, refined over iterations, and shared across a team compounds. Most people never take the five minutes to save a successful prompt. Avoid this by maintaining a prompt library from day one, even if it starts as a simple text file.

- **Pitfall: Spreading across too many AI tools.** Analysis paralysis from the AI tool landscape is real. Salem's advice is counterintuitive but effective: pick one generalist AI, fit as many use cases into it as possible, and only add specialist tools when the generalist genuinely falls short. Mastery of one tool beats shallow familiarity with ten.

- **Pitfall: Ignoring the "Goldilocks" zone for system prompts.** Berglund identifies a sweet spot between too vague ("do a good job") and too prescriptive (encoding if-then logic). Define outcomes and broad approaches, then let the LLM figure out implementation. If you are writing conditional logic in a system prompt, you are doing the model's job for it.

## Hands-On Exercises

1. **Write a specification before you prompt.** Pick a real task you would normally start by prompting immediately. Instead, spend 5 minutes writing a plain-language specification: what should it do, what does success look like, what are the edge cases, what does it NOT need to do. Then prompt using the specification. Compare the output quality to your usual approach.

2. **Build your first sticky workflow.** Choose a task you do at least weekly with AI. Write a prompt using the RTCEOC framework (or a subset). Save it in a text expander or prompt library. Use it three times over the next week and refine it after each use. Notice whether the compounding effect is real.

3. **Audit your context window usage.** In your next AI coding session, pay attention to when the model starts degrading (contradictions, forgotten context, lower quality). Note approximately how many exchanges in. Try breaking the same work into fresh-context tasks and compare the quality. This builds intuition for context window limits.

4. **Practice three-layer validation.** Generate a technical analysis or research summary in your primary AI tool. Then: (a) Ask the AI to score its own confidence on each claim. (b) Paste the output into a different model with the prompt "What is weakest, possibly fabricated, or needs a source?" (c) Manually verify the two lowest-confidence claims. Track how often the validation layers catch real errors.

5. **Map your automation candidates.** Follow Salem's three-step process: list your weekly tasks, identify which are repeatable, digital, and clearly definable, then filter by pain threshold. Pick the highest-pain candidate and build an AI workflow for it. If your generalist AI does not handle it well, find a specialist. The goal is one new sticky workflow, not ten experiments.

6. **Budget a context window.** For an agentic workflow (or a long conversation you are planning), estimate the token cost of each component: system prompt, tool descriptions, resources you will include, expected conversation history growth. Calculate when you will hit 60-70% capacity. Plan your compaction or decomposition strategy before starting.

## Source Material

| Source | Creator | Key Topics |
|--------|---------|------------|
| [005: 90% Fail at Vibe Coding](../../sources/005-nate-b-jones-vibe-coding-readiness.md) | Nate B Jones | Specification as key skill, failure modes, software vision, context discipline |
| [006: 4 AI Skills That Set You Apart](../../sources/006-ali-salem-4-ai-skills.md) | Ali H. Salem | RTCEOC prompt framework, sticky workflows, validation, tool stacking |
| [011: Prompt Engineering is Dead](../../sources/011-confluent-developer-context-engineering.md) | Tim Berglund (Confluent) | Context engineering, six context components, 60-70% rule, MCP, compaction |
| [038: When the Interface Flattens Into a Prompt](../../sources/038-interface-studies-prompt-interface.md) | Interface Studies (Sal) | Specification as cognitive demand, two paths from the chat box, Einstellung effect, interface shapes thinking |
| [040: Stop Feeding Claude Your Entire CLAUDE.md](../../sources/040-charlie-automates-claudemd-context.md) | Charlie Automates | Monolithic CLAUDE.md problem, domain-based rule segmentation, context brackets for adaptive verbosity, focus over intelligence |
| [042: Vibe Coding is a Trap](../../sources/042-devforge-vibe-coding-trap.md) | DevForge | Understand-first pattern, mental models as the real asset, senior developer AI usage pattern, design before generating |
| [031: 9 AI Concepts Explained](../../sources/031-bytebyteai-ai-concepts.md) | ByteByteAI | Prompt engineering techniques (few-shot, chain-of-thought), RAG as context strategy, tokenization basics |
| [070: Handoff Drift](../../sources/070-dhyey-mavani-handoff-drift.md) | Dhyey Mavani | Handoff drift elimination, PM-as-prototyper pattern, AI-friendly codebase prerequisite, experimentation velocity |
| [071: Future of Software Development](../../sources/071-martin-fowler-future-software-dev.md) | Martin Fowler (Deer Valley retreat) | Spec-as-library experiment, specification as primary artifact, developer experience = agent experience |
| [072: Build ANYTHING: Google Antigravity + Convex + Clerk](../../sources/072-income-stream-surfers-antigravity-convex.md) | Income stream surfers | Incremental prompting vs. monolithic, backend-as-a-service stack, step-by-step verification |
| [075: Stop Shipping AI Slop](../../sources/075-greg-isenberg-ai-slop-design.md) | Greg Isenberg / Sariah | AI slop problem, feelings-first design workflow, multi-tool AI brand pipeline, emotional specifications |
| [084: The 60% Rule Stops Context Rot](../../sources/084-dylan-davis-context-rot-60-rule.md) | Dylan Davis | 60% rule for context windows, four warning signs of context rot, handoff strategy, strategic file management |
| [091: Claude Code built me a $273/Day online directory](../../sources/091-greg-isenberg-claude-code-directory.md) | Greg Isenberg / Frey Chu | Sequential data enrichment passes, "game plan" prompting before execution, Claude Vision validation, directory building as incremental workflow |
| [100: How To Think Like The Top 1%](../../sources/100-justin-sung-top-1-percent-thinking.md) | Justin Sung | Meta-cognitive frameworks for prompt design, nonlinear thinking, framing bias, delayed discomfort as specification principle |
| [108: The 5 Levels of AI Coding](../../sources/108-nate-b-jones-five-levels-ai-coding.md) | Nate B Jones | Specification as bottleneck at Level 4-5, dark factory pattern, reverse-engineering specs for brownfield systems |
| [109: 5 Hacks To Use ChatGPT So Well It's Almost Unfair](../../sources/109-themitmonk-chatgpt-hacks.md) | theMITmonk | ESP framework for persistent context, adversarial prompting, domain-separated projects, voice mode for unstructured thinking |
| [113: I was an AI skeptic. Then I tried plan mode](../../sources/113-matt-pocock-plan-mode.md) | Matt Pocock | Plan mode as prompting discipline, think-before-act pattern, structured workflow for AI skeptics |
| [130: What is Prompt Caching? Optimize LLM Latency](../../sources/130-ibm-technology-prompt-caching.md) | IBM Technology | Prompt caching mechanics, latency optimization, cost reduction for repeated context |
| [138: I Started A Coding Habit](../../sources/138-neuralnine-coding-habit.md) | NeuralNine | Understand-first workflow, reference implementation as specification, daily coding habit for foundational skills, comprehension before delegation |
| [152: Never Run claude /init](../../sources/152-matt-pocock-never-run-init.md) | Matt Pocock | Four phases of agent context usage, instruction budget (300-500), discoverable vs. undiscoverable information, skills as alternative to global context |
| [153: Delete your CLAUDE.md](../../sources/153-theo-delete-claudemd.md) | Theo (t3.gg) | Study showing +4% improvement / -3% degradation, pink elephant problem, CLAUDE.md as diagnostic tool, strategic misdirection |
| [159: After Two Years of Vibecoding, I'm Back to Writing by Hand](../../sources/159-mo-bitar-vibecoding-handwriting.md) | Mo Bitar | Diff-level illusion, deception cycle of AI coding, specification limitations at every complexity level |
| [164: Your codebase is NOT ready for AI](../../sources/164-matt-pocock-codebase-ai-ready.md) | Matt Pocock | Deep modules for AI navigation, graybox modules (human interface / AI implementation), AI as perpetual new starter |
| [170: The 4 Skills That Actually 10x Output](../../sources/170-nate-b-jones-four-prompting-disciplines.md) | Nate B Jones | Four disciplines of prompting (craft/context/intent/specification), five specification primitives, synchronous-to-autonomous shift |

## Further Reading

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) -- Official documentation on prompting Claude effectively
- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/) -- The protocol Berglund references for intelligent resource discovery
- [Module 01: Foundations](../01-foundations/README.md) -- The landscape context that explains why these skills matter now
- [Module 03: Claude Code Essentials](../03-claude-code-essentials/README.md) -- Apply the prompting and workflow patterns from this module to a specific tool
- [Module 04: Agentic Patterns](../04-agentic-patterns/README.md) -- Agent decomposition, compaction, and memory as architectural solutions to context management
