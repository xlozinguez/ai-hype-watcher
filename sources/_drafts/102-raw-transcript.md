[00:00] Well, sitting on my desk is a new Mac
[00:02] Mini that I set up just for the purpose
[00:04] of running my team of AI agents using
[00:06] OpenClaw. I've got a developer, a
[00:09] marketer, a project manager, a system
[00:11] admin. They each have their own
[00:12] personality. They've got a queue of
[00:14] tasks tracked in this custom dashboard
[00:16] that I built and I'm chatting with them
[00:18] in Slack just like I would with my real
[00:20] team members except they're agents
[00:22] powered by OpenClaw and various large
[00:25] language models. What a time this is.
[00:28] But, you know, getting this up and
[00:29] running was not a plug-and-play
[00:31] situation. Over the past week and many
[00:33] late nights, I had to figure out my
[00:35] answers to question after question, some
[00:38] technical, some strategic, like, should
[00:40] I order a new Mac Mini or can I run
[00:42] OpenClaw on a VPS? And what's this going
[00:44] to cost me in API tokens? And could I
[00:47] use my Claw Max plan? And what chat tool
[00:50] is best for my agents, Telegram or
[00:52] WhatsApp or Slack? Should I have it
[00:54] power one agent or can I set up a team
[00:56] of agents? and am I going to need a
[00:58] custom dashboard for managing them? And
[01:01] let's not forget about security. What
[01:02] should my agents be able to access? And
[01:04] how should I think about safeguards? And
[01:06] most importantly, what's my use case
[01:08] here? What will I have my team of agents
[01:10] actually do for me? So today, I'll share
[01:13] where I've landed on all of those
[01:14] questions, and I'll show you my setup
[01:16] for all of it. You know, to be honest, I
[01:18] didn't see the appeal of OpenClaw at
[01:20] first. Back when it was called Claudebot
[01:22] and then Moltbot and it was buzzing
[01:23] around Twitter a couple weeks ago,
[01:25] everyone was talking about having their
[01:27] agent respond to their emails for them
[01:28] or book flights or order takeout. And I
[01:32] don't want or need an AI agent in my
[01:34] personal life and I don't even want it
[01:36] to manage my calendar. But then I
[01:38] started thinking about a real challenge
[01:39] that I've been having in my business and
[01:41] how setting up OpenClaw could help me
[01:43] solve it. You know, I run this YouTube
[01:45] channel and Builder Methods Pro on my
[01:47] courses and a weekly newsletter. And
[01:49] thanks to things like Claude Code, of
[01:51] course, building things has never been
[01:52] easier. But building it is only half of
[01:54] what I do. I develop training content. I
[01:57] manage a publishing pipeline. And I
[01:59] oversee my membership business. But
[02:01] lately, I've been bottlenecked. There's
[02:03] so much more that I want to create and
[02:05] deliver. If only I had the bandwidth. In
[02:07] my past businesses, I solved this by
[02:09] hiring real teams and building processes
[02:11] to help us scale. And that worked, but
[02:14] the overhead was real, too. So, when I
[02:16] gave OpenClaw another look, I asked a
[02:18] different question. Not do I want a
[02:20] personal assistant, but what if this
[02:22] could fill roles on my team? And now,
[02:25] I'm convinced that this paradigm,
[02:27] autonomous agents with defined roles
[02:29] running on their own machines, I think
[02:31] this is here to stay. Now, OpenCloud is
[02:34] just the first generation of what I
[02:35] think will be much bigger. So, I want to
[02:37] be figuring this out now, and maybe this
[02:39] video can help you get started, too. If
[02:41] you're new here, I'm Brian Castle. I
[02:43] help builders stay ahead of the curve
[02:44] with AI. And every Friday, I send my
[02:47] builder briefing. That's a free
[02:49] fiveminute read where I give you my no
[02:50] hype take on making this transition to
[02:53] adopting AI. You can get yours by going
[02:55] to buildermethods.com.
[02:57] And if you're serious about leveling up,
[02:59] check out builder methods pro where you
[03:00] can join our community and get training
[03:02] for builders. All right, so what
[03:04] actually is OpenClaw? It used to be
[03:05] called Cloudbot and then Moltbot. And
[03:08] how is this actually different from how
[03:09] you might use cloud code or any other
[03:11] agent? The core of OpenClaw is what's
[03:13] called the gateway. That's a process
[03:15] running on a machine, which shouldn't be
[03:17] your personal machine, but we'll talk
[03:19] about security in a moment. The
[03:20] OpenCloud gateway can run tools. It
[03:22] could use a browser. It can execute bash
[03:24] scripts. Of course, cloud code can do a
[03:27] lot of that, too. But what makes
[03:28] OpenCloud different is that it's always
[03:31] on. It maintains a persistent workspace
[03:33] with memory and session logs. So you can
[03:36] chat with your agents through Telegram
[03:38] or Slack and delegate tasks that they
[03:41] can do on their own in the background.
[03:43] So that's a fundamentally different
[03:44] paradigm from you personally managing
[03:47] cloud code sessions in your terminal.
[03:49] OpenClaw is closer to having teammates
[03:51] who do their work on their own
[03:53] workstations. The first question is
[03:55] where should this thing run? Now I don't
[03:57] recommend you run OpenClaw on your daily
[03:59] driver machine. You don't want to give
[04:01] it unfettered access to your files and
[04:03] your accounts. And even if you isolate
[04:05] it with something like Docker, your
[04:06] machine would need to be on and awake
[04:09] 24/7 for your agents to work. So,
[04:11] OpenClaw needs its own dedicated
[04:13] machine. That could be a cloud VPS
[04:15] starting at around five bucks a month.
[04:17] Or it could be a physical machine.
[04:19] Doesn't have to be a Mac Mini. Any kind
[04:20] of computer on your network. Both are
[04:22] valid and a lot of people are doing well
[04:23] with the VPS setups. But I went ahead
[04:26] and I spent the 600 bucks on a new Mac
[04:27] Mini M4. And call me old school, but I
[04:30] like to be able to screen share into it,
[04:32] see the desktop, install things, and
[04:34] manage it visually. And I SSH in too
[04:37] when I just need to run a quick command.
[04:39] And if I end up using my agent team for
[04:41] all the use cases that I have in mind,
[04:43] I'll need more storage and bandwidth
[04:45] than the cheap VPS tiers offer. So, the
[04:47] cost would start to balance out anyway.
[04:49] And hey, if none of this works out, I'll
[04:51] throw that Mac Mini up in my home music
[04:52] studio. I'll use it up there. So, I've
[04:54] got the dedicated machine. But that's
[04:56] just the first layer. I need to think
[04:57] carefully about what my agents can and
[04:59] can't access. Now, this is where the
[05:01] hiring metaphor really kicked in. If I'm
[05:04] bringing someone onto my team, I
[05:05] wouldn't give them access to my personal
[05:07] laptop or let them loose on a browser
[05:09] where I'm logged into everything. No, an
[05:11] employee would get their own machine,
[05:13] their own email, access to the files and
[05:15] services that they need with the right
[05:17] permissions, nothing more. So, that's
[05:19] what I did. I set up a dedicated email
[05:21] address for my agents. I created a
[05:23] GitHub username that I can invite to
[05:25] specific repos. I can grant and revoke
[05:28] access to services just like I would
[05:29] with any other team member. Now, files
[05:32] were a bit trickier. I want easy two-way
[05:34] syncing between my computer and the
[05:37] OpenClaw workspace on the Mac Mini,
[05:39] especially since I'm developing a a
[05:41] brain system where all my business
[05:43] activity gets logged into Markdown files
[05:46] that my agents can access and work with.
[05:48] More on the brain maybe another time. So
[05:51] all my files live either in GitHub repos
[05:53] or my main Dropbox account, but I don't
[05:56] want to just share my personal Dropbox
[05:58] with OpenClaw. That gives it access to
[06:00] way too much. So I had OpenClaw set up
[06:02] its own Dropbox account. And so the
[06:05] specific folders that I want to share
[06:06] between my main Mac and the OpenClaw Mac
[06:10] Mini, both Dropbox accounts have access
[06:12] to those. And so everything else stays
[06:14] walled off. All right, let's talk about
[06:17] costs because if you're not careful, you
[06:19] can easily run up hundreds or even
[06:21] thousands of dollars in token costs just
[06:23] chatting with your agents and running
[06:25] tasks. I blew past $200 in the first two
[06:28] days of setting up my system. Now, I
[06:30] already pay for a Cloud Max plan and I
[06:32] was hoping that I could just use that,
[06:33] but then I heard the stories of accounts
[06:35] being shut down because this type of
[06:37] usage might be against Anthropic's terms
[06:39] of service. And then within a few days
[06:42] he upgraded to the $200 subscription or
[06:45] euros because he's in Austria. And he
[06:47] was in love with that thing. That for me
[06:49] was like a very early product
[06:50] validation. It's like I built something
[06:52] that
[06:54] captures
[06:55] people. And then a few days later
[06:57] Andropic blocked him because based on
[07:00] their rules using the subscription is
[07:02] problematic or whatever.
[07:03] &gt;&gt; So there's real ambiguity there. And I
[07:05] genuinely wish that there would be some
[07:07] official word one way or the other. Now
[07:09] I intend to play by the rules. So,
[07:10] here's where I landed. My Cloud Max plan
[07:12] stays for my personal use with Claude
[07:14] and Claude code on my devices when I'm
[07:17] working. My OpenClaw agents use API
[07:20] tokens completely separate. I'm running
[07:22] those tokens through Open Router, which
[07:24] centralizes all my API usage and makes
[07:26] it easy to select from hundreds of
[07:28] models and providers. More importantly,
[07:30] it lets me carefully optimize which
[07:32] agents use which models for which tasks.
[07:35] You know, honestly, that optimization is
[07:37] probably where I spent the most time
[07:39] this past week, just figuring out which
[07:41] tasks need the power of Opus and which
[07:44] can run on cheaper, faster models.
[07:46] Still, running this team of agents is
[07:48] not cheap. And if you've been building
[07:49] with the frontier models, then you
[07:51] already know this isn't a free ride. And
[07:53] from a business standpoint, if you
[07:54] compare the token costs to the cost of
[07:57] hiring multiple team members to do the
[07:59] work that can maybe should be delegated
[08:01] to agents, the ROI math gets pretty
[08:04] compelling. Now to the question of
[08:06] chatting with my agents. OpenClaw
[08:08] supports a wide range of chat tools. I
[08:10] started with Telegram since that was the
[08:12] easiest to get up and running. It worked
[08:13] for a few days and I was even able to
[08:15] set up separate Telegram bots for each
[08:17] agent. I'll talk about my multi- aent
[08:19] configuration in just a minute. But
[08:21] after a few days on Telegram, I found
[08:23] the interface just wasn't comfortable,
[08:25] especially when agents would send me
[08:26] markdown formatted content, which kind
[08:28] of works, kind of doesn't. So again, I'm
[08:31] working with my agents like I tend to
[08:33] work with teammates. and my teams have
[08:35] always used Slack. So, I set up Slack
[08:37] bots for each of my agents and that was
[08:39] super easy. And Slack has great markdown
[08:42] support. And I really like how we can
[08:43] use threaded replies and that makes it
[08:46] easy to manage multiple agents with
[08:48] multiple requests and responses flying
[08:50] around. Now, here's what made OpenClaw
[08:52] really click for me. Instead of using it
[08:54] as a single agent, I set up a multi-
[08:57] aent configuration so that I can build
[08:59] an actual team of four agents. Claw is
[09:02] my system admin who I work with when I'm
[09:05] tinkering with my OpenClaw system
[09:06] itself. Bernard is my developer. Vale
[09:09] works on marketing tasks and Gumbo is my
[09:12] general assistant. Each agent runs as
[09:15] its own Slackbot with its own
[09:16] conversations. And I experimented with
[09:18] having them all in a group chat which
[09:20] kind of works but has some quirks. So I
[09:23] assigned a default model to each agent.
[09:25] Opus for Bernard the developer and Claw
[09:28] the system admin. That's where reasoning
[09:30] power really matters. And then Sonnet
[09:32] for Vale, the marketer, and Gumbo, the
[09:34] assistant. That's where speed and
[09:36] efficiency make more sense. But I often
[09:38] direct them to delegate parts of their
[09:40] work to sub agents for tasks where I
[09:44] need to specify a more expensive model
[09:46] or a cheaper model. Now, I decided to
[09:48] have them all share one workspace, which
[09:50] means they all access the same memory
[09:53] and I can manage configurations and
[09:55] agents MD directives all in one place.
[09:58] Also, my brain folder lives in this
[10:00] workspace and that's where all of our
[10:02] work gets synced up. And if you want to
[10:04] hear more about my productivity system
[10:06] with my agents, let me know in the
[10:07] comments and I'll make another video all
[10:09] about that. Now, OpenClaw has an
[10:11] identity.md file and that's typically
[10:14] used to define a single agents identity,
[10:17] but I use it to define multiple
[10:19] identities, one for each agent on my
[10:21] team. I even used Claude and Gemini to
[10:23] develop unique personality traits and a
[10:26] visual avatar for each agent. I wanted
[10:28] to have fun with it. You know, my bots
[10:29] are characters inspired by one of my
[10:31] favorite bands, Gorillas. Now, I did run
[10:34] into some challenges with OpenClaw's
[10:36] built-in cron system for scheduled
[10:38] tasks. It was hard to associate those
[10:40] tasks with specific agents on my team.
[10:43] And so, that ended up being one of the
[10:45] main reasons I built my own custom
[10:47] dashboard and task dispatching system.
[10:50] So, I quickly realized that managing my
[10:52] agents via chat alone was not going to
[10:54] cut it. I wanted to see all my scheduled
[10:56] tasks in one place and be able to assign
[10:58] them to specific agents. And I wanted to
[11:01] track token usage so I know how much all
[11:02] of this is costing me. You know, I just
[11:04] wanted a central dashboard where I could
[11:06] see the whole system at a glance. So,
[11:09] naturally, I built one. Any excuse to
[11:11] build something, right? I used cloud
[11:13] code and my design OS process and I had
[11:15] a working app in about a day. It's a
[11:18] simple Rails app that connects to
[11:19] OpenClaus Gateway and gives me a clean
[11:22] interface for managing everything.
[11:23] Honestly, that HQ dashboard was just the
[11:26] beginning. Now I'm building another app
[11:27] for editing and reading markdown files
[11:30] in my brain system so that I can easily
[11:32] manage what my agents have access to.
[11:34] This is what I love about this moment
[11:36] for builders. When a tool that I need
[11:38] doesn't exist yet, I just build it in a
[11:40] day. Now, the most important question
[11:42] and the one that I keep hearing
[11:43] everywhere is what are you actually
[11:45] going to use your agents for? So, I've
[11:47] identified a few specific areas where my
[11:49] agents can fill real gaps in my
[11:51] business. Let's start with the content
[11:53] that I publish. Now, I only put things
[11:55] out when I have something to say, and
[11:57] that'll never change. But the truth is,
[11:59] so much happens inside my projects and
[12:01] in my conversations with other builders
[12:04] that never makes it to a video or a
[12:06] social post. So, I'm building systems
[12:08] now that let my agents observe and
[12:10] capture more of that work and help me
[12:12] share more of it across my platforms.
[12:14] Second is development. Now, I still love
[12:16] to spend most of my time in cloud code
[12:19] and cursor designing and architecting
[12:21] products. That's not going to change,
[12:23] but I'm having Bernard, my developer
[12:25] agent, pick up backlog issues and track
[12:28] production errors and submit PRs during
[12:30] times when I can't get my hands on those
[12:32] things. Third is the glue work. This is
[12:35] a bottleneck that I feel every single
[12:37] day. Every minute that I spend project
[12:39] managing or copying and pasting or
[12:42] scheduling content or documenting
[12:44] things, that's time that I'm not
[12:46] thinking, creating or building. And
[12:48] those tasks should be automated or
[12:50] delegated. And that's exactly what my
[12:52] general assistant Gumbo is for. And the
[12:55] use case that has me most excited is
[12:57] reporting. So, having my agents surface
[12:59] trends and patterns and new ideas on a
[13:02] regular basis, helping me see blind
[13:04] spots that I wouldn't notice on my own,
[13:06] that's the kind of insight that helps me
[13:08] teach ideas that actually help builders
[13:10] get ahead and helps me create tools that
[13:12] solve real problems. Now, I've already
[13:15] started assembling the building blocks,
[13:16] the processes for my agents to follow,
[13:18] the automations, the custom tooling, and
[13:21] I'd love to report back on a future
[13:22] video to show you how all that's coming
[13:24] together. So, make sure you subscribe to
[13:26] the channel. Now, I want to be careful
[13:28] not to oversell OpenClaw. It's still
[13:30] very early, very raw, and I spent more
[13:32] late nights than I'd like to admit just
[13:34] getting things configured. But there's
[13:36] no denying the breakthrough as a concept
[13:38] that OpenClaw has broken open here, at
[13:40] least in our circles of AI pill
[13:42] builders. And I see this as one of those
[13:44] things that's worth our extra effort to
[13:46] be an early adopter on because systems
[13:48] like this are only going to become more
[13:50] commonplace as this year and next year
[13:52] play out. And that gets at something
[13:54] that I think is a fundamental skill for
[13:56] us as builders in 2026. We have to be
[13:59] willing to explore and tinker to figure
[14:01] out how new tools can help us make real
[14:04] progress in our business. That's the
[14:06] value that we bring to the table and
[14:08] it's one of the five essential skills
[14:10] that I think we need to master to go
[14:12] from being overwhelmed by the speed of
[14:14] change to actually thriving in this new
[14:16] environment. And I cover all five in my
[14:18] video on going from an AI skeptic to
[14:21] building an unfair advantage. So, right
[14:23] after you hit subscribe on the channel,
[14:24] I'll see you on that one next. Let's
[14:26] keep building.
