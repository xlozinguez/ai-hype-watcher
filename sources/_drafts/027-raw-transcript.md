---
source_id: "027"
title: "Devs can no longer avoid learning Git worktree"
creator: "Joshua Morony"
url: "https://www.youtube.com/watch?v=S8_AsOuAwLo"
extracted: "2026-02-12"
method: "yt-dlp"
segments: 142
---

[00:02] I've been fortunate enough to be able to collaborate with and generally just hang
[00:04] out on Discord with a particularly
[00:06] talented and productive software
[00:08] engineer over the past few years. This
[00:10] person, Chiao Tran, for those of you who
[00:12] may know him from his open source work,
[00:15] has helped shaped a lot of my workflow
[00:17] over the years. In general, if I see
[00:19] Chiao doing something, I can be
[00:21] reasonably sure I should probably be
[00:23] doing that as well. One of those things,
[00:25] something that came up many times, but I
[00:27] kept putting off bothering to learn, was
[00:30] git work trees. It sounded hard and
[00:32] generally I could avoid the scenarios
[00:34] where it seemed like they were most
[00:36] useful. Generally, when you suddenly
[00:38] need to context switch away from
[00:40] whatever you are working on to do
[00:42] something else in the codebase, maybe
[00:44] some kind of hot fix situation or
[00:47] reviewing a PR. I would generally just
[00:49] try to avoid those situations by
[00:52] attempting to get my code to a point
[00:53] where I could make a clean commit or
[00:55] worst case scenario I could just stash
[00:58] the changes. But work trees are actually
[01:00] pretty simple both conceptually and to
[01:03] use. Think of one of the main purposes
[01:06] of Git. It enables multiple developers
[01:08] working on different file systems to
[01:11] collaborate on code. You could be
[01:13] working on one feature on your machine
[01:15] and file system. Another developer could
[01:18] be working on another feature on their
[01:20] machine and file system. And when you're
[01:22] both done, you smash those features
[01:24] together and you have one unified
[01:26] codebase. To understand the problem git
[01:29] work trees address, let's focus on the
[01:32] problem AI creates. One that is much
[01:34] less avoidable than the other situations
[01:37] I outlined. The problem, or at least a
[01:39] problem, arises when you're using some
[01:42] kind of agentic AI process that is going
[01:45] to be working on a task for any
[01:47] non-trivial amount of time. Take my
[01:49] current agentic AI workflow for example.
[01:51] My general process is that I design a
[01:54] track which outlines work to be done in
[01:56] phases. I then trigger my script which
[01:59] will launch a new AI agent to tackle
[02:01] each phase in succession until the track
[02:04] is complete. and then a PR is opened by
[02:06] the agents for me to review. So, feel
[02:09] free to drop a comment and subscribe if
[02:11] you're interested in me diving into this
[02:13] workflow more. It's more or less the
[02:15] same Ralph approach a lot of people have
[02:17] been using lately, but I've been using
[02:18] it to build out a lot of complex
[02:20] features and have been having great
[02:22] success with it. But for this video,
[02:24] let's just focus on the problem git work
[02:26] solve. The problem is that these AI
[02:28] agents are using your file system and
[02:31] you want to use your file system, too. I
[02:34] get my Ralph agents to start executing
[02:36] on a task that is going to take 15
[02:38] minutes, 30 minutes, an hour maybe, and
[02:41] I just what? Watch YouTube for a bit
[02:43] until the PR is ready to review. Not a
[02:46] bad option, certainly, but not the most
[02:48] productive one. Likely, I'm also going
[02:50] to want to work within that same code
[02:53] base on something else. But I can't
[02:55] really because the AI agents are making
[02:57] edits to the same code base on the same
[02:59] file system at the same time. To deal
[03:02] with this, we can quite simply create a
[03:04] git work tree. You can run this command
[03:06] to create a work tree manually, but
[03:09] personally I use lazy git and other
[03:11] tools would support this as well. I can
[03:13] just come in here and create a new work
[03:15] tree based off of main. And what this is
[03:18] going to do basically is create a copy
[03:20] of the project file somewhere else on
[03:22] your file system. But both instances of
[03:25] those files will share the same git
[03:27] tracking. So I have my main repo called
[03:30] games and I have a sibling directory
[03:33] called games work trees and that is
[03:35] where I want to create this work tree.
[03:38] And then we can supply a name for the
[03:40] branch we will be working on. Keep in
[03:42] mind that you can't have the same branch
[03:44] checked out in a work tree that you also
[03:46] have checked out in your main project
[03:48] folder. I can make changes from within
[03:50] my main project folder and I can make
[03:52] changes within my work tree folder.
[03:54] These two folders can work entirely
[03:57] independently. And when I am done with
[03:59] the work tree, I can easily just merge
[04:01] the branch from the work tree into the
[04:04] main repo just as if it were a normal
[04:06] branch. To think of it most simply, work
[04:09] trees allow you to have different
[04:11] branches checked out at the same time on
[04:13] the same file system. And rather than
[04:15] bothering to create these work trees
[04:17] myself to deal with the AI problem, I've
[04:19] just got it incorporated as part of my
[04:21] agentic AI workflow. Whenever agents
[04:24] begin work on a new track, they will
[04:26] first create a work tree and branch for
[04:28] it. And they will only work within that
[04:31] work tree, which means I am then free to
[04:33] work on the main codebase as I please,
[04:35] and I can just review and merge the PR
[04:38] from the work tree when I am ready. One
[04:40] situation that comes up a lot in this
[04:42] workflow is that I will want to check
[04:44] out the branch the agents are working on
[04:46] to test or review it. But if a work tree
[04:48] has a branch checked out, you can't
[04:50] actually check out that same branch. But
[04:53] you can check out a commit in a detached
[04:55] readonly state. So instead of checking
[04:58] out the branch itself, you can instead
[05:00] just check out the latest commit from
[05:02] that branch. So you can still easily
[05:04] take a look at work tree branches from
[05:07] within the main project directory if you
[05:09] want. Alternatively, especially if you
[05:11] wanted to make some manual changes, you
[05:14] could also just switch into working in
[05:16] the workree folder directly. If you
[05:18] found this video useful, a like or
[05:20] subscribe before you go would be greatly
[05:22] appreciated.
