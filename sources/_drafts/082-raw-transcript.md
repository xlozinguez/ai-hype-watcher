[00:00] Some people just have odd hobbies, you
[00:02] know, like I know some of you out there
[00:03] after a long day at the pixel mines
[00:05] likes to go home and play that game of
[00:07] Factorio. Yes, Factorio for when
[00:10] assembly just doesn't feel like it gives
[00:12] you the same high used to. Now for
[00:14] Jeremir, his special hobby, as he likes
[00:16] to call it, is a habit of skimming the
[00:19] open JDK commit log every few weeks. And
[00:22] this time while scanning it, he ended up
[00:24] finding a commit that had 40line fix
[00:26] that eliminated a 400x performance gap.
[00:30] Now, this is actually it's super cool.
[00:32] How it works is pretty amazing. You got
[00:35] I I I love it. There's going to be flame
[00:37] graphs. I'm going to explain to you what
[00:38] flame graphs are if you've never used
[00:39] them. And also, hey, you shouldn't knock
[00:40] it until you rock it. Okay? Don't make
[00:42] fun of somebody for looking over change
[00:44] logs. Okay? That's a good pastime. Now,
[00:45] the change log that got his attention
[00:47] was this one right here. replacing
[00:49] reading proc to get thread CPU time with
[00:52] clock get time. And the diff contained
[00:54] 96 insertions, 54 deletions, and the
[00:57] change set adds a 55line JM benchmark,
[01:01] which means that the production code
[01:02] itself was actually reduced. And it
[01:04] turns out that this change is actually
[01:06] from like a 2018 bug JDK8210452
[01:12] that says get current thread user time
[01:14] is 30 to 400x slower than get current
[01:17] thread CPU time. So it's been around for
[01:19] a while. Okay, we've all we've all been
[01:21] there. Okay, I I've had a few Jirro
[01:22] tickets that lasted the entire tenure of
[01:25] my previous job and were never ever
[01:27] fixed. So I get it. I'm not no Hey, no
[01:30] stones being thrown here. Okay, buddy.
[01:32] All right, so let's first like let's
[01:33] look over the code that got deleted
[01:34] because when you see this, you'll be
[01:37] surprised at how much effort was
[01:39] required to get user current time for a
[01:42] thread. First thing they do is a bunch
[01:43] of like kind of declarations stuff,
[01:45] right? They get the current thread time
[01:47] right here and then a whole bunch of
[01:48] just initialization of either dummy
[01:50] variables or a buffer right here. The
[01:52] first thing it does is open up a file to
[01:54] the proc name. Then it's going to read
[01:56] out all the data into this 2K buffer,
[01:59] add a little kind of null terminator at
[02:01] the end, and then it's going to close
[02:02] down the file that was open. So then
[02:04] after reading everything from the file,
[02:06] it does this kind of reverse character
[02:07] look into a string right here. Now,
[02:09] apparently this was a source of many
[02:11] bugs. Like this just happened over and
[02:13] over again. And so they came up with
[02:15] this way where it would just find the
[02:17] last parenthesy. And then at that point,
[02:19] you knew, okay, everything after this,
[02:21] we're going to be able to get some
[02:22] information about the process. We're
[02:24] going to then skip a whole bunch of
[02:25] whites space until we get to a non-white
[02:27] space character. Then we're going to
[02:28] read 13 numbers. That's right. So that
[02:31] means the proc, which remember these
[02:33] proc files, they aren't just like actual
[02:35] real files. They are generated on the
[02:36] fly. So it actually takes a bunch of
[02:38] numbers, converts them into strings,
[02:40] copies them to user space. Then the user
[02:42] space is going to take that string back
[02:44] out, do a little bit of parsing itself
[02:46] with a little reverse char search. And
[02:48] then it's going to take those
[02:49] stringified numbers and reput them back
[02:52] into numbers just to get these last two
[02:54] right here. And then at that point, you
[02:57] got yourself a little bit of that user
[02:58] time. Okay, easy as that. Just a little
[03:01] one, two, three. By the way, you ever
[03:03] you ever wonder why people working at
[03:05] really low levels tend to be grumpy?
[03:07] Okay, we call them those angry neck
[03:08] beards. Okay, you understand why a lot
[03:10] of people had to put up with a lot of
[03:12] Okay, so don't you go don't you be
[03:14] just sitting there adjusting your little
[03:16] div being like, I just want a little
[03:18] drop shadow. Okay, there's people that
[03:19] spent their lives trying to figure out
[03:21] why drop shadows aren't working and
[03:22] you're over there complaining. You don't
[03:25] know what's going on in there. Okay,
[03:26] buddy. And of course, here's the new
[03:28] implementation. And there's like a bunch
[03:29] of kind of some internal stuff that is
[03:31] uh rather confusing exactly how it
[03:33] works. But nonetheless, it does a little
[03:35] bit of kind of flipping a couple bits
[03:37] inside of this little clock ID and then
[03:39] down here, boom, it just gets the thread
[03:41] time. Yes, it's still for a lot of
[03:43] people that looks like very ugly code,
[03:45] but it is significantly better. We can
[03:46] all agree, reading out from a proc file,
[03:48] doing a bit of string processing,
[03:50] hitting a scan f, and then grabbing 12th
[03:52] and 13th number out of a list. We can
[03:54] all agree this has to be better. Right
[03:56] now, the best way to kind of understand
[03:58] the performance of how something runs is
[04:00] using flame graphs. If you've never used
[04:01] a flame graph before, here one is
[04:03] they're actually not too confusing.
[04:05] They're actually pretty simple. How you
[04:07] read this is that you read this as uh
[04:10] from the very bottom. This is like the
[04:12] very bottom function call and then each
[04:13] one of these little tops. These are all
[04:15] different function calls. Now, the
[04:16] ordering doesn't necessarily matter.
[04:18] These are not uh these are not time
[04:20] dependent. Instead, you look at the very
[04:22] top and this top part. This is the
[04:25] percentage of the program that while
[04:27] running was within this function right
[04:29] here. So you just kind of look at it as
[04:31] like relative portions. You can say that
[04:33] hey the time spent closing a file. This
[04:36] operation right here looks to it was
[04:39] like 33% of the time of getting user
[04:42] time was just spent closing a file. What
[04:45] appears to be like 16%. Oh, hold on. I
[04:47] just realiz I forgot that they have
[04:49] this. It's 34% of the time. I forgot
[04:51] that it has like a little percent sign
[04:52] right there when you hover over it. uh
[04:54] read was 16.8% of the time and f open
[04:57] was 43% of the time. Yes, most of that
[05:00] time if you did quick maths in your head
[05:02] about 90% of the time was spent just
[05:05] just fangling and jangling around with
[05:08] files. This right here, this was the
[05:10] scan f time. Like very little just only
[05:13] 3.9% of the time was it actually doing
[05:16] something. The rest of the time is just
[05:18] off in file land hopping and doing the
[05:20] who whoever knows what all these little
[05:22] futexes and everything. These fast user
[05:24] space mutexes. Okay. Hey, get my mutex
[05:28] out your mouth, buddy. I actually I have
[05:30] no idea what that means. And of course,
[05:32] the change, this is what the change
[05:33] looks like. Now, you can tell right away
[05:35] that something's happened. Okay. You
[05:36] don't have to be a genius here. You
[05:37] don't really have to understand how this
[05:39] works to look at it and just say, "Hey,
[05:40] it just looks like a lot of stuff is not
[05:43] happening anymore. There's one little
[05:44] peak right here, one little flame.
[05:46] There's one super thin flame right here.
[05:47] We don't really care what that is. And
[05:49] that's it. It's just it's obvious. Okay.
[05:52] Very little things are happening.
[05:53] Jeremir was nice enough, of course, to
[05:55] actually do the benchmarking also, so
[05:56] that way we can have some real times.
[05:58] And it went from about 11 microsconds to
[06:01] 279 nconds. Now, this is shocking,
[06:04] right? I would have never I just would
[06:06] have never guessed that I would have
[06:07] been spending a lot of time. And by a
[06:10] lot of time, I mean it's micro seconds.
[06:11] Yeah, sure. You're right. It's not like
[06:12] a ton of time out there. Uh, but
[06:14] nonetheless, I would have just never
[06:16] guessed it. I would assume that's like
[06:17] the fastest pop possible operation. I
[06:20] would have never investigated it at any
[06:22] point, but this is what happened. This
[06:24] is just like a recent fix from just a
[06:26] couple weeks ago. And I just think these
[06:27] kind of investigations are super cool. I
[06:29] really do appreciate these write-ups.
[06:31] There's even more cool information
[06:32] within this write up about how it
[06:34] everything exactly works. But I just
[06:37] love the fact that there are just people
[06:39] out there making things better all the
[06:41] time, especially these super intense
[06:43] ones. And then you just get to read
[06:44] about just like, oh my gosh, like I
[06:46] would have never would have thought. I
[06:48] just would have never even put together
[06:50] that getting user time would have been
[06:52] so dang complicated. I just thought it
[06:54] was interesting. Okay, I thought I'd
[06:55] take my time and share a little
[06:56] something. By the way, if you like a
[06:58] little bit more of a technical one,
[06:59] okay, hey, the thing is is engineering
[07:00] is fun. I actually really like
[07:02] engineering even if I don't work in the
[07:04] JDK. I don't program C++. Okay, I don't
[07:07] do any of that. But it's still awesome
[07:09] to read this stuff. It's still super
[07:11] cool to look at it. And uh I I just
[07:13] enjoy, you know, enjoy engineering at
[07:15] its finest. So, I hope you enjoyed it,
[07:17] too. Hey, press that like button or
[07:18] something. Tell me you liked it or tell
[07:20] me you don't like it. Honestly, I don't
[07:22] really care whichever whichever one you
[07:24] choose. Don't don't be don't be a grump,
[07:26] okay? But don't be a grump. The name is
[07:29] the prime engine. Hey, do you want to
[07:31] learn how to code? If you want to become
[07:33] a better back-end engineer, well, you
[07:35] got to check out boot.dev. Now, I
[07:36] personally have made a couple courses
[07:37] from them. I have live walkthroughs free
[07:40] available on YouTube of the whole
[07:41] course. Everything on boot.dev you can
[07:44] go through for free. But if you want the
[07:46] gamified experience, the tracking of
[07:48] your learning and all that, then you got
[07:49] to pay up the money. But hey, go check
[07:51] them out. It's awesome. Many content
[07:52] creators you know and you like make
[07:55] courses there. boot.dev/prime for 25%
[07:58] off.
