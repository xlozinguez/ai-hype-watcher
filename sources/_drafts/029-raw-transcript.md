---
source_id: "029"
title: "We Studied 150 Developers Using AI (Here's What's Actually Changed...)"
creator: "Modern Software Engineering"
url: "https://www.youtube.com/watch?v=b9EbCb5A408"
extracted: "2026-02-12"
method: "yt-dlp"
segments: 285
---

[00:00] AI coding tools are everywhere now.
[00:03] GitHub Copilot, Cursor, Claude Code,
[00:06] Chat, GPT, and those are just the ones
[00:09] beginning with the letter C. We're told
[00:11] they make us faster, more productive,
[00:13] more efficient. But there's a much more
[00:15] important question that fewer people
[00:17] seem to ask. What happens after the AI
[00:20] has written the code? What happens when
[00:22] the next developer has to understand it?
[00:25] When the code has to be changed? When it
[00:27] has to be maintained? Does AI help with
[00:29] this or are we busy creating an AI slop
[00:33] driven maintenance nightmare? That's our
[00:35] topic for today.
[00:44] Hi, I'm Dave Farley and welcome to the
[00:46] modern software engineering channel. If
[00:48] you haven't been here before, please do
[00:50] hit subscribe and if you enjoy the
[00:53] content here today, hit like as well.
[00:55] Maintainability is so important because
[00:58] it is maintenance and not the initial
[01:01] development that is the dominant cost in
[01:03] software development. It's largely naive
[01:06] nonsense to imagine that you can develop
[01:08] software once and then never revisit
[01:11] again. Estimates range widely, but it's
[01:14] generally assumed that maintenance costs
[01:16] somewhere between three to four times
[01:19] more than the initial cost of
[01:21] development over the lifetime of a
[01:22] software system. with maintenance
[01:24] representing 50 to 80% of the total cost
[01:27] of ownership.
[01:29] Most of the money, time, and risk in
[01:31] software then happens after the first
[01:34] version has shipped. This is one of
[01:36] several reasons why developing software
[01:38] that's easy to maintain, easy to change,
[01:41] makes commercial sense. While optimizing
[01:44] for short-term dumb metrics like feature
[01:47] count is a rather silly tradeoff. Yet
[01:50] most AI studies stop at did the software
[01:54] developer finish faster? Did they type
[01:56] fewer characters? That's not
[01:58] engineering. That's measuring typing
[02:00] speed. So when I was asked to help with
[02:03] a pre-registered controlled experiment
[02:06] that actually looked at downstream
[02:08] maintainability, I paid attention. And
[02:11] yes, full disclosure here, I am one of
[02:13] the authors, though I confess that the
[02:16] other people did all of the real work,
[02:18] not me. I helped contribute some initial
[02:20] ideas very early on, and I helped the
[02:23] researchers to find experimental victims
[02:25] via this channel. Some longtime viewers
[02:27] may remember the episode.
[02:31] The research is now published, though,
[02:33] so let's take a look at the findings now
[02:35] that we have evidence on the table. This
[02:38] wasn't a toy experiment. In fact, it's
[02:40] one of the more thorough looks at the
[02:42] impact of AI on software development so
[02:45] far. It involved 151 participants with
[02:50] 95% of them being professional software
[02:52] developers. This is unusual. Most
[02:54] studies are based on students because
[02:56] they're usually easier to recruit. Our
[02:59] research asked these professionals to
[03:01] create and maintain a realistic Java web
[03:04] application in two carefully controlled
[03:07] phases. Phase one, developers were asked
[03:10] to add a feature to some rather
[03:12] unpleasant buggy code. Some using AI
[03:15] assistants, some not. Phase two, a
[03:18] different set of developers were then
[03:20] randomly assigned code produced in phase
[03:22] one and asked to evolve it without
[03:25] knowledge of whether it was originally
[03:27] written with the help of AI or not. No
[03:30] AI assistance was allowed in phase two.
[03:32] That's the key. We're not measuring how
[03:34] fast the same person works with AI.
[03:37] We're measuring how easy the code is for
[03:40] someone else to change it later on.
[03:42] That's a much better proxy for
[03:44] maintainability and generally for code
[03:46] health. The research was meant to
[03:48] simulate a more realistic, broader view
[03:51] of real world development in practice
[03:53] and measure the impact of AI assistance
[03:56] on that. Let me pause there and say
[03:59] thank you to our sponsors. We're
[04:01] extremely fortunate to be sponsored here
[04:03] by Equal Experts, Transfic, and Octopus
[04:07] Deploy. Equal Experts is a multinational
[04:10] consultancy built on applying the ideas
[04:12] and techniques that we talk about here
[04:14] to build great software for their
[04:16] clients. All of these companies offer
[04:19] products and services though that are
[04:20] very well aligned with the topics that
[04:22] we discuss on this channel every week.
[04:24] So if you're looking for excellence in
[04:26] continuous delivery and software
[04:27] engineering, do click on their links in
[04:29] the description below and check them
[04:31] out. The research that we're talking
[04:34] about here was conducted with the aim of
[04:36] controlling the variables where we
[04:38] could. So the researchers didn't just
[04:40] guess, they measured. They measured how
[04:43] long the next developer took to evolve
[04:45] the code. The objective code quality
[04:47] based on code scenes code health metric.
[04:50] There are links to that in the
[04:51] description below. test coverage and
[04:54] perceived productivity using the space
[04:57] framework also linked in the description
[04:59] below. This range of measures is
[05:01] important because maintainability is so
[05:03] multi-dimensional. There isn't just one
[05:05] magic number and anyone claiming that
[05:07] there is should probably be treated with
[05:09] a little bit of suspicion. So what did
[05:11] we find? Well, the headline is there was
[05:15] no significant difference between the
[05:17] cost of maintenance between AI and human
[05:20] generated code. That's interesting and
[05:23] perhaps not what we might have expected.
[05:25] Code written with AI assistance was no
[05:28] harder to change, no easier to change,
[05:31] no worse in quality and no better in
[05:33] quality. From a downstream perspective,
[05:36] AI didn't break anything. And frankly,
[05:39] given some of the fear-mongering, that's
[05:41] a pretty significant result and a
[05:43] finding that, as far as I understand it,
[05:45] is new to this research. Now, here's
[05:48] where things line up more with previous
[05:50] studies. In phase one, AI users were
[05:54] about 30% faster to get to a solution.
[05:57] Not as extravagant as some of the claims
[06:00] for AI productivity, but not nothing
[06:02] either. Habitual AI users were closer to
[06:05] 55% faster. So, yes, AI clearly speeds
[06:10] up initial development. That part isn't
[06:12] really very controversial anymore,
[06:14] though. I think the real question was
[06:16] whether that speed came at some hidden
[06:19] cost. And in this study, there was no
[06:21] evidence that it did. But there was
[06:23] something else that the study found that
[06:25] was very interesting. When experienced
[06:28] developers, people who already knew what
[06:30] they were doing, used AI habitually,
[06:33] their code showed a small but measurable
[06:36] improvement in maintainability later on.
[06:39] It's not a huge effect, but it is
[06:41] consistent. One explanation is that AI
[06:44] tends to produce boring, idiomatic,
[06:47] unsurprising code. And boring code is
[06:50] good. Surprise is usually the enemy of
[06:52] maintainability. But I wonder if there
[06:54] is more to it that's going on here. What
[06:57] is very clear is AI does not
[07:00] automatically improve code quality. We
[07:03] can't stop caring about engineering
[07:05] discipline. Junior developers can't
[07:08] simply vibe their way to good systems.
[07:11] In fact, the study shows that developer
[07:13] skill matters more than AI usage. This
[07:17] aligns strongly with a message that I
[07:19] have mentioned here before and that was
[07:22] backed up by the recent Dora research
[07:24] into the impact of AI. Fundamentally, AI
[07:28] code assistance acts as a kind of
[07:30] amplifier. If you're already doing the
[07:32] right things, AI will amplify the impact
[07:35] of those things. If you're already doing
[07:37] the wrong things, AO will help you to
[07:40] dig a deeper hole faster. Tools amplify
[07:43] capability. They don't replace it.
[07:45] There's an extremely good article by
[07:47] Jason Gorman. There's a link to that in
[07:49] the description below, too, that
[07:51] explores this idea in a bit more detail.
[07:53] But inevitably, I like his breakdown of
[07:56] what doing the right things means in the
[07:58] context of getting the best from AI
[08:00] coding assistants. He says, "Working in
[08:03] small batches, solving one problem at a
[08:05] time, iterating rapidly with continuous
[08:08] testing, code review, refactoring, and
[08:10] integration, architecting highly modular
[08:13] designs that localize the blast radius
[08:15] for changes. Organizing around
[08:17] end-to-end outcomes instead of around
[08:20] role or technology specialisms. Working
[08:22] with high autonomy, making timely
[08:25] decisions on the ground instead of
[08:27] sending them up the chain of command.
[08:29] For regular viewers of this channel,
[08:31] none of this will come as any surprise
[08:32] at all. I suppose that this may have
[08:34] inadvertently had an impact on the
[08:36] findings from the AI research. Most of
[08:39] the participants in the study were
[08:41] selected from people who responded to an
[08:43] invitation to participate here on this
[08:46] channel. So, they were viewers of this
[08:48] channel, which presumably, or at least
[08:50] I'd hope, means that they were already
[08:52] predisposed to doing a better job of
[08:54] development in this sense. So maybe they
[08:57] were pre-selected from the set of people
[08:59] more likely to do this better job. If
[09:02] you're interested in learning how to do
[09:03] a better job, why not join our mail list
[09:05] and get access to how-to guides, free
[09:08] tutorials, and discounts on training
[09:10] courses for you and your team, including
[09:13] discounts on our five-star rated
[09:15] accepted testdriven development with BDD
[09:17] course, which is particularly applicable
[09:19] to working more effectively with AI. The
[09:22] authors of our study highlight two other
[09:25] things that represent the slippery slope
[09:27] towards disaster. First is code bloat.
[09:30] When generating code becomes almost
[09:32] free, the temptation is to generate far
[09:35] too much of it. Volume alone is a
[09:38] massive driver of complexity in code and
[09:40] AI makes it easier than ever to drown in
[09:43] your own code base. The second problem
[09:46] is cognitive debt. If developers stop
[09:49] thinking, really thinking about the code
[09:52] that they create, then over time
[09:54] understanding erodess, skills atrophy,
[09:58] and innovation slows. This is exactly
[10:01] the kind of long-term risk that doesn't
[10:03] show up in a sprint metric. So, here's
[10:06] my conclusion. AI assistants clearly
[10:09] improve short-term productivity. And
[10:12] contrary to a lot of popular opinion,
[10:15] they do not appear to damage the
[10:16] maintainability of the systems that they
[10:18] produce. And they might even slightly
[10:20] improve it when they're used well, but
[10:22] they don't remove the need for good
[10:25] engineering. They don't remove the need
[10:27] for good design and the kind of broad
[10:30] understanding and experience that allows
[10:32] us to produce good design. And they
[10:35] certainly don't remove the need for
[10:37] thinking hard about the problems that we
[10:39] face, how to decompose them into small
[10:42] pieces that allow our AI assistants to
[10:44] do a good job and how to guide them
[10:47] towards solutions that we are happy
[10:48] with. This compartmentalization through
[10:51] decomposition is the central fundamental
[10:54] aspect of building software. This is the
[10:57] real technical skill at the heart of
[10:59] what it is that we do. And it is this
[11:02] rather than the speed of typing code
[11:04] that differentiates good software
[11:06] development from slop whether AI
[11:09] generated or not. As always tools matter
[11:13] but how we use them matters more. If you
[11:15] found this useful do hit subscribe and
[11:18] let me know how are the AI tools
[11:21] changing the way that you think about
[11:23] maintainability. I'll see you next time.
[11:26] Thank you very much for watching and if
[11:28] you enjoy our stuff here on the modern
[11:29] software engineering channel, please do
[11:31] consider supporting our work by joining
[11:34] our Patreon community. There are lots of
[11:36] benefits to that. To our existing
[11:39] Patreon members, as ever, I'd like to
[11:41] thank you for your support. It means a
[11:43] lot to us and it helps us to to carry on
[11:45] doing this. Thank you.
