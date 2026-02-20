[00:00] What's up engineers? Indie Devdan here.
[00:02] With the right skills, your agent can do
[00:04] tons of work for you. You know this, but
[00:07] by engineering the right stack of
[00:10] skills, sub aents, prompts, and
[00:12] reusability system, you can automate
[00:15] entire classes of work. If you don't
[00:17] have agents for these two classes of
[00:19] work we'll break down in this video,
[00:21] you're wasting time doing work your
[00:24] agents can do for you. This is the name
[00:26] of the game right now. How many problems
[00:28] can you hand off to your agents in a
[00:31] reusable scalable way? In the terminal J
[00:34] automate Amazon, we're kicking off a
[00:36] clawed code instance in fast mode. This
[00:39] is going to run a different type of
[00:41] workflow. This is going to run in a
[00:42] Gentic browser automation workflow. Now,
[00:45] this is a personal workflow that it's
[00:47] running. You can see here it's got a
[00:48] whole list of items that I need to
[00:51] purchase and it's going to do this for
[00:52] me. This is browser automation. As
[00:55] engineers, there's a more important task
[00:57] that we need to focus on as well. So,
[00:58] we'll open up a new terminal here, and
[01:00] we'll type JUI review. This is going to
[01:03] kick off a Gentic UI testing. You can
[01:06] see here we're kicking off three
[01:07] browsers. Uh, this is going to be a mock
[01:10] user test on top of Hacker News. And our
[01:12] UI tests are effectively going to
[01:14] operate a user story against Hacker
[01:17] News. You can have agents do your UI
[01:20] testing. Now, there are several benefits
[01:22] to this over traditional UI testing with
[01:24] justest or viest that we're going to
[01:26] cover in this video. But you can see
[01:27] here, you know, 40k tokens each they're
[01:29] completing. They're summarizing back to
[01:31] the primary agent. And you can see here
[01:33] these user stories have passed. Why is a
[01:36] gentic browser use so important? It's
[01:39] because it allows you to copy yourself
[01:41] into the digital world so you can
[01:43] automate two key classes of engineering
[01:46] work. Browser automation and UI testing.
[01:49] Whenever I sit down to automate a
[01:51] problem with agents, I always ask
[01:54] myself, what is the right combination of
[01:56] skills, sub agents, prompts, and tools I
[01:59] can use to solve this problem in a
[02:01] templated way for repeat success? In
[02:04] this video, I want to share my four
[02:06] layer approach for building agents that
[02:08] automate and test work on your behalf.
[02:10] Let's break down automating work on the
[02:13] web.
[02:17] Bowser is a opinionated structure using
[02:21] skill subvisions/comands and one
[02:23] additional layer we'll talk about. And
[02:25] the whole point here is to set up
[02:26] systems for agentic browser automation
[02:28] and UI testing. I don't just want to
[02:30] solve this problem for one codebase. I
[02:32] want a system that I can come to that's
[02:34] built in an agent first way to solve
[02:36] browser automation and UI testing. So
[02:39] let's start with the core technology. So
[02:40] you can see here the Amazon workflow is
[02:42] of course using claude with Chrome. You
[02:45] can activate this by using the d-chrome
[02:46] flag and it's a great way to use your
[02:49] existing browser session to accomplish
[02:51] work with agents. There are pros and
[02:53] cons to this approach which is why I
[02:55] needed another tool so that we could
[02:57] scale UI testing with agents. That is of
[02:59] course the playright CLI. Now this is
[03:02] super important and the developers know
[03:04] this. You want to be using CLIs, not MCP
[03:06] servers. MCP servers chew up your tokens
[03:08] and they're very rigid. You have to do
[03:10] it their way however the MCP server is
[03:12] built. This is why we always prefer CLIs
[03:15] and CLIs give us the massive benefit
[03:17] that we can build on top of it in our
[03:19] own opinionated way. So these are the
[03:22] two technologies that Bowser is built
[03:24] on. A couple key things to note here. We
[03:26] ran three agents that QA specific user
[03:28] stories and they all responded to the
[03:30] primary agent with success. You can see
[03:32] each of them has their own number of
[03:34] steps and they all have their own
[03:36] screenshots. This is super critical. You
[03:38] can see the autocomplete already picking
[03:40] up on what I want to do. I'm just going
[03:41] to hit tab enter. open the screenshots
[03:43] directory and let's go ahead and see
[03:45] what happened there. You can see that
[03:46] every step of the way our agents created
[03:49] a screenshot of the workflow view top
[03:52] post comments. We can walk through
[03:54] exactly what our agent did and how it
[03:56] validated everything. This is a simple
[03:58] mock example test, but imagine this
[04:00] running on your brand new user interface
[04:02] that you're building up with agents
[04:03] deploying very quickly. If one of your
[04:05] workflows goes wrong, your agents now
[04:07] have a trail of success and a trail of
[04:08] failure because they're taking
[04:10] screenshots along the way. I want to
[04:11] show you different ways you can layer
[04:13] your architecture. It's not just about
[04:15] skills. Everyone's very obsessed with
[04:16] skills. I want to show you how you can
[04:18] stack it up and layer it properly to get
[04:20] repeatable results at scale. So, let's
[04:22] jump into the codebase here. So, we'll
[04:24] start with the skill. So, include
[04:27] skills, we have two key skills, right?
[04:30] Cloud browser and playright browser.
[04:31] Let's start with the more interesting
[04:32] one, playright browser. If I open this
[04:34] up, you can see we have this structure.
[04:36] I'll collapse and you can see all the
[04:38] details of this skill. Now the key
[04:40] pieces are here. This is a token
[04:42] efficient CLI for playright. Runs
[04:44] headless supports parallel sessions and
[04:46] we have named sessions for stored state.
[04:48] All right. So if we open this up here,
[04:49] you know, you can see we have just a
[04:51] bunch of details on how this works. And
[04:53] this is directly using the playright
[04:55] CLI. You know, the nice part about
[04:56] building your own skill is you get to
[04:58] customize it however you want, right? So
[05:00] they have their own opinionated skill in
[05:01] here. You know, I always recommend you
[05:03] check out how other engineers are
[05:05] building their skill. There's reference
[05:07] files here and then they have a
[05:08] skill.mmd kind of just breaking down
[05:10] what the help command would do. Anyway,
[05:12] you can see that's how they broke that
[05:13] down inside of this. I'm breaking it
[05:15] down my own way. I'm setting up defaults
[05:17] that I want for repeated success for the
[05:19] way that I'm going to be building
[05:20] applications. This is an important thing
[05:22] to mention. Code is fully commoditized.
[05:24] Anyone can generate code. That is not an
[05:26] advantage anymore. What is an advantage
[05:28] is your specific solution to the problem
[05:30] you're solving. And that boils down all
[05:32] the way to how you write your skills. So
[05:34] you can see here you know the big
[05:35] advantage we get out of this is headless
[05:37] by default. We get parallel sessions and
[05:39] we get persistent profiles. So if you
[05:42] are running some type of login workflow
[05:44] with your playright testing agent you
[05:45] can persist the session which is really
[05:47] important. So that's great. We also have
[05:50] the claw browser scale. There's not much
[05:52] to document here because when you're
[05:54] using claude with the - chrome flag
[05:57] essentially what it does is it injects a
[05:59] bunch of additional tools that allows
[06:01] claude to access the browser. And so the
[06:03] only real checks we need to add into the
[06:04] skill is just to make sure that the flag
[06:06] is turned on. And then we have a couple,
[06:08] you know, opinionated pieces here.
[06:09] Resize the browser and then you execute
[06:11] the user request and return. So very
[06:13] simple. The skill isn't ultra necessary,
[06:15] but I wanted to build it to showcase how
[06:17] we can stack up this skill into
[06:20] different workflows. So that's great. We
[06:21] have our two skills, right? The skill is
[06:23] the capability. This is the foundational
[06:26] layer. The next piece of this layered
[06:27] approach is going to be our
[06:32] agents. So you can see here we have
[06:33] three agents. Let's start with a simple
[06:35] one. Let's start with our playright
[06:36] browser agent. Now check out how I'm
[06:38] prompt engineering this. This is a very
[06:40] simple sub agent that we can spin up to
[06:42] do arbitrary browser work with the
[06:44] playright CLI. So we've activated the
[06:46] skill in the front matter and then we're
[06:48] mentioning it just one more time inside
[06:50] of the actual workflow. So you can see
[06:52] here this agent is very simple. All
[06:54] we're doing is scaling this skill into a
[06:56] sub agent. We can prompt over and over
[06:58] for UI testing tasks and really just for
[07:01] any browser automation task. This
[07:03] doesn't have to be for UI testing. It
[07:04] just happens to be that it's great for
[07:05] that. Okay. And then we have the claw
[07:07] browser agent. So we can use the cloud
[07:10] code Chrome tools inside of a sub agent.
[07:12] The big problem with this is that it
[07:14] doesn't really belong here. We can check
[07:16] on our workflow right now. If we open up
[07:17] the terminal, you can see that our
[07:19] Amazon workflow is still working,
[07:21] purchasing things for us. Let's go and
[07:22] open up Chrome. You can see it's buying
[07:24] some blue light blockers for me. It's
[07:25] got a couple other things inside the the
[07:28] cart for me here, including, you know,
[07:30] flowers. Valentine's Day right around
[07:31] the corner. Got to pick up those flowers
[07:32] for the GF, right? It's fully automated
[07:34] and it's doing this work on my behalf.
[07:36] The big problem with this using the
[07:38] D-Chrome flag is that you cannot run
[07:40] this in parallel. Okay, so this is one
[07:42] of the big limitations, 14 minutes
[07:44] running AK tokens. It's just going to
[07:46] continue running my browser automation
[07:48] task for me. And let's move to our most
[07:50] important agent, the browser QA agent.
[07:53] And so here's where things get
[07:54] interesting. This is where we're
[07:55] actually building out a concrete
[07:57] workflow. This is where things get more
[07:59] specialized. This is a UI validation
[08:01] agent that's going to work through user
[08:03] stories. It's going to do it in a very
[08:04] specific way. This is where we start
[08:06] templating or engineering into a system
[08:09] for repeat success. All right, these
[08:10] agents can do a lot more than we give
[08:12] them credit for. It's time to start
[08:14] pushing them hard into specific
[08:16] workflows to automate classes of work.
[08:18] So let's understand how this agent
[08:20] allows us to do that exactly. We have a
[08:22] classic agent workflow here. Classic
[08:24] agentic prompt purpose variables
[08:25] workflow report examples. If you've been
[08:27] with the channel, you understand this
[08:29] structure very well. Let's jump into the
[08:30] workflow. Right? This is where the work
[08:32] actually happens. So this agent is going
[08:34] to parse a user story into specific
[08:36] steps, create a directory for it, work
[08:38] through the workflow, take screenshots,
[08:40] report pass or fail, and then actually
[08:43] close the browser. And so here we have
[08:44] an opinionated workflow with a few
[08:46] variables where our agent is going to be
[08:48] recording its journey along the way and
[08:51] saving screenshots. Very very powerful.
[08:52] You can see we have a output format.
[08:54] This is very important. We are
[08:56] specifically telling how our agent to
[08:58] respond and we have examples of some
[09:01] stepbystep workflows that this agent
[09:03] could actually execute. Okay. And so if
[09:05] we wanted to, we could do something like
[09:06] this, right? We can just copy one of
[09:07] these examples. We'll use the
[09:08] example.com, you know, we'll just copy
[09:10] this out. And it's going to turn this
[09:11] into a series of steps. fire up a cloud
[09:13] code instance and then we can just use
[09:15] the agent reference with at browser-qa.
[09:18] There's this agent and then we can just
[09:19] fire this prompt off. So we're giving it
[09:21] that step-by-step workflow and this is
[09:23] going to kick off a headless browser
[09:26] agent to actually validate this workflow
[09:28] to make sure that everything works. All
[09:30] right. And so this is just a random
[09:31] example. Uh example.com doesn't actually
[09:34] have, you know, any input field to enter
[09:36] anything into. So this workflow will
[09:38] likely come back failed, right? Because
[09:39] these steps don't really exist. failed
[09:41] to go to example.com. Reserved domain,
[09:43] paragraph of text, no login. Exactly.
[09:45] So, we got screenshots of the journey
[09:47] saved along the way. Now, this is the
[09:49] important piece that I really want to
[09:51] share with you here, right? We layered
[09:52] an agent on top of a skill and then we
[09:55] built an agent to use that skill, right?
[09:58] We can see that playright browser skill
[09:59] here. And we built a concrete workflow
[10:02] for repeat success. This bowser
[10:03] codebase, it isn't like a standalone
[10:05] codebase is a codebase that I and you
[10:07] can reference to pull a consistent
[10:09] structure of skills, sub aents, prompts,
[10:13] and one additional layer I'll share in a
[10:15] moment here for reusability. And it
[10:17] allows you to take this and apply to any
[10:19] problem, any code base with a consistent
[10:22] structure. Okay? And so the agent is
[10:23] where we start to specialize and scale
[10:26] where the skill is just our raw
[10:28] capability. Okay? And so I think if
[10:30] you're just looking at things from the
[10:31] angle of a skill, you're not using all
[10:34] agentics as well as you could, right?
[10:36] There are many other pieces that you can
[10:38] add to this to really expand what you
[10:40] can do with your agent. All right?
[10:42] Everyone is just spamming skills right
[10:43] now. And that's great. I understand why,
[10:45] but there's layers to how you can build
[10:47] this up for repeat success. Especially,
[10:49] and this is an important thing to
[10:50] mention, especially with these new agent
[10:52] orchestration features coming out of
[10:54] cloud code and other agent coding tools,
[10:57] knowing how to build these specialized
[10:58] agents that you can scale is going to be
[11:00] ultra important. I think sub agents got
[11:03] a massive buff and they're going to be a
[11:05] centerpiece as agent orchestration
[11:08] becomes the primary paradigm of agentic
[11:10] coding. I'll link the previous video
[11:11] where we talk about the powerful new
[11:13] agent orchestration features coming out
[11:15] of cloud code. You can see here the
[11:16] Amazon workflow has completed. It's
[11:18] walked right up to the doorstep of
[11:20] making the purchase. And if we open up
[11:22] the terminal here, you can see here that
[11:24] it, you know, set everything. This
[11:26] workflow took 20 minutes to run, but it
[11:28] did it all without us. All right? And
[11:29] so, you know, you can see this is a this
[11:31] is a risky workflow because it walked
[11:33] right up to the doorstep of the purchase
[11:35] and it has everything we asked for. This
[11:37] is one example. Browser automation has
[11:39] many many uses, many many things you can
[11:41] do from support workflow automation,
[11:43] from gathering documents, from you know
[11:45] different resources. There are many many
[11:47] ways to use browser automation and you
[11:49] can see here my agent emphasizing this
[11:51] stopping here not placing order very
[11:53] important. Uh the adherence of this Opus
[11:56] 4.6 model is really fantastic. It's
[11:58] great with directions and you can see
[11:59] that it you know completed this entire
[12:01] workflow. Definitely took some time
[12:02] though and if it took time that means it
[12:04] took tokens. So that's great. Let's
[12:05] continue to the next layer. Right. So,
[12:07] you can see here we're starting to build
[12:09] opinionated reusable agents on top of
[12:12] our skill. Right? We're not just relying
[12:13] on the skill. Although, if we want to,
[12:16] whenever we want to, we can kick off a
[12:18] brand new terminal, fire up Claude, and
[12:19] we can activate any one of these skills,
[12:21] right? So, if we wanted to, we could do
[12:22] Claude browser, kick the skill off, or
[12:25] playright browser, kick this off. So, we
[12:26] can hop into any layer we want to. This
[12:28] is a huge advantage that makes it easier
[12:30] to test and scale up your agents one
[12:32] step at a time as you add layer by layer
[12:34] by layer of agentics. But uh you can see
[12:36] here we have a couple prompts. So let's
[12:38] go ahead and get into the third layer of
[12:40] this stack which is the actual
[12:43] custom/comands. And I'm calling this the
[12:45] orchestration layer. Now let's break
[12:47] down why.
[12:51] Once you have the skill and once you
[12:53] stack agents on top of your workflow, I
[12:55] think the next thing you're going to
[12:56] want to go for is a command, a
[12:58] custom/comand, also just known as a
[13:00] reusable prompt. You can see we have
[13:02] that UI review prompt that ran. This is
[13:04] where things get a little more
[13:06] interesting, a little more complex. So,
[13:08] UR review fires off parallel story
[13:10] validation. So, you saw how this works
[13:12] at a high level, but you can see here we
[13:13] have stories glob. So, we have a bunch
[13:15] of variables set up here. So, if we open
[13:16] up AI review, you can see we have a
[13:18] single simple user story for hackernews.
[13:21] And if we open this up, you can see this
[13:22] very simple file format that is
[13:24] effectively a user story for your
[13:26] application. It has the name, the URL
[13:29] your agent's going to visit, and then
[13:30] the actual workflow. If this isn't
[13:32] clear, the true purpose of these
[13:33] workflows is, you know, you copy all
[13:35] these, you go lochost, you know, blah
[13:37] blah blah slash your page and then your
[13:40] agent validates against that specific
[13:42] page. Obviously, this is a very agent
[13:44] first approach to testing. But, you
[13:45] know, another great part here is that
[13:46] you can do things like this, you know,
[13:48] uh, your staging com/you
[13:51] page and then you can test against that
[13:53] as well. And if you wanted to, you can
[13:55] even modify this workflow so that, you
[13:57] know, you have multiple pages that
[13:59] you're going to test. Again, I want to
[14:00] emphasize this. This isn't just a random
[14:02] skill, right? I think of skills as
[14:04] low-level capabilities that you give
[14:06] your agent. After you have that, it's up
[14:08] to you to compose it into something
[14:09] useful and valuable in a repeat scalable
[14:12] way. And a great way to do that is by
[14:14] building out sub agents so that you can
[14:16] scale and then commands which gives you
[14:18] that real power, that real control. All
[14:21] right? And so more and more I'm thinking
[14:23] about commands, you know, prompts as the
[14:25] orchestration layer. So you can see this
[14:26] is a user story we built out and of
[14:28] course you can have an agent as you're
[14:30] building your application. You can have
[14:32] them very very quickly spin up new
[14:33] stories to test that workflow. All
[14:35] right, if you want to you can take this
[14:37] and add that next piece. This is what I
[14:39] do when I deploy this browser system
[14:41] into my applications. I'll take this
[14:43] workflow and actually add additional
[14:45] agents to it. So let me explain that
[14:46] part in UI review. This is our
[14:48] orchestration prompt. And of course it
[14:50] looks just like all of our other
[14:52] prompts. Very consistent prompt
[14:53] structure. You add the sections when you
[14:55] need them. When you don't, you remove
[14:56] them. Here we have a lot of them, right?
[14:57] Purpose, variables, code structure,
[14:59] instructions, workflow, report. What
[15:01] this does is it's going to create an
[15:02] agent team. We are leveraging the new
[15:04] orchestration feature coming out of
[15:06] cloud code, coming out of a lot of
[15:08] powerful agentic coding tools. Now,
[15:09] right, you can create teams of agents
[15:11] that work toward a common goal. In this
[15:13] case, we're creating a team that does UI
[15:15] review. All right, so you can see here
[15:16] in the instructions kind of breaking
[15:18] down how we'll do this, but the most
[15:19] important piece is the workflow. All
[15:21] right. So, we're going to discover all
[15:23] the UIs and set up the output directory.
[15:25] We're then going to spawn our agents,
[15:27] right? This is a team of agents and
[15:29] we're actually breaking down how to
[15:31] prompt each agent, right? So, for each
[15:33] task call, use this prompt. So, we are
[15:36] metaprompt engineering in a different
[15:38] type of way here. We're teaching our
[15:39] primary agent or the orchestrator agent
[15:42] how to prompt the sub aents. All right,
[15:43] we're being very explicit here. So, you
[15:45] can be very, very detailed with the
[15:47] results you're getting out of your sub
[15:48] agents. And then we have collect. After
[15:49] every teammate finishes, they're going
[15:51] to ping back via the task list as we've
[15:54] covered in previous videos. And then
[15:55] they're going to clean up and report.
[15:57] So, we're actually using this powerful
[15:58] UI review prompt, right? UI review as a
[16:01] consistent way to test our UI over and
[16:03] over and all we have to do is just
[16:05] activate this prompt and our entire UI
[16:07] gets tested by agents. And so, you know,
[16:09] you might be thinking, why would you use
[16:11] agents instead of a consistent, you
[16:13] know, UI testing framework? There are
[16:16] many reasons for that. I think the
[16:17] biggest one is that at a drop of a dime,
[16:19] if we open up our user stories, we can
[16:21] have our agent quickly build arbitrary
[16:24] workflows and you know very very easily
[16:28] and seamlessly. It's just you know walk
[16:29] through step by step exactly what
[16:31] happens and our agents will just
[16:33] validate against a URL. Right? To me
[16:36] this is the big advantage of a gentic UI
[16:38] testing. They just operate on the thing
[16:40] like a user would. Okay. No sea of
[16:42] testing configuration for your gest,
[16:44] your vi test, your, you know, whatever
[16:46] tests you're setting up. They're acting
[16:48] like a user would. You know, I
[16:49] understand that we're always playing
[16:50] this game of balance between are we
[16:53] going to build a a gentic
[16:54] non-deterministic solution? Are we going
[16:56] to build a very deterministic code
[16:59] solution for things like this, right?
[17:01] And I think more and more the answer is,
[17:02] you know, all the top I think all the
[17:04] best agentic engineers, they're going to
[17:06] be doing some combination of both, but
[17:07] they're also going to be leaning a
[17:09] little extra agentic. All right. And so
[17:11] this is one manifestation of that. We're
[17:13] setting up user stories that had a
[17:14] specific URL that we spread across
[17:17] multiple agents to run it in parallel.
[17:19] And now at any point in time, and we can
[17:21] just kick this off again, right? There's
[17:22] no cost here to us. And actually, I'll
[17:23] kick this off in headed mode so we can
[17:25] all see this. any point in time we can
[17:27] then just run the workflow to test our
[17:30] new application or to test whatever
[17:32] thing that you're working on right and
[17:33] so you know in the world of trusting and
[17:36] deploying agents I think this is going
[17:38] to be more and more valuable because we
[17:39] can just quickly add user stories and
[17:41] have our agents run through them very
[17:43] quickly you can see once again they're
[17:44] spinning up their own headed browser
[17:46] using the playright CLI they're working
[17:47] very very quickly you know they're
[17:49] operating with pretty great token
[17:50] efficiency because we're using the CLI
[17:52] instead of the MCP server so there's
[17:54] great token efficiency we can See all of
[17:56] our agents have completed almost here
[17:58] when they're all going to close their
[18:00] page. There we go. Done. And then
[18:01] they're going to merge their results
[18:03] back here. There it is. UI summary
[18:05] complete. This is us moving all the way
[18:07] up to that prompt level. And so the
[18:09] prompt control the sub aents. The sub
[18:11] aents use the skills. Okay. So very
[18:13] powerful. Let me show you the Amazon
[18:15] workflow. So if you're doing browser
[18:16] automation work, Amazon add to cart. We
[18:19] have a very very simple workflow. I
[18:21] think for browser automation, you know,
[18:22] the automations themselves are best
[18:25] written as an actual reusable custom
[18:28] slash command for testing purposes, but
[18:30] also so that we can scale them like
[18:32] this. So, some engineers on the channel,
[18:34] you may have come across patterns like
[18:35] this where you have something I call a
[18:37] hop or a higher order prompt. Okay, so
[18:39] this is an interesting type of prompt.
[18:41] Think of this like a function that takes
[18:43] a function as a parameter. All right,
[18:45] this is exactly what this does. So you
[18:46] can see here argument one. This actually
[18:48] takes a another prompt as a parameter.
[18:51] Why do we do this? We do this because we
[18:53] want to wrap that prompt that runs in a
[18:55] very consistent workflow. Okay. And so
[18:57] here's the workflow. This is the
[18:59] automate browser workflow. We're going
[19:00] to save browser automation workflow
[19:02] inside of this directory. So I can just
[19:04] store a bunch of automations here and
[19:06] then I can change the workflow that
[19:08] actually runs. Okay. So the consistent
[19:10] pieces go in the higher order prompt and
[19:11] then the details, right? the steps that
[19:13] you want to run go in the lower order
[19:15] prompt or just the prompt that you want
[19:17] to execute. As you can see here, very
[19:18] simple, we have a, you know, Amazon add
[19:20] to cart. That's what we ran before. And
[19:22] so at any point in time, we can run, you
[19:23] know, Amazon add to cart like this or we
[19:26] can run, you know, our proper higher
[19:28] order prompt to automate and then pass
[19:29] in the workflow, right? So we would do
[19:31] something like this and then we would
[19:32] execute it like this. And so this will
[19:34] kick off that purchase workflow. And the
[19:36] idea is, you know, relatively simple but
[19:38] very powerful. I can now run these
[19:40] automations, right? We're going to
[19:41] parse. We're going to load the workflow.
[19:43] And then we're going to execute the
[19:44] workflow. But we can save repeat
[19:46] instructions for every piece of this
[19:48] workflow that runs. Okay. So that's what
[19:50] this hop automate does. And this is us
[19:52] automating browser task in a repeat way.
[19:56] Okay. We're not just relying on skills.
[19:57] We're scaling it up into sub agents into
[20:00] reusable orchestration prompts. And then
[20:02] we have one more layer I want to show
[20:03] you here. This is a tool that I'm using
[20:05] on the channel and for all my private
[20:07] engineering work as well. After you have
[20:09] all these different ways to execute with
[20:11] your agent, you're going to want a
[20:12] repeat single place to call all these
[20:15] tools. And that's what you saw here in
[20:17] the beginning. If we close out this
[20:19] agent in the root of that directory, if
[20:21] we type J or if we type which J. So you
[20:23] can see my actual command, you can see
[20:25] that I have J alias to just is a
[20:28] powerful and simple command runner.
[20:30] Let's break this tool down.
[20:35] So just is the cherry on top for a lot
[20:38] of the workflows that I like to run.
[20:39] Open up this file here, just file.
[20:42] You'll see all the commands we just ran,
[20:44] all the permutations of how we want to
[20:46] execute and kick off our cloud agent.
[20:48] And you'll see all the workflows with
[20:50] variables we can pass in to overwrite
[20:53] them. This allows you and your team and
[20:55] other agents to build repeat solutions
[20:57] and then to quickly access them. Okay,
[20:59] so this is my reusability layer at the
[21:02] very very top. So we have skills
[21:04] capability at the bottom. We have sub
[21:06] agents to scale. You can give each one
[21:08] of your sub agents a different skill or
[21:09] the same skill. And then you want
[21:10] commands to orchestrate. And then right
[21:12] at the top I use just or just files for
[21:15] reusability. And I'll go ahead and add
[21:17] my just file. If we type just here, you
[21:19] can see I have a skill of course built
[21:22] up to quickly configure, set up, and
[21:23] adjust your just files. So I'll add this
[21:25] to this codebase for you here as well.
[21:27] And the idea is simple. We want to be
[21:29] able to customize and specialize our
[21:31] agents inside of our code bases. Great.
[21:33] So, how do we do that? After you have
[21:35] all of your agentics built in, how can
[21:37] you quickly call these in a reusable
[21:39] way, right? So that you, your team, and
[21:41] your agents know what is even available.
[21:43] So, I like to use just file as a
[21:44] reusability layer. And it is just a task
[21:47] runner. If we type just, you can see all
[21:49] the commands available. At any point in
[21:51] time, we can kick off one of our agents.
[21:52] Let's just kick off a couple agents here
[21:54] so I can show you exactly what this
[21:55] looks like. So if we have our let's find
[21:57] our Chrome browser agent here and let's
[22:00] just use the top level just paste this
[22:02] workflow here test Chrome skill we can
[22:04] then overwrite this default parameter
[22:06] and the default parameter here is
[22:08] default prompt get current date go to
[22:10] Simon Wilson find his latest blog
[22:12] summarize it give it a rating out of 10
[22:14] okay so we can just kick this default
[22:15] off that's fine and you can see we're
[22:17] opening up a cloud code instance to do
[22:19] that work exactly you can imagine this
[22:21] as anything right we could be you know
[22:22] looking for updates from our favorite
[22:24] blogs we want to collect them into some
[22:25] resource. We want to do some actual data
[22:27] entry. We want to run support. We want
[22:30] to do some information gathering. You
[22:31] can have your agents do that. And
[22:33] clauding chrome is a way to do it. You
[22:34] can also set up something like playright
[22:36] CLI to quickly, you know, build your own
[22:38] customizable skill that does things in a
[22:40] specific way on your behalf. But I like
[22:42] to use the just file here as that final
[22:45] layer of reusability on top of all of
[22:47] it. In the beginning of the video, we
[22:49] ran this just this workflow. At any
[22:52] point in time, we can come in automate
[22:53] Amazon or we can come to the workflow
[22:56] and we can build a brand new browser
[22:58] workflow and then we can pass this end
[22:59] to the automation workflow. That's the
[23:01] idea here. And notice here that I'm
[23:03] solving the class of problem. Okay? And
[23:06] that's the meta theme of what I wanted
[23:07] to share with you today. There are
[23:09] entire classes of problems that you
[23:11] don't need to solve anymore if you teach
[23:14] your agents to solve that problem. And
[23:15] so in this browser codebase, I have a
[23:18] templated repeat solution for solving
[23:21] browser automation and solving UI
[23:23] testing. Now, you know, there's tons of
[23:25] things in here we want to tweak, change,
[23:27] make our own, make fit the mold of your
[23:30] codebase. But the way I'm thinking about
[23:32] solving problems now in the age of
[23:33] agents is template engineering into a
[23:36] repeat opinionated solution that you can
[23:39] deploy over and over again and
[23:41] specialize. Right? This is just a mold.
[23:43] Bowser is just a mold with a great
[23:45] four-layer architecture where you have a
[23:47] capability which are your skills that
[23:49] you then roll into your agents which
[23:51] gives you scale right you can add them
[23:53] into teams you can parallelize these and
[23:55] then you have commands at the top which
[23:57] are effectively the API layer for
[23:59] running all of these in a more
[24:01] opinionated more specialized way right
[24:03] this is the orchestration piece then at
[24:05] the top of it all you can create what
[24:07] are effectively functions for your
[24:09] commands that you can run over and over
[24:11] and over this is my four-layer approach
[24:13] for browser automation and UI testing. I
[24:17] highly recommend you build something
[24:18] like this out for your own work. You can
[24:20] see here we finished looking at Simon's
[24:23] blog. Shout out Simon Willis. Always
[24:25] sharing top tier ideas for engineers.
[24:27] And you know, you can see here just a
[24:29] nice simple breakdown, right? But that
[24:30] was all done with browser automation.
[24:31] You can imagine we hit, you know, five
[24:33] or 10 top blogs to gather information
[24:35] from engineers giving us the greatest
[24:37] signal. And that's the big theme. You
[24:38] know, once again, we're striking on
[24:40] that. You want to be handing off more
[24:41] and more work to your agents. You want
[24:43] to be solving classes of problems in a
[24:46] repeat way. Every time you go to tackle
[24:48] that specific problem, you are doing
[24:50] less and your agents are doing more.
[24:52] You're scaling your compute to scale
[24:54] your impact. That's a big theme we talk
[24:55] about on the channel all the time.
[24:58] There's one more idea that I want to
[25:00] discuss with you here. You know, you
[25:01] might be thinking, Dan, why are you
[25:03] breaking things down so much like this?
[25:05] Skills, commands, agents. Why aren't you
[25:07] just throwing agents at the problem? Let
[25:09] them take care of how all of this looks.
[25:11] Just automate everything, right?
[25:13] Automate this stuff away. Don't
[25:14] outsource learning how to build with the
[25:17] most important technology of our
[25:18] lifetime, agents. Okay? If you're
[25:21] outsourcing your skills, I know a lot of
[25:23] people are using plugins now, your
[25:25] agents, your prompts. How will you
[25:27] improve? How will you build unique
[25:29] systems? How will you even know how to
[25:31] build powerful agentic layers around
[25:34] your codebase? All right. And the answer
[25:35] is you won't. You won't be able to.
[25:37] You'll be limited by what everyone else
[25:39] can do because you'll be dependent on
[25:41] what everyone else is doing. You'll
[25:42] always be using plugins. You'll be using
[25:44] someone else's prompts. And you know
[25:46] that in itself is super dangerous. We
[25:48] don't cover security a lot, but prompt
[25:50] injections are one of the most dangerous
[25:54] security vulnerabilities to exist for
[25:56] engineers because you can write and
[25:57] command anything. More on that later. I
[25:59] really want to emphasize this idea here.
[26:02] you know, if you can't look at a
[26:03] library, pull it into a skill, build it
[26:05] on your own, scale it with some sub
[26:07] agents, and then orchestrate it with a
[26:09] prompt, right? If if you can't really
[26:11] build it up, stack up these layers, you
[26:13] will constantly be limited. And this is
[26:15] one of the big differences once again
[26:17] between vibe coders and agentic
[26:19] engineers. Agentic engineers know what
[26:21] their agents are doing, and they know it
[26:23] so well, they don't have to look. Vibe
[26:25] coders don't know, and they don't look.
[26:28] If you master the agent, you will master
[26:30] knowledge work. Don't outsource
[26:32] learning. Check out the link in the
[26:34] description. Pull some ideas from this
[26:36] codebase. The organization here of the
[26:38] four layer architecture is the most
[26:40] important piece here. Take this, make it
[26:42] your own, roll it into your own skills,
[26:44] right? Create your own sub agents.
[26:46] Specialize your repeat solutions with
[26:48] your AI review directory or your AI docs
[26:51] directory with your commands, right?
[26:53] Make it your own. Specialization matters
[26:56] more than ever. Specialization combined
[26:58] with scale and agent orchestration is
[27:02] where the big nugget of gold is right
[27:04] now in the age of agents. Link in the
[27:08] description for this codebase. You know
[27:09] where to find me every single Monday.
[27:11] Stay focused and keep building.
