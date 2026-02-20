[00:00] Two visions of the Asian future shipped
[00:02] just 20 minutes apart a week or so ago.
[00:04] The one you pick changes how you work.
[00:06] Open AI shipped an AI system that's
[00:08] designed to be handed a task and left
[00:10] alone. You walk away, it works for
[00:12] hours, you come back to finished code.
[00:14] Anthropic shipped Opus 4.6. It's
[00:17] designed to plug into every tool you
[00:19] use, coordinate teams of agents that
[00:21] talk to each other, and it extends
[00:22] beyond code into every kind of knowledge
[00:25] work. same afternoon, two completely
[00:28] different answers in February to the
[00:30] same question. What should an AI agent
[00:32] actually do for you? Most of the
[00:35] coverage you're going to read is going
[00:36] to frame this as a race. Who's ahead?
[00:38] Open AI versus anthropic? Which
[00:40] benchmark is higher? Who shipped first
[00:43] and who is best? Look, I'm not here to
[00:46] get into the benchmark thing. The story
[00:47] that is really interesting to me is how
[00:50] genuinely different visions of agents
[00:53] fit into your work today. These both
[00:56] exist as shipped products. The one you
[00:58] reach for determines how your week
[01:00] actually changes. How the time you spend
[01:02] on AI shapes the things you can
[01:05] accomplish. The gap between the releases
[01:07] might be tiny 20 minutes. But the gap
[01:10] around what these companies think agents
[01:12] can do could not be wider.
[01:15] And that gap is what I want to talk
[01:17] about today. I covered Opus 4.6 in depth
[01:20] in a separate video. what the model can
[01:22] do, what the benchmarks mean, why the
[01:24] fact that it can build a C compiler
[01:26] matters. This video is more on the codec
[01:29] side. What did OpenAI ship? How does it
[01:31] work? And maybe if you don't understand
[01:34] Codeex and you're not a coder, how would
[01:36] you think about the approach to work
[01:38] that Codeex has versus what Claude has
[01:41] and what use cases you could use even as
[01:43] a non-engineer? This is what the
[01:45] divergence looks like if you strip away
[01:47] the model names and the benchmark scores
[01:49] and just think about how your week would
[01:51] change. Codeex is a system that you hand
[01:54] work to and you really can let go of it.
[01:57] You describe the task well. Say it's
[01:59] analyzing a codebase or processing a
[02:01] bunch of documents and then you go do
[02:03] something else. It will take its time.
[02:05] hours later, sometimes many hours later
[02:07] on complex coding challenges, the system
[02:10] will let you know when it's done and you
[02:14] can review it and you can figure out how
[02:16] it works. By the way, some people are
[02:18] actually hooking up their codeex
[02:20] instances into messaging apps so that
[02:22] Codex can let them know on their phones
[02:25] when work is done. That's how long the
[02:27] system is taking. That's true for cloud,
[02:29] too. Meanwhile, Anthropic, the makers of
[02:30] Claude, built a system that works inside
[02:33] the tools that you already use and that
[02:35] coordinates teams of agents that talk to
[02:37] each other directly. I want to be clear
[02:40] here. Codeex can run multi- aent systems
[02:42] as well. But Anthropics teams of agents
[02:45] are designed more for peer-to-peer
[02:48] communication among themselves. Whereas
[02:50] Codeex has adopted an agent framework
[02:52] that is more strictly spaghetti shaped
[02:55] where you actually have a central
[02:57] planning agent and the codeex agents
[02:59] stream out from that planner agent and
[03:02] don't have a lot of interaction
[03:03] together. Anthropics Opus 4.6 can hook
[03:06] into your Slack easily. It can check
[03:08] your project tracker. I talked in a
[03:10] previous video about how important it is
[03:12] to Anthropic to integrate with the
[03:14] places where work already happens and
[03:17] that's what we see with Opus' vision for
[03:19] work in the 4.6 release. So you can
[03:21] think of Codex as an employee who you
[03:23] delegate to who might have a team
[03:26] supporting them but you don't interact
[03:27] with them a whole lot. You can think of
[03:29] Claude more as a whole team that you're
[03:31] directing. Codeex tends to optimize for
[03:33] getting very complex technical
[03:35] challenges right on its own. Claude
[03:38] tends to optimize for fitting into how
[03:40] you already work and then scaling across
[03:42] your department and other departments to
[03:45] enable AI powered work inside current
[03:48] workflows. So codeex is more about
[03:50] changing your workflows and claude is a
[03:52] little bit more about fitting into your
[03:54] existing workflows. If you lead a team,
[03:56] the question you should be asking is not
[03:58] which one is better here. It is which of
[04:00] my team's workflows are delegationshaped
[04:03] problems? send it away and come back to
[04:06] me with finished work. And which are
[04:07] more coordination problems where the
[04:10] value comes from agents working across
[04:12] multiple tools and talking to each
[04:14] other, maybe talking to me, because the
[04:16] answer determines which system changes
[04:18] your operating model faster. And for
[04:21] most organizations, you may need a mix
[04:23] of both systems. With that framework in
[04:25] mind, let's look a little bit more about
[04:27] what's inside each of these. First,
[04:29] codecs. The hand it off and walk away
[04:32] experience that I'm describing with
[04:33] codeex 5.3 is backed up by benchmark
[04:37] scores that explain why it feels so
[04:39] different from what came before.
[04:40] Terminal Bench 2.0, the benchmark that
[04:43] measures whether a model can sit down
[04:44] with a real codebase and actually get
[04:46] work done, not just solve toy problems.
[04:49] Codeex really does well here. 4 point C
[04:52] codeex 5.3 delivers a 77.3% score here
[04:56] versus a notable gap with Opus 4.6 six,
[04:59] which sits at 65.4%.
[05:02] Codeex did not edge past this benchmark.
[05:05] It cleared it by 12 points on a scale
[05:07] where a single point improvement can
[05:09] make the news. In practical terms, the
[05:11] tasks your engineering team estimates at
[05:14] two sprint days are the kind of work
[05:16] codeex can handle overnight. Another
[05:18] benchmark is OS World Verified, which
[05:21] tests whether a model can operate a real
[05:23] computer, navigate interfaces, handle
[05:25] actual software environments. ODEX 5.3
[05:28] scored 64.7%.
[05:30] Its predecessor 5.2 managed only 38.2%
[05:35] and it is 25% faster than 5.2 while
[05:39] using 93% fewer tokens on the tasks
[05:42] where previous models were most
[05:44] wasteful. And so what does that add up
[05:46] to? It's faster, it's cheaper, and it's
[05:48] more capable. The usual trade-off
[05:51] between capability and cost does not
[05:53] apply here. I think the number that
[05:55] matters most is not in the benchmarks
[05:56] though. It's this. Codeex 5.3 is the
[06:00] first frontier AI model that really
[06:02] helped to build itself. Not
[06:04] metaphorically. OpenAI used earlier
[06:06] versions of codec during development to
[06:08] debug training code, optimize
[06:10] infrastructure, and identify issues in
[06:12] the pipeline that built the final model.
[06:14] The model didn't arrive magically from a
[06:16] clean room. It was tested against real
[06:18] production code bases from day one at
[06:21] OpenAI. not synthetic benchmarks, not
[06:23] curated problem sets. It was in the mess
[06:26] building itself. That's why the
[06:27] benchmark scores translate to production
[06:29] capability in a way that maybe previous
[06:32] scores often did not. One more result
[06:33] worth noting because I think it signals
[06:35] where capability is headed. Codeex 5.3
[06:38] is the first model to receive a high
[06:41] capability cyber security classification
[06:43] in red team evaluators
[06:46] concluded it could potentially automate
[06:48] end-to-end cyber operations not assist
[06:51] with fully automate. That finding
[06:53] triggered additional safety protocols
[06:55] before release and it's the kind of
[06:57] result that makes government start
[06:58] writing new rules. When a commercially
[07:00] available model can autonomously conduct
[07:03] the full cycle of a cyber operation, the
[07:05] regulatory frameworks that we build
[07:07] around human operated tools don't feel
[07:09] very adequate. Sam Alman has called
[07:11] Codex the most loved internal product
[07:14] we've ever had. And having chatted with
[07:15] folks at Codex, I fully believe that.
[07:17] When the CEO of the company that made
[07:19] Chat GPT says a different product is the
[07:22] internal favorite, that should tell you
[07:24] something about where value is starting
[07:26] to shift inside the business that
[07:27] understands these tools the best. I also
[07:30] don't want to forget the Codeex app. 3
[07:33] days before 5.3 dropped, OpenAI shipped
[07:36] the Codeex desktop app. It's not a
[07:38] chatbot. It's not a browser tab. It's a
[07:40] native app that's designed from scratch
[07:42] as a command center for managing
[07:44] autonomous coding agents. Every task you
[07:47] give codeex runs in its own work tree,
[07:50] which is an isolated copy of your
[07:51] codebase where the agent can make
[07:53] changes without touching the code that
[07:55] you're working on or another agent is
[07:57] working on. If the agent's work is good,
[07:59] you can merge it in. If not, you can
[08:01] dump it. No risk to your working branch.
[08:03] No merge conflicts with what you were
[08:05] doing while the agent ran. So that means
[08:07] multiple agents can run simultaneously
[08:10] in separate threads, which is what I was
[08:12] talking about, each with its own work
[08:13] tree. You're not waiting for one task to
[08:16] finish before starting the next. You
[08:17] dispatch work the way a manager
[08:19] dispatches work to a team. Here's the
[08:21] problem. Go figure it out. Check in when
[08:23] you're done. The app includes
[08:24] automations like predefined triggers
[08:26] that dispatch agents when conditions are
[08:28] met. And if a new issue gets filed, an
[08:30] agent can automatically start
[08:31] investigating. If a test fails, an agent
[08:34] can automatically start debugging. If a
[08:36] PR lands, an agent can can automatically
[08:38] review it, which matches the pattern at
[08:40] OpenAI. So you define those triggers
[08:42] once and the system can just run them
[08:44] continuously. A skill system lets you
[08:46] teach Codeex your codebas's conventions,
[08:49] your team's pattern, your deployment
[08:51] quirks. Code A skills system lets you
[08:55] teach Codeex your codebases conventions,
[08:57] your team's patterns, your deployment
[08:58] quirks. Basically, persistent knowledge
[09:00] that carries across sessions so the
[09:02] agent doesn't start from scratch every
[09:04] single time. Basically, the entire
[09:06] development loop from I noticed a bug to
[09:08] the fixes deployed lives in a single
[09:11] interface now. And at no point does the
[09:13] interface assume a human needs to write
[09:16] the code. The result is an environment
[09:18] where you're not writing code. You're
[09:20] directing agents that write code the way
[09:22] a manager directs reports. That sounds
[09:25] like the future of AI to me. The hand it
[09:27] off and walk away experience that codeex
[09:29] as a whole is predicated upon only works
[09:33] if you actually trust the output enough
[09:35] to walk away. And this is what makes
[09:37] that bet trustworthy. When you give
[09:39] codeex a task, it does not start
[09:42] autocompleting and typing right away.
[09:44] Instead, it builds an internal plan. It
[09:46] decomposes the problem. It runs its own
[09:49] tests. It checks its own work. And
[09:51] underneath it, there's a three layer
[09:53] system that helps ensure it works well.
[09:55] There's an orchestrator that manages the
[09:57] overall task. Executors handle
[09:59] individual subtasks and a recovery layer
[10:01] detects failures and corrects them. The
[10:04] entire system is designed for one
[10:06] outcome, producing work you can trust
[10:09] without reviewing every line. Because
[10:11] guys, the world of reviewing every line
[10:13] in code is over. Now, the tradeoff to
[10:16] that whole approach is real. Codeex is
[10:19] measurably slower on simple tasks than
[10:21] tools that will prioritize speed. It's
[10:23] just not designed for simple tasks. Now,
[10:26] on complex tasks like a module
[10:28] refactoring that touches a dozen or 20
[10:30] files or a feature in a new codebase or
[10:32] a bug that only surfaces under system
[10:34] load, that correctness architecture
[10:36] means you spend less total time because
[10:39] you're not cleaning up after the model
[10:41] or spending a long time figuring out
[10:42] where the problem is. You hand off a
[10:44] task your team estimated at a couple of
[10:46] sprint days and you get to come back to
[10:48] finished work. your net time investment
[10:51] was maybe a light review and it wasn't
[10:53] the execution at all. For an engineering
[10:56] manager or a team lead, that math
[10:57] changes frankly how you plan your
[11:00] sprints and your team capacity and you
[11:02] start to think about how your senior
[11:04] people spend their time because you know
[11:06] you can delegate more and more to
[11:07] codeex. Codeex already practices
[11:11] meaningful self-management from an
[11:12] engineering perspective. The system
[11:14] monitors its own quality. It corrects
[11:16] its own errors. It reorganizes task
[11:19] orders based on what it discovers while
[11:21] working. The next step, agents deciding
[11:23] on their own to spin up additional
[11:25] agents when a task would benefit from
[11:27] that, hasn't shipped yet, but the
[11:29] three-layer system is designed to
[11:31] support that kind of dynamism, and I
[11:32] expect it soon. The orchestrator already
[11:35] manages the orchestrator already manages
[11:38] executor agents, and managing sub
[11:39] orchestrator is a similar pattern, just
[11:41] one level up. Our agent hierarchy
[11:44] management is going to continue to level
[11:46] up over the course of 2026 and Codeex is
[11:49] designing an interface that is built for
[11:51] that kind of scale. The distinction
[11:53] between this and every AI tool you've
[11:55] used comes down to what changes about
[11:58] your day. A co-pilot would suggest the
[12:00] next line while you're writing. It might
[12:02] save you typing time. Codeex takes the
[12:04] keys to the car and drives to the
[12:06] destination while you do other work. So,
[12:08] the co-pilot might make you faster at
[12:10] the task, but the autonomous agent
[12:12] eliminates the task from your schedule
[12:14] entirely. It is a different operating
[12:16] model, and it takes some getting used
[12:18] to. Now, this is the part most coverage
[12:20] misses. I use codecs for things that
[12:23] have nothing to do with software
[12:24] development. when I come out of a
[12:26] three-hour meeting with a super dense
[12:28] transcript, multiple threads of
[12:30] conversation, no tagged speakers, action
[12:33] items buried in tangents, decisions made
[12:35] in the last 5 minutes, but but nobody
[12:38] remembered to write them down. I just
[12:39] dump that full transcript at codeex and
[12:42] I ask it for a clean, scannable HTML
[12:46] page that captures the meeting in a way
[12:48] that people will actually read. key
[12:50] decisions at the top, open questions
[12:52] flagged, action items pulled out with
[12:54] owners and deadlines, the whole tangled
[12:57] mess of a long conversation organized
[12:59] into something useful. And it does it.
[13:01] It handles hours and hours and hours of
[13:04] content without losing the thread at
[13:06] all. Because the same architecture that
[13:08] lets it sustain 7 hours or days of
[13:10] autonomous coding lets it sustain deep
[13:12] analysis of long complicated documents
[13:15] really, really easily. The correctness
[13:17] optimization turns out to be not just a
[13:19] coding feature. It's a reasoning feature
[13:21] and reasoning applies to everything.
[13:24] That is just one of the non-obvious
[13:26] implications of long-running agents
[13:29] optimized for correctness. If you you
[13:31] could hand it two years of employee
[13:33] survey data and ask for a structured
[13:35] analysis of retention risk factors. It
[13:37] would read every response. It's going to
[13:39] cross reference demographics. It will
[13:41] identify patterns across time periods
[13:42] and produce a report your CHRO can act
[13:45] on. You could hand it a 400page
[13:47] regulatory filing and ask it to check
[13:49] compliance against your own internal
[13:51] policies. It can hold both documents in
[13:53] working memory and flag every single
[13:55] discrepancy. The architecture does not
[13:57] know or care whether the input is Python
[13:59] or English. It cares about sustained
[14:02] accurate processing of complex
[14:04] information over long periods of time.
[14:06] And that becomes useful whether or not
[14:09] you write code. The pricing makes this
[14:11] really striking. At 20 bucks a month, a
[14:13] Chat GPT plus subscription includes full
[14:16] access to codecs. Not a separate
[14:18] product, not an enterprise add-on. The
[14:21] entire autonomous agent capability
[14:23] included. For context, the inference
[14:26] compute required to run a 7-hour session
[14:29] is, I would guess, a hex more easily
[14:32] than a chatbot conversation over that
[14:34] time period. You're burning way more
[14:35] tokens. Open AAI is subsidizing agent
[14:38] compute at scale. And that tells you
[14:40] they're building for adoption. They want
[14:43] people to use codecs. But it's time now
[14:45] to look at the other side of the coin.
[14:47] What does Opus 4.6 tell us about where
[14:50] Enthropic is going and how different
[14:52] that is from OpenAI and Codeex's vision?
[14:55] Where Codeex bets on autonomous
[14:57] correctness. Send it away. Trust the
[14:59] output. Claude Code bets on integration.
[15:02] It bets on coordination. It bets on
[15:04] expanding what agent means beyond code
[15:07] into explicitly every kind of knowledge
[15:10] work. If Codex is the meticulous
[15:12] employee who works alone in a quiet
[15:14] room, Claude is more like the team that
[15:16] sits in the open office floor plan, uses
[15:18] your tools, and talks to each other
[15:20] while they work. Claude Code's core is
[15:22] minimal to the point of provocation. It
[15:25] just has four tools. Read a file, write
[15:27] a file, edit a file, run a bash command
[15:30] in roughly 200 lines of code. No
[15:32] orchestrator, no recovery system, no
[15:35] multi-phase planner. All the
[15:37] intelligence is in the model itself. The
[15:39] simplicity exists for a specific reason.
[15:42] It lets claude extend in any direction
[15:45] through MCP model context protocol. The
[15:47] model can connect to essentially any
[15:49] external tool your organization already
[15:51] uses. GitHub, Slack, Postgress, Google
[15:54] Drive, you name it. Where Codeex works
[15:57] in its own isolated world and hands you
[15:59] back results, Claude works inside your
[16:02] existing workflow, pulling from the same
[16:04] sources your team uses and pushing
[16:05] results to the same places they check.
[16:08] For a team lead deciding between the
[16:09] two, this becomes a very practical
[16:11] distinction. Codeex will produce
[16:14] excellent work in isolation and Claude
[16:16] produces work that's already integrated
[16:18] into how your organization operates.
[16:21] Then there's the capability CEX doesn't
[16:22] have agent teams. Where Codex runs
[16:25] multiple agents in parallel but
[16:27] independently, each working on its own
[16:29] task, Claude's agents actually
[16:31] coordinate. A lead agent decomposes a
[16:34] project into work items. Specialist
[16:36] agents can handle subsystems and the
[16:38] agents can and do message each other
[16:40] directly, resolving dependencies and
[16:42] sharing context without routing
[16:44] everything through a bottleneck.
[16:46] 13 distinct operations arise for
[16:49] spawning, assigning, coordinating, and
[16:51] communicating between agents. So, think
[16:53] of it this way. Codex gives you, say,
[16:55] five skilled contractors who each work
[16:57] independently and hand you their
[16:59] deliverables. Claude gives you a team
[17:00] where the front-end specialist will tell
[17:02] the back-end specialist, I need this API
[17:04] endpoint shaped differently, and they
[17:06] sort it out between themselves. Both are
[17:08] really useful. They're useful for
[17:10] structurally different problems. and
[17:12] knowing which kind of problem you're
[17:14] looking at is a skill that separates
[17:16] people who get value from these tools
[17:18] from people who get frustrated by them.
[17:20] I would argue though that the biggest
[17:22] divergence is not about coding at all.
[17:24] It's about where each company thinks AI
[17:27] agents are headed. Anthropic launched
[17:29] Claude Co-work, a desktop application
[17:31] that extends the agent paradigm to
[17:33] knowledge work more broadly, not coding,
[17:35] knowledge work as a whole. marketing
[17:37] teams running content audits, finance
[17:39] teams processing due diligence
[17:41] documents, legal teams reviewing
[17:42] contracts, you name it. The non-coding
[17:44] implications of this work are concrete
[17:47] and immediate. A finance analyst can use
[17:49] Claude Co-work to hand a stack of due
[17:51] diligence documents into the model and
[17:53] get a set of evaluation criteria going.
[17:55] And then the agent will read every page,
[17:57] cross reference terms, flag risks, and
[17:59] produce lawyer ready redlines. work that
[18:01] took a team multiple days finished in a
[18:03] couple of hours with the agent pulling
[18:04] contacts from wherever it gets it from
[18:06] Google Drive from MCP. Maybe it pushes
[18:08] updates to Slack. This is all available
[18:11] right now. Codeex could also analyze
[18:13] those documents. It just would not route
[18:15] results through your existing tools and
[18:17] would require you to gather more of the
[18:19] context. Codex is betting that the
[18:22] biggest problems in the world are deep
[18:24] problems where you will need to assign
[18:27] an agent to just think about it for a
[18:30] long time and there is extremely high
[18:32] leverage on correct answers in the first
[18:35] try. Claude is betting on a wider bet.
[18:38] Claude wants agents in every workflow in
[18:40] every department connected to every tool
[18:43] all coordinating with each other. Codeex
[18:45] might be built so the agent can work
[18:47] alone and get it right. Claude is built
[18:49] so agents can plug into your existing
[18:51] tools and talk to each other as they go.
[18:53] So here's what I've learned from using
[18:54] both on a real work. The decision of
[18:56] which to pick comes down to three
[18:58] questions. First, can you tolerate
[19:01] errors in the initial output or is it a
[19:03] high correctness non-negotiable problem?
[19:06] If you're a developer refactoring a
[19:08] payment processing module or maybe a
[19:10] finance director preparing board numbers
[19:12] the execs must make decisions from
[19:14] Codeex's correctness architecture can
[19:17] earn the cost. Right? You hand it 200
[19:20] vendor contracts and ask it to flag
[19:22] every single non-standard term and it
[19:24] won't miss things. If you're iterating
[19:26] on something you'll review yourself
[19:27] anyway, like drafting a blog post or
[19:29] prototyping a dashboard, the correctness
[19:32] overhead isn't worth it and you might
[19:34] reach for clot. Second question, does
[19:36] the task live inside one environment or
[19:39] does it span a bunch of tools? Codeex
[19:41] works in its own isolated world. It
[19:42] takes whatever input you give it, it
[19:44] does the work and it hands it back. That
[19:46] isolation is a feature when the task is
[19:48] very self-contained. Analyze this
[19:50] codebase, build this component, audit
[19:52] this data. But most knowledge work is
[19:55] not very self-contained. a quarterly
[19:57] close where the agent pulls actuals from
[19:59] your accounting system, compares them
[20:00] against the forecast in sheets, drafts
[20:02] variance explanations in a doc. There's
[20:04] a bunch of tools in that workflow. You
[20:07] need to think about the tool you're
[20:09] choosing in the context of where the
[20:12] work lives. This is a situation where
[20:15] claude is shaped for the distributed
[20:18] nature of knowledge work and codeex is
[20:21] shaped for an assumption that you will
[20:24] want most heavy work done on a codebase
[20:27] that codecs can see. Third question is
[20:29] the work independent or interdependent?
[20:32] If you have five separate contract
[20:34] reviews that don't reference each other,
[20:35] you might start up five codec sessions
[20:37] in parallel and you get clean complete
[20:39] tasks for each of them. If you have a
[20:42] product launch where the press release
[20:43] needs to reference and align with
[20:45] landing page copy and the email sequence
[20:46] needs to pull quotes from the press
[20:48] release and the social post need to link
[20:50] to the landing page. It's very
[20:52] interdependent work where each piece
[20:54] starts to shape the others. Claude's
[20:56] agent team the press etc. And so the
[21:00] answer what most people as much as you
[21:02] would like is both in which tool the new
[21:05] one know one that to understand and draw
[21:07] from and that is why I am taking the
[21:09] time here to share with you the specific
[21:12] questions I ask myself when delegating
[21:14] work across these tools. There's one
[21:16] other question I think it's important
[21:18] that we ask here. Which approach ages
[21:21] better as capabilities improve every
[21:23] quarter? Codeex's bet gets stronger if
[21:26] individual agents keep getting more
[21:28] capable fast enough that coordination
[21:31] just becomes unnecessary. If an agent
[21:33] can handle an entire system end to end,
[21:36] not just a module, the whole thing, you
[21:37] don't really need agents talking to each
[21:39] other. The isolation that feels like a
[21:41] constraint today becomes absolutely
[21:43] irrelevant when a single agent is
[21:44] powerful enough to hold a complete
[21:46] project in its head. So the ceiling on
[21:48] Codex's model is one agent is so capable
[21:51] it can just delegate cleanly to sub
[21:53] agents eventually and it doesn't need
[21:55] teammates that can coordinate across.
[21:57] And frankly given that Codex 5.3 nearly
[21:59] doubled its predecessor scores tells me
[22:02] that OpenAI thinks that's a reasonable
[22:04] bet. I think Open AI also seems to think
[22:08] that code itself is a lever for
[22:10] attacking the rest of knowledge work.
[22:13] That the rest of knowledge work is
[22:15] starting to collapse into code. And if
[22:17] they doled a code agent that prioritizes
[22:20] correctness on very hard problems, they
[22:22] are at the highest leverage point in the
[22:24] ecosystem. Now Claude's bet gets
[22:26] stronger if real work stays
[22:28] fundamentally interdependent. If the
[22:30] most valuable problems cannot be cleanly
[22:33] decomposed into nice independent pieces
[22:35] of work, no matter how smart a given
[22:37] agent gets, if building a product isn't
[22:39] just building a front end and a backend
[22:41] separately and hoping they fit, or even
[22:44] giving that all to the agent and hoping
[22:46] it works, Claude is betting that we will
[22:49] continue to need to see strange edge
[22:52] cases, interdependencies, and frankly a
[22:55] lot more human involvement in how we use
[22:58] our AI thinking tools. tools. Remember,
[23:00] Claude's branding right now is all
[23:02] around thinking. And I think that the
[23:04] product shape they're choosing is a tool
[23:07] shape where they expect a human to
[23:09] interact with Claude and think about all
[23:13] of the edge cases and all of the
[23:15] interdependencies and help shape the
[23:18] final product through a lot of back and
[23:20] forth with an agent in a loop, which is
[23:22] really what Claude is. Then there's the
[23:24] network effect that a lot of analysis
[23:26] ignores. Every single new MCP
[23:28] integration makes the entire system more
[23:31] useful for everyone. So Claude's
[23:33] flywheel compounds very quickly. Now MCP
[23:36] support is enabled in OpenAI and Codeex.
[23:38] That's not a problem. But Codeex's
[23:41] isolated architecture doesn't
[23:43] automatically benefit from it in the
[23:45] same way. A Codeex agent cannot see your
[23:48] Jira board today nearly as easily as
[23:51] Claude. And if that's still the case
[23:53] when codec 6.0 know ships or whenever
[23:55] that will be. Then Claude's
[23:57] protocol-based approach means the
[23:59] integration ecosystem can continue to
[24:02] develop over time in a way that gives
[24:05] Claude a structural advantage if we're
[24:07] still using those other tools. Codeex is
[24:10] kind of betting that yes, you can roll
[24:12] your own. You can get connections into
[24:14] those tools as you need to, but
[24:16] fundamentally the future of work is not
[24:18] in ticket boards. The future of work is
[24:20] not in documents. It may not even be in
[24:22] spreadsheets. The future of work is
[24:23] code. And that knowledgework expansion
[24:25] question is the sleeper factor. If
[24:28] agents stay in engineering, both
[24:30] approaches can work and the choice can
[24:31] be about workflow preference. Claude is
[24:34] explicitly betting that agents will move
[24:36] into every department. Codeex seems to
[24:38] be starting to bet that agents will
[24:41] matter in code and department work will
[24:43] collapse into code. I think that's a
[24:45] very different vision of the future and
[24:47] I'm very curious to see which one starts
[24:49] to bear out. It's also possible these
[24:51] approaches will converge. Codeex is
[24:53] likely to add some integration
[24:54] capabilities. Claude will likely deepen
[24:56] its correctness architecture. Successful
[24:58] products tend to borrow from each other.
[25:00] iOS has gained customization and Android
[25:03] has gained polish over the years. But
[25:05] starting philosophies do shape products
[25:07] downstream. The way an initial decision
[25:10] echoes through every feature, every
[25:11] default, every assumption that's baked
[25:13] into the user experience. Open AI really
[25:16] started from the idea that correctness
[25:17] matters and agents should solve very
[25:19] hard problems in code. Anthropic started
[25:22] from agents should work together inside
[25:25] your tools. 10 generations later, those
[25:27] starting points are still going to be
[25:30] visible in how those systems approach
[25:32] work. If you're making decisions about
[25:34] what to pick this quarter, this means
[25:35] the choice isn't just which tool for
[25:38] which task. It's which organizational
[25:40] muscle do I want to build with my team,
[25:42] right? Do I want to build delegation? Do
[25:43] I want to build coordination? Which one
[25:46] serves the work my team does? If your
[25:48] highest value work is complicated,
[25:50] self-contained technical projects, you
[25:52] probably want to build that delegation
[25:54] muscle with codeex. If your highest
[25:56] value work crosses a lot of boundaries
[25:57] and runs through a bunch of tools, you
[25:59] may want to build the coordination
[26:01] muscle with clot. If you have both, and
[26:03] a lot of folks do, at least know when to
[26:06] use which. I'll remind you again, the
[26:08] people who are navigating a world where
[26:10] releases can come 20 minutes apart are
[26:13] not the ones who pick the tool and
[26:15] commit and say, "No, no, no, no, no. I'm
[26:17] not a codeex person or no no no no no no
[26:18] I'm not a claude person. They're the
[26:20] ones who develop the meta skill of
[26:22] understanding new capabilities quickly
[26:25] and they know how to restructure
[26:26] workflows around those capabilities and
[26:28] they know how to do it again when the
[26:30] next release ships. So taste, judgment,
[26:33] speed of adaptation, clarity about what
[26:35] you really need, those become durable
[26:38] advantages in a world where the
[26:40] underlying tech is changing faster than
[26:42] anybody can really absorb fully. The
[26:44] person who rebuilt their workflow around
[26:46] Opus 4.5 in Nove. The person who rebuilt
[26:49] their workflow around Opus 4.5 in
[26:51] November had to partially rebuild it
[26:54] again around Opus 4.6. I know some of
[26:56] those people. You will only thrive if
[26:58] you are ready for that. If you expect
[27:00] that and if you can adjust to that in a
[27:03] way that you you barely notice because
[27:05] AI just keeps coming and change is part
[27:07] of your workflow. Now, so two visions of
[27:10] the agent future ship 20 minutes apart.
[27:12] Which one wins is the wrong question.
[27:14] The right question is whether you are
[27:16] building the capacity personally or
[27:19] organizationally to use whichever one is
[27:21] best for the work in front of you to ask
[27:23] the right questions which that's why I
[27:25] shared them in this video. The agent
[27:28] world is arriving in 3D because it's
[27:31] arriving with two different visions that
[27:33] allow you to see a fully
[27:35] three-dimensional agent realized world.
[27:37] We would be silly to pretend that one is
[27:39] better than the other. would be smart to
[27:41] see both as competing visions and to use
[27:44] our binocular vision to understand how
[27:47] these competing visions of an agent
[27:49] world shape the software and the future
[27:51] of knowledge work. Look, probably
[27:54] something we'll release next Wednesday
[27:55] or Thursday or Friday. You will need to
[27:57] figure this out again. I will be back
[27:59] with another video. The one thing we
[28:02] know is that even though things are
[28:03] changing, some of these foundational
[28:06] questions about what work means and how
[28:09] AI agents should shape work, those are
[28:11] not changing. And we can follow that
[28:13] thread through when Codeex 5.4 ships or
[28:16] when Opus 4.7 ships. And uh I'll be back
[28:19] with a video then. Tears.
