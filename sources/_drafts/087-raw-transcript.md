[00:05] Hey, it's Steve Eisman and we're going
[00:07] to talk about AI today with our guest.
[00:10] This is a topic that we have explored
[00:13] for many, many months. It is crucial to
[00:16] the future of the US economy. Recently,
[00:19] hyperscalers have announced that they
[00:21] are increasing their budgets enormously.
[00:25] The top four hyperscalers are going to
[00:27] literally spend $650 billion dollar
[00:30] alone on tech stuff all related to AI.
[00:34] The future of the US economy is really
[00:36] at stake. And a few weeks ago we had on
[00:40] Gary Marcus who's a big critic of LLMs
[00:43] and argues that they are losing their
[00:45] efficaciousness. And so I wanted a
[00:47] second opinion because this is just too
[00:49] important a topic. And so today we have
[00:52] Columbia professor Danny Guetta who as
[00:54] you'll see agrees with Gary on certain
[00:57] points but disagrees on others and we're
[01:00] going to explore all of that and
[01:02] afterwards I'll be back to talk about
[01:04] what we've learned.
[01:08] Hi, this is Steve Eisman and welcome to
[01:10] another episode of the real Eisman
[01:12] playbook. And today we're going to
[01:14] explore the world of AI, but not per se
[01:17] from a business perspective, but from
[01:19] the within the guts of AI, you know, is
[01:22] AI a bubble? Is it going to change the
[01:24] world? You know, these are questions
[01:25] that we've explored over in our podcast
[01:28] over the last many, many months. And to
[01:31] help us go further is our guest,
[01:33] Professor Daniel Gua, who was a
[01:35] professor at the Columbia Business
[01:37] School. Daniel, welcome.
[01:39] &gt;&gt; Thank you so much for having me, Steve.
[01:40] This is going to be great. Really
[01:41] excited for the conversation. really
[01:43] excited. So before we get started, why
[01:44] don't you just give us a little bit
[01:46] about your background to explain why
[01:48] you're here?
[01:48] &gt;&gt; Yeah. No, absolutely. I mean, my whole
[01:50] sort of career has been working on kind
[01:52] of AI even before it was cool. Uh so I
[01:55] started off doing my PhD in datadriven
[01:58] supply chain management a while back and
[01:59] I was really lucky. I got to spend some
[02:01] time at Amazon doing that which
[02:02] obviously is a great place to study uh
[02:04] supply chains. After that PhD, I went to
[02:06] work at Palanteer Technologies. Um,
[02:09] yeah, I was not a US citizen at the
[02:10] time, so they didn't let me close to the
[02:12] government stuff, but I did get to work
[02:14] a lot on their commercial business and
[02:15] that just involved going around the
[02:17] world working with companies in just a
[02:18] whole range of industries and helping
[02:20] them figure out how to do what they do
[02:22] better, but using data, AI, analytics,
[02:25] that kind of stuff. And then around
[02:26] eight years ago, uh, the dean of the
[02:29] business school at Colombia, uh, Cassis
[02:31] McLaras, he kind of already back then
[02:33] had the foresight to realize that this
[02:34] kind of data analytics wave was, you
[02:37] know, not going anywhere, that it was
[02:38] here to stay. And so he asked me if I
[02:40] would come back to Colombia to kind of
[02:41] help build up the data and analytics
[02:43] curriculum. And that's kind of what I've
[02:44] been doing there. And, you know, I get
[02:45] to work with companies, help them figure
[02:47] out how to get value out of AI. I get to
[02:49] teach classes on AI, operations, coding,
[02:52] all that kind of stuff. And I'm very
[02:53] lucky to get to teach our MBA students,
[02:56] engineering students, executives, but
[02:58] then also um we even launched this open
[03:00] program with Wall Street prep. So now
[03:02] anyone can take that program. The reason
[03:03] I mentioned it is because we were
[03:05] introduced by a student of mine from
[03:06] that program. So hat trip to Ari. Thank
[03:08] you for the introduction. Yeah.
[03:10] &gt;&gt; So let's let's start with um the big
[03:13] topic which is large language models.
[03:16] Before we talk about how efficacious
[03:18] they are, you know, when when you watch
[03:22] business news, they all they're really
[03:24] talking about is how many chips are
[03:26] being bought? Who's who's ahead? Is it
[03:29] Google? Is it OpenAI? But let's go to
[03:31] let's get to basics. What exactly is a
[03:34] large language model? And how does it
[03:37] work?
[03:37] &gt;&gt; It's a great question and I think if I
[03:39] may, I think it makes sense to even take
[03:40] one step back and to say what even is
[03:42] AI? Like I think large language models
[03:44] have almost become synonymous with AI in
[03:46] people's minds, but they're not. I mean,
[03:48] that is not the only thing AI is. And I
[03:50] think it's actually helpful to think of
[03:52] two different kinds of AI. You have kind
[03:54] of predictive AI that you also hear
[03:56] called machine learning or predictive
[03:57] analytics. And that's been around for a
[03:59] while and very successful for a while.
[04:01] And then you have Gen AI, so including
[04:02] those large language models that have
[04:04] been uh kind of more recent. And it's
[04:06] actually really helpful to dig in to
[04:07] what each of those two mean because as
[04:10] we'll see it's really like understanding
[04:12] what those two things are really makes a
[04:13] difference to understanding how large
[04:15] language models work and how they sort
[04:16] of fit into the broader landscape. So if
[04:18] we start with this predictive AI been
[04:20] around for a while since the 80s or '9s
[04:22] and and the idea really is to just say
[04:24] can we look at a data set can we
[04:26] identify patterns in the data set and
[04:28] can we kind of do something useful with
[04:30] those patterns and so my favorite
[04:31] example is uh the Zestimate. You know,
[04:33] when you go on Zillow and you look at a
[04:35] property, it gives you the the estimated
[04:37] price of what that property would be. I
[04:39] always joke with my students, right?
[04:40] There's like all kinds of lofty reasons
[04:41] you might use it, like real estate
[04:43] development to buy a house, sell a
[04:44] house. Really, people are using it to
[04:45] find out how rich their neighbors are.
[04:47] So, that that number, right, that you
[04:48] just get when you go,
[04:49] &gt;&gt; how expensive is the house that's next
[04:51] door to me?
[04:51] &gt;&gt; How expensive is the house that's next
[04:52] door to me? That's exactly right. So,
[04:53] you know, that is a machine learning
[04:55] model. That is a predictive AI model. It
[04:57] uses stuff about the property to predict
[05:00] what it price is going to be. And if you
[05:02] were thinking, you know, how does it
[05:03] work? Obviously, it's quite complex. But
[05:05] if you were to build a slightly simple
[05:06] version, maybe just with houses on
[05:08] upware site, what could you do? Maybe
[05:10] you'd look at the square footage of the
[05:11] property plus, you know, the number of
[05:13] bedrooms, number of bathrooms, and then
[05:15] maybe you'd say every square foot is
[05:17] worth 2,000 bucks, every bathroom is
[05:19] worth 10,000 bucks, whatever. Add them
[05:21] all up.
[05:22] &gt;&gt; It'd be a fairly simple model.
[05:23] &gt;&gt; Fairly simple model. Now,
[05:25] what makes it a machine learning model
[05:27] rather than just like a sum you come up
[05:29] with yourself is the fact that the way
[05:31] Zillow creates it is they train it using
[05:33] historical data. And what do I mean by
[05:35] that? They're going to take a huge trove
[05:37] of data, right, from uh uh previous
[05:40] properties that have sold. They're going
[05:41] to look at data about those properties
[05:43] and they're going to start with totally
[05:44] random numbers for the value of each
[05:46] element. So, they might begin by saying
[05:48] a square foot is worth $1. Totally
[05:49] incorrect. That's going to give really
[05:51] bad predictions. But then they tweak
[05:53] that number, okay, until it fits the
[05:55] data as closely as possible, right? And
[05:57] that's absolutely fundamental as we'll
[05:59] see later to even how large language
[06:00] models are trained. And just in
[06:02] terminology, this is called training.
[06:04] The kind of tweaking of those numbers
[06:06] and you often hear something called
[06:07] parameters or weights. That is what
[06:09] those numbers are. They're kind of
[06:10] parameters or weights of those of those
[06:12] models. Uh and so you're tweaking them
[06:14] as you sort of create uh create the
[06:15] model.
[06:16] &gt;&gt; Okay. So that's been around for a long
[06:18] time.
[06:18] &gt;&gt; That's been around for a long time.
[06:19] Absolutely. And just it's worth just
[06:21] saying it's been around for a long time,
[06:22] but I think today if you tell me like if
[06:24] you look at the value generated by AI,
[06:26] what percentage of it comes from that,
[06:28] it's huge and it's still massive. Every
[06:30] time you swipe a credit card, fraud
[06:31] analytics, uh figuring out if someone
[06:34] should be able to borrow money, sort of
[06:35] uh uh you know, uh creditworthiness, um
[06:37] when you order a lift, right, how much
[06:39] it should cost and what the length of
[06:40] the trip is going to be, all that is
[06:41] really sort of based on that AI. So, you
[06:44] know, how's that different from the new
[06:45] kind of AI, the Gen AI, the LLMs? The
[06:47] problem with that old kind of AI is that
[06:49] it only really works with numbers, with
[06:51] numerical data, stuff you can put in
[06:52] Excel. So, thinking back to this
[06:54] estimate, you can use the square
[06:55] footage, the number of bedrooms, number
[06:57] of bathrooms, but what if you want to
[06:59] use the image, right, the picture of the
[07:01] house, or you want to use the text that
[07:02] you see inside the description.
[07:04] &gt;&gt; You can't really put that in a model
[07:06] like that because you can't multiply
[07:07] text. It's not a number, right? You
[07:08] can't do anything with it. and uh uh you
[07:10] know uh so that kind of was a limitation
[07:12] of those uh models and really that's
[07:15] where the deep learning the genai
[07:17] revolution sort of came along and
[07:18] overcame that limitation right so this
[07:21] was maybe in the mid2010s I mean it's
[07:23] started at various times but let's say
[07:25] sort of the mid2010s this new field
[07:26] called deep learning came along that
[07:28] introduced these models called deep
[07:30] neural networks and large language
[07:32] models are an example of those deep
[07:33] neural networks and what they can do is
[07:36] just like as a human you're if we're
[07:38] reading a piece of text, we kind of
[07:41] understand what it says. We get kind of
[07:42] the concept behind the piece of text.
[07:44] Those models can also do that, right?
[07:46] And the way they do that is by using an
[07:49] enormous number of parameters, an
[07:50] enormous amount of data. And maybe we'll
[07:52] get into how that works, right? Sort of
[07:54] mysteriously, but they're effectively
[07:55] using just enormous amounts of data to
[07:58] understand what's going on behind the
[07:59] text. But I think it's important to
[08:01] point out, and you discussed this with
[08:02] Gary Marcus a few weeks ago, and we'll
[08:03] touch on it today again, maybe
[08:05] understanding is a misnomer, right?
[08:07] because all they're doing is they're
[08:09] training themselves on historical data
[08:11] and trying to mimic those patterns. And
[08:12] so is that understanding? Is that not
[08:14] understanding? And maybe we'll we'll get
[08:16] into that, but that's how these models
[08:17] work. And sort of they overcame that
[08:19] limitation of machine learning because
[08:21] they're now able to use all this
[08:22] unstructured data.
[08:23] &gt;&gt; So
[08:25] what can a large language model do
[08:30] that the old probabilistic AI can't do?
[08:35] Give us an example.
[08:36] &gt;&gt; Yeah. So first of all, I don't know that
[08:38] it necessarily makes sense to say large
[08:41] language model versus probabilistic AI.
[08:43] These large language models are a kind
[08:45] of probabilistic AI, right? I mean they
[08:47] they sort of, you know, are a much
[08:48] bigger version. They have many more
[08:50] parameters. They have many more sort of
[08:51] uh so that's the first thing to point
[08:53] out, but generally it is that idea of
[08:55] looking at completely unstructured data.
[08:57] I mean that is sort of you know their
[08:59] magic. that is what they're able to do.
[09:00] A historical sort of one of those
[09:02] historical probabilistic AI, machine
[09:04] learning, predictive AI models couldn't
[09:06] look at a piece of text and understand
[09:08] what it says. Now, people had ways to
[09:09] get around that. They would say like,
[09:11] oh, if I want to understand a piece of
[09:12] text, let me look at the number of happy
[09:14] words in the piece of text. Like, you
[09:16] know, if the text says wonderful and
[09:18] amazing and fantabulous and whatever,
[09:20] then that means it's probably positive.
[09:21] But those were very sort of uh
[09:23] simplistic ways of looking at text.
[09:25] these large language models can actually
[09:27] look at text and kind of almost
[09:28] understand it.
[09:29] &gt;&gt; So why do large language models
[09:33] hallucinate? And let's talk about
[09:35] exactly what's a what is a
[09:37] hallucination?
[09:38] &gt;&gt; That's a great question. If you'll allow
[09:39] me, this is going to be a very long
[09:41] answer, but I think to kind of get to
[09:43] kind of I I want because I've, you know,
[09:45] I gave an example about a recent
[09:47] hallucination which I just discussed
[09:49] with Gary Morris, which was on the day
[09:51] that uh Madura was taken out of
[09:54] Venezuela, within like the first hour,
[09:56] um people went on to chat GPT and said,
[09:58] "What's going on with Madura getting
[10:00] taken out of Venezuela?" And chat GPT
[10:02] responds, "Maduro is still in
[10:03] Venezuela." Right? Because because
[10:06] apparently large language models have a
[10:08] problem with novelty, but let's talk
[10:10] about hallucination.
[10:11] &gt;&gt; Let's just tell you how they work. I
[10:12] mean, how those models work, how they
[10:14] end up hallucinating. Long story short,
[10:15] I'll tell you the answer already. What
[10:17] you should be surprised by is that they
[10:18] ever don't hallucinate, right? The fact
[10:20] they do hallucinate is kind of, you
[10:21] know, that's like not the surprising
[10:22] part.
[10:23] &gt;&gt; You got the right answer.
[10:24] &gt;&gt; The fact they ever get it right, right,
[10:25] is is crazy. So, okay, how do these
[10:27] models work? I'm going to explain it at
[10:28] various levels. Let's start at the top
[10:29] level. This is something your listeners
[10:31] may have heard already, but it's worth
[10:32] repeating. These are just autocomplete
[10:34] engines, right? So, I don't know if
[10:36] you've ever played a parlor game where
[10:38] you say a word, the next person says a
[10:40] word, the next person says a word, and
[10:41] you kind of build up a story together.
[10:43] Yes, that is basically what they're
[10:45] doing. So, for example, if you ask a
[10:47] model, you know, what is the capital of
[10:48] Argentina? It's going to look at the
[10:49] question, it's going to say, huh, I
[10:51] wonder what the next word would be.
[10:53] Maybe the capital of Argentina. And it
[10:56] would say, oh, buenos might be the next
[10:58] word. And then, and this is key, it's
[11:00] going to look back at the full
[11:01] conversation. What is the capital of
[11:03] Argentina, Buenos? And then it's going
[11:05] to say, if that was a useful
[11:07] conversation between a chatbot and a
[11:09] human, what would the next word after
[11:11] that be? And it would say iris. And it
[11:12] would continue until it decides, I'm
[11:14] done. Now, by the way, just a side note,
[11:17] unrelated to hallucinations, but this is
[11:18] why part of the reason they're so
[11:20] expensive is every time you want the
[11:23] next word, you have to reprocess the
[11:25] entire conversation from the beginning,
[11:27] right? Which is kind of wild. So if
[11:29] you've already spoken to it for like you
[11:30] know you know 10,000 words to generate
[11:33] the 10,000 and1 word it has to reprocess
[11:36] all those 10,000 words through the
[11:38] model. So that's kind of crazy.
[11:38] &gt;&gt; That eats up a lot of energy.
[11:40] &gt;&gt; Eats up a lot of energy, which is why,
[11:41] you know, I mean, we could talk about
[11:42] energy. Certainly get certainly get
[11:44] energy.
[11:44] &gt;&gt; But okay, so now I understand why it
[11:46] eats up so much energy.
[11:47] &gt;&gt; That's why eat up so much energy. Now,
[11:48] how does it do that? How does it know
[11:49] what the next word is? And the key
[11:51] concept you need to get, and I promise
[11:52] you this is as technical as this gets,
[11:54] but I think it's just it really helps to
[11:55] kind of know this is a concept called an
[11:57] embedding. And what an embedding is is
[12:00] you take a word and you basically turn
[12:02] it to numbers. Right? You remember I
[12:03] said that the limitation of those
[12:04] machine learning models was they
[12:06] couldn't look at words. Well, those
[12:07] embeddings convert the words to numbers
[12:09] so the computers can understand them.
[12:11] Okay? And maybe the easiest way to kind
[12:12] of get what an embedding is, imagine you
[12:14] take uh every word in the English
[12:16] language and you give it two scores.
[12:18] &gt;&gt; The first score is how alive it is. So
[12:20] maybe a human gets a 10, a rock gets a
[12:23] zero, uh uh I don't know, a spider gets
[12:25] a five, a carrot gets a two. You get the
[12:27] idea.
[12:27] &gt;&gt; Yes.
[12:28] &gt;&gt; And then the second score is maybe how
[12:29] loud it is. So maybe a loud. Yeah. Maybe
[12:32] a baby gets a 10. Maybe, you know, rock
[12:35] gets a zero. Maybe a carrot gets a one
[12:37] because it's like quiet, but if you
[12:38] crunch into it, it makes a sound.
[12:40] &gt;&gt; So, every word has two scores.
[12:41] &gt;&gt; Every word has two scores. Now, you
[12:42] could imagine taking those scores and
[12:44] putting them on this kind of XYaxis,
[12:46] right? On a piece of graph paper,
[12:47] &gt;&gt; every word.
[12:48] &gt;&gt; Every word based on those scores. So,
[12:49] the x axis is how alive it is and the
[12:51] y-axis is how loud it is.
[12:54] &gt;&gt; And if you think of that piece of paper,
[12:56] you're going to start
[12:57] &gt;&gt; who gives the score.
[12:59] &gt;&gt; Love the question. I promise you we're
[13:00] getting there in like 30 seconds. This
[13:02] is like
[13:02] &gt;&gt; there's is there a referee?
[13:04] &gt;&gt; Oh, so it's the key key question, right?
[13:06] And that's the first question.
[13:07] &gt;&gt; Who's making that decision?
[13:08] &gt;&gt; Whenever I tell students, they always
[13:09] ask me that question. And the answer is
[13:11] is crazy. But we we we'll get there. So,
[13:13] you know, you have that piece of paper,
[13:14] you got the scores, and you can imagine
[13:16] you're now going to get these kinds of
[13:17] clusters, right? Like the the vegetables
[13:18] are going to be, you know, bunched up in
[13:20] one side, the humans are on the other
[13:21] side, etc. And the profound thing about
[13:23] that is that now those scores kind of
[13:25] give you they allow the computer to look
[13:27] at numbers and those numbers kind of
[13:29] tell you ah I know something about the
[13:31] word right if I tell you a word is like
[13:33] zero on the live scale and nine on the
[13:36] loud scale
[13:37] &gt;&gt; guess what it's going to be close to the
[13:39] cluster that contains like fogghorn and
[13:41] bell and all these sort of loud things.
[13:42] So it really gives you a vibe. Now to
[13:44] your question right who the hell decides
[13:46] these words and of course right two
[13:48] scores is not enough in reality if you
[13:49] want to really know a word you got to go
[13:51] for thousands and the answer of course
[13:53] is uh no one uh the answer is machine
[13:56] learning so back remember this estimate
[13:58] case you remember I told you in this
[14:00] estimate case you don't decide how much
[14:02] a square foot is worth or how much a
[14:04] bathroom is worth you just give the
[14:05] model sort of the the the the the data
[14:08] and it figures it out it tweaks the
[14:10] numbers until you get to a good sort of
[14:12] result and it turns out That's what
[14:14] happens with these embeddings. And this
[14:16] is truly a wild idea, but have you heard
[14:18] this fact? People say that these large
[14:20] language models are trained using all
[14:22] the text on the internet.
[14:23] &gt;&gt; Yes,
[14:24] &gt;&gt; you've heard that said. That is the
[14:25] training data they use. So, let me
[14:26] explain how it works. They'll take
[14:28] something like two words, let's say like
[14:30] king or queen, two words. Those two
[14:32] words, if you look on all the internet,
[14:34] often they're going to be close to each
[14:36] other when you see king. And so the
[14:38] algorithm is going to realize, wait a
[14:39] second, those two words or my x and y on
[14:42] my piece of graph paper, they should be
[14:43] close to each other because they often
[14:45] occur together. And so they're going to
[14:46] tweak the scores by a few decimal points
[14:48] to get to get them closer to each other.
[14:50] &gt;&gt; On the other hand, a word like, I don't
[14:52] know, Pringle and existentialism, right?
[14:54] Probably far apart. And so they're going
[14:55] to be tweaked to get further apart.
[14:57] &gt;&gt; Okay.
[14:57] &gt;&gt; And Steve, it's actually astonishing.
[14:59] But if you do that,
[14:59] &gt;&gt; so the scores are constantly changing.
[15:01] &gt;&gt; Constantly changing while the model is
[15:03] being trained. So while OpenAI is
[15:04] training that model and amazingly if you
[15:06] do that enough you end up with something
[15:09] that actually captures the meaning of
[15:10] words. So you actually get clusters of
[15:12] words that mean the same thing. You get
[15:14] these crazy relationships where like if
[15:16] you look at the difference numerically
[15:18] on the graph paper between fkaca and
[15:20] baguette it's kind of the same
[15:22] difference as between France and Italy.
[15:24] So it kind of understands the concept of
[15:27] like country, right? And by the way I
[15:28] mentioned this before our podcast. We'll
[15:30] put a link in the show notes, but I
[15:31] created a little online tool that your
[15:32] listeners if they're interested, they
[15:34] can go actually check this out and try
[15:35] with a bunch of words. Um, and so at a
[15:37] high level that is sort of how a large
[15:39] language model understands text. There's
[15:42] another complexity which is that of
[15:43] course one word is not enough. You want
[15:45] words in context, right? So if I say I
[15:48] like figs and dates, I have a date
[15:51] tonight and what is today's date? The
[15:53] word date means very different things.
[15:55] And so there and just again to maybe
[15:57] link this to something some words your
[15:59] listeners may have heard. I don't know
[16:00] if you've heard of something called the
[16:02] transformer. So it's this uh uh uh uh
[16:04] mathematical technique that Google
[16:06] published in 2017 that was kind of a big
[16:08] uh breakthrough. All the transformer is
[16:10] is Google realize how to make these
[16:12] embeddings pay attention to each other.
[16:15] &gt;&gt; Okay. So that was my big explanation. So
[16:16] how does an LM work and how does that
[16:18] link to hallucinations? I know you are.
[16:19] So I promise we're getting back to it.
[16:21] &gt;&gt; I'm waiting with bait and breath
[16:23] &gt;&gt; on the edge of your seat. I the answer
[16:24] is going to be a little disappointing.
[16:25] I'm warning you. But
[16:26] &gt;&gt; okay,
[16:26] &gt;&gt; basically when you ask a question of an
[16:28] LLM,
[16:29] &gt;&gt; yeah,
[16:30] &gt;&gt; it first take your question, it
[16:32] converts.
[16:33] &gt;&gt; I got to ask you, why was Sandy Kofax
[16:35] such a great baseball player?
[16:36] &gt;&gt; What was Sandy Kofax such a great
[16:37] baseball?
[16:38] &gt;&gt; Perfect question to ask.
[16:39] &gt;&gt; You're picking someone who was born in
[16:40] France and grew up in England. So I may
[16:42] or may not have heard of Sandy Kofax,
[16:43] but we're not going to tell the
[16:44] listeners that.
[16:45] &gt;&gt; Great. He was the greatest baseball
[16:46] pitcher in the early60s.
[16:47] &gt;&gt; Great baseball pitcher. Great.
[16:49] &gt;&gt; So what the model is going to do is it's
[16:51] going to take all the machinery I just
[16:52] described. It's going to get this big
[16:54] list of numbers that captures the
[16:56] essence of your question. So if you
[16:58] think again of our graph paper, it's
[17:00] going to put it in a position that kind
[17:01] of implies, oh, this is the vibe of the
[17:03] question that Steve just asked. And then
[17:05] it's literally going to say, what are
[17:07] the words around? What are the words?
[17:08] &gt;&gt; What are the words around Sandy Kof's
[17:09] greatest picture?
[17:10] &gt;&gt; Exactly. What are the sort of And then
[17:12] it's going to pick one of those words
[17:13] and then it's going to respond with that
[17:15] one
[17:15] &gt;&gt; and then it'll add another one.
[17:17] &gt;&gt; But it's going to go back to the
[17:18] beginning and search again and then add
[17:19] another one.
[17:21] &gt;&gt; Create those numbers again. Look at a
[17:23] word nearby and another one, another
[17:24] one, another one. So to your answer, why
[17:25] does it hallucinate? The real crazy
[17:27] question is why does it ever not
[17:29] hallucinate, right? All it's doing is
[17:32] it's getting that essence of your
[17:33] question based on all the text he's seen
[17:35] on the internet and everything it knows
[17:36] about where text is on the internet and
[17:38] then it just generates the next word
[17:40] next word and the next word.
[17:41] &gt;&gt; This is not what we would think of as
[17:43] thinking.
[17:43] &gt;&gt; Well, that's a absolutely amazing
[17:45] question. Um there's actually a uh trick
[17:48] that I love doing uh and I think this
[17:50] really brings it home for people whether
[17:52] this is thinking or not because you know
[17:53] I think
[17:54] &gt;&gt; take a step back a big question people
[17:55] are asking is this going to get more
[17:57] intelligent than humans right is this
[17:58] going to eventually scale
[18:02] how much can it scale is that thing so
[18:04] &gt;&gt; but what you're saying is it's it's
[18:05] almost like a miracle that you ever get
[18:07] the right answer
[18:07] &gt;&gt; exactly and I'll give you an example
[18:09] that really shows what how much of a
[18:11] miracle it is so if you ask a question
[18:13] to this model and you Say, I have a bag
[18:16] with five balls and the balls are
[18:18] labeled A B CDE E.
[18:19] &gt;&gt; Okay,
[18:20] &gt;&gt; pick one at random and tell me the
[18:22] letter on the ball.
[18:24] So, as a human, if I ask you this,
[18:26] &gt;&gt; you could tell me I could ask a
[18:27] 10-year-old and they would tell me, "Oh,
[18:29] well, you know, 20% of the time I'm
[18:30] going to get A. 20% of the time I'm
[18:32] going to get B. 20% of the time I'm
[18:33] going to get C."
[18:34] &gt;&gt; Right?
[18:35] &gt;&gt; It turns out what you can do with these
[18:36] large language model is, and you can't
[18:38] do this on chairg.com, but if you can
[18:40] code using something called API, you can
[18:41] actually do this. You can ask chair GPT
[18:44] when I ask you that question in your
[18:46] internal LLM brain, what are the
[18:49] probabilities you're thinking of? Like
[18:50] what do you think the next word should
[18:52] be? And it goes completely off the
[18:54] rails. So Jad GBT will tell you 50% of
[18:56] the time the answer should be C and 20%
[18:58] of the time it should be A and 5% of the
[19:00] time it's basically wrong. Now if you
[19:03] think about why that is, it makes sense
[19:05] because all chpt is doing it's taking
[19:07] your big question, it's embedding it.
[19:09] So, it's creating that essence, those
[19:11] numbers, right, that that get the vibe
[19:13] of the question. And then it's saying,
[19:15] what is the closest sort of word that
[19:17] maybe fits that answer, but that is not
[19:19] how a human works. That's just not how
[19:21] we think. It's just a very, very
[19:23] different mode of thinking. Now, I need
[19:24] to be clear.
[19:25] &gt;&gt; It's not obvious to me that that mode of
[19:27] thinking is in any way inferior to a
[19:29] human mode of thinking. I mean, who
[19:30] knows? But it's definitely different. It
[19:32] is not the same thing. Okay. Yeah.
[19:34] &gt;&gt; Hi, Steve Eisman here. When my kids were
[19:36] little, I woke up one morning in a
[19:38] panic. I realized that if something
[19:40] happened to me, my family would be
[19:41] completely unprotected. I immediately
[19:44] went out and got life insurance so that
[19:46] my family would be financially secure.
[19:48] And I have never regretted that
[19:50] decision. So stop procrastinating.
[19:52] Getting life insurance is much easier
[19:54] than you think. Fabric by Gerber Life
[19:56] makes it easy to start the year knowing
[19:59] your family has more financial
[20:01] protection this year. Fabric by Gerber
[20:03] Life is term life insurance you can get
[20:06] done today. Made for busy parents like
[20:09] you. All online on your schedule right
[20:12] from your couch. You can be covered in
[20:14] under 10 minutes with no health exam
[20:17] required. If you've got kids and
[20:20] especially if you're young and healthy,
[20:21] the time to lock in low rates is now.
[20:24] Fabric has flexible, highquality
[20:26] policies that fit your family and your
[20:29] budget. Like a million dollars in
[20:31] coverage for less than a dollar a day.
[20:34] Fabric has partnered with Gerber Life,
[20:36] trusted by millions of families like
[20:38] yours for over 50 years. There's no
[20:40] risk. There's a 30-day money back
[20:42] guarantee, and you can cancel at any
[20:44] time. Join the thousands of parents who
[20:46] trust fabric to help protect their
[20:48] family. Apply today in just minutes at
[20:51] meetfabric.com/isman.
[20:54] That's
[20:54] meetfabric.com/isman.mefabric.com/isman.
[21:02] Policies issued by Western Southern Life
[21:04] Assurance Company, not available in
[21:06] certain states, prices subject to
[21:08] underwriting and health questions. Hi,
[21:11] Steve Eisman here. I run a small
[21:13] business, so I know that running a small
[21:15] business is tough. And when it's time to
[21:17] get a loan, it can feel impossible to
[21:19] find a lender you actually trust. Big
[21:22] banks say no, and the internet is full
[21:24] of sketchy offers with sky-high rates
[21:26] and fine print you can barely read.
[21:29] Whether you need help covering payroll,
[21:31] managing cash flow, or investing in
[21:33] growth, you deserve better. That's why I
[21:36] recommend the small business
[21:37] marketplace,
[21:39] powered by Nerd Wallet. It's a free,
[21:41] easytouse platform that lets you compare
[21:43] real financing offers from trusted
[21:45] lenders all in one place. What I like is
[21:49] that you don't need Perfect Credit to
[21:51] get started. No spam, no bait and
[21:53] switch, just personalized options that
[21:55] fit your business needs. In the future,
[21:58] when my business needs a small business
[22:00] loan, NerdWallet is where I'm going to
[22:02] go. And here's the best part. For a
[22:04] limited time, when you visit
[22:05] nerdwallet.com/isman
[22:08] and fill out the no obligation form,
[22:10] you'll get VIP treatment and talk with a
[22:13] real person who knows all the ins and
[22:14] outs of small business lending. Don't
[22:16] risk your business on unreliable
[22:19] lenders. Go to nerdwallet.com/isman
[22:22] to find the funding you deserve. Fender,
[22:26] Inc. NMLS ID number 1240038.
[22:33] &gt;&gt; So let's just explore for a second
[22:36] um Gary Marcus for a little bit.
[22:38] &gt;&gt; Yeah, totally.
[22:39] &gt;&gt; Because you you watched the podcast.
[22:40] &gt;&gt; I did listen to your fascinating
[22:43] &gt;&gt; it was wonderful. I learned a ton. But
[22:45] if I could maybe sum up his argument, I
[22:48] think it would be two parts. He would
[22:50] argue that
[22:53] the improvements that we are getting as
[22:56] large language mod the model that's out
[22:58] there is we're going to keep scaling
[23:00] large language models and they're going
[23:02] to continue to get much much much much
[23:04] better until we reach whatever we're
[23:06] supposed to reach. and his his argument
[23:10] is that we're already at a point where
[23:12] large language models the improve the
[23:14] marginal improvement from chap GPT5 to
[23:18] four is less than four to three which
[23:20] was less than 3 to two and so you're
[23:22] getting diminishing returns and so that
[23:23] if we're really going to take this thing
[23:25] to where it needs to be we have to
[23:28] go back almost to the to the drawing
[23:30] board and and put in what he called
[23:33] world models to to train these things on
[23:35] much better that that that's one part of
[23:37] his argument And his other part of his
[23:39] argument is that given the way LLMs
[23:41] work, they're always going to
[23:42] hallucinate, which is a problem because
[23:44] hallucinations are a problem because if
[23:46] you use it, how do you know it's
[23:47] hallucinating?
[23:48] &gt;&gt; So, what do you think about all that?
[23:51] &gt;&gt; I got so many thoughts. Uh, so let's
[23:53] first I think uh, you know, just
[23:56] definitionally for your listeners just
[23:57] so that they sort of get where we are
[23:59] when we say scaling a model,
[24:00] &gt;&gt; right? When I describe those embeddings
[24:02] and those transformers and those
[24:04] parameters that you look at data and you
[24:05] tweak the parameters scaling just means
[24:08] more data you just create more not so
[24:10] much well more data as well that's one
[24:12] way of scaling it that's one dimension
[24:13] but the other dimension is actually more
[24:15] parameters more complexity in the
[24:17] calculations right and that's why by the
[24:19] way it takes so many more chips and so
[24:21] much more energy and so on
[24:22] &gt;&gt; so in other words a a word doesn't have
[24:25] two variables two scores it might have a
[24:27] thousand variables
[24:28] &gt;&gt; that is exactly one way you could scale
[24:30] and another way you could scale is those
[24:31] transformers which we didn't spend too
[24:33] long talking about but they also have
[24:34] their own set of parameters and there's
[24:36] many more than in the variables and the
[24:38] words and you can add to those we don't
[24:40] need to get into the details but
[24:41] basically adding parameters is a big
[24:42] thing okay so that's just the first
[24:44] thing I want to put out there that's
[24:45] what we mean by scaling and as you said
[24:47] the sort of at least zit guys for a
[24:48] while was that the more we scale the
[24:50] better these models are going to get now
[24:52] I do want to say one thing and Gary
[24:53] almost touched on that in your
[24:55] conversation and I want to you know and
[24:56] I think he probably would have talked
[24:57] about it further
[24:58] &gt;&gt; I want to point out what we mean better
[25:00] because we never ask like what exactly
[25:02] does that mean better what does it mean
[25:03] better uh better typically when a new
[25:07] model comes out better means that it
[25:09] performs better on a very very specific
[25:11] set of benchmarks the computer science
[25:13] community has a whole bunch of these
[25:14] benchmarks that these models get tested
[25:16] on and you know there's a bunch of
[25:17] examples one of them is called the
[25:18] massive multitask language understanding
[25:20] benchmark stands for MMLU it's basically
[25:23] you can think of it as like an SAT exam
[25:25] you give it you give the large language
[25:26] model this exam can it answer the
[25:27] question so I just want to put that out
[25:29] that you know doing well at an SAT exam
[25:32] is not necessarily
[25:34] it is part of intelligence but it's not
[25:36] the only thing about intelligence and so
[25:37] there's actually a lot of research going
[25:39] on now on what it means to actually test
[25:42] those models better like what other
[25:44] benchmarks could we use that maybe are
[25:46] uh sort of you know more revealing than
[25:48] the current ones we're using I actually
[25:49] have a colleague at the business school
[25:50] Hong Namkung and I'm very fortunate to
[25:52] get to work with him a bit he's trying
[25:54] to build benchmarks based on like work
[25:55] in Excel right can we give it an Excel
[25:57] spreadsheet and can it actually build
[25:59] the DCF or can it figure out what the
[26:01] error is in the formula. So anyway, a
[26:03] lot of research there on figuring out
[26:05] how those models can sort of uh can sort
[26:07] of uh be made uh sort of uh be tested
[26:10] sort of better. So that's the first
[26:11] thing I would say. Second thing I would
[26:13] say is that you know Gary in some ways
[26:17] I he has incredible knowledge of what
[26:20] actual intelligence is. I mean he's done
[26:21] so much research that's been through you
[26:23] know his life's work. One thing that
[26:25] mystifies me a little, someone who
[26:27] doesn't have Gary's knowledge, is I
[26:29] think we easily throw around phrases
[26:30] like, "Oh, are these models going to get
[26:32] better than humans? Are we going to get
[26:33] super intelligence?" I'm like, I don't
[26:35] know what that means exactly in the
[26:37] sense of like,
[26:37] &gt;&gt; well, I think they're all thinking, you
[26:38] know, we all watch Terminator growing up
[26:41] and we're just trying to figure out when
[26:42] that's going to happen, we'll have to go
[26:45] into hiding. You know, I can't actually
[26:48] overstate this because all the people in
[26:50] this world are like science fiction
[26:52] geeks and they they grew up on this.
[26:54] They take this very seriously. They're
[26:56] sincerely worried about this.
[26:58] &gt;&gt; You know, Steve, it's funny. It reminds
[26:59] me of a Have you seen Goodwill Hunting?
[27:02] So, you know, for those who don't know,
[27:03] it's a movie about there's this genius
[27:05] genius kid, but he's very led a very
[27:07] troubled life and his therapist is
[27:08] played by the late Robin Williams. And
[27:10] there's this scene in that movie that I
[27:12] just love where the therapist is sitting
[27:14] with with with Matt Damon who's playing
[27:16] the who's playing the kid and he's like,
[27:17] you know,
[27:18] &gt;&gt; you're so smart. If I ask you about
[27:20] Michelangelo, you could tell me
[27:21] everything about him, right?
[27:22] &gt;&gt; But can you tell me what it smells like
[27:24] in the Systeine Chapel? Or if I asked
[27:26] you about love, you could like recite
[27:28] &gt;&gt; a but do you know what it is to really
[27:30] love a woman?
[27:30] &gt;&gt; Exactly. So it's like it's an amazing
[27:32] scene and sometimes I think about that
[27:33] when it comes to large language model
[27:34] where it's so difficult to get your
[27:36] finger on what it means for a model to
[27:38] be human and sure the model sort of you
[27:40] know destroying all of us is maybe an
[27:41] extreme version of that but there's
[27:42] plenty of steps in between and so it's
[27:44] kind of it's kind of hard to uh to uh to
[27:46] define Gary clearly thinks that they
[27:48] can't scale to sort of you know a level
[27:51] where they have the same intelligence as
[27:52] humans and the truth is I don't think I
[27:54] disagree I certainly that most people I
[27:56] respect would probably agree that the
[27:58] current way large language models just
[28:00] like this predict the next word, predict
[28:01] the next word, predict the next word
[28:03] might not scale to sort of a level of uh
[28:05] of superhuman intelligence. But I do
[28:07] just want to point out it's very
[28:08] difficult to really get your finger on
[28:11] what that means and to kind of know sort
[28:13] of, you know, when you've uh when you've
[28:14] reached uh uh that point. Um a few more
[28:17] things to say here. I'll just give you
[28:18] the headlines and you tell me if you
[28:19] want to hear about them. Uh, another
[28:21] thing I'd want to probably talk about is
[28:22] the fact that, you know, I think maybe
[28:24] we'll get there at the end, but one
[28:25] thing we sometimes miss, you know, in a
[28:28] conversation about is this going to get
[28:29] super intelligent is even if it isn't,
[28:31] &gt;&gt; maybe it's worthwhile anyway.
[28:33] &gt;&gt; Maybe there's so, and I'm going to take
[28:35] away the maybe from that, there is still
[28:37] so much value in the models. If you told
[28:39] me today these models will never get
[28:41] better. They will hallucinate forever.
[28:43] They will whatever sort of the
[28:44] shortcomings are today, they will remain
[28:46] forever. I have personally seen in my
[28:48] work with companies there is still so
[28:50] much value that you can capture.
[28:51] &gt;&gt; Let's explore that.
[28:52] &gt;&gt; Yeah. I just want to say maybe we'll
[28:53] talk about that at the end. There's a
[28:54] lot of research going on now on just
[28:56] whole new paradigm. So you mentioned
[28:57] world models. That's one example. Maybe
[28:59] at the end we'll talk about those but
[29:00] I'm saying like the research it's not
[29:02] like it's not like people at OpenAI and
[29:04] Anthropic are just sitting there being
[29:05] like well we give up. They're just you
[29:06] know scaling is done and you know that's
[29:08] it. We're done. There's plenty of other
[29:09] places people are going but maybe let's
[29:10] get to value. Yeah. What do you think
[29:13] these large language given the project
[29:15] that ex as as it exists today? What do
[29:19] you think these and we'll get to the
[29:21] agentic stuff? We'll come to that. Let's
[29:24] just start with the large language. What
[29:25] are these things good for?
[29:27] &gt;&gt; When I think of the value that I get out
[29:30] of them, that people I've worked with
[29:31] get out of them, that companies get out
[29:32] of them, I think about them in three
[29:34] buckets. Okay?
[29:35] &gt;&gt; Right? One bucket is probably uh the
[29:38] least obvious. That's why I say it first
[29:40] is taking those classical machine
[29:42] learning models which as you correctly
[29:43] pointed out have been around for like
[29:44] years and making them better using those
[29:46] LLMs and we can talk about some examples
[29:48] of that.
[29:49] &gt;&gt; The second bucket is aai and we'll talk
[29:51] about that too. And the third bucket is
[29:53] and this sounds very it's the most
[29:54] obvious one but just using them as chat
[29:56] bots. Like I think they've been around
[29:58] now for a few years and so it's easy to
[30:00] just like lose track of how magical they
[30:02] actually are.
[30:03] &gt;&gt; So let's let's explore all three. Let's
[30:05] start with the first one.
[30:06] &gt;&gt; Let's start with the first one. So
[30:07] probably easiest to explore with
[30:09] examples but I've seen so many places
[30:11] where this genai can take classical
[30:13] machine learning and supercharge it. So
[30:15] let's start with the first example.
[30:16] Okay,
[30:17] &gt;&gt; suppose you run a website where there is
[30:20] um user content that is posted and this
[30:24] could be anything. Could be a social
[30:25] media network. It could be a e-commerce
[30:27] platform where people write reviews,
[30:28] anything like that, a Reddit, whatever
[30:30] it might be. One problem that bedevils
[30:33] websites like that, companies like that,
[30:34] and that's been the case forever is
[30:36] content moderation. Right? You've got to
[30:37] if someone posts a comment to your
[30:39] website, you've got to make sure it's
[30:40] not illegal, it's not abusive, it's not
[30:42] you're going to have a bunch of rules as
[30:43] to what what comments can go on there.
[30:45] And you know it may sound like a kind of
[30:46] esoteric operational thing but this is
[30:49] huge. I mean people pay enormous teams
[30:51] of people and these are expensive teams
[30:53] to really look through those websites.
[30:55] And it turns out the quality of content
[30:56] like if you look at Amazon
[30:58] &gt;&gt; a lot of the value Amazon provides not
[31:00] the only value but a lot of the value is
[31:02] the reviews right I mean there's a lots
[31:04] for example super super super valuable.
[31:07] And so forever, for a long time, these
[31:09] companies have been using machine
[31:11] learning models to try and identify,
[31:12] automatically flag what comments should
[31:14] go to a human, right? How do we look at
[31:16] something and figure out, ah, this might
[31:17] be suspicious. Let's send it to a human
[31:19] to review. So, for example, they might
[31:21] look for specific words, right? They
[31:23] might look for maybe the length of the
[31:24] message, the time it's posted, the
[31:26] location it's posted from, etc. The
[31:28] problem with that, and it goes back to
[31:29] the problem from your very first
[31:31] question, what can these LLMs do that
[31:32] that machine learning can't? they can't
[31:35] actually understand the meaning of the
[31:36] message, right? They can look for a word
[31:37] in it, but that doesn't tell them what
[31:39] the, you know, the full meaning of the
[31:41] message is. So, for example, right, this
[31:43] is a law. I don't know if it's true, but
[31:45] people used to think that if you write a
[31:47] message or post a video with the word
[31:49] kill on Instagram, it'll de prioritize
[31:51] it because it thinks it's bad. And so
[31:52] now people have started using the word
[31:54] unal alive instead of kill because hey,
[31:56] then the algorithm, you know, can't
[31:57] can't catch it. And so these machine
[31:59] learning algorithms were always bedeled
[32:01] by this problem that they what I've seen
[32:04] people do with tremendous success is
[32:06] they now say wait a second we're going
[32:08] to stick with these machine learning
[32:09] algorithms but we're going to inject
[32:11] some Gen AI into it by having the Gen AI
[32:15] look at these comments people are
[32:16] posting and getting the Gen AI to
[32:19] actually extract meaning from it because
[32:20] we saw it can do that right it can
[32:22] actually get meaning from those messages
[32:23] and so examples of ways people have done
[32:25] it the simplest way which is not
[32:26] necessarily the is you literally go to a
[32:29] chatbot, you give it the message, and
[32:30] you say, "Hey, give me a score from 1 to
[32:32] 10. How likely is it that this is bad?"
[32:34] And then it'll give you a number, and
[32:36] then you put that into your machine
[32:37] learning model. But an even smarter way
[32:39] that I've seen is you can take that
[32:40] message, and you remember going way back
[32:42] when we talked about embeddings. So, you
[32:44] can take the message, you can get
[32:46] numbers for that message, right? Put it
[32:47] on this XY axis. And then you can use
[32:50] those numbers, those scores, even though
[32:52] they don't really mean anything. They're
[32:53] just like the internal guts of the of
[32:55] the Genai. You can use those numbers as
[32:57] an indicator. Maybe you look at
[32:58] historical data and you say, "Wait a
[33:00] second. When that second score is high,
[33:02] that tends to be suspicious, so I'm
[33:04] going to maybe moderate it." And I've
[33:05] really seen people do that to great
[33:06] effect. And the truth is, I talked about
[33:08] content moderation. Any example, any use
[33:11] case where you want to make predictions
[33:13] and there is text involved. This can
[33:16] really provide a lot of value and can be
[33:17] very useful. And notice how in some ways
[33:19] hallucinations don't really matter
[33:21] because you're now I mean, they matter,
[33:22] right? you'd rather the model didn't
[33:23] hallucinate but you're not using the
[33:25] model by itself you're putting it in the
[33:27] context of a bigger machine learning
[33:29] model that you can control that you can
[33:30] evaluate that you can check and so
[33:32] that's just one example I think where
[33:33] you know huge value uh uh can be
[33:35] generated
[33:36] &gt;&gt; so that's that's one let's talk about uh
[33:38] what is this agentic AI that I keep
[33:40] &gt;&gt; funny we will get to agentic just so you
[33:42] know we will I'll skip to aentic that
[33:44] first category I had six examples ready
[33:46] but we we'll go I mean I'm only saying
[33:47] that to give you an idea that like there
[33:49] is just so much there's a lot there's a
[33:50] lot you can do
[33:51] &gt;&gt; you know I don't on CNBC, I hear the
[33:53] words agentic AI and I I guarantee you
[33:56] that nine out of 10 people that are
[33:58] talking about agentic AI have absolutely
[34:00] no idea what they're talking and I'll be
[34:01] the first one to admit that I don't know
[34:03] what it is. So what what is it?
[34:05] &gt;&gt; It's so buzzy. Um
[34:06] &gt;&gt; it's it is so buzzy. I have good news.
[34:08] It's like it's like you hear this word
[34:09] like it's going to save the world. It's
[34:11] going to wipe out the management
[34:12] consulting business. I mean Agentic AI
[34:15] has accomplished so much and it hasn't
[34:16] accomplished anything yet. So what is
[34:18] this thing? Who was it that quipped in
[34:20] the early days of the PC revolution that
[34:22] you know you see PCs everywhere except
[34:23] for the productivities numbers or I
[34:25] there was like anyway okay I have good
[34:27] news for you. Agentic AI is really quite
[34:28] simple. It's basically just a large
[34:30] language model. A chatbot with a pair of
[34:32] hands.
[34:32] &gt;&gt; What does that mean?
[34:33] &gt;&gt; So what what does that mean? It is a
[34:35] chatbot that is given the ability to do
[34:37] things in the real world like send a
[34:39] text like send an email like process a
[34:41] credit card transaction like process a
[34:43] return. And so the way this works in
[34:44] practice, the way companies do this and
[34:45] let's take the most common example of an
[34:47] agentic AI is maybe a customer service
[34:49] chatbot. You as the company when you set
[34:53] up this agentic AI, you create a bunch
[34:56] of tools like a bunch of, you know, IT
[34:58] functions, basically functions that say,
[35:00] okay, this is, you know, will process a
[35:02] return for a customer. This will ship an
[35:04] order. This will send an email. This
[35:06] will send a text. This will refund a
[35:08] credit card transaction. And you make
[35:09] all those tools available. And when you
[35:12] set up your chatbot, you just tell the
[35:14] chatbot literally like in the text of
[35:16] the chatbot. There's smarter ways to do
[35:17] it, but that's a simple version. You
[35:20] tell it a customer is about to ask you a
[35:22] question. And by the way, here are a
[35:25] bunch of things you can do.
[35:27] &gt;&gt; This sounds a lot, but it sounds a lot I
[35:29] had an interview with uh the CFO of a
[35:31] new company that just went public in the
[35:33] summer, and it's a it's a travel agency
[35:35] company,
[35:36] &gt;&gt; but it's a completely new company. And
[35:39] the way the CFO described it was that
[35:43] prior to what they do, you know, if you
[35:45] were gonna if you were going to go and
[35:47] book a business trip, you know, from
[35:49] start to finish, it would take you at
[35:51] least 45 minutes to an hour to, you
[35:54] know, book the trip, book the the rental
[35:56] car, get the hotel. They have created a
[35:59] an an AI system from scratch where you
[36:01] can do this all in seven minutes.
[36:03] &gt;&gt; That's aentic AI
[36:04] &gt;&gt; precisely. And again, exactly as I
[36:06] described it, what I assume happens in
[36:08] that company is internally they've
[36:10] created some nice pipes where you can
[36:12] easily book a flight, book a hotel, look
[36:14] for flights, look for hotels, and then
[36:15] the chatbot gets the ability as you're
[36:17] chatting with the chatbot, it can say,
[36:19] "Ah, I would like to now call this hotel
[36:22] booking tool. I would like to call this
[36:23] send a text tool. I would like to call
[36:25] this send an email tool." And so on and
[36:26] so forth. And one thing I think this
[36:28] really highlights, and this is like the
[36:29] number one thing that usually, you know,
[36:30] if company comes to me and says, "We
[36:32] want to use AI, what can we do?" The
[36:34] number one thing I usually tell them is
[36:36] you've got to first create a fertile
[36:38] environment, a an environment in your
[36:40] company that is able to benefit from
[36:42] that AI. And in the example, for
[36:44] example, you need to have the IT systems
[36:47] that allow a computer to book a flight
[36:50] or to process a return or to whatever
[36:51] doesn't happen magically,
[36:52] &gt;&gt; right? If you're, let's say, a mandopme
[36:54] and you still take orders by hand and
[36:55] you're writing down, you don't need
[36:57] GPT75. You need like just your IT
[37:00] systems to be in a way that can actually
[37:01] sort of facilitate those things. And
[37:02] that's kind of why I say I think you
[37:04] know sometimes you know we talk about
[37:06] the AI bubble I sometimes people
[37:08] sometimes conflate the previous question
[37:10] we spoke about like will AI scale will
[37:12] it become super intelligent with do we
[37:14] have an AI bubble so they figure you
[37:16] know if AI scales to be like superhuman
[37:18] then we don't have an AI bubble but if
[37:20] AI stays the way it is today then we
[37:21] have an AI bubble and I don't think it's
[37:23] that simple like I would say even if
[37:25] models stay exactly the way they are
[37:26] today if companies get their house
[37:29] together in terms of the IT and in terms
[37:31] of the systems in terms of the data But
[37:32] that's a major issue because most of the
[37:35] companies in the world I don't think
[37:37] have their data set up in such a way
[37:39] where they can really say they have to
[37:41] actually go through a process where they
[37:43] have to put their data all in one place
[37:45] and clean it up etc before they can do
[37:47] any of this.
[37:47] &gt;&gt; And by the way Steve I got to say just
[37:48] as a human my favorite thing about Chen
[37:50] AI when I work with companies my
[37:52] favorite thing is it almost now
[37:54] motivates companies to do this. Like 5
[37:56] years ago I would go to a company and
[37:57] say you know you got to put your data
[37:58] into one place you got to organize. as
[38:00] you go and they'll be like ah boring you
[38:02] know we want now it's like all right
[38:04] that's what I got to do to get geni
[38:05] working let's go but but you know but uh
[38:08] absolutely you got to do that uh and so
[38:09] that really is what genti is by the way
[38:11] I mean just one more example because I
[38:13] think it's you know might be relevant to
[38:14] your listeners uh people are now working
[38:16] these are in their infancy uh uh
[38:18] anthropic is finally releasing this to
[38:20] the public there are excel agents now
[38:23] where the tools I mentioned that the
[38:25] chatbot has are tools like create a
[38:27] pivot table right into this Excel
[38:30] create change the color of a cell and so
[38:32] you're talking with a chatbot and you
[38:33] tell it for example can you build me a
[38:35] DCF for Nvidia right and it will be able
[38:38] to use that tool and actually change
[38:40] your Excel spreadsheet as you're talking
[38:41] to it right so if that actually works
[38:44] you can imagine that would sort of be uh
[38:45] pretty amazing I would say that's still
[38:47] in their infancy but you know things are
[38:48] moving fast so so who knows so that's
[38:49] the agenting sort of bucket
[38:51] &gt;&gt; and what else do you think this can do
[38:53] &gt;&gt; the large language models yeah so you
[38:55] know I think it's worth uh mentioning uh
[38:57] just chat bots themselves right I mean
[38:59] is literally chatgptt.com Claude Gemini
[39:02] whatever it might be uh they're great
[39:04] they can write emails they can sort of
[39:05] you know do all these things that uh uh
[39:07] again now we kind of take for granted
[39:09] I'm actually curious do you use them at
[39:10] all in your workflow dayto-day
[39:12] &gt;&gt; I I use you know uh Gemini all all the
[39:15] time for research
[39:16] &gt;&gt; it's useful for research sort of you
[39:17] know I mean to write code by the way I
[39:19] mean the extent to which these models
[39:20] have gotten better at writing code in
[39:22] the last 6 months is just I mean
[39:23] sometimes gives me existential dread I
[39:25] love writing code and I just like wow
[39:27] they're good now again still not I got a
[39:29] lot of push back on that from a whole
[39:31] bunch of different coders who watch my
[39:33] show. You know, some of them were of the
[39:35] view that, you know, there were parts of
[39:37] coding that that helped, but parts of
[39:39] coding that it really didn't help. It
[39:40] was kind of all over the place. There
[39:42] was no there was no consensus.
[39:43] &gt;&gt; I'm going to tell you two things about
[39:44] that. First thing is
[39:47] if you'd asked me six months ago,
[39:49] &gt;&gt; I would have basically said forget about
[39:50] it. They're useful search engine for
[39:52] code, right? If you want to create one
[39:54] or two lines of code, but you know,
[39:55] that's pretty much it. they've really
[39:58] improved. I mean, I would encourage any
[40:00] listeners who haven't used clawed code
[40:02] recently or just haven't used cloud just
[40:04] by itself to write code, especially
[40:06] front-end design. So, creating a web
[40:08] page, a nicel looking website. Uh truly,
[40:10] if you're someone who's sitting here
[40:11] thinking, nah, they'll never sort of do
[40:13] anything. Try it right now.
[40:14] &gt;&gt; Okay. So, it's gotten a lot better.
[40:16] &gt;&gt; Gotten a lot better. Having said that, I
[40:17] agree with them. I mean I still think
[40:18] there is a certain level of creativity
[40:21] required in sort of architecting a
[40:24] software solution in making sure it
[40:26] doesn't go off the rails and making sure
[40:27] it's secure and so on that is uh you
[40:29] know that still needs a human involved.
[40:32] That said sometimes I wonder and I got
[40:33] to tell you Steve like I I love coding.
[40:35] I think it's a fun exercise. It's
[40:36] creative and sometimes I wonder if I you
[40:38] know if I'm sounding like an artist who
[40:41] says like you know I I love creating art
[40:43] but these models you know well they're
[40:44] nowhere near as good as I am. And so I
[40:45] don't know that there's a there's an
[40:46] element of similarity there. So anyway,
[40:48] I'm not sort of saying it's definitely
[40:50] amazing at coding. I'm just saying there
[40:51] is certain parts of coding that it's
[40:53] certainly really uh really really good
[40:55] at. Uh last thing I'll say just about
[40:57] chatbots is I think they are um they are
[41:01] really uh something people sometimes
[41:02] don't know is at least from a enterprise
[41:04] setting they can be customized quite
[41:06] well. So you can do things like give
[41:08] them trolls of documents, right? Like
[41:10] thousands tens of thousands of documents
[41:12] and then what they do back to the
[41:14] embeddings we spoke about there's a
[41:15] reason I mentioned them. They're
[41:16] everywhere. You can take those
[41:17] documents, you can embed the documents.
[41:19] You give the documents like a vibe
[41:21] basically. You say, "Ah, this document
[41:22] has this kind of vibe. This one has this
[41:23] kind of vibe." And then when you're
[41:25] chatting with a chatbot, it can search
[41:27] through those documents because it can
[41:28] say, let's say you ask uh uh you ask the
[41:31] chatbot, "Show me my contract that has
[41:33] the highest, I don't know, the risk or
[41:36] whatever it might be that is the most."
[41:37] It can say, "Okay, risky contract that
[41:40] has a vibe. I can embed that and I can
[41:42] put that somewhere. Let me now look at
[41:44] the document that has the closest vibe
[41:45] and it finds it." And it's just amazing
[41:47] how well it does that.
[41:48] &gt;&gt; Let me ask you about uh sort of the from
[41:51] a business perspective two um what would
[41:55] be the right word
[41:58] hot topics.
[42:00] So
[42:02] you know last year if you were to look
[42:03] at uh you know what did well in tech and
[42:07] what did not do well in tech which is
[42:08] always I find it very interesting
[42:10] because people just say tech tech did
[42:11] great you know buy tech you know blah
[42:13] blah blah. So la last year you know
[42:16] leave leave aside just the mag seven as
[42:18] as a category but you know anybody
[42:21] involved with selling chips did great
[42:24] whether it's GPUs CPUs memory chips they
[42:28] did great so hardware companies
[42:30] generally did well um hyperscalers who
[42:32] are buying these chips and creating AI
[42:34] data centers did well but the two groups
[42:37] that did terribly would be software
[42:40] companies and some iconic software
[42:42] companies like Salesforce
[42:45] service now and the argument about why
[42:48] they did poorly was that the cost of
[42:50] creating software
[42:52] quote unquote is collapsing and so
[42:55] therefore the moes that these companies
[42:56] have around them are not as strong. That
[42:59] was one group and the other group were
[43:01] the management consultants because you
[43:03] know the argument is why do I need a
[43:05] management consultant when for you know
[43:07] 90% of the stuff that I used to ask a
[43:09] management consultant about I could ask
[43:10] chat GPT and he gives it to me for free.
[43:12] So what do you just think about those
[43:14] two sort of are it's you know sometimes
[43:17] it's a narrative and you know in the in
[43:20] the business world when a narrative
[43:21] takes hold it's very hard to for that
[43:24] narrative to die until it like somebody
[43:26] beats it to death.
[43:28] &gt;&gt; So I just curious what you think of
[43:29] those narratives.
[43:30] &gt;&gt; Let me give you some thoughts. I should
[43:31] just say up front I am like in awe of
[43:33] people like you who can actually
[43:36] get an idea at least of where the market
[43:37] is going. Like I always I can have an
[43:40] idea of I have an idea of these topics.
[43:42] How those are going to then move the
[43:43] market. God knows it seems to be like a
[43:45] beast that I sort of you know don't
[43:46] fully understand.
[43:47] &gt;&gt; That's okay. That's not why you're here.
[43:49] &gt;&gt; No totally totally. Um so let's talk
[43:50] about software companies first and we'll
[43:52] get to the you know the the cost of
[43:54] developing software or otherwise. I just
[43:56] want to first express some sympathy in
[43:58] the sense that like I've certainly felt
[43:59] this way even with teaching it is like
[44:03] we are building a car like sorry driving
[44:05] a car learning how to drive a car while
[44:07] it's being built like literally every 5
[44:09] seconds you sneeze and there's a new
[44:11] kind of AI that totally changes the way
[44:13] you uh uh uh you know your offering the
[44:16] way you should design your software the
[44:18] way you should offer it enterprises
[44:19] especially company of the size of the
[44:21] size of Salesforce they're just not
[44:23] designed to operate at that speed I mean
[44:25] that's Wild, wild, wild, wild.
[44:26] &gt;&gt; So things are happening very rapidly.
[44:27] &gt;&gt; Very rapidly. And I would just say I
[44:29] don't this is not a prediction, but I've
[44:32] got a thing just from like a just purely
[44:35] sort of logical perspective. It's going
[44:37] to have to slow down at some point. At
[44:38] some point we're going to reach a place
[44:39] where a lot of the low-lying fruits have
[44:41] been harvested and we're now and so I I
[44:43] would just sort of put that here first
[44:44] of all that you know we are very much
[44:46] it's like it's almost like saying you
[44:47] know eight months into co oh look this
[44:50] company is sort of doing well or badly
[44:51] or whatever. I mean sure but things were
[44:53] just moving like the entire structure of
[44:55] the world was was changing. So that's
[44:57] the first thing I'll say you know the
[44:58] fact that the cost of software is
[45:00] dropping and people might develop their
[45:01] own software maybe I mean I've told you
[45:03] I've you know put up front the fact that
[45:04] I think uh uh uh you know coding using
[45:06] LLM is uh is uh they're good whether
[45:10] they're perfect definitely not and so
[45:11] on. I will say though I think people are
[45:13] underestimating the fact that like
[45:14] Salesforce is not just providing code
[45:17] software. I mean they are but they're
[45:19] also providing an entire structure a way
[45:21] of thinking about your business a way of
[45:23] you know like can you corral a whole
[45:25] bunch of people together in your
[45:26] business to actually agree to use this
[45:28] piece of software. And so I'm not saying
[45:30] that's going to be replaced but I'm
[45:31] saying there's probably a place they
[45:33] could evolve that involves like that
[45:36] puts more emphasis on those on all the
[45:38] things around software rather than just
[45:40] the software itself. Right? Meaning
[45:42] imagine if every single employee of
[45:43] yours could build their own Salesforce,
[45:46] their own sort of I don't know CRM let's
[45:47] say to sort of manage customers. It
[45:49] would be chaos. I mean everyone has a
[45:51] CRM. Which one do you use? Which one is
[45:52] right? Which one is wrong? How do you
[45:53] verify it? Whom do you trust? So you
[45:54] know
[45:55] &gt;&gt; I was actually thinking about also you
[45:57] know there are certain companies that
[45:58] control databases.
[46:00] &gt;&gt; Yeah.
[46:01] &gt;&gt; And like let's say I'm the guy who has
[46:03] the best database about commercial real
[46:06] estate. Sure.
[46:06] &gt;&gt; And I've I've had this business forever.
[46:09] I would think somebody could come in
[46:11] today
[46:13] and do it a lot cheaper than I than I
[46:16] have done it. And you know, no one has
[46:18] ever been able to attack me because I
[46:20] quote unquote control this database. But
[46:22] I I think that that people who have
[46:24] certain types of databases are
[46:27] vulnerable to this world.
[46:29] &gt;&gt; I think that's true. I mean, I'll give
[46:30] you one example of some example of a
[46:31] place that's really vulnerable. If your
[46:34] entire database is predicated on the
[46:35] fact that you just like looked at a
[46:38] whole bunch of handwritten documents or
[46:40] type documents that weren't digitized
[46:42] and you you know painstakingly sort of
[46:45] you know extracted the data from them
[46:46] and that gave you that database you are
[46:48] really susceptible to disruption because
[46:50] now these large language models you give
[46:52] them a PDF and using all the techniques
[46:53] we spoke about they just extract the
[46:55] data in a second. So I think you know
[46:56] that's one end of the spectrum. the
[46:58] other end of the spectrum maybe the
[46:59] extreme version of such a company is
[47:01] Bloomberg right I mean there all these
[47:02] data feeds they have etc I would imagine
[47:04] and I don't know sort of a huge amount
[47:06] about it I would imagine there would be
[47:07] much harder
[47:08] &gt;&gt; that's much harder because they have so
[47:09] many different databases
[47:11] &gt;&gt; yeah and you know I'll say there is a
[47:12] world in which you know we always forget
[47:14] the fact and this is you know the the
[47:16] the paradox everyone likes to mention
[47:18] these days but the fact that and I
[47:19] forget the name of the paradox uh uh but
[47:21] if you now have a if it's now much
[47:23] easier to create these databases yes
[47:25] you're going to disrupt people who've
[47:27] had them in the past, but you're also
[47:28] going to have many more. There's going
[47:29] to be many sort of more places where
[47:31] you're suddenly able to create these
[47:32] databases you didn't have before. Uh uh
[47:34] right. Just I mean to give you another
[47:35] example, you know, I said when we first
[47:37] discussed using Genai to strengthen
[47:38] machine learning, I said I had plenty of
[47:40] other examples. I'll slip one in right
[47:41] now because it applies just you know the
[47:44] fact that you could now take a bunch of
[47:45] text and even take images and create
[47:47] these embeddings, these essences, these
[47:49] vibes that kind of allows you to build
[47:51] databases you would never have had
[47:53] before. You could look at millions of
[47:54] images, right? Look at millions of
[47:56] pieces of text. You can embed them. You
[47:58] can put them on this XY plane that kind
[47:59] of defines their essence and you can
[48:01] start saying, "Okay, if someone searches
[48:03] for a particular term, I can now surface
[48:05] the right images and the right pieces of
[48:07] text that just relate to that particular
[48:09] term." So, you can imagine whole new
[48:10] kinds of databases, whole new kinds of
[48:12] uh of uh of data that are created by
[48:14] this.
[48:15] &gt;&gt; So, let's talk about management
[48:16] consulting because because that's sort
[48:17] of a pet peeve of mine over the years.
[48:19] And you know the argument that people
[48:21] have is you know you used to hire a
[48:23] management consultant because you you
[48:25] they have this this information and
[48:26] they're going to come in and now I don't
[48:28] need a management consultant because
[48:29] I'll just ask chat GPT and it'll give it
[48:30] to me in two seconds.
[48:31] &gt;&gt; Let me just tell you something. I you
[48:32] know Palanteer is not a management
[48:34] consultant by any way shape or form but
[48:35] you know there is some services element
[48:37] to the to the business and I remember
[48:39] sometimes musing with um
[48:43] with my colleagues there maybe I
[48:44] shouldn't say this but I remember musing
[48:46] with my colleagues there that like
[48:48] sometimes a lot of the value we provided
[48:50] was just getting all the people in a
[48:52] room together like like literally we
[48:53] would go to a company because they
[48:54] wanted to use data analytics AI they
[48:56] wanted to use our platform and in that
[48:57] room there was the CEO and the CTO and
[49:00] someone on the ground who actually
[49:01] worked with the data and someone who
[49:02] knew what the day and like literally all
[49:04] those people had never been in a room
[49:06] together before, right? So, you know, so
[49:08] again I I'm I'm going to an extreme
[49:10] here. I'm simplifying, but I think there
[49:11] is that element of management
[49:13] consulting, that external view that
[49:15] getting people together, which yeah,
[49:16] maybe LLMs could put together, but I
[49:18] think and again also I don't know much
[49:20] necessarily about the world of
[49:22] management consulting. I haven't been at
[49:23] Mackenzie, Bane, or BTG or whatever. I
[49:25] was you know Palante which is a very
[49:26] different kind of kind of beast but I
[49:28] could definitely imagine you know
[49:29] thinking of the services side of
[49:31] Palante's business let's say right which
[49:32] is not management consulting but
[49:34] certainly that I I you know I really see
[49:36] a lot of value in like getting all the
[49:38] people in the room together
[49:39] understanding how you want to take again
[49:41] your very messy business where
[49:42] everything is done by pen and paper and
[49:44] bringing all the data into one place and
[49:45] figuring out what's happening so I could
[49:47] easily see the the the big management
[49:49] consulting shops kind of shifting and
[49:51] they already are kind of shifting in
[49:52] that direction. Uh and then also maybe
[49:54] there's still value to sort of classical
[49:56] management consulting. I don't know
[49:57] enough about it to you know.
[49:58] &gt;&gt; So le let's go back to something that we
[50:00] talked about where so many companies
[50:02] don't even have their data in a position
[50:04] to actually
[50:06] &gt;&gt; I mean in in your travels
[50:10] &gt;&gt; if we're talking about let's say the S&amp;P
[50:12] 500 or the S&amp;P 1000 you know whatever. I
[50:16] mean, if nobody's data is in a is in a
[50:19] position to do any of this stuff, then
[50:23] AI is academic at this point in that in
[50:26] that sense because so many of the
[50:28] companies don't. So, where do you think
[50:29] corporate America actually is to be able
[50:32] to to do any of this stuff these days?
[50:34] &gt;&gt; Yeah, it's a great question, you know,
[50:36] and the last research I've seen that
[50:38] actually tries to figure that out
[50:39] systematically was a long time ago. And
[50:41] there it was something like, you know,
[50:43] 5% some ridiculously small number, but
[50:44] it was a long time ago. I don't think
[50:46] that's true anymore today because you're
[50:48] right if if the data is not in the right
[50:49] place there's just nothing you can
[50:50] really do with any of this stuff. I will
[50:52] say that there's a there's a factor
[50:53] which is that the AI itself can be very
[50:55] helpful in cleaning that data, right?
[50:57] And so there's a company I worked with I
[51:00] read a case with AI consultant CEO
[51:01] called Blend 360. They had a client that
[51:04] had this issue in their data where they
[51:06] were the client was formed through a
[51:07] bunch of acquisitions and they were a
[51:09] B2B sort of shop and they were formed
[51:10] through a bunch of acquisitions and
[51:12] everyone they had multiple databases
[51:15] listing their customers and every
[51:17] database used a different name. So, one
[51:19] database would say the client is
[51:21] Coca-Cola. Let's say one database would
[51:22] say it's Coca-Cola Company. The other
[51:24] one would say it's Coke. The other one
[51:26] would say it's CCNA or whatever. And
[51:28] what they did, which I thought was just
[51:29] genius, is they used a large language
[51:32] model to clean that up because if you
[51:34] ask a large language model, is Coca-Cola
[51:35] the same as a Coca-Cola company? It is
[51:37] going to be damn good at doing that. It
[51:38] knows the world. It knows everything. So
[51:40] that's just one example where it's not
[51:41] geni quad geni it's not like for the
[51:43] geni itself but it really it transformed
[51:46] things for them because now they had
[51:47] this unified data set they could
[51:48] actually use use machine learning. So
[51:50] I'll say I know I'm not directly
[51:51] answering your question but but but I
[51:53] think there is hope that uh um the genai
[51:56] not only sort of is useful with the data
[51:58] but also that it can actually help uh uh
[52:00] uh sort of formalize and clean and sort
[52:03] of put that data in a better place in a
[52:05] way that that makes it more valuable.
[52:07] But I I do think we're far I mean I
[52:08] think you know outside from the very big
[52:10] companies uh uh that maybe have the
[52:12] resources or maybe need to for
[52:14] compliance reasons just have that data
[52:15] in a good place I think there's you know
[52:17] a lot uh of midsize companies certainly
[52:20] the not even close
[52:21] &gt;&gt; certainly the ones I speak to that
[52:22] there's just a lot of work to be done to
[52:24] get things in in in good places.
[52:26] &gt;&gt; So what else should we talk about before
[52:27] we we finish up here?
[52:28] &gt;&gt; What else should we talk about? maybe it
[52:30] makes sense to talk a little bit about
[52:33] um what people are excited about when it
[52:35] comes to kind of next generations of of
[52:37] models, things that are in research. So
[52:39] there's a bunch of places people are
[52:41] going. So one thing that I think your
[52:42] listeners may find interesting is um so
[52:45] you know how I I kind of explained how
[52:48] the way these models are trained is it
[52:50] just tries to predict the next word and
[52:51] the next word and the next word and the
[52:53] next word and you know a model is
[52:54] considered good at least in training
[52:56] when you're tweaking the weights. It's
[52:58] considered good if it does a good job
[52:59] predicting the next word.
[53:00] &gt;&gt; Correct?
[53:01] &gt;&gt; And so what people have started doing uh
[53:03] and they did this in the early days but
[53:04] now there are even sort of smarter ways
[53:06] of doing this is they're trying to say
[53:07] instead of just tweaking the parameters
[53:09] of the model using that the next word
[53:11] prediction can we actually look at the
[53:14] full answer maybe get the large language
[53:16] model to generate many answers because
[53:18] it can because of the randomness that I
[53:20] told you about. So you can get many
[53:21] answers and then you judge the answers
[53:24] not by each token one by one but by
[53:26] where it got to at the end. Did it
[53:28] finally at the end get me sort of the
[53:29] right result.
[53:30] &gt;&gt; And the traditional way of doing that
[53:32] was something called reinforcement
[53:33] learning with human feedback RLHF. Uh
[53:36] that's been around for a while but now
[53:38] people are doing and sorry for the
[53:39] jargon here but they're doing something
[53:40] called reinforcement learning with
[53:41] verifiable rewards RLVR. That's sort of
[53:44] a big new thing they're doing which is
[53:46] can you try and use things that are
[53:48] automatically verifiable like sums like
[53:50] math for example and can you use that to
[53:52] try and sort of train the models in that
[53:54] way and it's had you know quite a bit of
[53:56] quite a bit of success by the way do you
[53:57] remember deepseek that that novel that
[53:58] came out right that was
[54:00] &gt;&gt; people were amazed at how good it was
[54:01] and how it was trained sort of you know
[54:03] so so cheaply to the extent it was and
[54:04] there sort of
[54:06] &gt;&gt; statement to begin with that was a
[54:07] controversial statement to begin with
[54:08] but to the extent it was a lot of it was
[54:10] they improved that process the RHF
[54:12] process was you know they did a better
[54:13] job there so One direction to think
[54:14] about that I think has a lot of promise.
[54:16] World models is something Gary sort of
[54:18] mentioned last time. I don't know a huge
[54:20] amount about them. They're still very
[54:21] very experimental. But the idea behind
[54:23] these world models is basically can we
[54:26] give the large language model kind of
[54:27] its own version of the matrix like you
[54:29] know the movie like its own version of
[54:30] like a mini world inside of it. And so
[54:33] for example when we ask pick a ball from
[54:35] the bag you remember the example before
[54:37] five balls ABCDE E pick one at random.
[54:39] Instead of using the embeddings and
[54:41] figuring out where the embedding is and
[54:42] figuring out the next word, the model
[54:45] would be able to use this little mini
[54:46] matrix to actually like create a bag
[54:49] with five balls and pick the right ball
[54:51] and then see where the letter is and
[54:52] then give you sort of a better answer.
[54:54] And you can imagine a world model that
[54:56] like, you know, knows all the laws of
[54:57] physics and knows the way the planet
[54:59] works and so on. So that's kind of an
[55:00] exciting uh uh uh direction. I don't
[55:02] know enough about it to tell you whether
[55:03] it's something I'm, you know, I think is
[55:05] good, I think it's bad, whatever.
[55:06] there's clearly very very smart people
[55:08] that are sort of going down that
[55:09] direction. But that's another
[55:10] interesting thing to uh to think about.
[55:12] Um maybe last thing that's worth talking
[55:13] about
[55:14] &gt;&gt; for everything we've spoken about
[55:15] machine learning models, AI models etc.
[55:18] I think it is ultimately important to
[55:20] remember that these models are just at
[55:23] least right now statistical parrots that
[55:25] are just paring existing data and that
[55:27] can lead to all the kinds of issues
[55:28] we've spoken about things like
[55:30] statistical par. So exactly sort of what
[55:32] we were describing they will take a a
[55:35] question you put in they will embed them
[55:37] right put them in a space and then find
[55:39] sort of words around it but what that
[55:41] determination is based on is just all
[55:43] the historical data you put into the
[55:45] models to train them right so that's
[55:47] what I mean by statistical par this is
[55:49] all statistics that's being used to
[55:50] figure out you know what the embeddings
[55:51] are what the closest words are they're
[55:53] just trying to replicate
[55:54] &gt;&gt; so that's why it has problems with
[55:55] novelty because novelty is not in the
[55:58] database
[55:58] &gt;&gt; because novelty is not in the database
[56:00] but then it can have bigger problems
[56:01] which is just that like you know the
[56:03] training data that is put into the model
[56:05] by definition is going to have some
[56:06] biases it's going to have some
[56:07] preconceptions of the world it's going
[56:09] to have some and you know sometimes
[56:10] those work for you sometimes they don't
[56:12] I mean just to give you an example I
[56:13] recommend any of your listeners should
[56:14] go on uh on uh uh chipt and ask it or
[56:18] any other model generate a picture of a
[56:20] typical American boy for me and it'll
[56:22] come up with a picture might be what you
[56:24] had in mind what not what you had in
[56:26] mind but it has an assumption about what
[56:28] that is what that means what American
[56:29] means and You know, again, in that case,
[56:33] it's maybe innocuous, but in some cases,
[56:34] it's not innocuous.
[56:35] &gt;&gt; So, you're saying the models could have
[56:36] like a political bias, a moral bias.
[56:39] &gt;&gt; The model definitely has a political
[56:40] bias. The model definitely has a moral
[56:42] bias.
[56:42] &gt;&gt; How does it how does it get a political
[56:44] bias? How does it get a moral bias?
[56:46] &gt;&gt; So, two ways. The first way is through
[56:47] that training I spoke about, right? It
[56:49] looks at all the text on the internet
[56:50] and to the extent that all the text on
[56:52] the internet has a political bias, it's
[56:54] going to sort of absorb that. But then
[56:56] there's that second stage that I just
[56:57] briefly mentioned, this RLHF,
[56:59] reinforcement learning from human
[57:01] feedback. That is a process where AI
[57:03] companies will literally look at entire
[57:06] conversations and will tell the model
[57:08] that was a good conversation, that was a
[57:10] bad conversation. And so, for example,
[57:12] &gt;&gt; uh uh uh let's say you have a large
[57:14] language model that starts being like
[57:16] super abusive and threatening and
[57:17] anti-Semitic and racist and whatever.
[57:19] The AI company will say, "Whoa, that's a
[57:21] bad conversation. Let's try and shift
[57:23] the parameters to get less of that." And
[57:25] as part of that process, it can just
[57:28] gather all these sort of you know biases
[57:30] about the world. Some of them are
[57:31] intentional, but some of them can be
[57:32] unintentional, right? It's not to say
[57:33] that uh uh uh you know that they're
[57:35] intentional. So that's certainly sort of
[57:36] you know a uh and this gets especially
[57:39] bad. You know when we said agentic AI
[57:40] when we're giving the model a pair of
[57:42] hands
[57:42] &gt;&gt; if we now start allowing the model to do
[57:45] things in the real world right you were
[57:46] talking about Terminator. You could
[57:48] imagine a crazy situation where you have
[57:50] a model that isn't so good that
[57:51] hallucinates that can't come up with the
[57:53] right thing and you kind of allow it
[57:54] suddenly to do I don't know to sue
[57:57] someone let's say right as a law firm I
[57:58] mean that could be that could be quite
[58:00] &gt;&gt; send an email that's terrible
[58:02] &gt;&gt; send an email that's terrible you can
[58:03] imagine even worse you give it access to
[58:05] weapons or whatever things like that and
[58:06] so I always like to say like I'm not as
[58:08] worried about human intellig about
[58:10] artificial intelligence as I am about
[58:11] human stupidity right that they're
[58:12] giving those models a tool and so I
[58:15] think a lot of that infrastructure
[58:16] around getting those models to work. The
[58:18] thing I said that is currently the
[58:19] bottleneck, the gating factor being
[58:21] ready for this is also to think about,
[58:23] okay, if I give my tool the ability to,
[58:26] let's say, process a credit card
[58:27] transaction, what kind of fences do I
[58:30] put around that? What kind of, you know,
[58:32] safeguards? Maybe I only allow it to go
[58:34] up to a certain amount. Maybe, you know,
[58:35] that that that kind of stuff.
[58:37] &gt;&gt; So, I'm going to give you the last word.
[58:38] So, we had, as I said, Gary Marcus on.
[58:42] just sum up your view of where we are in
[58:43] this world and and and how hopeful you
[58:45] are about what what this world's going
[58:47] to be like.
[58:48] &gt;&gt; Good question. How hopeful am I? Okay,
[58:50] I'll tell you one thing. I don't know
[58:51] how hopeful or unhopful this makes me,
[58:52] but I think the one takeaway I want
[58:54] people to maybe take from my view here
[58:57] uh um is that even if everything uh Gary
[59:01] said was right and his view is right,
[59:03] which I actually don't, there's nothing
[59:04] he said that I thought, oh, I disagree
[59:05] with this. I want people to realize that
[59:08] there's still a lot of value to be
[59:10] gotten out today. And that value could
[59:11] be for real good. I mean, there's a lot
[59:12] of stuff, you know, you were talking,
[59:13] you spoke about the US healthcare system
[59:15] and how difficult it is and and and
[59:18] complicated it is to sometimes file
[59:19] claims and appeal things and whatever.
[59:21] That is something AI could really do a
[59:23] lot of good for, right, if it's done
[59:25] right, if it's structured correctly and
[59:26] so on and so forth. So, I think there's
[59:28] a lot of good and a lot of value that
[59:29] can be done, a lot of really a lot of
[59:31] sort of uh good stuff that can be done.
[59:32] And so, I guess I would encourage people
[59:34] to maybe worry a little well that's not
[59:36] true. they should also worry about the
[59:37] future and if we get Terminator and
[59:38] whatever that that's worthwhile but also
[59:40] spend a bit of time asking okay I've got
[59:42] this wonderful toy right now today sort
[59:45] of you know what can I do with it what
[59:46] can it do for me what what can I do with
[59:48] it and hopefully this has been a bit of
[59:49] a of inspiration for what uh and as I
[59:52] said I'll put we'll put in the show
[59:53] notes this little sort of tools I put
[59:55] together so people can actually play
[59:56] around with some of the concept sort of
[59:57] we we discussed and hopefully they
[59:59] really get to see how you know these are
[60:00] not uh these are not magical
[60:02] technologies these are very much just
[60:04] you know calculations statistics ics,
[60:06] but that put together just result in
[60:07] this truly wondrous uh sort of set of
[60:09] models.
[60:10] &gt;&gt; That was great. Thank you very much.
[60:12] &gt;&gt; So much fun. Thanks so much, Steve.
[60:13] &gt;&gt; Glad to have you.
[60:15] &gt;&gt; That was some interview. And my
[60:18] takeaways are that there's quite a bit
[60:21] of overlap in agreement between Gary and
[60:24] Professor Getta, but also quite a bit of
[60:27] disagreement. So if if Gary was here, he
[60:29] would say I think that the LLM models
[60:33] are losing their efficaciousness and
[60:35] they will never ever ever produce
[60:38] returns that justify the hundreds of
[60:40] billions of dollars that the industry is
[60:42] spending. I think that's what Gary would
[60:44] say. Professor Guetta I think pointed
[60:47] out he agrees that LLMs are not going to
[60:51] achieve artificial general intelligence
[60:53] but at the end he doesn't really think
[60:56] that matters because the LLM models and
[60:59] the agentic AI chat bots etc are good
[61:02] enough to produce really efficacious
[61:06] products and you know recently there
[61:09] have been a whole bunch bunch of
[61:10] announcements of agentic AI chat bots
[61:13] that have really shaken up the industry.
[61:16] You've seen insurance brokers get
[61:18] impacted, wealth managers get impacted.
[61:21] Everybody's scared that this is actually
[61:24] going to work and the amount of money
[61:26] that the industry is spending to achieve
[61:28] all this is not stopping. You know, I
[61:31] think I would side a little bit more
[61:32] with Professor Guetta here that you're
[61:34] going to see a lot more products. What
[61:37] we don't know and which I think is
[61:39] really the question is is all this money
[61:41] going to going to achieve returns that
[61:43] justify the investments and frankly
[61:46] we're not going to know that. We're not
[61:48] going to know that for a while. I don't
[61:49] think we're going to know that this
[61:50] year. I think all we're going to see are
[61:52] a lot of announcements that are sound
[61:53] very exciting but we may not know till
[61:56] 2027 2028 whether all the this
[61:59] investment is going to produce returns
[62:02] that justify it. So until then, I think
[62:05] the story will stay the same. The
[62:07] hyperscalers will continue to spend
[62:08] money and people will be questioning
[62:11] whether this is really all worth it.
[62:18] This podcast is forformational purposes
[62:20] only and does not constitute investment
[62:22] advice. The hosts and guests may hold
[62:24] positions in stocks discussed. Opinions
[62:26] expressed are their own and not
[62:28] recommendations. Please do your own due
[62:30] diligence and consult a licensed
[62:31] financial adviser before making any
[62:33] investment decisions.
