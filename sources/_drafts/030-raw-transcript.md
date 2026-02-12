---
source_id: "030"
title: "Playwright CLI vs MCP - a new tool for your coding agent"
creator: "Playwright"
url: "https://www.youtube.com/watch?v=Be0ceKN81S8"
extracted: "2026-02-12"
method: "yt-dlp"
segments: 165
---

[00:00] Hi there. Let me show you what Playright
[00:02] CLA is. It's a new tool in the Playright
[00:06] In this video, we're going to talk about
[00:07] what Playright CLA is. We'll compare it
[00:10] to MCP, give some demos, talk about
[00:12] token efficiency, uh some capabilities,
[00:15] and uh hopefully you'll have a better
[00:17] idea on which one you should be using in
[00:19] the future. Let me start with the demo.
[00:23] This is a demo of the Playright CLI
[00:25] functionality. I'm starting in an empty
[00:28] folder uh demo CLI and uh I'm going to
[00:30] install playright CLI globally. It means
[00:33] that it'll be available in all the
[00:35] locations and the first thing I do is
[00:37] I'm initializing my workspace. I'm
[00:38] saying playright CLI install which uh
[00:41] creates an empty folder called playrite
[00:44] playright and that's it. And we are
[00:45] using that to differentiate between
[00:47] different workspaces on your disk. Each
[00:49] of these workspaces uh is going to have
[00:51] its own set of browsers that it's going
[00:53] to use. more about that later. But I'd
[00:56] like to also install some skills in this
[00:58] workspace. I'm calling install skills
[01:00] and uh it installs a bunch of uh cloud
[01:03] skills in my workspace. Let me start
[01:05] cloud and give it a task. I'm going to
[01:09] ask it to open playright def which is a
[01:11] web page. Search for locators which is
[01:13] just a word and check that the doc is
[01:15] available for each language. And uh by
[01:17] the language we means that it's
[01:18] available for JavaScript, Python, Java
[01:20] and .NET. And I'm also asking it to take
[01:23] screenshots for each uh of the language
[01:25] docs. So let's see how it does it. What
[01:28] we're looking at is 16x uh time lapse of
[01:32] what was happening. And uh what was
[01:34] happening is just cloud was talking to a
[01:37] browser using the CLI utility. Let's see
[01:40] the result is there. Let's look at the
[01:43] context which allows us to see how much
[01:45] tokens we have spent. But we won't stop
[01:46] here for a long time. And we're going to
[01:48] proceed with the MCP version of the same
[01:51] task. Um, let me start cla
[01:55] um I see MCP server installed. Playright
[01:57] MCP is installed. No skills are
[02:00] installed in this work folder. So what
[02:02] I'm going to do is I'm going to give it
[02:03] exactly the same task and again 16x
[02:06] timelapse. And uh it's done. Let's also
[02:10] open the context stats here to see how
[02:12] much tokens we have consumed.
[02:19] All right. So what we are seeing here is
[02:22] that we have uh taken 114,000 tokens for
[02:26] this operation which is quite costly.
[02:29] Let's compare this to what we have
[02:30] gotten with CLI and the CLI has taken
[02:33] only 26.8,000 tokens.
[02:39] So what we have seen in the demo was
[02:41] that MTP consumed more context. But why?
[02:44] Let's dig a little deeper.
[02:47] This is what MTP was doing. So let's
[02:49] explore these two calls. First, it tried
[02:50] to navigate to a page and play rate dev
[02:52] is a docosource page. It's pretty big.
[02:54] It has a lot of content, a lot of uh DOM
[02:56] control, scripts, etc. And even though
[02:58] playrate MCP is uh very efficient in uh
[03:01] conveying only the accessibility
[03:02] snapshot to the LLM, it still replied
[03:04] with the entirety of it and it all has
[03:06] gotten into the context window. And we
[03:08] can see here that result exceeds the
[03:10] maximum amount of tokens.
[03:13] And after that it took a screenshot. But
[03:16] when uh MTP is taking a screenshot LLM
[03:18] is asking it to do so. So we are
[03:20] replying with all those bytes to the LLM
[03:22] itself. And again the image tokens end
[03:24] up in the context. And in this case that
[03:27] wasn't the goal. All we wanted was to
[03:28] capture a screenshot and save it on
[03:29] disk. Let's compare it to what CLI was
[03:33] doing. CLI said I'd like to go to a
[03:35] location. And then without even
[03:37] capturing a snapshot or reading a file
[03:39] with a snapshot from the disk which was
[03:40] created as a result of this call, it
[03:42] immediately took a screenshot and saved
[03:43] it this file. As a result, it saved
[03:46] context. None of these uh tokens got
[03:48] into it because LLM didn't actually need
[03:50] them. So what CLI is doing is uh all of
[03:53] the data that it emits it saves into
[03:55] files and then your coding agent is
[03:57] going to make a decision of whether it
[03:58] needs to go to LLM or not. Let's talk
[04:01] about capabilities.
[04:03] We saw how MCP worked but you will see
[04:05] that MCP only used a couple of dozens of
[04:07] commands and that is not because of uh
[04:09] we don't have those. We do have them. In
[04:11] fact, all the CLA capabilities are also
[04:13] present through MCP. We just don't
[04:15] enable them by default because they are
[04:16] consuming context.
[04:18] On the other hand, on CLI, we don't have
[04:20] that limitation. So, we can expose all
[04:22] of these commands and more.
[04:25] All right. So, we've seen uh the token
[04:27] use. We've talked about capabilities.
[04:29] Now, seems like it's a no-brainer. You
[04:31] should be using CLI, right? Well, let's
[04:33] talk about it a little bit.
[04:36] CLI is the new tool and it shines when
[04:39] it's being used as a part of the coding
[04:40] agent and the coding agent is uh your
[04:43] claude code or GitHub copilot or any
[04:46] other agent that can edit files that has
[04:48] access to your workspace. We can be
[04:50] efficient there. We can capture those
[04:51] snapshots, save them on disk, save those
[04:53] screenshots on disk and let coding agent
[04:55] decide whether it wants to read them in
[04:56] full or it wants to send the entirety
[04:58] into the LLM. So, it becomes token
[05:00] efficient that way. So CLI requires a
[05:02] coding agent to be efficient. Uh other
[05:05] than that it is skill-based and you can
[05:07] add knowledge about playrite and your
[05:09] scenarios and through the skills. So
[05:10] it's interoperable with other
[05:11] skill-based tools. It also is headless
[05:13] by default because we assume that you're
[05:15] going to run a lot of background agents
[05:17] in your coding agents with them.
[05:20] On the other hand, MCP is going to work
[05:22] with any generic agent. It's a strict
[05:24] standard and tools know what to expect,
[05:26] how to call these MTP tools, what the
[05:28] results are. But in this case,
[05:30] everything is in the hands of the LLM.
[05:32] So all of the replies are most likely
[05:34] going to make their way back into the
[05:35] LLM and are potentially going to
[05:37] overwhelm its context. You can still
[05:40] have multiple browsers in MTP. No
[05:42] problem. And the efficiency of MCP can
[05:44] actually be configured. You can uh allow
[05:46] and disallow those tools and see what
[05:48] you need. It's a little bit more manual
[05:50] in that regard. Also, historically MCP
[05:52] is by default. So to recap, if you're
[05:54] using a coding agent, if your tasks are
[05:57] coding, testing, you're using cloud,
[05:59] GitHub, copilot, you probably want to
[06:01] use CLI. On the other hand, if you are
[06:03] authoring an agentic loop that is
[06:05] performing certain tasks for your
[06:06] scenarios, MTP is still the way to go.
[06:09] That's about it. Heavy testing.
