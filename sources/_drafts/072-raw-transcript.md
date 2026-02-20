[00:00] Hey guys, welcome to this video. I think
[00:02] this is going to be a really, really
[00:03] interesting one. Somebody came into my
[00:05] live stream the other day and they asked
[00:06] me how to get started with Vibe coding
[00:08] and why it never works for them. So, in
[00:11] this video, what I thought I'd do is
[00:12] show you exactly how I start a project.
[00:15] Probably in the next 12 minutes, we're
[00:17] going to have an entire project built.
[00:19] Let's jump into things because we do
[00:21] need to move quite quickly. Now, the
[00:22] first thing you need is an AI Studio
[00:25] project. You don't have to use AI
[00:26] Studio. The reason I use AI Studio is
[00:28] because it creates a React project with
[00:30] Gemini inside. This is just what I'm
[00:33] using for ease. You can do whatever you
[00:35] want to make your AI project. But let's
[00:38] just jump into things. So the first
[00:39] thing you want to do is look, I just
[00:40] gave it a prompt like this. Very, very
[00:43] easy. This is just Google AI Studio.
[00:45] Just gave it a prompt and this works
[00:47] inside AI Studio. But how do I turn this
[00:49] into a full SAS? Before continuing guys,
[00:51] a very quick word from our sponsor, me.
[00:53] This is harbor.ai.
[00:55] AI and this is a tool that I created for
[00:58] people like you who have a SAS
[01:00] application or a blog or an e-commerce
[01:02] store and you need help with blogging.
[01:05] You discover keywords, you write
[01:06] articles and you help and we help you
[01:08] publish them as well. And we even have a
[01:11] link building tool which will help you
[01:13] build back links and a link bait tool
[01:16] which will let you build pages on your
[01:18] website that will get you back links.
[01:20] And if you need a little bit more help
[01:21] or if you want to push your tool a
[01:23] little bit more, you can also buy manual
[01:26] backlinks where we will actually fulfill
[01:28] them and you can even get half price off
[01:31] the first 3 months with the code half
[01:33] price links and we will build those back
[01:35] links for you. Thank you for the
[01:36] attention. Back to the video. Right. So
[01:38] the first thing you do is download the
[01:40] app and then you can just ignore that
[01:41] for 2 seconds. Then you want to go to
[01:43] Google and you want to type convex
[01:47] next.js JS
[01:49] and then click here and then just copy
[01:51] this button right here. Right. And then
[01:53] we're going to use anti-gravity and
[01:55] we're going to use the worst possible
[01:56] model. So we'll use Gemini 3 flash
[02:00] convex and then we'll open this folder.
[02:03] This is the folder that we're going to
[02:04] be using. We'll go to terminal new
[02:06] terminal and then paste that command
[02:08] from before.
[02:11] Uh we'll call this my app and we'll use
[02:13] NextJS app router. We'll use clerk. You
[02:15] can use whatever you want. If you don't
[02:16] want to use clerk, don't use clerk. Just
[02:18] whatever you guys prefer. It doesn't
[02:20] matter. I just use clerk because it's
[02:22] nice and easy. Next thing we want to do
[02:24] is we want to go to clerk.com.
[02:28] I really really do like Clerk. Uh if you
[02:30] want to uh sponsor me, Clerk, uh please
[02:34] do. Um I'd love that. Click here, create
[02:36] application. Call this Gemini 3/
[02:40] Convex and then create application. You
[02:43] have to do this every single time you
[02:45] start a project. One of the main things
[02:46] people do is they just jump into the
[02:49] project without setting the base of the
[02:51] project. So the point of this video is
[02:53] to show you how to create the base,
[02:55] right? So that's what we're doing. So go
[02:57] to configure, type JWT here, click here,
[03:00] add new uh template, write convex here.
[03:03] I do this every single time I start a
[03:05] new project without fail. Right? This is
[03:07] what I do. So, you want to press copy
[03:09] here and then you want to go to docs new
[03:13] and paste. And then copy this and then
[03:16] paste.
[03:18] There we go. We're now done here. So,
[03:21] let's just jump on over to Google again
[03:23] and type convex clerk and then click
[03:26] here. And then you basically just want
[03:28] to grab this entire bit here, right? Uh
[03:34] up to here. So, let's do control shift.
[03:36] No, you can't. So, let's just scroll up
[03:38] all the way like this. Kind of annoying
[03:40] to do it like this, but there we go.
[03:42] Copy that and then paste. And then let's
[03:46] just see if we need anything else. I
[03:48] don't believe we do actually. So, let's
[03:50] just go back to anti-gravity. Now, we
[03:52] need to It even tells us what we need to
[03:53] do here. Look, CD my app mpm rundev. So,
[03:56] cd my app mpm rundev. What this does is
[03:59] it starts the convex project, right? So,
[04:02] we're going to create a new project.
[04:03] This is going to be called uh Gemini 3
[04:06] flash convex cloud deployment. And then
[04:09] what this does is it actually starts the
[04:11] convex project. Right? So you'll see in
[04:14] a second this will open up convex. There
[04:16] we go. This is our database. Right? So
[04:18] this is not only our database, it's also
[04:19] our backend. Right? So just remember
[04:21] that. So we have database and backend
[04:24] right here. Now trust me guys, convex is
[04:27] incredible. You want to use it. It's so
[04:29] so good. Okay. So let's just do control
[04:33] arr c here. Here here I don't think oh
[04:35] yeah no I am missing something else.
[04:36] Sorry I need to go back to clerk and
[04:39] dashboard and then we need to grab these
[04:41] m variables right here. So these ones
[04:44] here we just press copy and then paste
[04:47] them here. There we go. Control arr c
[04:50] back on over to anti-gravity. Let's use
[04:52] Gemini 3 flash fast mode of course. And
[04:56] then we'll say please set up
[04:59] authentication
[05:01] with clerk in this project. Please make
[05:04] sure when a user uh presses login or
[05:08] sign up that an actual
[05:12] account is created inside convex
[05:16] and they see a page called /dashboard.
[05:21] Don't um create any dashboard uh just
[05:25] yet. And then all we do is Ctrl +V,
[05:28] paste all that. And then watch how quick
[05:30] this is. Right? It's 1252 right now.
[05:32] This is going to be extremely fast. This
[05:34] is the problem with how a lot of people
[05:36] build, right? They just go in, they
[05:39] build, they, you know, they say, "Make
[05:40] me an XJS project. Make me this. Make me
[05:43] that. Do this. Do that." But it's not
[05:45] going to work like that. The best thing
[05:47] to do is to slowly set up the base of
[05:49] the project and then you start to say
[05:52] right now add this now add that add this
[05:55] add that add the other etc etc right so
[05:59] this is kind of the biggest mistake that
[06:00] people do with vibe coding is they don't
[06:02] spend the time to sit and make sure that
[06:06] everything is working first right it's
[06:08] super important
[06:10] so now we'll just let this run like I
[06:12] said it's 12:52 now let's just see how
[06:14] quick this actually goes
[06:16] So, I did actually miss a step, guys.
[06:18] Another thing you can do is you can tag
[06:20] convex rules.mmdc. I would recommend
[06:22] doing that to be honest with you,
[06:23] especially with something like Gemini 3
[06:25] flash because it's not the best model,
[06:28] but it's okay. I think it will still do
[06:30] a pretty good job here. So, I can see
[06:33] now that it's created a new um schema,
[06:36] right? So, we now have a user uh thing
[06:39] in the database. You can actually see
[06:40] that happening right here. Now the only
[06:42] thing is for some reason local host 304
[06:44] is um 404ing. So we'll just wait a sec.
[06:48] Okay, beautiful. So now we have this set
[06:49] up. That was about 5 minutes. So let's
[06:50] do sign in here. This is why I love
[06:52] clerk because you already have the kind
[06:54] of signin thing here right here. And
[06:57] then this should go to slash dashboard
[06:59] after we have uh logged in. So let's
[07:02] see. This is actually quite hard to set
[07:05] up. So let's see. Okay, so it didn't go
[07:07] to slashboard, but we are logged in as
[07:08] you can see. Oops. dashboard. So, we
[07:12] should be able to now go to dashboard.
[07:13] There we go. Welcome to your dashboard.
[07:15] Beautiful. And then if we go to convex
[07:17] and go to data and look at users, we
[07:19] should have a user. We do not. So, this
[07:21] is super important, guys. You need to
[07:22] make sure that users are actually being
[07:23] created. Right? This is likely due to me
[07:26] not tagging convex rules.mdc.
[07:29] Okay, beautiful. There we go. There's my
[07:30] user. It's now being created. So, now
[07:33] all we have to do, right, is give this
[07:35] entire project from before this download
[07:37] that we just downloaded before. So,
[07:40] let's just unzip it.
[07:43] There we go. And then we just drag this
[07:45] in, right?
[07:48] So, let's drag it to the side, actually.
[07:49] So, we'll put it here. Add fold to
[07:52] workspace. There we go. And then we just
[07:55] tag studio batch. So, let's say at
[07:58] studio. No, doesn't come up.
[08:02] Okay. So, you can drag and drop it. I
[08:03] just drag and dropped it. Please now
[08:06] implement this on /dashboard.
[08:11] Okay. And there we go. We're now done.
[08:13] Uh I need to remove this select API key
[08:15] thing because that's from Google's AI
[08:17] studio. Okay. And there we go. Let's
[08:19] just see if this is actually working. So
[08:21] let's click the upload button. Let's
[08:23] just select uh this for example. This is
[08:25] just my logo. Then we'll select this and
[08:28] then generate batch. And we should be
[08:30] done. And we now have a complete not a
[08:33] complete SAS because obviously we don't
[08:35] have Stripe. But Stripe is actually
[08:36] really really easy to add.
[08:39] And then bang, you can see everything is
[08:41] working. We can press download here and
[08:43] we have the completed uh design. Don't
[08:46] worry about the crap guys. And yeah,
[08:49] that's pretty much it guys. That was
[08:51] literally what like a 15minute process
[08:54] to get to the point where we have this
[08:55] entire project. Now obviously you still
[08:58] need to make a homepage. You still need
[08:59] to do this. You still need to add
[09:00] Stripe. But like this is what I'm
[09:02] talking about. If I had tried to do this
[09:04] with Vive coding where I just gave this
[09:05] giant prompt to even claude code, right?
[09:10] It would have taken a lot longer and it
[09:12] probably wouldn't have even managed to
[09:14] do it, right? So this is what I'm trying
[09:16] to tell people. You there's no point
[09:18] going around Vibe coding when you can
[09:20] just do things this quickly anyway. Like
[09:23] that that took what like 14 minutes I
[09:25] think on Flash. Gemini 3 flash, which is
[09:29] not even a good model. But yeah, guys, I
[09:32] think I'll leave the video there. Thank
[09:33] you so much for watching. If you are
[09:34] watching all the way to the end of the
[09:35] video, you're an absolute legend. And
[09:37] I'll see you very, very soon with some
[09:38] more content. Peace off.
