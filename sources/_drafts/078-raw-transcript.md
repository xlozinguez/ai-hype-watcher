[00:00] Flawed code is blowing up right now and
[00:01] I've been right in the middle of it.
[00:02] I've been building full production
[00:04] systems, shipping MVPs, testing
[00:06] frameworks like GSD and the Ralph loop,
[00:08] but I've also been teaching N now for
[00:09] over two years to thousands of people
[00:11] and I genuinely love it. So, I've been
[00:13] using both daily side by side and I've
[00:15] been paying very close attention to
[00:17] where one is pulling ahead and where the
[00:19] other one still wins. And I keep seeing
[00:21] these posts everywhere. Is N dead? Is
[00:23] Claude Code going to kill N? And look, I
[00:25] do get why people are asking this, but I
[00:27] actually think they're asking the wrong
[00:29] question entirely because N and Claude
[00:31] Code aren't actually competitors. They
[00:33] do completely different jobs. And once
[00:35] you see them as one system, not two,
[00:37] what you can build actually changes
[00:39] dramatically. So in this video, I'm
[00:40] going to give you my honest wish list
[00:42] for what N needs to ship to stay on top.
[00:45] But I'm also going to show you what
[00:46] Claude Code does now that N was never
[00:49] designed to do. So, three big gaps, my
[00:51] [music] wish list for each one and the
[00:53] system that we're actually running
[00:55] today. So, let's get into number one.
[00:57] So, the whole promise of N was drag and
[00:59] drop, connect, and done. So, no code
[01:02] required at all. And that was genuinely
[01:03] faster than writing everything from
[01:05] scratch. I actually found N because I
[01:07] was trying to code a SAS app back in
[01:09] 2024 as a non-developer and it was super
[01:13] painful. But here's what changed.
[01:15] Prompting claw code is now just as fast
[01:17] as dragging nodes. And in some cases,
[01:19] it's blown right past it. I recently
[01:21] showed in a video me personally building
[01:23] a workflow in less than 10 minutes with
[01:25] claw code. The same one which I actually
[01:27] use in my business which took me an hour
[01:29] to build in nan. So think about what you
[01:31] actually do when you build an n. You're
[01:33] searching for the right node. You're
[01:35] configuring credentials, copying pasting
[01:38] JSON schemas, you're manually then
[01:39] mapping fields one by one. And if you
[01:41] need any custom logic, you basically put
[01:43] inside a code node and start writing
[01:45] some JavaScript anyway. But with claw
[01:47] code with MCPs to connect your systems
[01:50] and skills properly set up, you just
[01:52] describe what you want. It handles all
[01:53] of the API syntax, the credentials, and
[01:56] most time consumingly all of the
[01:58] individual data mapping. And you've got
[02:00] a working system in hours, not days. And
[02:02] that includes end to-end testing. And
[02:03] the crazy thing is iterating is even
[02:06] faster. You just tell it to write a test
[02:08] for this thing or handle this bug that's
[02:11] come up and it's basically done in a few
[02:13] minutes. You just go away, do something
[02:14] else, come back and it's done. Whereas
[02:15] in Nan, every single one of those
[02:17] changes means going back into the
[02:19] canvas, finding the right node,
[02:21] reconfiguring it, testing it. It's a lot
[02:23] more manual. And actually, there's
[02:25] already a bit of a community around
[02:26] this, trying to speed it up inside N. So
[02:29] the N MCP server and the N skills, they
[02:32] pair with Claude Code and N. So
[02:34] together, you can use Claw Code to
[02:36] actually build or edit your workflows
[02:39] much faster. Now n have their own
[02:41] in-built workflow builder but from my
[02:43] experience it's not as powerful as
[02:45] clawed code plus these connections and
[02:47] people are building with these things
[02:48] together network chuck built a full
[02:50] integration where n triggers claw code
[02:52] for specific use cases and they're doing
[02:54] that because they know alone one of
[02:56] these tools isn't enough whereas
[02:57] together combined they're much better.
[02:59] So the drag and drop speed that made nan
[03:01] actually special in the first place back
[03:03] when I started in 2024 well clawed code
[03:05] now just matches that with a prompt. So
[03:07] clawed code is fast, but speed isn't the
[03:10] only thing that's shifted over the last
[03:12] few months. There's something bigger
[03:13] that N simply wasn't built to do. So
[03:16] here's where the conversation gets
[03:17] really interesting because people keep
[03:19] comparing NAN and claw code like they're
[03:21] the same category of tool and they're
[03:23] not. And actually if you go to the N
[03:24] website, they even tell you exactly what
[03:26] they're for. If we hover over the use
[03:28] cases here, we've got building AI
[03:30] agents, rag, IT operations, lead
[03:33] automation, supercharge your CRM,
[03:34] back-end prototyping. And if you click
[03:36] into the backend prototyping page, we
[03:38] can go down to the properties here on
[03:40] why we would choose N. So, we're going
[03:42] to build back-end prototypes quickly.
[03:44] So, we're increasing our speed of
[03:46] learning by using N. We're gaining
[03:48] better observability than code. Really
[03:50] important one. And we're improving
[03:52] efficiency of our business operations.
[03:54] So if we think about it, that's all
[03:56] internal ops, observability, and fast
[03:59] experiments. And that makes total sense.
[04:01] That is genuinely what NAN is brilliant
[04:03] at. But here's the thing a lot of people
[04:05] in communities around NAN have wanted
[04:07] for a long time. We've wanted to build
[04:09] complete SAS products, multi-tenant
[04:11] systems, client portals with their own
[04:13] login, and full product stacks
[04:15] basically. And I do get that when you're
[04:17] inside N all day and you can see what it
[04:19] can do, how powerful it is, you
[04:21] naturally start to think, okay, how can
[04:22] I progress on this and just build a
[04:24] whole product in here, but actually if
[04:26] you go and check the license and I've
[04:28] got a specific video covering this and
[04:30] what's allowed versus what's not
[04:31] allowed. N sustainable use license
[04:33] restricts usage to your own internal
[04:36] business purposes only. So it
[04:37] specifically says you can't sell a
[04:38] product where the value derives entirely
[04:40] or substantially from the NAN
[04:42] functionality. So anything like white
[04:43] labeling it, hosting it for clients,
[04:45] building a multi-tenant SAS on top of
[04:47] it, that was never what NM was designed
[04:49] for is something that we just wanted to
[04:51] do with it. And this is where cloud code
[04:53] completely changes the game because with
[04:55] claw code, I can build a full
[04:56] multi-tenant backend in a few days. I
[04:59] can attach a proper front end, have a
[05:01] database with authentication, and even
[05:03] attach Stripe billing to take payments.
[05:05] We can build out client portals where
[05:07] each client can log in, see their own
[05:09] data, interact with their own interface,
[05:11] and I own every line of code that comes
[05:13] from claw code. Yes, I have to pay for
[05:15] the tokens to produce it, but I still
[05:17] own the code and I can host that
[05:18] wherever I want. So, when it comes to
[05:19] core code and you're a business owner,
[05:21] it's like being able to build your own
[05:23] internal tool with a proper interface
[05:25] that your team actually logs into every
[05:27] single day and not just have a workflow
[05:29] running in the background. It becomes a
[05:31] product. And if on the other side you're
[05:33] building an agency, imagine going from
[05:35] selling these 2K end workflows that the
[05:38] client still has to operate in the back
[05:39] end to actually selling 10K plus
[05:41] products with dashboards, client login,
[05:44] branded front ends. It's a lot more
[05:46] bespoke with not much additional work.
[05:48] And for you, that's a completely
[05:50] different value proposition. But if we
[05:52] go back to the point, N was never
[05:53] designed to do any of that. And it's not
[05:55] a criticism of N. Their own website, as
[05:58] we saw, tells you exactly what it's for.
[06:00] But Claude code is designed to fill that
[06:02] gap completely or that's how we use them
[06:04] together. So N builds your internal
[06:05] automations. Claude code builds
[06:07] customerf facing products. And the
[06:09] moment you see them that way the is n
[06:11] dead question kind of answers itself. So
[06:14] we've got speed and we've got product
[06:16] capability covered. But there's one more
[06:18] major gap that's been driving me mad and
[06:20] it's the one I think n actually should
[06:22] fix. So the biggest issue for any
[06:24] internal team running multiple workflows
[06:26] is this. Every N workflow is essentially
[06:28] in its own isolated little world.
[06:30] There's no global state management.
[06:32] There's no versioning across multiple
[06:34] instances and that creates a massive
[06:37] problem when you start to scale. So
[06:38] picture this. You've got 10 workflows
[06:41] for 10 different clients. They all share
[06:43] the same core logic and then you find a
[06:45] bug or you want to improve that logic.
[06:47] In Claude code, you just ask it to
[06:49] update one function and you push it and
[06:51] your multiple clients will receive the
[06:53] updates. Whereas in N you're opening
[06:55] each workflow one by one. you'll know
[06:57] the pain. You're manually updating the
[06:59] same node configuration in all 10 of the
[07:01] workflows. And this can somewhat be
[07:03] circumvented if you use subworkflows,
[07:06] but you still can't version them
[07:07] independently. You can't roll back one
[07:09] workflow without affecting the others.
[07:10] And you definitely can't do a global
[07:12] logic update across all your workflows
[07:14] in one go. And it's not just an
[07:15] exclusively agency problem. If you're an
[07:17] internal team and you've got five people
[07:19] who each built slightly different
[07:20] versions of the same workflow, which
[07:22] happens all the time, you still have to
[07:24] keep them all aligned. And these may be
[07:26] features that are available on N's
[07:28] enterprise plan or more so. But with
[07:30] Claude Code, we're pretty much able to
[07:32] do this for free. So here's my wish list
[07:33] for N. Give us a way to roll out
[07:35] versions across multiple instances. Let
[07:38] us treat that shared logic like shared
[07:39] code so that we can update once and just
[07:41] propagate it everywhere because right
[07:43] now that is where claw code I see it
[07:45] just running away with it and it's what
[07:47] you need to scale fundamentally. So
[07:48] without this N really hits a ceiling at
[07:51] scale. So, I know I've just spent a few
[07:52] minutes now being pretty critical to
[07:54] NAN, but here's the thing. I'm
[07:56] absolutely not telling you to ditch NAN.
[07:58] Not even close, actually, because N
[08:00] still does something that Claude code,
[08:02] in my opinion, genuinely can't match at
[08:04] this point. So, here's what the N is
[08:06] dead crowd actually keeps missing, and
[08:08] it's the thing that actually matters for
[08:09] most businesses. If you look at the N's
[08:12] execution history log, is genuinely one
[08:14] of the most powerful debugging tools
[08:16] I've ever used. It is so visual and so
[08:19] easy to use. You can literally see every
[08:21] single run. You click on any node and
[08:23] you can see exactly what data went in
[08:25] and what data came out. So every branch,
[08:27] every condition, every transformation,
[08:29] it's all right in a visual interface.
[08:31] And for nontechnical people like
[08:32] business owners, ops teams, clients who
[08:34] want to understand what happened and
[08:36] why, it's absolutely massive. Once they
[08:38] know the core fundamentals of the NAN
[08:40] interface, it's really easy to visually
[08:43] understand the bugs. You don't need to
[08:44] understand logging. You just need to
[08:46] click through and actually see it. And
[08:47] it's pretty much in plain English what
[08:49] the problem is to and actually this is
[08:51] why N in my opinion should stay as your
[08:54] core business logic layer. So the
[08:55] automations that actually add value the
[08:57] lead enrichment the data processing the
[08:59] client workflows that's where I think N
[09:02] really shines because when something
[09:04] goes wrong and ultimately things always
[09:06] go wrong anyone on your team can go into
[09:08] the interface and actually diagnose and
[09:10] help fix the problem. So your core
[09:12] business logic should live where it can
[09:14] be inspected, tested and debugged by the
[09:18] people who actually depend on it. And in
[09:19] my opinion, it's the same way in which
[09:21] you don't outsource the core parts of
[09:22] your business where you're actually
[09:24] adding value. You do those inhouse. We
[09:26] want visibility of those areas. We want
[09:28] full control and N gives us that. So
[09:31] don't get me wrong, claw code is
[09:32] incredible for building, but try handing
[09:34] a client the terminal or the code that
[09:36] you've created to a non-technical team
[09:38] and saying here check the logs. I mean,
[09:41] good luck with that. The visual
[09:42] transparency in N is actually probably
[09:45] where it shines the most. And right now,
[09:47] I've not found a solution for claw code
[09:50] that actually matches that visually. So,
[09:52] your business logic should live where
[09:53] your team can see it, where they can
[09:55] debug it, and where they can actually
[09:57] trust that it's going to be repeatable
[09:58] again and again. And right now, for me,
[10:00] that's inside N. So, here's how we're
[10:02] actually building now. And it's the most
[10:03] powerful setup that I've ever used.
[10:05] Clawed Code is building everything that
[10:07] N was never designed to do. the backend
[10:09] infrastructure, the front ends, the
[10:11] client portals, the multi-tenant
[10:13] hosting, the orth, the databases, all
[10:16] stuff that I don't really want to build
[10:17] myself. So, it builds the packaging
[10:19] around the product, whereas N I'm using
[10:22] to handle the core business logic. It
[10:24] might take more time to build this way,
[10:25] but I have more control and I can debug
[10:27] and test in this way. N is ultimately
[10:29] going to handle the automations that are
[10:31] actually going to drive value, the stuff
[10:32] that needs to be visual, debugable, and
[10:34] accessible to anyone in the team. And
[10:36] when you combine them together, you're
[10:37] not just building workflows anymore.
[10:39] You're building systems, complete
[10:41] systems that you can sell or you can
[10:43] operate entire businesses around. So, is
[10:45] N dead? No. But it does need to keep up.
[10:49] So, my wish list is super simple. Close
[10:51] the speed gap. So, N's built-in builder
[10:54] needs to be better. It needs to match
[10:55] the claw code NAN MCP and give us the
[10:58] ability to propagate versions, too. But
[11:00] here's the bigger picture. The builders
[11:01] who figure out how to combine clawed
[11:03] code and nan into one system, they are
[11:07] going to leave everyone else behind
[11:08] because they'll no longer be selling
[11:09] automations anymore. They'll be selling
[11:11] complete products and systems. So, if
[11:13] you want to see how we build full
[11:14] systems with claw code and n together,
[11:17] I've just released a complete course on
[11:18] exactly that. The link's down in the
[11:20] description below. Thanks for watching.
[11:22] Give it a like and subscribe if you want
[11:23] to see more content like
