[00:00] Picture
[00:09] an optimal approach for storing and
[00:11] retrieving data. Does something like
[00:13] this come to mind?
[00:14] &gt;&gt; Well, your mom tells you not to do,
[00:15] which is just like throw everything all
[00:17] over the floor in random locations is
[00:20] something that actually works on a
[00:21] computer. It's a very nonhuman data
[00:25] structure. These data structures called
[00:28] hashts are essential to modern
[00:30] computing.
[00:31] &gt;&gt; Hashts are really a generalpurpose tool
[00:34] that a program can then use on the fly.
[00:36] &gt;&gt; Hashts are designed to insert or store
[00:39] elements of information in empty slots
[00:42] and then search for these elements via
[00:44] queries.
[00:44] &gt;&gt; The big challenge in hasht design is the
[00:48] trade-off between the fullness of the
[00:50] hash table versus the insertion and
[00:52] query time. There's this tension between
[00:55] time and space.
[00:57] &gt;&gt; In 2025, a student and two co-authors
[01:00] published research that overturn the
[01:02] field's decadesl long understanding
[01:04] about the limits of how hashts can
[01:07] function.
[01:08] &gt;&gt; It is very impressive when an undergrad
[01:11] disproves a long-standing important
[01:13] conjecture of a touring award winner.
[01:16] But he actually did something more
[01:18] exciting.
[01:20] Hashts use an algorithm called a hash
[01:22] function to efficiently store and
[01:24] retrieve data. Like a librarian who uses
[01:27] an ingenious system to shelf books that
[01:30] speeds up locating them later on.
[01:32] &gt;&gt; The hasht can in principle do these very
[01:36] clever things in order to make these
[01:39] insertions and these queries be very
[01:41] timeefficient.
[01:43] &gt;&gt; The first hasht was invented in the
[01:45] 1950s by IBM engineer Hans Peter Lon. He
[01:49] had this insight that what you want to
[01:50] do when you're building a hash table is
[01:53] you want to use randomness to your
[01:56] advantage.
[01:57] &gt;&gt; The hash function uses randomness to
[01:59] help select locations in memory. It then
[02:02] inserts information in the first open
[02:04] slot it finds.
[02:06] &gt;&gt; Basically, you just try a bunch of
[02:08] random spots until you find a free one.
[02:11] In 1985, the computer scientist Andrew
[02:13] Yao, who would go on to win the touring
[02:15] award, the field's highest honor,
[02:17] concluded that this approach called
[02:19] uniform probing was the best possible.
[02:22] &gt;&gt; So Yao's paper had this really fantastic
[02:25] theorem that showed that yes, uniform
[02:28] probing is optimal.
[02:29] &gt;&gt; But optimal isn't always fast. As memory
[02:32] gets full, it can take longer and longer
[02:34] to find an empty slot. That last guy you
[02:38] need to insert, that's the killer,
[02:40] right? You're going to have to look and
[02:42] look and look. In the very basic table,
[02:44] if you have a million items, the last
[02:46] item you insert, you have to look in
[02:48] basically a million locations.
[02:50] &gt;&gt; And most computer scientists believed
[02:52] Yao's conclusion that this was the best
[02:54] that could be done.
[03:00] Four decades later, Andrew Karpivven met
[03:02] his future collaborators while in
[03:04] undergrad at Rutgers University.
[03:06] &gt;&gt; And he was taking my graduate algorithms
[03:08] class and he came up to me and says,
[03:10] "Oh, I have an improvement to your tiny
[03:12] pointers paper."
[03:13] &gt;&gt; While tinkering with his mentors data
[03:15] objects called tiny pointers, Andrew
[03:18] ended up inventing his own hasht.
[03:20] &gt;&gt; That hasht is a very simple counter
[03:24] example to Yao's conjecture. It kind of
[03:26] opened our eyes. is we said, "Wow, maybe
[03:29] our understanding of this area is not as
[03:30] complete as we thought."
[03:32] &gt;&gt; So, the team dived into the literature
[03:34] on the topic while continuing to develop
[03:36] a string of Andrew's new ideas.
[03:38] &gt;&gt; We ended up discovering this much more
[03:40] surprising result, which was that it's
[03:42] not just that Yao's conjecture isn't
[03:45] true. There's actually a way to just
[03:47] entirely bypass Yao's theorem.
[03:51] In their recent paper, Andrew and his
[03:53] collaborators constructed a new kind of
[03:55] hash table that doesn't always put data
[03:57] in the first empty slot.
[03:59] &gt;&gt; I'm going to look ahead and if I find a
[04:01] free slot that is for some reason a slot
[04:04] that I really want to fill, I will fill
[04:07] that slot instead. You're just not
[04:09] required to take the first one you can
[04:11] find. And it does better. That to me was
[04:15] completely shocking. And their hasht has
[04:18] another surprising property, a near
[04:21] constant average query time, which is
[04:23] something Yao thought impossible.
[04:26] &gt;&gt; We discovered that if you don't insert
[04:28] in the first spot,
[04:29] &gt;&gt; the queries are super fast on average.
[04:32] Actually, your average doesn't even
[04:33] depend on how full your table is. Even
[04:35] if you fill it up 100%, your average
[04:38] will still be some fixed number. The
[04:40] main result of the paper says there is
[04:43] no fundamental tension between space and
[04:46] time.
[04:52] Over the last two decades, dozens of
[04:54] research teams have raced to be the
[04:56] first to build a practical paradigm
[04:58] shifting quantum computer.
[05:00] &gt;&gt; The hope is that by building this
[05:01] quantum computer, we'll be able to solve
[05:02] these these problems that are basically
[05:04] completely intractable using uh
[05:06] classical machines. But the unique
[05:08] challenges of working with cubits, the
[05:10] finicky fundamental building blocks of
[05:12] quantum computers, have long kept this
[05:14] reality out of reach. We have a chasm, a
[05:18] chasm between what is physically
[05:20] achievable and physical cubits regarding
[05:22] error rates. How do we cross that chasm?
[05:24] Well, we're going to try to use quantum
[05:26] error correction as a bridge.
[05:28] &gt;&gt; In a major first, a team at Google
[05:30] surpassed a key milestone in quantum
[05:32] error correction, charting a path
[05:34] forward. Finally, you can kind of see in
[05:36] practice what we kind of already knew
[05:39] would happen in theory for like 20
[05:41] years, 25 years. So, yeah, that's very
[05:45] &gt;&gt; Unlike classical computers that perform
[05:47] calculations using bits that are either
[05:49] zeros or ones, quantum computers harness
[05:52] the unique properties of quantum
[05:54] mechanics.
[05:55] &gt;&gt; A cubit at the end of the day, it's kind
[05:57] of a mathematical object. A cubit can be
[05:58] sort of a continuum of states, including
[06:00] superpositions between 0 and one. By
[06:03] manipulating the collective states of
[06:04] cubits, quantum computers can perform
[06:07] powerful calculations. But performing
[06:09] calculations with cubits is tricky.
[06:12] Errors easily creep in.
[06:14] &gt;&gt; You can have a continuum of states,
[06:15] which means you also have a continuum of
[06:17] errors you need to correct. Sort of an
[06:19] infinity of errors
[06:20] &gt;&gt; and any single error can ruin the whole
[06:22] calculation.
[06:24] In the 1990s, the mathematician Peter
[06:27] Shore devised a groundbreaking factoring
[06:29] algorithm that demonstrated the
[06:31] potential of quantum computing. But it
[06:33] required so many steps that many thought
[06:36] it could never run.
[06:37] &gt;&gt; If you have a probability of an error
[06:39] every thousand steps, then you're never
[06:41] going to get through an algorithm that
[06:43] is a trillion steps without making a
[06:45] mistake.
[06:46] &gt;&gt; There was basically a lot of skepticism
[06:48] that we could ever control quantum
[06:50] effects to that level of precision.
[06:52] Shore and others realized that it's
[06:54] possible in principle to correct errors
[06:56] by adding extra cubits. Then in 1998,
[07:00] Russian physicist Alexi Katay proposed
[07:03] one such technique called the surface
[07:05] code.
[07:05] &gt;&gt; The surface code very surprisingly
[07:07] simple scheme. We just place our cubits
[07:10] on a square lettuce and then perform uh
[07:14] local measurements on these cubits. With
[07:16] the surface code, cubits are arranged in
[07:19] overlapping grids consisting of data
[07:21] cubits and error measurement cubits.
[07:23] &gt;&gt; And so they're all sharing the quantum
[07:25] information in a very carefully
[07:27] orchestrated way such that we can check
[07:29] for local errors.
[07:31] &gt;&gt; And this collection of physical cubits
[07:33] functions as a single highquality
[07:35] logical cubit.
[07:37] &gt;&gt; We have many cubits work together to
[07:39] express a single more perfect cubit. And
[07:42] that single logical cubit is more
[07:43] reliable than any of its physical parts.
[07:48] In order to build a viable quantum
[07:50] computer, Google's quantum AI team first
[07:53] needed to overcome a major hurdle.
[07:55] Engineering reliable cubits.
[07:57] &gt;&gt; If your physical cubits are good enough,
[07:59] their performance is better than a
[08:01] certain threshold. Then as we add more
[08:03] and more cubits, then we'll
[08:05] exponentially reduce the errors that
[08:06] we're experiencing.
[08:07] &gt;&gt; But at first, the team's cubits weren't
[08:09] up to snuff.
[08:11] &gt;&gt; We've had systems that were very, very
[08:12] good, but nonetheless, the physical
[08:14] cubits weren't quite there. As we made
[08:15] the system larger, the error just got
[08:17] worse and worse. The the errors
[08:19] overwhelmed the error correction. We
[08:21] basically had to go back to the drawing
[08:22] board.
[08:23] &gt;&gt; After years spent improving their cubit
[08:25] design and scaling up the size of the
[08:27] surface code, the team finally put their
[08:29] new 72 cubit processor cenamed Willow to
[08:33] the test.
[08:33] &gt;&gt; We saw like a 40 or 50% error
[08:36] suppression improvement just on this
[08:38] first run. Seeing it work convincingly
[08:40] for the first time, it was a much more
[08:42] joyous route. they had crossed a
[08:44] critical threshold causing error rates
[08:47] to plummet exponentially.
[08:49] &gt;&gt; This is the first time the whole system
[08:52] is working well together where we can
[08:54] actually see the exponential with our
[08:56] own eyes and see that error cutting in
[08:58] half as we increase the code size.
[09:00] &gt;&gt; I'm kind of in awe of like the the
[09:02] engineering that kind of went into this.
[09:03] It's really really complicated. I think
[09:05] there's still uh a way to go um to make
[09:08] things practical. So I think this is
[09:10] kind of a demonstration of that that
[09:11] things work. We know now that we can
[09:14] build devices that are accurate enough
[09:17] that if they are scaled they will be
[09:19] able to solve some of the hardest
[09:21] problems uh that you know humanity
[09:23] faces.
[09:29] &gt;&gt; A key challenge for programmers is
[09:31] managing trade-offs between
[09:32] computational speed or time and space
[09:35] and memory.
[09:36] &gt;&gt; We want to minimize the the time that we
[09:39] take to solve problems. We also don't
[09:42] want our programs to consume a lot of
[09:44] memory.
[09:45] &gt;&gt; For decades, computer scientists assumed
[09:48] that for certain problems, the
[09:50] relationship between time and space was
[09:52] essentially fixed.
[09:53] &gt;&gt; If a computation used a certain amount
[09:55] of time, it will probably use roughly
[09:57] that amount of space.
[09:59] &gt;&gt; Now, in a groundbreaking paper, MIT
[10:02] researcher Ryan Williams has proved that
[10:04] you can always get away with a lot less
[10:06] space.
[10:07] &gt;&gt; His improvement was enormous. No, it was
[10:10] completely unexpected and I didn't
[10:12] believe it was true.
[10:14] &gt;&gt; The space-time problem is central to the
[10:16] field of complexity theory.
[10:17] &gt;&gt; Complexity theory studies what problems
[10:21] can be solved with efficient resources.
[10:25] &gt;&gt; The resource of time refers specifically
[10:27] to the number of steps a computation
[10:29] takes.
[10:29] &gt;&gt; Like say how many instructions that your
[10:32] processor goes through in order to find
[10:34] the end result. While space is the
[10:36] amount of memory utilized during this
[10:38] computation,
[10:39] &gt;&gt; how much space does it need to like
[10:41] store intermediate results in its
[10:43] computation while it's working?
[10:45] &gt;&gt; For many algorithms, the amount of space
[10:47] needed is roughly proportional to
[10:49] runtime.
[10:50] &gt;&gt; If you take t steps of time, then uh the
[10:54] amount of space you consume is only
[10:56] about tight. You can't really add any
[11:00] more to your memory in one step than
[11:02] like one more unit of space. The longer
[11:04] and longer a computation takes, the more
[11:07] and more memory it will use.
[11:09] &gt;&gt; In 1975, a trio of computer scientists
[11:12] found a way to tweak this dynamic. They
[11:15] devised what's called a universal
[11:17] simulation, a technique that could take
[11:19] any algorithm and convert it so it saves
[11:21] a little bit of space. From a
[11:23] theoretical perspective, this is amazing
[11:25] that you can even do this little bit of
[11:26] savings.
[11:27] &gt;&gt; But for the next 50 years, any further
[11:30] progress seemed impossible. there were
[11:32] like uh provable limitations on the
[11:35] particular strategy that people were
[11:37] using.
[11:39] &gt;&gt; In 2024, Williams curiosity was aroused
[11:42] by his students presentation on the work
[11:44] of researchers James Cook and Ian Mertz.
[11:47] The pair were focused on a seemingly
[11:49] unrelated problem called tree
[11:51] evaluation.
[11:52] &gt;&gt; When we worked on tree evaluation, we
[11:54] didn't think anything of uh space versus
[11:56] time in that way.
[11:57] &gt;&gt; Williams noticed something interesting
[11:59] at its core. The way the cook merch tree
[12:01] evaluation algorithm goes, they say,
[12:04] "Hey, what if you just try to reuse the
[12:06] space over and over? I've already got
[12:08] space that's already allocated. I'm
[12:10] going to add on top of it."
[12:11] &gt;&gt; The algorithm can squeeze more
[12:13] information into locations and memory
[12:16] already in use.
[12:17] &gt;&gt; Adding in a bunch of extra things, but
[12:20] all the extra things are going to cancel
[12:22] out, but you didn't get have to use
[12:24] extra space. Williams also realized that
[12:27] Cook and Mertz's approach could possibly
[12:29] be used for something more wide ranging.
[12:32] &gt;&gt; It gives a very specific, very
[12:34] well-defined procedure for taking sort
[12:36] of any computation and re-implementing
[12:39] it so that it uses drastically less
[12:41] space than before.
[12:43] &gt;&gt; So, Williams wrote down his thoughts
[12:45] before setting them aside for a few
[12:47] months.
[12:48] &gt;&gt; I just thought this was like another one
[12:50] of my hairbrain ideas. I went back, I
[12:52] returned, I decided, okay, I'm just
[12:54] going to confirm that this thing doesn't
[12:57] work.
[12:58] &gt;&gt; But it did work and it functions as a
[13:00] universal simulation that converts any
[13:03] algorithm to save a substantial amount
[13:05] of space.
[13:06] &gt;&gt; In my uh paper uh I show that uh
[13:10] actually time t in this very general uh
[13:14] framework can be simulated only about
[13:16] square root of t space. It's a it's a
[13:19] it's a drastic space savings and this is
[13:22] true regardless of uh the the kind of
[13:25] computation you're running. When it
[13:27] comes down to it, all I'm all I did was
[13:28] sort of uncover the magic that was
[13:30] already there.
[13:31] &gt;&gt; So Ryan did the most important thing
[13:35] that you could do, which is that he drew
[13:37] a connection between things that were
[13:39] already in the literature and then put
[13:43] in the pure elbow grease to make the
[13:44] whole thing work. I'm in awe of uh the
[13:48] work that he did, but of course I'm also
[13:50] thrilled to have played a part in it.
