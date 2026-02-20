[00:00] This video is going to sound like I
[00:01] really dislike chord code, and I do. But
[00:04] honestly, even if all it can do is
[00:06] rewrite existing software, but worse and
[00:09] in Rust, then there is no doubt that it
[00:11] will replace most modern developers.
[00:13] Over the course of 2 weeks, a team of
[00:15] clawed code agents built a C compiler
[00:18] from scratch. Let's get one thing out of
[00:20] the way first. Of course, it can compile
[00:22] hello world. This controversial issue is
[00:24] just 100% user error. If I do exactly
[00:27] what the readme says using Linux and
[00:29] compiling the program with cargo, I can
[00:31] run the exact command that's prescribed
[00:34] and you can clearly see that it doesn't
[00:36] work. Well, you know, that's not fair.
[00:39] It's not actually an issue with the
[00:40] compiler. The standard library should
[00:42] just be available. Take Wreck for
[00:44] example, another C compiler written in
[00:46] Rust with no dependencies. It was made
[00:48] by a solo dev in his spare time. And
[00:50] when I follow the same process, it will
[00:52] obviously run into the same issue that
[00:54] Claude did. Yeah. Okay, it works
[00:56] completely fine, but that's that's not
[00:58] fair. How's Claude supposed to know
[01:00] where the sanded library is? It's only
[01:02] been in the same spot for 20 years.
[01:04] Anyway, this is kind of embarrassing for
[01:06] Claude, but it's a reasonable mistake
[01:08] and not a good enough reason to throw
[01:10] away the whole compiler. Once the
[01:12] dependencies are set up correctly, it
[01:14] can genuinely compile hello world and
[01:16] the Linux kernel, which is by no means
[01:18] an easy feat and something that Wreck is
[01:20] unable to do. I found this guide showing
[01:22] you how to compile the Linux kernel. I'm
[01:25] using the version of Linux that claude
[01:26] code used and according to this text
[01:28] file in the repo I can run the same
[01:30] commands but change for C compiler by
[01:32] setting the CC and host CC variables.
[01:35] The first make to create the config
[01:37] works correctly but the main make the
[01:40] one that I assume builds for kernel
[01:42] returns an error from CCC that saysov
[01:45] requires two operants got one. And look,
[01:48] I'm not some kind of assembly genius,
[01:51] but to me it sounds like the compiler
[01:53] couldn't even create correct syntax for
[01:55] assembly, which is impressive because
[01:58] assembly probably has the simplest
[01:59] syntax of any language. It's just a
[02:02] keyword followed by one or two
[02:04] variables, but it somehow managed to get
[02:06] that wrong. I'll be honest though, I'm
[02:08] not familiar with building Linux from
[02:10] source, so I'm willing to admit that I
[02:11] may have done something wrong. But come
[02:13] to think of it, I haven't seen a single
[02:15] person use this to compile the Linux
[02:17] kernel and then use that to actually run
[02:19] Linux. I ran into an assembly issue.
[02:22] This guy ran into a linking issue and
[02:23] gave up. And this other person testing
[02:25] the compiler didn't even use it with the
[02:27] Linux kernel. When the guy recreated
[02:29] Coke from scratch, it took 2 days for
[02:31] someone to reproduce the same recipe in
[02:33] their backyard. But I still haven't seen
[02:35] anyone use this public GitHub repository
[02:38] to do the exact thing that it's marketed
[02:40] as doing. Are we really just going to
[02:42] believe these claims when the example in
[02:45] the readme doesn't even work for most
[02:46] modern Linux distros? If there is an
[02:49] example of someone doing this, please
[02:50] let me know because I would love to see
[02:52] it. Okay, so I had another look while
[02:54] editing and I did find someone who
[02:56] managed to compile and run Linux, but
[02:59] that's using risk 5 and a VM. So I don't
[03:01] know if it's an x86 issue. If it is,
[03:04] maybe they just shouldn't put that in
[03:06] the repo description. I might still be
[03:09] missing something and it is possible to
[03:10] compile it on x86. So if there is, I'll
[03:13] just leave that in the pin comment. But
[03:16] for now, let's assume that
[03:17] hypothetically it does compile the Linux
[03:20] kernel as advertised. This whole
[03:22] compiler is still completely useless.
[03:25] This is the perfect project for an LLM
[03:27] to tackle. It's impressive and somewhat
[03:29] novel, but it's very well doumented with
[03:32] many examples across different languages
[03:34] in the training set. Saying that this
[03:36] compiler only cost $20,000 to make is
[03:39] disingenuous in my opinion since it's
[03:41] not factoring in the thousands of hours
[03:43] that were spent writing tests that
[03:44] happen to be useful for this exact use
[03:47] case. Tests that other projects simply
[03:49] won't have. Claude got to use many
[03:51] existing test suites for GCC and for C
[03:54] programs like SQLite and Postgress all
[03:56] for free. tests that you would have to
[03:58] spend time writing if you were actually
[04:00] creating a new project with additional
[04:02] tests that the researchers had to write
[04:04] when it still kept getting stuck. And
[04:06] when that didn't work, they just gave up
[04:08] and let it see what GCC does so that it
[04:10] could copy that. And even then, it's
[04:12] barely functional. I cannot believe that
[04:14] Enthropic published this blog post,
[04:16] especially with all the details of how
[04:18] this just did not work at all. This is
[04:21] not a usable compiler, and even when it
[04:23] does compile, it's mind-numbingly slow.
[04:26] I mentioned Hashanu's blog post before.
[04:28] He took some time to benchmark SQLite
[04:30] when compiled with GCC and with Claude C
[04:33] compiler. It managed to compile SQLite
[04:35] because SQLite is one of the simplest C
[04:37] projects to compile ever created. Simple
[04:40] queries are up to seven times slower.
[04:42] But the real banger is this nested
[04:44] subquery that takes 4700th of a second
[04:47] in GCC but over 2 hours with Claude's
[04:50] compiler. That's a 158,129
[04:54] times increase. I'm cherry-picking the
[04:56] worst offender, but come on, how is that
[04:58] even possible? And sometimes the joints
[05:01] also just don't work. So, not sure about
[05:03] that one. And good luck fixing that
[05:05] because the codebase is now at a point
[05:07] where Claude cannot make new changes
[05:09] without breaking existing functionality.
[05:11] Anthropic has written in plain words
[05:14] what our future will look like if we go
[05:16] down this path, and some still treat
[05:18] this as a massive success. There is no
[05:20] reason to use this project. It provides
[05:23] no benefit over the existing compiler.
[05:25] And I think this is the perfect
[05:26] representation of what LLM coding feels
[05:29] like. It's expensive, confusing, and at
[05:32] the end, you're left with something
[05:33] that's somehow even worse than when you
[05:35] started. And even with every single
[05:37] advantage it had, this project still
[05:39] serves no purpose. In fact, I'm going to
[05:42] create an even better cla compiler named
[05:45] BCC. And it's going to take 2 minutes
[05:47] instead of two weeks. I'm using codeex
[05:49] because that's what I've been given a
[05:51] license for, but they're all the same.
[05:53] My compiler is just a simple bash
[05:55] script. I write a prompt that tells the
[05:57] LLM to guess what the project is based
[05:59] off the source file names, generate C
[06:02] files, and then compile it using GCC.
[06:04] This compiler successfully compiles
[06:07] Hello World with no issues first try.
[06:09] And if you just believe me without
[06:10] trying it yourself, it also compiles the
[06:13] Linux kernel in record time, I might
[06:15] add. meaning this compiler is better or
[06:17] at least equivalent to Claude's original
[06:20] C compiler. But none of this even
[06:22] matters. LLMs will still become
[06:24] ubiquitous. As developers, we have shown
[06:27] an unnerving determination to make the
[06:29] wrong choice at every conceivable
[06:32] opportunity. We did it with JavaScript
[06:34] in the browser. We did it with cloud
[06:35] computing. We did it with frameworks.
[06:37] And it will be the same story with LMS.
[06:40] The initial velocity increase and
[06:42] marketing hype is enough for people to
[06:44] convince themselves that this is a good
[06:46] decision. Despite the clear evidence
[06:48] that these short-term benefits are far
[06:50] outweighed by the long-term trade-off,
[06:52] the majority of developers will spend
[06:54] most of their time vibe coding. But the
[06:57] whole system will not collapse. It will
[06:59] just get worse. There will be more bugs
[07:01] and more security vulnerabilities and
[07:04] everything will break and users will
[07:06] just live with it and it will become the
[07:08] new normal. I actually predict
[07:09] programming jobs will go up since our
[07:11] industry has a history of creating
[07:13] terrible practices and then compensating
[07:15] by hiring magnitudes more developers.
[07:18] You'd be forgiven for forgetting that
[07:19] the mythical man month was released in
[07:21] 1975, more than 50 years ago. And it's
[07:25] sad to be a programmer in a world where
[07:27] everything we do is a broken mess and
[07:29] nobody cares. But just when I was about
[07:31] to give up all hope, the man, the myth,
[07:34] the legend, the Sha Barrett has decided
[07:37] to start streaming again. This guy was
[07:39] writing CC code in Visual Studio 6
[07:42] before I was born. And you can bet that
[07:44] he's writing CC code in Visual Studio 6
[07:46] today. And that's what I love about
[07:48] software. Everything always changes.
[07:50] Tools and technologies come and go. But
[07:53] at the end of the day, it all compiles
[07:55] to the same assembly and runs on the
[07:57] same CPU. Well, it doesn't always
[07:59] compile to the same assembly. You should
[08:01] just use GCC.
[08:05] Thank you for watching. And I'm supposed
[08:08] to say that you have to smash the
[08:10] subscribe button. I don't know what that
[08:11] means. Got to smash it. Smash the
[08:15] button. Smash the subscribe button. SM.
