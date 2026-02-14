# Raw Transcript: The 100x AI Breakthrough No One is Talking About

[0:00]

Okay, so Google just released an update Okay, so Google just released an update to Gemini Deep Think. Now it's powered to Gemini Deep Think. Now it's powered to Gemini Deep Think. Now it's powered by Gemini 3. And everybody's kind of by Gemini 3. And everybody's kind of

by Gemini 3. And everybody's kind of losing their minds on benchmark numbers. losing their minds on benchmark numbers. losing their minds on benchmark numbers. 84% on RKGI 2, gold medals on math, 84% on RKGI 2, gold medals on math, 84% on RKGI 2, gold medals on math, physics, chemistry, Olympiad, and

physics, chemistry, Olympiad, and physics, chemistry, Olympiad, and legendary Grandmaster on Code Force. legendary Grandmaster on Code Force.

legendary Grandmaster on Code Force. Now, these are impressive, but if that's Now, these are impressive, but if that's Now, these are impressive, but if that's all you take away from this release, all you take away from this release, all you take away from this release, you're missing the actual story here.

you're missing the actual story here. you're missing the actual story here. Google actually did three things all at Google actually did three things all at Google actually did three things all at once and most people are conflating all once and most people are conflating all

once and most people are conflating all of them into one announcement. So there of them into one announcement. So there of them into one announcement. So there is a product update of deep think is a product update of deep think is a product update of deep think version 2 shipping to subscribers. Then

version 2 shipping to subscribers. Then version 2 shipping to subscribers. Then there is a research agent called Eliteia there is a research agent called Eliteia there is a research agent called Eliteia that nobody is really talking about but that nobody is really talking about but

that nobody is really talking about but it's very critical and there are two it's very critical and there are two it's very critical and there are two archive papers documenting 18 solved archive papers documenting 18 solved archive papers documenting 18 solved research problems. So the distance

research problems. So the distance research problems. So the distance between what was shipped to the between what was shipped to the between what was shipped to the consumers and what is happening in the consumers and what is happening in the

consumers and what is happening in the research lab is the real story here. So research lab is the real story here. So research lab is the real story here. So let me try to break it down. Now first let me try to break it down. Now first let me try to break it down. Now first let's get the benchmarks out of the way

let's get the benchmarks out of the way let's get the benchmarks out of the way because that's what most people are because that's what most people are because that's what most people are talking about. For humanity's last exam talking about. For humanity's last exam

talking about. For humanity's last exam who is seeing 48.4%. who is seeing 48.4%. who is seeing 48.4%. This is a benchmark specifically This is a benchmark specifically This is a benchmark specifically designed to test the absolute limits of

designed to test the absolute limits of designed to test the absolute limits of frontier models when it comes to human frontier models when it comes to human frontier models when it comes to human knowledge. Then there is ARC AGI2. Now knowledge. Then there is ARC AGI2. Now

knowledge. Then there is ARC AGI2. Now here it's able to get 84.6% which is 15 here it's able to get 84.6% which is 15 here it's able to get 84.6% which is 15 points ahead of Cloud Opus 46 and over points ahead of Cloud Opus 46 and over points ahead of Cloud Opus 46 and over 30 points ahead of GPT52

30 points ahead of GPT52 30 points ahead of GPT52 which is kind of crazy. I don't think we which is kind of crazy. I don't think we which is kind of crazy. I don't think we were expecting this. And then there is were expecting this. And then there is

were expecting this. And then there is code forces. So, it gets an ELO score of code forces. So, it gets an ELO score of code forces. So, it gets an ELO score of 3455, which is pretty incredible because 3455, which is pretty incredible because 3455, which is pretty incredible because this puts Gemini 3 Deep Think at the

this puts Gemini 3 Deep Think at the this puts Gemini 3 Deep Think at the eighth best computer programmer position eighth best computer programmer position eighth best computer programmer position in the world right now, which is a very in the world right now, which is a very

in the world right now, which is a very incredible feat to say the least. Now, incredible feat to say the least. Now, incredible feat to say the least. Now, there is a lot of discussion about the there is a lot of discussion about the there is a lot of discussion about the actual effectiveness of Gemini 3 as a

actual effectiveness of Gemini 3 as a actual effectiveness of Gemini 3 as a programmer compared to some of the other programmer compared to some of the other programmer compared to some of the other models. We're going to talk about that models. We're going to talk about that

[2:00]

models. We're going to talk about that later in the video. Now let's later in the video. Now let's later in the video. Now let's specifically talk about this Arc Asia 2 specifically talk about this Arc Asia 2 specifically talk about this Arc Asia 2 score because this is probably one of

score because this is probably one of score because this is probably one of the most important result for deep the most important result for deep the most important result for deep think. So first the cost story deep think. So first the cost story deep

think. So first the cost story deep things cost about 13.62 things cost about 13.62 things cost about 13.62 per task. That's actually 82% cheaper per task. That's actually 82% cheaper per task. That's actually 82% cheaper than the earlier deep think versions.

than the earlier deep think versions. than the earlier deep think versions. Now, this matters because a company Now, this matters because a company Now, this matters because a company called Poetic built an agentic harness called Poetic built an agentic harness

called Poetic built an agentic harness on top of regular Gemini 3 Pro that hit on top of regular Gemini 3 Pro that hit on top of regular Gemini 3 Pro that hit 54% on RKGI 2 at $31 per task, which was 54% on RKGI 2 at $31 per task, which was 54% on RKGI 2 at $31 per task, which was way less than $77 per task of earlier

way less than $77 per task of earlier way less than $77 per task of earlier version of Deep Think. So, these systems version of Deep Think. So, these systems version of Deep Think. So, these systems are becoming extremely smart at a are becoming extremely smart at a

are becoming extremely smart at a reasonable efficiency now. So, that reasonable efficiency now. So, that reasonable efficiency now. So, that tells you something about what Deep tells you something about what Deep tells you something about what Deep Think actually is. Now one thing to uh

Think actually is. Now one thing to uh Think actually is. Now one thing to uh consider some of the benchmarks that consider some of the benchmarks that consider some of the benchmarks that Google reported for Gemini 3 deep think Google reported for Gemini 3 deep think

Google reported for Gemini 3 deep think uses tools on compared to tools off with uses tools on compared to tools off with uses tools on compared to tools off with some of the other providers. But before some of the other providers. But before some of the other providers. But before that let's talk about what deep think

that let's talk about what deep think that let's talk about what deep think technically is. And this is important technically is. And this is important technically is. And this is important because a lot of people think it's a because a lot of people think it's a

because a lot of people think it's a separate model. It's not. Deepthink is a separate model. It's not. Deepthink is a separate model. It's not. Deepthink is a reasoning mode within Gemini 3. It is reasoning mode within Gemini 3. It is reasoning mode within Gemini 3. It is the same base model but it allocates

the same base model but it allocates the same base model but it allocates additional compute at inference time. So additional compute at inference time. So additional compute at inference time. So instead of giving you the fastest instead of giving you the fastest

instead of giving you the fastest possible answer it thinks longer before possible answer it thinks longer before possible answer it thinks longer before responding. Now to understand this this responding. Now to understand this this responding. Now to understand this this here is a very high level overview.

here is a very high level overview. here is a very high level overview. Standard chain of thought is linear. So Standard chain of thought is linear. So Standard chain of thought is linear. So step one, step two, step three and the step one, step two, step three and the

step one, step two, step three and the model is done. Now in case of deep think model is done. Now in case of deep think model is done. Now in case of deep think it does something different. So, it does something different. So, it does something different. So, Deepthink does something significantly

Deepthink does something significantly Deepthink does something significantly different. It explores multiple different. It explores multiple different. It explores multiple hypotheses in parallel, tests each one hypotheses in parallel, tests each one

hypotheses in parallel, tests each one of them, refine the best, verifies it, of them, refine the best, verifies it, of them, refine the best, verifies it, and then gives you the answer. And more and then gives you the answer. And more and then gives you the answer. And more critically, it can backtrack. So, let's

critically, it can backtrack. So, let's critically, it can backtrack. So, let's say if you go down hypothesis one and say if you go down hypothesis one and say if you go down hypothesis one and hits a dead end, it can reverse course.

[4:05]

hits a dead end, it can reverse course. hits a dead end, it can reverse course. Standard chain of thought cannot do Standard chain of thought cannot do Standard chain of thought cannot do that. More importantly, the number of that. More importantly, the number of

that. More importantly, the number of reasoning rounds is also dynamic. So a reasoning rounds is also dynamic. So a reasoning rounds is also dynamic. So a simple question might get two to three simple question might get two to three simple question might get two to three rounds and a complex physics problem

rounds and a complex physics problem rounds and a complex physics problem might get 10 rounds or more. Now here is might get 10 rounds or more. Now here is might get 10 rounds or more. Now here is the real number that matters the most.

the real number that matters the most. the real number that matters the most. The January 2026 version of deep think The January 2026 version of deep think The January 2026 version of deep think reduced the compute required for Olympia reduced the compute required for Olympia

reduced the compute required for Olympia level performance by 100x compared to level performance by 100x compared to level performance by 100x compared to the July 2025 version. And they showed the July 2025 version. And they showed the July 2025 version. And they showed that the infant's time scaling loss

that the infant's time scaling loss that the infant's time scaling loss continues to even beyond Olympiate continues to even beyond Olympiate continues to even beyond Olympiate problems into PhD level exercises. Don't problems into PhD level exercises. Don't

problems into PhD level exercises. Don't need bigger models. You need smarter need bigger models. You need smarter need bigger models. You need smarter allocation of compute at inference time.

allocation of compute at inference time. allocation of compute at inference time. Let the model think longer. Let it Let the model think longer. Let it Let the model think longer. Let it explore more paths along the way and explore more paths along the way and

explore more paths along the way and backtrack when it needs and you get backtrack when it needs and you get backtrack when it needs and you get dramatically better results without dramatically better results without dramatically better results without touching the weights. Now alongside the

touching the weights. Now alongside the touching the weights. Now alongside the product update, Deep Mind published a product update, Deep Mind published a product update, Deep Mind published a paper introducing Althium which I think paper introducing Althium which I think

paper introducing Althium which I think is the most interesting update and is the most interesting update and is the most interesting update and nobody's talking about this. So this is nobody's talking about this. So this is nobody's talking about this. So this is a research agent built on top of deep

a research agent built on top of deep a research agent built on top of deep thing and it tells you where exactly the thing and it tells you where exactly the thing and it tells you where exactly the technology is heading. The Althia agent technology is heading. The Althia agent

technology is heading. The Althia agent works as a three-part loop generator, works as a three-part loop generator, works as a three-part loop generator, verifier and reviser. First verifier verifier and reviser. First verifier verifier and reviser. First verifier takes a research task or problem and

takes a research task or problem and takes a research task or problem and proposes a candidate solution. Then the proposes a candidate solution. Then the proposes a candidate solution. Then the verifier which is a separate natural verifier which is a separate natural

verifier which is a separate natural language mechanism checks the solution language mechanism checks the solution language mechanism checks the solution for flaws. We're not talking about just for flaws. We're not talking about just for flaws. We're not talking about just looking at does this look right but

looking at does this look right but looking at does this look right but actually probing the logic for gaps and actually probing the logic for gaps and actually probing the logic for gaps and hallucination. And then the last step of hallucination. And then the last step of

hallucination. And then the last step of this whole architecture is the revisor this whole architecture is the revisor this whole architecture is the revisor which basically patches minor issues or which basically patches minor issues or which basically patches minor issues or if the solution is critically flawed, it

if the solution is critically flawed, it if the solution is critically flawed, it triggers a complete restart back to the triggers a complete restart back to the triggers a complete restart back to the generator. Now there are two things that generator. Now there are two things that

generator. Now there are two things that I've personally found very interesting. I've personally found very interesting. I've personally found very interesting. So first, Althia uses Google search in So first, Althia uses Google search in So first, Althia uses Google search in web browsing to navigate real

[6:05]

web browsing to navigate real web browsing to navigate real mathematical literature. And this is mathematical literature. And this is mathematical literature. And this is huge because uh foundation models huge because uh foundation models

huge because uh foundation models hallucinate citations constantly in hallucinate citations constantly in hallucinate citations constantly in specialized domains. In this case, specialized domains. In this case, specialized domains. In this case, Althia is grounding its citation to a

Althia is grounding its citation to a Althia is grounding its citation to a specific reference. Now the second one specific reference. Now the second one specific reference. Now the second one is that it can admit where it cannot is that it can admit where it cannot

is that it can admit where it cannot when it cannot solve a problem. And this when it cannot solve a problem. And this when it cannot solve a problem. And this is huge because LLMs by design are very is huge because LLMs by design are very is huge because LLMs by design are very confident and they will hallucinate

confident and they will hallucinate confident and they will hallucinate results or it's going to make up stuff. results or it's going to make up stuff.

results or it's going to make up stuff. But they specifically trained this agent But they specifically trained this agent But they specifically trained this agent to admit when it cannot solve a problem.

to admit when it cannot solve a problem. to admit when it cannot solve a problem. Now the question is what did Althia Now the question is what did Althia Now the question is what did Althia actually achieved? We're looking at actually achieved? We're looking at

actually achieved? We're looking at 91.9% 91.9% 91.9% on advanced proof bench. The previous on advanced proof bench. The previous on advanced proof bench. The previous record was uh 65.7%.

record was uh 65.7%. record was uh 65.7%. And this is not just incremental And this is not just incremental And this is not just incremental improvement. Now here's the most improvement. Now here's the most

improvement. Now here's the most interesting bit. On the 29 out of 30 interesting bit. On the 29 out of 30 interesting bit. On the 29 out of 30 problems where Althia actually returned problems where Althia actually returned problems where Althia actually returned a solution, its conditional accuracy was

a solution, its conditional accuracy was a solution, its conditional accuracy was 98.3%. But here is the results that matters the But here is the results that matters the most. Althia outperformed standard deep most. Althia outperformed standard deep

most. Althia outperformed standard deep thinking thinking thinking compute scale they tested. So you're compute scale they tested. So you're compute scale they tested. So you're talking about the agent wrapper with

talking about the agent wrapper with talking about the agent wrapper with this generate verify revise loop is this generate verify revise loop is this generate verify revise loop is going to be more important than throwing going to be more important than throwing

going to be more important than throwing just raw compute at the base model which just raw compute at the base model which just raw compute at the base model which is significant. That means that the is significant. That means that the is significant. That means that the harness around the model itself is going

harness around the model itself is going harness around the model itself is going to be more important than just trying to to be more important than just trying to to be more important than just trying to increase the test time compute. Now we increase the test time compute. Now we

increase the test time compute. Now we see this pattern everywhere. So poetex see this pattern everywhere. So poetex see this pattern everywhere. So poetex beats raw deep think on RKGI2 that was beats raw deep think on RKGI2 that was beats raw deep think on RKGI2 that was the previous best cloud code with tools

the previous best cloud code with tools the previous best cloud code with tools performs better than the base OPUS or uh performs better than the base OPUS or uh performs better than the base OPUS or uh aet models. So I think the meta lesson aet models. So I think the meta lesson

aet models. So I think the meta lesson of this year is going to be very clear. of this year is going to be very clear. of this year is going to be very clear. The agent layer is where the real The agent layer is where the real The agent layer is where the real capability gains come from not just the

[8:05]

capability gains come from not just the capability gains come from not just the base model itself. to this point. base model itself. to this point.

base model itself. to this point. There's a very interesting blog post There's a very interesting blog post There's a very interesting blog post from Ken Bulock where he showed that from Ken Bulock where he showed that from Ken Bulock where he showed that just by changing the tool the models

just by changing the tool the models just by changing the tool the models have access to. You can easily get 5 to have access to. You can easily get 5 to have access to. You can easily get 5 to 8% performance improvement on the model 8% performance improvement on the model

8% performance improvement on the model itself which usually is not possible itself which usually is not possible itself which usually is not possible with even the update to a next with even the update to a next with even the update to a next generation model which is kind of a very

generation model which is kind of a very generation model which is kind of a very interesting point. I will probably cover interesting point. I will probably cover interesting point. I will probably cover that in another video. Now with Althium that in another video. Now with Althium

that in another video. Now with Althium and deep think Gemini 3 they also and deep think Gemini 3 they also and deep think Gemini 3 they also released two different interesting released two different interesting released two different interesting papers. The first one was towards

papers. The first one was towards papers. The first one was towards autonomous mathematics research and the autonomous mathematics research and the autonomous mathematics research and the second one is accelerating scientific second one is accelerating scientific

second one is accelerating scientific research with Gemini case studies and research with Gemini case studies and research with Gemini case studies and common techniques. In this they common techniques. In this they common techniques. In this they collaborated with domain experts on 18

collaborated with domain experts on 18 collaborated with domain experts on 18 research problems. We're not talking research problems. We're not talking research problems. We're not talking about just benchmark problems uh because about just benchmark problems uh because

about just benchmark problems uh because I think everybody talks about I think everybody talks about I think everybody talks about benchmaxing but these are real open benchmaxing but these are real open benchmaxing but these are real open research questions that humans has been

research questions that humans has been research questions that humans has been stuck on and they show that aentic stuck on and they show that aentic stuck on and they show that aentic systems based on Gemini 3 can actually systems based on Gemini 3 can actually

systems based on Gemini 3 can actually help solve some of these research help solve some of these research help solve some of these research questions questions questions which is fascinating because now we're

which is fascinating because now we're which is fascinating because now we're going to be able to do research with the going to be able to do research with the going to be able to do research with the help of these agentic systems. So let me help of these agentic systems. So let me

help of these agentic systems. So let me talk about three interesting ones. There talk about three interesting ones. There talk about three interesting ones. There are a total of 18 uh they are documented are a total of 18 uh they are documented are a total of 18 uh they are documented within this blog post and in the paper

within this blog post and in the paper within this blog post and in the paper if you are interested. Now the first one if you are interested. Now the first one if you are interested. Now the first one was that it was able to dis a decade old was that it was able to dis a decade old

was that it was able to dis a decade old conjecture. In the second example it conjecture. In the second example it conjecture. In the second example it crossed mathematical boundaries by crossed mathematical boundaries by crossed mathematical boundaries by pulling tools from an entirely unrelated

pulling tools from an entirely unrelated pulling tools from an entirely unrelated branch of mathematics to solve a problem branch of mathematics to solve a problem branch of mathematics to solve a problem that was unsolved. And in third case it that was unsolved. And in third case it

that was unsolved. And in third case it caught a critical error in cryptography. caught a critical error in cryptography. caught a critical error in cryptography. Well, none of them are my domain Well, none of them are my domain Well, none of them are my domain expertise, so I'm not going to even

expertise, so I'm not going to even expertise, so I'm not going to even pretend that I know anything about them, pretend that I know anything about them, pretend that I know anything about them, but they are in the blog post, which but they are in the blog post, which

but they are in the blog post, which I'll highly recommend to read if you're I'll highly recommend to read if you're I'll highly recommend to read if you're interested. Okay, so before somebody interested. Okay, so before somebody interested. Okay, so before somebody starts making a video claiming that AI

[10:05]

starts making a video claiming that AI starts making a video claiming that AI has solved mathematics, I actually want has solved mathematics, I actually want has solved mathematics, I actually want to highlight something very important to highlight something very important

to highlight something very important that unfortunately gets ignored in the that unfortunately gets ignored in the that unfortunately gets ignored in the headlines that we see. So in here they headlines that we see. So in here they headlines that we see. So in here they say that the results of this paper

say that the results of this paper say that the results of this paper should not be interpreted as suggesting should not be interpreted as suggesting should not be interpreted as suggesting that AI can consistently solve research that AI can consistently solve research

that AI can consistently solve research level mathematic questions. And this is level mathematic questions. And this is level mathematic questions. And this is very important because previously some very important because previously some very important because previously some of the frontier labs have made claims

of the frontier labs have made claims of the frontier labs have made claims about solving certain problem sets and about solving certain problem sets and about solving certain problem sets and they had to take them back. So here is they had to take them back. So here is

they had to take them back. So here is what exactly Google deep mind is saying. what exactly Google deep mind is saying. what exactly Google deep mind is saying. The first thing is that out of the 700 The first thing is that out of the 700 The first thing is that out of the 700 open problems that are on the ERDOS

open problems that are on the ERDOS open problems that are on the ERDOS problem set they filter it down to 200 problem set they filter it down to 200 problem set they filter it down to 200 AI generated responses which were graded AI generated responses which were graded

AI generated responses which were graded by humans. Now out of those 200 63 were by humans. Now out of those 200 63 were by humans. Now out of those 200 63 were technically correct four were technically correct four were technically correct four were autonomously solved. We are looking at a

autonomously solved. We are looking at a autonomously solved. We are looking at a success rate of about 6.5% success rate of about 6.5% success rate of about 6.5% on research grade problems which might on research grade problems which might

on research grade problems which might look small but this is significant look small but this is significant look small but this is significant success rate compared to some of the success rate compared to some of the success rate compared to some of the earlier models that we have seen. Now uh

earlier models that we have seen. Now uh earlier models that we have seen. Now uh Deepoint also created a tonomy of u how Deepoint also created a tonomy of u how Deepoint also created a tonomy of u how they are thinking about solving research they are thinking about solving research

they are thinking about solving research problems with AI. So there are four problems with AI. So there are four problems with AI. So there are four different levels for solution proposed different levels for solution proposed different levels for solution proposed by AI systems. So level zero is uh

by AI systems. So level zero is uh by AI systems. So level zero is uh reproducing known results and this has reproducing known results and this has reproducing known results and this has happened with some of the open AI happened with some of the open AI

happened with some of the open AI models. Level one is novel but models. Level one is novel but models. Level one is novel but incremental. Level two is what they're incremental. Level two is what they're incremental. Level two is what they're calling publishable quality. Level three

calling publishable quality. Level three calling publishable quality. Level three is major advances. And level four is is major advances. And level four is is major advances. And level four is what they're calling landmark what they're calling landmark

what they're calling landmark breakthrough. They explicitly stated breakthrough. They explicitly stated breakthrough. They explicitly stated that they do not claim any level three that they do not claim any level three that they do not claim any level three or level four results. Everything they

or level four results. Everything they or level four results. Everything they published is level zero through level published is level zero through level published is level zero through level two. And this is refreshingly honest. In two. And this is refreshingly honest. In

[12:07]

two. And this is refreshingly honest. In a field where companies routinely claim a field where companies routinely claim a field where companies routinely claim breakthroughs and revolution by breakthroughs and revolution by breakthroughs and revolution by incremental improvements, deep mind

incremental improvements, deep mind incremental improvements, deep mind said, "We are at a publishable quality. said, "We are at a publishable quality.

said, "We are at a publishable quality. We are not at a major advance yet." We are not at a major advance yet." We are not at a major advance yet." Now before this release, Google actually Now before this release, Google actually Now before this release, Google actually ran a real world experiment. They offer

ran a real world experiment. They offer ran a real world experiment. They offer stock 2026 um conference author a stock 2026 um conference author a stock 2026 um conference author a presubmission feedback generated by an presubmission feedback generated by an

presubmission feedback generated by an earlier version of deep think and the earlier version of deep think and the earlier version of deep think and the tool reviewed papers for mathematical tool reviewed papers for mathematical tool reviewed papers for mathematical correctness identified calculation

correctness identified calculation correctness identified calculation errors incorrectly inequities errors incorrectly inequities errors incorrectly inequities applications logical gaps in the proofs applications logical gaps in the proofs

applications logical gaps in the proofs and real stuff that makes breaks a paper and real stuff that makes breaks a paper and real stuff that makes breaks a paper which was I think a very interesting which was I think a very interesting which was I think a very interesting application of this technology and to be

application of this technology and to be application of this technology and to be honest this is probably more important honest this is probably more important honest this is probably more important to me than any benchmarks that we are to me than any benchmarks that we are

to me than any benchmarks that we are seeing we are looking at an AI tool that seeing we are looking at an AI tool that seeing we are looking at an AI tool that is already being integrated into paper is already being integrated into paper is already being integrated into paper reviews at the top academic conferences.

reviews at the top academic conferences. reviews at the top academic conferences. We're not talking about replacing We're not talking about replacing We're not talking about replacing reviewers but rather helping authors reviewers but rather helping authors

reviewers but rather helping authors catch errors before submission. Okay, so catch errors before submission. Okay, so catch errors before submission. Okay, so what exactly are the takeaways from this what exactly are the takeaways from this what exactly are the takeaways from this new release? I think there are three

new release? I think there are three new release? I think there are three now. The first one is that inference now. The first one is that inference now. The first one is that inference time compute scaling works and it's time compute scaling works and it's

time compute scaling works and it's getting dramatically more efficient. We getting dramatically more efficient. We getting dramatically more efficient. We talking about 100x reduction in compute talking about 100x reduction in compute talking about 100x reduction in compute for the same quality in 6 months. So

for the same quality in 6 months. So for the same quality in 6 months. So here we are not talking about bigger here we are not talking about bigger here we are not talking about bigger models equal better. Uh I think this is models equal better. Uh I think this is

models equal better. Uh I think this is smarter thinking equals better within smarter thinking equals better within smarter thinking equals better within agentic loop which is fundamentally agentic loop which is fundamentally agentic loop which is fundamentally different scaling paradigm than what we

different scaling paradigm than what we different scaling paradigm than what we have been living in the past few years. have been living in the past few years.

have been living in the past few years. Second is going to be uh the importance Second is going to be uh the importance Second is going to be uh the importance of harness and agent being better than of harness and agent being better than of harness and agent being better than the raw model. If you're building any

the raw model. If you're building any the raw model. If you're building any agentic systems, the orchestration layer agentic systems, the orchestration layer agentic systems, the orchestration layer is going to be the most important one is going to be the most important one

is going to be the most important one because this is where I think we're because this is where I think we're because this is where I think we're going to get the most gains other than going to get the most gains other than going to get the most gains other than retraining the models. And the third is

retraining the models. And the third is retraining the models. And the third is that we are seeing early glimpse of AI that we are seeing early glimpse of AI that we are seeing early glimpse of AI research collaborators and not just a research collaborators and not just a

[14:07]

research collaborators and not just a coding agent that can generate code for coding agent that can generate code for coding agent that can generate code for you, but an AI system that can actually you, but an AI system that can actually you, but an AI system that can actually do research and solve hard problems. Now

do research and solve hard problems. Now do research and solve hard problems. Now these are very early days right as we these are very early days right as we these are very early days right as we saw we're looking at 6.5% success rate saw we're looking at 6.5% success rate

saw we're looking at 6.5% success rate on the hardest problems but still this on the hardest problems but still this on the hardest problems but still this is humbling for a system that is is humbling for a system that is is humbling for a system that is supposed to be just a next token

supposed to be just a next token supposed to be just a next token generator and just like coding system I generator and just like coding system I generator and just like coding system I think these are going to be early signs think these are going to be early signs

think these are going to be early signs of a junior capable researcher that can of a junior capable researcher that can of a junior capable researcher that can help you with some tasks so really help you with some tasks so really help you with some tasks so really exciting times and I'm actually excited

exciting times and I'm actually excited exciting times and I'm actually excited for where this goes beyond just the for where this goes beyond just the for where this goes beyond just the benchmarks and normal demos that we benchmarks and normal demos that we

benchmarks and normal demos that we create. Now, this is very exciting create. Now, this is very exciting create. Now, this is very exciting stuff. One thing, don't try Gemini 3 stuff. One thing, don't try Gemini 3 stuff. One thing, don't try Gemini 3 deep think on normal oneshot prompts.

deep think on normal oneshot prompts. deep think on normal oneshot prompts. This is probably not going to impress This is probably not going to impress This is probably not going to impress you, but if you have hard technical you, but if you have hard technical

you, but if you have hard technical problems, I highly recommend to put it problems, I highly recommend to put it problems, I highly recommend to put it through it and you're going to be through it and you're going to be through it and you're going to be surprised. Anyways, I hope you found

surprised. Anyways, I hope you found surprised. Anyways, I hope you found this video useful. Thanks for watching this video useful. Thanks for watching this video useful. Thanks for watching and as always, see you in the next one.

