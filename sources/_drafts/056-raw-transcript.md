# Raw Transcript: Dario Amodei — We are near the end of the exponential

[0:00]

So we talked three years ago. I'm So we talked three years ago. I'm curious in your view, what has been the curious in your view, what has been the curious in your view, what has been the biggest update of the last three years?

biggest update of the last three years? biggest update of the last three years? What has been the biggest difference What has been the biggest difference What has been the biggest difference between what it felt like last three between what it felt like last three

between what it felt like last three years versus now? years versus now? years versus now? &gt;&gt; Yeah, I would say actually the &gt;&gt; Yeah, I would say actually the &gt;&gt; Yeah, I would say actually the underlying technology like the

underlying technology like the underlying technology like the exponential of the technology has has exponential of the technology has has exponential of the technology has has gone broadly speaking I would say about gone broadly speaking I would say about

gone broadly speaking I would say about about as I expected it to go. I mean about as I expected it to go. I mean about as I expected it to go. I mean there's like plus or minus you know a there's like plus or minus you know a there's like plus or minus you know a couple there's plus or minus a year or

couple there's plus or minus a year or couple there's plus or minus a year or two here. There's plus or minus a year two here. There's plus or minus a year two here. There's plus or minus a year or two there. I don't know that I would or two there. I don't know that I would

or two there. I don't know that I would have predicted the specific direction of have predicted the specific direction of have predicted the specific direction of code. Um but but actually when I look at code. Um but but actually when I look at code. Um but but actually when I look at the exponential it it is roughly what I

the exponential it it is roughly what I the exponential it it is roughly what I expected in terms of the march of the expected in terms of the march of the expected in terms of the march of the models from like you know smart high models from like you know smart high

models from like you know smart high school student to smart college student school student to smart college student school student to smart college student to like you know beginning to do PhD and to like you know beginning to do PhD and to like you know beginning to do PhD and professional stuff and in the case of

professional stuff and in the case of professional stuff and in the case of code reaching beyond that. So you know code reaching beyond that. So you know code reaching beyond that. So you know the frontier is a little bit uneven.

the frontier is a little bit uneven. the frontier is a little bit uneven. It's roughly what I expected. I will It's roughly what I expected. I will It's roughly what I expected. I will tell you though what the most surprising tell you though what the most surprising

tell you though what the most surprising thing has been. The most surprising thing has been. The most surprising thing has been. The most surprising thing has been the lack of public thing has been the lack of public thing has been the lack of public recognition of how close we are to the

recognition of how close we are to the recognition of how close we are to the end of the exponential. To me, it is end of the exponential. To me, it is end of the exponential. To me, it is absolutely wild that, you know, you have absolutely wild that, you know, you have

absolutely wild that, you know, you have people, you know, within the bubble and people, you know, within the bubble and people, you know, within the bubble and outside the bubble, you know, but but outside the bubble, you know, but but outside the bubble, you know, but but you have people talking about these

you have people talking about these you have people talking about these these, you know, just the same tired old these, you know, just the same tired old these, you know, just the same tired old hot button political issues and like, hot button political issues and like,

hot button political issues and like, you know, around us. We're like near the you know, around us. We're like near the you know, around us. We're like near the end of the exponential. I I want to end of the exponential. I I want to end of the exponential. I I want to understand what that exponential looks

understand what that exponential looks understand what that exponential looks like right now because the first like right now because the first like right now because the first question I asked you when we recorded question I asked you when we recorded

question I asked you when we recorded three years ago was, you know, what's up three years ago was, you know, what's up three years ago was, you know, what's up with scaling? How why does it work? Um I with scaling? How why does it work? Um I with scaling? How why does it work? Um I have a similar question now but I feel

have a similar question now but I feel have a similar question now but I feel like it's a more complicated question like it's a more complicated question like it's a more complicated question because at least from the public's point because at least from the public's point

because at least from the public's point of view. of view. of view. &gt;&gt; Yes.

&gt;&gt; Yes. &gt;&gt; Yes. &gt;&gt; Three years ago there were these you &gt;&gt; Three years ago there were these you &gt;&gt; Three years ago there were these you know well-known public trends where know well-known public trends where

know well-known public trends where across many orders of magnitude of across many orders of magnitude of across many orders of magnitude of compute you could see how the loss compute you could see how the loss compute you could see how the loss improves and now we have RL scaling and

improves and now we have RL scaling and improves and now we have RL scaling and there's no publicly known scaling law there's no publicly known scaling law there's no publicly known scaling law for it. It's not even clear what exactly for it. It's not even clear what exactly

for it. It's not even clear what exactly the story is of is this supposed to be the story is of is this supposed to be the story is of is this supposed to be teaching the model skills is supposed to teaching the model skills is supposed to teaching the model skills is supposed to be teaching metalarning. Um what is the

be teaching metalarning. Um what is the be teaching metalarning. Um what is the scaling hypothesis at this point? scaling hypothesis at this point?

scaling hypothesis at this point? &gt;&gt; Yeah. So, so I have actually the same &gt;&gt; Yeah. So, so I have actually the same &gt;&gt; Yeah. So, so I have actually the same hypothesis that I had even all the way hypothesis that I had even all the way hypothesis that I had even all the way back in 2017. So, in 2017, I think I

[2:06]

back in 2017. So, in 2017, I think I back in 2017. So, in 2017, I think I talked about it last time, but I wrote a talked about it last time, but I wrote a talked about it last time, but I wrote a doc called the the big blob of compute doc called the the big blob of compute

doc called the the big blob of compute hypothesis. And and and you know, it it hypothesis. And and and you know, it it hypothesis. And and and you know, it it wasn't about the scaling of language wasn't about the scaling of language wasn't about the scaling of language models in particular. When I when I

models in particular. When I when I models in particular. When I when I wrote it, GPT1 had had just come out, wrote it, GPT1 had had just come out, wrote it, GPT1 had had just come out, right? So, that was you know, one among right? So, that was you know, one among

right? So, that was you know, one among many things, right? There was back in many things, right? There was back in many things, right? There was back in those days there was robotics. People those days there was robotics. People those days there was robotics. People tried to work on reasoning as a separate

tried to work on reasoning as a separate tried to work on reasoning as a separate thing from language models. there was thing from language models. there was thing from language models. there was scaling of the kind of RL that happened scaling of the kind of RL that happened

scaling of the kind of RL that happened that you know kind of happened in Alph that you know kind of happened in Alph that you know kind of happened in Alph Go and uh you know that that happened at Go and uh you know that that happened at Go and uh you know that that happened at Dota at OpenAI and um you know people

Dota at OpenAI and um you know people Dota at OpenAI and um you know people remember Starcraft at Deep Mind you know remember Starcraft at Deep Mind you know remember Starcraft at Deep Mind you know the Alpha Star um so uh it was written the Alpha Star um so uh it was written

the Alpha Star um so uh it was written as a more general document and and the as a more general document and and the as a more general document and and the specific thing I said was the following specific thing I said was the following specific thing I said was the following that and you know it's it's very you

that and you know it's it's very you that and you know it's it's very you know Rich Sutton put out the bitter know Rich Sutton put out the bitter know Rich Sutton put out the bitter lesson a couple years later um uh but lesson a couple years later um uh but

lesson a couple years later um uh but you know the the hypothesis is is you know the the hypothesis is is you know the the hypothesis is is basically the same so so what it says is basically the same so so what it says is basically the same so so what it says is all the cleverness, all the techniques,

all the cleverness, all the techniques, all the cleverness, all the techniques, all all the kind of we need a new method all all the kind of we need a new method all all the kind of we need a new method to to do something like that doesn't to to do something like that doesn't

to to do something like that doesn't matter very much. There are only a few matter very much. There are only a few matter very much. There are only a few things that matter and I think I listed things that matter and I think I listed things that matter and I think I listed seven of them. One is like how much raw

seven of them. One is like how much raw seven of them. One is like how much raw compute you have. The other is the compute you have. The other is the compute you have. The other is the quantity of data that you have. Then the quantity of data that you have. Then the

quantity of data that you have. Then the third is kind of the quality and third is kind of the quality and third is kind of the quality and distribution of data, right? It needs to distribution of data, right? It needs to distribution of data, right? It needs to be a broad broad distribution of data.

be a broad broad distribution of data. be a broad broad distribution of data. The fourth is I think how long you train The fourth is I think how long you train The fourth is I think how long you train for. Um the fifth is you need an for. Um the fifth is you need an

for. Um the fifth is you need an objective function that can scale to the objective function that can scale to the objective function that can scale to the moon. So the pre-training objective moon. So the pre-training objective moon. So the pre-training objective function is one such objective function

function is one such objective function function is one such objective function right another objective function is you right another objective function is you right another objective function is you know the the kind of RL objective know the the kind of RL objective

know the the kind of RL objective function that says like you have a goal function that says like you have a goal function that says like you have a goal you're going to go out and reach the you're going to go out and reach the you're going to go out and reach the goal within that of course there's

goal within that of course there's goal within that of course there's objective rewards like you know like you objective rewards like you know like you objective rewards like you know like you see in math and coding and there's more see in math and coding and there's more

see in math and coding and there's more subjective rewards like you see in RL subjective rewards like you see in RL subjective rewards like you see in RL from human feedback are kind of higher from human feedback are kind of higher from human feedback are kind of higher order higher order versions of that and

order higher order versions of that and order higher order versions of that and and then the sixth and seventh were and then the sixth and seventh were and then the sixth and seventh were things around kind of like normaliz things around kind of like normaliz

things around kind of like normaliz ation or conditioning like you know just ation or conditioning like you know just ation or conditioning like you know just getting the numerical stability so that getting the numerical stability so that getting the numerical stability so that kind of the big blob of compute flows in

[4:07]

kind of the big blob of compute flows in kind of the big blob of compute flows in this laminer way instead of instead of this laminer way instead of instead of this laminer way instead of instead of running into problems. So that was the running into problems. So that was the

running into problems. So that was the hypothesis and it's a hypothesis I still hypothesis and it's a hypothesis I still hypothesis and it's a hypothesis I still hold. I I don't think I've seen very hold. I I don't think I've seen very hold. I I don't think I've seen very much that is not in line with that

much that is not in line with that much that is not in line with that hypothesis. And so the pre-trained hypothesis. And so the pre-trained hypothesis. And so the pre-trained scaling laws were one example of what of scaling laws were one example of what of

scaling laws were one example of what of of of kind of what we see there. And of of kind of what we see there. And of of kind of what we see there. And indeed those have continued going like indeed those have continued going like indeed those have continued going like you know uh you know I think I think now

you know uh you know I think I think now you know uh you know I think I think now it's been it's been widely reported like it's been it's been widely reported like it's been it's been widely reported like you know we feel good about pre-training you know we feel good about pre-training

you know we feel good about pre-training like pre-training is continuing to give like pre-training is continuing to give like pre-training is continuing to give us gains. What has changed is that now us gains. What has changed is that now us gains. What has changed is that now we're also seeing the same thing for RL

we're also seeing the same thing for RL we're also seeing the same thing for RL right so we're seeing a pre-training right so we're seeing a pre-training right so we're seeing a pre-training phase and then we're seeing like an RL phase and then we're seeing like an RL

phase and then we're seeing like an RL phase on top of that. Um and with RL phase on top of that. Um and with RL phase on top of that. Um and with RL it's it's actually just the same like it's it's actually just the same like it's it's actually just the same like you know even even other companies have

you know even even other companies have you know even even other companies have have published um uh um like um you know have published um uh um like um you know have published um uh um like um you know in some of their in some of their in some of their in some of their

in some of their in some of their releases have published things that say releases have published things that say releases have published things that say look you know we train the model on math look you know we train the model on math look you know we train the model on math contests you know aime or or the kind of

contests you know aime or or the kind of contests you know aime or or the kind of other things and you know how well how other things and you know how well how other things and you know how well how well the model does is log linear and well the model does is log linear and

well the model does is log linear and how long we've trained it and we see how long we've trained it and we see how long we've trained it and we see that as well and it's not just math that as well and it's not just math that as well and it's not just math contest it's a wide variety of RL tasks.

contest it's a wide variety of RL tasks. contest it's a wide variety of RL tasks. And so we're seeing the same scaling in And so we're seeing the same scaling in And so we're seeing the same scaling in RL that we saw for pre-training. Um you RL that we saw for pre-training. Um you

RL that we saw for pre-training. Um you mentioned Richard Sutton and the bitter mentioned Richard Sutton and the bitter mentioned Richard Sutton and the bitter lesson. Yeah, lesson. Yeah, lesson. Yeah, &gt;&gt; I interviewed him last year and he is

&gt;&gt; I interviewed him last year and he is &gt;&gt; I interviewed him last year and he is actually very non LLM pill. And if I'm actually very non LLM pill. And if I'm actually very non LLM pill. And if I'm if I I don't know if this is his if I I don't know if this is his

if I I don't know if this is his perspective, but one way to paraphrase perspective, but one way to paraphrase perspective, but one way to paraphrase this objection is something like look this objection is something like look this objection is something like look something which possesses the true core

something which possesses the true core something which possesses the true core of human learning would not require all of human learning would not require all of human learning would not require all these billions of dollars of data and these billions of dollars of data and

these billions of dollars of data and compute and these bespoke environments compute and these bespoke environments compute and these bespoke environments to learn how to use Excel or how does an to learn how to use Excel or how does an to learn how to use Excel or how does an you know how to how to use PowerPoint,

you know how to how to use PowerPoint, you know how to how to use PowerPoint, how to navigate a web browser. And the how to navigate a web browser. And the how to navigate a web browser. And the fact that we have to build in these fact that we have to build in these

fact that we have to build in these skills using these RL environments hints skills using these RL environments hints skills using these RL environments hints that we're actually lacking this core that we're actually lacking this core that we're actually lacking this core human learning algorithm. Uh and so

[6:10]

human learning algorithm. Uh and so human learning algorithm. Uh and so we're scaling the wrong thing. And so we're scaling the wrong thing. And so we're scaling the wrong thing. And so yeah, that does raise a question. Why yeah, that does raise a question. Why

yeah, that does raise a question. Why are we doing all this RL scaling if we are we doing all this RL scaling if we are we doing all this RL scaling if we do think there's something that's going do think there's something that's going do think there's something that's going to be humanlike in its ability to learn

to be humanlike in its ability to learn to be humanlike in its ability to learn on the fly? on the fly?

on the fly? &gt;&gt; Yeah. Yeah. So I think I think this kind &gt;&gt; Yeah. Yeah. So I think I think this kind &gt;&gt; Yeah. Yeah. So I think I think this kind of puts together several things that of puts together several things that of puts together several things that should be kind of thought of thought of

should be kind of thought of thought of should be kind of thought of thought of differently. differently.

differently. &gt;&gt; Yeah. I think there is a genuine puzzle &gt;&gt; Yeah. I think there is a genuine puzzle &gt;&gt; Yeah. I think there is a genuine puzzle here, but it it may not matter. Um, in here, but it it may not matter. Um, in here, but it it may not matter. Um, in fact, I would guess it probably it

fact, I would guess it probably it fact, I would guess it probably it probably doesn't matter. So, let's take probably doesn't matter. So, let's take probably doesn't matter. So, let's take the RL out of it for a second because I the RL out of it for a second because I

the RL out of it for a second because I actually think RL and it's a red herring actually think RL and it's a red herring actually think RL and it's a red herring to say that RL is any different from to say that RL is any different from to say that RL is any different from pre-training in this matter. Um, so if

pre-training in this matter. Um, so if pre-training in this matter. Um, so if we if we look at pre-training scaling, we if we look at pre-training scaling, we if we look at pre-training scaling, um, it it was very interesting back in, um, it it was very interesting back in,

um, it it was very interesting back in, you know, 2017 when Alec Radford was you know, 2017 when Alec Radford was you know, 2017 when Alec Radford was doing GPT1. If you look at the models doing GPT1. If you look at the models doing GPT1. If you look at the models before GPT1, they were trained on these

before GPT1, they were trained on these before GPT1, they were trained on these data sets that didn't represent a wide, data sets that didn't represent a wide, data sets that didn't represent a wide, you know, distribution of text, right?

you know, distribution of text, right? you know, distribution of text, right? You had like, you know, these very You had like, you know, these very You had like, you know, these very standard, you know, kind of language standard, you know, kind of language

standard, you know, kind of language modeling benchmarks and GBT1 itself was modeling benchmarks and GBT1 itself was modeling benchmarks and GBT1 itself was trained on a bunch of, I think it was trained on a bunch of, I think it was trained on a bunch of, I think it was fanfiction actually. Um, but you know,

fanfiction actually. Um, but you know, fanfiction actually. Um, but you know, it was it was like literary, you know, it was it was like literary, you know, it was it was like literary, you know, it's like literary text, which is a very it's like literary text, which is a very

it's like literary text, which is a very small fraction of the text that you get. small fraction of the text that you get. small fraction of the text that you get. And what we found with that, you know, And what we found with that, you know, And what we found with that, you know, and in those days it was like a billion

and in those days it was like a billion and in those days it was like a billion words or something. So small data sets words or something. So small data sets words or something. So small data sets and represented a pretty narrow and represented a pretty narrow

and represented a pretty narrow distribution, right? Like a narrow distribution, right? Like a narrow distribution, right? Like a narrow distribution of kind of what what you distribution of kind of what what you distribution of kind of what what you can see what you can see in the world.

can see what you can see in the world. can see what you can see in the world. And it didn't generalize well. If you And it didn't generalize well. If you And it didn't generalize well. If you did better on um you know the the you did better on um you know the the you

did better on um you know the the you know I forget what but some some kind of know I forget what but some some kind of know I forget what but some some kind of fanfiction corpus um it wouldn't fanfiction corpus um it wouldn't fanfiction corpus um it wouldn't generalize that well to kind of the

generalize that well to kind of the generalize that well to kind of the other hat. you know, we had all these other hat. you know, we had all these other hat. you know, we had all these measures of like, you know, how well measures of like, you know, how well

measures of like, you know, how well does how well does a model do at does how well does a model do at does how well does a model do at predicting all of these other kinds of predicting all of these other kinds of predicting all of these other kinds of texts. You really didn't see the

texts. You really didn't see the texts. You really didn't see the generalization. It was only when you generalization. It was only when you generalization. It was only when you trained over all the tasks on the you, trained over all the tasks on the you,

trained over all the tasks on the you, you know, the internet when you when you you know, the internet when you when you you know, the internet when you when you kind of did a general internet scrape, kind of did a general internet scrape, kind of did a general internet scrape, right, from something like, you know,

right, from something like, you know, right, from something like, you know, common crawl or scraping links on common crawl or scraping links on common crawl or scraping links on Reddit, which is what we did for GPT2.

Reddit, which is what we did for GPT2. Reddit, which is what we did for GPT2. It's only when you do that that you kind It's only when you do that that you kind It's only when you do that that you kind of started to get generalization. Um, of started to get generalization. Um,

[8:13]

of started to get generalization. Um, and I think we're seeing the same thing and I think we're seeing the same thing and I think we're seeing the same thing on RL that we're starting with first on RL that we're starting with first on RL that we're starting with first very simple RL tasks like training on

very simple RL tasks like training on very simple RL tasks like training on math competitions. Then we're kind of math competitions. Then we're kind of math competitions. Then we're kind of moving to, you know, kind of broader moving to, you know, kind of broader

moving to, you know, kind of broader broader training that involves things broader training that involves things broader training that involves things like code as a task. And now we're like code as a task. And now we're like code as a task. And now we're moving to do kind of many many other

moving to do kind of many many other moving to do kind of many many other tasks. And then I think we're going to tasks. And then I think we're going to tasks. And then I think we're going to increasingly get generalization. So that increasingly get generalization. So that

increasingly get generalization. So that that kind of takes out the RL versus the that kind of takes out the RL versus the that kind of takes out the RL versus the pre-training side of it. But I think pre-training side of it. But I think pre-training side of it. But I think there is a puzzle here either way which

there is a puzzle here either way which there is a puzzle here either way which is that on pre-training when we train is that on pre-training when we train is that on pre-training when we train the model on pre-training you know we we the model on pre-training you know we we

the model on pre-training you know we we use like trillions of tokens right and use like trillions of tokens right and use like trillions of tokens right and and humans don't see trillions of words and humans don't see trillions of words and humans don't see trillions of words so there is an actual sample efficiency

so there is an actual sample efficiency so there is an actual sample efficiency difference here there is actually difference here there is actually difference here there is actually something different that's that's something different that's that's

something different that's that's happening here which is that the models happening here which is that the models happening here which is that the models start from scratch and you know they start from scratch and you know they start from scratch and you know they have to get much more much more training

have to get much more much more training have to get much more much more training but we also see that once they're but we also see that once they're but we also see that once they're trained if we give them a long context trained if we give them a long context

trained if we give them a long context length. The only thing blocking a long length. The only thing blocking a long length. The only thing blocking a long context length is like inference. But if context length is like inference. But if context length is like inference. But if we give them like a context length of a

we give them like a context length of a we give them like a context length of a million, they're very good at learning million, they're very good at learning million, they're very good at learning and adapting within that context length.

and adapting within that context length. and adapting within that context length. And and so I don't know the full answer And and so I don't know the full answer And and so I don't know the full answer to this, but but I think there's to this, but but I think there's

to this, but but I think there's something going on that pre-training something going on that pre-training something going on that pre-training it's it's not like the process of humans it's it's not like the process of humans it's it's not like the process of humans learning. It's somewhere between the

learning. It's somewhere between the learning. It's somewhere between the process of humans learning and the process of humans learning and the process of humans learning and the process of human evolution. It's like process of human evolution. It's like

process of human evolution. It's like it's somewhere between like we get many it's somewhere between like we get many it's somewhere between like we get many of our priors from evolution. Our brain of our priors from evolution. Our brain of our priors from evolution. Our brain isn't just a blank slate, right? Whole

isn't just a blank slate, right? Whole isn't just a blank slate, right? Whole books have been written about. I think books have been written about. I think books have been written about. I think the language models, they're much more the language models, they're much more

the language models, they're much more blank slates. They literally start as blank slates. They literally start as blank slates. They literally start as like random weights. Whereas the human like random weights. Whereas the human like random weights. Whereas the human brain starts with all these regions.

brain starts with all these regions. brain starts with all these regions. It's connected to all these inputs and It's connected to all these inputs and It's connected to all these inputs and outputs. Um and and so maybe we should outputs. Um and and so maybe we should

outputs. Um and and so maybe we should think of pre-training and for that think of pre-training and for that think of pre-training and for that matter RL as well as as being something matter RL as well as as being something matter RL as well as as being something that exists in the middle space between

that exists in the middle space between that exists in the middle space between human evolution and you know kind of human evolution and you know kind of human evolution and you know kind of human on on the spot learning and as the human on on the spot learning and as the

human on on the spot learning and as the in context learning that the models do in context learning that the models do in context learning that the models do as as something between long-term human as as something between long-term human as as something between long-term human learning and short-term human learning.

[10:17]

learning and short-term human learning. learning and short-term human learning. So, you know, there there's this So, you know, there there's this So, you know, there there's this hierarchy of like there's evolution, hierarchy of like there's evolution,

hierarchy of like there's evolution, there's long-term learning, there's there's long-term learning, there's there's long-term learning, there's short-term learning, and there's just short-term learning, and there's just short-term learning, and there's just human reaction. And the LOM phases exist

human reaction. And the LOM phases exist human reaction. And the LOM phases exist along this spectrum, but not necessarily along this spectrum, but not necessarily along this spectrum, but not necessarily exactly at the same points that there's exactly at the same points that there's

exactly at the same points that there's no analog to some of the human modes of no analog to some of the human modes of no analog to some of the human modes of learning. The LOMs are kind of falling learning. The LOMs are kind of falling learning. The LOMs are kind of falling between the points. Does that make

between the points. Does that make between the points. Does that make sense? sense?

sense? &gt;&gt; Um, yes. Although some things are still &gt;&gt; Um, yes. Although some things are still &gt;&gt; Um, yes. Although some things are still a bit confusing. For example, if the a bit confusing. For example, if the a bit confusing. For example, if the analogy is that this is like evolution,

analogy is that this is like evolution, analogy is that this is like evolution, so it's fine that it's not that sample so it's fine that it's not that sample so it's fine that it's not that sample efficient, then like well, if we're efficient, then like well, if we're

efficient, then like well, if we're going to get the kind of super sample going to get the kind of super sample going to get the kind of super sample efficient agent from in context efficient agent from in context efficient agent from in context learning, why are we bothering to build

learning, why are we bothering to build learning, why are we bothering to build in, you know, there's RL environment in, you know, there's RL environment in, you know, there's RL environment companies which are it seems like what companies which are it seems like what

companies which are it seems like what they're doing is they're teaching it how they're doing is they're teaching it how they're doing is they're teaching it how to use this API, how to use Slack, how to use this API, how to use Slack, how to use this API, how to use Slack, how to use whatever. It's confusing to me

to use whatever. It's confusing to me to use whatever. It's confusing to me why there's so much emphasis on that if why there's so much emphasis on that if why there's so much emphasis on that if the kind of agent that can just learn on the kind of agent that can just learn on

the kind of agent that can just learn on the fly is emerging or is going to soon the fly is emerging or is going to soon the fly is emerging or is going to soon emerge or has already emerged.

emerge or has already emerged. emerge or has already emerged. &gt;&gt; Yeah. Yeah. So I I I mean I can't speak &gt;&gt; Yeah. Yeah. So I I I mean I can't speak &gt;&gt; Yeah. Yeah. So I I I mean I can't speak for the emphasis of anyone else. I can I for the emphasis of anyone else. I can I

for the emphasis of anyone else. I can I can only talk about how we how we think can only talk about how we how we think can only talk about how we how we think about it. I think the way we think about about it. I think the way we think about about it. I think the way we think about it is the goal is not to teach the model

it is the goal is not to teach the model it is the goal is not to teach the model every possible skill within RL just as every possible skill within RL just as every possible skill within RL just as we don't do that within pre-training.

we don't do that within pre-training. we don't do that within pre-training. Right? Within pre-training we're not Right? Within pre-training we're not Right? Within pre-training we're not trying to expose the model to you know trying to expose the model to you know

trying to expose the model to you know every every possible uh you know way every every possible uh you know way every every possible uh you know way that words could be put together. Right?

that words could be put together. Right? that words could be put together. Right? you know, we're it's it's rather that you know, we're it's it's rather that you know, we're it's it's rather that the model trains on a lot of things and the model trains on a lot of things and

the model trains on a lot of things and then and then it reaches generalization then and then it reaches generalization then and then it reaches generalization across pre-training, right? That was across pre-training, right? That was across pre-training, right? That was that was the transition from GPT1 to

that was the transition from GPT1 to that was the transition from GPT1 to GPT2 that I saw up close which is like GPT2 that I saw up close which is like GPT2 that I saw up close which is like you know the the model reaches a point you know the the model reaches a point

you know the the model reaches a point you know I I I I like had these moments you know I I I I like had these moments you know I I I I like had these moments where I was like oh yeah you just give where I was like oh yeah you just give where I was like oh yeah you just give the model like you just give the model a

the model like you just give the model a the model like you just give the model a list of numbers that's like you know um list of numbers that's like you know um list of numbers that's like you know um you know this is the cost of the house you know this is the cost of the house

you know this is the cost of the house this is the square feet of the house and this is the square feet of the house and this is the square feet of the house and the model completes the pattern and does the model completes the pattern and does the model completes the pattern and does linear regression like not great but it

linear regression like not great but it linear regression like not great but it does it but it's never seen that exact does it but it's never seen that exact does it but it's never seen that exact thing before and and so to you know to thing before and and so to you know to

thing before and and so to you know to to the extent that we are building these to the extent that we are building these to the extent that we are building these RL environments the the goal is is very RL environments the the goal is is very RL environments the the goal is is very similar to what is be you know to what

[12:21]

similar to what is be you know to what similar to what is be you know to what was done five or 10 years ago with was done five or 10 years ago with was done five or 10 years ago with pre-training with we're trying to get a pre-training with we're trying to get a

pre-training with we're trying to get a we're trying to get a whole bunch of we're trying to get a whole bunch of we're trying to get a whole bunch of data not because we want to cover a data not because we want to cover a data not because we want to cover a specific document or a specific skill

specific document or a specific skill specific document or a specific skill but because we want to generalize. I but because we want to generalize. I but because we want to generalize. I mean I I think the framework you're mean I I think the framework you're

mean I I think the framework you're laying down obviously makes sense like laying down obviously makes sense like laying down obviously makes sense like we're making progress towards AGI. I we're making progress towards AGI. I we're making progress towards AGI. I think the crux is something like nobody

think the crux is something like nobody think the crux is something like nobody at this point disagrees that we're going at this point disagrees that we're going at this point disagrees that we're going to achieve AGI in this century. And the to achieve AGI in this century. And the

to achieve AGI in this century. And the crux is you say we're hitting the end of crux is you say we're hitting the end of crux is you say we're hitting the end of the exponential um and somebody else the exponential um and somebody else the exponential um and somebody else looks at this and says, "Oh yeah, we

looks at this and says, "Oh yeah, we looks at this and says, "Oh yeah, we we're making progress. We've been making we're making progress. We've been making we're making progress. We've been making progress since 2012 and then 2035 we'll progress since 2012 and then 2035 we'll

progress since 2012 and then 2035 we'll have a humanlike agent." And so I want have a humanlike agent." And so I want have a humanlike agent." And so I want to understand what it is that you're to understand what it is that you're to understand what it is that you're seeing which makes you think um yeah

seeing which makes you think um yeah seeing which makes you think um yeah obviously we're seeing the kinds of obviously we're seeing the kinds of obviously we're seeing the kinds of things that evolution did or that human things that evolution did or that human

things that evolution did or that human within the human lifetime learning is within the human lifetime learning is within the human lifetime learning is like in these models and why think that like in these models and why think that like in these models and why think that it's one year away and not 10 years

it's one year away and not 10 years it's one year away and not 10 years away. away.

away. &gt;&gt; I I I actually think of it as like two &gt;&gt; I I I actually think of it as like two &gt;&gt; I I I actually think of it as like two there's kind of two cases to be made there's kind of two cases to be made there's kind of two cases to be made here or like two two claims you could

here or like two two claims you could here or like two two claims you could make. One of which is like stronger and make. One of which is like stronger and make. One of which is like stronger and the other of which is weaker. So, I the other of which is weaker. So, I

the other of which is weaker. So, I think starting starting with the weaker think starting starting with the weaker think starting starting with the weaker claim, you know, when when I first saw claim, you know, when when I first saw claim, you know, when when I first saw the scaling back in like, you know,

the scaling back in like, you know, the scaling back in like, you know, 2019, 2019, 2019, um, you know, I wasn't sure. You know, um, you know, I wasn't sure. You know,

um, you know, I wasn't sure. You know, this was the whole this was kind of a this was the whole this was kind of a this was the whole this was kind of a 50/50 thing, right? I thought I saw 50/50 thing, right? I thought I saw 50/50 thing, right? I thought I saw something that was, you know, and and my

something that was, you know, and and my something that was, you know, and and my claim was this is much more likely than claim was this is much more likely than claim was this is much more likely than anyone thinks it is. Like, this is wild.

anyone thinks it is. Like, this is wild. anyone thinks it is. Like, this is wild. No one else would even consider this. No one else would even consider this.

No one else would even consider this. Maybe there's a 50% chance this happens. Maybe there's a 50% chance this happens. Maybe there's a 50% chance this happens. um on the basic hypothesis of you know um on the basic hypothesis of you know um on the basic hypothesis of you know as you put it within 10 years we'll get

as you put it within 10 years we'll get as you put it within 10 years we'll get to you know you know what I call kind of to you know you know what I call kind of to you know you know what I call kind of country of geniuses in a data center I'm country of geniuses in a data center I'm

country of geniuses in a data center I'm at like 90% on that um and it's hard to at like 90% on that um and it's hard to at like 90% on that um and it's hard to go much higher than 90% cuz the world is go much higher than 90% cuz the world is go much higher than 90% cuz the world is so unpredictable um maybe the

so unpredictable um maybe the so unpredictable um maybe the irreducible uncertainty would be if we irreducible uncertainty would be if we irreducible uncertainty would be if we were at 95% where you get to things like were at 95% where you get to things like

were at 95% where you get to things like I don't know may maybe multi you know I don't know may maybe multi you know I don't know may maybe multi you know multiple companies have you know kind of multiple companies have you know kind of multiple companies have you know kind of internal turmoil and nothing happens and

[14:21]

internal turmoil and nothing happens and internal turmoil and nothing happens and then Taiwan gets invaded and like all then Taiwan gets invaded and like all then Taiwan gets invaded and like all the all the fabs get blown up by the all the fabs get blown up by

the all the fabs get blown up by missiles and and you know and then now missiles and and you know and then now missiles and and you know and then now you scenario you know just you could you scenario you know just you could you scenario you know just you could construct a scenario where there's like

construct a scenario where there's like construct a scenario where there's like a 5% chance that it it or you know you a 5% chance that it it or you know you a 5% chance that it it or you know you can construct a 5% world where like can construct a 5% world where like

can construct a 5% world where like things things get delayed for for for things things get delayed for for for things things get delayed for for for for for 10 years that's maybe 5%.

for for 10 years that's maybe 5%. for for 10 years that's maybe 5%. There's another 5% which is that I'm There's another 5% which is that I'm There's another 5% which is that I'm very confident on tasks that can be very confident on tasks that can be

very confident on tasks that can be verified. So I think I think with coding verified. So I think I think with coding verified. So I think I think with coding I'm just except for that irreducible I'm just except for that irreducible I'm just except for that irreducible uncertainty there's just there's I mean

uncertainty there's just there's I mean uncertainty there's just there's I mean I think we'll be there in one or two I think we'll be there in one or two I think we'll be there in one or two years there's no way we will not be years there's no way we will not be

years there's no way we will not be there there in 10 years in terms of there there in 10 years in terms of there there in 10 years in terms of being able to do it end to end coding.

being able to do it end to end coding. being able to do it end to end coding. My one little bit the one little bit of My one little bit the one little bit of My one little bit the one little bit of of fundamental uncertainty even on long of fundamental uncertainty even on long

of fundamental uncertainty even on long time scales is this thing about tasks time scales is this thing about tasks time scales is this thing about tasks that aren't verifiable like planning a that aren't verifiable like planning a that aren't verifiable like planning a mission to Mars like uh you know doing

mission to Mars like uh you know doing mission to Mars like uh you know doing some fundamental scientific discovery some fundamental scientific discovery some fundamental scientific discovery like like crisper like you know writing like like crisper like you know writing

like like crisper like you know writing a writing a novel hard to hard to verify a writing a novel hard to hard to verify a writing a novel hard to hard to verify those tasks. I am almost certain that those tasks. I am almost certain that those tasks. I am almost certain that we have a reliable path to get there.

we have a reliable path to get there. we have a reliable path to get there. But like if there was a little bit But like if there was a little bit But like if there was a little bit uncertainty, it's there. So, so, so, so, uncertainty, it's there. So, so, so, so,

uncertainty, it's there. So, so, so, so, so on the 10 years, I'm like, you know, so on the 10 years, I'm like, you know, so on the 10 years, I'm like, you know, 90% which is about as certain as you can 90% which is about as certain as you can 90% which is about as certain as you can be. Like I think it's I think it's crazy

be. Like I think it's I think it's crazy be. Like I think it's I think it's crazy to say that this won't happen by by by to say that this won't happen by by by to say that this won't happen by by by 2035. Like in some sane world, it would 2035. Like in some sane world, it would

2035. Like in some sane world, it would be outside the mainstream. But but the be outside the mainstream. But but the be outside the mainstream. But but the emphasis on verification hints to me as emphasis on verification hints to me as emphasis on verification hints to me as a lack of a lack of uh belief that these

a lack of a lack of uh belief that these a lack of a lack of uh belief that these models are generalized. If you think models are generalized. If you think models are generalized. If you think about humans, about humans,

about humans, &gt;&gt; we are good at things that both which we &gt;&gt; we are good at things that both which we &gt;&gt; we are good at things that both which we get verifiable reward and things which get verifiable reward and things which get verifiable reward and things which we don't. You're like you have no no

we don't. You're like you have no no we don't. You're like you have no no this is this is why I'm almost sure we this is this is why I'm almost sure we this is this is why I'm almost sure we already see substantial generalization already see substantial generalization

already see substantial generalization from things that that verify to things from things that that verify to things from things that that verify to things that don't ver. We're already seeing that don't ver. We're already seeing that don't ver. We're already seeing that. But but it seems like you were

that. But but it seems like you were that. But but it seems like you were emphasizing this as a spectrum which emphasizing this as a spectrum which emphasizing this as a spectrum which will will

will uh split apart which domains we see more uh split apart which domains we see more uh split apart which domains we see more progress and I'm like but that's it progress and I'm like but that's it progress and I'm like but that's it doesn't seem like how humans get there.

[16:23]

doesn't seem like how humans get there. doesn't seem like how humans get there. &gt;&gt; The world in which we don't make it or &gt;&gt; The world in which we don't make it or &gt;&gt; The world in which we don't make it or or or the world in which we don't get or or the world in which we don't get

or or the world in which we don't get there is the world in which we do we do there is the world in which we do we do there is the world in which we do we do all the things that are that are all the things that are that are all the things that are that are verifiable and then they like you know

verifiable and then they like you know verifiable and then they like you know many of them generalize but but we kind many of them generalize but but we kind many of them generalize but but we kind of don't get fully there. We don't we of don't get fully there. We don't we

of don't get fully there. We don't we don't we don't fully you know we don't don't we don't fully you know we don't don't we don't fully you know we don't fully color in this side of the box.

fully color in this side of the box. fully color in this side of the box. It's it's it's not a it's not a binary It's it's it's not a it's not a binary It's it's it's not a it's not a binary thing. But but it also seems to me even thing. But but it also seems to me even

thing. But but it also seems to me even if even if in the world where if even if in the world where if even if in the world where generalization is weak when you only say generalization is weak when you only say generalization is weak when you only say baref domains it's not clear to me in

baref domains it's not clear to me in baref domains it's not clear to me in such a world you could automate software such a world you could automate software such a world you could automate software engineering because software like in engineering because software like in

engineering because software like in some sense you are quote unquote a some sense you are quote unquote a some sense you are quote unquote a software engineer but part of being a software engineer but part of being a software engineer but part of being a software engineer for you involves

software engineer for you involves software engineer for you involves writing these like long memos about your writing these like long memos about your writing these like long memos about your grand vision about different things and grand vision about different things and

grand vision about different things and so I don't think that's part of the job so I don't think that's part of the job so I don't think that's part of the job of sui that's part that's part of the of sui that's part that's part of the of sui that's part that's part of the job of the company but I do think

job of the company but I do think job of the company but I do think involves like design documents and other involves like design documents and other involves like design documents and other things like that um which by the way the things like that um which by the way the

things like that um which by the way the models are not bad they're already models are not bad they're already models are not bad they're already pretty good at writing comments and pretty good at writing comments and pretty good at writing comments and start and so with with again I'm making

start and so with with again I'm making start and so with with again I'm making like much weaker claims here than I like much weaker claims here than I like much weaker claims here than I believe to like you know to to to to believe to like you know to to to to

believe to like you know to to to to kind of set up a you know to to kind of set up a you know to to kind of set up a you know to to distinguish between two things like distinguish between two things like distinguish between two things like we're we're already almost there for

we're we're already almost there for we're we're already almost there for software engineering and we are already software engineering and we are already software engineering and we are already almost there by by what metric there's almost there by by what metric there's

almost there by by what metric there's one metric which is like how many lines one metric which is like how many lines one metric which is like how many lines of code are written by AI and if you use of code are written by AI and if you use of code are written by AI and if you use if you consider other productivity

if you consider other productivity if you consider other productivity improvements in the course of the improvements in the course of the improvements in the course of the history of software engineering history of software engineering

history of software engineering compilers write all the lines of compilers write all the lines of compilers write all the lines of software and but we there's a difference software and but we there's a difference software and but we there's a difference between how many lines are written and

between how many lines are written and between how many lines are written and how big the productivity improvement Oh how big the productivity improvement Oh how big the productivity improvement Oh yeah. And um and then like we're almost yeah. And um and then like we're almost

yeah. And um and then like we're almost there, meaning like the how big is the there, meaning like the how big is the there, meaning like the how big is the productivity improvement, not just how productivity improvement, not just how productivity improvement, not just how many lines are written.

many lines are written. many lines are written. &gt;&gt; Yeah. Yeah. So so I actually um I &gt;&gt; Yeah. Yeah. So so I actually um I &gt;&gt; Yeah. Yeah. So so I actually um I actually I actually agree with you on actually I actually agree with you on

actually I actually agree with you on this. So I I've made this series of this. So I I've made this series of this. So I I've made this series of predictions on um code and software predictions on um code and software predictions on um code and software engineering and and and I think people

engineering and and and I think people engineering and and and I think people have repeatedly kind of misunderstood have repeatedly kind of misunderstood have repeatedly kind of misunderstood them. So So let me let me let me let me them. So So let me let me let me let me

them. So So let me let me let me let me let me lay out the spectrum, right? Like let me lay out the spectrum, right? Like let me lay out the spectrum, right? Like I think it was like you know like you I think it was like you know like you I think it was like you know like you know eight eight or nine months ago or

know eight eight or nine months ago or know eight eight or nine months ago or something I said you know the AI model something I said you know the AI model something I said you know the AI model will be writing 90 90% of the lines of will be writing 90 90% of the lines of

will be writing 90 90% of the lines of code in like you know 3 to 6 months code in like you know 3 to 6 months code in like you know 3 to 6 months which which happened at least at some which which happened at least at some which which happened at least at some places right happened happened at

places right happened happened at places right happened happened at entropic happened with many people entropic happened with many people entropic happened with many people downstream using our models but but downstream using our models but but

[18:24]

downstream using our models but but that's actually a very weak criterion that's actually a very weak criterion that's actually a very weak criterion right people thought I was saying like right people thought I was saying like right people thought I was saying like we won't need 90% of the software

we won't need 90% of the software we won't need 90% of the software engineers those things are worlds apart engineers those things are worlds apart engineers those things are worlds apart right like I would put the spectrum term right like I would put the spectrum term

right like I would put the spectrum term as 90% of code is written by the model, as 90% of code is written by the model, as 90% of code is written by the model, 100% of code is written by the model and 100% of code is written by the model and 100% of code is written by the model and that's a big difference in productivity.

that's a big difference in productivity. that's a big difference in productivity. Um 90% of the end toend SWE tasks, Um 90% of the end toend SWE tasks, Um 90% of the end toend SWE tasks, right? Including things like compiling, right? Including things like compiling,

right? Including things like compiling, including things like setting up including things like setting up including things like setting up clusters and environments, testing clusters and environments, testing clusters and environments, testing features, writing memos, 90% of the SU

features, writing memos, 90% of the SU features, writing memos, 90% of the SU tasks are written by the models. 100% of tasks are written by the models. 100% of tasks are written by the models. 100% of today's suite tasks are are are written today's suite tasks are are are written

today's suite tasks are are are written by the models. And and even when when by the models. And and even when when by the models. And and even when when when that happen doesn't mean software when that happen doesn't mean software when that happen doesn't mean software engineers are out of a job like there's

engineers are out of a job like there's engineers are out of a job like there's like new higher level things they can do like new higher level things they can do like new higher level things they can do where they can they can manage and then where they can they can manage and then

where they can they can manage and then there's a further down the spectrum like there's a further down the spectrum like there's a further down the spectrum like you know there's 90% less demand for you know there's 90% less demand for you know there's 90% less demand for SWES which I think will happen but like

SWES which I think will happen but like SWES which I think will happen but like this is this this is a spectrum and you this is this this is a spectrum and you this is this this is a spectrum and you know I wrote about it in in the know I wrote about it in in the

know I wrote about it in in the adolescence of technology where I went adolescence of technology where I went adolescence of technology where I went through this kind of spectrum with through this kind of spectrum with through this kind of spectrum with farming um uh uh and so I I actually

farming um uh uh and so I I actually farming um uh uh and so I I actually totally agree with you on that. It's totally agree with you on that. It's totally agree with you on that. It's just these are very different benchmarks just these are very different benchmarks

just these are very different benchmarks from each other but we're proceeding from each other but we're proceeding from each other but we're proceeding through them super fast. It seems like through them super fast. It seems like through them super fast. It seems like in part of your vision it's like going

in part of your vision it's like going in part of your vision it's like going from 90 to 100 um first it's going to from 90 to 100 um first it's going to from 90 to 100 um first it's going to happen fast and two that somehow that happen fast and two that somehow that

happen fast and two that somehow that leads to huge productivity improvements. leads to huge productivity improvements. leads to huge productivity improvements. Um whereas when I noticed even in green Um whereas when I noticed even in green Um whereas when I noticed even in green field projects that people start with

field projects that people start with field projects that people start with cloud code or something people report cloud code or something people report cloud code or something people report starting a lot of projects and I'm like starting a lot of projects and I'm like

starting a lot of projects and I'm like do we see in the world out there a do we see in the world out there a do we see in the world out there a renaissance of software all these new renaissance of software all these new renaissance of software all these new features that wouldn't exist otherwise

features that wouldn't exist otherwise features that wouldn't exist otherwise and at least so far it doesn't seem like and at least so far it doesn't seem like and at least so far it doesn't seem like we see that and so that does make me we see that and so that does make me

we see that and so that does make me wonder even if even if like I never had wonder even if even if like I never had wonder even if even if like I never had to intervene on cloud code um there is to intervene on cloud code um there is to intervene on cloud code um there is this thing of like there's just the

this thing of like there's just the this thing of like there's just the world is complicated jobs are world is complicated jobs are world is complicated jobs are complicated and complicated and

complicated and closing the loop on self-contained closing the loop on self-contained closing the loop on self-contained systems whether just writing software or systems whether just writing software or systems whether just writing software or something how much sort of how much

something how much sort of how much something how much sort of how much broader gains we would see just from broader gains we would see just from broader gains we would see just from that. And so maybe that makes us this that. And so maybe that makes us this

that. And so maybe that makes us this should dilute our estimation of the should dilute our estimation of the should dilute our estimation of the country of geniuses.

[20:24]

country of geniuses. country of geniuses. &gt;&gt; I well well I actually I I like I like &gt;&gt; I well well I actually I I like I like &gt;&gt; I well well I actually I I like I like simultaneously simultaneously

simultaneously I simultaneously agree with you agree I simultaneously agree with you agree I simultaneously agree with you agree that it's a reason why these things that it's a reason why these things that it's a reason why these things don't happen instantly but at the same

don't happen instantly but at the same don't happen instantly but at the same time I think the the the effect is going time I think the the the effect is going time I think the the the effect is going to be very fast. So like I don't know to be very fast. So like I don't know

to be very fast. So like I don't know you could have these two poles right one you could have these two poles right one you could have these two poles right one is like um you know AI is like you know is like um you know AI is like you know is like um you know AI is like you know it's not going to make progress it's

it's not going to make progress it's it's not going to make progress it's slow like it's going to take you know slow like it's going to take you know slow like it's going to take you know kind of forever to diffuse within the kind of forever to diffuse within the

kind of forever to diffuse within the economy right economic diffusion has economy right economic diffusion has economy right economic diffusion has become one of these buzzwords that's become one of these buzzwords that's become one of these buzzwords that's like a a reason why we're not going to

like a a reason why we're not going to like a a reason why we're not going to make AI progress or why AI progress make AI progress or why AI progress make AI progress or why AI progress doesn't matter and and you know the doesn't matter and and you know the

doesn't matter and and you know the other axis is like we'll get recursive other axis is like we'll get recursive other axis is like we'll get recursive self-improvement you know the whole self-improvement you know the whole self-improvement you know the whole thing you know can't you just draw an

thing you know can't you just draw an thing you know can't you just draw an exponential line on the on the curve you exponential line on the on the curve you exponential line on the on the curve you know it's it's we're going to have you know it's it's we're going to have you

know it's it's we're going to have you know Dyson spheres around the sun in know Dyson spheres around the sun in know Dyson spheres around the sun in like you know like you know like you know you know so many nanconds after you know

you know so many nanconds after you know you know so many nanconds after you know after after we get recursive I mean I'm after after we get recursive I mean I'm after after we get recursive I mean I'm completely caricaturing the view here completely caricaturing the view here

completely caricaturing the view here but like you know there there there are but like you know there there there are but like you know there there there are these two extremes but what we've seen these two extremes but what we've seen these two extremes but what we've seen from from the beginning you know at

from from the beginning you know at from from the beginning you know at least if you look within anthropic least if you look within anthropic least if you look within anthropic there's this bizarre 10x per year growth there's this bizarre 10x per year growth

there's this bizarre 10x per year growth in revenue that we've seen right so you in revenue that we've seen right so you in revenue that we've seen right so you know in 2023 it was like 0 to 100 know in 2023 it was like 0 to 100 know in 2023 it was like 0 to 100 million 2024 it was 100 million to a

million 2024 it was 100 million to a million 2024 it was 100 million to a billion. 2025 it was a billion to like 9 billion. 2025 it was a billion to like 9 billion. 2025 it was a billion to like 9 or 10 billion. And then or 10 billion. And then

or 10 billion. And then &gt;&gt; you guys should have just bought like a &gt;&gt; you guys should have just bought like a &gt;&gt; you guys should have just bought like a billion dollars with your own product so billion dollars with your own product so billion dollars with your own product so you could just like have a clean 10V and

you could just like have a clean 10V and you could just like have a clean 10V and and the first month of this year like and the first month of this year like and the first month of this year like that that exponential is you would think that that exponential is you would think

that that exponential is you would think it would slow down but it would like you it would slow down but it would like you it would slow down but it would like you know we added another few billion to know we added another few billion to know we added another few billion to like you know to to to we added another

like you know to to to we added another like you know to to to we added another few billion to revenue in January and few billion to revenue in January and few billion to revenue in January and and so you know obviously that curve and so you know obviously that curve

and so you know obviously that curve can't go on forever right you know the can't go on forever right you know the can't go on forever right you know the GDP is only so large I don't you know I GDP is only so large I don't you know I GDP is only so large I don't you know I I would even guess that it bends that it

I would even guess that it bends that it I would even guess that it bends that it bends bends somewhat this here. But like bends bends somewhat this here. But like bends bends somewhat this here. But like that is like a fast curve, right? That's that is like a fast curve, right? That's

that is like a fast curve, right? That's like a that's like a really fast curve. like a that's like a really fast curve. like a that's like a really fast curve. And I would bet it stays pretty fast And I would bet it stays pretty fast And I would bet it stays pretty fast even as the scale goes to the entire

[22:25]

even as the scale goes to the entire even as the scale goes to the entire economy. So like I I think we should be economy. So like I I think we should be economy. So like I I think we should be thinking about this middle world where thinking about this middle world where

thinking about this middle world where things are like extremely fast but not things are like extremely fast but not things are like extremely fast but not instant where they take time because of instant where they take time because of instant where they take time because of economic diffusion because of the need

economic diffusion because of the need economic diffusion because of the need to close the loop because you know it's to close the loop because you know it's to close the loop because you know it's like this fiddly oh man I have to do like this fiddly oh man I have to do

like this fiddly oh man I have to do change management within my enterprise change management within my enterprise change management within my enterprise you know I have to like you know uh uh you know I have to like you know uh uh you know I have to like you know uh uh you know I I I I like I set this up but

you know I I I I like I set this up but you know I I I I like I set this up but but you know I have to change the but you know I have to change the but you know I have to change the security permissions on this in order to security permissions on this in order to

security permissions on this in order to make it actually work or you know, I had make it actually work or you know, I had make it actually work or you know, I had this like old piece of software that, this like old piece of software that, this like old piece of software that, you know, that like, you know, checks

you know, that like, you know, checks you know, that like, you know, checks the model before it's compiled and and the model before it's compiled and and the model before it's compiled and and and like released and I have to rewrite and like released and I have to rewrite

and like released and I have to rewrite it. And yes, the model can do that, but it. And yes, the model can do that, but it. And yes, the model can do that, but I have to tell the model to do that and I have to tell the model to do that and I have to tell the model to do that and it has to it has to take time to do

it has to it has to take time to do it has to it has to take time to do that. and and and so I think everything that. and and and so I think everything that. and and and so I think everything we've seen so far is is compatible with we've seen so far is is compatible with

we've seen so far is is compatible with the idea that there's one fast the idea that there's one fast the idea that there's one fast exponential that's the the capability of exponential that's the the capability of exponential that's the the capability of the model and then there's another fast

the model and then there's another fast the model and then there's another fast exponential that's downstream of that exponential that's downstream of that exponential that's downstream of that which is the diffusion of the model into which is the diffusion of the model into

which is the diffusion of the model into the economy not instant the economy not instant the economy not instant not slow much faster than any previous not slow much faster than any previous not slow much faster than any previous technology but it has its limits and and

technology but it has its limits and and technology but it has its limits and and and and this is what we you know when I and and this is what we you know when I and and this is what we you know when I when I look inside anthropic when I look when I look inside anthropic when I look

when I look inside anthropic when I look at our customers fast adoption but not at our customers fast adoption but not at our customers fast adoption but not infinitely fast.

infinitely fast. infinitely fast. &gt;&gt; Um can I try a hot take on you? &gt;&gt; Um can I try a hot take on you?

&gt;&gt; Um can I try a hot take on you? &gt;&gt; Yeah. &gt;&gt; Yeah. &gt;&gt; Yeah. &gt;&gt; I feel like diffusion is cope that &gt;&gt; I feel like diffusion is cope that &gt;&gt; I feel like diffusion is cope that people use to say when it's like if the

people use to say when it's like if the people use to say when it's like if the model isn't able to do something they're model isn't able to do something they're model isn't able to do something they're like oh but the diffus it's like a like oh but the diffus it's like a

like oh but the diffus it's like a diffusion issue. But then you should use diffusion issue. But then you should use diffusion issue. But then you should use the comparison to humans. You would the comparison to humans. You would the comparison to humans. You would think that the inherent advantages that

think that the inherent advantages that think that the inherent advantages that AIs have would make diffusion a much AIs have would make diffusion a much AIs have would make diffusion a much easier problem for new AIs getting easier problem for new AIs getting

easier problem for new AIs getting onboarded than new humans getting onboarded than new humans getting onboarded than new humans getting onboarded. So an AI can read your entire onboarded. So an AI can read your entire onboarded. So an AI can read your entire Slack and your drive in minutes. They

Slack and your drive in minutes. They Slack and your drive in minutes. They can share all the knowledge that the can share all the knowledge that the can share all the knowledge that the other copy other copies of the same other copy other copies of the same

other copy other copies of the same instance have. You don't have this instance have. You don't have this instance have. You don't have this adverse selection problem when you're adverse selection problem when you're adverse selection problem when you're hiring AI because you can just hire

hiring AI because you can just hire hiring AI because you can just hire copies of a vetted AI model. Um hiring a copies of a vetted AI model. Um hiring a copies of a vetted AI model. Um hiring a human is like so much more hassle. And human is like so much more hassle. And

human is like so much more hassle. And people hire humans all the time, right? people hire humans all the time, right? people hire humans all the time, right? We pay humans upwards of $50 trillion in We pay humans upwards of $50 trillion in We pay humans upwards of $50 trillion in wages because they're useful. Uh even

[24:26]

wages because they're useful. Uh even wages because they're useful. Uh even though it's like in principle it would though it's like in principle it would though it's like in principle it would be much easier to integrate AI into the be much easier to integrate AI into the

be much easier to integrate AI into the economy than it is to hire humans. I economy than it is to hire humans. I economy than it is to hire humans. I think like the diffusion I feel like think like the diffusion I feel like think like the diffusion I feel like doesn't really I I think diffusion is

doesn't really I I think diffusion is doesn't really I I think diffusion is very real and and and and and doesn't very real and and and and and doesn't very real and and and and and doesn't have to you know doesn't exclusively have to you know doesn't exclusively

have to you know doesn't exclusively have to do with limitation limitation have to do with limitation limitation have to do with limitation limitation limitations on the AI models like again limitations on the AI models like again limitations on the AI models like again there are people who use diffusion to to

there are people who use diffusion to to there are people who use diffusion to to you know as kind of a buzzword to say you know as kind of a buzzword to say you know as kind of a buzzword to say this isn't a big deal. I'm not talking this isn't a big deal. I'm not talking

this isn't a big deal. I'm not talking about that. I'm not talking about, you about that. I'm not talking about, you about that. I'm not talking about, you know, AI will diffuse at the speed that know, AI will diffuse at the speed that know, AI will diffuse at the speed that previous I think AI will diffuse much

previous I think AI will diffuse much previous I think AI will diffuse much faster than previous technologies have, faster than previous technologies have, faster than previous technologies have, but but not infinitely fast. So, I'll but but not infinitely fast. So, I'll

but but not infinitely fast. So, I'll I'll just give an example of this, I'll just give an example of this, I'll just give an example of this, right? Like there's like claude code.

right? Like there's like claude code. right? Like there's like claude code. Like claude code is extremely easy to Like claude code is extremely easy to Like claude code is extremely easy to set up. Um, you know, if you're a set up. Um, you know, if you're a

set up. Um, you know, if you're a developer, you can kind of just start developer, you can kind of just start developer, you can kind of just start using cla code. There is no reason why a using cla code. There is no reason why a using cla code. There is no reason why a developer at a large enterprise should

developer at a large enterprise should developer at a large enterprise should not be adopting claude code as quickly not be adopting claude code as quickly not be adopting claude code as quickly as you know individual developer as you know individual developer

as you know individual developer developer at a startup and we do developer at a startup and we do developer at a startup and we do everything we can to promote it right we everything we can to promote it right we everything we can to promote it right we sell uh we sell cla code to enterprises

sell uh we sell cla code to enterprises sell uh we sell cla code to enterprises and big enterprises like you know big and big enterprises like you know big and big enterprises like you know big big financial companies big big financial companies big

big financial companies big pharmaceutical companies all of them pharmaceutical companies all of them pharmaceutical companies all of them they're adopting claude code much faster they're adopting claude code much faster they're adopting claude code much faster than enterprises typically adopt new

than enterprises typically adopt new than enterprises typically adopt new technology, right? But but again, it technology, right? But but again, it technology, right? But but again, it like it it it it takes time like any like it it it it takes time like any

like it it it it takes time like any given feature or any given product like given feature or any given product like given feature or any given product like claude code or like co-work will get claude code or like co-work will get claude code or like co-work will get adopted by the you know the individual

adopted by the you know the individual adopted by the you know the individual developers who are on Twitter all the developers who are on Twitter all the developers who are on Twitter all the time by the like series A startups time by the like series A startups

time by the like series A startups many months faster than than you know many months faster than than you know many months faster than than you know than they will get adopted by like you than they will get adopted by like you than they will get adopted by like you know a like large enterprise that does

know a like large enterprise that does know a like large enterprise that does food sales. Um there are a number of food sales. Um there are a number of food sales. Um there are a number of factors like you have to go through factors like you have to go through

factors like you have to go through legal, you have to provision it for legal, you have to provision it for legal, you have to provision it for everyone. It has to you know like it has everyone. It has to you know like it has everyone. It has to you know like it has to pass security and compliance. The

to pass security and compliance. The to pass security and compliance. The leaders of the company who are further leaders of the company who are further leaders of the company who are further away from the AI revolution you know are away from the AI revolution you know are

away from the AI revolution you know are are forwardlooking but they have to say are forwardlooking but they have to say are forwardlooking but they have to say oh it makes sense for us to spend 50 oh it makes sense for us to spend 50 oh it makes sense for us to spend 50 million. This is what this claud code

[26:32]

million. This is what this claud code million. This is what this claud code thing is. This is why it helps our thing is. This is why it helps our thing is. This is why it helps our company. This is why it makes us more company. This is why it makes us more

company. This is why it makes us more productive. And then they have to productive. And then they have to productive. And then they have to explain to the people two levels below.

explain to the people two levels below. explain to the people two levels below. and they have to say, "Okay, we have and they have to say, "Okay, we have and they have to say, "Okay, we have 3,000 developers. Like, here's how we're 3,000 developers. Like, here's how we're

3,000 developers. Like, here's how we're going to roll it out to our developers." going to roll it out to our developers." going to roll it out to our developers." And we have conversations like this And we have conversations like this And we have conversations like this every day. Like, you know, we are doing

every day. Like, you know, we are doing every day. Like, you know, we are doing everything we can to make Anthropics everything we can to make Anthropics everything we can to make Anthropics revenue grow 20 or 30x a year instead of revenue grow 20 or 30x a year instead of

revenue grow 20 or 30x a year instead of 10x a year. Um, you know, and and and 10x a year. Um, you know, and and and 10x a year. Um, you know, and and and again, you know, many enterprises are again, you know, many enterprises are again, you know, many enterprises are just saying this is so productive like,

just saying this is so productive like, just saying this is so productive like, you know, we're going to take shortcuts you know, we're going to take shortcuts you know, we're going to take shortcuts in our usual procurement process, right?

in our usual procurement process, right? in our usual procurement process, right? they're moving much faster than you know they're moving much faster than you know they're moving much faster than you know when we tried to sell them just the when we tried to sell them just the

when we tried to sell them just the ordinary API which many of them use but ordinary API which many of them use but ordinary API which many of them use but quad code is a more compelling product quad code is a more compelling product quad code is a more compelling product um but it's not an infinitely compelling

um but it's not an infinitely compelling um but it's not an infinitely compelling product and I don't think even AGI or product and I don't think even AGI or product and I don't think even AGI or powerful AI or country of geniuses in powerful AI or country of geniuses in

powerful AI or country of geniuses in the data center will be an infinitely the data center will be an infinitely the data center will be an infinitely compelling product it will be a compelling product it will be a compelling product it will be a compelling product enough maybe to get

compelling product enough maybe to get compelling product enough maybe to get three or five or 10x a year growth even three or five or 10x a year growth even three or five or 10x a year growth even when you're in the hundreds of billions when you're in the hundreds of billions

when you're in the hundreds of billions of dollars which is extremely hard to do of dollars which is extremely hard to do of dollars which is extremely hard to do and has never been done in history and has never been done in history and has never been done in history before but not infinitely fast I I buy

before but not infinitely fast I I buy before but not infinitely fast I I buy that it would be a slight slowdown and that it would be a slight slowdown and that it would be a slight slowdown and maybe this is not your claim but maybe this is not your claim but

maybe this is not your claim but sometimes people talk about this like oh sometimes people talk about this like oh sometimes people talk about this like oh the capabilities are there but because the capabilities are there but because the capabilities are there but because of diffusion um otherwise like we're

of diffusion um otherwise like we're of diffusion um otherwise like we're basically at AGI and then basically at AGI and then basically at AGI and then &gt;&gt; I I I don't believe we're basically at &gt;&gt; I I I don't believe we're basically at

&gt;&gt; I I I don't believe we're basically at AGI. AGI. AGI. &gt;&gt; I think if you had the country of &gt;&gt; I think if you had the country of &gt;&gt; I think if you had the country of geniuses in a data center if your

geniuses in a data center if your geniuses in a data center if your company didn't company didn't company didn't geniuses in a data center we would know geniuses in a data center we would know

geniuses in a data center we would know it. We would know it if you had the it. We would know it if you had the it. We would know it if you had the country of geniuses in a data center country of geniuses in a data center country of geniuses in a data center like everyone in this room would know

like everyone in this room would know like everyone in this room would know it. Everyone in Washington would know it. Everyone in Washington would know it. Everyone in Washington would know it. like you know people in rural rural it. like you know people in rural rural

it. like you know people in rural rural parts might not know it but but but like parts might not know it but but but like parts might not know it but but but like we would know it we don't have that now we would know it we don't have that now we would know it we don't have that now that that's very clear as Dario was

that that's very clear as Dario was that that's very clear as Dario was ending at to get generalization you need ending at to get generalization you need ending at to get generalization you need to train across a wide variety of to train across a wide variety of

to train across a wide variety of realistic tasks and environments for realistic tasks and environments for realistic tasks and environments for example with a sales agent the hardest example with a sales agent the hardest example with a sales agent the hardest part isn't teaching it to mash buttons

part isn't teaching it to mash buttons part isn't teaching it to mash buttons in a specific database in Salesforce in a specific database in Salesforce in a specific database in Salesforce it's training the agent's judgment it's training the agent's judgment

it's training the agent's judgment across ambiguous situations how do you across ambiguous situations how do you across ambiguous situations how do you sort through a database with thousands sort through a database with thousands sort through a database with thousands of leads to figure out which ones are

[28:33]

of leads to figure out which ones are of leads to figure out which ones are How do you actually reach out? What do How do you actually reach out? What do How do you actually reach out? What do you do when you get ghosted? When an AI you do when you get ghosted? When an AI

you do when you get ghosted? When an AI lab wanted to train a sales agent, lab wanted to train a sales agent, lab wanted to train a sales agent, Labelbox brought in dozens of Fortune Labelbox brought in dozens of Fortune Labelbox brought in dozens of Fortune 500 sales people to build a bunch of

500 sales people to build a bunch of 500 sales people to build a bunch of different RL environments. They created different RL environments. They created different RL environments. They created thousands of scenarios where the sales thousands of scenarios where the sales

thousands of scenarios where the sales agent had to engage with the potential agent had to engage with the potential agent had to engage with the potential customer, which was roleplayed by a customer, which was roleplayed by a customer, which was roleplayed by a second AI. Limblebox made sure that this

second AI. Limblebox made sure that this second AI. Limblebox made sure that this customer AI had a few different customer AI had a few different customer AI had a few different personas. Because when you cold call, personas. Because when you cold call,

personas. Because when you cold call, you have no idea who's going to be on you have no idea who's going to be on you have no idea who's going to be on the other end. You need to be able to the other end. You need to be able to the other end. You need to be able to deal with a whole range of

deal with a whole range of deal with a whole range of possibilities. Limblebox's sales experts possibilities. Limblebox's sales experts possibilities. Limblebox's sales experts monitored these conversations turn by monitored these conversations turn by

monitored these conversations turn by turn, tweaking the role playinging agent turn, tweaking the role playinging agent turn, tweaking the role playinging agent to ensure it did the kinds of things an to ensure it did the kinds of things an to ensure it did the kinds of things an actual customer would do. Label Box

actual customer would do. Label Box actual customer would do. Label Box could iterate faster than anybody else could iterate faster than anybody else could iterate faster than anybody else in the industry. This is super important in the industry. This is super important

in the industry. This is super important because RL is an empirical science. It's because RL is an empirical science. It's because RL is an empirical science. It's not a solve problem. Labelbox has a not a solve problem. Labelbox has a not a solve problem. Labelbox has a bunch of tools for monitoring agent

bunch of tools for monitoring agent bunch of tools for monitoring agent performance in real time. This lets performance in real time. This lets performance in real time. This lets their experts keep coming up with tasks their experts keep coming up with tasks

their experts keep coming up with tasks so that the model stays in the right so that the model stays in the right so that the model stays in the right distribution of difficulty and gets the distribution of difficulty and gets the distribution of difficulty and gets the optimal reward signal during training.

optimal reward signal during training. optimal reward signal during training. Label box can do this sort of thing in Label box can do this sort of thing in Label box can do this sort of thing in almost every domain. They've got almost every domain. They've got

almost every domain. They've got headphone managers, radiologists, even headphone managers, radiologists, even headphone managers, radiologists, even airline pilots. So, whatever you're airline pilots. So, whatever you're airline pilots. So, whatever you're working on, Labelbox can help. Learn

working on, Labelbox can help. Learn working on, Labelbox can help. Learn more at labelbox.com/vorcash. Coming back to concrete predictions Coming back to concrete predictions because I think because there's so many because I think because there's so many

because I think because there's so many different things to dis ambiguate, it different things to dis ambiguate, it different things to dis ambiguate, it can be easy to talk past each other when can be easy to talk past each other when can be easy to talk past each other when we're talking about capabilities. So,

we're talking about capabilities. So, we're talking about capabilities. So, for example, when I interviewed 3 years for example, when I interviewed 3 years for example, when I interviewed 3 years ago, I asked her a prediction about what ago, I asked her a prediction about what

ago, I asked her a prediction about what should we expect 3 years from now. I should we expect 3 years from now. I should we expect 3 years from now. I think you were right. So you said we think you were right. So you said we think you were right. So you said we should expect systems which if you talk

should expect systems which if you talk should expect systems which if you talk to them for the course of an hour it's to them for the course of an hour it's to them for the course of an hour it's hard to tell them apart from a generally hard to tell them apart from a generally

hard to tell them apart from a generally well educated human. Yes. well educated human. Yes. well educated human. Yes. &gt;&gt; I think you were right about that and I &gt;&gt; I think you were right about that and I &gt;&gt; I think you were right about that and I think spiritually I feel unsatisfied

think spiritually I feel unsatisfied think spiritually I feel unsatisfied because my internal expectation was was because my internal expectation was was because my internal expectation was was that such a system could automate large that such a system could automate large

that such a system could automate large parts of white collar work and so it parts of white collar work and so it parts of white collar work and so it might be more productive to talk about might be more productive to talk about might be more productive to talk about the actual end capabilities. You want

the actual end capabilities. You want the actual end capabilities. You want such a system. such a system.

such a system. &gt;&gt; So so I will I will I will basically &gt;&gt; So so I will I will I will basically &gt;&gt; So so I will I will I will basically tell you what what you know where where tell you what what you know where where tell you what what you know where where I think we are. So but let me let me ask

I think we are. So but let me let me ask I think we are. So but let me let me ask it in a very specific question so that it in a very specific question so that it in a very specific question so that we can figure out exactly what kinds of we can figure out exactly what kinds of

we can figure out exactly what kinds of capabilities we should expect soon. So capabilities we should expect soon. So capabilities we should expect soon. So maybe I'll ask about it in the context maybe I'll ask about it in the context maybe I'll ask about it in the context of a job I understand well not because

[30:35]

of a job I understand well not because of a job I understand well not because it's the most relevant job but um just it's the most relevant job but um just it's the most relevant job but um just because I can evaluate the claims about because I can evaluate the claims about

because I can evaluate the claims about it. Um take video editors right I have it. Um take video editors right I have it. Um take video editors right I have video editors and part of their invol video editors and part of their invol video editors and part of their invol job involves learning about our

job involves learning about our job involves learning about our audience's preferences learning about my audience's preferences learning about my audience's preferences learning about my preferences and tastes and the different preferences and tastes and the different

preferences and tastes and the different trade-offs we have and how just over the trade-offs we have and how just over the trade-offs we have and how just over the course of many months building up this course of many months building up this course of many months building up this understanding of context. And so the

understanding of context. And so the understanding of context. And so the skill and ability they have six months skill and ability they have six months skill and ability they have six months into the job, a model that can pick up into the job, a model that can pick up

into the job, a model that can pick up that skill on the job on the fly. When that skill on the job on the fly. When that skill on the job on the fly. When should we be expect such an AI system?

should we be expect such an AI system? should we be expect such an AI system? Yeah. So I guess what you're talking Yeah. So I guess what you're talking Yeah. So I guess what you're talking about is like you know we've we're we're about is like you know we've we're we're

about is like you know we've we're we're doing this interview for 3 hours and doing this interview for 3 hours and doing this interview for 3 hours and then like you know someone's going to then like you know someone's going to then like you know someone's going to come in, someone's going to edit it,

come in, someone's going to edit it, come in, someone's going to edit it, they're going to be like oh you know you they're going to be like oh you know you they're going to be like oh you know you know I don't know Dario like you know know I don't know Dario like you know

know I don't know Dario like you know scratched his head and you know we could scratched his head and you know we could scratched his head and you know we could we could edit that out and you magnify we could edit that out and you magnify we could edit that out and you magnify that. there was this like long there was

that. there was this like long there was that. there was this like long there was this like long discussion that like is this like long discussion that like is this like long discussion that like is less interesting to people and then then less interesting to people and then then

less interesting to people and then then you know then there's other thing that's you know then there's other thing that's you know then there's other thing that's like more interesting to people so you like more interesting to people so you like more interesting to people so you know let's let's let's kind of make this

know let's let's let's kind of make this know let's let's let's kind of make this this edit so you know I think the this edit so you know I think the this edit so you know I think the country of geniuses in a data center w country of geniuses in a data center w

country of geniuses in a data center w will be able to do that the the way it will be able to do that the the way it will be able to do that the the way it will be able to do that is you know it will be able to do that is you know it will be able to do that is you know it will have general control of a computer

will have general control of a computer will have general control of a computer screen right like you know and and and screen right like you know and and and screen right like you know and and and you'll be able to feed this in and it'll you'll be able to feed this in and it'll

you'll be able to feed this in and it'll be able to also use the computer screen be able to also use the computer screen be able to also use the computer screen to like go on the web look at all your to like go on the web look at all your to like go on the web look at all your previous look at all your previous

previous look at all your previous previous look at all your previous interviews like look at what people are interviews like look at what people are interviews like look at what people are saying on Twitter in response to your saying on Twitter in response to your

saying on Twitter in response to your interviews like talk to you ask you interviews like talk to you ask you interviews like talk to you ask you questions talk to your staff look at the questions talk to your staff look at the questions talk to your staff look at the history of kind of edits edits that you

history of kind of edits edits that you history of kind of edits edits that you did and from that like do the job um so did and from that like do the job um so did and from that like do the job um so I think that's dependent on several I think that's dependent on several

I think that's dependent on several things one that's dependent and and and things one that's dependent and and and things one that's dependent and and and and I think this is one of the things and I think this is one of the things and I think this is one of the things that's actually blocking deployment um

that's actually blocking deployment um that's actually blocking deployment um getting to the point on computer use getting to the point on computer use getting to the point on computer use where the models are really masters at where the models are really masters at

where the models are really masters at using the computer right and you know using the computer right and you know using the computer right and you know we've seen this climb in in benchmarks we've seen this climb in in benchmarks we've seen this climb in in benchmarks and benchmarks are always you know

and benchmarks are always you know and benchmarks are always you know imperfect measures but like you know OS imperfect measures but like you know OS imperfect measures but like you know OS world is you know went from you know world is you know went from you know

world is you know went from you know like 5% a you know like uh I think when like 5% a you know like uh I think when like 5% a you know like uh I think when we first re released you know uh uh we first re released you know uh uh we first re released you know uh uh computer use like a a year and a quarter

computer use like a a year and a quarter computer use like a a year and a quarter ago it was like maybe 15% I don't ago it was like maybe 15% I don't ago it was like maybe 15% I don't remember exactly but we've climbed from remember exactly but we've climbed from

[32:36]

remember exactly but we've climbed from that to like 65 or 70%. Um and and you that to like 65 or 70%. Um and and you that to like 65 or 70%. Um and and you know there may be harder measures as know there may be harder measures as know there may be harder measures as well but but I think computer use has to

well but but I think computer use has to well but but I think computer use has to pass a point of reliability. Can I just pass a point of reliability. Can I just pass a point of reliability. Can I just ask to follow up on that before you move ask to follow up on that before you move

ask to follow up on that before you move to the next point? Um I often for years to the next point? Um I often for years to the next point? Um I often for years I've been trying to build different I've been trying to build different I've been trying to build different internal LLM tools for myself and I

internal LLM tools for myself and I internal LLM tools for myself and I often I have these text in text out often I have these text in text out often I have these text in text out tasks which should be dead center in the tasks which should be dead center in the

tasks which should be dead center in the repertoire of these models and yet I repertoire of these models and yet I repertoire of these models and yet I still hire humans to do them just still hire humans to do them just still hire humans to do them just because it's if it's something like make

because it's if it's something like make because it's if it's something like make identify what the best clips would be in identify what the best clips would be in identify what the best clips would be in this transcript and maybe they'll do this transcript and maybe they'll do

this transcript and maybe they'll do like a seven out of 10 job at them but like a seven out of 10 job at them but like a seven out of 10 job at them but there's not this ongoing way I can there's not this ongoing way I can there's not this ongoing way I can engage with them to help them get better

engage with them to help them get better engage with them to help them get better at the job the way I could with a human at the job the way I could with a human at the job the way I could with a human employee and so that missing ability employee and so that missing ability

employee and so that missing ability even if you saw computer use would still even if you saw computer use would still even if you saw computer use would still block my ability to like offload an block my ability to like offload an block my ability to like offload an actual job to them.

actual job to them. actual job to them. &gt;&gt; Again, there's there's this gets back to &gt;&gt; Again, there's there's this gets back to &gt;&gt; Again, there's there's this gets back to what to to kind to kind of what we were what to to kind to kind of what we were

what to to kind to kind of what we were talking about before with learning on talking about before with learning on talking about before with learning on the job where it's it's very the job where it's it's very the job where it's it's very interesting. You know, I think I think

interesting. You know, I think I think interesting. You know, I think I think with the coding agents like I don't with the coding agents like I don't with the coding agents like I don't think people would say that learning on think people would say that learning on

think people would say that learning on the job is what is what is you know the job is what is what is you know the job is what is what is you know preventing the coding agents from like preventing the coding agents from like preventing the coding agents from like you know doing everything end to end

you know doing everything end to end you know doing everything end to end like they keep they keep getting better. like they keep they keep getting better.

like they keep they keep getting better. We have engineers at Enthropic who like We have engineers at Enthropic who like We have engineers at Enthropic who like don't write any code. And when I look at don't write any code. And when I look at don't write any code. And when I look at the productivity to your to your

the productivity to your to your the productivity to your to your previous question, you know, we have previous question, you know, we have previous question, you know, we have folks who say this this GPU kernel, this folks who say this this GPU kernel, this

folks who say this this GPU kernel, this chip, I used to write it myself. I just chip, I used to write it myself. I just chip, I used to write it myself. I just have Claude do it. And so there's this have Claude do it. And so there's this have Claude do it. And so there's this there's this enormous improvement in

there's this enormous improvement in there's this enormous improvement in productivity. And I don't know like when productivity. And I don't know like when productivity. And I don't know like when I see Claude code like familiarity with I see Claude code like familiarity with

I see Claude code like familiarity with the code base or like it you know or or the code base or like it you know or or the code base or like it you know or or a feeling that the model hasn't worked a feeling that the model hasn't worked a feeling that the model hasn't worked at the company for for a year that's not

at the company for for a year that's not at the company for for a year that's not high up on the list of complaints I see. high up on the list of complaints I see.

high up on the list of complaints I see. And so I think what I'm saying is we're And so I think what I'm saying is we're And so I think what I'm saying is we're we're like we're kind of taking a we're like we're kind of taking a we're like we're kind of taking a different path. Don't don't you think

different path. Don't don't you think different path. Don't don't you think with coding that's because there is an with coding that's because there is an with coding that's because there is an external scaffold of memory which exists external scaffold of memory which exists

external scaffold of memory which exists instantiated in the codebase which I instantiated in the codebase which I instantiated in the codebase which I don't know how many other jobs have don't know how many other jobs have don't know how many other jobs have coding made fast progress precisely

coding made fast progress precisely coding made fast progress precisely because it has this unique um advantage because it has this unique um advantage because it has this unique um advantage that other economic activity doesn't that other economic activity doesn't

[34:37]

that other economic activity doesn't &gt;&gt; but but when you say that what you're &gt;&gt; but but when you say that what you're &gt;&gt; but but when you say that what you're what you're implying is that by reading what you're implying is that by reading what you're implying is that by reading the code base into the context I have

the code base into the context I have the code base into the context I have everything that the human needed to everything that the human needed to everything that the human needed to learn on the job. So that would be an learn on the job. So that would be an

learn on the job. So that would be an example of whether it's written or not, example of whether it's written or not, example of whether it's written or not, whether it's available or not, a case whether it's available or not, a case whether it's available or not, a case where everything you needed to know, you

where everything you needed to know, you where everything you needed to know, you got from the context window, right? And got from the context window, right? And got from the context window, right? And that and that what we think of as that and that what we think of as

that and that what we think of as learning like, oh man, I started this learning like, oh man, I started this learning like, oh man, I started this job, it's going to take me 6 months to job, it's going to take me 6 months to job, it's going to take me 6 months to understand the codebase, the model just

understand the codebase, the model just understand the codebase, the model just did it in the context. did it in the context.

did it in the context. &gt;&gt; Yeah. I honestly don't know how to think &gt;&gt; Yeah. I honestly don't know how to think &gt;&gt; Yeah. I honestly don't know how to think about this because there there are about this because there there are about this because there there are people who qualitatively report what

people who qualitatively report what people who qualitatively report what you're saying. Um there was a meter you're saying. Um there was a meter you're saying. Um there was a meter study I'm sure you saw last year where study I'm sure you saw last year where

study I'm sure you saw last year where they they they &gt;&gt; had experienced developers try to close &gt;&gt; had experienced developers try to close &gt;&gt; had experienced developers try to close uh pull requests in repositories that

uh pull requests in repositories that uh pull requests in repositories that they were familiar with and those they were familiar with and those they were familiar with and those developers reported an uplift. They they developers reported an uplift. They they

developers reported an uplift. They they reported that they felt more productive reported that they felt more productive reported that they felt more productive with the use of these models but in fact with the use of these models but in fact with the use of these models but in fact if you look at their output and how much

if you look at their output and how much if you look at their output and how much was actually merged back in there's a was actually merged back in there's a was actually merged back in there's a 20% downlift. They were less productive 20% downlift. They were less productive

20% downlift. They were less productive as a result of using these models. And as a result of using these models. And as a result of using these models. And so I'm trying to square the qualitative so I'm trying to square the qualitative so I'm trying to square the qualitative feeling that people feel with these

feeling that people feel with these feeling that people feel with these models versus um one in a macro level models versus um one in a macro level models versus um one in a macro level where are all these where is this like where are all these where is this like

where are all these where is this like renaissance of software and two when renaissance of software and two when renaissance of software and two when people do these independent evaluations people do these independent evaluations people do these independent evaluations why are we not seeing the creative

why are we not seeing the creative why are we not seeing the creative benefits that we would expect benefits that we would expect benefits that we would expect &gt;&gt; within anthropic this is just really &gt;&gt; within anthropic this is just really

&gt;&gt; within anthropic this is just really unambiguous right we're under an unambiguous right we're under an unambiguous right we're under an incredible amount of commercial pressure incredible amount of commercial pressure incredible amount of commercial pressure and make it even hard harder for

and make it even hard harder for and make it even hard harder for ourselves because we have all this ourselves because we have all this ourselves because we have all this safety stuff we do that I think we do safety stuff we do that I think we do

safety stuff we do that I think we do more than than than other companies so more than than than other companies so more than than than other companies so like the the the pressure to survive like the the the pressure to survive like the the the pressure to survive economically while also keeping our

economically while also keeping our economically while also keeping our values is is just incredible, right? values is is just incredible, right?

values is is just incredible, right? We're trying to keep this 10x revenue We're trying to keep this 10x revenue We're trying to keep this 10x revenue curve going. There's like there is zero curve going. There's like there is zero curve going. There's like there is zero time for [&nbsp;__&nbsp;] There is zero time

time for [&nbsp;__&nbsp;] There is zero time time for [&nbsp;__&nbsp;] There is zero time for feeling like we're productive when for feeling like we're productive when for feeling like we're productive when we're not. Like these tools make us a we're not. Like these tools make us a

we're not. Like these tools make us a lot more productive. Like why why do you lot more productive. Like why why do you lot more productive. Like why why do you think we're concerned about competitors think we're concerned about competitors think we're concerned about competitors using the tools? because we think we're

using the tools? because we think we're using the tools? because we think we're ahead of the competitors and like we ahead of the competitors and like we ahead of the competitors and like we don't we don't want to accel we we we we don't we don't want to accel we we we we

[36:39]

don't we don't want to accel we we we we wouldn't be going through all this wouldn't be going through all this wouldn't be going through all this trouble if this was secretly reducing trouble if this was secretly reducing trouble if this was secretly reducing reducing our productivity like we see

reducing our productivity like we see reducing our productivity like we see the end productivity every few months in the end productivity every few months in the end productivity every few months in the form of model launches like there's the form of model launches like there's

the form of model launches like there's no kidding yourself about this like the no kidding yourself about this like the no kidding yourself about this like the models make you more productive models make you more productive models make you more productive &gt;&gt; um one that is people feeling like

&gt;&gt; um one that is people feeling like &gt;&gt; um one that is people feeling like they're more productive is qualitatively they're more productive is qualitatively they're more productive is qualitatively predicted by studies like this but two predicted by studies like this but two

predicted by studies like this but two if I Look at the end output. Obviously, if I Look at the end output. Obviously, if I Look at the end output. Obviously, you guys are making fast progress. But you guys are making fast progress. But you guys are making fast progress. But the fact, you know, the the the idea was

the fact, you know, the the the idea was the fact, you know, the the the idea was supposed to be with recursive supposed to be with recursive supposed to be with recursive self-improvement is that you make a self-improvement is that you make a

self-improvement is that you make a better AI, the AI helps you build a better AI, the AI helps you build a better AI, the AI helps you build a better next AI, etc., etc. And what I better next AI, etc., etc. And what I better next AI, etc., etc. And what I see instead, if I look at the you open

see instead, if I look at the you open see instead, if I look at the you open AI, deep mind, is that people are just AI, deep mind, is that people are just AI, deep mind, is that people are just shifting around the podium every few shifting around the podium every few

shifting around the podium every few months. And maybe you think that stops months. And maybe you think that stops months. And maybe you think that stops because you you won or whatever, but um because you you won or whatever, but um because you you won or whatever, but um but why why are we not seeing the person

but why why are we not seeing the person but why why are we not seeing the person with the best coding model have this with the best coding model have this with the best coding model have this lasting advantage if in fact there are lasting advantage if in fact there are

lasting advantage if in fact there are these enormous productivity gains from these enormous productivity gains from these enormous productivity gains from the last model?

the last model? the last model? &gt;&gt; So no, no, no. I I I mean I mean I mean &gt;&gt; So no, no, no. I I I mean I mean I mean &gt;&gt; So no, no, no. I I I mean I mean I mean I think it's all like my my model of the I think it's all like my my model of the

I think it's all like my my model of the situation is there's there's an situation is there's there's an situation is there's there's an advantage that's gradually growing. Like advantage that's gradually growing. Like advantage that's gradually growing. Like I would say right now the coding models

I would say right now the coding models I would say right now the coding models give maybe I don't know a a like 15 give maybe I don't know a a like 15 give maybe I don't know a a like 15 maybe 20% total factor speed up like maybe 20% total factor speed up like

maybe 20% total factor speed up like that's my view. Um uh and 6 months ago that's my view. Um uh and 6 months ago that's my view. Um uh and 6 months ago it was maybe 5%. And so and so it didn't it was maybe 5%. And so and so it didn't it was maybe 5%. And so and so it didn't matter like 5% doesn't register. It's

matter like 5% doesn't register. It's matter like 5% doesn't register. It's now just getting to the point where it's now just getting to the point where it's now just getting to the point where it's like one of several factors that that like one of several factors that that

like one of several factors that that kind of matters and and that's gonna kind of matters and and that's gonna kind of matters and and that's gonna that's going to keep speeding up. And so that's going to keep speeding up. And so that's going to keep speeding up. And so I think 6 months ago like you know there

I think 6 months ago like you know there I think 6 months ago like you know there were several there were several were several there were several were several there were several companies that were at roughly the same companies that were at roughly the same

companies that were at roughly the same point because uh you know this this point because uh you know this this point because uh you know this this wasn't uh this wasn't a notable factor wasn't uh this wasn't a notable factor wasn't uh this wasn't a notable factor but I think it's starting to speed up

but I think it's starting to speed up but I think it's starting to speed up more and more. I you know I I would I more and more. I you know I I would I more and more. I you know I I would I would also say there are multiple would also say there are multiple

would also say there are multiple companies that you know write models companies that you know write models companies that you know write models that are used for code and you know that are used for code and you know that are used for code and you know we're not perfectly good at you know

we're not perfectly good at you know we're not perfectly good at you know preventing some of these other companies preventing some of these other companies preventing some of these other companies from from from using from from from kind from from from using from from from kind

from from from using from from from kind of using our models internally. Um, so, of using our models internally. Um, so, of using our models internally. Um, so, uh, you know, I think I think everything uh, you know, I think I think everything uh, you know, I think I think everything we're kind kind of everything we're

[38:45]

we're kind kind of everything we're we're kind kind of everything we're seeing is consistent with this kind of, seeing is consistent with this kind of, seeing is consistent with this kind of, um, this kind of snowball model where um, this kind of snowball model where

um, this kind of snowball model where where, you know, there's no hard. Again, where, you know, there's no hard. Again, where, you know, there's no hard. Again, my my my my theme in all of this is like my my my my theme in all of this is like my my my my theme in all of this is like all of this is soft takeoff, like soft

all of this is soft takeoff, like soft all of this is soft takeoff, like soft smooth exponentials, although the smooth exponentials, although the smooth exponentials, although the exponentials are relatively steep. And exponentials are relatively steep. And

exponentials are relatively steep. And so and so we're seeing this snowball so and so we're seeing this snowball so and so we're seeing this snowball gather momentum where it's like 10% 20% gather momentum where it's like 10% 20% gather momentum where it's like 10% 20% 25% you know for 40% and as you go yeah

25% you know for 40% and as you go yeah 25% you know for 40% and as you go yeah AMD doll's law you have to get all the AMD doll's law you have to get all the AMD doll's law you have to get all the like things that are preventing you from like things that are preventing you from

like things that are preventing you from from closing the loop out of the way but from closing the loop out of the way but from closing the loop out of the way but like this is one of the biggest like this is one of the biggest like this is one of the biggest priorities within anthropic. Um

priorities within anthropic. Um priorities within anthropic. Um stepping back I think before in the stepping back I think before in the stepping back I think before in the stack we were talking about um well when stack we were talking about um well when

stack we were talking about um well when do we get this on the job learning and do we get this on the job learning and do we get this on the job learning and it seems like the coding the point you it seems like the coding the point you it seems like the coding the point you were making the coding thing is we

were making the coding thing is we were making the coding thing is we actually don't need on the job learning actually don't need on the job learning actually don't need on the job learning uh that you can have tremendous uh that you can have tremendous

uh that you can have tremendous productivity improvements you can have productivity improvements you can have productivity improvements you can have potentially trillions of dollars of potentially trillions of dollars of potentially trillions of dollars of revenue for AI companies without this

revenue for AI companies without this revenue for AI companies without this basic human abil maybe that's not your basic human abil maybe that's not your basic human abil maybe that's not your claim you should clarify um but without claim you should clarify um but without

claim you should clarify um but without this basic human ability to learn on the this basic human ability to learn on the this basic human ability to learn on the job but I just look at like in in in job but I just look at like in in in job but I just look at like in in in most domain of economic activity. People

most domain of economic activity. People most domain of economic activity. People say, "I hired somebody. They weren't say, "I hired somebody. They weren't say, "I hired somebody. They weren't that useful for the first few months and that useful for the first few months and

that useful for the first few months and then over time they built up the context then over time they built up the context then over time they built up the context understanding. It's actually hard to understanding. It's actually hard to understanding. It's actually hard to define what we're talking about here,

define what we're talking about here, define what we're talking about here, but they they got something and then now but they they got something and then now but they they got something and then now now they're they're a power horse and now they're they're a power horse and

now they're they're a power horse and they're so valuable to us." And if AI they're so valuable to us." And if AI they're so valuable to us." And if AI doesn't develop this ability to learn on doesn't develop this ability to learn on doesn't develop this ability to learn on the fly, I'm not I'm a bit skeptical

the fly, I'm not I'm a bit skeptical the fly, I'm not I'm a bit skeptical that we're going to see huge changes to that we're going to see huge changes to that we're going to see huge changes to the world without the world without

the world without &gt;&gt; So I think I think I think two things &gt;&gt; So I think I think I think two things &gt;&gt; So I think I think I think two things here, right? There's the state of the here, right? There's the state of the here, right? There's the state of the technology right now um which is again

technology right now um which is again technology right now um which is again we have these two stages. We have the we have these two stages. We have the we have these two stages. We have the pre-training and RL stage where you pre-training and RL stage where you

pre-training and RL stage where you throw you throw a bunch of data and throw you throw a bunch of data and throw you throw a bunch of data and tasks into the models and then they tasks into the models and then they tasks into the models and then they generalize. So it's like learning but

generalize. So it's like learning but generalize. So it's like learning but it's like learning from more data and it's like learning from more data and it's like learning from more data and and not you know not learning over kind and not you know not learning over kind

and not you know not learning over kind of one human or one model's lifetime. So of one human or one model's lifetime. So of one human or one model's lifetime. So again this is situated between evolution again this is situated between evolution again this is situated between evolution and and and human learning. But once you

and and and human learning. But once you and and and human learning. But once you learn all those skills, you have them. learn all those skills, you have them.

[40:45]

learn all those skills, you have them. And and just like with pre-training, And and just like with pre-training, And and just like with pre-training, just how the models know more, you know, just how the models know more, you know, just how the models know more, you know, if if I look at a pre-trained model, you

if if I look at a pre-trained model, you if if I look at a pre-trained model, you know, it knows more about the history of know, it knows more about the history of know, it knows more about the history of samurai in Japan than I do. It knows samurai in Japan than I do. It knows

samurai in Japan than I do. It knows more about baseball than I do. It knows, more about baseball than I do. It knows, more about baseball than I do. It knows, you know, it knows more about, you know, you know, it knows more about, you know, you know, it knows more about, you know, lowass filters and electronics and, you

lowass filters and electronics and, you lowass filters and electronics and, you know, all all of these things. Its know, all all of these things. Its know, all all of these things. Its knowledge is way broader than mine. So I knowledge is way broader than mine. So I

knowledge is way broader than mine. So I think I think even even just that um you think I think even even just that um you think I think even even just that um you know may get us to the point where the know may get us to the point where the know may get us to the point where the models are better at you know kind of

models are better at you know kind of models are better at you know kind of better at everything and then we also better at everything and then we also better at everything and then we also have again just with scaling the kind of have again just with scaling the kind of

have again just with scaling the kind of existing setup we have the in context existing setup we have the in context existing setup we have the in context learning which I would describe as kind learning which I would describe as kind learning which I would describe as kind of like human on the job learning but

of like human on the job learning but of like human on the job learning but like a little weaker and a little short like a little weaker and a little short like a little weaker and a little short term like you look at in context term like you look at in context

term like you look at in context learning the you give the model a bunch learning the you give the model a bunch learning the you give the model a bunch of examples it does get it there's real of examples it does get it there's real of examples it does get it there's real learning that happens in context and

learning that happens in context and learning that happens in context and like a million tokens is a lot. That's like a million tokens is a lot. That's like a million tokens is a lot. That's that's you know that can be days of that's you know that can be days of

that's you know that can be days of human learning right you know if you human learning right you know if you human learning right you know if you think about the model you know you know think about the model you know you know think about the model you know you know kind of read reading reading a million

kind of read reading reading a million kind of read reading reading a million words you know you know it takes me how words you know you know it takes me how words you know you know it takes me how long would it take me to read a million long would it take me to read a million

long would it take me to read a million I mean you know like days or weeks at I mean you know like days or weeks at I mean you know like days or weeks at least um uh so you have these two things least um uh so you have these two things least um uh so you have these two things and and I think these two these two

and and I think these two these two and and I think these two these two things within the existing paradigm may things within the existing paradigm may things within the existing paradigm may just be enough to get you the country of just be enough to get you the country of

just be enough to get you the country of geniuses in the data center I don't know geniuses in the data center I don't know geniuses in the data center I don't know for sure but I think they're going to for sure but I think they're going to for sure but I think they're going to get you a large fraction of it there may

get you a large fraction of it there may get you a large fraction of it there may be gaps but I I certainly think just as be gaps but I I certainly think just as be gaps but I I certainly think just as things are this I believe is enough to things are this I believe is enough to

things are this I believe is enough to generate trillions of dollars of generate trillions of dollars of generate trillions of dollars of revenue. That's one that's all one. Two revenue. That's one that's all one. Two revenue. That's one that's all one. Two is this idea of continual learning. This

is this idea of continual learning. This is this idea of continual learning. This idea of a single model learning on the idea of a single model learning on the idea of a single model learning on the job. Um I think we're working on that job. Um I think we're working on that

job. Um I think we're working on that too and I think there's a good chance too and I think there's a good chance too and I think there's a good chance that in the next year or two we also that in the next year or two we also that in the next year or two we also make we also solve that. Um I I again I

make we also solve that. Um I I again I make we also solve that. Um I I again I I I I you know I think you get most of I I I you know I think you get most of I I I you know I think you get most of the way there without it. I think the the way there without it. I think the

the way there without it. I think the trillions of dollars of of you know the trillions of dollars of of you know the trillions of dollars of of you know the the I think the trillions of dollars a the I think the trillions of dollars a the I think the trillions of dollars a year market maybe all the national

[42:46]

year market maybe all the national year market maybe all the national security implications and the safety security implications and the safety security implications and the safety implications that I wrote about in implications that I wrote about in

implications that I wrote about in adolescence of technology can happen adolescence of technology can happen adolescence of technology can happen without it. But I I I also think we and without it. But I I I also think we and without it. But I I I also think we and I imagine others are working on it. And

I imagine others are working on it. And I imagine others are working on it. And I think there's a good chance that that I think there's a good chance that that I think there's a good chance that that you know that we get there within the you know that we get there within the

you know that we get there within the next year or two. There are a bunch of next year or two. There are a bunch of next year or two. There are a bunch of ideas. I won't go into all of them in ideas. I won't go into all of them in ideas. I won't go into all of them in detail, but um you know, one is just

detail, but um you know, one is just detail, but um you know, one is just make the context longer. There's there's make the context longer. There's there's make the context longer. There's there's nothing preventing longer context from nothing preventing longer context from

nothing preventing longer context from working. You just have to train at working. You just have to train at working. You just have to train at longer context and then learn to to longer context and then learn to to longer context and then learn to to serve them at inference. And both of

serve them at inference. And both of serve them at inference. And both of those are engineering problems that we those are engineering problems that we those are engineering problems that we are working on and that I would assume are working on and that I would assume

are working on and that I would assume others are working on as well. Yeah. So others are working on as well. Yeah. So others are working on as well. Yeah. So this context length increase, it seemed this context length increase, it seemed this context length increase, it seemed like there was a period from 2020 to

like there was a period from 2020 to like there was a period from 2020 to 2023 where from GPD3 to GP4 Turbo, there 2023 where from GPD3 to GP4 Turbo, there 2023 where from GPD3 to GP4 Turbo, there was an increase from like 2,000 context was an increase from like 2,000 context

was an increase from like 2,000 context lines to 128K. I feel like for the next lines to 128K. I feel like for the next lines to 128K. I feel like for the next for the twoish years since then, we've for the twoish years since then, we've for the twoish years since then, we've been in the sameish ballpark. Yeah. And

been in the sameish ballpark. Yeah. And been in the sameish ballpark. Yeah. And when model context lines get much longer when model context lines get much longer when model context lines get much longer than that, people report qualitative than that, people report qualitative

than that, people report qualitative degradation in the ability of the model degradation in the ability of the model degradation in the ability of the model to consider that full context. Um, so to consider that full context. Um, so to consider that full context. Um, so I'm curious what you're internally

I'm curious what you're internally I'm curious what you're internally seeing that makes you think like, oh, 10 seeing that makes you think like, oh, 10 seeing that makes you think like, oh, 10 million context, 100 million contexts to million context, 100 million contexts to

million context, 100 million contexts to get human like six months learning get human like six months learning get human like six months learning billion.

billion. billion. &gt;&gt; This isn't a research problem. This is a &gt;&gt; This isn't a research problem. This is a &gt;&gt; This isn't a research problem. This is a this is an engineering and inference this is an engineering and inference

this is an engineering and inference problem, right? If you want to serve problem, right? If you want to serve problem, right? If you want to serve long context, you have to like store long context, you have to like store long context, you have to like store your entire KV cache. You have to, you

your entire KV cache. You have to, you your entire KV cache. You have to, you know, um, uh, you know, it's it's it's know, um, uh, you know, it's it's it's know, um, uh, you know, it's it's it's it's difficult to store all the memory it's difficult to store all the memory

it's difficult to store all the memory in the GPUs to juggle the memory around. in the GPUs to juggle the memory around. in the GPUs to juggle the memory around. I don't even know the detail, you know, I don't even know the detail, you know, I don't even know the detail, you know, at this point. this is at a level of

at this point. this is at a level of at this point. this is at a level of detail that that that that I'm no longer detail that that that that I'm no longer detail that that that that I'm no longer able to follow although you know I I able to follow although you know I I

able to follow although you know I I knew it in the GPD3 era of like you know knew it in the GPD3 era of like you know knew it in the GPD3 era of like you know these are the weights these are the these are the weights these are the these are the weights these are the activations you have to store um uh but

activations you have to store um uh but activations you have to store um uh but you know you know these days the whole you know you know these days the whole you know you know these days the whole thing has flipped because we have models thing has flipped because we have models

thing has flipped because we have models and and and kind of all of that but um and and and kind of all of that but um and and and kind of all of that but um uh and and this degradation you're uh and and this degradation you're uh and and this degradation you're talking about like again without getting

talking about like again without getting talking about like again without getting too specific like a question I would ask too specific like a question I would ask too specific like a question I would ask is like there's two things there's the is like there's two things there's the

is like there's two things there's the context length you train at and there's context length you train at and there's context length you train at and there's a context length that you serve at if If a context length that you serve at if If a context length that you serve at if If you train at a small context length and

you train at a small context length and you train at a small context length and then try to serve at a long context then try to serve at a long context then try to serve at a long context length like maybe you get these length like maybe you get these

[44:48]

length like maybe you get these degradations. degradations. degradations. &gt;&gt; It's better than nothing. You might &gt;&gt; It's better than nothing. You might &gt;&gt; It's better than nothing. You might still offer it but you get these

still offer it but you get these still offer it but you get these degradations and maybe it's harder to degradations and maybe it's harder to degradations and maybe it's harder to train at a long context length. Yeah.

train at a long context length. Yeah. train at a long context length. Yeah. So, you know, there's there's a lot I I So, you know, there's there's a lot I I So, you know, there's there's a lot I I I want to at the same time ask about I want to at the same time ask about

I want to at the same time ask about like maybe some rabbit holes of like like maybe some rabbit holes of like like maybe some rabbit holes of like well wouldn't you expect that if you had well wouldn't you expect that if you had well wouldn't you expect that if you had to train on longer context length that

to train on longer context length that to train on longer context length that would mean that um you're able to get would mean that um you're able to get would mean that um you're able to get sort of like less samples in for the sort of like less samples in for the

sort of like less samples in for the same amount of compute. But before maybe same amount of compute. But before maybe same amount of compute. But before maybe it's not worth diving deep on that. I I it's not worth diving deep on that. I I it's not worth diving deep on that. I I want to get an answer to the bigger

want to get an answer to the bigger want to get an answer to the bigger picture question, which is like, okay, picture question, which is like, okay, picture question, which is like, okay, so so

so um I don't feel a preference for a human um I don't feel a preference for a human um I don't feel a preference for a human editor that's been working for me for 6 editor that's been working for me for 6 editor that's been working for me for 6 months versus an AI that's been working

months versus an AI that's been working months versus an AI that's been working with me for 6 months. What year do you with me for 6 months. What year do you with me for 6 months. What year do you predict that that will be the case?

predict that that will be the case? predict that that will be the case? &gt;&gt; I my I mean, you know, my guess for that &gt;&gt; I my I mean, you know, my guess for that &gt;&gt; I my I mean, you know, my guess for that is, you know, there's there's a lot of is, you know, there's there's a lot of

is, you know, there's there's a lot of problems that are basically like we can problems that are basically like we can problems that are basically like we can do this when we have the country of do this when we have the country of do this when we have the country of geniuses in a data center. Um, and so,

geniuses in a data center. Um, and so, geniuses in a data center. Um, and so, you know, my my my my picture for that you know, my my my my picture for that you know, my my my my picture for that is, you know, again, if you if you if is, you know, again, if you if you if

is, you know, again, if you if you if you if you know, if you made me guess, you if you know, if you made me guess, you if you know, if you made me guess, it's like one to two years, maybe one to it's like one to two years, maybe one to it's like one to two years, maybe one to three years. It's really hard to tell. I

three years. It's really hard to tell. I three years. It's really hard to tell. I have a I have a strong view 99 95% that have a I have a strong view 99 95% that have a I have a strong view 99 95% that like all this will happen in 10 years.

like all this will happen in 10 years. like all this will happen in 10 years. Like that's I think that's just a super Like that's I think that's just a super Like that's I think that's just a super safe bet. And then I have a hunch this safe bet. And then I have a hunch this

safe bet. And then I have a hunch this is more like a 50/50 thing that it's is more like a 50/50 thing that it's is more like a 50/50 thing that it's going to be more like 1 to two, maybe going to be more like 1 to two, maybe going to be more like 1 to two, maybe more like 1 to three.

more like 1 to three. more like 1 to three. &gt;&gt; So 1 to three years. country of genius &gt;&gt; So 1 to three years. country of genius &gt;&gt; So 1 to three years. country of genius says um and then the slightly less says um and then the slightly less

says um and then the slightly less economically valuable task of editing economically valuable task of editing economically valuable task of editing videos videos videos I

I I &gt;&gt; it seems pretty economically valuable &gt;&gt; it seems pretty economically valuable &gt;&gt; it seems pretty economically valuable let me tell you it's just there are a let me tell you it's just there are a

let me tell you it's just there are a lot of use cases like that right there lot of use cases like that right there lot of use cases like that right there are a lot of similar ones so you're are a lot of similar ones so you're are a lot of similar ones so you're predicting that within 1 to 3 years um

predicting that within 1 to 3 years um predicting that within 1 to 3 years um and in gerally enthropic has predicted and in gerally enthropic has predicted and in gerally enthropic has predicted that by late 26 early 27 we will have AI that by late 26 early 27 we will have AI

that by late 26 early 27 we will have AI systems that are quote um have the systems that are quote um have the systems that are quote um have the ability to navigate interfaces available ability to navigate interfaces available ability to navigate interfaces available to humans doing digital work today

to humans doing digital work today to humans doing digital work today intellectual capabilities matching or intellectual capabilities matching or intellectual capabilities matching or exceeding that of Nobel prize winners exceeding that of Nobel prize winners

exceeding that of Nobel prize winners and the ability to interface with the and the ability to interface with the and the ability to interface with the physical world. And then you gave an physical world. And then you gave an physical world. And then you gave an interview two months ago with Dealbook

interview two months ago with Dealbook interview two months ago with Dealbook where you were emphasizing your um your where you were emphasizing your um your where you were emphasizing your um your company's more responsible comput company's more responsible comput

[46:48]

company's more responsible comput scaling as compared to your competitors. scaling as compared to your competitors. scaling as compared to your competitors. And I'm trying to square these two views And I'm trying to square these two views And I'm trying to square these two views where if you really believe that we're

where if you really believe that we're where if you really believe that we're going to have a country of geniuses, you going to have a country of geniuses, you going to have a country of geniuses, you you want as big a data center as you can you want as big a data center as you can

you want as big a data center as you can get, there's no reason to slow down. The get, there's no reason to slow down. The get, there's no reason to slow down. The TAM of a Nobel Prize winner that is TAM of a Nobel Prize winner that is TAM of a Nobel Prize winner that is actually can do everything a Nobel Prize

actually can do everything a Nobel Prize actually can do everything a Nobel Prize winner can do is like trillions of winner can do is like trillions of winner can do is like trillions of dollars. And so I'm trying to square dollars. And so I'm trying to square

dollars. And so I'm trying to square this conservatism this conservatism this conservatism uh which seems rational if you have more uh which seems rational if you have more uh which seems rational if you have more moderate timelines with your stated

moderate timelines with your stated moderate timelines with your stated views about AI progress. views about AI progress.

views about AI progress. &gt;&gt; Yeah. So so it actually all fits &gt;&gt; Yeah. So so it actually all fits &gt;&gt; Yeah. So so it actually all fits together and and we go back to this fast together and and we go back to this fast together and and we go back to this fast but not infinitely fast diffusion. So

but not infinitely fast diffusion. So but not infinitely fast diffusion. So like let's say that we're making like let's say that we're making like let's say that we're making progress at this rate. Um you know the progress at this rate. Um you know the

progress at this rate. Um you know the the the technology is making progress the the technology is making progress the the technology is making progress this fast. Again, I have, you know, very this fast. Again, I have, you know, very this fast. Again, I have, you know, very high conviction that like it's going,

high conviction that like it's going, high conviction that like it's going, you know, the the, you know, we're going you know, the the, you know, we're going you know, the the, you know, we're going to get there within within a few years.

to get there within within a few years. to get there within within a few years. I have a hunch that we're going to get I have a hunch that we're going to get I have a hunch that we're going to get there within a year or two. So, a little there within a year or two. So, a little

there within a year or two. So, a little uncertainty on the technical side, but uncertainty on the technical side, but uncertainty on the technical side, but like, you know, pretty pretty strong like, you know, pretty pretty strong like, you know, pretty pretty strong confidence that it won't be off by much.

confidence that it won't be off by much. confidence that it won't be off by much. What I'm less certain about is again the What I'm less certain about is again the What I'm less certain about is again the economic diffusion side. Like I really economic diffusion side. Like I really

economic diffusion side. Like I really do believe that we could have models do believe that we could have models do believe that we could have models that are a country of geniuses country that are a country of geniuses country that are a country of geniuses country of geniuses in a data center in one to

of geniuses in a data center in one to of geniuses in a data center in one to two years. One question is how many two years. One question is how many two years. One question is how many years after that do the trillions in you years after that do the trillions in you

years after that do the trillions in you know do do the do the trillions in know do do the do the trillions in know do do the do the trillions in revenue start rolling in? Um I don't revenue start rolling in? Um I don't revenue start rolling in? Um I don't think it's guaranteed that it's going to

think it's guaranteed that it's going to think it's guaranteed that it's going to be immediate. Um, you know, I think it be immediate. Um, you know, I think it be immediate. Um, you know, I think it could be um one year, it could be two could be um one year, it could be two

could be um one year, it could be two years, I could even stretch it to five years, I could even stretch it to five years, I could even stretch it to five years, although I'm like I'm skeptical years, although I'm like I'm skeptical years, although I'm like I'm skeptical of that. And so we have this uncertainty

of that. And so we have this uncertainty of that. And so we have this uncertainty which is even if the technology goes as which is even if the technology goes as which is even if the technology goes as fast as I suspect that it will, we we fast as I suspect that it will, we we

fast as I suspect that it will, we we don't know exactly how fast it's going don't know exactly how fast it's going don't know exactly how fast it's going to drive revenue. We we know it's to drive revenue. We we know it's to drive revenue. We we know it's coming, but with the way you buy these

coming, but with the way you buy these coming, but with the way you buy these data centers, if you're off by a couple data centers, if you're off by a couple data centers, if you're off by a couple years, that can be ruinous. It is just years, that can be ruinous. It is just

[48:49]

years, that can be ruinous. It is just like how I wrote, you know, in machines like how I wrote, you know, in machines like how I wrote, you know, in machines of loving grace, I said, look, I think of loving grace, I said, look, I think of loving grace, I said, look, I think we might get this powerful AI, this

we might get this powerful AI, this we might get this powerful AI, this country of genius in the data center. country of genius in the data center.

country of genius in the data center. That description you gave comes from the That description you gave comes from the That description you gave comes from the machines of loving grace. I said, we'll machines of loving grace. I said, we'll machines of loving grace. I said, we'll get that 2026, maybe 2027. Again, that

get that 2026, maybe 2027. Again, that get that 2026, maybe 2027. Again, that is that is my hunch. Wouldn't be is that is my hunch. Wouldn't be is that is my hunch. Wouldn't be surprised if I'm off by a year or two, surprised if I'm off by a year or two,

surprised if I'm off by a year or two, but like that is my hunch. Let's say but like that is my hunch. Let's say but like that is my hunch. Let's say that happens. That's the starting gun.

that happens. That's the starting gun. that happens. That's the starting gun. How long does it take to cure all the How long does it take to cure all the How long does it take to cure all the diseases, right? That's that's one of diseases, right? That's that's one of

diseases, right? That's that's one of the ways that like drives a huge amount the ways that like drives a huge amount the ways that like drives a huge amount of of of of economic value, right? Like of of of of economic value, right? Like of of of of economic value, right? Like you cure you cure every disease. You

you cure you cure every disease. You you cure you cure every disease. You know, there's a question of how much of know, there's a question of how much of know, there's a question of how much of that goes to the pharmaceutical company that goes to the pharmaceutical company

that goes to the pharmaceutical company to the AI company, but there's an to the AI company, but there's an to the AI company, but there's an enormous consumer surplus because enormous consumer surplus because enormous consumer surplus because everyone, you know, assuming we can get

everyone, you know, assuming we can get everyone, you know, assuming we can get access for everyone, which I care about access for everyone, which I care about access for everyone, which I care about greatly. We, you know, we we cure all of greatly. We, you know, we we cure all of

greatly. We, you know, we we cure all of these diseases. How long does it take? these diseases. How long does it take? these diseases. How long does it take? You have to do the biological discovery.

You have to do the biological discovery. You have to do the biological discovery. you have to, you know, go you have to, you have to, you know, go you have to, you have to, you know, go you have to, you know, manufacture the new drug. You you know, manufacture the new drug. You

you know, manufacture the new drug. You have to, you know, go through the have to, you know, go through the have to, you know, go through the regulatory process. I mean, we saw this regulatory process. I mean, we saw this regulatory process. I mean, we saw this with like vaccines and COVID, right?

with like vaccines and COVID, right? with like vaccines and COVID, right? Like it there's just this we we got the Like it there's just this we we got the Like it there's just this we we got the vaccine out to everyone, but it took a vaccine out to everyone, but it took a

vaccine out to everyone, but it took a year and a half, right? And and so my year and a half, right? And and so my year and a half, right? And and so my question is, how long does it take to question is, how long does it take to question is, how long does it take to get the cure for everything, which AI is

get the cure for everything, which AI is get the cure for everything, which AI is the genius that can in theory invent out the genius that can in theory invent out the genius that can in theory invent out to everyone? How long from when that AI to everyone? How long from when that AI

to everyone? How long from when that AI first exists in the lab to when diseases first exists in the lab to when diseases first exists in the lab to when diseases have actually been cured for everyone have actually been cured for everyone have actually been cured for everyone right in in you know we've had a polio

right in in you know we've had a polio right in in you know we've had a polio vaccine for 50 years we're still trying vaccine for 50 years we're still trying vaccine for 50 years we're still trying to eradicate it in the most remote to eradicate it in the most remote

to eradicate it in the most remote corners of Africa and you know the corners of Africa and you know the corners of Africa and you know the Gateson nation is trying as hard as they Gateson nation is trying as hard as they Gateson nation is trying as hard as they can others are trying as hard as they

can others are trying as hard as they can others are trying as hard as they can but you know that's difficult again can but you know that's difficult again can but you know that's difficult again I you know I don't expect most of the I you know I don't expect most of the

I you know I don't expect most of the economic diffusion to be as difficult as economic diffusion to be as difficult as economic diffusion to be as difficult as that right that's like the most that right that's like the most that right that's like the most difficult case but but there's a There's

difficult case but but there's a There's difficult case but but there's a There's a real dilemma here and and where I've a real dilemma here and and where I've a real dilemma here and and where I've settled on it is it will be it will be a settled on it is it will be it will be a

settled on it is it will be it will be a it will be faster than anything we've it will be faster than anything we've it will be faster than anything we've seen in the world but it still has its seen in the world but it still has its seen in the world but it still has its limits and and so then when we go to

limits and and so then when we go to limits and and so then when we go to buying data centers you know you again buying data centers you know you again buying data centers you know you again again again the curve I'm looking at is again again the curve I'm looking at is

[50:49]

again again the curve I'm looking at is okay we you know we've had a 10x a year okay we you know we've had a 10x a year okay we you know we've had a 10x a year increase every year so beginning of this increase every year so beginning of this increase every year so beginning of this year we're looking at 10 billion in in

year we're looking at 10 billion in in year we're looking at 10 billion in in in annual in you know rate of annual ize in annual in you know rate of annual ize in annual in you know rate of annual ize revenue at the beginning of the year. We revenue at the beginning of the year. We

revenue at the beginning of the year. We have to decide how much compute to buy. have to decide how much compute to buy. have to decide how much compute to buy. Um Um Um and you know it takes a year or two to

and you know it takes a year or two to and you know it takes a year or two to actually build out the data centers to actually build out the data centers to actually build out the data centers to reserve the data centers. So basically reserve the data centers. So basically

reserve the data centers. So basically I'm saying like in uh 2027 how much I'm saying like in uh 2027 how much I'm saying like in uh 2027 how much compute do I get? Well I could assume um compute do I get? Well I could assume um compute do I get? Well I could assume um uh that uh the uh revenue will continue

uh that uh the uh revenue will continue uh that uh the uh revenue will continue growing 10x a year. So it'll be uh one growing 10x a year. So it'll be uh one growing 10x a year. So it'll be uh one uh one uh 100 billion at the end of 2026 uh one uh 100 billion at the end of 2026

uh one uh 100 billion at the end of 2026 and 1 trillion at the end of 2027. And and 1 trillion at the end of 2027. And and 1 trillion at the end of 2027. And so I could buy a trillion dollar so I could buy a trillion dollar so I could buy a trillion dollar actually would be like5 trillion dollars

actually would be like5 trillion dollars actually would be like5 trillion dollars of compute because it would be a of compute because it would be a of compute because it would be a trillion dollar a year for for five trillion dollar a year for for five

trillion dollar a year for for five years, right? I could buy a trillion years, right? I could buy a trillion years, right? I could buy a trillion dollars of compute that starts at the dollars of compute that starts at the dollars of compute that starts at the end of 2027. And if my if my revenue is

end of 2027. And if my if my revenue is end of 2027. And if my if my revenue is not a trillion dollars, if it's even not a trillion dollars, if it's even not a trillion dollars, if it's even 800 billion, there's no force on earth, 800 billion, there's no force on earth,

800 billion, there's no force on earth, there's there's no hedge on earth that there's there's no hedge on earth that there's there's no hedge on earth that could stop me from going bankrupt if I could stop me from going bankrupt if I could stop me from going bankrupt if I if I buy that much compute. And and so

if I buy that much compute. And and so if I buy that much compute. And and so even though a part of my brain wonders even though a part of my brain wonders even though a part of my brain wonders if it's going to keep growing 10x, I if it's going to keep growing 10x, I

if it's going to keep growing 10x, I can't buy a trillion dollars a year of can't buy a trillion dollars a year of can't buy a trillion dollars a year of compute in in in in in in in compute in in in in in in in compute in in in in in in in 2027. If I'm just off by a year in that

2027. If I'm just off by a year in that 2027. If I'm just off by a year in that rate of growth, or if the the growth rate of growth, or if the the growth rate of growth, or if the the growth rate is 5x a year instead of 10x a year, rate is 5x a year instead of 10x a year,

rate is 5x a year instead of 10x a year, then then you know that you go bankrupt. then then you know that you go bankrupt. then then you know that you go bankrupt. Um and and and so you end up in a world Um and and and so you end up in a world Um and and and so you end up in a world where you know you're supporting

where you know you're supporting where you know you're supporting hundreds of billions not trillions and hundreds of billions not trillions and hundreds of billions not trillions and you accept you accept some risk that you accept you accept some risk that

you accept you accept some risk that there's so much demand that you can't there's so much demand that you can't there's so much demand that you can't support the revenue and you accept still support the revenue and you accept still support the revenue and you accept still some risk that you know you got it wrong

some risk that you know you got it wrong some risk that you know you got it wrong and it still slow and so when I talked and it still slow and so when I talked and it still slow and so when I talked about behaving responsibly what I meant about behaving responsibly what I meant

about behaving responsibly what I meant actually was not the absolute amount actually was not the absolute amount actually was not the absolute amount that that actually was not um you know I that that actually was not um you know I that that actually was not um you know I think it is true we're spending somewhat

[52:53]

think it is true we're spending somewhat think it is true we're spending somewhat less than some of the other players. less than some of the other players.

less than some of the other players. It's actually the other things like have It's actually the other things like have It's actually the other things like have we been thoughtful about it or are we we been thoughtful about it or are we we been thoughtful about it or are we yoloing and saying, "Oh, we're going to

yoloing and saying, "Oh, we're going to yoloing and saying, "Oh, we're going to do $100 billion here, hundred billion do $100 billion here, hundred billion do $100 billion here, hundred billion dollars there." I kind of get the dollars there." I kind of get the

dollars there." I kind of get the impression that, you know, some of the impression that, you know, some of the impression that, you know, some of the other companies have not written down other companies have not written down other companies have not written down the spreadsheet that they don't really

the spreadsheet that they don't really the spreadsheet that they don't really understand the risk they're taking. understand the risk they're taking.

understand the risk they're taking. They're just kind of doing stuff because They're just kind of doing stuff because They're just kind of doing stuff because it sounds cool. Um uh and and we've it sounds cool. Um uh and and we've it sounds cool. Um uh and and we've thought carefully about it, right? We're

thought carefully about it, right? We're thought carefully about it, right? We're an enterprise business. Therefore, you an enterprise business. Therefore, you an enterprise business. Therefore, you know, we can rely more on revenue. It's know, we can rely more on revenue. It's

know, we can rely more on revenue. It's less fickle than consumer. We have less fickle than consumer. We have less fickle than consumer. We have better margins, which is the buffer better margins, which is the buffer better margins, which is the buffer between buying too much and buying too

between buying too much and buying too between buying too much and buying too little. And so, I think we bought an little. And so, I think we bought an little. And so, I think we bought an amount that allows us to capture pretty amount that allows us to capture pretty

amount that allows us to capture pretty strong upside worlds. It won't capture strong upside worlds. It won't capture strong upside worlds. It won't capture the full 10x a year. Um, and things the full 10x a year. Um, and things the full 10x a year. Um, and things would have to go pretty badly for us to

would have to go pretty badly for us to would have to go pretty badly for us to be for us to be in financial trouble. be for us to be in financial trouble.

be for us to be in financial trouble. So, I think we've thought carefully and So, I think we've thought carefully and So, I think we've thought carefully and we've made that balance. And and that's we've made that balance. And and that's we've made that balance. And and that's what I mean when I say that we're being

what I mean when I say that we're being what I mean when I say that we're being responsible. Okay. So, it seems like um responsible. Okay. So, it seems like um responsible. Okay. So, it seems like um it's possible that we're we actually it's possible that we're we actually

it's possible that we're we actually just have different definitions of the just have different definitions of the just have different definitions of the country of a genius in a data center country of a genius in a data center country of a genius in a data center because when I think of like actual

because when I think of like actual because when I think of like actual human geniuses, an actual country of human geniuses, an actual country of human geniuses, an actual country of human geniuses in a data center, I'm human geniuses in a data center, I'm

human geniuses in a data center, I'm like like like I would happily buy $5 trillion worth of I would happily buy $5 trillion worth of I would happily buy $5 trillion worth of compute to run actual country of human

compute to run actual country of human compute to run actual country of human genius in a data center. So, let's say genius in a data center. So, let's say genius in a data center. So, let's say JP Morgan or Madna or whatever doesn't JP Morgan or Madna or whatever doesn't

JP Morgan or Madna or whatever doesn't want to use them. Also, I've got a want to use them. Also, I've got a want to use them. Also, I've got a country of geniuses. they they'll start country of geniuses. they they'll start country of geniuses. they they'll start their own company and if like they they

their own company and if like they they their own company and if like they they can't start their own company and can't start their own company and can't start their own company and they're bottlenecked by clinical trials.

they're bottlenecked by clinical trials. they're bottlenecked by clinical trials. It is worth stating with clinical trials It is worth stating with clinical trials It is worth stating with clinical trials like most clinical trials fail because like most clinical trials fail because

like most clinical trials fail because the drug doesn't work. There's not the drug doesn't work. There's not the drug doesn't work. There's not efficacy, right?

efficacy, right? efficacy, right? &gt;&gt; And I make exactly that point in in &gt;&gt; And I make exactly that point in in &gt;&gt; And I make exactly that point in in machines of love and grace. I say the machines of love and grace. I say the

machines of love and grace. I say the clinical trials are going to go much clinical trials are going to go much clinical trials are going to go much faster than we're used to, but not not faster than we're used to, but not not faster than we're used to, but not not instant not infinitely fast.

instant not infinitely fast. instant not infinitely fast. &gt;&gt; And then suppose it takes a year to for &gt;&gt; And then suppose it takes a year to for &gt;&gt; And then suppose it takes a year to for the clinical trials to work out so that the clinical trials to work out so that

the clinical trials to work out so that you're getting revenue from that and you you're getting revenue from that and you you're getting revenue from that and you can make more drugs. Okay. Hey, well, can make more drugs. Okay. Hey, well, can make more drugs. Okay. Hey, well, you've got a country of geniuses and

you've got a country of geniuses and you've got a country of geniuses and you're an AI lab and you have you could you're an AI lab and you have you could you're an AI lab and you have you could use uh many more AI researchers. Um, you use uh many more AI researchers. Um, you

use uh many more AI researchers. Um, you also think that there's these like also think that there's these like also think that there's these like self-reinforcing gains from, you know, self-reinforcing gains from, you know, self-reinforcing gains from, you know, smart people working on AI tech. So,

[54:53]

smart people working on AI tech. So, smart people working on AI tech. So, like, okay, you can have the right you like, okay, you can have the right you like, okay, you can have the right you can have the data center working on like can have the data center working on like

can have the data center working on like AI progress. AI progress. AI progress. &gt;&gt; Is there more gains from buying &gt;&gt; Is there more gains from buying &gt;&gt; Is there more gains from buying &gt;&gt; like substantially more gains from

&gt;&gt; like substantially more gains from &gt;&gt; like substantially more gains from buying a trillion dollars a year of buying a trillion dollars a year of buying a trillion dollars a year of compute versus $300 billion a year of compute versus $300 billion a year of

compute versus $300 billion a year of compute? If your competitor is buying a compute? If your competitor is buying a compute? If your competitor is buying a trillion, yes, there is.

trillion, yes, there is. trillion, yes, there is. &gt;&gt; Well, no, there's some gain, but then &gt;&gt; Well, no, there's some gain, but then &gt;&gt; Well, no, there's some gain, but then but again, there's this chance that they but again, there's this chance that they

but again, there's this chance that they go bankrupt before, go bankrupt before, go bankrupt before, you know, be again, if you're off by you know, be again, if you're off by you know, be again, if you're off by only a year, you destroy yourselves.

only a year, you destroy yourselves. only a year, you destroy yourselves. That's the That's the balance. We're That's the That's the balance. We're That's the That's the balance. We're buying a lot. We're buying a hell of a buying a lot. We're buying a hell of a

buying a lot. We're buying a hell of a lot. Like, we're not we're you know, lot. Like, we're not we're you know, lot. Like, we're not we're you know, we're buying an amount that's comparable we're buying an amount that's comparable we're buying an amount that's comparable to that that, you know, the the the the

to that that, you know, the the the the to that that, you know, the the the the biggest players in the game are buying. biggest players in the game are buying.

biggest players in the game are buying. Um but but if you're asking me why why Um but but if you're asking me why why Um but but if you're asking me why why haven't we signed you know 10 10 haven't we signed you know 10 10 haven't we signed you know 10 10 trillion of compute starting in starting

trillion of compute starting in starting trillion of compute starting in starting in mid 2027 first of all it can't be in mid 2027 first of all it can't be in mid 2027 first of all it can't be produced there isn't that much in the produced there isn't that much in the

produced there isn't that much in the world um uh but but second um what if world um uh but but second um what if world um uh but but second um what if the country of geniuses comes but it the country of geniuses comes but it the country of geniuses comes but it comes in mid 2028 instead of mid2027 you

comes in mid 2028 instead of mid2027 you comes in mid 2028 instead of mid2027 you go bankrupt. So if your projection is 1 go bankrupt. So if your projection is 1 go bankrupt. So if your projection is 1 to 3 years, it seems like you should to 3 years, it seems like you should

to 3 years, it seems like you should want $10 trillion of compute by um 2029 want $10 trillion of compute by um 2029 want $10 trillion of compute by um 2029 2020 maybe 2020 latest 2020 maybe 2020 latest 2020 maybe 2020 latest &gt;&gt; like I mean you know you are like it

&gt;&gt; like I mean you know you are like it &gt;&gt; like I mean you know you are like it seems like even in your the longest seems like even in your the longest seems like even in your the longest version of the timelines you state the version of the timelines you state the

version of the timelines you state the compute you are ramping up to build compute you are ramping up to build compute you are ramping up to build doesn't seem doesn't seem doesn't seem &gt;&gt; in accordance what what makes you think

&gt;&gt; in accordance what what makes you think &gt;&gt; in accordance what what makes you think that that that &gt;&gt; well as you said you would want the 10 &gt;&gt; well as you said you would want the 10

&gt;&gt; well as you said you would want the 10 trillion the human wages let's say are trillion the human wages let's say are trillion the human wages let's say are um on the order of 50 trillion a year um on the order of 50 trillion a year um on the order of 50 trillion a year &gt;&gt; if you look at so so I won't I won't

&gt;&gt; if you look at so so I won't I won't &gt;&gt; if you look at so so I won't I won't talk about entropic in particular but if talk about entropic in particular but if talk about entropic in particular but if you talk about the industry like um the you talk about the industry like um the

you talk about the industry like um the amount of compute the industry had you amount of compute the industry had you amount of compute the industry had you know the the the the amount of compute know the the the the amount of compute know the the the the amount of compute the industry is building this year is

the industry is building this year is the industry is building this year is probably in the you know I don't know probably in the you know I don't know probably in the you know I don't know very low tens of you know call it 10 15 very low tens of you know call it 10 15

very low tens of you know call it 10 15 gawatts next year I you know it goes up gawatts next year I you know it goes up gawatts next year I you know it goes up by roughly 3x a year so like next year's by roughly 3x a year so like next year's by roughly 3x a year so like next year's 30 or 40 gigawatts and um 2028 might be

[56:53]

30 or 40 gigawatts and um 2028 might be 30 or 40 gigawatts and um 2028 might be 100 202 might like three 300 gigawatts 100 202 might like three 300 gigawatts 100 202 might like three 300 gigawatts and like each gigawatt costs like um and like each gigawatt costs like um

and like each gigawatt costs like um maybe 10 I mean I'm doing the math in my maybe 10 I mean I'm doing the math in my maybe 10 I mean I'm doing the math in my head but each gigawatt costs maybe 10 head but each gigawatt costs maybe 10 head but each gigawatt costs maybe 10 billion you know order 10 to 15 billion

billion you know order 10 to 15 billion billion you know order 10 to 15 billion a year so you know you kind of you you a year so you know you kind of you you a year so you know you kind of you you know you put that all together and know you put that all together and

know you put that all together and you're getting about about what you you're getting about about what you you're getting about about what you described you're getting multiple described you're getting multiple described you're getting multiple trillions a year by 2028 or 2029 so

trillions a year by 2028 or 2029 so trillions a year by 2028 or 2029 so you're you're getting exactly that you're you're getting exactly that you're you're getting exactly that you're getting you're getting exactly you're getting you're getting exactly

you're getting you're getting exactly what you predict what you predict what you predict &gt;&gt; um that's for the industry &gt;&gt; um that's for the industry &gt;&gt; um that's for the industry &gt;&gt; that that's for the industry That's

&gt;&gt; that that's for the industry That's &gt;&gt; that that's for the industry That's right. So suppose anthropics comput right. So suppose anthropics comput right. So suppose anthropics comput keeps 3xing a year and then by like 27 keeps 3xing a year and then by like 27

keeps 3xing a year and then by like 27 you have uh or 27 28 you have 10 gawatt you have uh or 27 28 you have 10 gawatt you have uh or 27 28 you have 10 gawatt and like multiply that by as you say um and like multiply that by as you say um and like multiply that by as you say um 10 billion. So then it's like 100

10 billion. So then it's like 100 10 billion. So then it's like 100 billion a year but then you were saying billion a year but then you were saying billion a year but then you were saying the TAM by 2028.

the TAM by 2028. the TAM by 2028. &gt;&gt; I I don't want to give exact numbers for &gt;&gt; I I don't want to give exact numbers for &gt;&gt; I I don't want to give exact numbers for anthropic but but these numbers are too anthropic but but these numbers are too

anthropic but but these numbers are too small. These numbers are too small. small. These numbers are too small. small. These numbers are too small. &gt;&gt; Okay. Interesting. I'm really proud that &gt;&gt; Okay. Interesting. I'm really proud that &gt;&gt; Okay. Interesting. I'm really proud that the puzzles I've worked on with Jane

the puzzles I've worked on with Jane the puzzles I've worked on with Jane Street have resulted in them hiring a Street have resulted in them hiring a Street have resulted in them hiring a bunch of people for my audience. Well, bunch of people for my audience. Well,

bunch of people for my audience. Well, they're still hiring and they just sent they're still hiring and they just sent they're still hiring and they just sent me another puzzle. For this one, they me another puzzle. For this one, they me another puzzle. For this one, they spent about 20,000 GPU hours training

spent about 20,000 GPU hours training spent about 20,000 GPU hours training backd doors into three different backd doors into three different backd doors into three different language models. Each one has a hidden language models. Each one has a hidden

language models. Each one has a hidden prompt that elicits completely different prompt that elicits completely different prompt that elicits completely different behavior. You just have to find the behavior. You just have to find the behavior. You just have to find the trigger. This is particularly cool

trigger. This is particularly cool trigger. This is particularly cool because finding backd doorors is because finding backd doorors is because finding backd doorors is actually an open question in Frontier AI actually an open question in Frontier AI

actually an open question in Frontier AI research. Enthropic actually released a research. Enthropic actually released a research. Enthropic actually released a couple of papers about sleep agents and couple of papers about sleep agents and couple of papers about sleep agents and they showed that you can build a simple

they showed that you can build a simple they showed that you can build a simple classifier on the residual stream to classifier on the residual stream to classifier on the residual stream to detect when a back door is about to detect when a back door is about to

detect when a back door is about to fire, but they already knew what the fire, but they already knew what the fire, but they already knew what the triggers were because they built them.

triggers were because they built them. triggers were because they built them. Here you don't. And it's not feasible to Here you don't. And it's not feasible to Here you don't. And it's not feasible to check the activations for all possible check the activations for all possible

check the activations for all possible trigger phrases. Unlike the other trigger phrases. Unlike the other trigger phrases. Unlike the other puzzles they made for this podcast, Jane puzzles they made for this podcast, Jane puzzles they made for this podcast, Jane Street isn't even sure this one is

Street isn't even sure this one is Street isn't even sure this one is solvable, but they've set aside $50,000 solvable, but they've set aside $50,000 solvable, but they've set aside $50,000 for the best attempts and write-ups. The for the best attempts and write-ups. The

for the best attempts and write-ups. The puzzle's live at puzzle's live at puzzle's live at janestreet.com/themarcash janestreet.com/themarcash janestreet.com/themarcash and they're accepting submissions until

and they're accepting submissions until and they're accepting submissions until April 1st. All right, back to Dario. April 1st. All right, back to Dario.

April 1st. All right, back to Dario. You've told investors that you plan to You've told investors that you plan to You've told investors that you plan to be profitable starting 28 and this is be profitable starting 28 and this is be profitable starting 28 and this is the year where we're like potentially

[58:55]

the year where we're like potentially the year where we're like potentially getting the country of geniuses at a getting the country of geniuses at a getting the country of geniuses at a data center and you know this is like data center and you know this is like

data center and you know this is like going to now unlock all this uh progress going to now unlock all this uh progress going to now unlock all this uh progress and uh medicine and uh health and etc and uh medicine and uh health and etc and uh medicine and uh health and etc etc and new technologies. Wouldn't this

etc and new technologies. Wouldn't this etc and new technologies. Wouldn't this be a particular exactly the time where be a particular exactly the time where be a particular exactly the time where you'd like want to reinvest in the you'd like want to reinvest in the

you'd like want to reinvest in the business and build bigger countries so business and build bigger countries so business and build bigger countries so they can make more discoveries?

they can make more discoveries? they can make more discoveries? &gt;&gt; So I mean profit profitability is this &gt;&gt; So I mean profit profitability is this &gt;&gt; So I mean profit profitability is this kind of like weird thing in this field.

kind of like weird thing in this field. kind of like weird thing in this field. I I like like I don't think I I don't I I like like I don't think I I don't I I like like I don't think I I don't think in this field profitability is think in this field profitability is

think in this field profitability is actually a measure of actually a measure of actually a measure of uh um you know kind of spending down uh um you know kind of spending down uh um you know kind of spending down versus investing in the business like

versus investing in the business like versus investing in the business like let's let's just let's just take a model let's let's just let's just take a model let's let's just let's just take a model of this. I actually think profitability of this. I actually think profitability

of this. I actually think profitability happens when you underestimated the happens when you underestimated the happens when you underestimated the amount of demand you were going to get amount of demand you were going to get amount of demand you were going to get and loss happens when you overestimated

and loss happens when you overestimated and loss happens when you overestimated the amount of demand you were going to the amount of demand you were going to the amount of demand you were going to get. Um because you're buying the data get. Um because you're buying the data

get. Um because you're buying the data centers ahead of time. So think about it centers ahead of time. So think about it centers ahead of time. So think about it this way. Um ideally you would like and this way. Um ideally you would like and this way. Um ideally you would like and again these are stylized facts. These

again these are stylized facts. These again these are stylized facts. These numbers are not exact for I'm just numbers are not exact for I'm just numbers are not exact for I'm just trying to make a toy model here. Let's trying to make a toy model here. Let's

trying to make a toy model here. Let's say half of your compute is for training say half of your compute is for training say half of your compute is for training and half of your compute is for and half of your compute is for and half of your compute is for inference. Um, and you know the

inference. Um, and you know the inference. Um, and you know the inference has some gross margin that's inference has some gross margin that's inference has some gross margin that's like more than 50%. Um, and so what that like more than 50%. Um, and so what that

like more than 50%. Um, and so what that means is that if you were in steady means is that if you were in steady means is that if you were in steady state, you build a data center, if you state, you build a data center, if you state, you build a data center, if you knew exactly exactly exactly the demand

knew exactly exactly exactly the demand knew exactly exactly exactly the demand you were getting, you would um uh uh uh you were getting, you would um uh uh uh you were getting, you would um uh uh uh you know you would you would you you you know you would you would you you

you know you would you would you you would you would get a certain amount of would you would get a certain amount of would you would get a certain amount of revenue. say, I don't know, uh, uh, revenue. say, I don't know, uh, uh, revenue. say, I don't know, uh, uh, let's say you pay $100 billion a year

let's say you pay $100 billion a year let's say you pay $100 billion a year for compute and on $50 billion a year, for compute and on $50 billion a year, for compute and on $50 billion a year, you support $150 billion on of of of of you support $150 billion on of of of of

you support $150 billion on of of of of revenue and the other 50 billion the revenue and the other 50 billion the revenue and the other 50 billion the other 50 billion are used for training.

other 50 billion are used for training. other 50 billion are used for training. Um, so basically, you're profitable. You Um, so basically, you're profitable. You Um, so basically, you're profitable. You make you make you make $50 billion of make you make you make $50 billion of

make you make you make $50 billion of profit. Those are the economics of the profit. Those are the economics of the profit. Those are the economics of the industry today or or sorry, not today, industry today or or sorry, not today, industry today or or sorry, not today, but like that's where we're where we're

but like that's where we're where we're but like that's where we're where we're projecting forward in a year or two. The projecting forward in a year or two. The projecting forward in a year or two. The only thing that makes that not the case only thing that makes that not the case

only thing that makes that not the case is if you get less demand than 50 is if you get less demand than 50 is if you get less demand than 50 billion um then you have more than 50% billion um then you have more than 50% billion um then you have more than 50% of your your data center for research

[60:58]

of your your data center for research of your your data center for research and you're not profitable. So you you and you're not profitable. So you you and you're not profitable. So you you know you train stronger models but know you train stronger models but

know you train stronger models but you're like not profitable. Um if you uh you're like not profitable. Um if you uh you're like not profitable. Um if you uh get more demand than you thought then get more demand than you thought then get more demand than you thought then your research gets squeezed um but uh

your research gets squeezed um but uh your research gets squeezed um but uh you know you're you're you're kind of you know you're you're you're kind of you know you're you're you're kind of able to support more inference and able to support more inference and

able to support more inference and you're more profitable. So it's maybe you're more profitable. So it's maybe you're more profitable. So it's maybe I'm not explaining it well but but the I'm not explaining it well but but the I'm not explaining it well but but the thing I'm trying to say is you decide

thing I'm trying to say is you decide thing I'm trying to say is you decide the amount of compute first and then you the amount of compute first and then you the amount of compute first and then you have some target desire of of inference have some target desire of of inference

have some target desire of of inference versus versus training but that gets versus versus training but that gets versus versus training but that gets determined by demand. It doesn't get determined by demand. It doesn't get determined by demand. It doesn't get determined by

determined by determined by &gt;&gt; what I'm hearing is the reason you're &gt;&gt; what I'm hearing is the reason you're &gt;&gt; what I'm hearing is the reason you're predicting profit is that you are predicting profit is that you are

predicting profit is that you are systematically underestimate uh systematically underestimate uh systematically underestimate uh underinvesting in compute right because underinvesting in compute right because underinvesting in compute right because if you actually

if you actually if you actually &gt;&gt; No I'm saying I'm saying it's hard to &gt;&gt; No I'm saying I'm saying it's hard to &gt;&gt; No I'm saying I'm saying it's hard to predict. So, so these things about 2028 predict. So, so these things about 2028

predict. So, so these things about 2028 and when it will happen, that's our and when it will happen, that's our and when it will happen, that's our that's our attempt to do the best we can that's our attempt to do the best we can that's our attempt to do the best we can with investors, all of this stuff is

with investors, all of this stuff is with investors, all of this stuff is really uncertain because of the cone of really uncertain because of the cone of really uncertain because of the cone of uncertainty. Like we could be profitable uncertainty. Like we could be profitable

uncertainty. Like we could be profitable in 2026 if the if the revenue grows fast in 2026 if the if the revenue grows fast in 2026 if the if the revenue grows fast enough and then and then um uh you know enough and then and then um uh you know enough and then and then um uh you know if we if we overestimate or

if we if we overestimate or if we if we overestimate or underestimate the next year that could underestimate the next year that could underestimate the next year that could swing wildly. Like I I I what I'm trying swing wildly. Like I I I what I'm trying

swing wildly. Like I I I what I'm trying to get at is you have a model in your to get at is you have a model in your to get at is you have a model in your head of like the the business invests head of like the the business invests head of like the the business invests invests invests invests gets scale and

invests invests invests gets scale and invests invests invests gets scale and and and and kind of then becomes and and and kind of then becomes and and and kind of then becomes profitable. There's a single point at profitable. There's a single point at

profitable. There's a single point at which things turn around. I don't think which things turn around. I don't think which things turn around. I don't think the economics of this industry work that the economics of this industry work that the economics of this industry work that way.

way. way. &gt;&gt; I see. So if I'm understanding &gt;&gt; I see. So if I'm understanding &gt;&gt; I see. So if I'm understanding correctly, you're saying because of the correctly, you're saying because of the

correctly, you're saying because of the discrepancy between the amount of discrepancy between the amount of discrepancy between the amount of compute we should have gotten and the compute we should have gotten and the compute we should have gotten and the amount of compute we got, we we were

amount of compute we got, we we were amount of compute we got, we we were like sort of forced to make profit. But like sort of forced to make profit. But like sort of forced to make profit. But that that doesn't mean we're going to that that doesn't mean we're going to

that that doesn't mean we're going to continue making profit. But we're going continue making profit. But we're going continue making profit. But we're going to like reinvest the money because well to like reinvest the money because well to like reinvest the money because well now AI has made so much progress and we

now AI has made so much progress and we now AI has made so much progress and we want the bigger country of geniuses and want the bigger country of geniuses and want the bigger country of geniuses and so then back into uh revenue is high but so then back into uh revenue is high but

so then back into uh revenue is high but losses are also high. If we if we losses are also high. If we if we losses are also high. If we if we predict if every year we predict exactly predict if every year we predict exactly predict if every year we predict exactly what the demand is going to be will be

what the demand is going to be will be what the demand is going to be will be profitable every year because grow profitable every year because grow profitable every year because grow because spending spending 50% of your because spending spending 50% of your

because spending spending 50% of your compute on on 50% of your compute on compute on on 50% of your compute on compute on on 50% of your compute on research roughly um plus a gross margin research roughly um plus a gross margin research roughly um plus a gross margin that's higher than 50%. And and correct

[63:01]

that's higher than 50%. And and correct that's higher than 50%. And and correct demand prediction leads to profit. demand prediction leads to profit.

demand prediction leads to profit. That's the prof that's that's the That's the prof that's that's the That's the prof that's that's the profitable business model that I think profitable business model that I think profitable business model that I think is kind of like there but like obsc

is kind of like there but like obsc is kind of like there but like obsc obscured by these like building ahead obscured by these like building ahead obscured by these like building ahead and prediction errors. I and prediction errors. I

and prediction errors. I &gt;&gt; I guess you're treating the 50% as a uh &gt;&gt; I guess you're treating the 50% as a uh &gt;&gt; I guess you're treating the 50% as a uh as a sort of like you know just like a as a sort of like you know just like a as a sort of like you know just like a given constant whereas you in fact if

given constant whereas you in fact if given constant whereas you in fact if you if AI progress is fast and you can you if AI progress is fast and you can you if AI progress is fast and you can increase the progress by scaling up more increase the progress by scaling up more

increase the progress by scaling up more you just have more than 50% and not make you just have more than 50% and not make you just have more than 50% and not make profit.

profit. profit. &gt;&gt; Here's what I'll say. You might want to &gt;&gt; Here's what I'll say. You might want to &gt;&gt; Here's what I'll say. You might want to scale up it more. you might want to scale up it more. you might want to

scale up it more. you might want to scale it up more, but but but you know, scale it up more, but but but you know, scale it up more, but but but you know, remember the log returns to scale, remember the log returns to scale, remember the log returns to scale, right? If if 70% would get you a very

right? If if 70% would get you a very right? If if 70% would get you a very little bit of a smaller model through a little bit of a smaller model through a little bit of a smaller model through a factor of of 1.4x, right? like that factor of of 1.4x, right? like that

factor of of 1.4x, right? like that extra $20 billion is is is is you know extra $20 billion is is is is you know extra $20 billion is is is is you know that each each dollar there is worth that each each dollar there is worth that each each dollar there is worth much less to you because because the log

much less to you because because the log much less to you because because the log linear setup and so you might find that linear setup and so you might find that linear setup and so you might find that it's better to invest that that that it's better to invest that that that

it's better to invest that that that that it's better to invest that $20 that it's better to invest that $20 that it's better to invest that $20 billion in you know in in serving billion in you know in in serving billion in you know in in serving inference or in hiring engineers who are

inference or in hiring engineers who are inference or in hiring engineers who are who who are kind of better who are who who who are kind of better who are who who who are kind of better who are who are kind of better who are kind of are kind of better who are kind of

are kind of better who are kind of better at what they're doing. So the the better at what they're doing. So the the better at what they're doing. So the the reason I said 50% that's not that's not reason I said 50% that's not that's not reason I said 50% that's not that's not exactly our target. It's not exactly

exactly our target. It's not exactly exactly our target. It's not exactly going to be 50%. It will probably vary going to be 50%. It will probably vary going to be 50%. It will probably vary vary over time. What what I'm saying is vary over time. What what I'm saying is

vary over time. What what I'm saying is the the the the like log linear return the the the the like log linear return the the the the like log linear return what it leads to is you spend of order what it leads to is you spend of order what it leads to is you spend of order one fraction of the business, right?

one fraction of the business, right? one fraction of the business, right? Like not 5% not 95%. And then it then Like not 5% not 95%. And then it then Like not 5% not 95%. And then it then you know then then then you get you know then then then you get

you know then then then you get diminishing returns because of the diminishing returns because of the diminishing returns because of the because the walls that I'm like because the walls that I'm like because the walls that I'm like convincing Dario to like believe in AI

convincing Dario to like believe in AI convincing Dario to like believe in AI progress or something but like uh okay progress or something but like uh okay progress or something but like uh okay you you don't invest in research because you you don't invest in research because

you you don't invest in research because it has diminishing returns but you it has diminishing returns but you it has diminishing returns but you invest in the other things you mentioned invest in the other things you mentioned invest in the other things you mentioned &gt;&gt; again again we're talking about

&gt;&gt; again again we're talking about &gt;&gt; again again we're talking about diminishing returns diminishing returns diminishing returns after you're spending 50 billion a year after you're spending 50 billion a year

after you're spending 50 billion a year right like this is a point I'm sure you right like this is a point I'm sure you right like this is a point I'm sure you would make but like diminishing returns would make but like diminishing returns would make but like diminishing returns on a genius is could be quite high and

on a genius is could be quite high and on a genius is could be quite high and more generally like what is profit put more generally like what is profit put more generally like what is profit put in a market economy profit is basically in a market economy profit is basically

in a market economy profit is basically saying the other companies in the market saying the other companies in the market saying the other companies in the market can like do more things with this money can like do more things with this money can like do more things with this money that I

[65:01]

that I that I &gt;&gt; yeah put aside entropic I'm just trying &gt;&gt; yeah put aside entropic I'm just trying &gt;&gt; yeah put aside entropic I'm just trying to like because I you know I don't want to like because I you know I don't want

to like because I you know I don't want to give information about entropic is to give information about entropic is to give information about entropic is why I'm giving these stylized numbers why I'm giving these stylized numbers why I'm giving these stylized numbers but like let's just derive the

but like let's just derive the but like let's just derive the equilibrium of the industry right I equilibrium of the industry right I equilibrium of the industry right I think the so so so why doesn't everyone think the so so so why doesn't everyone

think the so so so why doesn't everyone spend 100% of their um uh you know 100% spend 100% of their um uh you know 100% spend 100% of their um uh you know 100% of their compute on training and not of their compute on training and not of their compute on training and not serve any customers right it's because

serve any customers right it's because serve any customers right it's because if They didn't get any revenue. They if They didn't get any revenue. They if They didn't get any revenue. They couldn't raise money. They couldn't do couldn't raise money. They couldn't do

couldn't raise money. They couldn't do comput deals. They couldn't buy more comput deals. They couldn't buy more comput deals. They couldn't buy more compute the next year. So, there's going compute the next year. So, there's going compute the next year. So, there's going to be an equilibrium where every every

to be an equilibrium where every every to be an equilibrium where every every company spends less than 100% on on on company spends less than 100% on on on company spends less than 100% on on on on on training and certainly less than on on training and certainly less than

on on training and certainly less than 100% on inference. It should be clear 100% on inference. It should be clear 100% on inference. It should be clear why you don't just serve the current why you don't just serve the current why you don't just serve the current models and and you know and and and

models and and you know and and and models and and you know and and and never train another model because then never train another model because then never train another model because then you don't have any demand because you you don't have any demand because you

you don't have any demand because you because you'll fall behind. So, there's because you'll fall behind. So, there's because you'll fall behind. So, there's some equilibrium. It's it's not going to some equilibrium. It's it's not going to some equilibrium. It's it's not going to be 10%, it's not going to be 90%. Let's

be 10%, it's not going to be 90%. Let's be 10%, it's not going to be 90%. Let's just say as a stylized fact it's 50%. just say as a stylized fact it's 50%.

just say as a stylized fact it's 50%. That's what I'm getting at. And and and That's what I'm getting at. And and and That's what I'm getting at. And and and I think we're going to be in a position I think we're going to be in a position I think we're going to be in a position where that equilibrium of how much you

where that equilibrium of how much you where that equilibrium of how much you spend on training is less than the gross spend on training is less than the gross spend on training is less than the gross margins that that you're that that that margins that that you're that that that

margins that that you're that that that you're able to get on compute. And so you're able to get on compute. And so you're able to get on compute. And so the the the the underlying economics are the the the the underlying economics are the the the the underlying economics are profitable. The problem is you have this

profitable. The problem is you have this profitable. The problem is you have this this hellish demand prediction problem this hellish demand prediction problem this hellish demand prediction problem when you're when you're buying the next when you're when you're buying the next

when you're when you're buying the next year of compute and you might guess year of compute and you might guess year of compute and you might guess under and be very profitable but have no under and be very profitable but have no under and be very profitable but have no compute for research or you might guess

compute for research or you might guess compute for research or you might guess over and you know you're you're you're over and you know you're you're you're over and you know you're you're you're um uh you you are not profitable and you um uh you you are not profitable and you

um uh you you are not profitable and you have all the compute compute for have all the compute compute for have all the compute compute for research in the world.

research in the world. research in the world. &gt;&gt; Does does that make sense just as a &gt;&gt; Does does that make sense just as a &gt;&gt; Does does that make sense just as a dynamic model of the industry? May maybe dynamic model of the industry? May maybe

dynamic model of the industry? May maybe stepping back I'm like uh I I I'm not stepping back I'm like uh I I I'm not stepping back I'm like uh I I I'm not saying I I think the country of genius saying I I think the country of genius saying I I think the country of genius is going to come in two years and

is going to come in two years and is going to come in two years and therefore you should buy this compute. therefore you should buy this compute.

therefore you should buy this compute. Um to me what you're saying the end Um to me what you're saying the end Um to me what you're saying the end conclusion you're arriving at makes a conclusion you're arriving at makes a conclusion you're arriving at makes a lot of sense but uh that's because like

lot of sense but uh that's because like lot of sense but uh that's because like oh it seems like country geniuses is oh it seems like country geniuses is oh it seems like country geniuses is hard and there's a long way to go. And hard and there's a long way to go. And

hard and there's a long way to go. And so the stepping back the thing I'm so the stepping back the thing I'm so the stepping back the thing I'm trying to get at is more like trying to get at is more like trying to get at is more like it seems like your worldview is

[67:03]

it seems like your worldview is it seems like your worldview is compatible with somebody who says uh compatible with somebody who says uh compatible with somebody who says uh we're like 10 years away from a world in we're like 10 years away from a world in

we're like 10 years away from a world in which like we're generating trillions of which like we're generating trillions of which like we're generating trillions of dollars.

dollars. dollars. &gt;&gt; That's just that's just not my view. &gt;&gt; That's just that's just not my view.

&gt;&gt; That's just that's just not my view. That is that is not my view. Like I I so That is that is not my view. Like I I so That is that is not my view. Like I I so so I'll like I'll like make another so I'll like I'll like make another so I'll like I'll like make another prediction. It is hard for me to see

prediction. It is hard for me to see prediction. It is hard for me to see that that there won't be trillions of that that there won't be trillions of that that there won't be trillions of dollars in revenue before 2030. Um like dollars in revenue before 2030. Um like

dollars in revenue before 2030. Um like uh I can I can construct a plausible uh I can I can construct a plausible uh I can I can construct a plausible world. It takes maybe three years. So world. It takes maybe three years. So world. It takes maybe three years. So that that you know that would be the end

that that you know that would be the end that that you know that would be the end of what I think it's plausible like in of what I think it's plausible like in of what I think it's plausible like in 2028 we get the the real country of 2028 we get the the real country of

2028 we get the the real country of geniuses in a data center. You know the geniuses in a data center. You know the geniuses in a data center. You know the revenue's been been go you know the revenue's been been go you know the revenue's been been go you know the revenue has been going into the maybe is

revenue has been going into the maybe is revenue has been going into the maybe is is in the low hundreds of billions by by is in the low hundreds of billions by by is in the low hundreds of billions by by by by 2028 and and and then the country by by 2028 and and and then the country

by by 2028 and and and then the country of geniuses accelerates it to trillions, of geniuses accelerates it to trillions, of geniuses accelerates it to trillions, you know, and and we're basically we're you know, and and we're basically we're you know, and and we're basically we're basically on the slow end of diffusion.

basically on the slow end of diffusion. basically on the slow end of diffusion. It takes two years to get to the It takes two years to get to the It takes two years to get to the trillions. that that that would that trillions. that that that would that

trillions. that that that would that that that would be the world where it that that would be the world where it that that would be the world where it takes until that would be the world takes until that would be the world takes until that would be the world where it takes until 2030. I I I suspect

where it takes until 2030. I I I suspect where it takes until 2030. I I I suspect even composing the technical exponential even composing the technical exponential even composing the technical exponential and the diffusion exponential will get and the diffusion exponential will get

and the diffusion exponential will get there before 2030. So you laid out a there before 2030. So you laid out a there before 2030. So you laid out a model where anthropic makes profit model where anthropic makes profit model where anthropic makes profit because it seems like fundamentally

because it seems like fundamentally because it seems like fundamentally we're in a computed world and so it's we're in a computed world and so it's we're in a computed world and so it's like eventually we keep growing comput.

like eventually we keep growing comput. like eventually we keep growing comput. Well, I think I think the way the profit Well, I think I think the way the profit Well, I think I think the way the profit comes is again and and you know, let's comes is again and and you know, let's

comes is again and and you know, let's let's just abstract the whole industry let's just abstract the whole industry let's just abstract the whole industry here. Like we have a you know, let's here. Like we have a you know, let's here. Like we have a you know, let's just imagine we're we're in like an

just imagine we're we're in like an just imagine we're we're in like an economics textbook. We have a small economics textbook. We have a small economics textbook. We have a small number of firms each can invest a number of firms each can invest a

number of firms each can invest a limited amount in you know or or or like limited amount in you know or or or like limited amount in you know or or or like each can invest some fra fraction in each can invest some fra fraction in each can invest some fra fraction in R&amp;D. They have some marginal cost to

R&amp;D. They have some marginal cost to R&amp;D. They have some marginal cost to serve. the margins on that the profit serve. the margins on that the profit serve. the margins on that the profit mar the gross profit margins on that mar the gross profit margins on that

mar the gross profit margins on that marginal cost are like very high because marginal cost are like very high because marginal cost are like very high because because because because inference is because because because inference is because because because inference is efficient there's some competition but

efficient there's some competition but efficient there's some competition but the models are also differentiated the models are also differentiated the models are also differentiated there's some there's some um you know there's some there's some um you know

there's some there's some um you know companies will compete to push their companies will compete to push their companies will compete to push their research budgets up but like because research budgets up but like because research budgets up but like because there's a small number of players you

there's a small number of players you there's a small number of players you know we have the what is it called in know we have the what is it called in know we have the what is it called in the corno equilibrium I think is what the corno equilibrium I think is what

the corno equilibrium I think is what the what the small number of firm the what the small number of firm the what the small number of firm equilibrium is it the point is it it equilibrium is it the point is it it equilibrium is it the point is it it doesn't equilibrate to perfect

[69:08]

doesn't equilibrate to perfect doesn't equilibrate to perfect competition with with with with with competition with with with with with competition with with with with with with with

with zero margins. If there's like three zero margins. If there's like three zero margins. If there's like three firms, if there's three firms in the firms, if there's three firms in the firms, if there's three firms in the economy, all are kind of independently

economy, all are kind of independently economy, all are kind of independently behaving behaving rationally, it doesn't behaving behaving rationally, it doesn't behaving behaving rationally, it doesn't equilibrate to zero.

equilibrate to zero. equilibrate to zero. &gt;&gt; Um, help me understand that because &gt;&gt; Um, help me understand that because &gt;&gt; Um, help me understand that because right now we do have three leading firms right now we do have three leading firms

right now we do have three leading firms and they're not making profit. Um, and and they're not making profit. Um, and and they're not making profit. Um, and so what what uh yeah, what what is so what what uh yeah, what what is so what what uh yeah, what what is changing? Yeah. So the the again the

changing? Yeah. So the the again the changing? Yeah. So the the again the gross margins right now are very gross margins right now are very gross margins right now are very positive. What's happen what what's positive. What's happen what what's

positive. What's happen what what's happening is a combination of two happening is a combination of two happening is a combination of two things. One is we're still in the things. One is we're still in the things. One is we're still in the exponential scale up phase of compute.

exponential scale up phase of compute. exponential scale up phase of compute. Um, so what basically what that means is Um, so what basically what that means is Um, so what basically what that means is we're training like a model gets we're training like a model gets

we're training like a model gets trained, it costs, you know, let's say a trained, it costs, you know, let's say a trained, it costs, you know, let's say a model got trained that costs uh a model got trained that costs uh a model got trained that costs uh a billion last year. Um, and then uh this

billion last year. Um, and then uh this billion last year. Um, and then uh this year it produced uh $4 billion of year it produced uh $4 billion of year it produced uh $4 billion of revenue and cost $1 billion to to uh to revenue and cost $1 billion to to uh to

revenue and cost $1 billion to to uh to to to inference from. Um so you know to to inference from. Um so you know to to inference from. Um so you know again I'm using stylized number here but again I'm using stylized number here but again I'm using stylized number here but you know that would be 75% you know

you know that would be 75% you know you know that would be 75% you know gross gross gross margins and you know gross gross gross margins and you know gross gross gross margins and you know this this 25% tax. So that model as a this this 25% tax. So that model as a

this this 25% tax. So that model as a whole makes $2 billion. Um but at the whole makes $2 billion. Um but at the whole makes $2 billion. Um but at the same time we're spending $10 billion to same time we're spending $10 billion to same time we're spending $10 billion to train the next model because there's an

train the next model because there's an train the next model because there's an exponential scale up and so the company exponential scale up and so the company exponential scale up and so the company loses money. Each model makes money but loses money. Each model makes money but

loses money. Each model makes money but the company loses money. The equilibrium the company loses money. The equilibrium the company loses money. The equilibrium I'm talking about is an equilibrium I'm talking about is an equilibrium I'm talking about is an equilibrium where we have the country of geniuses.

where we have the country of geniuses. where we have the country of geniuses. We have the country of geniuses in a We have the country of geniuses in a We have the country of geniuses in a data center, but that that um model data center, but that that um model

data center, but that that um model training scale up has equilibrated more. training scale up has equilibrated more. training scale up has equilibrated more. Maybe maybe it's still it's still going Maybe maybe it's still it's still going Maybe maybe it's still it's still going up. We're still trying to predict the

up. We're still trying to predict the up. We're still trying to predict the demand, but it's more it's more um demand, but it's more it's more um demand, but it's more it's more um leveled out. Um I'll give you a couple leveled out. Um I'll give you a couple

leveled out. Um I'll give you a couple things there. So, um let's start with things there. So, um let's start with things there. So, um let's start with the current world. Um in the current the current world. Um in the current the current world. Um in the current world, you're right that as you said

world, you're right that as you said world, you're right that as you said before, if you treat each individual before, if you treat each individual before, if you treat each individual model as a company, it's profitable. But model as a company, it's profitable. But

model as a company, it's profitable. But of course, a big part of the production of course, a big part of the production of course, a big part of the production function of being a frontier lab is function of being a frontier lab is function of being a frontier lab is training the next model, right? So if

[71:13]

training the next model, right? So if training the next model, right? So if you didn't do that, then you'd make you didn't do that, then you'd make you didn't do that, then you'd make profit for two months and then you profit for two months and then you

profit for two months and then you wouldn't have margins because you wouldn't have margins because you wouldn't have margins because you wouldn't have the best model and then so wouldn't have the best model and then so wouldn't have the best model and then so yeah, you can make profits for two

yeah, you can make profits for two yeah, you can make profits for two months on the current at some point that months on the current at some point that months on the current at some point that reaches the biggest scale that it can reaches the biggest scale that it can

reaches the biggest scale that it can reach and then and then in equilibrium reach and then and then in equilibrium reach and then and then in equilibrium we have algorithmic improvements, but we have algorithmic improvements, but we have algorithmic improvements, but we're spending roughly the same amount

we're spending roughly the same amount we're spending roughly the same amount to train the next model as as as we to train the next model as as as we to train the next model as as as we spent to train the current model. Um so spent to train the current model. Um so

spent to train the current model. Um so this equilibrium relies this equilibrium relies this equilibrium relies &gt;&gt; I mean at some point at some at at some &gt;&gt; I mean at some point at some at at some &gt;&gt; I mean at some point at some at at some point you run out of money in the

point you run out of money in the point you run out of money in the economy economy economy &gt;&gt; uh a fixed lump of labor files the &gt;&gt; uh a fixed lump of labor files the

&gt;&gt; uh a fixed lump of labor files the economy is going to grow right that's economy is going to grow right that's economy is going to grow right that's one of your predictions we're going to one of your predictions we're going to one of your predictions we're going to have but this is but this is another

have but this is but this is another have but this is but this is another example of the theme I was talking about example of the theme I was talking about example of the theme I was talking about which is that the economy will grow much which is that the economy will grow much

which is that the economy will grow much faster with AI than I think it ever has faster with AI than I think it ever has faster with AI than I think it ever has before but it's not like right now the before but it's not like right now the before but it's not like right now the compute is growing 3x a year I don't

compute is growing 3x a year I don't compute is growing 3x a year I don't believe the economy is going to grow believe the economy is going to grow believe the economy is going to grow 300% % a year. Like I said this in 300% % a year. Like I said this in

300% % a year. Like I said this in Machines of Loving Grace, like I think Machines of Loving Grace, like I think Machines of Loving Grace, like I think we we may get 10 or 20% per year growth we we may get 10 or 20% per year growth we we may get 10 or 20% per year growth in the economy, but we're not going to

in the economy, but we're not going to in the economy, but we're not going to get 300% growth in the economy. So I get 300% growth in the economy. So I get 300% growth in the economy. So I think I think in the end, you know, if think I think in the end, you know, if

think I think in the end, you know, if if compute becomes the majority of what if compute becomes the majority of what if compute becomes the majority of what the economy produces, it's it's going to the economy produces, it's it's going to the economy produces, it's it's going to be capped by that. So okay, now let's

be capped by that. So okay, now let's be capped by that. So okay, now let's assume a model where compute stays assume a model where compute stays assume a model where compute stays capped. Yeah. Um, the world where capped. Yeah. Um, the world where

capped. Yeah. Um, the world where Frontier Labs are making money is one Frontier Labs are making money is one Frontier Labs are making money is one where they continue to make um, fast where they continue to make um, fast where they continue to make um, fast progress because fundamentally your

progress because fundamentally your progress because fundamentally your margin is limited by how good the margin is limited by how good the margin is limited by how good the alternative is. And so you are able to alternative is. And so you are able to

alternative is. And so you are able to make money because you have a frontier make money because you have a frontier make money because you have a frontier model. Um, if you didn't have frontier model. Um, if you didn't have frontier model. Um, if you didn't have frontier model, you wouldn't be making money. Um,

model, you wouldn't be making money. Um, model, you wouldn't be making money. Um, &gt;&gt; and and so this this model requires &gt;&gt; and and so this this model requires &gt;&gt; and and so this this model requires there never to be a steady state like there never to be a steady state like

there never to be a steady state like forever and ever you keep making more forever and ever you keep making more forever and ever you keep making more progress.

progress. progress. &gt;&gt; I don't think that's true. True. I mean &gt;&gt; I don't think that's true. True. I mean &gt;&gt; I don't think that's true. True. I mean I I feel feel like we're we're like I I feel feel like we're we're like

I I feel feel like we're we're like we're talk we're we're you know I feel we're talk we're we're you know I feel we're talk we're we're you know I feel like this is an economics uh like uh you like this is an economics uh like uh you like this is an economics uh like uh you know this is like an economics class you

know this is like an economics class you know this is like an economics class you know quote we never stop talking about know quote we never stop talking about know quote we never stop talking about economics.

economics. economics. &gt;&gt; We never we never stop talking about &gt;&gt; We never we never stop talking about &gt;&gt; We never we never stop talking about economics. So no but but there there are economics. So no but but there there are

economics. So no but but there there are worlds in which um you know there so I I worlds in which um you know there so I I worlds in which um you know there so I I don't think this field's going to be a I don't think this field's going to be a I don't think this field's going to be a I don't think this field's going to be a

don't think this field's going to be a don't think this field's going to be a monopoly. All my lawyers never want me monopoly. All my lawyers never want me monopoly. All my lawyers never want me to say the word monopoly. Um but I don't to say the word monopoly. Um but I don't

[73:16]

to say the word monopoly. Um but I don't think this field's going to be a think this field's going to be a think this field's going to be a monopoly. But but you do get you get monopoly. But but you do get you get monopoly. But but you do get you get industries in which there are small

industries in which there are small industries in which there are small number of players, not one but a small number of players, not one but a small number of players, not one but a small number of players. And ordinarily like number of players. And ordinarily like

number of players. And ordinarily like the the way you get monopolies like the the way you get monopolies like the the way you get monopolies like Facebook or or Meta, I always call them Facebook or or Meta, I always call them Facebook or or Meta, I always call them Facebook but um uh uh is is these kind

Facebook but um uh uh is is these kind Facebook but um uh uh is is these kind of is these kind of these kind of of is these kind of these kind of of is these kind of these kind of network effects. The way you get network effects. The way you get

network effects. The way you get industries in which there are small industries in which there are small number of players are very high costs of number of players are very high costs of number of players are very high costs of entry, right? Um so you know uh cloud is entry, right? Um so you know uh cloud is

entry, right? Um so you know uh cloud is like this. I think cloud is a good like this. I think cloud is a good like this. I think cloud is a good example of this. You have three maybe example of this. You have three maybe example of this. You have three maybe four players within cloud. I think I

four players within cloud. I think I four players within cloud. I think I think that's the same for AI. Three think that's the same for AI. Three think that's the same for AI. Three maybe four. Um uh and the reason is that maybe four. Um uh and the reason is that

maybe four. Um uh and the reason is that it's it's so expensive. It requires so it's it's so expensive. It requires so it's it's so expensive. It requires so much expertise and so much capital to much expertise and so much capital to much expertise and so much capital to like run a cloud company, right? And so

like run a cloud company, right? And so like run a cloud company, right? And so you have to put up all this capital. And you have to put up all this capital. And you have to put up all this capital. And then in addition to putting up all this then in addition to putting up all this

then in addition to putting up all this capital, you have to get all of this capital, you have to get all of this capital, you have to get all of this other stuff that like, you know, other stuff that like, you know, other stuff that like, you know, requires a lot of skill to, you know, to

requires a lot of skill to, you know, to requires a lot of skill to, you know, to make it happen. And so it's like if you make it happen. And so it's like if you make it happen. And so it's like if you go to someone and you're like, I want to go to someone and you're like, I want to

go to someone and you're like, I want to disrupt this industry. Here's hundred disrupt this industry. Here's hundred disrupt this industry. Here's hundred billion dollars. You're like, okay, I'm billion dollars. You're like, okay, I'm billion dollars. You're like, okay, I'm putting $100 billion and also betting

putting $100 billion and also betting putting $100 billion and also betting that you can do all these other things that you can do all these other things that you can do all these other things that these people have been doing that these people have been doing

that these people have been doing &gt;&gt; decrease the profit in the industry. &gt;&gt; decrease the profit in the industry. &gt;&gt; decrease the profit in the industry. &gt;&gt; Yeah. And and and then and then the &gt;&gt; Yeah. And and and then and then the &gt;&gt; Yeah. And and and then and then the effect of your entering is the profit

effect of your entering is the profit effect of your entering is the profit margins go down. And so you know we have margins go down. And so you know we have margins go down. And so you know we have equilibria like this all the time in the equilibria like this all the time in the

equilibria like this all the time in the economy where we have a few we have a economy where we have a few we have a economy where we have a few we have a few players profits are not astronomical few players profits are not astronomical few players profits are not astronomical margins are not astronomical but they're

margins are not astronomical but they're margins are not astronomical but they're they're not zero right um uh and and you they're not zero right um uh and and you they're not zero right um uh and and you know I think I think that's what we see know I think I think that's what we see

know I think I think that's what we see on cloud cloud is very undifferentiated on cloud cloud is very undifferentiated on cloud cloud is very undifferentiated models are more differentiated than models are more differentiated than models are more differentiated than cloud right like everyone knows claude

cloud right like everyone knows claude cloud right like everyone knows claude is claude claude is good at different is claude claude is good at different is claude claude is good at different things than GPT is good at is than than things than GPT is good at is than than

things than GPT is good at is than than Gemini is good at and it's not just Gemini is good at and it's not just Gemini is good at and it's not just claude's good at coding GP PT is good at claude's good at coding GP PT is good at claude's good at coding GP PT is good at you know math and reasoning you know um

you know math and reasoning you know um you know math and reasoning you know um uh it's more subtle than that like uh it's more subtle than that like uh it's more subtle than that like models are good at different types of models are good at different types of

models are good at different types of coding models have different styles like coding models have different styles like coding models have different styles like I think I think these things are I think I think these things are I think I think these things are actually you know quite different from

actually you know quite different from actually you know quite different from each other and so I would expect more each other and so I would expect more each other and so I would expect more differentiation than you see in in um differentiation than you see in in um

[75:19]

differentiation than you see in in um cloud now there there actually is a uh cloud now there there actually is a uh cloud now there there actually is a uh counter there there there is one counter there there there is one counter there there there is one counterargument um and that

counterargument um and that counterargument um and that counterargument is that if all of that counterargument is that if all of that counterargument is that if all of that the process of producing models the process of producing models

the process of producing models um becomes uh if AI models can do that um becomes uh if AI models can do that um becomes uh if AI models can do that themselves, then that could spread themselves, then that could spread themselves, then that could spread throughout the economy. But that is not

throughout the economy. But that is not throughout the economy. But that is not an argument for commoditizing AI models an argument for commoditizing AI models an argument for commoditizing AI models in general. That's kind of an argument in general. That's kind of an argument

in general. That's kind of an argument for commoditizing the whole economy at for commoditizing the whole economy at for commoditizing the whole economy at once. Um I don't know what what quite once. Um I don't know what what quite once. Um I don't know what what quite happens in that world where basically

happens in that world where basically happens in that world where basically anyone can do anything, anyone can build anyone can do anything, anyone can build anyone can do anything, anyone can build anything, and there's like no mode anything, and there's like no mode

anything, and there's like no mode around anything at all. I mean, I don't around anything at all. I mean, I don't around anything at all. I mean, I don't know, maybe we want that world like like know, maybe we want that world like like know, maybe we want that world like like maybe that's the maybe that's the end

maybe that's the maybe that's the end maybe that's the maybe that's the end state here. like maybe maybe um you know state here. like maybe maybe um you know state here. like maybe maybe um you know when maybe when when when kind of AI when maybe when when when kind of AI

when maybe when when when kind of AI models can do you know when when when models can do you know when when when models can do you know when when when when AI models can do everything if when AI models can do everything if when AI models can do everything if we've solved all the safety and security

we've solved all the safety and security we've solved all the safety and security problems like you know that's one of the problems like you know that's one of the problems like you know that's one of the one of the one of the mechanisms for for one of the one of the mechanisms for for

one of the one of the mechanisms for for uh you know um uh uh you know just just uh you know um uh uh you know just just uh you know um uh uh you know just just kind of the economy flattening itself kind of the economy flattening itself kind of the economy flattening itself again but but that's kind of like post

again but but that's kind of like post again but but that's kind of like post like far post country of geniuses in a like far post country of geniuses in a like far post country of geniuses in a data center. Um maybe a finer way to put data center. Um maybe a finer way to put

data center. Um maybe a finer way to put that uh potential point is one um it that uh potential point is one um it that uh potential point is one um it seems like AI research is especially seems like AI research is especially seems like AI research is especially loaded on raw intellectual power which

loaded on raw intellectual power which loaded on raw intellectual power which will be especially abundant in a world will be especially abundant in a world will be especially abundant in a world with AGI and two if you just look at the with AGI and two if you just look at the

with AGI and two if you just look at the world today there's very few world today there's very few world today there's very few technologies that seem to be diffusing technologies that seem to be diffusing technologies that seem to be diffusing as fast as um as AI algorithmic progress

as fast as um as AI algorithmic progress as fast as um as AI algorithmic progress and so that does hint that this industry and so that does hint that this industry and so that does hint that this industry is sort of structurally diffusive is sort of structurally diffusive

is sort of structurally diffusive So I think coding is going fast but I So I think coding is going fast but I So I think coding is going fast but I think AI research is a supererset of think AI research is a supererset of think AI research is a supererset of coding and there are aspects of it that

coding and there are aspects of it that coding and there are aspects of it that are not going fast. Um uh but I but I do are not going fast. Um uh but I but I do are not going fast. Um uh but I but I do think again once we get coding once we think again once we get coding once we

think again once we get coding once we get AI models going fast then you know get AI models going fast then you know get AI models going fast then you know AI you know that will speed up the AI you know that will speed up the AI you know that will speed up the ability of AI models to kind to kind of

ability of AI models to kind to kind of ability of AI models to kind to kind of do everything else. So I think while do everything else. So I think while do everything else. So I think while coding is going fast now I think once coding is going fast now I think once

coding is going fast now I think once the AI models are building the next AI the AI models are building the next AI the AI models are building the next AI models and building everything else the models and building everything else the models and building everything else the kind of whole the whole economy will

[77:19]

kind of whole the whole economy will kind of whole the whole economy will kind of go at the same pace. I am I am kind of go at the same pace. I am I am kind of go at the same pace. I am I am worried geographically though. I'm a worried geographically though. I'm a

worried geographically though. I'm a little worried that like just proximity little worried that like just proximity little worried that like just proximity to AI having heard about AI um uh that to AI having heard about AI um uh that to AI having heard about AI um uh that that that may be one differentiator. And

that that may be one differentiator. And that that may be one differentiator. And so when I said the like you know 10 or so when I said the like you know 10 or so when I said the like you know 10 or 20% growth rate a worry I have is that 20% growth rate a worry I have is that

20% growth rate a worry I have is that the growth rate could be like 50% in the growth rate could be like 50% in the growth rate could be like 50% in Silicon Valley and you know parts of the Silicon Valley and you know parts of the Silicon Valley and you know parts of the world that are kind of socially

world that are kind of socially world that are kind of socially connected to Silicon Valley and you know connected to Silicon Valley and you know connected to Silicon Valley and you know not that much faster than its current not that much faster than its current

not that much faster than its current pace elsewhere and I think that'd be a pace elsewhere and I think that'd be a pace elsewhere and I think that'd be a pretty messed up world. So I one of the pretty messed up world. So I one of the pretty messed up world. So I one of the things I think about a lot is how to

things I think about a lot is how to things I think about a lot is how to prevent that. prevent that.

prevent that. &gt;&gt; Yeah. Do you think that once we have uh &gt;&gt; Yeah. Do you think that once we have uh &gt;&gt; Yeah. Do you think that once we have uh this country of geniuses in a data this country of geniuses in a data this country of geniuses in a data center that robotics is sort of quickly

center that robotics is sort of quickly center that robotics is sort of quickly solved afterwards because it seems like solved afterwards because it seems like solved afterwards because it seems like a big problem with robotics is that um a a big problem with robotics is that um a

a big problem with robotics is that um a human can learn how to teleoperate human can learn how to teleoperate human can learn how to teleoperate current hardware but current AI models current hardware but current AI models current hardware but current AI models can't at least not not in a way that's

can't at least not not in a way that's can't at least not not in a way that's super productive and so if we have this super productive and so if we have this super productive and so if we have this ability to learn like a human should it ability to learn like a human should it

ability to learn like a human should it solve robotics immediately as well solve robotics immediately as well solve robotics immediately as well &gt;&gt; I don't think it's dependent on learning &gt;&gt; I don't think it's dependent on learning &gt;&gt; I don't think it's dependent on learning like a human it could happen in

like a human it could happen in like a human it could happen in different ways again we could have different ways again we could have different ways again we could have trained the model on many different trained the model on many different

trained the model on many different video games which like robotic controls video games which like robotic controls video games which like robotic controls or many different simulated robotics or many different simulated robotics or many different simulated robotics environments or just you know train them

environments or just you know train them environments or just you know train them to control computer screens and they to control computer screens and they to control computer screens and they learn to generalize. So it will happen.

learn to generalize. So it will happen. learn to generalize. So it will happen. It's not necessarily dependent on It's not necessarily dependent on It's not necessarily dependent on humanlike learning. Humanlike learning humanlike learning. Humanlike learning

humanlike learning. Humanlike learning is one way it could happen. If the is one way it could happen. If the is one way it could happen. If the model's like, "Oh, I pick up a robot. I model's like, "Oh, I pick up a robot. I model's like, "Oh, I pick up a robot. I don't know how to use it. I learn that.

don't know how to use it. I learn that. don't know how to use it. I learn that. That could happen because we discovered That could happen because we discovered That could happen because we discovered discovering continual learning." That discovering continual learning." That

discovering continual learning." That could also happen because we train the could also happen because we train the could also happen because we train the model on a bunch of environments and model on a bunch of environments and model on a bunch of environments and then it generalized. Or it could happen

then it generalized. Or it could happen then it generalized. Or it could happen because the model learns that in the because the model learns that in the because the model learns that in the context length. It it doesn't actually context length. It it doesn't actually

context length. It it doesn't actually matter which way. If we go back to the matter which way. If we go back to the matter which way. If we go back to the discussion we had like like an hour ago, discussion we had like like an hour ago, discussion we had like like an hour ago, that type of thing can happen in that

that type of thing can happen in that that type of thing can happen in that type of thing can happen in several type of thing can happen in several type of thing can happen in several different ways. Um uh uh but but I do different ways. Um uh uh but but I do

different ways. Um uh uh but but I do think when for for whatever reason the think when for for whatever reason the think when for for whatever reason the models have those skills then uh models have those skills then uh models have those skills then uh robotics will be revolutionized both the

robotics will be revolutionized both the robotics will be revolutionized both the design of robots because the models will design of robots because the models will design of robots because the models will be much better than humans at that um be much better than humans at that um

[79:22]

be much better than humans at that um and also the the ability to kind of and also the the ability to kind of and also the the ability to kind of control robots. So we'll get better at control robots. So we'll get better at control robots. So we'll get better at the physical building the physical

the physical building the physical the physical building the physical hardware building the physical robots hardware building the physical robots hardware building the physical robots and we'll also get better at controlling and we'll also get better at controlling

and we'll also get better at controlling it. Now you know does that mean the it. Now you know does that mean the it. Now you know does that mean the robotics industry will also be robotics industry will also be robotics industry will also be generating trillions of dollars of

generating trillions of dollars of generating trillions of dollars of revenue? My answer there is yes but revenue? My answer there is yes but revenue? My answer there is yes but there will be the same extremely fast there will be the same extremely fast

there will be the same extremely fast but not infinitely fast diffusion. So but not infinitely fast diffusion. So will robotics be be revolutionized? will robotics be be revolutionized?

will robotics be be revolutionized? Yeah, maybe tack on another year or two. Yeah, maybe tack on another year or two. Yeah, maybe tack on another year or two. &gt;&gt; That's that's my that's the way I think &gt;&gt; That's that's my that's the way I think &gt;&gt; That's that's my that's the way I think about these things.

about these things. about these things. Uh there's a general skepticism about Uh there's a general skepticism about Uh there's a general skepticism about extremely fast progress. Like here extremely fast progress. Like here

extremely fast progress. Like here here's my view which is like it sounds here's my view which is like it sounds here's my view which is like it sounds like you are going to solve continual like you are going to solve continual like you are going to solve continual learning one way or another within a

learning one way or another within a learning one way or another within a matter of years. But just as people matter of years. But just as people matter of years. But just as people weren't talking about continual learning weren't talking about continual learning

weren't talking about continual learning a couple years ago and then we realized a couple years ago and then we realized a couple years ago and then we realized oh why aren't these models as useful as oh why aren't these models as useful as oh why aren't these models as useful as they could be right now even though they

they could be right now even though they they could be right now even though they are clearly passing the touring test and are clearly passing the touring test and are clearly passing the touring test and are experts in so many different are experts in so many different

are experts in so many different domains. Maybe it's this thing. And then domains. Maybe it's this thing. And then domains. Maybe it's this thing. And then we solve this thing and we realize we solve this thing and we realize we solve this thing and we realize actually there's another

actually there's another actually there's another um another thing that human intelligence um another thing that human intelligence um another thing that human intelligence can do. that's a basis of human labor can do. that's a basis of human labor

can do. that's a basis of human labor that these models can't do. And then so that these models can't do. And then so that these models can't do. And then so why not think there will be more things why not think there will be more things why not think there will be more things like this? Why I think that like we're

like this? Why I think that like we're like this? Why I think that like we're we're you know we've like found the we're you know we've like found the we're you know we've like found the pieces of human intelligence.

pieces of human intelligence. pieces of human intelligence. &gt;&gt; Well well to be clear I mean I think &gt;&gt; Well well to be clear I mean I think &gt;&gt; Well well to be clear I mean I think continual learning as I've said before continual learning as I've said before

continual learning as I've said before might not be a barrier at all right like might not be a barrier at all right like might not be a barrier at all right like like you know I think I think we maybe like you know I think I think we maybe like you know I think I think we maybe just get there by pre-training

just get there by pre-training just get there by pre-training generalization and and and and and and generalization and and and and and and generalization and and and and and and RL generalization. Like I I think there RL generalization. Like I I think there

RL generalization. Like I I think there just might not be um there basically just might not be um there basically just might not be um there basically might not be such a thing at all. In might not be such a thing at all. In might not be such a thing at all. In fact, I would point to the history in in

fact, I would point to the history in in fact, I would point to the history in in ML of people coming up with things that ML of people coming up with things that ML of people coming up with things that are barriers that end up kind of are barriers that end up kind of

are barriers that end up kind of dissolving within the big blob of dissolving within the big blob of dissolving within the big blob of compute, right? That, you know, people compute, right? That, you know, people compute, right? That, you know, people talked about, you know,

talked about, you know, talked about, you know, you know, how do you have, you know, how you know, how do you have, you know, how you know, how do you have, you know, how do how do your models keep track of do how do your models keep track of

do how do your models keep track of nouns and verbs and, you know, how do nouns and verbs and, you know, how do nouns and verbs and, you know, how do they, you know, they can understand they, you know, they can understand they, you know, they can understand semant syntactically, but they can't

semant syntactically, but they can't semant syntactically, but they can't understand semantically. You know, it's understand semantically. You know, it's understand semantically. You know, it's only statistical correlations. You can only statistical correlations. You can

only statistical correlations. You can understand a paragraph, but you can't understand a paragraph, but you can't understand a paragraph, but you can't understand a word. There's reasoning, understand a word. There's reasoning, understand a word. There's reasoning, you can't do reasoning, but then

you can't do reasoning, but then you can't do reasoning, but then suddenly it turns out you can do code suddenly it turns out you can do code suddenly it turns out you can do code and math very well at all. So and math very well at all. So

[81:25]

and math very well at all. So &gt;&gt; I I think there actually there's there's &gt;&gt; I I think there actually there's there's &gt;&gt; I I think there actually there's there's actually a stronger history of some of actually a stronger history of some of actually a stronger history of some of these things seeming like a big deal and

these things seeming like a big deal and these things seeming like a big deal and then and then kind of and then kind of then and then kind of and then kind of then and then kind of and then kind of dissolving. Some of them are real. I dissolving. Some of them are real. I

dissolving. Some of them are real. I mean the need for data is real. May mean the need for data is real. May mean the need for data is real. May maybe continual maybe continual maybe continual continual learn continual learning is a

continual learn continual learning is a continual learn continual learning is a real thing. But again, I would ground us real thing. But again, I would ground us real thing. But again, I would ground us in something like code. Like I think we in something like code. Like I think we

in something like code. Like I think we may get to the point in like a year or may get to the point in like a year or may get to the point in like a year or two where the models can just do end to two where the models can just do end to two where the models can just do end to end. Like that's a whole task. That's a

end. Like that's a whole task. That's a end. Like that's a whole task. That's a whole sphere of human activity that that whole sphere of human activity that that whole sphere of human activity that that we're just saying models can do it now.

we're just saying models can do it now. we're just saying models can do it now. Um when you say end to end, do you mean Um when you say end to end, do you mean Um when you say end to end, do you mean um setting technical direction, um setting technical direction,

um setting technical direction, understanding the context of the understanding the context of the understanding the context of the problem, etc.? Okay. Yes. I mean all of problem, etc.? Okay. Yes. I mean all of problem, etc.? Okay. Yes. I mean all of that. Interesting. I mean that that is I

that. Interesting. I mean that that is I that. Interesting. I mean that that is I feel like AGI complete um which maybe is feel like AGI complete um which maybe is feel like AGI complete um which maybe is internally consistent but um it's not internally consistent but um it's not

internally consistent but um it's not like saying 90% of code or 100% of code like saying 90% of code or 100% of code like saying 90% of code or 100% of code it's like no no the other parts of the it's like no no the other parts of the it's like no no the other parts of the &gt;&gt; no no I gave this I gave the spectrum

&gt;&gt; no no I gave this I gave the spectrum &gt;&gt; no no I gave this I gave the spectrum 90% of code 100% of code 90% of N10 90% of code 100% of code 90% of N10 90% of code 100% of code 90% of N10 suite 100% of N10 suite new tasks are suite 100% of N10 suite new tasks are

suite 100% of N10 suite new tasks are created for SWES eventually those get created for SWES eventually those get created for SWES eventually those get done as well but it's a long spectrum done as well but it's a long spectrum done as well but it's a long spectrum there but we're traversing the spectrum

there but we're traversing the spectrum there but we're traversing the spectrum very quickly very quickly very quickly &gt;&gt; um I do think it's funny that I I've &gt;&gt; um I do think it's funny that I I've

&gt;&gt; um I do think it's funny that I I've seen a couple podcasts you've done where seen a couple podcasts you've done where seen a couple podcasts you've done where um the host will be like a butcher wrote um the host will be like a butcher wrote um the host will be like a butcher wrote the essay about the control learning

the essay about the control learning the essay about the control learning thing and it always makes me crack up thing and it always makes me crack up thing and it always makes me crack up because you're like you know you've been because you're like you know you've been

because you're like you know you've been an AI researcher for like 10 years and an AI researcher for like 10 years and an AI researcher for like 10 years and I'm sure there's like some uh feeling of I'm sure there's like some uh feeling of I'm sure there's like some uh feeling of like okay so podcaster wrote an essay

like okay so podcaster wrote an essay like okay so podcaster wrote an essay like every interview I get asked about like every interview I get asked about like every interview I get asked about it it

it &gt;&gt; you know the the truth of the truth of &gt;&gt; you know the the truth of the truth of &gt;&gt; you know the the truth of the truth of the matter is that we're all trying to the matter is that we're all trying to the matter is that we're all trying to figure this out together right there

figure this out together right there figure this out together right there there are some ways in which I'm able to there are some ways in which I'm able to there are some ways in which I'm able to see things that others aren't these days see things that others aren't these days

see things that others aren't these days That probably has more to do with like I That probably has more to do with like I That probably has more to do with like I can see a bunch of stuff within can see a bunch of stuff within can see a bunch of stuff within Enthropic and have to make a bunch of

Enthropic and have to make a bunch of Enthropic and have to make a bunch of decisions than I have any great research decisions than I have any great research decisions than I have any great research insight that that that others don't.

insight that that that others don't. insight that that that others don't. Right? I you know I'm running a 2500 Right? I you know I'm running a 2500 Right? I you know I'm running a 2500 person company. Like it's it's actually person company. Like it's it's actually

person company. Like it's it's actually pretty hard for me to have have concrete pretty hard for me to have have concrete pretty hard for me to have have concrete research insight you know much harder research insight you know much harder research insight you know much harder than you know than than it would have

[83:27]

than you know than than it would have than you know than than it would have been you know 10 years ago or or you been you know 10 years ago or or you been you know 10 years ago or or you know or even two or three years ago. Um, know or even two or three years ago. Um,

know or even two or three years ago. Um, as we go towards a world of a full drop as we go towards a world of a full drop as we go towards a world of a full drop in remote worker replacement, does a API in remote worker replacement, does a API in remote worker replacement, does a API pricing model still make the most sense?

pricing model still make the most sense? pricing model still make the most sense? And if not, what is the correct way to And if not, what is the correct way to And if not, what is the correct way to price AGI or serve AGI?

price AGI or serve AGI? price AGI or serve AGI? &gt;&gt; Yeah, I mean, I think there's going to &gt;&gt; Yeah, I mean, I think there's going to &gt;&gt; Yeah, I mean, I think there's going to be a bunch of different business models be a bunch of different business models

be a bunch of different business models here sort of all at once that are going here sort of all at once that are going here sort of all at once that are going to be that are going to be experimented to be that are going to be experimented to be that are going to be experimented with. Um, I I I actually do think that

with. Um, I I I actually do think that with. Um, I I I actually do think that the the API the the API the the API um um model is is more durable than many

model is is more durable than many model is is more durable than many people think. Um, one way I think about people think. Um, one way I think about people think. Um, one way I think about it is if the technology is kind of it is if the technology is kind of

it is if the technology is kind of advancing quickly, if it's advancing advancing quickly, if it's advancing advancing quickly, if it's advancing exponentially, what that means is exponentially, what that means is exponentially, what that means is there's there's always kind of like a

there's there's always kind of like a there's there's always kind of like a surface area of of kind of new use cases surface area of of kind of new use cases surface area of of kind of new use cases that have been developed in in the last that have been developed in in the last

that have been developed in in the last uh in the last three months. And any uh in the last three months. And any uh in the last three months. And any kind of product surface you put in place kind of product surface you put in place kind of product surface you put in place is always at risk of sort of becoming

is always at risk of sort of becoming is always at risk of sort of becoming irrelevant, right? Any given product irrelevant, right? Any given product irrelevant, right? Any given product surface probably makes sense for, you surface probably makes sense for, you

surface probably makes sense for, you know, a range of capabilities of the know, a range of capabilities of the know, a range of capabilities of the model, right? The the chatbot is already model, right? The the chatbot is already model, right? The the chatbot is already running into limitations of, you know,

running into limitations of, you know, running into limitations of, you know, making it smarter doesn't really help making it smarter doesn't really help making it smarter doesn't really help the average consumer that much. But I the average consumer that much. But I

the average consumer that much. But I don't think that's a limitation of AI don't think that's a limitation of AI don't think that's a limitation of AI models. I don't think that's evidence models. I don't think that's evidence models. I don't think that's evidence that, you know, the models are are the

that, you know, the models are are the that, you know, the models are are the models are good enough and they're models are good enough and they're models are good enough and they're they're, you know, them getting better they're, you know, them getting better

they're, you know, them getting better doesn't matter to the economy. It doesn't matter to the economy. It doesn't matter to the economy. It doesn't matter to that particular doesn't matter to that particular doesn't matter to that particular product. Um, and and so I think the

product. Um, and and so I think the product. Um, and and so I think the value of the API is the API always value of the API is the API always value of the API is the API always offers an opportunity, you know, very offers an opportunity, you know, very

offers an opportunity, you know, very close to the bare metal to build on what close to the bare metal to build on what close to the bare metal to build on what the latest thing is. Um, and so there, the latest thing is. Um, and so there, the latest thing is. Um, and so there, you know, there's there's there's kind

you know, there's there's there's kind you know, there's there's there's kind of always going to be this, you know, of always going to be this, you know, of always going to be this, you know, this this kind of front of new startups this this kind of front of new startups

this this kind of front of new startups and new ideas that weren't possible a and new ideas that weren't possible a and new ideas that weren't possible a few months ago and are possible because few months ago and are possible because few months ago and are possible because the model is advancing. And and so I I

the model is advancing. And and so I I the model is advancing. And and so I I actually I I I kind of actually predict actually I I I kind of actually predict actually I I I kind of actually predict that we are it's going to exist that we are it's going to exist

that we are it's going to exist alongside other models, but we're always alongside other models, but we're always alongside other models, but we're always going to have the API business model going to have the API business model going to have the API business model because there's there's always going to

[85:32]

because there's there's always going to because there's there's always going to be a need for a thousand different be a need for a thousand different be a need for a thousand different people to try experimenting with the people to try experimenting with the

people to try experimenting with the model in different way and a hundred of model in different way and a hundred of model in different way and a hundred of them become startups and 10 of them them become startups and 10 of them them become startups and 10 of them become big successful startups and you

become big successful startups and you become big successful startups and you know two or three really end up being know two or three really end up being know two or three really end up being the the way that people use the model of the the way that people use the model of

the the way that people use the model of a of a given generation. So I I a of a given generation. So I I a of a given generation. So I I basically think it's always going to basically think it's always going to basically think it's always going to exist. At the same time, I'm sure

exist. At the same time, I'm sure exist. At the same time, I'm sure there's going to be other models as there's going to be other models as there's going to be other models as well. Like not every token that's output well. Like not every token that's output

well. Like not every token that's output by the model is worth the same amount. by the model is worth the same amount. by the model is worth the same amount. Think about, you know, how how what is Think about, you know, how how what is Think about, you know, how how what is the value of the tokens that are like,

the value of the tokens that are like, the value of the tokens that are like, you know, that the model outputs when you know, that the model outputs when you know, that the model outputs when someone, you know, call, you know, someone, you know, call, you know,

someone, you know, call, you know, someone, you know, calls them up and someone, you know, calls them up and someone, you know, calls them up and says, "My Mac isn't working or says, "My Mac isn't working or says, "My Mac isn't working or something." You know, the model's like,

something." You know, the model's like, something." You know, the model's like, "Restart it, right?" Yeah. "Restart it, right?" Yeah.

"Restart it, right?" Yeah. &gt;&gt; And like you know someone hasn't heard &gt;&gt; And like you know someone hasn't heard &gt;&gt; And like you know someone hasn't heard that before but like you know the model that before but like you know the model that before but like you know the model said that like 10 million times you know

said that like 10 million times you know said that like 10 million times you know that maybe that's worth like a dollar or that maybe that's worth like a dollar or that maybe that's worth like a dollar or a few cents or something. Um whereas if a few cents or something. Um whereas if

a few cents or something. Um whereas if uh the model you know the model goes to uh the model you know the model goes to uh the model you know the model goes to you know one of the one of the you know one of the one of the you know one of the one of the pharmaceutical companies and it says oh

pharmaceutical companies and it says oh pharmaceutical companies and it says oh you know this molecule you're developing you know this molecule you're developing you know this molecule you're developing you should take the aromatic ring from you should take the aromatic ring from

you should take the aromatic ring from that end of the molecule and put it on that end of the molecule and put it on that end of the molecule and put it on that end of the molecule. Um and and you that end of the molecule. Um and and you that end of the molecule. Um and and you know if you do that wonderful things

know if you do that wonderful things know if you do that wonderful things will happen. um uh like like those will happen. um uh like like those will happen. um uh like like those tokens could be worth, you know, tens of tokens could be worth, you know, tens of

tokens could be worth, you know, tens of millions of dollars, right? Um uh so so millions of dollars, right? Um uh so so millions of dollars, right? Um uh so so I think we're definitely going to see I think we're definitely going to see I think we're definitely going to see business models that that recognize

business models that that recognize business models that that recognize that, you know, at some point we're that, you know, at some point we're that, you know, at some point we're going to see, you know, pay for results going to see, you know, pay for results

going to see, you know, pay for results or you know, in some in some form or we or you know, in some in some form or we or you know, in some in some form or we may see forms of compensation that are may see forms of compensation that are may see forms of compensation that are like labor um uh you know, that that

like labor um uh you know, that that like labor um uh you know, that that kind of work by the hour. Um I I I you kind of work by the hour. Um I I I you kind of work by the hour. Um I I I you know, I don't Oh, I think I think I know, I don't Oh, I think I think I

know, I don't Oh, I think I think I think because it's a new industry, a lot think because it's a new industry, a lot think because it's a new industry, a lot of things are going to be tried and I of things are going to be tried and I of things are going to be tried and I you know I don't know what will turn out

you know I don't know what will turn out you know I don't know what will turn out to be the right thing. to be the right thing.

to be the right thing. &gt;&gt; Um what I find uh I I take your point &gt;&gt; Um what I find uh I I take your point &gt;&gt; Um what I find uh I I take your point that people will have to try things to that people will have to try things to that people will have to try things to figure out what is the best way to use

figure out what is the best way to use figure out what is the best way to use this blob of intelligence. But what I this blob of intelligence. But what I this blob of intelligence. But what I find striking is clawed code. So I don't find striking is clawed code. So I don't

[87:33]

find striking is clawed code. So I don't think in the history of startups there think in the history of startups there think in the history of startups there has been a single application that has has been a single application that has has been a single application that has been as hotly competed in as coding

been as hotly competed in as coding been as hotly competed in as coding agents and um and and cloud code is a agents and um and and cloud code is a agents and um and and cloud code is a category leader here and that seems category leader here and that seems

category leader here and that seems surprising to me like it doesn't seem surprising to me like it doesn't seem surprising to me like it doesn't seem intrinsically like enthropic had to intrinsically like enthropic had to intrinsically like enthropic had to build this and I wonder if you have an

build this and I wonder if you have an build this and I wonder if you have an accounting of why it had to be enthropic accounting of why it had to be enthropic accounting of why it had to be enthropic or why how enthropic ended up building or why how enthropic ended up building

or why how enthropic ended up building an application in addition to the model an application in addition to the model an application in addition to the model underlying it. Yeah. So it actually underlying it. Yeah. So it actually underlying it. Yeah. So it actually happened in a pretty simple way which is

happened in a pretty simple way which is happened in a pretty simple way which is we had our own um you know we had our we had our own um you know we had our we had our own um you know we had our coding models which were good at coding coding models which were good at coding

coding models which were good at coding and and you know around the beginning of and and you know around the beginning of and and you know around the beginning of 2025 I said I I think the time has come 2025 I said I I think the time has come 2025 I said I I think the time has come where you can have non-trivial

where you can have non-trivial where you can have non-trivial acceleration of your own research um if acceleration of your own research um if acceleration of your own research um if you're an AI company by using these you're an AI company by using these

you're an AI company by using these models and of course you know we you models and of course you know we you models and of course you know we you need an interface you need a harness to need an interface you need a harness to need an interface you need a harness to use them and so I encourage people

use them and so I encourage people use them and so I encourage people internally you know I didn't say this is internally you know I didn't say this is internally you know I didn't say this is one thing that you know you have to use.

one thing that you know you have to use. one thing that you know you have to use. I I just said people should experiment I I just said people should experiment I I just said people should experiment with this and then you know this thing I with this and then you know this thing I

with this and then you know this thing I think it might have been originally think it might have been originally think it might have been originally called claude CLI and then the name called claude CLI and then the name called claude CLI and then the name eventually got changed to cloud code

eventually got changed to cloud code eventually got changed to cloud code internally um was the thing that kind of internally um was the thing that kind of internally um was the thing that kind of everyone was using and it was seeing everyone was using and it was seeing

everyone was using and it was seeing fast internal adoption and I looked at fast internal adoption and I looked at fast internal adoption and I looked at it and I said probably we should launch it and I said probably we should launch it and I said probably we should launch this externally right um uh you know

this externally right um uh you know this externally right um uh you know it's it's seen such fast adoption within it's it's seen such fast adoption within it's it's seen such fast adoption within anthropic like you know like you know anthropic like you know like you know

anthropic like you know like you know coding is a lot of what we do and and so coding is a lot of what we do and and so coding is a lot of what we do and and so you know we have a we have audience of you know we have a we have audience of you know we have a we have audience of many many hundreds of people that's in

many many hundreds of people that's in many many hundreds of people that's in some ways at least representative of the some ways at least representative of the some ways at least representative of the external audience. So it looks like we external audience. So it looks like we

external audience. So it looks like we already have product market fit. Let's already have product market fit. Let's already have product market fit. Let's launch this thing. Um and and then we launch this thing. Um and and then we launch this thing. Um and and then we launched it and and and I think you know

launched it and and and I think you know launched it and and and I think you know just just the fact that we ourselves are just just the fact that we ourselves are just just the fact that we ourselves are kind of developing the model and we kind of developing the model and we

kind of developing the model and we ourselves know what we most need to use ourselves know what we most need to use ourselves know what we most need to use the model. I think it's it's kind of the model. I think it's it's kind of the model. I think it's it's kind of creating this feedback loop.

creating this feedback loop. creating this feedback loop. &gt;&gt; I see. in the sense that you let's say a &gt;&gt; I see. in the sense that you let's say a &gt;&gt; I see. in the sense that you let's say a developer at Enthropic is like ah it it developer at Enthropic is like ah it it

developer at Enthropic is like ah it it would be better if it was better at this would be better if it was better at this would be better if it was better at this X thing and then you bake that into the X thing and then you bake that into the X thing and then you bake that into the next model that you build that that's

[89:35]

next model that you build that that's next model that you build that that's that's one version of it but but then that's one version of it but but then that's one version of it but but then there's just the ordinary product there's just the ordinary product

there's just the ordinary product iteration of like you know we have a iteration of like you know we have a iteration of like you know we have a bunch of we have a bunch of coders bunch of we have a bunch of coders bunch of we have a bunch of coders within anthropic like we um you know

within anthropic like we um you know within anthropic like we um you know they like use cloud code every day and they like use cloud code every day and they like use cloud code every day and so we get fast feedback that was more so we get fast feedback that was more

so we get fast feedback that was more important in the early days now of important in the early days now of important in the early days now of course there are millions of people course there are millions of people course there are millions of people using it um and so we get a bunch of

using it um and so we get a bunch of using it um and so we get a bunch of external feedback as well. But it's, you external feedback as well. But it's, you external feedback as well. But it's, you know, it's just great to be able to get, know, it's just great to be able to get,

know, it's just great to be able to get, you know, kind of kind of uh um fast you know, kind of kind of uh um fast you know, kind of kind of uh um fast fast internal feedback. You know, I fast internal feedback. You know, I fast internal feedback. You know, I think this is the reason why we launched

think this is the reason why we launched think this is the reason why we launched a coding model and, you know, didn't a coding model and, you know, didn't a coding model and, you know, didn't launch a pharmaceutical company, right?

launch a pharmaceutical company, right? launch a pharmaceutical company, right? It you know, you know, my background is It you know, you know, my background is It you know, you know, my background is in in my background's in in like in in my background's in in like

in in my background's in in like biology, but like we don't have any of biology, but like we don't have any of biology, but like we don't have any of the resources that are needed to launch the resources that are needed to launch the resources that are needed to launch a pharmaceutical company. So, there's

a pharmaceutical company. So, there's a pharmaceutical company. So, there's been a ton of hype around OpenClaw, and been a ton of hype around OpenClaw, and been a ton of hype around OpenClaw, and I wanted to check it out for myself.

I wanted to check it out for myself. I wanted to check it out for myself. I've got a day coming up this weekend I've got a day coming up this weekend I've got a day coming up this weekend and I don't have anything planned yet.

and I don't have anything planned yet. and I don't have anything planned yet. So, I gave Open Claw a Mercury debit So, I gave Open Claw a Mercury debit So, I gave Open Claw a Mercury debit card. I set a couple hundred limit and I card. I set a couple hundred limit and I

card. I set a couple hundred limit and I said, "Surprise me." Okay, so here's the said, "Surprise me." Okay, so here's the said, "Surprise me." Okay, so here's the Mac Mini it's on. And besides having Mac Mini it's on. And besides having Mac Mini it's on. And besides having access to my Mercury, it's totally

access to my Mercury, it's totally access to my Mercury, it's totally quarantined. They actually felt quite quarantined. They actually felt quite quarantined. They actually felt quite comfortable giving it access to a debit comfortable giving it access to a debit

comfortable giving it access to a debit card because Mercury makes it super easy card because Mercury makes it super easy card because Mercury makes it super easy to set up guardrails. I was able to to set up guardrails. I was able to to set up guardrails. I was able to customize permissions, cap the spend,

customize permissions, cap the spend, customize permissions, cap the spend, and restrict the category of purchases. and restrict the category of purchases.

and restrict the category of purchases. I wanted to make sure the debit card I wanted to make sure the debit card I wanted to make sure the debit card worked, so I asked OpenCloud to just worked, so I asked OpenCloud to just worked, so I asked OpenCloud to just make a test transaction and decided to

make a test transaction and decided to make a test transaction and decided to donate a couple bucks to Wikipedia. donate a couple bucks to Wikipedia.

donate a couple bucks to Wikipedia. Besides that, I have no idea what's Besides that, I have no idea what's Besides that, I have no idea what's going to happen. I will report back on going to happen. I will report back on going to happen. I will report back on the next episode about how it goes. In

the next episode about how it goes. In the next episode about how it goes. In the meantime, if you want a personal the meantime, if you want a personal the meantime, if you want a personal banking solution that can accommodate banking solution that can accommodate

banking solution that can accommodate all the different ways that people use all the different ways that people use all the different ways that people use their money, even experimental ones like their money, even experimental ones like their money, even experimental ones like this one, visit mercury.com/personal.

this one, visit mercury.com/personal. this one, visit mercury.com/personal. Mercury is a fintech company, not an Mercury is a fintech company, not an Mercury is a fintech company, not an FDIC insured bank. Banking services FDIC insured bank. Banking services

FDIC insured bank. Banking services provided through Choice Financial Group provided through Choice Financial Group provided through Choice Financial Group and column NA members FDIC. You know, and column NA members FDIC. You know, and column NA members FDIC. You know, she thinks we're getting coffee and

she thinks we're getting coffee and she thinks we're getting coffee and walking around the neighborhood. walking around the neighborhood.

walking around the neighborhood. Um let me ask you about now um making AI Um let me ask you about now um making AI Um let me ask you about now um making AI go well. Um it seems like whatever go well. Um it seems like whatever go well. Um it seems like whatever vision we have about how AI goes well

vision we have about how AI goes well vision we have about how AI goes well has to be compatible with two things. has to be compatible with two things.

has to be compatible with two things. One is the ability to build and run AIs One is the ability to build and run AIs One is the ability to build and run AIs is diffusing extremely rapidly and two is diffusing extremely rapidly and two is diffusing extremely rapidly and two is that the population of AIS the amount

[91:39]

is that the population of AIS the amount is that the population of AIS the amount we have in their intelligence will also we have in their intelligence will also we have in their intelligence will also increase very rapidly and that means increase very rapidly and that means

increase very rapidly and that means that lots of people will be able to that lots of people will be able to that lots of people will be able to build huge populations of misaligned AIs build huge populations of misaligned AIs build huge populations of misaligned AIs or uh AIs which are just like companies

or uh AIs which are just like companies or uh AIs which are just like companies which are trying to increase their uh which are trying to increase their uh which are trying to increase their uh footprint or have weird psyches like footprint or have weird psyches like

footprint or have weird psyches like Sydney Bing but now they're superhuman. Sydney Bing but now they're superhuman. Sydney Bing but now they're superhuman. What is a vision for a world in which we What is a vision for a world in which we What is a vision for a world in which we have an equilibrium that is compatible

have an equilibrium that is compatible have an equilibrium that is compatible with lots of different AI some of which with lots of different AI some of which with lots of different AI some of which are misaligned running around?

are misaligned running around? are misaligned running around? &gt;&gt; Yeah. Yeah. So I think you know in the &gt;&gt; Yeah. Yeah. So I think you know in the &gt;&gt; Yeah. Yeah. So I think you know in the adolescence of technology I was kind of adolescence of technology I was kind of

adolescence of technology I was kind of you know skeptical of like the balance you know skeptical of like the balance you know skeptical of like the balance of power but I I think I was of power but I I think I was of power but I I think I was particularly skeptical of or the thing I

particularly skeptical of or the thing I particularly skeptical of or the thing I was specifically skeptical of is you was specifically skeptical of is you was specifically skeptical of is you have like three or four of these have like three or four of these

have like three or four of these companies like kind of all building companies like kind of all building companies like kind of all building models that are kind of derive you know models that are kind of derive you know models that are kind of derive you know sort of sort of um uh uh like derived

sort of sort of um uh uh like derived sort of sort of um uh uh like derived from the like derived from the same from the like derived from the same from the like derived from the same thing and uh you know that that these thing and uh you know that that these

thing and uh you know that that these would check each or or even that kind of would check each or or even that kind of would check each or or even that kind of you know any number of them would would you know any number of them would would you know any number of them would would would would uh would would check each

would would uh would would check each would would uh would would check each other like we might live in a offense other like we might live in a offense other like we might live in a offense dominant world where you know like one dominant world where you know like one

dominant world where you know like one person or one AI model is like smart person or one AI model is like smart person or one AI model is like smart enough to do something that like causes enough to do something that like causes enough to do something that like causes damage for everything else. Um I think

damage for everything else. Um I think damage for everything else. Um I think in the I mean in the short run we have a in the I mean in the short run we have a in the I mean in the short run we have a limited number of players now. So we can limited number of players now. So we can

limited number of players now. So we can start by within the limited number of start by within the limited number of start by within the limited number of players we uh you know we kind of you players we uh you know we kind of you players we uh you know we kind of you know we we need to put in place the you

know we we need to put in place the you know we we need to put in place the you know the safeguards. We need to make know the safeguards. We need to make know the safeguards. We need to make sure everyone does the right alignment sure everyone does the right alignment

sure everyone does the right alignment work. we need to make sure everyone has work. we need to make sure everyone has work. we need to make sure everyone has bio classifiers like you know those are bio classifiers like you know those are bio classifiers like you know those are those are kind of the immediate things

those are kind of the immediate things those are kind of the immediate things we need to do. I agree that you know we need to do. I agree that you know we need to do. I agree that you know that that doesn't solve the problem in that that doesn't solve the problem in

that that doesn't solve the problem in the long run particularly if the ability the long run particularly if the ability the long run particularly if the ability of AI models to make other AI models of AI models to make other AI models of AI models to make other AI models proliferates then you know the the whole

proliferates then you know the the whole proliferates then you know the the whole thing can kind of um you know can become thing can kind of um you know can become thing can kind of um you know can become harder to solve. You know I think I harder to solve. You know I think I

harder to solve. You know I think I think in the long run we need some think in the long run we need some think in the long run we need some architecture of governance right some architecture of governance right some architecture of governance right some some architecture of governance that

some architecture of governance that some architecture of governance that preserves human freedom but but kind of preserves human freedom but but kind of preserves human freedom but but kind of also allows us to like you know govern also allows us to like you know govern

also allows us to like you know govern the the very large number of kind of um the the very large number of kind of um the the very large number of kind of um you know uh uh uh human systems AI you know uh uh uh human systems AI you know uh uh uh human systems AI systems hybrid hybrid human human um you

[93:50]

systems hybrid hybrid human human um you systems hybrid hybrid human human um you know hybrid hybrid human AI like you know hybrid hybrid human AI like you know hybrid hybrid human AI like you know companies or or like or like or know companies or or like or like or

know companies or or like or like or like economic units. So, you know, we're like economic units. So, you know, we're like economic units. So, you know, we're we're going to need to think about like, we're going to need to think about like, we're going to need to think about like, you know, how do we how do we protect

you know, how do we how do we protect you know, how do we how do we protect the world against, you know, the world against, you know, the world against, you know, bioteterrorism? How do we protect the bioteterrorism? How do we protect the

bioteterrorism? How do we protect the world against like, you know, against world against like, you know, against world against like, you know, against like against like mirror life? Like, you like against like mirror life? Like, you like against like mirror life? Like, you know, pro probably we're going to need

know, pro probably we're going to need know, pro probably we're going to need to, you know, need some kind of like AI to, you know, need some kind of like AI to, you know, need some kind of like AI monitoring system that like moni, you monitoring system that like moni, you

monitoring system that like moni, you know, kind of monitors for for all these know, kind of monitors for for all these know, kind of monitors for for all these things, but then we need to build this things, but then we need to build this things, but then we need to build this in a way that like, you know, preserves

in a way that like, you know, preserves in a way that like, you know, preserves civil liberties and like our civil liberties and like our civil liberties and like our constitutional rights. So I think just constitutional rights. So I think just

constitutional rights. So I think just just as is as is anything else like it's just as is as is anything else like it's just as is as is anything else like it's it's like a new security landscape with it's like a new security landscape with it's like a new security landscape with a new set of you know a new set of tools

a new set of you know a new set of tools a new set of you know a new set of tools and a new set of vulnerabilities. And I and a new set of vulnerabilities. And I and a new set of vulnerabilities. And I I think my worry is if we had a hundred I think my worry is if we had a hundred

I think my worry is if we had a hundred years for this to happen all very years for this to happen all very years for this to happen all very slowly, we'd get used to it, you know, slowly, we'd get used to it, you know, slowly, we'd get used to it, you know, like we've gotten used to like, you

like we've gotten used to like, you like we've gotten used to like, you know, the presence of, you know, the know, the presence of, you know, the know, the presence of, you know, the presence of explosives in society or presence of explosives in society or

presence of explosives in society or like the, you know, the presence of like the, you know, the presence of like the, you know, the presence of various um, you know, like new weapons various um, you know, like new weapons various um, you know, like new weapons or the, you know, the pre the presence

or the, you know, the pre the presence or the, you know, the pre the presence of video cameras. Um, we would get used of video cameras. Um, we would get used of video cameras. Um, we would get used to it over over over over 100 and we'd to it over over over over 100 and we'd

to it over over over over 100 and we'd develop governance mechanisms. We'd make develop governance mechanisms. We'd make develop governance mechanisms. We'd make our mistakes. My my worry is just that our mistakes. My my worry is just that our mistakes. My my worry is just that this is happening all so fast and so I

this is happening all so fast and so I this is happening all so fast and so I think maybe we need to do our thinking think maybe we need to do our thinking think maybe we need to do our thinking faster about how to make these faster about how to make these

faster about how to make these governance mechanisms work. governance mechanisms work. governance mechanisms work. &gt;&gt; Yeah, it seems like in a offense &gt;&gt; Yeah, it seems like in a offense &gt;&gt; Yeah, it seems like in a offense dominant world

dominant world dominant world over the course of the next century. So over the course of the next century. So over the course of the next century. So the idea is AI is making the progress the idea is AI is making the progress

the idea is AI is making the progress that would happen over the next century that would happen over the next century that would happen over the next century happen in some period of 5 to 10 years.

happen in some period of 5 to 10 years. happen in some period of 5 to 10 years. But we would still need the same But we would still need the same But we would still need the same mechanisms or balance of power would be mechanisms or balance of power would be

mechanisms or balance of power would be similarly intractable even if humans similarly intractable even if humans similarly intractable even if humans were the only game in town. Um, and so I were the only game in town. Um, and so I were the only game in town. Um, and so I guess we have the advice of AI. We it

guess we have the advice of AI. We it guess we have the advice of AI. We it fundamentally doesn't seem like a fundamentally doesn't seem like a fundamentally doesn't seem like a totally different ballgame here. If totally different ballgame here. If

totally different ballgame here. If checks and balances were going to work, checks and balances were going to work, checks and balances were going to work, they would work with humans as well. If they would work with humans as well. If they would work with humans as well. If they aren't going to work, they wouldn't

they aren't going to work, they wouldn't they aren't going to work, they wouldn't work with AIS as well. Um, and so maybe work with AIS as well. Um, and so maybe work with AIS as well. Um, and so maybe this just dooms human checks and this just dooms human checks and

this just dooms human checks and balances as well. But yeah, again, I balances as well. But yeah, again, I balances as well. But yeah, again, I think there's some way to I think think there's some way to I think think there's some way to I think there's some way to make this happen.

[95:55]

there's some way to make this happen. there's some way to make this happen. Like it, you know, it just it just, you Like it, you know, it just it just, you Like it, you know, it just it just, you know, the governments of the world may know, the governments of the world may

know, the governments of the world may have to work together to make it happen. have to work together to make it happen. have to work together to make it happen. like you know we may have to you may like you know we may have to you may like you know we may have to you may have to talk to AIS about kind of you

have to talk to AIS about kind of you have to talk to AIS about kind of you know building societal structures in know building societal structures in know building societal structures in such a way that like these these such a way that like these these

such a way that like these these defenses are possible. I I I don't know. defenses are possible. I I I don't know. defenses are possible. I I I don't know. I mean this is so this is you know I I mean this is so this is you know I I mean this is so this is you know I don't want to say so far ahead in time

don't want to say so far ahead in time don't want to say so far ahead in time but like so far ahead in technological but like so far ahead in technological but like so far ahead in technological ability that may happen over a short ability that may happen over a short

ability that may happen over a short period of time that it's hard for us to period of time that it's hard for us to period of time that it's hard for us to anticipated in advance. Um, speaking of anticipated in advance. Um, speaking of anticipated in advance. Um, speaking of governments getting involved, on

governments getting involved, on governments getting involved, on December 26th, the Tennessee legislature December 26th, the Tennessee legislature December 26th, the Tennessee legislature introduced a bill which uh said, quote, introduced a bill which uh said, quote,

introduced a bill which uh said, quote, um, it would be an offense for a person um, it would be an offense for a person um, it would be an offense for a person to knowingly train artificial to knowingly train artificial to knowingly train artificial intelligence to provide emotional

intelligence to provide emotional intelligence to provide emotional support, including through open-ended support, including through open-ended support, including through open-ended conversations with a user. And of conversations with a user. And of

conversations with a user. And of course, one of the things that Claude course, one of the things that Claude course, one of the things that Claude attempts to do is be uh a thoughtful um attempts to do is be uh a thoughtful um attempts to do is be uh a thoughtful um thoughtful friend, thoughtful,

thoughtful friend, thoughtful, thoughtful friend, thoughtful, knowledgeable friend. And in general, it knowledgeable friend. And in general, it knowledgeable friend. And in general, it seems like we're going to have this seems like we're going to have this

seems like we're going to have this patchwork of state laws. A lot of the patchwork of state laws. A lot of the patchwork of state laws. A lot of the benefits that normal people could benefits that normal people could benefits that normal people could experience as a result of AI are going

experience as a result of AI are going experience as a result of AI are going to be curtailed, especially when we get to be curtailed, especially when we get to be curtailed, especially when we get into the kinds of things you discussed into the kinds of things you discussed

into the kinds of things you discussed in machines of love and grace, in machines of love and grace, in machines of love and grace, biological freedom, mental health biological freedom, mental health biological freedom, mental health improvements, etc., etc. It seems easier

improvements, etc., etc. It seems easier improvements, etc., etc. It seems easier to imagine worlds in which these get to imagine worlds in which these get to imagine worlds in which these get whack-a-ole away by different laws. Um, whack-a-ole away by different laws. Um,

whack-a-ole away by different laws. Um, whereas whereas whereas bills like this don't seem to address bills like this don't seem to address bills like this don't seem to address the actual existential threats that

the actual existential threats that the actual existential threats that you're concerned about. So I'm curious you're concerned about. So I'm curious you're concerned about. So I'm curious about to understand in the context of about to understand in the context of

about to understand in the context of things like this your anthropics things like this your anthropics things like this your anthropics position against the federal moratorium position against the federal moratorium position against the federal moratorium on state AI laws.

on state AI laws. on state AI laws. &gt;&gt; Yes. So I don't know there's there's &gt;&gt; Yes. So I don't know there's there's &gt;&gt; Yes. So I don't know there's there's many different things going on at once, many different things going on at once,

many different things going on at once, right? I think I think that that I think right? I think I think that that I think right? I think I think that that I think that particular law is is dumb. Like you that particular law is is dumb. Like you that particular law is is dumb. Like you know I think it was it was clearly made

know I think it was it was clearly made know I think it was it was clearly made by legislators who just probably had by legislators who just probably had by legislators who just probably had little idea what AI models could do and little idea what AI models could do and

little idea what AI models could do and not do. They're like AI models serving not do. They're like AI models serving not do. They're like AI models serving as that just sounds scary. Like I don't as that just sounds scary. Like I don't as that just sounds scary. Like I don't want I don't want that to happen. So,

want I don't want that to happen. So, want I don't want that to happen. So, you know, we're we're we're not we're you know, we're we're we're not we're you know, we're we're we're not we're not in favor of that, right? But but but not in favor of that, right? But but but

not in favor of that, right? But but but that, you know, that that wasn't the that, you know, that that wasn't the that, you know, that that wasn't the thing that was being voted on. The thing thing that was being voted on. The thing thing that was being voted on. The thing that was being voted on is we're going

that was being voted on is we're going that was being voted on is we're going to ban all state regulation of AI for 10 to ban all state regulation of AI for 10 to ban all state regulation of AI for 10 years with no apparent plan to to do any years with no apparent plan to to do any

[98:00]

years with no apparent plan to to do any federal regulation of AI, which would federal regulation of AI, which would federal regulation of AI, which would take Congress to pass, which is a very take Congress to pass, which is a very take Congress to pass, which is a very high bar. Um so you know the idea that

high bar. Um so you know the idea that high bar. Um so you know the idea that we'd ban states from doing anything for we'd ban states from doing anything for we'd ban states from doing anything for 10 years and people said they had a plan 10 years and people said they had a plan

10 years and people said they had a plan for federal government but you know for federal government but you know for federal government but you know there was no actual there was no there was no actual there was no there was no actual there was no proposal on the table. There was no

proposal on the table. There was no proposal on the table. There was no actual attempt. Um given the serious actual attempt. Um given the serious actual attempt. Um given the serious dangers that I lay out in adolescence of dangers that I lay out in adolescence of

dangers that I lay out in adolescence of technology around things like the you technology around things like the you technology around things like the you know kind of biological weapons and know kind of biological weapons and know kind of biological weapons and bioteterrorism autonomy risk and the

bioteterrorism autonomy risk and the bioteterrorism autonomy risk and the timelines we've been talking about like timelines we've been talking about like timelines we've been talking about like 10 years is an eternity. like that's 10 years is an eternity. like that's

10 years is an eternity. like that's that's a that's a I I think that's a that's a that's a I I think that's a that's a that's a I I think that's a crazy thing to do. So if if that's the crazy thing to do. So if if that's the crazy thing to do. So if if that's the choice, if that's what you force us to

choice, if that's what you force us to choice, if that's what you force us to choose, then then we're going to we're choose, then then we're going to we're choose, then then we're going to we're going to choose not to have that going to choose not to have that

going to choose not to have that moratorum. And you know, I think the the moratorum. And you know, I think the the moratorum. And you know, I think the the the benefits of that position exceed the the benefits of that position exceed the the benefits of that position exceed the costs. But it's it's not a perfect

costs. But it's it's not a perfect costs. But it's it's not a perfect position if that's the choice. Now, I position if that's the choice. Now, I position if that's the choice. Now, I think the thing that we should do, the think the thing that we should do, the

think the thing that we should do, the thing that I would support is the thing that I would support is the thing that I would support is the federal government should step in, not federal government should step in, not federal government should step in, not saying states you can't regulate, but

saying states you can't regulate, but saying states you can't regulate, but here's what we're going to do and and here's what we're going to do and and here's what we're going to do and and states you can't differ from this, states you can't differ from this,

states you can't differ from this, right? Like I think preeemption is fine right? Like I think preeemption is fine right? Like I think preeemption is fine in the sense of saying that federal in the sense of saying that federal in the sense of saying that federal government says here's our standard.

government says here's our standard. government says here's our standard. This applies to everyone. States can't This applies to everyone. States can't This applies to everyone. States can't do something different. That would be do something different. That would be

do something different. That would be something I would support if it would be something I would support if it would be something I would support if it would be done in the right way. What um but but done in the right way. What um but but done in the right way. What um but but this idea of states you can't do

this idea of states you can't do this idea of states you can't do anything and we're not doing anything anything and we're not doing anything anything and we're not doing anything either that that struck that struck us either that that struck that struck us

either that that struck that struck us as you know very much not making sense as you know very much not making sense as you know very much not making sense and I think will not age well it's and I think will not age well it's and I think will not age well it's already starting to not age well with

already starting to not age well with already starting to not age well with with all the um backlash that that with all the um backlash that that with all the um backlash that that you've seen now in terms of in terms of you've seen now in terms of in terms of

you've seen now in terms of in terms of what we would want I mean you know the what we would want I mean you know the what we would want I mean you know the things we've talked about are are things we've talked about are are things we've talked about are are starting with transparency standards um

starting with transparency standards um starting with transparency standards um uh uh you know in order to monitor some uh uh you know in order to monitor some uh uh you know in order to monitor some of these autonomy risks and bio of these autonomy risks and bio

of these autonomy risks and bio terrorism risks as the risks become more terrorism risks as the risks become more terrorism risks as the risks become more serious um as we as we get more evidence serious um as we as we get more evidence serious um as we as we get more evidence for them then I think we could be more

for them then I think we could be more for them then I think we could be more aggressive in some targeted ways and and aggressive in some targeted ways and and aggressive in some targeted ways and and say hey AI bioteterrorism is really a say hey AI bioteterrorism is really a

[100:01]

say hey AI bioteterrorism is really a threat let's let's pass a law that kind threat let's let's pass a law that kind threat let's let's pass a law that kind of forces people to have classifiers and of forces people to have classifiers and of forces people to have classifiers and I could even imagine it it depends it

I could even imagine it it depends it I could even imagine it it depends it depends how serious a threat it ends up depends how serious a threat it ends up depends how serious a threat it ends up being we don't know for sure and we need being we don't know for sure and we need

being we don't know for sure and we need to pursue this in an intellectually to pursue this in an intellectually to pursue this in an intellectually honest way where we say ahead of time honest way where we say ahead of time honest way where we say ahead of time the risk has not emerged yet but I could

the risk has not emerged yet but I could the risk has not emerged yet but I could certainly imagine with the pace that certainly imagine with the pace that certainly imagine with the pace that things are going that you know I could things are going that you know I could

things are going that you know I could imagine a world where later this year we imagine a world where later this year we imagine a world where later this year we say hey this this AI bioteterrorism say hey this this AI bioteterrorism say hey this this AI bioteterrorism stuff is really serious we should do

stuff is really serious we should do stuff is really serious we should do something about it we should put it in a something about it we should put it in a something about it we should put it in a federal we should you know put it in a federal we should you know put it in a

federal we should you know put it in a federal standard and if the federal federal standard and if the federal federal standard and if the federal government won't act we should put it in government won't act we should put it in government won't act we should put it in a state standard I could totally see

a state standard I could totally see a state standard I could totally see that I I I'm concerned about a world that I I I'm concerned about a world that I I I'm concerned about a world where where

where if you just consider the the pace of if you just consider the the pace of if you just consider the the pace of progress you're expecting the life cycle progress you're expecting the life cycle progress you're expecting the life cycle of of legislation you the the benefits

of of legislation you the the benefits of of legislation you the the benefits are, as you say, because of diffusion are, as you say, because of diffusion are, as you say, because of diffusion lag, the benefits are slow enough that I lag, the benefits are slow enough that I

lag, the benefits are slow enough that I really do think this patchwork of on the really do think this patchwork of on the really do think this patchwork of on the current trajectory, this patchwork of current trajectory, this patchwork of current trajectory, this patchwork of state laws would prohibit. I mean,

state laws would prohibit. I mean, state laws would prohibit. I mean, having an emotional chatbot friend is having an emotional chatbot friend is having an emotional chatbot friend is something that freaks people out, then something that freaks people out, then

something that freaks people out, then just imagine the kinds of actual just imagine the kinds of actual just imagine the kinds of actual benefits from AI we want normal people benefits from AI we want normal people benefits from AI we want normal people to be able to experience from

to be able to experience from to be able to experience from improvements in health and health span improvements in health and health span improvements in health and health span and improvements in mental health and so and improvements in mental health and so

and improvements in mental health and so forth. whereas at the same time uh it forth. whereas at the same time uh it forth. whereas at the same time uh it seems like you think the dangers are seems like you think the dangers are seems like you think the dangers are already on the horizon and I just don't

already on the horizon and I just don't already on the horizon and I just don't see that much um it seems like would be see that much um it seems like would be see that much um it seems like would be especially injurious to the benefits of especially injurious to the benefits of

especially injurious to the benefits of AI uh as compared to the the dangers of AI uh as compared to the the dangers of AI uh as compared to the the dangers of AI and so that that's maybe the where AI and so that that's maybe the where AI and so that that's maybe the where the cost benefit makes less sense to me.

the cost benefit makes less sense to me. the cost benefit makes less sense to me. So, so, so there's a few things here, So, so, so there's a few things here, So, so, so there's a few things here, right? I mean, people talk about there right? I mean, people talk about there

right? I mean, people talk about there being thousands of these state laws. being thousands of these state laws. being thousands of these state laws. First of all, the vast vast majority of First of all, the vast vast majority of First of all, the vast vast majority of them do not pass. Um, and you know, the

them do not pass. Um, and you know, the them do not pass. Um, and you know, the the the the you know, the world works a the the the you know, the world works a the the the you know, the world works a certain way in theory, but like just certain way in theory, but like just

certain way in theory, but like just because a law has been passed doesn't because a law has been passed doesn't because a law has been passed doesn't mean it's really enforced, right? The mean it's really enforced, right? The mean it's really enforced, right? The people the people you know implementing

people the people you know implementing people the people you know implementing it may be like, "Oh my god, this is it may be like, "Oh my god, this is it may be like, "Oh my god, this is stupid." It would mean shutting off stupid." It would mean shutting off

stupid." It would mean shutting off like, you know, everything that's ever like, you know, everything that's ever like, you know, everything that's ever been built and everything that's ever been built and everything that's ever been built and everything that's ever been built in Tennessee. So, you know,

been built in Tennessee. So, you know, been built in Tennessee. So, you know, very often laws are interpreted in like, very often laws are interpreted in like, very often laws are interpreted in like, you know, a way that makes them that you know, a way that makes them that

you know, a way that makes them that that that makes them not as dangerous or that that makes them not as dangerous or that that makes them not as dangerous or not as harmful. On on the same side, of not as harmful. On on the same side, of not as harmful. On on the same side, of course, you have to worry if you're

[102:04]

course, you have to worry if you're course, you have to worry if you're passing a law to stop a bad thing, you passing a law to stop a bad thing, you passing a law to stop a bad thing, you had this you had this problem as well.

had this you had this problem as well. had this you had this problem as well. Yeah. Um uh look my my look I mean my Yeah. Um uh look my my look I mean my Yeah. Um uh look my my look I mean my basic view is you know if if if basic view is you know if if if

basic view is you know if if if you know we could decide you know what you know we could decide you know what you know we could decide you know what laws were passed and how things were laws were passed and how things were laws were passed and how things were done which you know we're only one small

done which you know we're only one small done which you know we're only one small input input into that you know I would input input into that you know I would input input into that you know I would deregulate a lot of the stuff around the deregulate a lot of the stuff around the

deregulate a lot of the stuff around the health benefits of AI. Um I think you health benefits of AI. Um I think you health benefits of AI. Um I think you know I I don't worry as much about the know I I don't worry as much about the know I I don't worry as much about the like the the the kind of chatbot laws. I

like the the the kind of chatbot laws. I like the the the kind of chatbot laws. I I actually worry more about the drug I actually worry more about the drug I actually worry more about the drug approval process where I think AI models approval process where I think AI models

approval process where I think AI models are going to greatly accelerate um the are going to greatly accelerate um the are going to greatly accelerate um the rate at which we discover drugs and just rate at which we discover drugs and just rate at which we discover drugs and just the the pipeline will get jammed up like

the the pipeline will get jammed up like the the pipeline will get jammed up like the pipeline will not be prepared to the pipeline will not be prepared to the pipeline will not be prepared to like process all all of the stuff that's like process all all of the stuff that's

like process all all of the stuff that's going through it. So um you know I I I going through it. So um you know I I I going through it. So um you know I I I think I think reform of the regulatory think I think reform of the regulatory think I think reform of the regulatory process to buy us more towards we have a

process to buy us more towards we have a process to buy us more towards we have a lot of things coming where the safety lot of things coming where the safety lot of things coming where the safety and the efficacy is actually going to be and the efficacy is actually going to be

and the efficacy is actually going to be really crisp and clear like I mean a really crisp and clear like I mean a really crisp and clear like I mean a beautiful thing really really crisp and beautiful thing really really crisp and beautiful thing really really crisp and clear and like really really effective

clear and like really really effective clear and like really really effective but you know and and and maybe we don't but you know and and and maybe we don't but you know and and and maybe we don't need all this all this um uh uh like um need all this all this um uh uh like um

need all this all this um uh uh like um all this superructure around it that was all this superructure around it that was all this superructure around it that was designed around an era of drugs that designed around an era of drugs that designed around an era of drugs that barely work and often and have serious

barely work and often and have serious barely work and often and have serious side effects. Um but at the same time I side effects. Um but at the same time I side effects. Um but at the same time I think we should be ramping up quite think we should be ramping up quite

think we should be ramping up quite significantly the um uh you know this significantly the um uh you know this significantly the um uh you know this this kind of safety and security this kind of safety and security this kind of safety and security legislation and you know like I've said

legislation and you know like I've said legislation and you know like I've said um you know starting with transparency um you know starting with transparency um you know starting with transparency is is my view of trying not to hamper is is my view of trying not to hamper

is is my view of trying not to hamper the industry right trying to find the the industry right trying to find the the industry right trying to find the right balance. I'm worried about it.

right balance. I'm worried about it. right balance. I'm worried about it. Some people criticize my essay for Some people criticize my essay for Some people criticize my essay for saying that's too slow. The dangers of saying that's too slow. The dangers of

saying that's too slow. The dangers of AI will come too soon if we do that. AI will come too soon if we do that. AI will come too soon if we do that. Well, basically I kind of think like the Well, basically I kind of think like the Well, basically I kind of think like the last 6 months and maybe the next few

last 6 months and maybe the next few last 6 months and maybe the next few months are going to be about months are going to be about months are going to be about transparency. And then if these ris if transparency. And then if these ris if

transparency. And then if these ris if these risks emerge when we're more these risks emerge when we're more these risks emerge when we're more certain of them, which I think we might certain of them, which I think we might certain of them, which I think we might be as soon as as later this year, then I

[104:05]

be as soon as as later this year, then I be as soon as as later this year, then I think we need to act very fast in the think we need to act very fast in the think we need to act very fast in the areas that we've actually seen the risk.

areas that we've actually seen the risk. areas that we've actually seen the risk. Like I think the only way to do this is Like I think the only way to do this is Like I think the only way to do this is to be nimble. Now the legislative to be nimble. Now the legislative

to be nimble. Now the legislative process is normally not nimble but we we process is normally not nimble but we we process is normally not nimble but we we need to emphasize to everyone involved need to emphasize to everyone involved need to emphasize to everyone involved the urgency of this. That's why I'm

the urgency of this. That's why I'm the urgency of this. That's why I'm sending this message of urgency, right? sending this message of urgency, right?

sending this message of urgency, right? That's why I wrote adolescence of That's why I wrote adolescence of That's why I wrote adolescence of technology. I wanted policy makers to technology. I wanted policy makers to technology. I wanted policy makers to read it. I wanted economists to read it.

read it. I wanted economists to read it. read it. I wanted economists to read it. I want national security professionals I want national security professionals I want national security professionals to read it. You know, I want decision to read it. You know, I want decision

to read it. You know, I want decision makers to read it so that they have some makers to read it so that they have some makers to read it so that they have some hope of acting faster than they would hope of acting faster than they would hope of acting faster than they would have otherwise. Is there anything you

have otherwise. Is there anything you have otherwise. Is there anything you can do or advocate that would can do or advocate that would can do or advocate that would make it more certain that the benefits make it more certain that the benefits

make it more certain that the benefits of AI are um are better instantiated of AI are um are better instantiated of AI are um are better instantiated where I feel like you have worked with where I feel like you have worked with where I feel like you have worked with legislators to be like okay we're going

legislators to be like okay we're going legislators to be like okay we're going to prevent biotterism here way we're to prevent biotterism here way we're to prevent biotterism here way we're going to increase we're going to going to increase we're going to

going to increase we're going to increase whistleblower protection and I increase whistleblower protection and I increase whistleblower protection and I just think by default the actual ben just think by default the actual ben just think by default the actual ben like the things we're looking forward to

like the things we're looking forward to like the things we're looking forward to here it just seems very easy they seem here it just seems very easy they seem here it just seems very easy they seem very fragile to uh different kinds of very fragile to uh different kinds of

very fragile to uh different kinds of moral panics or political economy moral panics or political economy moral panics or political economy problems.

problems. problems. &gt;&gt; Yeah, I don't actually so so I don't &gt;&gt; Yeah, I don't actually so so I don't &gt;&gt; Yeah, I don't actually so so I don't actually agree that much in the actually agree that much in the

actually agree that much in the developed world. I feel like, you know, developed world. I feel like, you know, developed world. I feel like, you know, in the developed world like markets in the developed world like markets in the developed world like markets function pretty well and when there's

function pretty well and when there's function pretty well and when there's when there's like a lot of money to be when there's like a lot of money to be when there's like a lot of money to be made on something and it's clearly the made on something and it's clearly the

made on something and it's clearly the best available alternative, it's best available alternative, it's best available alternative, it's actually hard for the regulatory system actually hard for the regulatory system actually hard for the regulatory system to stop it. You know, we're we're seeing

to stop it. You know, we're we're seeing to stop it. You know, we're we're seeing that in AI itself, right? I you know, that in AI itself, right? I you know, that in AI itself, right? I you know, like a thing I've been trying to fight like a thing I've been trying to fight

like a thing I've been trying to fight for is export controls on chips to for is export controls on chips to for is export controls on chips to China, right? And like that's in the China, right? And like that's in the China, right? And like that's in the national security interests of the US

national security interests of the US national security interests of the US like you know that's like square within like you know that's like square within like you know that's like square within the you know the the policy beliefs of the you know the the policy beliefs of

the you know the the policy beliefs of you know every almost everyone in you know every almost everyone in you know every almost everyone in Congress of both parties but and you Congress of both parties but and you Congress of both parties but and you know I think the case is very clear. The

know I think the case is very clear. The know I think the case is very clear. The counterarguments against it are I'll counterarguments against it are I'll counterarguments against it are I'll politely call them fishy. Um uh and yet politely call them fishy. Um uh and yet

politely call them fishy. Um uh and yet it doesn't happen and we sell the chips it doesn't happen and we sell the chips it doesn't happen and we sell the chips because there's there's so much money because there's there's so much money because there's there's so much money there's so much money riding on it. um

[106:06]

there's so much money riding on it. um there's so much money riding on it. um and you know the the that money wants to and you know the the that money wants to and you know the the that money wants to be made and and in that case in my be made and and in that case in my

be made and and in that case in my opinion that's a bad thing. Um and but opinion that's a bad thing. Um and but opinion that's a bad thing. Um and but but it also it also applies when when but it also it also applies when when but it also it also applies when when it's a good thing and and so I I don't

it's a good thing and and so I I don't it's a good thing and and so I I don't think that if we're talking about drugs think that if we're talking about drugs think that if we're talking about drugs and benefits of the technology I I I I and benefits of the technology I I I I

and benefits of the technology I I I I am not as worried about those benefits am not as worried about those benefits am not as worried about those benefits being hampered in the developed world. I being hampered in the developed world. I being hampered in the developed world. I am a little worried about them going too

am a little worried about them going too am a little worried about them going too slow and I as I said I do think we slow and I as I said I do think we slow and I as I said I do think we should work to speed the approval should work to speed the approval

should work to speed the approval process in the FDA. I do think we should process in the FDA. I do think we should process in the FDA. I do think we should fight against these chatbot bills that fight against these chatbot bills that fight against these chatbot bills that you're describing right described

you're describing right described you're describing right described individually. I'm against them. I think individually. I'm against them. I think individually. I'm against them. I think they're stupid. Um but I actually think they're stupid. Um but I actually think

they're stupid. Um but I actually think the bigger worry is a developing world the bigger worry is a developing world the bigger worry is a developing world um where we don't have functioning um where we don't have functioning um where we don't have functioning markets where um you know we often can't

markets where um you know we often can't markets where um you know we often can't build on the technology that that we've build on the technology that that we've build on the technology that that we've had. I worry more that those folks will had. I worry more that those folks will

had. I worry more that those folks will get left behind. And I worry that even get left behind. And I worry that even get left behind. And I worry that even if the cures are developed, you know, if the cures are developed, you know, if the cures are developed, you know, maybe there's someone in rural

maybe there's someone in rural maybe there's someone in rural Mississippi who who doesn't get it as Mississippi who who doesn't get it as Mississippi who who doesn't get it as well. Right? That's a that's a that's a well. Right? That's a that's a that's a

well. Right? That's a that's a that's a kind of smaller version of the thing the kind of smaller version of the thing the kind of smaller version of the thing the concern we have in the in the developing concern we have in the in the developing concern we have in the in the developing world. And so the things we've been

world. And so the things we've been world. And so the things we've been doing are you know you know we work with doing are you know you know we work with doing are you know you know we work with you know we work with you know you know we work with you know

you know we work with you know philanthropists right you know we work philanthropists right you know we work philanthropists right you know we work with folks um who you know who you know with folks um who you know who you know with folks um who you know who you know deliver you know medicine and health

deliver you know medicine and health deliver you know medicine and health interventions to you know to to interventions to you know to to interventions to you know to to developing world to subsaharan Africa developing world to subsaharan Africa

developing world to subsaharan Africa you know India Latin America you know you know India Latin America you know you know India Latin America you know you know other other developing parts of you know other other developing parts of you know other other developing parts of the world that's the thing I think that

the world that's the thing I think that the world that's the thing I think that won't happen on its own you mentioned won't happen on its own you mentioned won't happen on its own you mentioned export controls Yeah.

export controls Yeah. export controls Yeah. &gt;&gt; Why can't US and China both have a &gt;&gt; Why can't US and China both have a &gt;&gt; Why can't US and China both have a country of geniuses country of geniuses

country of geniuses &gt;&gt; on a data center? &gt;&gt; on a data center? &gt;&gt; on a data center? &gt;&gt; Why can't you know why won't it happen &gt;&gt; Why can't you know why won't it happen &gt;&gt; Why can't you know why won't it happen or why should

or why should or why should &gt;&gt; why shouldn't it happen? &gt;&gt; why shouldn't it happen?

&gt;&gt; why shouldn't it happen? &gt;&gt; Why shouldn't it happen? Um, you know, I &gt;&gt; Why shouldn't it happen? Um, you know, I &gt;&gt; Why shouldn't it happen? Um, you know, I think I think if this does happen, um, think I think if this does happen, um, think I think if this does happen, um, you know, then then we kind of have a

you know, then then we kind of have a you know, then then we kind of have a well, we could have a few situ if we well, we could have a few situ if we well, we could have a few situ if we have like an offense dominant situation.

have like an offense dominant situation. have like an offense dominant situation. We could have a situation like nuclear We could have a situation like nuclear We could have a situation like nuclear weapons, but like more dangerous, right?

[108:07]

weapons, but like more dangerous, right? weapons, but like more dangerous, right? Where it's like um, you know, kind of Where it's like um, you know, kind of Where it's like um, you know, kind of kind of either side could could easily kind of either side could could easily

kind of either side could could easily destroy everything. Um, we could also destroy everything. Um, we could also destroy everything. Um, we could also have a world where it's kind of it's have a world where it's kind of it's have a world where it's kind of it's unstable. Like the nuclear equilibrium

unstable. Like the nuclear equilibrium unstable. Like the nuclear equilibrium is stable, right? Because it's, you is stable, right? Because it's, you is stable, right? Because it's, you know, it's like deterrence. But let's know, it's like deterrence. But let's

know, it's like deterrence. But let's say there were uncertainty about like if say there were uncertainty about like if say there were uncertainty about like if the two AIs fought, which AI would win.

the two AIs fought, which AI would win. the two AIs fought, which AI would win. Um, that could create instability, Um, that could create instability, Um, that could create instability, right? You often have conflict when the right? You often have conflict when the

right? You often have conflict when the two sides have a different assessment of two sides have a different assessment of two sides have a different assessment of their likelihood of winning, right? If their likelihood of winning, right? If their likelihood of winning, right? If one side is like, oh yeah, there's a 90%

one side is like, oh yeah, there's a 90% one side is like, oh yeah, there's a 90% chance I'll win. And the other side's chance I'll win. And the other side's chance I'll win. And the other side's like, there's a 90% chance I'll win, like, there's a 90% chance I'll win,

like, there's a 90% chance I'll win, then then a fight is much more likely. then then a fight is much more likely. then then a fight is much more likely. Um, they can't both be right, but they Um, they can't both be right, but they Um, they can't both be right, but they can both think that. But this seems like

can both think that. But this seems like can both think that. But this seems like a fully general argument against the a fully general argument against the a fully general argument against the diffusion of AI technology which it may diffusion of AI technology which it may

diffusion of AI technology which it may which is that's the implication of this which is that's the implication of this which is that's the implication of this world.

world. world. &gt;&gt; Let me let me just go on because I think &gt;&gt; Let me let me just go on because I think &gt;&gt; Let me let me just go on because I think we will get diffusion eventually. The we will get diffusion eventually. The

we will get diffusion eventually. The other concern I have is that people the other concern I have is that people the other concern I have is that people the governments will oppress their own governments will oppress their own governments will oppress their own people with AI and and and so um you

people with AI and and and so um you people with AI and and and so um you know I'm I'm just I'm worried about some know I'm I'm just I'm worried about some know I'm I'm just I'm worried about some world where you have a country that's world where you have a country that's

world where you have a country that's already you know kind of a uh you know already you know kind of a uh you know already you know kind of a uh you know you know there's there's a government you know there's there's a government you know there's there's a government that kind of kind of already um you know

that kind of kind of already um you know that kind of kind of already um you know is is kind of kind of building a you is is kind of kind of building a you is is kind of kind of building a you know a tech high-tech authoritarian know a tech high-tech authoritarian

know a tech high-tech authoritarian state. Um and to be clear this is about state. Um and to be clear this is about state. Um and to be clear this is about the government. this is not about the the government. this is not about the the government. this is not about the people like people we need to find a way

people like people we need to find a way people like people we need to find a way for people everywhere to benefit. Um my for people everywhere to benefit. Um my for people everywhere to benefit. Um my worry here is about governments. Um so worry here is about governments. Um so

worry here is about governments. Um so yeah my you know my my worry is the yeah my you know my my worry is the yeah my you know my my worry is the world gets carved up into two pieces one world gets carved up into two pieces one world gets carved up into two pieces one of those two pieces could be

of those two pieces could be of those two pieces could be authoritarian or totalitarian in a way authoritarian or totalitarian in a way authoritarian or totalitarian in a way that's very difficult to displace. Um that's very difficult to displace. Um

that's very difficult to displace. Um now will will governments eventually get now will will governments eventually get now will will governments eventually get powerful AI and and you know there's powerful AI and and you know there's powerful AI and and you know there's risk of authoritarianism? Yes. Will

risk of authoritarianism? Yes. Will risk of authoritarianism? Yes. Will governments eventually get powerful AI governments eventually get powerful AI governments eventually get powerful AI and there's risk of um uh you know of of and there's risk of um uh you know of of

and there's risk of um uh you know of of kind of bad bad bad equilibria? Yes, I kind of bad bad bad equilibria? Yes, I kind of bad bad bad equilibria? Yes, I think both things, but the initial think both things, but the initial think both things, but the initial conditions matter, right? You know, at

conditions matter, right? You know, at conditions matter, right? You know, at at some point we're need we're going to at some point we're need we're going to at some point we're need we're going to need to set up the rules of the road.

need to set up the rules of the road. need to set up the rules of the road. I'm not saying that one country, either I'm not saying that one country, either I'm not saying that one country, either the United States or a coalition of the United States or a coalition of

the United States or a coalition of democracies, which I think is would be a democracies, which I think is would be a democracies, which I think is would be a better setup, although it requires more better setup, although it requires more better setup, although it requires more international cooperation than we

[110:11]

international cooperation than we international cooperation than we currently seem to want to make. Um, but currently seem to want to make. Um, but currently seem to want to make. Um, but you know, I don't I don't think a you know, I don't I don't think a

you know, I don't I don't think a coalition of democracies or or certainly coalition of democracies or or certainly coalition of democracies or or certainly one country should just say these are one country should just say these are one country should just say these are the rules of the road. There's going to

the rules of the road. There's going to the rules of the road. There's going to be some negotiation, right? The world is be some negotiation, right? The world is be some negotiation, right? The world is going to have to grapple with this. And going to have to grapple with this. And

going to have to grapple with this. And what I would like is that the the the what I would like is that the the the what I would like is that the the the democratic nations of the world, those democratic nations of the world, those democratic nations of the world, those with, you know, who are clo whose

with, you know, who are clo whose with, you know, who are clo whose governments have represent closer to governments have represent closer to governments have represent closer to prohuman values are are holding a prohuman values are are holding a

prohuman values are are holding a stronger hand then have have more stronger hand then have have more stronger hand then have have more leverage when the rules of the road are leverage when the rules of the road are leverage when the rules of the road are set. And and so I'm I'm very concerned

set. And and so I'm I'm very concerned set. And and so I'm I'm very concerned about that initial condition. I um I was about that initial condition. I um I was about that initial condition. I um I was relisting to an interview from three relisting to an interview from three

relisting to an interview from three years ago and one of the ways it aged years ago and one of the ways it aged years ago and one of the ways it aged poorly is that I kept asking questions poorly is that I kept asking questions poorly is that I kept asking questions assuming there's going to be some key

assuming there's going to be some key assuming there's going to be some key fulcrum moment two to three years from fulcrum moment two to three years from fulcrum moment two to three years from now when in fact being that far out it now when in fact being that far out it

now when in fact being that far out it just seems like progress continues AI just seems like progress continues AI just seems like progress continues AI improves AI is more diffused and people improves AI is more diffused and people improves AI is more diffused and people will use it for more things. It seems

will use it for more things. It seems will use it for more things. It seems like you're imagining a world in the like you're imagining a world in the like you're imagining a world in the future where the countries get together future where the countries get together

future where the countries get together and here's the rules of the road and and here's the rules of the road and and here's the rules of the road and here's the leverage we have, here's the here's the leverage we have, here's the here's the leverage we have, here's the leverage you have when it seems like on

leverage you have when it seems like on leverage you have when it seems like on current trajectory, everybody will have current trajectory, everybody will have current trajectory, everybody will have more AI. Um, some of that AI will be more AI. Um, some of that AI will be

more AI. Um, some of that AI will be used by authoritarian countries. Some of used by authoritarian countries. Some of used by authoritarian countries. Some of that within the authoritarian countries that within the authoritarian countries that within the authoritarian countries will be by private actors versus state

will be by private actors versus state will be by private actors versus state actors. It's not clear who will benefit actors. It's not clear who will benefit actors. It's not clear who will benefit more. It's always unpredictable to tell more. It's always unpredictable to tell

more. It's always unpredictable to tell tell in advance. You know, it seems like tell in advance. You know, it seems like tell in advance. You know, it seems like the internet privileged authoritarian the internet privileged authoritarian the internet privileged authoritarian countries more than you would have

countries more than you would have countries more than you would have expected. Um, and maybe the AI will be expected. Um, and maybe the AI will be expected. Um, and maybe the AI will be the opposite way around. Um so I I I the opposite way around. Um so I I I

the opposite way around. Um so I I I want to better understand what you're want to better understand what you're want to better understand what you're imagining here.

imagining here. imagining here. &gt;&gt; Yeah. Yeah. So so just to be precise &gt;&gt; Yeah. Yeah. So so just to be precise &gt;&gt; Yeah. Yeah. So so just to be precise about it, I think the exponential of the about it, I think the exponential of the

about it, I think the exponential of the underlying technology will continue as underlying technology will continue as underlying technology will continue as it has before, right? The models get it has before, right? The models get it has before, right? The models get smarter and smarter even when they get

smarter and smarter even when they get smarter and smarter even when they get to country of geniuses in a data center. to country of geniuses in a data center.

to country of geniuses in a data center. You know, I I think you can continue to You know, I I think you can continue to You know, I I think you can continue to make the model smarter. There's a make the model smarter. There's a make the model smarter. There's a question of like getting diminishing

question of like getting diminishing question of like getting diminishing returns on their value in the world, returns on their value in the world, returns on their value in the world, right? How much does it matter after right? How much does it matter after

right? How much does it matter after you've already solved human biology or you've already solved human biology or you've already solved human biology or you know you know at some point you can you know you know at some point you can you know you know at some point you can do harder math you can do more abstuse

do harder math you can do more abstuse do harder math you can do more abstuse math problems but nothing after that math problems but nothing after that math problems but nothing after that matters but putting that aside I do matters but putting that aside I do

[112:14]

matters but putting that aside I do think the the exponential will continue think the the exponential will continue think the the exponential will continue but there will be certain distinguished but there will be certain distinguished but there will be certain distinguished points on the exponential and companies

points on the exponential and companies points on the exponential and companies individuals countries will reach those individuals countries will reach those individuals countries will reach those points at different times um and and so points at different times um and and so

points at different times um and and so you know there's there's you know could you know there's there's you know could you know there's there's you know could there be some you know you know I talk there be some you know you know I talk there be some you know you know I talk about is a nuclear deterrent still in

about is a nuclear deterrent still in about is a nuclear deterrent still in adolescence of technology is a nuclear adolescence of technology is a nuclear adolescence of technology is a nuclear deterrent still stable uh in the world deterrent still stable uh in the world

deterrent still stable uh in the world of of of AI I don't know but that's of of of AI I don't know but that's of of of AI I don't know but that's that's an example of like one thing that's an example of like one thing that's an example of like one thing we've taken for granted that like the

we've taken for granted that like the we've taken for granted that like the technology could reach such a level that technology could reach such a level that technology could reach such a level that it's no longer like you know we can no it's no longer like you know we can no

it's no longer like you know we can no longer be certain of it at least um uh longer be certain of it at least um uh longer be certain of it at least um uh you know think of think of others you you know think of think of others you you know think of think of others you know there there you know there there

know there there you know there there know there there you know there there are kind of points where if you if you are kind of points where if you if you are kind of points where if you if you reach a certain point you maybe you have reach a certain point you maybe you have

reach a certain point you maybe you have offensive cyber dominance and like every offensive cyber dominance and like every offensive cyber dominance and like every every computer system is transparent to every computer system is transparent to every computer system is transparent to you after that. Um, unless the other

you after that. Um, unless the other you after that. Um, unless the other side has a has a kind of equivalent side has a has a kind of equivalent side has a has a kind of equivalent defense. So, I don't know what the defense. So, I don't know what the

defense. So, I don't know what the critical moment is or if there's a critical moment is or if there's a critical moment is or if there's a single critical moment. But I think single critical moment. But I think single critical moment. But I think there will be either a critical moment,

there will be either a critical moment, there will be either a critical moment, a small number of critical moments or a small number of critical moments or a small number of critical moments or some critical window where it's like AI some critical window where it's like AI

some critical window where it's like AI is AI confers some large advantage from is AI confers some large advantage from is AI confers some large advantage from the perspective of national security and the perspective of national security and the perspective of national security and one country or coalition has reached it

one country or coalition has reached it one country or coalition has reached it before others that that you know that before others that that you know that before others that that you know that that that you know I'm not advocating that that you know I'm not advocating

that that you know I'm not advocating that they're just like okay we're in that they're just like okay we're in that they're just like okay we're in charge now. That's not that's not how charge now. That's not that's not how charge now. That's not that's not how that's not how I think about it. you

that's not how I think about it. you that's not how I think about it. you know that there's always the the other know that there's always the the other know that there's always the the other side is catching up. There's extreme side is catching up. There's extreme

side is catching up. There's extreme actions you're not willing to take and actions you're not willing to take and actions you're not willing to take and and and it's not right to take, you and and it's not right to take, you and and it's not right to take, you know, to take complete um to take

know, to take complete um to take know, to take complete um to take complete control anyway. But but at at complete control anyway. But but at at complete control anyway. But but at at the point that that happens, I think the point that that happens, I think

the point that that happens, I think people are going to understand that the people are going to understand that the people are going to understand that the world has changed. And there there's world has changed. And there there's world has changed. And there there's going to be some negotiation, implicit

going to be some negotiation, implicit going to be some negotiation, implicit or implicit, about what what is the what or implicit, about what what is the what or implicit, about what what is the what is the post AI world order look like?

is the post AI world order look like? is the post AI world order look like? And and I think my interest is in, And and I think my interest is in, And and I think my interest is in, you know, making that ne negotiation you know, making that ne negotiation

[114:15]

you know, making that ne negotiation be one in which, you know, classical be one in which, you know, classical be one in which, you know, classical liberal democracy has, you know, has a liberal democracy has, you know, has a liberal democracy has, you know, has a strong hand. Well, I want to understand

strong hand. Well, I want to understand strong hand. Well, I want to understand what that better means because you say what that better means because you say what that better means because you say in the essay, quote, autocracy is simply in the essay, quote, autocracy is simply

in the essay, quote, autocracy is simply not a form of government that people can not a form of government that people can not a form of government that people can accept in the post powerful AI. And that accept in the post powerful AI. And that accept in the post powerful AI. And that sounds like you're saying the CCP as an

sounds like you're saying the CCP as an sounds like you're saying the CCP as an institution cannot exist after we get institution cannot exist after we get institution cannot exist after we get AGI. Um, and that seems like AGI. Um, and that seems like

AGI. Um, and that seems like a like a very strong demand and it seems a like a very strong demand and it seems a like a very strong demand and it seems to imply a world where the leading lab to imply a world where the leading lab to imply a world where the leading lab or the leading country will be able to

or the leading country will be able to or the leading country will be able to and by that language should get to and by that language should get to and by that language should get to determine how the world is governed or determine how the world is governed or

determine how the world is governed or what kinds of governments are allowed what kinds of governments are allowed what kinds of governments are allowed and not allowed.

and not allowed. and not allowed. &gt;&gt; Yeah. So when I when I um I I believe &gt;&gt; Yeah. So when I when I um I I believe &gt;&gt; Yeah. So when I when I um I I believe that paragraph was I think I said that paragraph was I think I said

that paragraph was I think I said something like you could take it even something like you could take it even something like you could take it even further and say X. So I wasn't I wasn't further and say X. So I wasn't I wasn't further and say X. So I wasn't I wasn't necessarily endorsing that that that I

necessarily endorsing that that that I necessarily endorsing that that that I wasn't necessarily endorsing that view. wasn't necessarily endorsing that view.

wasn't necessarily endorsing that view. I you know I was saying like here's if I you know I was saying like here's if I you know I was saying like here's if first you know here here's a weaker first you know here here's a weaker first you know here here's a weaker thing that I believe you know I think I

thing that I believe you know I think I thing that I believe you know I think I you know I think I said you know we have you know I think I said you know we have you know I think I said you know we have to worry a lot about authoritarians and to worry a lot about authoritarians and

to worry a lot about authoritarians and you know we should try and you know kind you know we should try and you know kind you know we should try and you know kind of kind of check them and limit their of kind of check them and limit their of kind of check them and limit their power. Like you could take this kind of

power. Like you could take this kind of power. Like you could take this kind of further much more interventionist view further much more interventionist view further much more interventionist view that says like authoritarian countries that says like authoritarian countries

that says like authoritarian countries with AI are these you know the the you with AI are these you know the the you with AI are these you know the the you know the these kind of self-fulfilling know the these kind of self-fulfilling know the these kind of self-fulfilling cycles that that you can't that are very

cycles that that you can't that are very cycles that that you can't that are very hard to displace and so you just need to hard to displace and so you just need to hard to displace and so you just need to get rid of them from from the beginning get rid of them from from the beginning

get rid of them from from the beginning that that has exactly all the problems that that has exactly all the problems that that has exactly all the problems you say which is you know you know if you say which is you know you know if you say which is you know you know if you were to make a commitment to

you were to make a commitment to you were to make a commitment to overthrowing every authoritarian country overthrowing every authoritarian country overthrowing every authoritarian country I mean they then they would take a bunch I mean they then they would take a bunch

I mean they then they would take a bunch of actions now that like you know that of actions now that like you know that of actions now that like you know that that that could could lead to that that could could lead to that that could could lead to instability so that that may or you know

instability so that that may or you know instability so that that may or you know that that just that just may not be that that just that just may not be that that just that just may not be possible. But the point I was making possible. But the point I was making

possible. But the point I was making that I do endorse is that it is it is that I do endorse is that it is it is that I do endorse is that it is it is quite possible that you know today you quite possible that you know today you quite possible that you know today you know the view or at least my view or the

know the view or at least my view or the know the view or at least my view or the view in most the western world is is view in most the western world is is view in most the western world is is democracy is a better form of government democracy is a better form of government

[116:16]

democracy is a better form of government than authoritarianism. But it's not like than authoritarianism. But it's not like than authoritarianism. But it's not like if a country is authoritarian, we don't if a country is authoritarian, we don't if a country is authoritarian, we don't react the way we reacted if they

react the way we reacted if they react the way we reacted if they committed a genocide or something, committed a genocide or something, committed a genocide or something, right? And and I'm I guess what I'm right? And and I'm I guess what I'm

right? And and I'm I guess what I'm saying is I'm a little worried that in saying is I'm a little worried that in saying is I'm a little worried that in the age of AGI, authoritarianism will the age of AGI, authoritarianism will the age of AGI, authoritarianism will have a different meaning. It will be a

have a different meaning. It will be a have a different meaning. It will be a graver thing. Um and and we have to graver thing. Um and and we have to graver thing. Um and and we have to decide one way or another how to h how decide one way or another how to h how

decide one way or another how to h how to deal with that. And the to deal with that. And the to deal with that. And the interventionist view is one possible interventionist view is one possible interventionist view is one possible view. I was exploring such views. um you

view. I was exploring such views. um you view. I was exploring such views. um you know know know it may end up being the right view. It it may end up being the right view. It

it may end up being the right view. It it may end up being too extreme to be it may end up being too extreme to be it may end up being too extreme to be the right view. But I do have hope and the right view. But I do have hope and the right view. But I do have hope and one piece of hope I have is

one piece of hope I have is one piece of hope I have is there there is we have seen that as new there there is we have seen that as new there there is we have seen that as new technologies are invented technologies are invented

technologies are invented forms of government become obsolete. I I forms of government become obsolete. I I forms of government become obsolete. I I mentioned this in adolescence of mentioned this in adolescence of mentioned this in adolescence of technology where I said you know like

technology where I said you know like technology where I said you know like feudalism was basically you know like a feudalism was basically you know like a feudalism was basically you know like a form of government right and and then form of government right and and then

form of government right and and then when when we invented industrialization when when we invented industrialization when when we invented industrialization feudalism was no longer sustainable it feudalism was no longer sustainable it feudalism was no longer sustainable it no longer made sense why is that hope

no longer made sense why is that hope no longer made sense why is that hope couldn't that imply that democracy is no couldn't that imply that democracy is no couldn't that imply that democracy is no longer going to be a competitive system longer going to be a competitive system

longer going to be a competitive system &gt;&gt; it it could right it could go it could &gt;&gt; it it could right it could go it could &gt;&gt; it it could right it could go it could go either way right but but I actually go either way right but but I actually go either way right but but I actually so I these problems with

so I these problems with so I these problems with authoritarianism, right? That the authoritarianism, right? That the authoritarianism, right? That the problems with authoritarianism get problems with authoritarianism get

problems with authoritarianism get deeper. I just I wonder if that's an deeper. I just I wonder if that's an deeper. I just I wonder if that's an indicator of other problems that indicator of other problems that indicator of other problems that authoritarianism will have, right? In

authoritarianism will have, right? In authoritarianism will have, right? In other words, people become because other words, people become because other words, people become because authoritarianism becomes worse, people authoritarianism becomes worse, people

authoritarianism becomes worse, people are more afraid of authoritarianism. are more afraid of authoritarianism. are more afraid of authoritarianism. They work harder to stop it. It's it's They work harder to stop it. It's it's They work harder to stop it. It's it's more of a like you have to think in

more of a like you have to think in more of a like you have to think in terms of total equilibrium, right? Um, I terms of total equilibrium, right? Um, I terms of total equilibrium, right? Um, I just wonder if it will motivate new ways just wonder if it will motivate new ways

just wonder if it will motivate new ways of thinking about with the with with the of thinking about with the with with the of thinking about with the with with the new technology how to preserve and new technology how to preserve and new technology how to preserve and protect freedom

protect freedom protect freedom &gt;&gt; and and even more optimistically, will &gt;&gt; and and even more optimistically, will &gt;&gt; and and even more optimistically, will it lead to a collective reckoning and, it lead to a collective reckoning and,

[118:18]

it lead to a collective reckoning and, you know, a kind of a a more emphatic you know, a kind of a a more emphatic you know, a kind of a a more emphatic realization of how important some of the realization of how important some of the realization of how important some of the things we take as individual rights are,

things we take as individual rights are, things we take as individual rights are, right? a more emphatic realization that right? a more emphatic realization that right? a more emphatic realization that we just we really can't give these away.

we just we really can't give these away. we just we really can't give these away. There's there we've seen there's no There's there we've seen there's no There's there we've seen there's no other way to live that actually works.

other way to live that actually works. other way to live that actually works. Um I I I I am actually I am actually Um I I I I am actually I am actually Um I I I I am actually I am actually hopeful that I I guess one way to say it hopeful that I I guess one way to say it

hopeful that I I guess one way to say it it sounds too idealistic but I actually it sounds too idealistic but I actually it sounds too idealistic but I actually believe it could be the case is is that believe it could be the case is is that believe it could be the case is is that is that dictatorships become morally

is that dictatorships become morally is that dictatorships become morally obsolete. They become morally unworkable obsolete. They become morally unworkable obsolete. They become morally unworkable forms of government. Um and that and forms of government. Um and that and

forms of government. Um and that and that and that the the the the crisis that and that the the the the crisis that and that the the the the crisis that that creates is is is sufficient to that that creates is is is sufficient to that that creates is is is sufficient to force us to find another way. Um I I

force us to find another way. Um I I force us to find another way. Um I I think there is genuinely a tough think there is genuinely a tough think there is genuinely a tough question here which I'm not sure how you question here which I'm not sure how you

question here which I'm not sure how you resolve for and we've had to come out resolve for and we've had to come out resolve for and we've had to come out one way or another on it through history one way or another on it through history one way or another on it through history right so with China in the 70s and ' 80s

right so with China in the 70s and ' 80s right so with China in the 70s and ' 80s we decided even though it's an we decided even though it's an we decided even though it's an authoritarian system we will engage with authoritarian system we will engage with

authoritarian system we will engage with it and I think in retrospect that was it and I think in retrospect that was it and I think in retrospect that was the right call because it has stayed the right call because it has stayed the right call because it has stayed authoritarian system but a billion plus

authoritarian system but a billion plus authoritarian system but a billion plus people are much wealthier and better off people are much wealthier and better off people are much wealthier and better off than they would have otherwise been um than they would have otherwise been um

than they would have otherwise been um and it's not clear that it would have and it's not clear that it would have and it's not clear that it would have stopped being an authoritarian country stopped being an authoritarian country stopped being an authoritarian country otherwise you can just look at North

otherwise you can just look at North otherwise you can just look at North Korea uh as an example of that, right? Korea uh as an example of that, right?

Korea uh as an example of that, right? And I don't know if that takes that much And I don't know if that takes that much And I don't know if that takes that much that much intelligence to remain an that much intelligence to remain an that much intelligence to remain an authoritarian country that continues to

authoritarian country that continues to authoritarian country that continues to coales its own power. And so you can coales its own power. And so you can coales its own power. And so you can just imagine a North Korea with an AI just imagine a North Korea with an AI

just imagine a North Korea with an AI that's much worse than everybody else's that's much worse than everybody else's that's much worse than everybody else's but still enough to keep power and and but still enough to keep power and and but still enough to keep power and and and and then so in general it seems like

and and then so in general it seems like and and then so in general it seems like should we just have this attitude of the should we just have this attitude of the should we just have this attitude of the benefits of AI will in the form of all benefits of AI will in the form of all

benefits of AI will in the form of all these empowerments of humanity and these empowerments of humanity and these empowerments of humanity and health and so forth will be big and in health and so forth will be big and in health and so forth will be big and in historically we have decided it's good

historically we have decided it's good historically we have decided it's good to spread the benefits of technology to spread the benefits of technology to spread the benefits of technology widely even with even to people whose widely even with even to people whose

widely even with even to people whose governments are authoritarian and I governments are authoritarian and I governments are authoritarian and I think I guess it is a tough question how think I guess it is a tough question how think I guess it is a tough question how to think about it with AI but um

to think about it with AI but um to think about it with AI but um historically we have said Yes, this historically we have said Yes, this historically we have said Yes, this there this is a positive some world and there this is a positive some world and

there this is a positive some world and it's still worth diffusing technology. it's still worth diffusing technology. it's still worth diffusing technology. &gt;&gt; Yeah. So so there are a number of &gt;&gt; Yeah. So so there are a number of &gt;&gt; Yeah. So so there are a number of choices we have. I you know I think

choices we have. I you know I think choices we have. I you know I think framing this as a kind of government to framing this as a kind of government to framing this as a kind of government to government decision and and you know in government decision and and you know in

[120:23]

government decision and and you know in in national security terms that's like in national security terms that's like in national security terms that's like one lens but there are a lot of other one lens but there are a lot of other one lens but there are a lot of other lenses like you could imagine a world

lenses like you could imagine a world lenses like you could imagine a world where you know we produce all these where you know we produce all these where you know we produce all these cures to diseases and like the you know cures to diseases and like the you know

cures to diseases and like the you know the the the cures to diseases are fine the the the cures to diseases are fine the the the cures to diseases are fine to sell to authoritarian countries. The to sell to authoritarian countries. The to sell to authoritarian countries. The data centers just aren't right. the

data centers just aren't right. the data centers just aren't right. the chips and the data centers just aren't chips and the data centers just aren't chips and the data centers just aren't um and that the AI industry itself. Um um and that the AI industry itself. Um

um and that the AI industry itself. Um uh you know like like another uh you know like like another uh you know like like another possibility is and and I think folks possibility is and and I think folks possibility is and and I think folks should think about this like you know

should think about this like you know should think about this like you know could there be developments we can make could there be developments we can make could there be developments we can make either that naturally happen as a result either that naturally happen as a result

either that naturally happen as a result of AI or that we could make happen by of AI or that we could make happen by of AI or that we could make happen by building technology on AI. Could we building technology on AI. Could we building technology on AI. Could we create an equilibrium where where it

create an equilibrium where where it create an equilibrium where where it becomes infeasible for authoritarian becomes infeasible for authoritarian becomes infeasible for authoritarian countries to deny their people kind of countries to deny their people kind of

countries to deny their people kind of private use of the benefits of the private use of the benefits of the private use of the benefits of the technology? Um uh you know are there are technology? Um uh you know are there are technology? Um uh you know are there are there are there are there equilibria

there are there are there equilibria there are there are there equilibria where we can kind of give everyone in where we can kind of give everyone in where we can kind of give everyone in authoritarian country their own AI model authoritarian country their own AI model

authoritarian country their own AI model that kind of you you know like defends that kind of you you know like defends that kind of you you know like defends themselves from surveillance and there themselves from surveillance and there themselves from surveillance and there isn't a way for the authoritarian

isn't a way for the authoritarian isn't a way for the authoritarian country to like crack crack down on this country to like crack crack down on this country to like crack crack down on this while while retaining power. I don't while while retaining power. I don't

while while retaining power. I don't know that that sounds to me like if that know that that sounds to me like if that know that that sounds to me like if that went far enough it would be it would be went far enough it would be it would be went far enough it would be it would be a reason why authoritarian countries

a reason why authoritarian countries a reason why authoritarian countries would disintegrate from the inside. Um would disintegrate from the inside. Um would disintegrate from the inside. Um but but maybe there's a middle world but but maybe there's a middle world

but but maybe there's a middle world where like there there's an equilibrium where like there there's an equilibrium where like there there's an equilibrium where if they want to hold on to power where if they want to hold on to power where if they want to hold on to power the authoritarians can't deny kind of

the authoritarians can't deny kind of the authoritarians can't deny kind of individualized access access to the individualized access access to the individualized access access to the technology. But I actually do have a technology. But I actually do have a

technology. But I actually do have a hope for the for the um for the for the hope for the for the um for the for the hope for the for the um for the for the more radical version which is you know more radical version which is you know more radical version which is you know is it possible that the technology might

is it possible that the technology might is it possible that the technology might inherently have properties or that by inherently have properties or that by inherently have properties or that by building on it in certain ways we could building on it in certain ways we could

building on it in certain ways we could create properties um that that that that create properties um that that that that create properties um that that that that have this kind of dissolving effect on have this kind of dissolving effect on have this kind of dissolving effect on authoritarian structures. Now, we we

authoritarian structures. Now, we we authoritarian structures. Now, we we hoped originally, if we think back to hoped originally, if we think back to hoped originally, if we think back to the beginning of the Obama the beginning of the Obama

the beginning of the Obama administration, we thought originally administration, we thought originally administration, we thought originally that that, you know, social media and that that, you know, social media and that that, you know, social media and and the internet would have that

and the internet would have that and the internet would have that property, and it turns out not to. But, property, and it turns out not to. But, property, and it turns out not to. But, but I I don't know what what if we could but I I don't know what what if we could

but I I don't know what what if we could uh what if we could try again with with uh what if we could try again with with uh what if we could try again with with the knowledge of how many things could the knowledge of how many things could the knowledge of how many things could go wrong and that this is a different

go wrong and that this is a different go wrong and that this is a different technology. I don't know that it would technology. I don't know that it would technology. I don't know that it would work, but it's worth a try.

[122:25]

work, but it's worth a try. work, but it's worth a try. &gt;&gt; Yeah. I think it's just it's very &gt;&gt; Yeah. I think it's just it's very &gt;&gt; Yeah. I think it's just it's very unpredictable. Like there's first unpredictable. Like there's first

unpredictable. Like there's first principles reasons why authoritarianism. principles reasons why authoritarianism. principles reasons why authoritarianism. &gt;&gt; It's all very unpredictable. I I don't &gt;&gt; It's all very unpredictable. I I don't &gt;&gt; It's all very unpredictable. I I don't think I mean we got to we we just got to

think I mean we got to we we just got to think I mean we got to we we just got to we kind of we got to recognize the we kind of we got to recognize the we kind of we got to recognize the problem and then we got to come up with problem and then we got to come up with

problem and then we got to come up with 10 things we can try and we got to try 10 things we can try and we got to try 10 things we can try and we got to try those and then assess whether they're those and then assess whether they're those and then assess whether they're working or which ones are working if any

working or which ones are working if any working or which ones are working if any and and then try new ones if the old and and then try new ones if the old and and then try new ones if the old ones aren't. I guess what that nets out ones aren't. I guess what that nets out

ones aren't. I guess what that nets out to today is you say we will not sell to today is you say we will not sell to today is you say we will not sell data centers or sorry chips and then the data centers or sorry chips and then the data centers or sorry chips and then the ability to make chips to China and so in

ability to make chips to China and so in ability to make chips to China and so in some sense you are denying there would some sense you are denying there would some sense you are denying there would be some benefits to that's right the be some benefits to that's right the

be some benefits to that's right the Chinese economy Chinese people etc Chinese economy Chinese people etc Chinese economy Chinese people etc because we're doing that and then because we're doing that and then because we're doing that and then there'd also be benefits to the American

there'd also be benefits to the American there'd also be benefits to the American economy because it's a positive sum economy because it's a positive sum economy because it's a positive sum world we could trade they could have world we could trade they could have

world we could trade they could have their country data centers doing one their country data centers doing one their country data centers doing one thing we could have ours doing another thing we could have ours doing another thing we could have ours doing another and already we you're saying it's not

and already we you're saying it's not and already we you're saying it's not worth that positive sum worth that positive sum worth that positive sum stipend to empower this country's stipend to empower this country's

stipend to empower this country's &gt;&gt; what what I would say is that you know &gt;&gt; what what I would say is that you know &gt;&gt; what what I would say is that you know we are we are about to be in a world we are we are about to be in a world we are we are about to be in a world where growth and economic value will

where growth and economic value will where growth and economic value will come very easily if right if we're able come very easily if right if we're able come very easily if right if we're able to build these powerful AI models growth to build these powerful AI models growth

to build these powerful AI models growth and economic value will come very easily and economic value will come very easily and economic value will come very easily what will not come easily is what will not come easily is what will not come easily is distribution of benefits distribution of

distribution of benefits distribution of distribution of benefits distribution of wealth political freedom um you know wealth political freedom um you know wealth political freedom um you know these are the things that are going to these are the things that are going to

these are the things that are going to be hard to achieve and so when I think be hard to achieve and so when I think be hard to achieve and so when I think about policy about policy about policy I think I think that the technology and

I think I think that the technology and I think I think that the technology and the market will deliver all the the market will deliver all the the market will deliver all the fundamental benefits, you know, almost fundamental benefits, you know, almost

fundamental benefits, you know, almost almost faster than we can take them. Um almost faster than we can take them. Um almost faster than we can take them. Um uh and and that these questions about uh and and that these questions about uh and and that these questions about about distribution and political freedom

about distribution and political freedom about distribution and political freedom and rights are are are the ones that and rights are are are the ones that and rights are are are the ones that that will actually matter and that that will actually matter and that

that will actually matter and that policy should focus on. Okay. So policy should focus on. Okay. So policy should focus on. Okay. So speaking of distribution, as you're speaking of distribution, as you're speaking of distribution, as you're mentioning, we have developing countries

mentioning, we have developing countries mentioning, we have developing countries and and and &gt;&gt; um &gt;&gt; um

&gt;&gt; um &gt;&gt; in many cases catchup growth has weak &gt;&gt; in many cases catchup growth has weak &gt;&gt; in many cases catchup growth has weak been weaker than we would have hoped been weaker than we would have hoped been weaker than we would have hoped for. When catchup growth does happen,

for. When catchup growth does happen, for. When catchup growth does happen, it's fundamentally because they have it's fundamentally because they have it's fundamentally because they have underutilized labor and we can bring the underutilized labor and we can bring the

underutilized labor and we can bring the capital and knowhow from developed capital and knowhow from developed capital and knowhow from developed countries to these countries and then countries to these countries and then countries to these countries and then they can grow quite rapidly.

they can grow quite rapidly. they can grow quite rapidly. &gt;&gt; Obviously in a world where labor is no &gt;&gt; Obviously in a world where labor is no &gt;&gt; Obviously in a world where labor is no longer the constraining factor, this longer the constraining factor, this

[124:28]

longer the constraining factor, this mechanism no longer works. mechanism no longer works. mechanism no longer works. &gt;&gt; And so is the hope basically to rely on &gt;&gt; And so is the hope basically to rely on &gt;&gt; And so is the hope basically to rely on philanthropy from the people who

philanthropy from the people who philanthropy from the people who immediately get wealthy from AI or from immediately get wealthy from AI or from immediately get wealthy from AI or from the countries that get wealthy from AI?

the countries that get wealthy from AI? the countries that get wealthy from AI? What what is the hope for? Yeah, I I What what is the hope for? Yeah, I I What what is the hope for? Yeah, I I mean philanthropy should obviously play mean philanthropy should obviously play

mean philanthropy should obviously play some role as it has the you know as has some role as it has the you know as has some role as it has the you know as has in the past but I think growth is always in the past but I think growth is always in the past but I think growth is always growth is always better and stronger if

growth is always better and stronger if growth is always better and stronger if we can make it endogenous. So you know we can make it endogenous. So you know we can make it endogenous. So you know what are the relevant industries in like what are the relevant industries in like

what are the relevant industries in like in like in like in like an AI driven in like in like in like an AI driven in like in like in like an AI driven world. Look there's lots of stuff you world. Look there's lots of stuff you world. Look there's lots of stuff you know like there's you know I said I said

know like there's you know I said I said know like there's you know I said I said we shouldn't build data centers in China we shouldn't build data centers in China we shouldn't build data centers in China but there's no reason we shouldn't build but there's no reason we shouldn't build

but there's no reason we shouldn't build data centers in Africa right? Um in fact data centers in Africa right? Um in fact data centers in Africa right? Um in fact I think it'd be great to build data I think it'd be great to build data I think it'd be great to build data centers in Africa. um you know as not

centers in Africa. um you know as not centers in Africa. um you know as not long as they're not owned by China. We long as they're not owned by China. We long as they're not owned by China. We should we should build we should build should we should build we should build

should we should build we should build data centers in Africa. I think that's a data centers in Africa. I think that's a data centers in Africa. I think that's a that's that's I think that's a great that's that's I think that's a great that's that's I think that's a great thing to do. um you know we should also

thing to do. um you know we should also thing to do. um you know we should also build you know there's no reason we build you know there's no reason we build you know there's no reason we can't build you know a pharmaceutical can't build you know a pharmaceutical

can't build you know a pharmaceutical industry that's like AIdriven like you industry that's like AIdriven like you industry that's like AIdriven like you know the the if if AI is accelerating know the the if if AI is accelerating know the the if if AI is accelerating accelerating drug discovery then you

accelerating drug discovery then you accelerating drug discovery then you know there will be a bunch of biotech know there will be a bunch of biotech know there will be a bunch of biotech startups like let's make sure some of startups like let's make sure some of

startups like let's make sure some of those happen in the developing world and those happen in the developing world and those happen in the developing world and certainly during the transition I mean certainly during the transition I mean certainly during the transition I mean we can talk about the point where humans

we can talk about the point where humans we can talk about the point where humans have no role but but humans will have have no role but but humans will have have no role but but humans will have still have some role in starting up still have some role in starting up

still have some role in starting up these companies and supervising these companies and supervising these companies and supervising supervising the AI models so let's make supervising the AI models so let's make supervising the AI models so let's make sure some of those humans are humans in

sure some of those humans are humans in sure some of those humans are humans in developing world so that fast growth can developing world so that fast growth can developing world so that fast growth can happen there as well.

happen there as well. happen there as well. &gt;&gt; You guys recently announced quad is &gt;&gt; You guys recently announced quad is &gt;&gt; You guys recently announced quad is going to have a constitution that's going to have a constitution that's

going to have a constitution that's aligned to a set of values and not aligned to a set of values and not aligned to a set of values and not necessarily just the end user and necessarily just the end user and necessarily just the end user and there's a world you can imagine where if

there's a world you can imagine where if there's a world you can imagine where if it is aligned to the end user it it is aligned to the end user it it is aligned to the end user it preserves the balance of power we have preserves the balance of power we have

preserves the balance of power we have in the world today because everybody in the world today because everybody in the world today because everybody gets to have their own AI that's gets to have their own AI that's gets to have their own AI that's advocating for them and so the ratio of

advocating for them and so the ratio of advocating for them and so the ratio of bad actors to good actors stays bad actors to good actors stays bad actors to good actors stays constant. It seems to work out for our constant. It seems to work out for our

constant. It seems to work out for our world today. Um why is it better not to world today. Um why is it better not to world today. Um why is it better not to do that but to have a specific set of do that but to have a specific set of do that but to have a specific set of values that the AI should carry forward?

values that the AI should carry forward? values that the AI should carry forward? &gt;&gt; Uh yeah so I'm not sure I'd quite draw &gt;&gt; Uh yeah so I'm not sure I'd quite draw &gt;&gt; Uh yeah so I'm not sure I'd quite draw the distinction in that way. Um there the distinction in that way. Um there

the distinction in that way. Um there there are maybe two relevant there are maybe two relevant there are maybe two relevant distinctions here which are I think distinctions here which are I think distinctions here which are I think you're talking about a mix of the two

you're talking about a mix of the two you're talking about a mix of the two like one is should we give the model a like one is should we give the model a like one is should we give the model a set of instructions about do this and set of instructions about do this and

[126:29]

set of instructions about do this and versus don't do this versus don't do this versus don't do this &gt;&gt; and the other you know versus should we &gt;&gt; and the other you know versus should we &gt;&gt; and the other you know versus should we give the model a set of principles for

give the model a set of principles for give the model a set of principles for you know for kind of how to act. Um and you know for kind of how to act. Um and you know for kind of how to act. Um and and and there it's it's you know it's I and and there it's it's you know it's I

and and there it's it's you know it's I you know it's it's just p it's kind of you know it's it's just p it's kind of you know it's it's just p it's kind of purely a practical and empirical thing purely a practical and empirical thing purely a practical and empirical thing that we've observed that by teaching the

that we've observed that by teaching the that we've observed that by teaching the model principles getting it to learn model principles getting it to learn model principles getting it to learn from principles its behavior is more from principles its behavior is more

from principles its behavior is more consistent. It's easier to cover edge consistent. It's easier to cover edge consistent. It's easier to cover edge cases and the model is more likely to do cases and the model is more likely to do cases and the model is more likely to do what people want it to do. In other

what people want it to do. In other what people want it to do. In other words, if you, you know, if you're like, words, if you, you know, if you're like, words, if you, you know, if you're like, you know, don't tell people how to you know, don't tell people how to

you know, don't tell people how to hotwire a car, don't speak in Korea, and hotwire a car, don't speak in Korea, and hotwire a car, don't speak in Korea, and don't, you know, you know, just, you don't, you know, you know, just, you don't, you know, you know, just, you know, if you give it a list of rules, it

know, if you give it a list of rules, it know, if you give it a list of rules, it doesn't really understand the rules, and doesn't really understand the rules, and doesn't really understand the rules, and it's kind of hard to generalize from it's kind of hard to generalize from

it's kind of hard to generalize from them. Um, you know, if if it's just kind them. Um, you know, if if it's just kind them. Um, you know, if if it's just kind of a like, you know, list of do dos and of a like, you know, list of do dos and of a like, you know, list of do dos and don'ts. Whereas, if you give it

don'ts. Whereas, if you give it don'ts. Whereas, if you give it principles and then, you know, it has principles and then, you know, it has principles and then, you know, it has some hard guard rails like don't make some hard guard rails like don't make

some hard guard rails like don't make biological weapons. But overall you're biological weapons. But overall you're biological weapons. But overall you're trying to understand trying to understand trying to understand what it should be aiming to do h how it

what it should be aiming to do h how it what it should be aiming to do h how it should be aiming to operate. So just should be aiming to operate. So just should be aiming to operate. So just from a practical perspective that turns from a practical perspective that turns

from a practical perspective that turns out to be just a more effective way to out to be just a more effective way to out to be just a more effective way to train the model. That's one piece of it.

train the model. That's one piece of it. train the model. That's one piece of it. So that you know it's the kind of rules So that you know it's the kind of rules So that you know it's the kind of rules versus principles trade-off. Then versus principles trade-off. Then

versus principles trade-off. Then there's another thing you're talking there's another thing you're talking there's another thing you're talking about which is kind of like the about which is kind of like the about which is kind of like the cageability versus um like you know I

cageability versus um like you know I cageability versus um like you know I would say kind of intr intrinsic would say kind of intr intrinsic would say kind of intr intrinsic motivation trade-off which is like how motivation trade-off which is like how

motivation trade-off which is like how much should the model be a kind of I much should the model be a kind of I much should the model be a kind of I don't know like a a skin suit or don't know like a a skin suit or don't know like a a skin suit or something where you know you know you

something where you know you know you something where you know you know you know you just kind of you know it just know you just kind of you know it just know you just kind of you know it just kind of directly follows the kind of directly follows the

kind of directly follows the instructions that are given to it by instructions that are given to it by instructions that are given to it by whoever is giving it those instructions.

whoever is giving it those instructions. whoever is giving it those instructions. um versus how much should the model have um versus how much should the model have um versus how much should the model have an inherent set of values and and go off an inherent set of values and and go off

an inherent set of values and and go off and do things on its own. Um and and and and do things on its own. Um and and and and do things on its own. Um and and and and and there I I would actually say and and there I I would actually say and and there I I would actually say everything about the model is actually

everything about the model is actually everything about the model is actually closer to the direction of of like you closer to the direction of of like you closer to the direction of of like you know it should mostly do what people know it should mostly do what people

know it should mostly do what people want. It should mostly follow the we're want. It should mostly follow the we're want. It should mostly follow the we're not trying to build something that like not trying to build something that like not trying to build something that like you know goes off and runs the world on

you know goes off and runs the world on you know goes off and runs the world on its own. We're actually pretty far on its own. We're actually pretty far on its own. We're actually pretty far on the corable side. Now, now what we do the corable side. Now, now what we do

[128:32]

the corable side. Now, now what we do say is there are certain things that the say is there are certain things that the say is there are certain things that the model won't do, right? That it's like model won't do, right? That it's like model won't do, right? That it's like you know that that that I think we say

you know that that that I think we say you know that that that I think we say it in various ways in the constitution it in various ways in the constitution it in various ways in the constitution that under normal circumstances if that under normal circumstances if

that under normal circumstances if someone asks the model to do a task it someone asks the model to do a task it someone asks the model to do a task it should do that task that that should be should do that task that that should be should do that task that that should be the default. Um but if you've asked it

the default. Um but if you've asked it the default. Um but if you've asked it to do something dangerous or if you've to do something dangerous or if you've to do something dangerous or if you've you know if you've um asked it to um you you know if you've um asked it to um you

you know if you've um asked it to um you know uh uh uh to kind of harm someone know uh uh uh to kind of harm someone know uh uh uh to kind of harm someone else um then the model is unwilling to else um then the model is unwilling to else um then the model is unwilling to do that. So I I actually think of it as

do that. So I I actually think of it as do that. So I I actually think of it as like a mostly a mostly corable model like a mostly a mostly corable model like a mostly a mostly corable model that has some limits but those limits that has some limits but those limits

that has some limits but those limits are based on principles. are based on principles. are based on principles. &gt;&gt; Yeah. I mean then the fundamental &gt;&gt; Yeah. I mean then the fundamental &gt;&gt; Yeah. I mean then the fundamental question is how are those principles

question is how are those principles question is how are those principles determined? And this is not a special determined? And this is not a special determined? And this is not a special question for anthropic. would be a question for anthropic. would be a

question for anthropic. would be a question for any company but um question for any company but um question for any company but um &gt;&gt; uh because you have been the ones to &gt;&gt; uh because you have been the ones to &gt;&gt; uh because you have been the ones to actually write down the principles I get

actually write down the principles I get actually write down the principles I get to ask you this question normally a to ask you this question normally a to ask you this question normally a constitution is like you write it down constitution is like you write it down

constitution is like you write it down it's set in stone and there's a process it's set in stone and there's a process it's set in stone and there's a process of updating it and changing it and so of updating it and changing it and so of updating it and changing it and so forth in this case it seems like a

forth in this case it seems like a forth in this case it seems like a document that people anthropic write document that people anthropic write document that people anthropic write that can be changed at any time that that can be changed at any time that

that can be changed at any time that guides the behavior of systems are going guides the behavior of systems are going guides the behavior of systems are going to be the basis of a lot of economic to be the basis of a lot of economic to be the basis of a lot of economic activity what is H how do you think

activity what is H how do you think activity what is H how do you think about ho how those principles should be about ho how those principles should be about ho how those principles should be set?

set? set? &gt;&gt; Yes. Um so I think there's there's two &gt;&gt; Yes. Um so I think there's there's two &gt;&gt; Yes. Um so I think there's there's two there's maybe three there's maybe three

there's maybe three three kind of sizes of loop here, right? three kind of sizes of loop here, right? three kind of sizes of loop here, right? Three three ways to iterate. One is you Three three ways to iterate. One is you Three three ways to iterate. One is you can iterate. We iterate within

can iterate. We iterate within can iterate. We iterate within enthropic. We train the model. We're not enthropic. We train the model. We're not enthropic. We train the model. We're not happy with it and we kind of change the happy with it and we kind of change the

happy with it and we kind of change the constitution. constitution. constitution. &gt;&gt; And I think that's good to do. Um and &gt;&gt; And I think that's good to do. Um and &gt;&gt; And I think that's good to do. Um and you know putting out publicly you know

you know putting out publicly you know you know putting out publicly you know making updates to the constitution every making updates to the constitution every making updates to the constitution every once in a while saying here's a new once in a while saying here's a new

once in a while saying here's a new constitution. I think that's good to do constitution. I think that's good to do constitution. I think that's good to do because people can comment on it. The because people can comment on it. The because people can comment on it. The second level of loop is different

second level of loop is different second level of loop is different companies will have different companies will have different companies will have different constitutions. Um and you know I think constitutions. Um and you know I think

constitutions. Um and you know I think it's useful for like anthropic puts out it's useful for like anthropic puts out it's useful for like anthropic puts out a constitution and you know you the a constitution and you know you the a constitution and you know you the Gemini model puts out a constitution and

Gemini model puts out a constitution and Gemini model puts out a constitution and you know other companies put out a you know other companies put out a you know other companies put out a constitution and then then they can kind constitution and then then they can kind

constitution and then then they can kind of look at them compare outside of look at them compare outside of look at them compare outside observers can critique and say this this observers can critique and say this this observers can critique and say this this I like this one this thing from this

[130:36]

I like this one this thing from this I like this one this thing from this constitution and this thing for that constitution and this thing for that constitution and this thing for that constitution and and then kind of that constitution and and then kind of that

constitution and and then kind of that that creates some kind of you know soft that creates some kind of you know soft that creates some kind of you know soft incentive and feedback for all the incentive and feedback for all the incentive and feedback for all the companies to like take the best of each

companies to like take the best of each companies to like take the best of each elements and improve Then I think elements and improve Then I think elements and improve Then I think there's a third loop which is you know there's a third loop which is you know

there's a third loop which is you know society beyond the AI companies and society beyond the AI companies and society beyond the AI companies and beyond just those who kind of you know beyond just those who kind of you know beyond just those who kind of you know who who comment on the constitutions

who who comment on the constitutions who who comment on the constitutions without hard power and and there you without hard power and and there you without hard power and and there you know we've done some experiments like know we've done some experiments like

know we've done some experiments like you know a couple years ago we did an you know a couple years ago we did an you know a couple years ago we did an experiment with I think it was called experiment with I think it was called experiment with I think it was called the collective intelligence project to

the collective intelligence project to the collective intelligence project to like um you know to to basically pull like um you know to to basically pull like um you know to to basically pull people and ask them what should be in people and ask them what should be in

people and ask them what should be in our AI constitution. um uh and and you our AI constitution. um uh and and you our AI constitution. um uh and and you know I think at the time we incorporated know I think at the time we incorporated know I think at the time we incorporated some of those changes and so you could

some of those changes and so you could some of those changes and so you could imagine with the new approach we've imagine with the new approach we've imagine with the new approach we've taken to the constitution doing taken to the constitution doing

taken to the constitution doing something like that it's a little harder something like that it's a little harder something like that it's a little harder because it's like that was actually an because it's like that was actually an because it's like that was actually an easier approach to take when the

easier approach to take when the easier approach to take when the constitution was like a list of dos and constitution was like a list of dos and constitution was like a list of dos and don'ts um at the level of principles it don'ts um at the level of principles it

don'ts um at the level of principles it has to have a certain amount of has to have a certain amount of has to have a certain amount of coherence um but but you could you could coherence um but but you could you could coherence um but but you could you could still imagine getting views from a wide

still imagine getting views from a wide still imagine getting views from a wide variety of people and I think you could variety of people and I think you could variety of people and I think you could also imagine and this is like a crazy also imagine and this is like a crazy

also imagine and this is like a crazy idea but hey you know this whole idea but hey you know this whole idea but hey you know this whole interview is about crazy ideas, right?

interview is about crazy ideas, right? interview is about crazy ideas, right? So, um uh you know, you could even So, um uh you know, you could even So, um uh you know, you could even imagine systems of of kind of imagine systems of of kind of

imagine systems of of kind of representative government having having representative government having having representative government having having input, right? Like, you know, I wouldn't input, right? Like, you know, I wouldn't input, right? Like, you know, I wouldn't I wouldn't do this today because the

I wouldn't do this today because the I wouldn't do this today because the legislative process is so slow. Like legislative process is so slow. Like legislative process is so slow. Like this is exactly why I think we should be this is exactly why I think we should be

this is exactly why I think we should be careful about the legislative process careful about the legislative process careful about the legislative process and AI regulation. But there's no reason and AI regulation. But there's no reason and AI regulation. But there's no reason you couldn't in principle say like you

you couldn't in principle say like you you couldn't in principle say like you know all AI you know all AI models have know all AI you know all AI models have know all AI you know all AI models have to have a constitution that starts with to have a constitution that starts with

to have a constitution that starts with like these things and then like you can like these things and then like you can like these things and then like you can append you can append other things after append you can append other things after append you can append other things after it but like there has to be this special

it but like there has to be this special it but like there has to be this special section that like takes precedence. I section that like takes precedence. I section that like takes precedence. I wouldn't do that. That's too rigid. That wouldn't do that. That's too rigid. That

wouldn't do that. That's too rigid. That that sounds um you know that that that that sounds um you know that that that that sounds um you know that that that that sounds kind of overly prescriptive that sounds kind of overly prescriptive that sounds kind of overly prescriptive in a way that I think overly aggressive

in a way that I think overly aggressive in a way that I think overly aggressive legislation is. But like that is a thing legislation is. But like that is a thing legislation is. But like that is a thing you could you know like like that is you could you know like like that is

you could you know like like that is that is a thing you could try to do. Is that is a thing you could try to do. Is that is a thing you could try to do. Is is there some much less heavy-handed is there some much less heavy-handed is there some much less heavy-handed version of that? Maybe I really like

version of that? Maybe I really like version of that? Maybe I really like control loop too. um where obviously control loop too. um where obviously control loop too. um where obviously this is not how constitutions of actual this is not how constitutions of actual

[132:40]

this is not how constitutions of actual governments do or should work where governments do or should work where governments do or should work where there there's not this vague sense in there there's not this vague sense in there there's not this vague sense in which the Supreme Court will feel out

which the Supreme Court will feel out which the Supreme Court will feel out how people are feeling and what are how people are feeling and what are how people are feeling and what are their vibes and then update the of the their vibes and then update the of the

their vibes and then update the of the constitution accordingly. There's with constitution accordingly. There's with constitution accordingly. There's with actual governments there's a more actual governments there's a more actual governments there's a more procedural process. Exactly. But you

procedural process. Exactly. But you procedural process. Exactly. But you actually have a vision actually have a vision actually have a vision &gt;&gt; of competition between constitutions &gt;&gt; of competition between constitutions

&gt;&gt; of competition between constitutions which is actually very reminiscent of which is actually very reminiscent of which is actually very reminiscent of how um how um how um &gt;&gt; some libertarian charter cities people

&gt;&gt; some libertarian charter cities people &gt;&gt; some libertarian charter cities people used to talk about what an archipelago used to talk about what an archipelago used to talk about what an archipelago of different kinds of governments could of different kinds of governments could

of different kinds of governments could look like and then there would be look like and then there would be look like and then there would be selection among them of who could selection among them of who could selection among them of who could operate the most effectively in which

operate the most effectively in which operate the most effectively in which place people would be the happiest. And place people would be the happiest. And place people would be the happiest. And in a sense you're actually yeah there's in a sense you're actually yeah there's

in a sense you're actually yeah there's this vision. I'm I'm kind of recreating this vision. I'm I'm kind of recreating this vision. I'm I'm kind of recreating that.

that. that. &gt;&gt; Yeah. Yeah. This utopia of archipelago, &gt;&gt; Yeah. Yeah. This utopia of archipelago, &gt;&gt; Yeah. Yeah. This utopia of archipelago, &gt;&gt; you know, again, you know, I think I &gt;&gt; you know, again, you know, I think I

&gt;&gt; you know, again, you know, I think I think that vision has has, you know, think that vision has has, you know, think that vision has has, you know, things to recommend it and things that things to recommend it and things that things to recommend it and things that things things that will kind of kind of

things things that will kind of kind of things things that will kind of kind of go wrong with it. You know, I think I go wrong with it. You know, I think I go wrong with it. You know, I think I think it's a I think it's an interesting think it's a I think it's an interesting

think it's a I think it's an interesting in some ways compelling vision, but also in some ways compelling vision, but also in some ways compelling vision, but also things will go wrong with it that you things will go wrong with it that you things will go wrong with it that you hadn't that you hadn't imagined. So, you

hadn't that you hadn't imagined. So, you hadn't that you hadn't imagined. So, you know, I I I like loop 2 as well, but I I know, I I I like loop 2 as well, but I I know, I I I like loop 2 as well, but I I I feel like the whole thing has got to I feel like the whole thing has got to

I feel like the whole thing has got to be some some mix of loops one, two, and be some some mix of loops one, two, and be some some mix of loops one, two, and three. And it's it's a matter of the three. And it's it's a matter of the three. And it's it's a matter of the proportions, right? I I think that's got

proportions, right? I I think that's got proportions, right? I I think that's got to be the the answer. to be the the answer.

to be the the answer. &gt;&gt; Um &gt;&gt; Um &gt;&gt; when somebody eventually writes the &gt;&gt; when somebody eventually writes the &gt;&gt; when somebody eventually writes the equivalent of the making of the atomic equivalent of the making of the atomic

equivalent of the making of the atomic bomb for this era, what is the thing bomb for this era, what is the thing bomb for this era, what is the thing that will be hardest to glean from the that will be hardest to glean from the that will be hardest to glean from the historical record that they're most

historical record that they're most historical record that they're most likely to miss? I think a few things. likely to miss? I think a few things.

likely to miss? I think a few things. One is at every moment of this One is at every moment of this One is at every moment of this exponential, the extent to which the exponential, the extent to which the exponential, the extent to which the world outside it didn't understand it.

world outside it didn't understand it. world outside it didn't understand it. This is this is a bias that's often This is this is a bias that's often This is this is a bias that's often present in history where anything that present in history where anything that

present in history where anything that actually happened looks inevitable in actually happened looks inevitable in actually happened looks inevitable in retrospect and and so you know I I think retrospect and and so you know I I think retrospect and and so you know I I think when people when people look back it

when people when people look back it when people when people look back it will be hard for them to put themselves will be hard for them to put themselves will be hard for them to put themselves in the place of people who were actually in the place of people who were actually

in the place of people who were actually making a bet on this thing to happen making a bet on this thing to happen making a bet on this thing to happen that wasn't inevitable that we had these that wasn't inevitable that we had these that wasn't inevitable that we had these arguments like the arguments you know

arguments like the arguments you know arguments like the arguments you know that I make for scaling or that that I make for scaling or that that I make for scaling or that continual learning will be solved um uh continual learning will be solved um uh

[134:43]

continual learning will be solved um uh uh you know that that you know some of uh you know that that you know some of uh you know that that you know some of us internally in our heads put a high us internally in our heads put a high us internally in our heads put a high probability on this happening but but

probability on this happening but but probability on this happening but but it's like there's there's a world it's like there's there's a world it's like there's there's a world outside us that's not that's not acting outside us that's not that's not acting

outside us that's not that's not acting on it's not kind of not acting on that on it's not kind of not acting on that on it's not kind of not acting on that at all. Um uh and and and I think I at all. Um uh and and and I think I at all. Um uh and and and I think I think the the weirdness of it um I I I I

think the the weirdness of it um I I I I think the the weirdness of it um I I I I think unfortunately like the insolerity think unfortunately like the insolerity think unfortunately like the insolerity of it like you know of it like you know

of it like you know if if we're one year or two years away if if we're one year or two years away if if we're one year or two years away from it happening like the average from it happening like the average from it happening like the average person on the street has no idea and

person on the street has no idea and person on the street has no idea and that's one of the things I'm trying to that's one of the things I'm trying to that's one of the things I'm trying to change like with the memos with talking change like with the memos with talking

change like with the memos with talking to policy makers but like I don't know I to policy makers but like I don't know I to policy makers but like I don't know I think I I I think that's just a that's think I I I think that's just a that's think I I I think that's just a that's just like a crazy that's just like a

just like a crazy that's just like a just like a crazy that's just like a crazy thing. Yeah. Um, finally I would crazy thing. Yeah. Um, finally I would crazy thing. Yeah. Um, finally I would say and and this probably applies to say and and this probably applies to

say and and this probably applies to almost all historical moments of crisis. almost all historical moments of crisis. almost all historical moments of crisis. Um, how absolutely fast it was Um, how absolutely fast it was Um, how absolutely fast it was happening, how everything was happening

happening, how everything was happening happening, how everything was happening all at once. And so decisions that you all at once. And so decisions that you all at once. And so decisions that you might think, you know, were kind of might think, you know, were kind of

might think, you know, were kind of carefully calculated, well, actually you carefully calculated, well, actually you carefully calculated, well, actually you have to make that decision and then you have to make that decision and then you have to make that decision and then you have to make 30 other decisions on the

have to make 30 other decisions on the have to make 30 other decisions on the on the same day because it's all on the same day because it's all on the same day because it's all happening so fast and and you don't even happening so fast and and you don't even

happening so fast and and you don't even know which decisions are going to turn know which decisions are going to turn know which decisions are going to turn out to be consequential. So, you know, out to be consequential. So, you know, out to be consequential. So, you know, one of my one of my I guess worries,

one of my one of my I guess worries, one of my one of my I guess worries, although it's also an insight into into, although it's also an insight into into, although it's also an insight into into, you know, into kind of what's happening you know, into kind of what's happening

you know, into kind of what's happening is that, you know, some very critical is that, you know, some very critical is that, you know, some very critical decision will be will be some decision decision will be will be some decision decision will be will be some decision that, you know, someone just comes into

that, you know, someone just comes into that, you know, someone just comes into my office and is like, Dario, you have my office and is like, Dario, you have my office and is like, Dario, you have two minutes like, you know, should we two minutes like, you know, should we

two minutes like, you know, should we should we do, you know, should we do should we do, you know, should we do should we do, you know, should we do thing thing A or thing B on this like, thing thing A or thing B on this like, thing thing A or thing B on this like, you know, someone gives me this random,

you know, someone gives me this random, you know, someone gives me this random, you know, half page half page memo and you know, half page half page memo and you know, half page half page memo and is like, should we should we do A or B?

is like, should we should we do A or B? is like, should we should we do A or B? And I'm like, I don't know. I have to And I'm like, I don't know. I have to And I'm like, I don't know. I have to eat lunch. Let's do B. And and you know, eat lunch. Let's do B. And and you know,

eat lunch. Let's do B. And and you know, that ends up being the most that ends up being the most that ends up being the most consequential thing ever.

consequential thing ever. consequential thing ever. &gt;&gt; So, final question. Uh, it seems like &gt;&gt; So, final question. Uh, it seems like &gt;&gt; So, final question. Uh, it seems like you have you have

you have there's not tech CEOs who are usually there's not tech CEOs who are usually there's not tech CEOs who are usually writing 50page memos every few months, writing 50page memos every few months, writing 50page memos every few months, and it seems like you have managed to

and it seems like you have managed to and it seems like you have managed to build a role for yourself and a company build a role for yourself and a company build a role for yourself and a company around you which is compatible with this around you which is compatible with this

around you which is compatible with this more intellectual type role of CEO. And more intellectual type role of CEO. And more intellectual type role of CEO. And I want to understand how you construct I want to understand how you construct I want to understand how you construct that and how like how does that work to

[136:51]

that and how like how does that work to that and how like how does that work to be you just go away for a couple weeks be you just go away for a couple weeks be you just go away for a couple weeks and then you tell your company this is and then you tell your company this is

and then you tell your company this is the memo like here's what we're doing. the memo like here's what we're doing. the memo like here's what we're doing. It's also reported you write a bunch of It's also reported you write a bunch of It's also reported you write a bunch of these internally.

these internally. these internally. &gt;&gt; Yeah. So I mean for this particular one &gt;&gt; Yeah. So I mean for this particular one &gt;&gt; Yeah. So I mean for this particular one you know I wrote it over winter break.

you know I wrote it over winter break. you know I wrote it over winter break. Um uh so it was the time you know and I Um uh so it was the time you know and I Um uh so it was the time you know and I was having a a hard time finding the was having a a hard time finding the

was having a a hard time finding the time to actually find it to actually time to actually find it to actually time to actually find it to actually write it. But I actually think about write it. But I actually think about write it. But I actually think about this in a broader way. Um I actually

this in a broader way. Um I actually this in a broader way. Um I actually think it relates to the culture of the think it relates to the culture of the think it relates to the culture of the company. So I probably spend a third company. So I probably spend a third

company. So I probably spend a third maybe 40% of my time making sure the maybe 40% of my time making sure the maybe 40% of my time making sure the culture of Enthropic is good. As culture of Enthropic is good. As culture of Enthropic is good. As Enthropic has gotten larger, it's it's

Enthropic has gotten larger, it's it's Enthropic has gotten larger, it's it's gotten harder to just, you know, get gotten harder to just, you know, get gotten harder to just, you know, get involved in like, you know, directly involved in like, you know, directly

involved in like, you know, directly involved in like the training of the involved in like the training of the involved in like the training of the models, the launch of the models, the models, the launch of the models, the models, the launch of the models, the building of the products. Like it's 2500

building of the products. Like it's 2500 building of the products. Like it's 2500 people. It's like, you know, there's people. It's like, you know, there's people. It's like, you know, there's just, you know, I have certain just, you know, I have certain

just, you know, I have certain instincts, but like there's only, you instincts, but like there's only, you instincts, but like there's only, you know, I it's very difficult to get to know, I it's very difficult to get to know, I it's very difficult to get to get to get involved in every single

get to get involved in every single get to get involved in every single detail. You know, I like I I try as much detail. You know, I like I I try as much detail. You know, I like I I try as much as possible, but one thing that's very as possible, but one thing that's very

as possible, but one thing that's very leveraged is making sure Anthropic is a leveraged is making sure Anthropic is a leveraged is making sure Anthropic is a good place to work. People like working good place to work. People like working good place to work. People like working there. Everyone thinks of themselves as

there. Everyone thinks of themselves as there. Everyone thinks of themselves as team members. Everyone works together team members. Everyone works together team members. Everyone works together instead of against each other. And you instead of against each other. And you

instead of against each other. And you know, we've seen as some of the other AI know, we've seen as some of the other AI know, we've seen as some of the other AI companies have grown without naming any companies have grown without naming any companies have grown without naming any names, you know, we're starting to see

names, you know, we're starting to see names, you know, we're starting to see decoherence and people fighting each decoherence and people fighting each decoherence and people fighting each other. And you know, I would argue there other. And you know, I would argue there

other. And you know, I would argue there was even a lot of that from the was even a lot of that from the was even a lot of that from the beginning, but but you know, that it's beginning, but but you know, that it's beginning, but but you know, that it's it's gotten worse. But I I think we've

it's gotten worse. But I I think we've it's gotten worse. But I I think we've done an extraordinarily good job, even done an extraordinarily good job, even done an extraordinarily good job, even if not perfect, of holding the company if not perfect, of holding the company

if not perfect, of holding the company together, making everyone feel the together, making everyone feel the together, making everyone feel the mission, that we're sincere about the mission, that we're sincere about the mission, that we're sincere about the mission, and that, you know, everyone

mission, and that, you know, everyone mission, and that, you know, everyone has faith that everyone else there is has faith that everyone else there is has faith that everyone else there is working for the right reason, that we're working for the right reason, that we're

working for the right reason, that we're a team, that people aren't trying to get a team, that people aren't trying to get a team, that people aren't trying to get ahead at each other's expense or ahead at each other's expense or ahead at each other's expense or backstab each other, which again, I

backstab each other, which again, I backstab each other, which again, I think happens a lot at some of the other think happens a lot at some of the other think happens a lot at some of the other places. Um, and and how do you make that places. Um, and and how do you make that

places. Um, and and how do you make that the case? I mean it's a lot of things the case? I mean it's a lot of things the case? I mean it's a lot of things you know it's me it's it's it's Daniela you know it's me it's it's it's Daniela you know it's me it's it's it's Daniela who you know runs the company dayto-day

who you know runs the company dayto-day who you know runs the company dayto-day it's the co-founders it's the other it's the co-founders it's the other it's the co-founders it's the other people we hire it's the environment we people we hire it's the environment we

people we hire it's the environment we try to create but I think an important try to create but I think an important try to create but I think an important thing in the culture is I some and you thing in the culture is I some and you thing in the culture is I some and you know the the you know the other leaders

[138:51]

know the the you know the other leaders know the the you know the other leaders as well but especially me have to as well but especially me have to as well but especially me have to articulate what the company is about why articulate what the company is about why

articulate what the company is about why it's doing what it's doing what its it's doing what it's doing what its it's doing what it's doing what its strategy is what its values are what its strategy is what its values are what its strategy is what its values are what its mission is and what it stands for And um

mission is and what it stands for And um mission is and what it stands for And um you know when you get to 2500 people you you know when you get to 2500 people you you know when you get to 2500 people you can't do that person by person. You have can't do that person by person. You have

can't do that person by person. You have to write or you have to speak to the to write or you have to speak to the to write or you have to speak to the whole company. This is why I get up in whole company. This is why I get up in whole company. This is why I get up in front of the whole company every two

front of the whole company every two front of the whole company every two weeks and speak for an hour. It's weeks and speak for an hour. It's weeks and speak for an hour. It's actually I mean I wouldn't say I write actually I mean I wouldn't say I write

actually I mean I wouldn't say I write essays internally. I do two things. One essays internally. I do two things. One essays internally. I do two things. One I write this thing called DVQ Dario I write this thing called DVQ Dario I write this thing called DVQ Dario Vision Quest. Um uh uh I wasn't the one

Vision Quest. Um uh uh I wasn't the one Vision Quest. Um uh uh I wasn't the one who named it that. That's the name it it who named it that. That's the name it it who named it that. That's the name it it it received and it's one of these names it received and it's one of these names

it received and it's one of these names that I kind of I tried to fight it that I kind of I tried to fight it that I kind of I tried to fight it because it made it sound like I was like because it made it sound like I was like because it made it sound like I was like going off and smoking peyote or

going off and smoking peyote or going off and smoking peyote or something. Um uh but but the name just something. Um uh but but the name just something. Um uh but but the name just stuck. Um so I get up in front of the stuck. Um so I get up in front of the

stuck. Um so I get up in front of the company every two weeks. I have like a company every two weeks. I have like a company every two weeks. I have like a three or four page document and I just three or four page document and I just three or four page document and I just kind of talk through like three or four

kind of talk through like three or four kind of talk through like three or four different topics about what's going on different topics about what's going on different topics about what's going on internally the you know the the models internally the you know the the models

internally the you know the the models we're producing the products the outside we're producing the products the outside we're producing the products the outside industry the world as a whole as it industry the world as a whole as it industry the world as a whole as it relates to AI and geopolitically in

relates to AI and geopolitically in relates to AI and geopolitically in general you know just some mix of that general you know just some mix of that general you know just some mix of that and I just go through very very honestly and I just go through very very honestly

and I just go through very very honestly I just go through and I just I just say I just go through and I just I just say I just go through and I just I just say you know this is this is what I'm you know this is this is what I'm you know this is this is what I'm thinking this is what anthropic

thinking this is what anthropic thinking this is what anthropic leadership is thinking and then I answer leadership is thinking and then I answer leadership is thinking and then I answer questions and and that direct connection questions and and that direct connection

questions and and that direct connection I think has a lot of value that is hard I think has a lot of value that is hard I think has a lot of value that is hard to achieve when you're passing things to achieve when you're passing things to achieve when you're passing things down the chain you know six six levels

down the chain you know six six levels down the chain you know six six levels deep um uh and you know large fraction deep um uh and you know large fraction deep um uh and you know large fraction of the company comes comes to attend of the company comes comes to attend

of the company comes comes to attend either either in person or um either in either either in person or um either in either either in person or um either in person or virtually and you know it person or virtually and you know it person or virtually and you know it really means that you can communicate a

really means that you can communicate a really means that you can communicate a lot and then the other thing I do is I lot and then the other thing I do is I lot and then the other thing I do is I just you know I have a channel in Slack just you know I have a channel in Slack

just you know I have a channel in Slack where I just write a bunch of things and where I just write a bunch of things and where I just write a bunch of things and comment a lot um and often that's in comment a lot um and often that's in comment a lot um and often that's in response to you know just things I'm

response to you know just things I'm response to you know just things I'm seeing at the company or questions seeing at the company or questions seeing at the company or questions people ask or like you know we do people ask or like you know we do

people ask or like you know we do internal surveys and there are things internal surveys and there are things internal surveys and there are things people are concerned about and so I'll people are concerned about and so I'll people are concerned about and so I'll write them up and I'm like I'm you know

write them up and I'm like I'm you know write them up and I'm like I'm you know I'm I'm I'm just I'm very honest about I'm I'm I'm just I'm very honest about I'm I'm I'm just I'm very honest about these things you know I just I just say these things you know I just I just say

[140:54]

these things you know I just I just say them very directly and the point is to them very directly and the point is to them very directly and the point is to get a reputation of telling the company get a reputation of telling the company get a reputation of telling the company the truth about what's happening to call

the truth about what's happening to call the truth about what's happening to call things what they are to acknowledge things what they are to acknowledge things what they are to acknowledge problems to avoid the sort of corpo problems to avoid the sort of corpo

problems to avoid the sort of corpo speak the kind of defensive speak the kind of defensive speak the kind of defensive communication that often is necessary in communication that often is necessary in communication that often is necessary in public because you know the world is

public because you know the world is public because you know the world is very large and full of people who are very large and full of people who are very large and full of people who are you know interpreting things in bad you know interpreting things in bad

you know interpreting things in bad faith. Um but you know if you have a faith. Um but you know if you have a faith. Um but you know if you have a company of people who you trust and we company of people who you trust and we company of people who you trust and we try to hire people that we trust then

try to hire people that we trust then try to hire people that we trust then then you know you can you can you can then you know you can you can you can then you know you can you can you can you know you can you can really just be you know you can you can really just be

you know you can you can really just be entirely unfiltered. Um and uh you know entirely unfiltered. Um and uh you know entirely unfiltered. Um and uh you know I think I think that's an enormous I think I think that's an enormous I think I think that's an enormous strength of the company. It makes it a

strength of the company. It makes it a strength of the company. It makes it a better place to work. It makes people better place to work. It makes people better place to work. It makes people more you know more the sum of their more you know more the sum of their

more you know more the sum of their parts and increases likelihood that we parts and increases likelihood that we parts and increases likelihood that we accomplish the mission because everyone accomplish the mission because everyone accomplish the mission because everyone is on the same page about the mission

is on the same page about the mission is on the same page about the mission and everyone is debating and discussing and everyone is debating and discussing and everyone is debating and discussing how best to accomplish the mission.

how best to accomplish the mission. how best to accomplish the mission. &gt;&gt; Well in lie of an external Dario vision &gt;&gt; Well in lie of an external Dario vision &gt;&gt; Well in lie of an external Dario vision quest we have this interview.

quest we have this interview. quest we have this interview. &gt;&gt; This this interview is a little like &gt;&gt; This this interview is a little like &gt;&gt; This this interview is a little like that.

that. &gt;&gt; Uh this is fun Dario. Thanks for doing &gt;&gt; Uh this is fun Dario. Thanks for doing &gt;&gt; Uh this is fun Dario. Thanks for doing it.

it. it. &gt;&gt; Yeah thank you Dash. Hey everybody I &gt;&gt; Yeah thank you Dash. Hey everybody I &gt;&gt; Yeah thank you Dash. Hey everybody I hope you enjoyed that episode. If you hope you enjoyed that episode. If you

hope you enjoyed that episode. If you did the most helpful thing you can do is did the most helpful thing you can do is did the most helpful thing you can do is just share it with other people who you just share it with other people who you just share it with other people who you think might enjoy it. It's also helpful

think might enjoy it. It's also helpful think might enjoy it. It's also helpful if you leave a rating or a comment on if you leave a rating or a comment on if you leave a rating or a comment on whatever platform you're listening on.

whatever platform you're listening on. whatever platform you're listening on. If you're interested in sponsoring the If you're interested in sponsoring the If you're interested in sponsoring the podcast, you can reach out at podcast, you can reach out at

podcast, you can reach out at dwarcash.com/advertise. Otherwise, I'll see you on the next one.

