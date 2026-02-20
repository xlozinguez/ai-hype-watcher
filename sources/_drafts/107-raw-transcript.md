[00:00] Anthropic just released a marketing
[00:01] video proving that Claude, their
[00:03] flagship programming model, can produce
[00:06] a C compiler from scratch, no human
[00:10] intervention, and they can do it in
[00:12] parallel. And it can compile Linux,
[00:15] SQLite, Reddus, Lua,
[00:19] and even Doom. Hey, what's with the
[00:22] frame rate? This is going to be a weird
[00:23] video because I'm going to say something
[00:25] positive about Anthropic. And then I'm
[00:28] also gonna call Anthropics one of the
[00:30] most deceitful companies I have ever
[00:32] seen. This little product demo that they
[00:35] did, the language inside the video, it
[00:37] is the most dishonest framing of what
[00:40] they actually did versus what they're
[00:42] saying they did. Anthropic and its
[00:44] non-stop hyping of the AI models is
[00:46] perhaps one of the most annoying
[00:48] features of 2025 and it's coming into
[00:51] 2026 with a whole new level of rigor and
[00:54] completeness. All right, so let's go
[00:56] over what they did, what the actual cool
[00:58] part, and actually why what they did was
[01:01] complete hype nonsense. So don't worry,
[01:04] it's not over. You don't have to pack it
[01:06] up. Software engineering is in fact not
[01:09] over quite yet. Now, that video that you
[01:11] just got done seeing, there's so many
[01:12] lies into it. So, we're going to just
[01:13] try we're going to try our best to kind
[01:15] of take apart the lie. So, first off,
[01:19] the thing that they were actually
[01:20] building was trying to see, can they get
[01:22] Claude to run by itself long enough to
[01:25] produce a functional piece of software.
[01:27] Functional, of course, just means that
[01:29] it can do what it says it does,
[01:32] regardless of how good it does it. Long
[01:34] as at the end of the day, you say do X,
[01:37] it does X. you compile Linux, it should
[01:40] produce Linux as an artifact. Also, put
[01:42] a little star on that because that even
[01:43] that not so true. All right, the article
[01:46] kind of kicks off with to test it. Now,
[01:49] it being this multi- aent harness to be
[01:52] able to have Claude run autonomously for
[01:54] multiple weeks. I task 16 agents with
[01:56] writing a Rustbased C compiler from
[01:58] scratch capable of compiling the Linux
[02:00] kernel. Over nearly 2,000 cloud code
[02:02] sessions and $20,000 worth of API cost.
[02:05] The agent produced a 100,000 line
[02:07] compiler that can build Linux 6.9 on x86
[02:10] ARM and risk 5. Again, there's no
[02:13] asterisk. So, what are these so-called
[02:15] asterisks? Well, first off, I don't know
[02:17] if you know this, but GCC, which is what
[02:20] they're basing this off of, not only is
[02:22] it open source, which means that they've
[02:24] already trained on top of it. And we all
[02:26] know if in case you didn't know that uh
[02:28] these models, you can produce nearly
[02:30] perfect identical copyright works back
[02:32] out of them if you can convince them to
[02:34] produce it. Like this one right here
[02:35] showing that Claude 37 can produce 95.8%
[02:38] of the first book of Harry Potter.
[02:40] Almost a near verbatim reproduction. But
[02:43] Anthropic in its in its wisdom when
[02:45] starting from scratch, scratch meant 37
[02:48] years of developed torture test suite
[02:51] from GCC. Yes, you know this classic way
[02:53] of doing software development. Usually
[02:55] when I start a new project, I first get
[02:57] handed 37 years of prior art in which
[03:00] contains the perfect golden test suite
[03:02] so that I can test my new project in
[03:05] every conceivable way possible. And then
[03:07] on top of it, I have the actual working
[03:10] version of the thing I'm about to build
[03:12] that I can also test my working version
[03:14] against. And that's known as the online
[03:16] Oracle. As we as we say in this software
[03:19] biz. Also, when I say it can compile
[03:21] Linux from scratch, I want you to
[03:23] understand that it lacks a 16bit x86
[03:26] compiler necessary to boot Linux out of
[03:28] the real mode. That's because Opus was
[03:30] unable to implement a 16-bit x86 code
[03:33] generated needed to boot into 16-bit
[03:35] real mode. While the compiler can output
[03:37] the correct 16-bit x86 via the 66 and 67
[03:41] op code prefixes, the resulting compiled
[03:44] output is over 60KB, far exceeding the
[03:46] 32K code limit enforced by Linux. See,
[03:49] it's honestly it's Linux's fault. Like,
[03:51] they have this stupid 32bit maximum
[03:54] number on. It's not my fault. I'm not
[03:57] holding it wrong. It's Lionus. He's
[03:59] holding it wrong. All right. So to say
[04:01] that all in a quick sentence, they
[04:03] started a project from scratch having
[04:05] every single conceivable test and a way
[04:07] to test it under all conditions. They
[04:10] had an online version of it, GCC online,
[04:12] to be able to call out to to validate
[04:14] everything they've done. And lastly,
[04:16] they couldn't actually make Linux boot
[04:18] because they were unable to produce an
[04:20] artifact small enough. So they built a
[04:22] compiler completely from scratch in two
[04:24] weeks and they just had to walk away.
[04:26] Okay. They also couldn't walk away
[04:28] during those two weeks because sometimes
[04:29] it did things and it would crash itself
[04:31] and we had to restart it and make sure
[04:33] things were working. Now, that's what I
[04:34] call from scratch. And this is exactly
[04:37] what I mean by dishonesty. Like look at
[04:39] that. You saw the video in the
[04:42] beginning. It's like yeah dude we said
[04:44] hey Claude you'll build this from
[04:46] scratch. Walked away two weeks later.
[04:49] Linux was working. SQL light was
[04:52] working. Reddus was working. And yeah,
[04:55] we even played Doom, loser. This is not
[04:58] from scratch. There's no from scratch,
[05:01] no human intervention that don't just
[05:04] just say what you did. Like, okay, so
[05:06] the real takeaway, which everybody
[05:08] should have, which is what is triggering
[05:09] me and making me so angry again at
[05:12] Anthropic, is that the real cool thing
[05:15] is that they figured out how to get 16
[05:17] agents to mostly run by themselves for
[05:19] two weeks straight and actually produce
[05:20] something given the correct guidelines
[05:22] at the end of the day. Hey, that's
[05:24] pretty cool. It's a pretty large
[05:26] project. It shows that models are in
[05:28] fact improving and can handle kind of
[05:30] context up to this size and able to kind
[05:32] of work together given the right
[05:34] orchestration. Like that's a neat
[05:36] takeaway, but that's not what they said.
[05:38] And that of course is driving me nuts.
[05:41] Which of course led to hilarious issues
[05:42] on GitHub. Like the very first issue,
[05:44] hello world does not compile cuz it
[05:46] turns out the example program that they
[05:48] put in their readme does not compile.
[05:51] Sorry, that doesn't compile. You didn't
[05:53] provide the linker, bro. You idiot.
[05:55] Okay, CCC is not like GCC. It only is
[05:57] the compiler. It's not an assembler or
[05:59] linker. Okay, you think you just get
[06:01] those for free, buddy? Which, by the
[06:02] way, there's like 300 and some comments
[06:05] on here of just people arguing back and
[06:07] forth. Oh my gosh, it is just a actual
[06:11] It's a claw slot mess in there. Okay,
[06:13] and of course, I'm not the only person
[06:15] saying this. There are some other people
[06:17] saying, "Hey, this is kind of
[06:18] ridiculous. This is a little out of like
[06:21] out of pocket here calling this from
[06:23] scratch and no human intervention. So,
[06:25] at the end of the day, this could have
[06:26] been an article about how we got Claude
[06:28] to run for multiple weeks and produce
[06:30] something with very little to almost
[06:32] none uh human interaction and being able
[06:34] to fulfill a spec. But instead, it
[06:36] became a spectacle about how Anthropic
[06:39] yet again is completely dishonest. This
[06:42] is just another example of the AI hype
[06:44] cycle. They're just here to try to raise
[06:46] money and to take every piece of novel
[06:49] work possible and sell it back to you.
[06:50] Now, this is a future I'm personally
[06:54] excited about. Am I right? Let's go. Oh
[06:57] my gosh. The name is anthropic. If you
[07:00] were just like a little bit more honest
[07:02] about what you're doing, honestly, I
[07:03] think a lot of people would be much more
[07:05] excited about it and probably cheer you
[07:06] on from the sideline. I think you have a
[07:08] lot of potential. Your models are pretty
[07:10] good. There's a lot of cool stuff about
[07:12] AI. We don't have to be AI haters, but
[07:14] sometimes you just say the stupidest
[07:17] crap ever and just do the stupidest
[07:19] stuff and make everybody hate you. How
[07:20] about you just don't do that anymore?
[07:22] Hey, you know what? I will give you my
[07:24] service for free the next time you
[07:25] decide to release another marketing
[07:27] video. Just let me watch it and read
[07:29] your article right I'll do it for free
[07:31] for you. Okay, Daario. Okay. And maybe
[07:34] we could frame this with a crazy radical
[07:37] idea. Honesty. I know. It's a whole new
[07:41] novel concept. A gen. Hey, is that HTTP?
[07:45] Get that out of here. That's not how we
[07:47] order coffee. We order coffee via SSH
[07:50] terminal.shop. Yeah. You want a real
[07:52] experience? You want real coffee? You
[07:54] want awesome subscriptions so you never
[07:56] have to remember again? Oh, you want
[07:58] exclusive blends with exclusive coffee
[08:00] and exclusive content? Then check out
[08:03] Kron. You don't know what SSH is?
[08:06] &gt;&gt; Well, maybe the coffee is not for you.
[08:08] Terminal [singing]
[08:09] coffee [music]
[08:11] in hand.
[08:13] Living the dream.
