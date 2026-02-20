[00:00] At Enthropic, the way that we thought
[00:01] about it is we don't build for the model
[00:03] of today. We build for the model six
[00:05] months from now. That's actually like
[00:06] still my advice to to founders that are
[00:08] building on LLM. Just try to think about
[00:10] like what is that frontier where the
[00:12] model is not very good at today cuz it's
[00:14] going to get good at it. All of Quad
[00:15] Code has just been written and rewritten
[00:16] and rewritten and rewritten over and
[00:18] over and over. There is no part of Quad
[00:19] Code that was around 6 months ago. You
[00:21] try a thing, you give it to users, you
[00:22] talk to users, you learn, and then
[00:24] eventually you might end up at a good
[00:26] idea. Sometimes you don't. Are you also
[00:27] in the back of your mind thinking that
[00:28] maybe like in 6 months you won't need to
[00:30] prompt that explicitly? Like the model
[00:32] will just be good enough to figure out
[00:33] on its own?
[00:34] &gt;&gt; Maybe in a month,
[00:36] &gt;&gt; no more need for plan mode in a month.
[00:38] &gt;&gt; Oh my god.
[00:46] Welcome to another episode of the light
[00:49] cone and today we have an extremely
[00:51] special guest, Boris Churnney, the
[00:53] creator engineer of Claude Code. Boris,
[00:57] thanks for joining us.
[00:58] &gt;&gt; Thanks for having me.
[00:59] &gt;&gt; Thanks for creating a thing that has
[01:00] taken away my sleep for about 3 weeks
[01:02] straight.
[01:05] &gt;&gt; I am very addicted to Cloud Code and uh
[01:07] it feels like rocket boosters. Has it
[01:10] felt like this for people like for you
[01:12] know months at this point. I think it
[01:13] was like end of November is where uh a
[01:16] lot of my friends said like something
[01:18] changed.
[01:19] &gt;&gt; I remember for me I felt this way when I
[01:21] first created Quad Code and I didn't yet
[01:22] know if I was on to something. I kind of
[01:24] felt like I was on to something and then
[01:26] that's when I wasn't sleeping.
[01:27] &gt;&gt; Yeah.
[01:28] &gt;&gt; And that was just like three straight
[01:29] months.
[01:30] &gt;&gt; This was uh September 2024. Yeah. It was
[01:33] like three straight months. I I didn't
[01:34] take a single day vacation. Worked
[01:36] through the weekends. Worked every
[01:37] single night. I was just like, "Oh my
[01:39] god, this is I think this is going to be
[01:40] a thing. I don't know if it's useful yet
[01:43] because it it couldn't actually code
[01:44] yet."
[01:45] &gt;&gt; If you look back on uh those moments to
[01:48] now, like what would be like the most
[01:50] surprising thing about this moment right
[01:52] now?
[01:52] &gt;&gt; It's unbelievable that we're still using
[01:54] a terminal. That was supposed to be the
[01:55] starting point. I didn't think that
[01:56] would be the ending point. And then the
[01:58] second one is that it's even useful cuz
[02:00] uh you know at the beginning it didn't
[02:02] really write code. Even in February when
[02:04] we G it wrote maybe like 10% of my code
[02:06] or something like that. I didn't really
[02:07] use it to write code. it wasn't very
[02:08] good at it. I still wrote most of my
[02:10] code by hand. Uh so the fact that it it
[02:13] actually like our bets paid off and it
[02:15] got good at the thing that we thought it
[02:18] was going to get good at because it
[02:19] wasn't obvious. At Enthropic, the way
[02:21] that we thought about it is we don't
[02:22] build for the model of today. We build
[02:24] for the model 6 months from now. And
[02:27] that's actually like still my advice to
[02:28] to founders that are building on LLM is,
[02:31] you know, just try to think about like
[02:32] what is that frontier where the model is
[02:34] not very good at today. um because it's
[02:36] going to get good at it and you just
[02:37] have to wait.
[02:38] &gt;&gt; Going back though, but when do you
[02:39] remember when you first got the idea?
[02:41] Can you just talk us through that? Like
[02:42] was it some like a spark or what was
[02:44] even the first version of it in your
[02:46] mind?
[02:46] &gt;&gt; You know, it's funny. It was like it was
[02:48] so accidental that it just kind of
[02:49] evolved into this. Um you know as as
[02:52] anthropic I think for Ant the bet has
[02:54] been coding for a long time and the bet
[02:57] has been the path to save to safe AGI is
[03:01] through coding
[03:02] &gt;&gt; and this is this has kind of always been
[03:03] the idea and the way you get there is
[03:06] you you teach the model how to code then
[03:07] you teach it how to use tools then you
[03:08] teach it how to use computers um and you
[03:11] can kind of see that because the the
[03:12] first team that I joined at Enthropic it
[03:14] was called the anthropic labs team uh
[03:16] and it produced three products it was
[03:18] quadcode MCP and in the desktop app. So
[03:21] you can kind of see how these like weave
[03:22] together. The particular product that we
[03:24] built, you know, like no one no one
[03:27] asked me to build a CLI.
[03:29] Um we kind of knew maybe it was time to
[03:32] build some kind of coding product cuz it
[03:33] seemed like the model was ready, but no
[03:35] one had yet really built the product
[03:37] that harnessed this capability. So like
[03:39] still there's this insane feeling of
[03:41] product overhang. But at the time it was
[03:42] just like even crazier cuz like no one
[03:44] had built this yet. And so I I started
[03:46] like hacking around uh and I was like,
[03:49] "Okay, we build a coding product. What
[03:50] do I have to do first? I have to
[03:52] understand how to use the API because I
[03:53] hadn't used anthropic API at that
[03:55] point." Um and so I I just built like a
[03:58] little terminal app to use the API.
[04:00] That's all that I did. And it was a
[04:01] little chat app because you know like
[04:02] you think about the you know AI
[04:04] applications of the time and you know
[04:05] for non-coders today most what what are
[04:08] most people using is just a chat app. So
[04:09] that's what I built. Uh and you know it
[04:12] was in a terminal. I can ask questions.
[04:13] I give answers. Then I think tool use
[04:16] came out. I just wanted to try out tool
[04:17] use because I I don't really understand
[04:19] what this is. I was like to use this is
[04:20] cool. Is this actually useful? Probably
[04:22] not. Let me just try it.
[04:23] &gt;&gt; You built it in terminal just because it
[04:25] was the easiest way to get something up
[04:26] and running.
[04:27] &gt;&gt; Yes. Cuz I didn't have to build a UI.
[04:29] &gt;&gt; Okay.
[04:30] &gt;&gt; It was just me
[04:31] &gt;&gt; at that point. It was like the IDEs,
[04:32] Cursor, Windsurf
[04:34] taking off. Were you sort of under any
[04:37] pressure or getting lots of suggestions
[04:38] of, hey, like we should build this out
[04:40] as a plugin or as a as a fully featured
[04:42] ID itself? There was no pressure because
[04:44] we didn't even know what we wanted to
[04:45] build. Like the the team was just in
[04:47] explore mode, you know, like we we
[04:48] didn't we know vaguely we wanted to do
[04:50] something in coding, but it wasn't
[04:51] obvious what no one was high confidence
[04:53] enough. That was like my job to figure
[04:55] out. And so I g I gave the model uh the
[04:57] batch tool. That was the first tool that
[04:59] that I gave it just cuz I think that was
[05:00] literally the example in our docs. I
[05:03] just like took the example. It was in
[05:04] Python. I just ported it to TypeScript
[05:05] because that that's how I wrote it. You
[05:07] know, I didn't know like what the model
[05:08] could do with bash. So I asked it to
[05:09] like read a file. It could like cat the
[05:11] file. So like that was cool. And then I
[05:13] was like, "Okay, like what can you
[05:14] actually do?" And and I asked her, "What
[05:16] music am I listening to?" He wrote some
[05:18] like Apple script to script my my Mac
[05:21] and look up the music in my music
[05:23] player.
[05:24] &gt;&gt; And this was Sauna 3.5.
[05:26] &gt;&gt; And you know, like I I didn't think the
[05:28] model could do that. And that was my
[05:30] first I think ever fuel the AGI moment
[05:33] &gt;&gt; where I was just like, "Oh my god, the
[05:34] model it just wants to use tools. That's
[05:37] all it wants."
[05:38] &gt;&gt; That's kind of fascinating. I mean it's
[05:39] very kind of contrarian that clocker
[05:44] works so well in such an elegant simple
[05:46] form factor. I mean terminals have been
[05:48] around for a really long time and that
[05:51] seemed to be like a good design
[05:53] constraint that allowed a lot of
[05:55] interesting developer experiences like
[05:58] it doesn't feel like working. It just
[06:00] feels fun as a developer. I don't think
[06:02] about files where everything is and that
[06:05] came by accident almost.
[06:07] &gt;&gt; Yeah, it was an accident. I remember so
[06:09] after the terminal started to take off
[06:11] internally. Um and honestly like after
[06:13] building this thing I think like 2 days
[06:15] after the first prototype I started
[06:16] giving it to my team just for dogfooting
[06:18] cuz you know like you know if you come
[06:20] up with an idea and it seems useful the
[06:22] first thing you want to do is you want
[06:23] to give it to people to see how they use
[06:24] it. And then I came in the next day and
[06:26] then Robert who sits across from me
[06:28] who's another engineer he he just like
[06:31] had quad code on his computer and he was
[06:32] like using it to code. I was like I was
[06:34] like what what are you what are you
[06:35] doing? Like this thing isn't ready. It's
[06:36] just a prototype. But yeah, it it was
[06:38] already useful in that form factor. And
[06:40] I remember when we did our launch review
[06:42] to kind of launch quad code externally,
[06:44] this was in December, November,
[06:47] something like that in 2024. Um Dario
[06:50] asked and he was like, "The us chart
[06:52] internally like the the Dow chart is
[06:53] like vertical. Are you like forcing
[06:55] engineers to use it? Like why are you
[06:57] mandating them?"
[06:58] &gt;&gt; And I was just like, "No, no, we didn't.
[07:00] We I just like posted about it and they
[07:02] they' just been like telling each other
[07:03] about it." Honestly, it was it was just
[07:05] accidental. We we started with the CLI
[07:06] because it was the cheapest thing and it
[07:08] just kind of stayed there for a bit.
[07:09] &gt;&gt; So in that 2024 period, what how were
[07:13] the engineers using it? Were they sort
[07:14] of shipping code with it yet or were
[07:16] they using it in a different way?
[07:18] &gt;&gt; The model is not very good at coding
[07:19] yet. I I was using it personally for
[07:21] automating git. Um I think at this point
[07:24] I I probably forgotten most of my git
[07:26] because cloud code has just been doing
[07:28] it for so long. But yeah, like
[07:29] automating uh bash commands that that
[07:31] was a very early use case and like
[07:33] operating like Kubernetes and kind of
[07:34] things like this. People were using it
[07:36] for coding. So there were some early
[07:37] signs of this. I think the first use
[07:39] case was actually writing unit tests
[07:40] because it's a little bit lower risk and
[07:42] the model was still pretty bad at it
[07:44] &gt;&gt; but people were were were kind of
[07:46] figuring it out and and they were
[07:47] figuring out how to use this thing.
[07:49] &gt;&gt; Um and one thing that we saw is people
[07:51] started writing these markdown files for
[07:53] themselves and then having the model
[07:55] read that markdown file. And this is
[07:57] where QuadMD came from. Probably the
[07:59] single for me biggest principle in
[08:00] product is latent demand. Um and the
[08:03] just every bit of this product is built
[08:04] through latent demand after their
[08:06] initial CLI. Uh and so quadmd is an
[08:09] example of that. There's this other
[08:10] general principle that I think is maybe
[08:12] interesting where you can build for the
[08:15] model and then you can build scaffolding
[08:17] around the model in order to improve
[08:18] performance a little bit and depending
[08:20] on the domain you can improve
[08:22] performance maybe 10 20% something like
[08:24] that and then essentially the gain is
[08:26] wiped out with the next model. So either
[08:28] you can build build the scaffolding and
[08:30] then you know get some performance gain
[08:31] and then rebuild it again or you just
[08:33] wait for the next model and then you
[08:35] kind of get it for free. the quantumd
[08:36] and kind of the scaffolding is an
[08:38] example of that and really I think
[08:39] that's why we stayed in the CLI is
[08:41] because we felt there is no UI we could
[08:44] build that would still be relevant in 6
[08:46] months because the model was improving
[08:48] so quickly
[08:49] &gt;&gt; earlier we were saying like we should
[08:50] compare cloud MDs but you said something
[08:52] very profound which is you know yours is
[08:55] actually very short which is almost like
[08:57] the opposite of what you know people
[08:58] might expect why is that what's in your
[09:01] cloud MD
[09:01] &gt;&gt; okay so I I checked this before we came
[09:04] so my my cloud has two
[09:06] Um, one is, uh, there it's just two
[09:09] lines. So, the first line is whenever
[09:11] you put up a PR, enable automerge. Um,
[09:14] so as soon as someone accepts it, it's
[09:15] merged. That's just so I can like code
[09:17] and I don't have to kind of go back and
[09:19] forth with CR or whatever. And then the
[09:21] second one is whenever I put up a PR,
[09:22] post it in our internal team stamps
[09:24] channel. Uh, just so someone can stamp
[09:26] it and I can get unblocked. Uh, and the
[09:29] idea is every other instruction is in
[09:31] our quadmd that's checked into the
[09:33] codebase and it's something our entire
[09:35] team contributes to multiple times a
[09:37] week. And very often I'll see someone's
[09:40] PR and they make some like mistake
[09:43] that's totally preventable and I'll just
[09:44] literally tag Claude on the PR. I'll
[09:46] just do like add quad, you know, like
[09:48] add this to the quad MD and I'll do
[09:49] this, you know, like many times a week.
[09:51] &gt;&gt; Do you have to like compact the Claude
[09:52] MD? Like I definitely reached a point
[09:54] where I got the message at the top
[09:56] saying your cloud MD is like thousands
[09:58] of tokens now. What do you do when you
[10:00] guys hit that?
[10:01] &gt;&gt; So our quadm is actually pretty short. I
[10:03] think it's like couple thousand tokens
[10:05] maybe something like that. Um if if you
[10:07] hit this my recommendation would be
[10:08] delete your quadmd and just start fresh.
[10:10] &gt;&gt; Interesting.
[10:11] &gt;&gt; I think a lot of people like they try to
[10:12] overengineer this right and and really
[10:15] like the capability changes with every
[10:16] model. And so the thing that you want is
[10:19] do the minimal possible thing in order
[10:21] to get the model on track. And so if you
[10:23] delete your quadd and then you know the
[10:25] model is getting off track, it does the
[10:26] wrong thing. That's when you kind of add
[10:28] back a little bit at a time. And what
[10:30] you're probably going to find is with
[10:31] every model, you have to add less and
[10:32] less. For me, I consider myself a pretty
[10:34] average engineer to be honest. Like I
[10:36] don't use a lot of fancy tools. Like I I
[10:38] don't use like Vim. I use, you know, VS
[10:40] Code because it's simpler. Um I don't
[10:42] really
[10:42] &gt;&gt; Wait, really? I would have assumed that
[10:44] because you built this in the terminal
[10:45] that you were sort of like a dieh hard
[10:47] ter terminal like Vim Vim only person
[10:49] you know screw those VS code people you
[10:51] know
[10:52] &gt;&gt; well we have people like that on the
[10:53] team there's you know like Adam Wolf for
[10:54] example he's he's on the team he's like
[10:56] you will never take Vim for my cold dead
[10:58] hands like yeah so there's definitely a
[11:00] lot of people like that on the team and
[11:01] this is one of the things that I learned
[11:02] early on is every engineer likes to hold
[11:04] their dev tools differently they like to
[11:06] use different tools there's just no one
[11:07] tool that works for everyone but I think
[11:08] also this is one of the things that
[11:10] makes it possible for quad code to be so
[11:13] good because I kind of think about it as
[11:15] what is the product that I would use
[11:17] that makes sense to me and so to use
[11:19] quad code you don't have to understand
[11:20] Vim you don't have to understand TMX you
[11:22] don't have to know how to like SSH you
[11:24] don't have to know all the stuff you
[11:25] just have to open up the tool and it'll
[11:27] guide you it'll it'll do all this stuff
[11:28] &gt;&gt; how do you decide how verbose you want
[11:30] like sort of the terminal to be like
[11:32] sometimes you have to go you know
[11:34] control O and check it out and is it
[11:36] like internal bike shed battles around
[11:38] like longer shorter I mean every user
[11:42] probably has a for an opinion like how
[11:44] do you make those sorts of decisions?
[11:45] &gt;&gt; What What's your opinion? Is it is it
[11:47] too verbose right now?
[11:48] &gt;&gt; Oh, I love the verbosity cuz basically
[11:50] sometimes it just like goes off the deep
[11:52] end and I'm watching and then I can just
[11:54] read very quickly and it's like, "Oh,
[11:55] no, no, it's not that." And then I
[11:57] escape and then just stop it and then it
[11:59] just like stops an entire bug farm like
[12:02] as it's happening. I mean, that's
[12:03] usually when I didn't do plan mode
[12:05] properly.
[12:05] &gt;&gt; This is something that we probably
[12:07] change pretty often. Um, I remember
[12:09] early on, this is maybe six months ago,
[12:11] I tried to get rid of bash output just
[12:13] internally just to like summarize it
[12:14] because I was like these giant long bash
[12:16] commands, I don't actually care. And
[12:18] then I gave it to anthropic employees
[12:19] for a day and everyone just revolted.
[12:22] I want to see my dash because it it
[12:23] actually is quite useful for, you know,
[12:25] like for something like git output,
[12:27] maybe it's not useful, but if you're
[12:29] running, you know, like Kubernetes jobs
[12:30] or something like this, you actually do
[12:31] want to see it. We recently hit the hid
[12:33] the file reads and uh file searches. So
[12:36] you'll notice instead of saying, you
[12:38] know, like read food.md said, you know,
[12:40] like read one file, search searched one
[12:42] pattern. And this is something I think
[12:44] we could not have shipped six months ago
[12:45] because the model just was not ready. It
[12:47] would have, you know, it still read the
[12:48] wrong thing pretty often. As a user, you
[12:50] still had to be there and kind of catch
[12:51] it and debug it. But nowadays, I just
[12:53] noticed it's on the right track almost
[12:55] every time. And because it's using tools
[12:57] so much, it's actually a lot better just
[12:59] to summarize it. Um, but then we shipped
[13:01] it. Uh, we dog fooded it for like a
[13:03] month and then people on GitHub didn't
[13:04] like it. Uh so there was a big issue
[13:06] where people like no like I want to see
[13:07] the details and that was really great
[13:09] feedback. Um and so we added a new
[13:11] verbose mode and so that's just like in
[13:13] slash config you can enable verbose mode
[13:15] and if you want to see all the file
[13:16] outputs you can continue to do that and
[13:18] then I posted on the issue and people
[13:20] still still didn't like it which is
[13:22] again awesome because like my favorite
[13:23] thing in the world is just hearing
[13:25] people's feedback and hearing how they
[13:26] actually want to use it. Um and so we
[13:28] just like iterated more and more and
[13:29] more to get that really good and to make
[13:30] it the thing that people want. I'm
[13:32] amazed like how much I enjoy uh fixing
[13:34] bugs now. And then all you have to do is
[13:37] uh have really good logging and then
[13:40] even just say like hey check out that
[13:42] you know this particular object it
[13:44] messed up in this way and it like
[13:46] searches the log. It figures everything
[13:47] out. It can like go into your you can
[13:49] make a production tunnel and it'll look
[13:51] at your production DB for you. It's like
[13:53] this is insane. Bug fixing is just going
[13:55] to sentry copy markdown. You know pretty
[13:57] soon it's just going to be straight MCP.
[13:59] It's like an autobug fixing like and
[14:02] test making sort of uh what's the new uh
[14:05] term they call it like a making a
[14:07] startup factory. Oh yeah.
[14:08] &gt;&gt; Right. There's like all these concepts
[14:10] now of rather than having to review the
[14:13] code, you know, I'm I'm old school, so I
[14:16] like the verbosity. I like to say, "Oh,
[14:18] well, you're doing this, but I want you
[14:19] to do that." Right? But there's a
[14:21] totally different school of thought now
[14:23] that says like anytime an a real human
[14:26] being has to look at code uh that's bad.
[14:29] &gt;&gt; Yeah. Yeah. Yeah.
[14:30] &gt;&gt; Which is fascinating.
[14:31] &gt;&gt; I think like Dan Chipper talks about
[14:32] this a lot as kind of when whenever you
[14:35] see the model make a mistake try to put
[14:36] in the quadmd try to put it in like
[14:38] skills or something like that so it's
[14:39] reusable. But I I think there's this
[14:42] meta point that I actually struggle with
[14:43] a lot. And I people talk about like
[14:46] agents can do this, agents can do that,
[14:47] but actually what agents can do, it
[14:49] changes with every single model. And so
[14:51] sometimes there's a new person that
[14:52] joins the team and they actually use
[14:53] quad code more than I would have used
[14:56] it.
[14:56] &gt;&gt; And I'm just constantly surprised by
[14:58] this. Like for example, there was a we
[15:01] had like a memory leak and we were
[15:02] trying to debug it. Um and by the way,
[15:04] like Jared Sumar has just been on this
[15:05] crusade killing all the memory leaks and
[15:07] it's just been amazing. But before Jared
[15:09] was on the team, I had to do this and
[15:11] there was this memory leak. I I was
[15:12] trying to debug it. And so I I took a
[15:14] heap dump. I opened it in DevTools. I
[15:16] was looking through the profile. Then I
[15:17] was looking through the code and I I was
[15:18] just trying to figure this out. And then
[15:20] another engineer on the team, Chris, he
[15:23] just like asked Quad Code. He was like,
[15:25] "Hey, I think there's a memory leak. Can
[15:26] you like run this?" And then like try to
[15:28] figure it out. And Quad Code like took
[15:29] the heap dump. It wrote a little tool
[15:30] for itself to like analyze the heap
[15:32] dump. And then it found the leak faster
[15:34] than I did. And this is just something I
[15:37] have to constantly relearn because my
[15:40] brain is still stuck somewhere six
[15:42] months ago at times.
[15:44] &gt;&gt; So what would be some advice for
[15:46] technical founders to really become
[15:49] maximalists at the latest model release?
[15:52] It sounds like people off of fresh off
[15:54] of school or that don't have any
[15:56] assumptions might be better suited than
[15:58] maybe sometimes engineers who have been
[16:00] working at it for a long time. And how
[16:02] do the experts get better? I think for
[16:05] yourself it's kind of beginner mindset
[16:07] and uh I don't know maybe just like
[16:10] humility like I feel like engineers as a
[16:12] discipline we've learned to have very
[16:14] strong opinions and senior engineers are
[16:16] kind of rewarded for this in my old job
[16:18] at a big company when I hired like
[16:19] architects and this kind of a type of
[16:21] engineer you look for people that have a
[16:23] lot of experience and really strong
[16:24] opinions but it actually turns out a lot
[16:26] of this stuff just isn't relevant
[16:27] anymore and a lot of these opinions
[16:29] should change because the model is
[16:31] getting better um so I think actually
[16:33] the biggest skill is people that can
[16:35] think scientifically and can just think
[16:37] from first principles.
[16:38] &gt;&gt; How do you screen for that when you try
[16:40] to hire someone now for for your team?
[16:42] &gt;&gt; I sometimes ask about what's an example
[16:44] of when you're wrong. It's a really good
[16:45] one. You know, some of these like
[16:47] classic behavioral questions like not
[16:48] even coding questions I think are quite
[16:50] useful because you can see if people can
[16:52] recognize their mistake in hindsight, if
[16:53] they can claim credit for the mistake
[16:55] and if they learn something from it. And
[16:58] I think a lot of these like very senior
[16:59] people especially there there are some
[17:01] founder types like this but I think
[17:02] founders in particular are actually
[17:04] quite good at it. Um but other people
[17:06] sometimes will never really take uh
[17:09] they'll never take the blame for a
[17:10] mistake. But I don't know like for me
[17:12] personally I'm wrong probably half the
[17:14] time. Like half my ideas are bad and you
[17:16] just have to try stuff and you know you
[17:18] try a thing you give it to users you
[17:20] talk to users you learn and then
[17:23] idea. Sometimes you don't. And this is
[17:25] the skill that I think in in the past
[17:27] was very important for founders, but now
[17:30] I think it's very important for every
[17:31] engineer.
[17:32] &gt;&gt; Do you think um you would ever hire
[17:34] someone based on the uh claude code
[17:37] transcript of uh them working with the
[17:39] agent cuz we're actively doing that
[17:42] right now. We just added uh just as a
[17:44] test like you can upload a transcript of
[17:47] you coding a feature with cloud code or
[17:50] codeex or whatever it is. Personally, I
[17:52] think that like it's going to work. I
[17:53] mean, you can figure out uh how someone
[17:56] thinks, like whether they're looking at
[17:58] the logs or not, like can they correct
[18:00] the agent if it goes off off the rails?
[18:02] Like, does do they use plan mode? You
[18:04] know, when they use plan mode, do they
[18:06] make sure that there are tests or you
[18:08] know, all of these different things
[18:09] that,
[18:10] &gt;&gt; you know, do they think about systems?
[18:11] Do they even understand systems? Like,
[18:13] there's just so much that's sort of
[18:14] embedded in that that I imagine. I just
[18:17] want like a spider uh a spiderweb graph,
[18:19] you know, like in those video games like
[18:21] NBA 2K. It's like, oh, this person's
[18:23] really good at shooting or defense. It's
[18:24] like you could imagine a spiderweb graph
[18:26] of like, you know, someone's claude code
[18:29] skill level.
[18:30] &gt;&gt; Yeah. What would what would the skills
[18:31] be? What would be those?
[18:32] &gt;&gt; I mean, I think it's like systems
[18:34] testing must be like user behavior. I
[18:37] mean, there's got to be a design part
[18:39] like product sense maybe also just like
[18:41] automating stuff. Mhm. My favorite thing
[18:43] in CloudMD uh for me is I have a thing
[18:46] that says for every plan decide whether
[18:49] it's overengineered, underengineered, or
[18:51] perfectly engineered and why.
[18:53] &gt;&gt; I think this is something that we're
[18:54] trying to figure out, too, cuz I I think
[18:56] uh when I look at engineers on the team
[18:57] that I think are the most effective,
[18:59] there's essentially two, it's very
[19:00] biodal. Um there's one side where it's
[19:03] extreme specialists. Um and so like I
[19:05] named Jared before, like he's a really
[19:06] good example of this and kind of the bun
[19:08] team is a really good example. Just
[19:09] hyper specialist. They understand dev
[19:11] tools better than anyone else. They
[19:13] understand JavaScript runtime systems
[19:14] better than anyone else. And then
[19:16] there's the flip side of kind of hyper
[19:18] generalists and that's kind of the rest
[19:19] of the team. And a lot of people they
[19:21] span like product and info or product
[19:23] and design um or you know like product
[19:25] and user research, product and business.
[19:27] I really like to see people that just do
[19:30] weird stuff. I think that's one of these
[19:32] things that was kind of a warning sign
[19:33] in the past because it's like can these
[19:35] people actually build something useful?
[19:37] &gt;&gt; Um that's the limits test. Yeah, that's
[19:39] what must but but nowadays like for
[19:42] example an engineer on the team Daisy,
[19:44] she was on a different team and then she
[19:45] transferred onto our team and the reason
[19:47] that I wanted her to transfer is she put
[19:51] up a PR for Claude Code like a couple
[19:53] weeks after she joined or something and
[19:56] the PR was to add a new feature to
[19:57] Claude Code and then instead of just
[19:59] adding the feature what she did is first
[20:01] she put up a PR to give Claude code a
[20:03] tool so that it can test an arbitrary
[20:05] tool and verify that that works. And
[20:07] then she put up that PR and then she had
[20:09] Quad write its own tool instead of
[20:11] herself implementing it. And I think
[20:13] it's this kind of out of the box
[20:14] thinking that is is just so interesting
[20:16] because not a lot of people get it yet.
[20:17] You know, like we use the Quad agents
[20:19] SDK to automate pretty much every part
[20:21] of development. It automates code
[20:23] review, security review. Uh it labels
[20:25] all of our issues. It shephards things
[20:27] to production. It does pretty much
[20:29] everything for us. But I think
[20:30] externally I'm seeing a lot of people
[20:32] start to figure this out, but it's
[20:34] actually taken a while to figure out how
[20:35] do you use LMS in this way? How do you
[20:38] use this new kind of automation? So it's
[20:40] kind of a new skill.
[20:40] &gt;&gt; I guess one of the uh funnier things
[20:42] that I've been having office hours with
[20:44] various founders about is um you have
[20:46] like sort of the visionary founder who
[20:48] has like the idea they've like built
[20:50] this like crystal palace of the product
[20:53] that they want to build. they've totally
[20:54] loaded in their brain, you know, who the
[20:57] user is and what they feel and what
[20:58] they're motivated by and then they're
[21:01] sitting in claude code and they can do
[21:02] like, you know, 50x work and then but
[21:06] they have engineers who work for them
[21:07] who like don't have the, you know,
[21:09] crystal memory palace of like the
[21:11] platonic ideal of the product that the
[21:13] pro founder has and they can only do
[21:15] like 5x work. Are you hearing stories
[21:17] like that? there's usually a person
[21:20] who's like the core like designer of a
[21:23] thing and they're just like, you know,
[21:25] trying to blast it out of their brain.
[21:27] What's the nature of like teams like
[21:30] that? You know, it seems like that's
[21:31] almost a stable configuration. Like
[21:33] you're going to have the visionary who
[21:35] like now is unleashed, but you know,
[21:38] maybe going back to the top of it, like
[21:40] I'm experiencing this right now. I was
[21:41] like, "Oh, well, I'm only a solo person
[21:44] and you know, I need to eat and sleep
[21:46] and I have, you know, a whole job. It's
[21:49] like, how am I going to do this?" You
[21:50] know,
[21:51] &gt;&gt; you know, like we just launched quad
[21:52] teams and, you know, this is a way to do
[21:54] it, but you can also just build your own
[21:55] way to do it. It's pretty easy.
[21:57] &gt;&gt; What's the vision for cloud teams?
[21:59] &gt;&gt; Just collaboration. It's like there's
[22:01] this whole new field of like agent top
[22:02] apologies that people are exploring.
[22:03] Like what are the ways that you can
[22:05] configure agents? There's this one sub
[22:07] idea which is uncorrelated context
[22:08] windows. And the idea is just multiple
[22:10] agents, they have fresh context windows
[22:12] that aren't essentially polluted with
[22:13] each other's context or their own
[22:15] previous context. And if you throw more
[22:17] context at a problem, that's like a form
[22:18] of test time compute. Um, and so you
[22:21] just get more capability that way. And
[22:22] then if you have the right topology on
[22:24] top of it, so the agents can communicate
[22:25] in the right way, they're laid out in
[22:27] the right way, then they can just build
[22:29] bigger stuff. And so Teams is kind of
[22:31] like one idea. There's a few more that
[22:33] are coming pretty soon. Um, and the idea
[22:35] is just maybe it can build a little bit
[22:37] more. I think the first kind of big
[22:40] example where it worked is our plugins
[22:41] feature was entirely built by a swarm
[22:44] over over a weekend. It just ran for
[22:46] like a few days. There wasn't really
[22:47] human intervention. And plugins is
[22:50] pretty much in the form that it was when
[22:51] when it came out.
[22:52] &gt;&gt; How did you set that up? Like did you
[22:54] spec out sort of the outcome that you
[22:56] were hoping for and then let it sort of
[22:59] figure out the details and then like let
[23:01] it run?
[23:02] &gt;&gt; Yeah. an engineer on the team just gave
[23:04] uh gave Quad a spec and um told Quad to
[23:08] use a Asauna board and then Quad just
[23:11] put up a bunch of tickets on a sauna and
[23:13] then spawned a bunch of agents and the
[23:14] agent started picking up tasks. The main
[23:16] quad just gave it instructions and they
[23:18] all just figured it out
[23:19] &gt;&gt; like independent um agents that didn't
[23:21] have the context of the bigger spec.
[23:23] Right.
[23:23] &gt;&gt; Right. If you if you think about the way
[23:25] that uh you know like how our agents
[23:27] actually started nowadays and you know I
[23:29] haven't pulled the data on this but I
[23:30] would bet the majority of agents are
[23:32] actually prompted by quad today in the
[23:34] form of uh sub agents cuz like a sub
[23:37] agent is just like a recursive quad code
[23:38] that's all it is in the code and it's
[23:40] just prompted by we call her mama quad
[23:43] &gt;&gt; and that that's all it is and I think
[23:45] probably if you look at most agents
[23:46] they're launched in this way
[23:47] &gt;&gt; my claude insights just told me to do
[23:49] this more for debugging so that I get
[23:51] like I spend a lot of time on debugging
[23:53] And it would just be better to have like
[23:55] multiple sub agents spin up and like
[23:57] debug something in parallel. And so then
[23:59] I just like added that to my claude MD
[24:01] to just be like, hey, like next time you
[24:02] try and fix a bug like have one agent
[24:04] that like looks in the log, like one
[24:06] that looks in the code path. That just
[24:07] seems sort of inevitable.
[24:09] &gt;&gt; For weird scary bugs, I try to uh fix
[24:11] bugs in plan mode and then it seems to
[24:13] use the agents to sort of search
[24:15] everything. Whereas like when you're
[24:17] just trying to do it in line, it's like,
[24:19] okay, I'm going to do like this one task
[24:21] instead of search wide. This is
[24:23] something I do all the time too. I I
[24:24] just say if the if the test seems kind
[24:26] of hard, this kind of research test,
[24:28] I'll calibrate the number of sub aents I
[24:29] ask it to use based on the difficulty of
[24:31] the task.
[24:32] &gt;&gt; So if it's like really hard, I'll say
[24:33] like use three or maybe five or even 10
[24:35] sub aents, research in parallel and then
[24:38] see what they come up with.
[24:39] &gt;&gt; I'm curious. So then why don't you put
[24:40] that in your clawed MD file?
[24:42] &gt;&gt; It's kind of case by case, you know,
[24:44] like quadm like what is it? It's just a
[24:47] it's a shortcut. Like if you find
[24:48] yourself repeating the same thing over
[24:50] and over, you put in the quad MD. But
[24:52] otherwise, you don't have to put
[24:53] everything there. You can just prompt
[24:54] quad.
[24:54] &gt;&gt; Are you also in the back of your mind
[24:56] thinking that maybe like in six months,
[24:57] you won't need to prompt that
[24:59] explicitly? Like the model will just be
[25:01] good enough to figure out on its own.
[25:03] &gt;&gt; Maybe in a month.
[25:05] &gt;&gt; No more need for plan mode in a month.
[25:08] &gt;&gt; I think plan mode probably has a limited
[25:09] lifespan.
[25:11] &gt;&gt; That's some alpha for everyone here.
[25:12] What would the world look like without
[25:14] plan mode? Do you just describe it at
[25:16] the prompt level and it would just do
[25:18] it? One shot it? Yeah, we've uh we've
[25:20] started experimenting with this because
[25:21] quad code can now enter plan mode by
[25:23] itself. I don't know if you've you guys
[25:25] have seen that.
[25:26] &gt;&gt; So, we're trying to kind of get this
[25:28] experience really good. So, it would
[25:30] enter plan mode the same point where a
[25:32] human would have wanted to enter it. So,
[25:34] I think it's like I think it's something
[25:35] like this, but actually plan mode
[25:37] there's no there's no big secret to it.
[25:38] All it does is it adds one sentence to
[25:41] the prompt that's like please don't
[25:42] code.
[25:43] &gt;&gt; That's all it is. You can you can
[25:44] actually just say that.
[25:45] &gt;&gt; Yeah. So it sounds like a lot of the
[25:47] feature development for clock code is
[25:48] very much a what we talk about a YC talk
[25:51] to your users
[25:52] &gt;&gt; and then you come and implemented it. It
[25:54] wasn't the other way that you had this
[25:55] master plan and then implemented all the
[25:57] features.
[25:58] &gt;&gt; Yeah. Yeah. I mean that that's all it
[25:59] was like plan mode was we saw users that
[26:01] that were like hey quad come up with an
[26:03] idea plan this out but don't write any
[26:05] code yet. And there was kind of various
[26:06] versions of this. Sometimes it was just
[26:08] talking through an idea. Sometimes it
[26:09] was these very sophisticated specs that
[26:11] that they were asking Claude to write,
[26:13] but the common dimension was do a thing
[26:15] without coding yet. And so literally
[26:17] like this was like Sunday night at 10
[26:19] p.m. I was I was just like looking at
[26:21] GitHub issues and kind of seeing what
[26:22] people were talking about and looking at
[26:24] our internal Slack feedback channel and
[26:26] I just wrote this thing in like 30
[26:27] minutes and then uh shipped it that
[26:29] night. It went out Monday morning. That
[26:30] was plan mode. So do you mean that there
[26:32] will be no need for plan mode to in the
[26:34] sense of I'm worried that the model's
[26:36] going to do like it's going to do like
[26:38] the wrong thing or head off in the wrong
[26:39] direction but there will still be a need
[26:41] for that. You need to think through the
[26:43] idea and figure out exactly what it is
[26:45] that you want and you have to do that
[26:46] somewhere.
[26:47] &gt;&gt; I kind of think about it in terms of
[26:49] like kind of increasing model
[26:50] capabilities. So maybe 6 months ago a
[26:53] plan was insufficient. So you get Claude
[26:55] to make a plan. Let's say even with plan
[26:57] mode you still have to kind of sit there
[26:58] and babysit cuz it can go off track.
[27:00] Nowadays what I do is probably 80% of my
[27:02] sessions I say I say plan mode has a
[27:03] limited lifespan but I I'm a heavy plan
[27:05] mode user. Um I probably 80% of my
[27:08] sessions I start in plan mode and claude
[27:11] will you know it'll start it'll start
[27:13] making a plan. I'll move on to my second
[27:14] terminal tab and then I'll have it make
[27:16] another plan and then when I run out of
[27:18] tabs I open the desktop app and then I
[27:20] go to the code tab and then I just start
[27:21] a bunch of tabs there and they all start
[27:22] in plan mode probably know like 80% of
[27:25] the time. Once the plan is good, and
[27:26] sometimes it takes a little back and
[27:27] forth, they just get clawed to execute.
[27:30] And nowadays, what I find with Opus 4.5,
[27:33] I think it started with 4.6 it got
[27:35] really good. Once the plan is good, it
[27:37] just stays on track and it'll just do
[27:39] the thing exactly right almost every
[27:40] time. And so, you know, before you had
[27:42] to babysit after the plan and before the
[27:44] plan, now it's just before the plan. So,
[27:47] maybe the next thing is you just won't
[27:48] have to babysit. You can just kind of
[27:49] give a prompt and Quad will figure it
[27:51] out.
[27:51] &gt;&gt; The next step is Claude just speaks to
[27:53] your users directly.
[27:56] Yeah, it just bypasses you entirely.
[27:58] &gt;&gt; It's funny. This is actually the current
[27:59] stuff for us. Our quads actually like
[28:00] they talk to each other. They talk to
[28:02] our users on Slack, at least internally
[28:04] pretty often. Um, my quad will like
[28:07] tweet once in a while.
[28:08] &gt;&gt; No way.
[28:08] &gt;&gt; Um, but I actually like delete it. It's
[28:11] just like it's a little like cheesy.
[28:13] Like I don't love the tone.
[28:14] &gt;&gt; What does it want to tweet about?
[28:16] &gt;&gt; Sometimes it'll just like respond to
[28:17] someone cuz I always have like co-work
[28:19] in the background and it's like it's the
[28:20] co-work that really loves to do that
[28:22] because it likes using a browser.
[28:23] &gt;&gt; That's funny. A a really common pattern
[28:25] is I ask Quad to build something. It'll
[28:27] look in the codebase. Uh it'll see some
[28:29] engineer touch something in the git
[28:30] flame and then it'll message that
[28:32] engineer on Slack. Um just like asking a
[28:34] clarifying question and then once it
[28:36] gets answer back, it'll keep going.
[28:37] &gt;&gt; What are some tips for founders now on
[28:40] how to build for the future? Sounds like
[28:42] everything is really changing. What are
[28:44] like some principles that will stay on
[28:46] and what will change?
[28:48] &gt;&gt; So I think some of these are pretty are
[28:49] pretty basic, but I think they're even
[28:51] more important now than they were
[28:52] before. Um, so one example is latent
[28:55] demand. Like I mentioned it a thousand
[28:56] times for me. It's just like the single
[28:58] biggest idea in product. It's a it's a
[29:00] thing that no one understands. It's a
[29:03] thing I certainly did not understand my
[29:04] first few startups. And and the idea is
[29:06] like people will only do a thing that
[29:08] they already do. You can't get people to
[29:10] do a new thing. If people are trying to
[29:11] do a thing and you make it easier,
[29:13] that's a good idea. But if if people are
[29:15] doing a thing and you try to make them
[29:16] do a different thing, they're not going
[29:17] to do that. And so you just have to make
[29:19] the thing that they're trying to do
[29:20] easier. And I think quad is going to get
[29:22] increasingly good at kind of figuring
[29:23] out these kind of product ideas for you
[29:25] just because it can look at feedback, it
[29:26] can look at debug logs, it can kind of
[29:28] figure this out.
[29:28] &gt;&gt; That's what you mean by plan mode was
[29:30] latent demand that people were already
[29:32] like I don't know had their clawed chat
[29:34] window open in a browser and were like
[29:36] talking to it to figure out like the
[29:38] spec and and what it should do. And now
[29:42] that like pi mode just became that you
[29:43] just do it in claw code.
[29:44] &gt;&gt; Yeah. Yeah, that's it. Some sometimes
[29:46] what I'll do is I'll just walk around
[29:47] the office on on our floor and I'll just
[29:49] kind of stand behind people like I I'll
[29:52] say like hi so it's not and then um I'll
[29:54] I'll just see kind of like how they're
[29:55] using quad code. Um and this is also
[29:57] just something I saw a lot um but it
[29:59] also came up in GitHub issues like
[30:00] people were talking about it. It seems
[30:02] like so you're surprised how far the
[30:04] terminal has gone and how far it's been
[30:06] pushed like how far do you think it has
[30:08] left to go just given with this world of
[30:11] swore multiple agents like do you think
[30:13] there's going to be a new a need for a
[30:16] different UI on top of it?
[30:17] &gt;&gt; It's funny if you asked me this a year
[30:19] ago I would have said the terminal has
[30:20] like a threemonth lifespan and then
[30:21] we're going to move on to the next
[30:22] thing. Uh and you can see us
[30:24] experimenting with this right because
[30:25] quad code started in a terminal but now
[30:27] it's in you know it's on web you can
[30:29] like quadcode it's in the desktop app
[30:32] you know we've had that for you know
[30:33] like three months or six months or
[30:34] something just in the code tab um it's
[30:37] in the iOS and Android apps just like in
[30:38] the code tab it's in slack it's in
[30:41] GitHub there's VS Code extensions
[30:43] there's Jet Brains extensions so we're
[30:45] just like we're always experimenting
[30:46] with different form factors for this
[30:48] thing to figure out what's the next
[30:50] thing I've been wrong so far about the
[30:53] of the CLI. So, I'm probably not the
[30:54] person to forecast that.
[30:56] &gt;&gt; What about like your advice to DevTool
[30:58] founders? Like, someone's building a
[31:00] DevTool company today. Should they just
[31:02] like be building for engineers and
[31:05] humans or should they be thinking more
[31:06] about like what Claude going to think
[31:08] and want and build for sort of like the
[31:10] agent?
[31:11] &gt;&gt; The way I would frame it is think about
[31:13] the thing that the model wants to do and
[31:16] figure out how do you make that easier.
[31:19] And that's something that we saw, you
[31:20] know, like when I first started hacking
[31:22] on quad code, I I realized like this
[31:23] thing just wants to use tools. It just
[31:25] wants to interact with the world. And
[31:27] how how do you how do you enable that?
[31:29] Well, the way you don't do it is you put
[31:31] it in a box and you're like, here's the
[31:33] API, here's how you interact with me,
[31:34] and here's how you interact with the
[31:36] world. The way you do it is you see what
[31:37] tools it wants to use. You see what it's
[31:39] trying to do, and you enable that the
[31:40] same way that you do for your users. And
[31:43] so, like for if you're building a dev
[31:44] tool startup, I would think about like
[31:45] what is the problem you want to solve
[31:47] for the user? And then when you use when
[31:49] you apply the model to solving this
[31:50] problem, what is the thing the model
[31:51] wants to do?
[31:52] &gt;&gt; And then what is the technical and
[31:54] product solution that serves the weight
[31:55] and demand of both? YC's next batch is
[31:58] now taking applications. Got a startup
[32:00] in you? Apply at y combinator.com/apply.
[32:04] It's never too early and filling out the
[32:06] app will level up your idea. Okay, back
[32:09] to the video. Back in the day, more than
[32:12] 10 years ago, you were a very heav heavy
[32:15] user and you wrote a book about
[32:17] TypeScript, right? Before Typescript was
[32:20] cool. This is when everyone was a deep
[32:22] in JavaScript. This is back in early
[32:24] 2010s, right?
[32:25] &gt;&gt; Yeah, something like that.
[32:27] &gt;&gt; Before Typescript was a thing because
[32:29] back then is a very weird language. It's
[32:32] not supposed to do a lot of things with
[32:34] being typed in JavaScript and now it's
[32:37] the right thing and it feels like clot
[32:39] code in the terminal has a lot of
[32:41] parallels with TypeScript at the
[32:43] beginning.
[32:44] &gt;&gt; TypeScript makes a lot of really weird
[32:47] language decisions. So if you look at
[32:49] the type system pretty much anything can
[32:51] be a literal type for example and this
[32:53] is like this is super weird cuz like
[32:55] even like like Haskell doesn't even do
[32:57] this. It's just like it's too extreme or
[33:00] it has like conditional types which I
[33:02] don't think any language thought of at
[33:04] all.
[33:05] &gt;&gt; It was like very strongly typed.
[33:06] &gt;&gt; Yeah, it was very strongly and and the
[33:08] idea was like when you know like when
[33:10] Joe Pamer and Anders and the early team
[33:12] was like building this thing, the way
[33:14] they built it is we okay, we have these
[33:16] teams with these big untyped JavaScript
[33:17] code bases. We have to get types in
[33:19] there, but we're not going to get
[33:20] engineers to change that the way that
[33:22] they code. You're not going to get
[33:23] JavaScript people to have like, you
[33:25] know, 15 layers of class inheritance
[33:27] like you would a Java programmer, right?
[33:28] They're going to write code the way
[33:29] they're going to write it. They're
[33:30] they're going to use reflection and
[33:31] they're going to use mutation and
[33:33] they're going to use all these features
[33:34] that traditionally are very very
[33:35] difficult to type.
[33:36] &gt;&gt; They're a very unsafe type to any strong
[33:38] functional programmer.
[33:40] &gt;&gt; That's right. That's right. That's
[33:41] right. And so the thing that they did
[33:42] instead of getting people to kind of
[33:44] change the way that they code, they they
[33:45] built a type system around this. And it
[33:48] was just it's brilliant because there's
[33:50] all these ideas that no one was thinking
[33:52] about even in academia like no one
[33:53] thought of a bunch of these ideas. It
[33:55] purely came out of the practice of
[33:56] observing people and seeing how
[33:58] JavaScript programmers want to write
[33:59] code. And so you know for for quad code
[34:02] it there there are some ideas that are
[34:04] kind of similar in that you know like
[34:05] you can use it like a Unix utility. You
[34:07] can pipe into it. You can pipe out of
[34:08] it. Um in some ways it is kind of
[34:10] rigorous in this way but in in almost
[34:13] every other way it's just the tool that
[34:15] we wanted. like I I build a tool for
[34:17] myself and then the team builds the tool
[34:18] for themselves and then for anthropic
[34:21] employees and then for users and it just
[34:23] ends up being really useful. It's not
[34:25] it's not this like principled and
[34:26] academic thing which I think the the
[34:29] proof is actually in the results. Now
[34:31] fast forward more than 15 years later
[34:34] not many codebases are in Haskell which
[34:36] is more academic and there's tons of
[34:39] them now on TypeScript because it's way
[34:40] more practical
[34:41] &gt;&gt; right
[34:42] &gt;&gt; which is interesting. Yeah, it is
[34:43] interesting, right? It's like TypeScript
[34:44] solves a problem.
[34:45] &gt;&gt; I guess one thing that's cool, I don't
[34:47] know how many people know, but the
[34:48] terminal is actually one of the most
[34:50] beautiful terminal apps out there and is
[34:54] actually written with React terminal.
[34:57] &gt;&gt; When I first started building it, you
[34:58] know, like I I did front-end engineering
[35:00] for for a while. So, and I was also like
[35:02] a, you know, I'm I'm sort of like a
[35:04] hybrid, like I do like design and user
[35:06] research and, you know, write code and
[35:08] all this stuff. And we love hiring
[35:09] engineers that are like this. Um, so we
[35:11] just we love generalists. So for me it's
[35:13] like okay, I'm building a thing for the
[35:14] terminal. I'm actually kind of a shitty
[35:15] Vim user. So like how do I build a thing
[35:18] for people like me that um you know are
[35:20] are going to be working in a terminal.
[35:22] And I think just the delight is so
[35:24] important. And I feel like at YC this is
[35:26] something you talk about a lot, right?
[35:27] It's like build a thing that people
[35:28] love. If the product is useful but you
[35:30] don't fall in love with it, that's not
[35:31] great. Um so it kind of has to do both.
[35:34] Designing for the terminal honestly has
[35:35] been hard, right? It's like uh it's like
[35:37] 80 by 100 characters or whatever. you
[35:39] have like 256 colors, you have one font
[35:41] size, you don't have like mouse
[35:43] interactions, there's all this stuff you
[35:45] can't do, and there's all these very
[35:46] hard trade-offs. So, like a little known
[35:48] thing, for example, is you can actually
[35:49] enable mouse interactions in a terminal.
[35:51] So, you can enable like clicking and
[35:53] stuff.
[35:53] &gt;&gt; Oh, how do you do that in cloud code?
[35:54] I've been trying to figure out how to do
[35:55] this.
[35:56] &gt;&gt; We don't we don't have it in cloud code
[35:58] because we actually prototyped it a few
[35:59] times and it felt really bad because the
[36:00] trade-off is you have to virtualize
[36:02] scrolling and so there's all these weird
[36:04] trade-offs because like the way
[36:05] terminals work is like there's no DOM,
[36:07] right? It's like there's like anti-
[36:08] escape codes and these kind of weird
[36:11] organically evolved specs since like the
[36:12] 1960s or whatever.
[36:14] &gt;&gt; Yeah. It feels like BBS's. It's like a
[36:16] BBS door game.
[36:18] &gt;&gt; That's like that's like a great
[36:19] compliment. Yeah. Yeah. Like it should
[36:20] feel like you're discovering
[36:22] &gt;&gt; Lord of the Red Dragon. It's fantastic.
[36:24] Oh my god.
[36:24] &gt;&gt; Yeah. But we have we've had to just like
[36:26] discover all these kind of UX principles
[36:28] for building the terminal cuz no one
[36:30] really writes about this stuff. And if
[36:32] you look at the big terminal apps of,
[36:34] you know, like the 80s or 90s or 2000s
[36:35] or whatever, they use like ed curses and
[36:37] they have all these like windows and
[36:39] things like this. And it just looks kind
[36:40] of like janky by modern standards. It
[36:42] just looks too heavy and complicated.
[36:44] And so we had to like reinvent a lot.
[36:46] And you know, for example, something
[36:47] like the terminal spinner, like just
[36:49] like the spinner words, it's gone
[36:50] through probably I want to say like 50
[36:54] maybe 100 iterations at this point. And
[36:56] probably 80% of those didn't ship. So we
[36:58] tried it, it didn't feel good, move on
[37:00] to the next one. try it, didn't feel
[37:01] good, move on to the next one. Uh, and
[37:03] this was like sort of one of the amazing
[37:04] things about quad code, right? Is like
[37:06] you can write these prototypes and you
[37:07] can just do like 20 prototypes back to
[37:09] back, see which one you like, and then
[37:11] ship that and the whole thing takes
[37:12] maybe a couple hours.
[37:13] &gt;&gt; Whereas in the past, what you would have
[37:14] had to do is like wen to use origami or
[37:16] framer or something like this. You built
[37:18] like maybe three prototypes, it took
[37:19] like two weeks. It just took much much
[37:21] longer.
[37:22] &gt;&gt; And so we have this luxury of we have to
[37:24] discover this new thing. We have to
[37:25] build a thing. We don't know what the
[37:26] right endpoint is, but we can iterate
[37:29] there so quickly and that's what makes
[37:31] it really easy and that's what lets us
[37:33] build a product that's like joyous and
[37:35] that people like to use.
[37:36] &gt;&gt; Boris, you had other advice for for
[37:38] builders and we kept interrupting you
[37:40] because we have so many questions, but
[37:43] &gt;&gt; I would say um so okay, so maybe two
[37:45] pieces of advice that are kind of weird
[37:48] because it's like about building for the
[37:49] model. So one is uh don't build for the
[37:52] model of today, build for the model of 6
[37:54] months from now. This is like sort of
[37:55] weird, right? Because like you can't
[37:56] find PMF if the product doesn't work.
[37:58] But actually this is the thing that you
[37:59] should do because otherwise what will
[38:00] happen is you spend a bunch of work you
[38:02] find PMF for the product right now and
[38:04] then you're just going to get leaprogged
[38:05] by someone else um because they're
[38:07] building for the next model and a new
[38:08] model comes out every few months. Use
[38:10] the model, feel out the boundary of what
[38:11] it can do and then build for the model
[38:13] that you think will be the model maybe 6
[38:15] months from now. I think the second
[38:16] thing is um you know actually in the in
[38:19] the quad code where in the quad code
[38:20] area where we sit we have a framed copy
[38:22] of the bitter lesson on the wall. Um and
[38:24] this is this like rich sutton uh I like
[38:27] everyone should read it if if you
[38:28] haven't uh and the idea is the more
[38:31] general model will always be the more
[38:33] specific model and there's a lot of
[38:35] corlaries to this but essentially what
[38:37] it boils down to is never bet against
[38:39] the model. Uh, and so this is just like
[38:41] a thing to that that we always think
[38:43] about where we could build a feature
[38:45] into cloud code. We could make it better
[38:47] as a product and we call this
[38:48] scaffolding. That's all this code that's
[38:50] not the model itself. But we could also
[38:51] just wait like a couple months and the
[38:53] model can probably just do the thing
[38:54] instead. Um, and there's always this
[38:57] trade-off, right? It's like engineering
[38:58] work now and you can kind of extend the
[39:00] capability a little bit, maybe 10 20% or
[39:02] whatever in whatever domain on this
[39:04] like, you know, like the spider chart of
[39:05] what you're trying to extend. Um, or you
[39:07] can just wait and the next model will do
[39:09] it. So just always always think in terms
[39:10] of this trade-off where where do you
[39:12] actually want to invest and assume that
[39:14] whatever the scaffolding is it's just
[39:15] tech.
[39:16] &gt;&gt; How often do you rewrite the code ways
[39:18] of uh clock code is every six months
[39:20] with this with this
[39:23] &gt;&gt; is there scaffolding that you've deleted
[39:24] because you don't need it anymore
[39:25] because the model just improved.
[39:26] &gt;&gt; Oh so much. Yeah. Like all of quad code
[39:29] has just been written and rewritten and
[39:30] rewritten and rewritten over and over
[39:31] and over. We unhip tools every couple
[39:34] weeks. We add new tools every couple
[39:36] weeks.
[39:37] There's no part of quad code that was
[39:38] around six months ago. It's just
[39:40] constantly rewritten.
[39:41] &gt;&gt; Would you say most of the code base for
[39:43] current cloud code is only say 80% of it
[39:46] is only less than a couple months old.
[39:48] &gt;&gt; Yeah, definitely. It might it might even
[39:50] be like less than Yeah, maybe like a
[39:51] couple months. That that feels about
[39:53] right.
[39:53] &gt;&gt; So it's like the life cycle of code now.
[39:55] That's another alpha is expecting it to
[39:56] be the shelf life to be just couple
[39:59] &gt;&gt; For the best founders.
[40:00] &gt;&gt; Do you see uh Steve Yaggi's uh post
[40:02] about how awesome working at Anthropic
[40:05] is? And I think there's a line in there
[40:06] that says that an anthropic engineer uh
[40:09] currently averages 1,000x more
[40:12] productivity than a Google engineer at
[40:15] Google's peak which is really an insane
[40:19] number honestly like 1,000x like you
[40:22] know we're 3 years ago we were still
[40:23] talking about 10x engineers now we're
[40:25] talking about 1000x on top of a Google
[40:27] engineer in the prime like this is
[40:29] unbelievable honestly. Yeah, I mean
[40:31] internally if you if you look at like
[40:32] technical employees, they all use quad
[40:34] code every day. Um, and even
[40:36] non-technical employees, I think like
[40:37] half the sales team uses quad code. Um,
[40:39] they they've started switching to
[40:41] co-work because it's a little easier to
[40:42] use. It has like a VM, so it's a little
[40:44] bit safer. But yeah, we actually we just
[40:45] pulled a stat and the I think the team
[40:48] doubled in size last year, but
[40:50] productivity per engineer grew something
[40:52] like 70%.
[40:53] &gt;&gt; It's measured by
[40:54] &gt;&gt; just like the simplest stupidest
[40:56] measure, pull requests. Um, but we also
[40:57] kind of cross check that against like
[40:59] commits and like uh the lifetime of
[41:00] commits and things like this. And since
[41:02] quad code came out, productivity per
[41:04] engineer at anthropic has grown 150%.
[41:07] &gt;&gt; Um, and this is crazy because I in my
[41:10] old life I was responsible for code
[41:12] quality at Meta.
[41:13] &gt;&gt; Um, and I was responsible for the
[41:14] quality of all of our code bases across
[41:16] every product across like you know
[41:17] Facebook, Instagram, WhatsApp, whatever.
[41:20] &gt;&gt; And one of the things that the team
[41:22] worked on was improving productivity.
[41:24] And back then seeing a gain of something
[41:26] like 2% in productivity that was like a
[41:28] year of work by hundreds of people. And
[41:30] so this like 100% this is just like
[41:33] unheard of just completely unheard of.
[41:35] &gt;&gt; What drove you to come over to
[41:36] Anthropic? I mean basically as a builder
[41:38] you could go anywhere. What was the
[41:40] moment that made you say like actually
[41:42] this is the set of people or this is the
[41:44] approach. I was living in rural Japan
[41:47] and I was opening up Hacker News every
[41:50] morning and I was reading the news and
[41:52] uh it was all it just started to be like
[41:54] AI stuff at some point and uh I started
[41:57] to use some of these early products and
[41:59] uh I remember like the first couple
[42:00] times that I used it I was just like it
[42:02] just took my breath away. That was like
[42:04] very cheesy to say, but that was
[42:05] actually that was actually the feeling.
[42:06] Like it was just like it was amazing
[42:08] like as a as as a builder, I've just
[42:11] never kind of felt felt this feeling
[42:12] like using these very very early
[42:14] products. That was like in the quad 2
[42:15] days or you know something like that.
[42:17] And so I I just talking started talking
[42:19] to friends at Labs um just to kind of
[42:21] see what was going on. Um and uh I met
[42:25] Ben man who's one of the founders at uh
[42:27] at Anthropic and uh he just immediately
[42:30] won me over. Um and as soon as I met
[42:32] kind of the rest of the team at an it
[42:33] just won me over and I think I think
[42:35] probably in two ways. So one is it
[42:36] operates as a research lab. Um so the
[42:40] product was teeny teeny tiny. It's
[42:42] really all about building a safe model.
[42:44] That's all that matters. Um and so this
[42:46] idea of just being very close to the
[42:47] model and being very close to
[42:48] development and being not the most
[42:51] important thing because the product
[42:52] isn't anymore. It's just the model is
[42:54] the thing that's the most important. Um
[42:56] that really resonated with me after
[42:58] building product for many years. And
[42:59] then the second thing was just how
[43:01] missiondriven it is. Um like I'm I'm a
[43:04] huge sci-fi reader. My bookshelf is just
[43:05] like filled with sci-fi. And so like I
[43:08] just know how bad this can go.
[43:10] &gt;&gt; And when I kind of think about what's
[43:11] going to happen this year, it you know
[43:13] it's going to be totally insane. And in
[43:15] the worst case it can go very very bad.
[43:17] &gt;&gt; Um and so I just wanted to be at a place
[43:19] that really understood that and kind of
[43:20] really internalized that. And at Ant,
[43:23] you know, like if you overhear
[43:24] conversations in the lunchroom or in the
[43:26] hallway, people are talking about AI
[43:27] safety. this is really the thing that
[43:30] everyone cares about more than anything.
[43:32] Um, and so I just wanted to be in a
[43:33] place like that. I I know I know for me
[43:35] personally the mission is just so
[43:36] important.
[43:37] &gt;&gt; What is gonna happen this year?
[43:40] &gt;&gt; Okay. So if you think back like six
[43:42] months ago and uh kind of what are the
[43:44] predictions that people are making? So
[43:45] Daario predicted that 90% of the code at
[43:48] Anthropic would be would be written by
[43:50] Quad. This is true. Um for me personally
[43:52] it's been 100% for like since Opus 4.5.
[43:56] Um I just I uninstalled my IDE. I don't
[43:59] edit a single line of code by hand. It's
[44:00] just 100% quad code and Opus. Um and you
[44:04] know I land you know like 20 PR a day
[44:05] every day. If you look at Enthropic
[44:07] overall it ranges between like 70 to 90%
[44:11] uh you know depending on the team. For a
[44:12] lot of teams it's also like 100% for a
[44:14] lot of people it's 100%. And I remember
[44:16] making this prediction back in May when
[44:18] we ged cloud code that you wouldn't need
[44:21] an ID to code anymore. Uh and it was
[44:24] totally crazy to say. I feel like people
[44:25] in the audience gasped
[44:27] &gt;&gt; because it was such like a silly
[44:28] prediction at the time. But really all
[44:29] it is is like you just like trace the
[44:31] you know the exponential
[44:32] &gt;&gt; and this is just like so deep in you
[44:34] know the DNA at cuz like you know three
[44:36] of our founders were co-authors of the
[44:38] scaling laws paper they kind of they saw
[44:40] this very early and so this is just like
[44:42] tracing the exponential this is what's
[44:43] going to happen and yes that happened.
[44:45] So continuing to trace the exponential I
[44:47] think what will happen is coding will be
[44:49] generally solved for everyone. Um, and I
[44:52] think today coding is practically
[44:53] solved, you know, for me and I think
[44:54] it'll be the case for everyone. Um, you
[44:56] know, regardless of domain, I think
[44:58] we're going to start to see the title
[44:59] software engineer go away. And I think
[45:01] it's just going to be maybe builder,
[45:03] maybe product manager, maybe we'll keep
[45:05] the title as kind of a vestigial thing,
[45:07] but the work that people do, it's not
[45:09] just going to be coding. It's software
[45:10] engineers are also going to be writing
[45:12] specs. They're going to be talking to
[45:13] users. like this thing that we're
[45:15] starting to see right now in our team
[45:16] where engineers are very much
[45:18] generalists and every single function on
[45:21] our team codes like our PM's code, our
[45:22] designers code, our EM codes, our um
[45:26] like everyone our our finance guy codes
[45:28] like everyone on our team codes. We're
[45:30] going to start to see this everywhere.
[45:31] So this is sort of uh this is kind of
[45:33] like the lower bound if we just continue
[45:35] the trend. The upper bound I think is a
[45:38] lot scarier. Um, and this is something
[45:40] like, you know, we hit ASL4. Um, and
[45:42] this, you know, at anthropic, we talked
[45:43] about these safety levels. ASL3 is where
[45:46] the models are right now. ASL4 is the
[45:48] model is recursively self-improving. Um,
[45:50] and so if this happens, essentially, we
[45:51] have to meet a bunch of criteria before
[45:53] we can release a model. And so the the
[45:55] extreme is that, you know, this happens
[45:57] um or there's some kind of catastrophic
[45:58] misuse like people are using the model
[46:00] to design bioiruses, design zero days,
[46:03] stuff like this. Um, and this is
[46:05] something that we're really really
[46:06] actively working on so that doesn't
[46:07] happen. I think uh it's just been
[46:10] honestly it's just been like so exciting
[46:11] and humbling like seeing how people are
[46:13] using quad code like uh you know I just
[46:15] wanted to build a cool thing and it
[46:17] ended up being really useful uh and that
[46:19] was so surprising and so exciting.
[46:21] &gt;&gt; My impression from Twitter or just the
[46:23] outside is basically everyone went away
[46:25] over the holidays and then like found
[46:26] out about Claude code and it's just been
[46:28] crazy ever since. Is that how it was for
[46:30] you at like internally? Did you were you
[46:33] having like a nice Christmas break and
[46:35] then came back and like what happened?
[46:37] Well, actually for all of December, I
[46:38] was traveling around. Uh, and I I took a
[46:40] coding vacation. So, we were kind of
[46:42] traveling around and I was just like
[46:43] coding every day. So, that was really
[46:44] nice. Uh, and then I also started to use
[46:46] Twitter at the time cuz like I I worked
[46:48] on Threads back then way back when. So,
[46:50] I've been a Threads user for a while.
[46:52] So, I just like tried to see kind of
[46:53] like other platforms where people are.
[46:55] Yeah. I think for a lot of people they
[46:56] kind of discovered that was the moment
[46:58] where they discovered Opus 4.5. I kind
[46:59] of already knew.
[47:00] &gt;&gt; Mhm.
[47:01] &gt;&gt; Uh, and internally quad code's just been
[47:02] on this like exponential tear for many
[47:05] many months now. So that just like it it
[47:07] became even more steep. That's what we
[47:09] saw. And if you look at cloud code now,
[47:12] you know, there was some stat from
[47:13] Mercury that like 70% of startups are
[47:15] you know choosing cloud as their model
[47:17] of choice. There was some other stat
[47:19] from like semi analysis that 4% of all
[47:21] public commits are made by cloud code.
[47:23] um like of all code written everywhere.
[47:26] All the companies, you know, use squad
[47:27] code from like the biggest companies to
[47:29] kind of, you know, smallest startups,
[47:31] you know, like it it wrote it it plotted
[47:33] the course for Perseverance like for
[47:35] like the Mars rover. This is just like
[47:37] this is the coolest thing for me. And we
[47:38] like we even printed posters cuz the
[47:40] team was like, "Wow, this is just like
[47:41] so cool that NASA chooses to use this
[47:43] thing." So, yeah, it's just like it's
[47:44] humbling. Um but it also feels like the
[47:46] very beginning. What's the sort of
[47:48] interaction between uh claude code and
[47:50] then co-work like you know was it a fork
[47:53] of cla code? Was it like you had cla
[47:56] code look at the cloud code and say
[47:59] let's make a new spec for nontechnical
[48:02] people that you know keeps all the
[48:03] lessons and then you know it sort of
[48:05] went off for a couple days and did that.
[48:07] What's the genesis of that and you know
[48:09] where do you think that goes?
[48:11] &gt;&gt; This is going to be like my fifth time
[48:12] using the word wait and demand.
[48:15] It was just that I mean like we we were
[48:16] looking at Twitter and there was like
[48:17] that one guy that was using quad code to
[48:19] like monitor his tomato plants.
[48:21] &gt;&gt; Uh there was like this other person that
[48:23] was using it to like recover wedding
[48:24] photos off of a corrupted hard drive.
[48:26] There were people that using it for like
[48:28] uh for finance. When we looked
[48:30] internally at anthropic, every designer
[48:32] is using it all the entire finance team
[48:34] at this point is using it. The entire
[48:36] data science team is using it not for
[48:37] coding. People are jumping over hoops to
[48:39] install a thing in the terminal so that
[48:41] they could use this. So we knew for a
[48:42] while that we wanted to build something
[48:43] and so we're experimenting with a bunch
[48:45] of different ideas and the thing that
[48:47] kind of took off was just you know a
[48:49] little cloud code wrapper in a guey in
[48:50] the desktop app and that's all it is.
[48:52] It's just quad code under the hood. It's
[48:53] the same agent.
[48:54] &gt;&gt; Oh wow.
[48:55] &gt;&gt; Um and uh Felix and the team and Felix
[48:58] was early Electron contributor. He kind
[49:00] of knows that stack really well and he
[49:01] was hacking on various ideas and uh they
[49:04] they built it in I think something like
[49:06] 10 days. It was it was just like 100%
[49:08] written by quad code. Uh and it just
[49:10] felt ready to release. There was a lot
[49:12] of stuff that we had to build for
[49:14] nontechnical users. So it's a little bit
[49:15] different than a technical audience. Uh
[49:18] it runs in a all the code runs in a
[49:20] virtual machine. Uh there's a lot of
[49:22] delete uh protections for deletion and
[49:24] things like this. There's a lot of
[49:26] permission prompting and kind of other
[49:27] guardrails for users. Um yeah, it was
[49:31] honestly pretty obvious. Boris, thank
[49:33] you so much for making something that uh
[49:35] is taking away all my sleep, but in
[49:38] return, it's making me feel creator mode
[49:40] again, sort of founder mode again. It's
[49:42] been an exhilarating 3 weeks. I like
[49:45] can't believe I waited that long since
[49:46] November to actually get into it. Thank
[49:48] you so much for being with us. Thank you
[49:50] for building what you're building.
[49:52] &gt;&gt; Yeah, thanks for having me. And uh send
[49:54] bugs.
[49:56] &gt;&gt; Sounds good.
[49:59] Come
[50:01] on now.
