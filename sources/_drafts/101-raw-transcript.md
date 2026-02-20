[00:00] Right now I have five agents working in
[00:02] a swarm on my codebase. They are working
[00:05] in isolated work trees sending mail
[00:07] between one another. There's a
[00:09] communication layer that is happening.
[00:11] They are all working on uh issues that
[00:13] are tracked. We can see, you know,
[00:15] another piece of mail just got sent over
[00:17] here. We can inspect an agent down here,
[00:19] watch what it's up to, as well as talk
[00:22] with the coordinator agent, which is in
[00:23] charge of the whole workflow. Today, I'm
[00:25] going to talk about what it feels like
[00:27] to develop this way. uh why I am using
[00:31] this system more and more as well as
[00:33] point you towards how you can use this
[00:35] system that I have built. If you don't
[00:37] know me, my name is Jamon West. I'm an
[00:39] agentic engineer. I obsess over AI
[00:42] agents and AI agent coding. Um I am
[00:46] about as AI native as engineers can be.
[00:48] What I am working on and talking about
[00:51] today is Overstory. Um, and I want to
[00:55] say that the the concepts I'm going to
[00:57] be discussing right now. Um, these are
[00:59] true for any sort of agentic swarm
[01:01] system. Overstory is just the project
[01:03] that I've built because I want to
[01:05] understand how a swarm actually operates
[01:08] and have full customization over my
[01:10] swarm. So, uh, this repo is pretty
[01:13] crazy. Uh, in the past I started it on
[01:15] Friday and we have, you know, 235
[01:18] commits already. It's going lightning
[01:20] quick. Um, so today I'm going to turn
[01:22] Overtory on itself and dog food it. Um,
[01:26] sort of build this self-improving
[01:27] system. So before I jump any further
[01:29] into this, I want to put a huge
[01:31] disclaimer here. Agent swarms are brand
[01:33] new. Uh, they require a ton of trust in
[01:35] agentic systems. If you are not very
[01:39] excited about where AI development is
[01:41] going, um, where AI coding tools can
[01:44] take you, this might be a lot of
[01:46] information to take in. So, just putting
[01:48] a disclaimer here that this is crazy and
[01:51] this does not look like traditional
[01:53] development in any sort of way. Um, this
[01:55] doesn't even look like using cloud code.
[01:57] So, here I am in the Overstory repo. Um,
[02:01] I've had people ask me, you know, what
[02:03] does it actually look like to run the
[02:05] Overstory system? What does it look like
[02:07] to run an agent swarm? So hopefully I
[02:09] can showcase a little bit about a proper
[02:12] workflow that I go through when I'm
[02:13] developing a system like this as well as
[02:15] any other project where I'm using
[02:16] Overstory. So Overstory has a
[02:19] coordinator system. You can think of
[02:20] this as like the uh orchestration agent.
[02:22] Um and I can just run overstory
[02:24] coordinator start and this will boot up
[02:26] the coordinator agent. So this agent is
[02:28] in charge of the entire orchestration of
[02:32] my swarm of my agent swarm. So in
[02:35] another terminal I can run overstory
[02:37] dashboard and this will show me all the
[02:39] agents that I have running right now.
[02:40] You know these are previous merges that
[02:42] previous workflows have gone through. Um
[02:44] you can see this agent is asking me what
[02:46] to work on next. Um I have a list of
[02:49] beads issues that I want to have this
[02:52] coordination agent work on. So I'm going
[02:55] to copy those in real quick and I'll be
[02:56] right back. Okay. So I've just sent the
[02:58] coordinator agent a list of issues.
[03:01] These are tracked via beads. If you're
[03:03] not familiar with feeds, I'd recommend
[03:05] going and check that out. Um, but this
[03:07] is just a selection of issues that the
[03:09] agent is going to go work through, get
[03:10] context on, and then we'll see the
[03:12] delegation process begin. As my
[03:14] coordinator is gathering context here, I
[03:17] want to say that that is likely the only
[03:19] prompt that I'll have to send the
[03:21] coordinator agent for all, you know,
[03:24] seven or eight of those issues to be
[03:26] completely fixed end to end, which is a
[03:29] wild thing to say. Um, but that is sort
[03:31] of the truth of agentic swarms, right?
[03:33] We are very much abstracting our role as
[03:37] the human in the loop to a point of
[03:38] where I am now out of the loop. I I sent
[03:41] my single prompt of what I want the
[03:43] swarm to work on. And now the swarm is
[03:45] going to get started working on that
[03:47] selection of problems. My coordinator
[03:50] agent has just gathered all the context
[03:51] it needs to begin work on these issues.
[03:54] We can see this coordinator broke it up
[03:56] into three different team leads. So each
[03:58] of these team leads will spawn their own
[04:00] series of sub aents and begin work on
[04:03] these various issues. So over in the
[04:06] dashboard, we can watch each of these
[04:08] different agents get spawned. Um and if
[04:11] we want to go ahead and inspect what
[04:13] these agents are up to, we can run
[04:16] overstory inspect and then just the
[04:19] agent name. So say I want to inspect
[04:21] this infra lead. This will give me a
[04:23] snapshot of what the cloud code instance
[04:25] that is working on the infrastructure
[04:27] lead team wi is up to. So in addition to
[04:31] being able to inspect a specific agent
[04:34] state, we can run overstory watch and
[04:36] this will showcase what exactly every
[04:39] agent is doing. You know do health
[04:41] checks on each of them um as well as
[04:44] send nudges between agents. So, for
[04:46] example, if the orchestrator or the, you
[04:50] know, coordinator agent here, um, sorry
[04:52] about the terminology with orchestrator
[04:54] and coordinator, um, if that runs into a
[04:57] problem, it can send an urgent nudge to
[04:59] one of the lead agents, which will
[05:01] provide that agent with instructions on
[05:03] what to do instead of what it is
[05:05] currently doing. Here, one of my lead
[05:07] agents has just spawned the first
[05:09] builder agent. So this agent is the one
[05:12] responsible for making actual changes to
[05:14] the codebase. Lead agents and
[05:16] coordination agents aren't able to
[05:18] directly edit files. Um so they delegate
[05:23] by design to agents that are
[05:25] hyperfocused on that specific problem.
[05:27] So now over in the coordinator window,
[05:29] I've just prompted the coordinator to
[05:31] continuously be checking on the leads.
[05:34] This is again something that I'm working
[05:36] on in the system. um sending nudges
[05:39] between one another. But right now, I
[05:41] want the coordinator to be up to date
[05:45] with what is happening in case one of
[05:47] these agents, you know, goes rogue, does
[05:49] something that isn't supposed to happen.
[05:51] We just had a seventh agent boot up. So
[05:54] now we're working with three different
[05:56] leads, three different builders. And as
[05:58] projects get larger and as um specs get
[06:01] larger and as issues get larger, um I've
[06:04] seen this system easily scale up to 30
[06:07] agents at a time. Um and also run for
[06:11] over 2 hours autonomously. Um especially
[06:14] in the case of like building a brand new
[06:16] complicated project, I just pass in the
[06:19] spec file and the coordinator takes care
[06:21] of the rest. So, it's a very hands-off
[06:23] process um that requires a ton of trust
[06:26] with agents. We just had the first agent
[06:28] complete its work. So, this builder um
[06:31] looks like it was there just to build
[06:33] out some markdown specs or alter some
[06:36] markdown specs, but this agent just
[06:38] wrapped up. So, we will be able to see
[06:41] um a merge request come through here
[06:43] eventually after the um review agent
[06:47] here reviews the code. So, this is very
[06:50] important. This is a review agent
[06:52] spawned by one of these team leads to
[06:54] review the work of a builder. We're
[06:56] getting some interesting behavior over
[06:58] here from the coordinator. This swarm,
[07:01] like I said, was built with the
[07:03] intention of um fanning out the agent
[07:06] roles a bit more so we don't just have
[07:08] leads and builders. So now that a
[07:10] reviewer is actually being run, the
[07:13] coordinator recognizes that this is a um
[07:16] new mandatory review loop which was just
[07:18] added in this uh this run. So uh we have
[07:21] another agent booting up. So now we're
[07:23] up to nine different agents in this
[07:25] swarm um and it's been running for about
[07:27] 11 minutes. Another piece of interesting
[07:29] behavior that just came about is this uh
[07:32] infra lead agent just created a new
[07:35] beads issue. So it ran into something
[07:37] that needed to be fixed. um filed a bug
[07:40] for it and then immediately um slung or
[07:43] delegated that task to a new agent. So
[07:46] now we're up to 11 agents in this swarm.
[07:48] So our agent swarm is progressing quite
[07:50] nicely. This lead agent finished up. So
[07:53] now we'll see the coordinator pick up
[07:54] that this agent was done and it's likely
[07:58] going to set up a merge um which is
[08:02] handled through Overstory. If we look in
[08:05] the overstory directory, what happens is
[08:08] we have different work trees for each
[08:10] active agent. So this lead agent
[08:13] finished up and now we're going to see
[08:15] this
[08:17] coordinator agent is you know recognized
[08:19] that this agent is done and it's merge
[08:21] ready. Now we have a merge pending in
[08:23] the merge queue and
[08:26] you know the agent saw that this was a
[08:28] clean merge and went ahead and just
[08:30] cleaned that up. So now all of the
[08:32] changes made by this lead agent as well
[08:34] as any other builder agents that had
[08:37] spawned are in the um the root
[08:40] directory. So this is the main branch
[08:42] now. So we've just merged it locally
[08:44] with the main branch. Um I started this
[08:46] project with no local commits. Now if I
[08:48] run get status, you can see we're ahead
[08:50] by one commit here. I have again sent
[08:54] one prompt I mean two prompts um one
[08:56] real substantive prompt that was just a
[08:59] list of issues and so far everything has
[09:01] been done perfectly. Things are coming
[09:03] along quite nicely. Basically every
[09:05] agent has been completed or killed off
[09:07] here. So this is a zombie agent now. Uh
[09:10] we have merges going through actively.
[09:12] So everything is being merged back to
[09:14] main. The coordinator has completed um
[09:18] delegating several of the issues that we
[09:20] started. So here's a little status
[09:22] update. We have several issues that have
[09:24] been either merged or closed. Now we
[09:27] have several that are in progress and
[09:29] this coordinator is now delegating these
[09:33] remaining open issues to the new lead
[09:37] agents. So now we have lead agents
[09:39] booting back up. Um this looks like a
[09:42] second observability lead which is
[09:44] totally fine. So this is booting back
[09:46] up. Our coordinator agent once again has
[09:48] noticed several issues ready for
[09:50] merging. So this is a great example of
[09:52] where swarms are highly unpredictable.
[09:55] This is just the nature of having a ton
[09:58] of LLMs running at once. We can see this
[10:00] is the observability lead 2 agent up
[10:03] here. And this agent is attempting to
[10:06] modify files by itself. So Overstory is
[10:10] prepped for this. it uh is denying the
[10:12] edit tool from this lead agent, forcing
[10:15] this lead agent to delegate this fix to
[10:19] a builder agent. So, this might be
[10:21] overkill for some tasks. Um, however, in
[10:24] my experience,
[10:26] I found that
[10:28] forcing delegation like this allows for
[10:31] me to place more trust into my system. I
[10:33] would rather an agent with a fresh
[10:35] context window try and fix a problem
[10:37] than an agent dig itself into a hole
[10:40] trying to fix five problems at once. Our
[10:43] agent swarm here is up to 17 agents. We
[10:46] can see a reviewer was just spawned.
[10:49] Like I said, reviewers weren't being
[10:50] spawned before the fixes made earlier in
[10:54] this agentic swarm session were
[10:56] implemented and merged via the
[10:58] coordinator. So we've watched this
[11:00] codebase evolve and improve itself in
[11:03] real time here which is absolutely
[11:05] insane. Our coordinator agent also
[11:08] realized that the review loop that was
[11:10] implemented in this session is working
[11:12] now. So the re review loop is working as
[11:14] designed which again didn't exist before
[11:18] this specific run of swarm. So the swarm
[11:21] is improving its own code in real time.
[11:24] 17 agents running strong. Last agent,
[11:27] last lead agent. It just finished up.
[11:30] It's running the session close protocol.
[11:32] So, just committing everything, syncing
[11:34] with beads, as well as hopefully
[11:38] recording some mulch learnings here. In
[11:41] the next 10 seconds here, we'll see the
[11:43] coordinator agent pick up on all these
[11:45] changes. Yep, we're doing mulch. And
[11:48] begin to do a massive merge here. Okay,
[11:50] once again, so we have 22 agents in this
[11:53] swarm. It's just finishing up. Our
[11:57] overstory coordinator is last merge
[12:00] here. And now we're going to see it
[12:02] clean all of these work trees up. All of
[12:04] these work trees that were just created
[12:06] in the overstory directory. It's running
[12:09] the clean command. We can see all of
[12:11] those were just removed. Our swarm is
[12:14] cleaned up. This ran for an hour, which
[12:17] is pretty crazy. It finished uh I think
[12:20] nine issues that needed to be worked on.
[12:25] We can check get status here
[12:28] and we're ahead by 26 commits. So in
[12:31] that time the agents did 26 different
[12:34] commits. Um the coordinator is now
[12:37] recording all of the insights to mulch
[12:40] which is perfect. Like I said that was
[12:43] 21 different agents a single coordinator
[12:45] that orchestrated all of them. We had
[12:49] 26 different commits. And if I run over
[12:52] story here, we will be able to see some
[12:54] new um like this feed command is brand
[12:57] new. Heirs command is brand new. Looks
[13:00] like we have feed commands here. So
[13:02] that's thing that needs to be fixed, but
[13:04] nothing major. This was all of the
[13:07] agents that we just ran. Uh the
[13:09] coordinator has reported back and all of
[13:12] those issues that I sent over uh at the
[13:15] very beginning with again this was one
[13:17] single prompt uh with one other prompt.
[13:20] So, two prompts, one just reminding me
[13:22] or reminding the coordinator how to uh
[13:24] run the sleep command and stuff. But
[13:26] again, one prompt just ran for an hour.
[13:30] Nine different issues got fixed. 26
[13:32] commits, 20 plus agents, 20 different
[13:36] work trees. Absolutely amazing stuff.
[13:39] So, please go check out Overstory if you
[13:42] like this. If you're interested in
[13:44] agentic swarms, this stuff is moving so
[13:47] crazy fast. So, I'd recommend you get
[13:49] dialed in sooner rather than later
[13:51] because I'm sure by the time I release
[13:53] my video on Friday. Overstory will be
[13:57] leagues ahead of where it is now. So,
[13:58] before I close out this video, thank you
[14:01] so much for watching. If you're
[14:02] interested in hearing more from me,
[14:04] seeing some live streams where I'm doing
[14:06] live developer sessions, um please check
[14:08] out Promprad. It'll be linked down
[14:10] below. That's my school community. It's
[14:12] completely free right now. So, go check
[14:14] it out. Um, and if you're interested in
[14:16] working with me, I do consulting work,
[14:18] so please go check out
[14:19] consulting.jimmanwest.com.
[14:21] That'll be linked down below. Again,
[14:23] thank you so much for watching. Go check
[14:25] out Overstory, and I will see you again
[14:27] on Friday if I don't make a video before
[14:29] then.
