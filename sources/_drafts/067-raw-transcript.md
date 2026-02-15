# Raw Transcript: Learn 90% Of Claude Code Agent Teams in 22 Minutes (Opus 4.6)

[0:00]

Hello legends. In this video, I'm going Hello legends. In this video, I'm going to turn you into a master of claude code to turn you into a master of claude code to turn you into a master of claude code agent teams. So, as you know, we agent teams. So, as you know, we

agent teams. So, as you know, we recently got the Opus 4.6 model and with recently got the Opus 4.6 model and with recently got the Opus 4.6 model and with it, we got a brand new feature called it, we got a brand new feature called it, we got a brand new feature called agent teams. We're going to start with

agent teams. We're going to start with agent teams. We're going to start with an overview of what agent teams is and an overview of what agent teams is and an overview of what agent teams is and how it's different to using sub aents or how it's different to using sub aents or

how it's different to using sub aents or even just a default mode of claude code. even just a default mode of claude code. even just a default mode of claude code. We'll then make sure that you're We'll then make sure that you're We'll then make sure that you're correctly set up, including that you

correctly set up, including that you correctly set up, including that you have the latest version of claude code, have the latest version of claude code, have the latest version of claude code, so you can access all the models, that so you can access all the models, that

so you can access all the models, that you have all the correct settings and you have all the correct settings and you have all the correct settings and configurations, so you can actually configurations, so you can actually configurations, so you can actually access the agent team mode. And then I'm

access the agent team mode. And then I'm access the agent team mode. And then I'm going to show you something called going to show you something called going to show you something called TeamUx, which is an easier way for you TeamUx, which is an easier way for you

TeamUx, which is an easier way for you to actually manage and interact with to actually manage and interact with to actually manage and interact with your different agents on a team. We'll your different agents on a team. We'll your different agents on a team. We'll then take a look at session management

then take a look at session management then take a look at session management because it's a very specific way to because it's a very specific way to because it's a very specific way to actually spool up your agent team to actually spool up your agent team to

actually spool up your agent team to then manage and interact with it. And then manage and interact with it. And then manage and interact with it. And that's where that T-max thing comes into that's where that T-max thing comes into that's where that T-max thing comes into play as well. And then finally, a

play as well. And then finally, a play as well. And then finally, a specific way to actually shut down the specific way to actually shut down the specific way to actually shut down the team, then close all the tasks that team, then close all the tasks that

team, then close all the tasks that you're working on. And then at the end you're working on. And then at the end you're working on. And then at the end of the video, I'm going to show you how of the video, I'm going to show you how of the video, I'm going to show you how to use the claw code skills to actually

to use the claw code skills to actually to use the claw code skills to actually make it easier for you to manage future make it easier for you to manage future make it easier for you to manage future teams. So now that we have agent teams, teams. So now that we have agent teams,

teams. So now that we have agent teams, there's actually three different ways there's actually three different ways there's actually three different ways that you can use claude code. The that you can use claude code. The that you can use claude code. The original way, the very first way to use

original way, the very first way to use original way, the very first way to use claude code was in the default mode. So claude code was in the default mode. So claude code was in the default mode. So the default mode is where you open up a the default mode is where you open up a

the default mode is where you open up a new terminal, you launch claude code, new terminal, you launch claude code, new terminal, you launch claude code, and you have a conversation for one of and you have a conversation for one of and you have a conversation for one of the claude models. You can do things

the claude models. You can do things the claude models. You can do things like write code, debug code, do web like write code, debug code, do web like write code, debug code, do web search. So now technically speaking, search. So now technically speaking,

search. So now technically speaking, everything you can do in agent team mode everything you can do in agent team mode everything you can do in agent team mode and sub agent mode, you can also do on a and sub agent mode, you can also do on a and sub agent mode, you can also do on a default mode. The biggest difference is

default mode. The biggest difference is default mode. The biggest difference is in how the session is managed. So in in how the session is managed. So in in how the session is managed. So in default mode, you have one session. In default mode, you have one session. In

default mode, you have one session. In sub agent mode, you have one session, sub agent mode, you have one session, sub agent mode, you have one session, but then in agent team mode, each of but then in agent team mode, each of but then in agent team mode, each of these little guys actually has their own

these little guys actually has their own these little guys actually has their own session. And this is incredibly session. And this is incredibly session. And this is incredibly important because when you're using important because when you're using

important because when you're using something like default mode, you already something like default mode, you already something like default mode, you already know this, right? There is a certain know this, right? There is a certain know this, right? There is a certain amount of tokens that you can consume

amount of tokens that you can consume amount of tokens that you can consume for that specific session before the for that specific session before the for that specific session before the model starts to hallucinate, before it model starts to hallucinate, before it

model starts to hallucinate, before it starts to lose track of what you were starts to lose track of what you were starts to lose track of what you were speaking about earlier in a speaking about earlier in a speaking about earlier in a conversation. And that's why people have

conversation. And that's why people have conversation. And that's why people have all these like tips and tricks about all these like tips and tricks about all these like tips and tricks about having dedicated MD files, skill files, having dedicated MD files, skill files,

having dedicated MD files, skill files, memory files, so you can kind of memory files, so you can kind of memory files, so you can kind of maintain the context across longer runs, maintain the context across longer runs, maintain the context across longer runs, longer sessions where there's more and

longer sessions where there's more and longer sessions where there's more and more tokens going into the bag. So for more tokens going into the bag. So for more tokens going into the bag. So for default mode, what actually happens is default mode, what actually happens is

[2:00]

default mode, what actually happens is if you give like a really big code base, if you give like a really big code base, if you give like a really big code base, it's very difficult for this agent to be it's very difficult for this agent to be it's very difficult for this agent to be able to look at all the different points

able to look at all the different points able to look at all the different points of that codebase. And therefore what of that codebase. And therefore what of that codebase. And therefore what anthropic says is that these models tend anthropic says is that these models tend

anthropic says is that these models tend to gravitate towards one specific area to gravitate towards one specific area to gravitate towards one specific area and kind of get like tunnel vision and and kind of get like tunnel vision and and kind of get like tunnel vision and only focus on that one area. So this is

only focus on that one area. So this is only focus on that one area. So this is now starting to like tell us when we now starting to like tell us when we now starting to like tell us when we should be using these different modes.

should be using these different modes. should be using these different modes. So for default mode now that we have So for default mode now that we have So for default mode now that we have these other two modes really this is these other two modes really this is

these other two modes really this is like your general like uh system admin like your general like uh system admin like your general like uh system admin panel. You can kind of come into here.

panel. You can kind of come into here. panel. You can kind of come into here. Really the main use case for this now is Really the main use case for this now is Really the main use case for this now is to choose your model that you're using, to choose your model that you're using,

to choose your model that you're using, figure out what skills you have, set up figure out what skills you have, set up figure out what skills you have, set up the project, figure out like what sub the project, figure out like what sub the project, figure out like what sub aents you want to have, what your team's

aents you want to have, what your team's aents you want to have, what your team's going to look like and kind of use it as going to look like and kind of use it as going to look like and kind of use it as a control panel. So now we come to sub a control panel. So now we come to sub

a control panel. So now we come to sub agent mode. What's the use case here? agent mode. What's the use case here? agent mode. What's the use case here? Imagine you have a security company and Imagine you have a security company and Imagine you have a security company and you have a control room in a very big

you have a control room in a very big you have a control room in a very big tower and everyone's inside that control tower and everyone's inside that control tower and everyone's inside that control room and you have these monitors on a room and you have these monitors on a

room and you have these monitors on a wall and you're kind of watching what wall and you're kind of watching what wall and you're kind of watching what each monitor is showing and there's like each monitor is showing and there's like each monitor is showing and there's like a breach in one of the rooms. Well, what

a breach in one of the rooms. Well, what a breach in one of the rooms. Well, what you do from the terminal here, from this you do from the terminal here, from this you do from the terminal here, from this thing, is you take one of these agents thing, is you take one of these agents

thing, is you take one of these agents and you say, "Hey, agent, you go down to and you say, "Hey, agent, you go down to and you say, "Hey, agent, you go down to the third floor into that fifth door and the third floor into that fifth door and the third floor into that fifth door and go into this room and then investigate

go into this room and then investigate go into this room and then investigate this issue that we see on the screen." this issue that we see on the screen." this issue that we see on the screen." The agent will then go away, go down the The agent will then go away, go down the

The agent will then go away, go down the elevator, take the stairs, turn left, elevator, take the stairs, turn left, elevator, take the stairs, turn left, speak to five people, go into that room, speak to five people, go into that room, speak to five people, go into that room, figure out the issue, come back,

figure out the issue, come back, figure out the issue, come back, elevator, stairs, then come back to the elevator, stairs, then come back to the elevator, stairs, then come back to the control room, and just give you the control room, and just give you the

control room, and just give you the summary. Okay, I fixed it. you know, summary. Okay, I fixed it. you know, summary. Okay, I fixed it. you know, Bart was running around and I told him Bart was running around and I told him Bart was running around and I told him to sit down and all the additional like

to sit down and all the additional like to sit down and all the additional like the many steps in between completing the many steps in between completing the many steps in between completing that task, we don't actually get back in that task, we don't actually get back in

that task, we don't actually get back in that control room. So, the value here is that control room. So, the value here is that control room. So, the value here is if you have something like a codebase if you have something like a codebase if you have something like a codebase and you only have an authentication

and you only have an authentication and you only have an authentication method using password and email, in this method using password and email, in this method using password and email, in this case, you might spool up a sub agent to case, you might spool up a sub agent to

case, you might spool up a sub agent to just go away and add the additional just go away and add the additional just go away and add the additional functionality of using Google to sign functionality of using Google to sign functionality of using Google to sign into your app as well. So, like we said

into your app as well. So, like we said into your app as well. So, like we said before, we still only have one main before, we still only have one main before, we still only have one main session over here. So then the value of session over here. So then the value of

session over here. So then the value of this is the way that you actually this is the way that you actually this is the way that you actually conserve the tokens for your primary conserve the tokens for your primary conserve the tokens for your primary session because you know these models

session because you know these models session because you know these models don't have an infinity capacity to have don't have an infinity capacity to have don't have an infinity capacity to have these tokens. That's the reason why these tokens. That's the reason why

[4:00]

these tokens. That's the reason why these sub agents actually go away and these sub agents actually go away and these sub agents actually go away and instead of giving you all that feedback instead of giving you all that feedback instead of giving you all that feedback that he turned left, he turned right

that he turned left, he turned right that he turned left, he turned right spoke to five people. What did they say? spoke to five people. What did they say?

spoke to five people. What did they say? He just gives you the ultimate output He just gives you the ultimate output He just gives you the ultimate output which is I went to this place, I which is I went to this place, I which is I went to this place, I completed the task and it's done or

completed the task and it's done or completed the task and it's done or actually I went there and I couldn't actually I went there and I couldn't actually I went there and I couldn't complete it. Now we have a new issue.

complete it. Now we have a new issue. complete it. Now we have a new issue. Gives it summary back into the main Gives it summary back into the main Gives it summary back into the main context to preserve the overall context context to preserve the overall context

context to preserve the overall context of this session. That's why these sub of this session. That's why these sub of this session. That's why these sub agents are different in that way. So now agents are different in that way. So now agents are different in that way. So now when it comes to agent team mode, so

when it comes to agent team mode, so when it comes to agent team mode, so let's imagine you actually have this big let's imagine you actually have this big let's imagine you actually have this big tower, right, of of like 10 levels and tower, right, of of like 10 levels and

tower, right, of of like 10 levels and there's 10 rooms per level. Agent teams there's 10 rooms per level. Agent teams there's 10 rooms per level. Agent teams mode is like you are the security mode is like you are the security mode is like you are the security company coming into this tower and you

company coming into this tower and you company coming into this tower and you have a task from the terminal which is have a task from the terminal which is have a task from the terminal which is go into this building and then like do go into this building and then like do

go into this building and then like do the do the full security for this the do the full security for this the do the full security for this building. We have an event tonight. We building. We have an event tonight. We building. We have an event tonight. We need to fully secure every single floor,

need to fully secure every single floor, need to fully secure every single floor, all the ins and outs. When people come all the ins and outs. When people come all the ins and outs. When people come in, we have to scan there, make sure in, we have to scan there, make sure

in, we have to scan there, make sure everything's good. we need to fully run everything's good. we need to fully run everything's good. we need to fully run the security operation. So then in any the security operation. So then in any the security operation. So then in any security team, you have the team leader

security team, you have the team leader security team, you have the team leader who understands the assignment and then who understands the assignment and then who understands the assignment and then delegates the work. The team leader delegates the work. The team leader

delegates the work. The team leader figures out the plan which is therefore figures out the plan which is therefore figures out the plan which is therefore like the the plan for the actual session like the the plan for the actual session like the the plan for the actual session and then the prompts that he gives to

and then the prompts that he gives to and then the prompts that he gives to each agent and the prompt is like the each agent and the prompt is like the each agent and the prompt is like the instruction that he gives and this instruction that he gives and this

instruction that he gives and this person might have to go to the left side person might have to go to the left side person might have to go to the left side and do the first three floors and then and do the first three floors and then and do the first three floors and then this person might have to go to the

this person might have to go to the this person might have to go to the right side and do the next three floors right side and do the next three floors right side and do the next three floors and each person has their own delegated and each person has their own delegated

and each person has their own delegated work. Now, the interesting thing is that work. Now, the interesting thing is that work. Now, the interesting thing is that in terms of like having this security in terms of like having this security in terms of like having this security team, what you need to do is you have to

team, what you need to do is you have to team, what you need to do is you have to be able to get your walkie-talkie and as be able to get your walkie-talkie and as be able to get your walkie-talkie and as the team leader say, "Hey guys, is the team leader say, "Hey guys, is

the team leader say, "Hey guys, is everyone at the location? Cool. We can everyone at the location? Cool. We can everyone at the location? Cool. We can start the event." And when you're start the event." And when you're start the event." And when you're actually at these events, you might say,

actually at these events, you might say, actually at these events, you might say, "Hey, I'm on the floor six. There's "Hey, I'm on the floor six. There's "Hey, I'm on the floor six. There's someone that's doing something bad. He's someone that's doing something bad. He's

someone that's doing something bad. He's coming down the floors. So, hey teammate coming down the floors. So, hey teammate coming down the floors. So, hey teammate A, be ready for this next person that's A, be ready for this next person that's A, be ready for this next person that's going to come into your area very soon."

going to come into your area very soon." going to come into your area very soon." And that communication actually helps And that communication actually helps And that communication actually helps you be more effective in the overall job you be more effective in the overall job

you be more effective in the overall job of security for this building because of security for this building because of security for this building because you can communicate and say there's you can communicate and say there's you can communicate and say there's there's a specific issue happening in

there's a specific issue happening in there's a specific issue happening in this area. Please be notified, please this area. Please be notified, please this area. Please be notified, please prepare for or like come and help me fix prepare for or like come and help me fix

prepare for or like come and help me fix this. So just a few moments ago, I this. So just a few moments ago, I this. So just a few moments ago, I mentioned how when you have default mentioned how when you have default mentioned how when you have default mode, you only have one agent. And the

mode, you only have one agent. And the mode, you only have one agent. And the one of the biggest issues with agents in one of the biggest issues with agents in one of the biggest issues with agents in general or LLM in general is that in a general or LLM in general is that in a

[6:01]

general or LLM in general is that in a single session, they typically gravitate single session, they typically gravitate single session, they typically gravitate towards one specific area. And once towards one specific area. And once towards one specific area. And once they're there, it's very hard for them

they're there, it's very hard for them they're there, it's very hard for them to kind of come back out of that area. to kind of come back out of that area.

to kind of come back out of that area. Which is why you might notice that you Which is why you might notice that you Which is why you might notice that you have like that yes man syndrome when have like that yes man syndrome when have like that yes man syndrome when you're in something like chat GBT or

you're in something like chat GBT or you're in something like chat GBT or claude where whatever idea you say claude where whatever idea you say claude where whatever idea you say typically get echoed back to you and typically get echoed back to you and

typically get echoed back to you and then it's very difficult for you to get then it's very difficult for you to get then it's very difficult for you to get new ideas outside of that original idea.

new ideas outside of that original idea. new ideas outside of that original idea. So the advantage of teams is that you So the advantage of teams is that you So the advantage of teams is that you still get the exact same thing. Like still get the exact same thing. Like

still get the exact same thing. Like each agent that you have typically each agent that you have typically each agent that you have typically gravitates towards one specific area, gravitates towards one specific area, gravitates towards one specific area, but since you have multiple like

but since you have multiple like but since you have multiple like possibility for multiple different possibility for multiple different possibility for multiple different agents to spool up for that one problem agents to spool up for that one problem

agents to spool up for that one problem that you want to do, for that one code that you want to do, for that one code that you want to do, for that one code base that you want to investigate, for base that you want to investigate, for base that you want to investigate, for that one feature that you want to add,

that one feature that you want to add, that one feature that you want to add, you can actually deploy each of these you can actually deploy each of these you can actually deploy each of these agents and tell them you look at this agents and tell them you look at this

agents and tell them you look at this from the left side, you look at this from the left side, you look at this from the left side, you look at this from the right side, and you go upstairs from the right side, and you go upstairs from the right side, and you go upstairs and you look at it from the top down.

and you look at it from the top down. and you look at it from the top down. And the cool thing is you don't actually And the cool thing is you don't actually And the cool thing is you don't actually have to manage all those different like have to manage all those different like

have to manage all those different like points of view and context because the points of view and context because the points of view and context because the team leader takes your problem, team leader takes your problem, team leader takes your problem, understands it, and then spools up and

understands it, and then spools up and understands it, and then spools up and gives the appropriate context to each of gives the appropriate context to each of gives the appropriate context to each of these sub agents so that on the outset these sub agents so that on the outset

these sub agents so that on the outset you actually get the 360deree report you actually get the 360deree report you actually get the 360deree report returned to you. So now at this stage returned to you. So now at this stage returned to you. So now at this stage we've got a pretty good idea of the

we've got a pretty good idea of the we've got a pretty good idea of the three different modes for clawed code three different modes for clawed code three different modes for clawed code and we're beginning to understand the and we're beginning to understand the

and we're beginning to understand the strengths and weaknesses of each of strengths and weaknesses of each of strengths and weaknesses of each of those different modes. So now let's go those different modes. So now let's go those different modes. So now let's go into the setup and just make sure that

into the setup and just make sure that into the setup and just make sure that our environment is ready to use all the our environment is ready to use all the our environment is ready to use all the new features. So the first thing we want new features. So the first thing we want

new features. So the first thing we want to do is make sure we have the latest to do is make sure we have the latest to do is make sure we have the latest version of Claude installed on our version of Claude installed on our version of Claude installed on our system. To do that, let's just open up a

system. To do that, let's just open up a system. To do that, let's just open up a terminal and type in claude update and terminal and type in claude update and terminal and type in claude update and hit enter. Claude will then check for hit enter. Claude will then check for

hit enter. Claude will then check for updates and then it'll either update for updates and then it'll either update for updates and then it'll either update for you or it will just confirm that you are you or it will just confirm that you are you or it will just confirm that you are on the latest version. So now for the

on the latest version. So now for the on the latest version. So now for the T-max and configuration, I asked Chat T-max and configuration, I asked Chat T-max and configuration, I asked Chat GPT to help me with the instructions of GPT to help me with the instructions of

GPT to help me with the instructions of how to set this up. So T-Max is just a how to set this up. So T-Max is just a how to set this up. So T-Max is just a way that you can create separate windows way that you can create separate windows way that you can create separate windows in your terminal so that you can

in your terminal so that you can in your terminal so that you can actually view each of those independent actually view each of those independent actually view each of those independent agents. Imagine you're running agents. Imagine you're running

agents. Imagine you're running interviews and you have five people in interviews and you have five people in interviews and you have five people in the same room speaking to at the exact the same room speaking to at the exact the same room speaking to at the exact same time. You're trying to speak with

same time. You're trying to speak with same time. You're trying to speak with each of them and interview them. It's each of them and interview them. It's each of them and interview them. It's just impossible. There's too much noise, just impossible. There's too much noise,

just impossible. There's too much noise, too many conversations. So, the better too many conversations. So, the better too many conversations. So, the better way to do this is to get a separate room way to do this is to get a separate room way to do this is to get a separate room for each person. So, you can kind of go

for each person. So, you can kind of go for each person. So, you can kind of go in there and just peacefully be able to in there and just peacefully be able to in there and just peacefully be able to say, "What are you working on? What are say, "What are you working on? What are

say, "What are you working on? What are you doing? Here's the updated you doing? Here's the updated you doing? Here's the updated instructions." So, T-Mox is like setting instructions." So, T-Mox is like setting instructions." So, T-Mox is like setting up rooms for each of your agents. So at

[8:04]

up rooms for each of your agents. So at up rooms for each of your agents. So at any stage you can just take a screenshot any stage you can just take a screenshot any stage you can just take a screenshot of the screen and then send across to of the screen and then send across to

of the screen and then send across to your chat GBT or claude and ask it to your chat GBT or claude and ask it to your chat GBT or claude and ask it to help with specific instructions for your help with specific instructions for your help with specific instructions for your setup. But for example for me I'm just

setup. But for example for me I'm just setup. But for example for me I'm just going to take this I'm on Mac. So by the going to take this I'm on Mac. So by the going to take this I'm on Mac. So by the way Timox is not going to work in way Timox is not going to work in

way Timox is not going to work in something like VS Code or cursor. It has something like VS Code or cursor. It has something like VS Code or cursor. It has to be in your core terminal. So I'm to be in your core terminal. So I'm to be in your core terminal. So I'm going to paste that command into here.

going to paste that command into here. going to paste that command into here. So I already had T-Max installed. So the So I already had T-Max installed. So the So I already had T-Max installed. So the process was very quick for me. But this process was very quick for me. But this

process was very quick for me. But this will typically take like a minute or two will typically take like a minute or two will typically take like a minute or two to just install on your machine. So now to just install on your machine. So now to just install on your machine. So now with T-Max installed there's actually

with T-Max installed there's actually with T-Max installed there's actually two different ways that you can manage two different ways that you can manage two different ways that you can manage agents. The first is that you have this agents. The first is that you have this

agents. The first is that you have this in process which is where you have that in process which is where you have that in process which is where you have that one terminal and then all the agents are one terminal and then all the agents are one terminal and then all the agents are literally speaking in that one terminal

literally speaking in that one terminal literally speaking in that one terminal like having that one room and it's so like having that one room and it's so like having that one room and it's so noisy. Well, the second way is to have noisy. Well, the second way is to have

noisy. Well, the second way is to have these split panes and a split panes is these split panes and a split panes is these split panes and a split panes is what you need t-mucks for which is what you need t-mucks for which is what you need t-mucks for which is having all those separate rooms. So, we

having all those separate rooms. So, we having all those separate rooms. So, we just need to add that setting into our just need to add that setting into our just need to add that setting into our configuration file which is going to be configuration file which is going to be

configuration file which is going to be this t-m split panes to true and in that this t-m split panes to true and in that this t-m split panes to true and in that same file we're also going to be sending same file we're also going to be sending same file we're also going to be sending claude code experimental agents to one

claude code experimental agents to one claude code experimental agents to one which is just the other configuration which is just the other configuration which is just the other configuration that we need to enable agent teams. So, that we need to enable agent teams. So,

that we need to enable agent teams. So, we're just going to copy this entire we're just going to copy this entire we're just going to copy this entire command and then paste it into the command and then paste it into the command and then paste it into the terminal. We're going to hit enter. So,

terminal. We're going to hit enter. So, terminal. We're going to hit enter. So, now we've just updated the settings.json now we've just updated the settings.json now we've just updated the settings.json to enable agent teams and also give to enable agent teams and also give

to enable agent teams and also give separate rooms to each of those teams. A separate rooms to each of those teams. A separate rooms to each of those teams. A quick note here that this is actually quick note here that this is actually quick note here that this is actually going to be your global configuration.

going to be your global configuration. going to be your global configuration. I've decided to do this because I I've decided to do this because I I've decided to do this because I actually just want to have agent teams actually just want to have agent teams

actually just want to have agent teams ready across all of my sessions with ready across all of my sessions with ready across all of my sessions with Claude. So, instead of me just like Claude. So, instead of me just like Claude. So, instead of me just like closing my terminal, starting a new one,

closing my terminal, starting a new one, closing my terminal, starting a new one, having to change the configuration having to change the configuration having to change the configuration again, I've just done it globally for again, I've just done it globally for

again, I've just done it globally for all of my sessions. So now before we all of my sessions. So now before we all of my sessions. So now before we launch Claude code, the first thing we launch Claude code, the first thing we launch Claude code, the first thing we need to do is start a T-max session. So

need to do is start a T-max session. So need to do is start a T-max session. So I'm just going to copy this command. Now I'm just going to copy this command. Now I'm just going to copy this command. Now once again, don't just start a new once again, don't just start a new

once again, don't just start a new claude session by typing the claude claude session by typing the claude claude session by typing the claude command. We first need to start a new command. We first need to start a new command. We first need to start a new T-mark session. So we're going to paste

T-mark session. So we're going to paste T-mark session. So we're going to paste this command into here. Hit enter. And this command into here. Hit enter. And this command into here. Hit enter. And now we are prepared to create all those now we are prepared to create all those

now we are prepared to create all those different rooms for agents. So now we different rooms for agents. So now we different rooms for agents. So now we can come back and start Claude. I'm just can come back and start Claude. I'm just can come back and start Claude. I'm just going to start mine with the dangerously

going to start mine with the dangerously going to start mine with the dangerously skip permissions. Let's accept this skip permissions. Let's accept this skip permissions. Let's accept this security warning. And now we are logged security warning. And now we are logged

security warning. And now we are logged into Claude. So, at this stage, we've into Claude. So, at this stage, we've into Claude. So, at this stage, we've done the overview and we've done the done the overview and we've done the done the overview and we've done the setup. Now, let's take a look at how to

setup. Now, let's take a look at how to setup. Now, let's take a look at how to manage sessions. So, the first thing we manage sessions. So, the first thing we manage sessions. So, the first thing we want to do is actually go into our want to do is actually go into our

want to do is actually go into our models and make sure we're using the models and make sure we're using the models and make sure we're using the correct model. So, we have the OP 4.6 correct model. So, we have the OP 4.6 correct model. So, we have the OP 4.6 model. And I'm pretty sure this first

[10:06]

model. And I'm pretty sure this first model. And I'm pretty sure this first one here is the 200,000 token context one here is the 200,000 token context one here is the 200,000 token context model. Then you have the second one, model. Then you have the second one,

model. Then you have the second one, which is the 1 million token context which is the 1 million token context which is the 1 million token context model. So, with that 1 million token model. So, with that 1 million token model. So, with that 1 million token context model, what's really happening

context model, what's really happening context model, what's really happening is that for the first 200,000 tokens, is that for the first 200,000 tokens, is that for the first 200,000 tokens, you're technically using that original you're technically using that original

you're technically using that original model. you're getting charged the model. you're getting charged the model. you're getting charged the regular rates, but then for anything regular rates, but then for anything regular rates, but then for anything above 200,000 tokens, you get the

above 200,000 tokens, you get the above 200,000 tokens, you get the premium pricing, which is the $10 and premium pricing, which is the $10 and premium pricing, which is the $10 and $3750 per million input output tokens.

$3750 per million input output tokens. $3750 per million input output tokens. And then for Opus, you also have the And then for Opus, you also have the And then for Opus, you also have the effort toggle where if you click left effort toggle where if you click left

effort toggle where if you click left and right, you can actually go from low and right, you can actually go from low and right, you can actually go from low effort to medium to high. And then we effort to medium to high. And then we effort to medium to high. And then we have the explanation of all the effort

have the explanation of all the effort have the explanation of all the effort levels here. So low is the most levels here. So low is the most levels here. So low is the most efficient and it has some capability efficient and it has some capability

efficient and it has some capability reduction. So it's going to be a little reduction. So it's going to be a little reduction. So it's going to be a little bit like not as smart or not as capable, bit like not as smart or not as capable, bit like not as smart or not as capable, not as good. Then you have medium for a

not as good. Then you have medium for a not as good. Then you have medium for a balanced approach and moderate token balanced approach and moderate token balanced approach and moderate token savings. And then high which is the savings. And then high which is the

savings. And then high which is the basically like the best for complex basically like the best for complex basically like the best for complex reasoning, difficult coding problems.

reasoning, difficult coding problems. reasoning, difficult coding problems. And then for absolute maximum And then for absolute maximum And then for absolute maximum capability, it's only for the Opus 4.6 capability, it's only for the Opus 4.6

capability, it's only for the Opus 4.6 model. And this is like putting the foot model. And this is like putting the foot model. And this is like putting the foot to the floor and just like letting go of to the floor and just like letting go of to the floor and just like letting go of the steering wheel and then like let's

the steering wheel and then like let's the steering wheel and then like let's see what happens. So my recommendation see what happens. So my recommendation see what happens. So my recommendation is just to start with the regular Opus is just to start with the regular Opus

is just to start with the regular Opus model and go all the way to low effort. model and go all the way to low effort. model and go all the way to low effort. Then as you run into like speed bumps Then as you run into like speed bumps Then as you run into like speed bumps and issues or as you figure out when

and issues or as you figure out when and issues or as you figure out when you're deploying agent teams which model you're deploying agent teams which model you're deploying agent teams which model is better to use, you can just toggle up is better to use, you can just toggle up

is better to use, you can just toggle up the effort, go into the next opus mode, the effort, go into the next opus mode, the effort, go into the next opus mode, start from low and then go medium and start from low and then go medium and start from low and then go medium and then high. So let's go to opus. Let's go

then high. So let's go to opus. Let's go then high. So let's go to opus. Let's go to low. Now that we have the model set, to low. Now that we have the model set, to low. Now that we have the model set, it's time for us to actually start a new it's time for us to actually start a new

it's time for us to actually start a new agent team. And anthropic tells us agent team. And anthropic tells us agent team. And anthropic tells us specifically that we must tell Claude to specifically that we must tell Claude to specifically that we must tell Claude to create an agent team. In all the

create an agent team. In all the create an agent team. In all the examples that it give us, it always says examples that it give us, it always says examples that it give us, it always says create an agent team. Sometimes it says create an agent team. Sometimes it says

create an agent team. Sometimes it says create three different team members that create three different team members that create three different team members that focus on A, B, and C. Or sometimes it focus on A, B, and C. Or sometimes it focus on A, B, and C. Or sometimes it just says create the agent team and kind

just says create the agent team and kind just says create the agent team and kind of like figure out yourself where to of like figure out yourself where to of like figure out yourself where to deploy those agents. So to touch on how deploy those agents. So to touch on how

deploy those agents. So to touch on how these agents work together, a little bit these agents work together, a little bit these agents work together, a little bit on memory and also a little bit on task on memory and also a little bit on task on memory and also a little bit on task assignment. When you enter a command

assignment. When you enter a command assignment. When you enter a command into here to basically say, hey, create into here to basically say, hey, create into here to basically say, hey, create me an agent team. What you get is you me an agent team. What you get is you

me an agent team. What you get is you get a team leader that takes your get a team leader that takes your get a team leader that takes your request and then it determines, okay, request and then it determines, okay, request and then it determines, okay, what are the what's the job to be done

what are the what's the job to be done what are the what's the job to be done here? What are the different tasks that here? What are the different tasks that here? What are the different tasks that we need to complete? and what are the we need to complete? and what are the

[12:08]

we need to complete? and what are the different prompts that we need for each different prompts that we need for each different prompts that we need for each of these agents. So when when they of these agents. So when when they of these agents. So when when they actually decide that the team leader

actually decide that the team leader actually decide that the team leader will generate a certain amount of will generate a certain amount of will generate a certain amount of context and like information as part of context and like information as part of

context and like information as part of the instructions and prompt for each of the instructions and prompt for each of the instructions and prompt for each of these guys but technically actually not these guys but technically actually not these guys but technically actually not even technically just truly what happens

even technically just truly what happens even technically just truly what happens is these guys do not get access to the is these guys do not get access to the is these guys do not get access to the entire conversation thread. So if you're entire conversation thread. So if you're

entire conversation thread. So if you're here having the like a default here having the like a default here having the like a default conversation, you kind of start here.

conversation, you kind of start here. conversation, you kind of start here. You're just chatting for like 10, 20, 30 You're just chatting for like 10, 20, 30 You're just chatting for like 10, 20, 30 minutes. You're doing a bunch of web minutes. You're doing a bunch of web

minutes. You're doing a bunch of web searching. You're doing a bunch of like searching. You're doing a bunch of like searching. You're doing a bunch of like understanding a certain codebase. When understanding a certain codebase. When understanding a certain codebase. When you go to your agent team mode, you

you go to your agent team mode, you you go to your agent team mode, you actually want to deploy get your MD file actually want to deploy get your MD file actually want to deploy get your MD file set up and then get the agent from the set up and then get the agent from the

set up and then get the agent from the default mode to actually provide the default mode to actually provide the default mode to actually provide the correct context for whatever session correct context for whatever session correct context for whatever session you've correct you've already had so

you've correct you've already had so you've correct you've already had so far. So that when it distributes the far. So that when it distributes the far. So that when it distributes the work to the team leader or so teammates, work to the team leader or so teammates,

work to the team leader or so teammates, it can just tell them and instruct them it can just tell them and instruct them it can just tell them and instruct them and say read the MD file, understand and say read the MD file, understand and say read the MD file, understand what the context is and then here's your

what the context is and then here's your what the context is and then here's your specific task as well. So then you can specific task as well. So then you can specific task as well. So then you can go away and do your task but have the go away and do your task but have the

go away and do your task but have the additional context. So just be mindful additional context. So just be mindful additional context. So just be mindful these guys do not get the all the these guys do not get the all the these guys do not get the all the context from the original conversation.

context from the original conversation. context from the original conversation. Now, the next thing you might not know Now, the next thing you might not know Now, the next thing you might not know is when the team leader creates the is when the team leader creates the

is when the team leader creates the tasks, it depending on how they actually tasks, it depending on how they actually tasks, it depending on how they actually structure the team, there is a list of structure the team, there is a list of structure the team, there is a list of tasks that have to be completed. And

tasks that have to be completed. And tasks that have to be completed. And sometimes it's like a free-for-all, sometimes it's like a free-for-all, sometimes it's like a free-for-all, like, hey, here's your four or five like, hey, here's your four or five

like, hey, here's your four or five tasks. You two guys work on these five tasks. You two guys work on these five tasks. You two guys work on these five tasks. And um one issue that you might tasks. And um one issue that you might tasks. And um one issue that you might think would happen is if I finish my

think would happen is if I finish my think would happen is if I finish my task at the same time that you do, we task at the same time that you do, we task at the same time that you do, we both reach for the next task. How do we both reach for the next task. How do we

both reach for the next task. How do we know that we're both not wasting tokens know that we're both not wasting tokens know that we're both not wasting tokens working on the same task when it's working on the same task when it's working on the same task when it's already being taken care of? So, um

already being taken care of? So, um already being taken care of? So, um Anthropic actually takes care of this. Anthropic actually takes care of this.

Anthropic actually takes care of this. They have like a race condition check in They have like a race condition check in They have like a race condition check in place that basically whenever I take the place that basically whenever I take the place that basically whenever I take the task if I'm just incrementally faster

task if I'm just incrementally faster task if I'm just incrementally faster than you, it's already blocked off. You than you, it's already blocked off. You than you, it's already blocked off. You cannot take it. Therefore, we don't cannot take it. Therefore, we don't

cannot take it. Therefore, we don't double use tokens on the same tasks. The double use tokens on the same tasks. The double use tokens on the same tasks. The one final thing I want to mention, and one final thing I want to mention, and one final thing I want to mention, and this is actually a token saving

this is actually a token saving this is actually a token saving strategy, is when you're first building strategy, is when you're first building strategy, is when you're first building out your team and you give the prompt to out your team and you give the prompt to

out your team and you give the prompt to your team leader to create you a team your team leader to create you a team your team leader to create you a team with four agents that's going to with four agents that's going to with four agents that's going to refactor these modules, you can also

refactor these modules, you can also refactor these modules, you can also define which model you want to use for define which model you want to use for define which model you want to use for those team members, which in this is those team members, which in this is

those team members, which in this is actually pretty good because instead of actually pretty good because instead of actually pretty good because instead of using the Opus 4.6, 6 which is the most using the Opus 4.6, 6 which is the most using the Opus 4.6, 6 which is the most expensive model. Sometimes if you don't

[14:10]

expensive model. Sometimes if you don't expensive model. Sometimes if you don't need the best model for a specific task, need the best model for a specific task, need the best model for a specific task, you can just say use a use a lower model you can just say use a use a lower model

you can just say use a use a lower model which is cheaper for you but you will which is cheaper for you but you will which is cheaper for you but you will still get the correct outcome that you still get the correct outcome that you still get the correct outcome that you need. So you don't actually have to only

need. So you don't actually have to only need. So you don't actually have to only use the opus 4.6. So now for our use the opus 4.6. So now for our use the opus 4.6. So now for our example, we're not going to be doing example, we're not going to be doing

example, we're not going to be doing anything with code. I'm actually going anything with code. I'm actually going anything with code. I'm actually going to be deploying a team of researchers to to be deploying a team of researchers to to be deploying a team of researchers to understand a specific topic and give me

understand a specific topic and give me understand a specific topic and give me some recommendations. So I've just some recommendations. So I've just some recommendations. So I've just created a prompt using some of the created a prompt using some of the

created a prompt using some of the strategies that we were just speaking strategies that we were just speaking strategies that we were just speaking about. I'm specifically saying to create about. I'm specifically saying to create about. I'm specifically saying to create an agent team. I'm then giving my uh my

an agent team. I'm then giving my uh my an agent team. I'm then giving my uh my problem that I want to research and I'm problem that I want to research and I'm problem that I want to research and I'm also defining two different agents that also defining two different agents that

also defining two different agents that I want to create and then giving the I want to create and then giving the I want to create and then giving the team leader some freedom to uh figure team leader some freedom to uh figure team leader some freedom to uh figure out some opposing angles or that we want

out some opposing angles or that we want out some opposing angles or that we want to investigate. Finally, I'm also to investigate. Finally, I'm also to investigate. Finally, I'm also defining that be using Sonut for all the defining that be using Sonut for all the

defining that be using Sonut for all the agents. So now let's fire this off and agents. So now let's fire this off and agents. So now let's fire this off and we're not going to be splitting up our we're not going to be splitting up our we're not going to be splitting up our windows just yet because we have teams

windows just yet because we have teams windows just yet because we have teams enabled. The first thing that has to enabled. The first thing that has to enabled. The first thing that has to happen is the agent has to the team happen is the agent has to the team

happen is the agent has to the team leader has to identify all right what's leader has to identify all right what's leader has to identify all right what's this request about what do we need to do this request about what do we need to do this request about what do we need to do define the tasks that have to be

define the tasks that have to be define the tasks that have to be completed then define the prompts and completed then define the prompts and completed then define the prompts and then go and establish each of those then go and establish each of those

then go and establish each of those agents only at that moment when the agents only at that moment when the agents only at that moment when the agents are up and running will then we agents are up and running will then we agents are up and running will then we go into this split view of different

go into this split view of different go into this split view of different windows. Nice. Look at that. So we're windows. Nice. Look at that. So we're windows. Nice. Look at that. So we're spinning up our first agent in this spinning up our first agent in this

spinning up our first agent in this split view. Looks like we have our split view. Looks like we have our split view. Looks like we have our second agent in the second split view.

second agent in the second split view. second agent in the second split view. Okay. So we spled up our fourth agent. Okay. So we spled up our fourth agent.

Okay. So we spled up our fourth agent. Is this going to be the final one? 1 2 3 Is this going to be the final one? 1 2 3 Is this going to be the final one? 1 2 3 4 5. There might actually be five 4 5. There might actually be five 4 5. There might actually be five different agents we're spooling up. So,

different agents we're spooling up. So, different agents we're spooling up. So, it's a little bit hard to see. So now at it's a little bit hard to see. So now at it's a little bit hard to see. So now at this stage, we see all of our agents on this stage, we see all of our agents on

this stage, we see all of our agents on this right hand side panel. And we can this right hand side panel. And we can this right hand side panel. And we can just drill into one of these agents and just drill into one of these agents and just drill into one of these agents and just have a conversation with them as

just have a conversation with them as just have a conversation with them as well. So over here we have the SAS AI well. So over here we have the SAS AI well. So over here we have the SAS AI adoption. And if I type on my keyboard adoption. And if I type on my keyboard

adoption. And if I type on my keyboard like, hey, how are you going? I can hit like, hey, how are you going? I can hit like, hey, how are you going? I can hit enter and then I can get a response back enter and then I can get a response back enter and then I can get a response back specifically from this SAS AI adoption

specifically from this SAS AI adoption specifically from this SAS AI adoption agent. Now, as we just saw, we had four agent. Now, as we just saw, we had four agent. Now, as we just saw, we had four different panels of teammates working.

different panels of teammates working. different panels of teammates working. If at some stage you have like four If at some stage you have like four If at some stage you have like four agents working and you realize that one agents working and you realize that one

agents working and you realize that one of the agents doesn't need to keep of the agents doesn't need to keep of the agents doesn't need to keep working and you want to save those working and you want to save those working and you want to save those tokens, you can go to the team leader

tokens, you can go to the team leader tokens, you can go to the team leader and ask them specifically using the and ask them specifically using the and ask them specifically using the agent's name and just say, "Can you agent's name and just say, "Can you

[16:10]

agent's name and just say, "Can you please shut this specific agent down?" please shut this specific agent down?" please shut this specific agent down?" So, the team leader will then send a So, the team leader will then send a So, the team leader will then send a request to the agent. Most of the time,

request to the agent. Most of the time, request to the agent. Most of the time, the team the teammate can approve that the team the teammate can approve that the team the teammate can approve that and then gracefully shut down. But if and then gracefully shut down. But if

and then gracefully shut down. But if they are working on something that's they are working on something that's they are working on something that's like mission critical or they believe like mission critical or they believe like mission critical or they believe it's mission critical, they can reject

it's mission critical, they can reject it's mission critical, they can reject the claim or the the request with an the claim or the the request with an the claim or the the request with an explanation. So then the final stage of explanation. So then the final stage of

explanation. So then the final stage of working with an agent team is that um working with an agent team is that um working with an agent team is that um this is actually done automatically by this is actually done automatically by this is actually done automatically by the team leader. But basically the team

the team leader. But basically the team the team leader. But basically the team leader goes through all the agents, make leader goes through all the agents, make leader goes through all the agents, make sure all the tasks are complete and then sure all the tasks are complete and then

sure all the tasks are complete and then they finished working and then they'll they finished working and then they'll they finished working and then they'll just like close down the team so we can just like close down the team so we can just like close down the team so we can shut down all the shared resources.

shut down all the shared resources. shut down all the shared resources. Essentially closing down all those Essentially closing down all those Essentially closing down all those separate sessions then bringing separate sessions then bringing

separate sessions then bringing everything back into just one session. everything back into just one session. everything back into just one session. And that's what we saw happen over here.

And that's what we saw happen over here. And that's what we saw happen over here. So the team leader actually went away So the team leader actually went away So the team leader actually went away and shut down and cleaned up all those and shut down and cleaned up all those

and shut down and cleaned up all those agents. Now this for this research use agents. Now this for this research use agents. Now this for this research use case this is an easy like a easy case this is an easy like a easy case this is an easy like a easy shutdown. It just closes the entire team

shutdown. It just closes the entire team shutdown. It just closes the entire team down for applications for like coding, down for applications for like coding, down for applications for like coding, creating apps, refactoring, debugging.

creating apps, refactoring, debugging. creating apps, refactoring, debugging. Typically the team leader will leave Typically the team leader will leave Typically the team leader will leave either the entire team or certain agents either the entire team or certain agents

either the entire team or certain agents up and idling. So instead of just up and idling. So instead of just up and idling. So instead of just closing everything up when a task is closing everything up when a task is closing everything up when a task is complete, they'll actually wait for you

complete, they'll actually wait for you complete, they'll actually wait for you to come back, give the final test, and to come back, give the final test, and to come back, give the final test, and then just say, okay, you can close the then just say, okay, you can close the

then just say, okay, you can close the team down or please, you know, go back team down or please, you know, go back team down or please, you know, go back to the QA agent and just make them to the QA agent and just make them to the QA agent and just make them recheck this part because it's actually

recheck this part because it's actually recheck this part because it's actually still broken. Or please go back to the still broken. Or please go back to the still broken. Or please go back to the backend agent, tell them to fix this backend agent, tell them to fix this

backend agent, tell them to fix this part cuz it's still broken. And that's part cuz it's still broken. And that's part cuz it's still broken. And that's important because you maintain like that important because you maintain like that important because you maintain like that backend agent maintains the context of

backend agent maintains the context of backend agent maintains the context of what they were working on and all the what they were working on and all the what they were working on and all the different changes, all the different different changes, all the different

different changes, all the different issues they ran into. So they should be issues they ran into. So they should be issues they ran into. So they should be able to just jump back into the project able to just jump back into the project able to just jump back into the project and fix whatever you're telling them.

and fix whatever you're telling them. and fix whatever you're telling them. And that's important because you don't And that's important because you don't And that's important because you don't want to lose their specific context want to lose their specific context

want to lose their specific context anyway. Now another strategy for anyway. Now another strategy for anyway. Now another strategy for maintaining memory between each of these maintaining memory between each of these maintaining memory between each of these sessions like this as well. Like for

sessions like this as well. Like for sessions like this as well. Like for example, if I fully shut down this team example, if I fully shut down this team example, if I fully shut down this team and we were doing working on some kind and we were doing working on some kind

and we were doing working on some kind of code, you could create a shared of code, you could create a shared of code, you could create a shared memory MD file where you get all the memory MD file where you get all the memory MD file where you get all the agents to log all their issues like all

agents to log all their issues like all agents to log all their issues like all the bugs they ran into and all the all the bugs they ran into and all the all the bugs they ran into and all the all the stuff they've tried to debug to that the stuff they've tried to debug to that

the stuff they've tried to debug to that stage or if they have debugged basically stage or if they have debugged basically stage or if they have debugged basically like a running list of all the issues like a running list of all the issues like a running list of all the issues and fixes that they've had. So if you do

and fixes that they've had. So if you do and fixes that they've had. So if you do spool up other agents for different in spool up other agents for different in spool up other agents for different in the same session or different sessions, the same session or different sessions,

[18:12]

the same session or different sessions, you can just reference that memory file you can just reference that memory file you can just reference that memory file basically longterm persistently through basically longterm persistently through basically longterm persistently through different sessions. And now at this

different sessions. And now at this different sessions. And now at this stage, I just want to go through and stage, I just want to go through and stage, I just want to go through and look at the cost of the session that we look at the cost of the session that we

look at the cost of the session that we just ran. And it looks like it was $1.15 just ran. And it looks like it was $1.15 just ran. And it looks like it was $1.15 to run all those agents to do that to run all those agents to do that to run all those agents to do that research across a 4minute duration. So I

research across a 4minute duration. So I research across a 4minute duration. So I think something actually happened here. think something actually happened here.

think something actually happened here. This is not 100% correct. Typically when This is not 100% correct. Typically when This is not 100% correct. Typically when you're running multiple different you're running multiple different you're running multiple different agents, their API duration will

agents, their API duration will agents, their API duration will compound. So if you have five agents compound. So if you have five agents compound. So if you have five agents running for 5 minutes, it'll typically running for 5 minutes, it'll typically

running for 5 minutes, it'll typically say 25m minute duration. Here these say 25m minute duration. Here these say 25m minute duration. Here these agents were not running for that short agents were not running for that short agents were not running for that short amount of time. for example, worked for

amount of time. for example, worked for amount of time. for example, worked for 5 minutes and 33 seconds. So something 5 minutes and 33 seconds. So something 5 minutes and 33 seconds. So something here is not fully lining up. But in here is not fully lining up. But in

here is not fully lining up. But in general, you should just be going to general, you should just be going to general, you should just be going to your cost tab after each session or your cost tab after each session or your cost tab after each session or after each agent spool up and spool down

after each agent spool up and spool down after each agent spool up and spool down just to see what it's costing you. So just to see what it's costing you. So just to see what it's costing you. So you can kind of be smarter for next time you can kind of be smarter for next time

you can kind of be smarter for next time with your prompting or your model with your prompting or your model with your prompting or your model selection. So at this stage, we've selection. So at this stage, we've selection. So at this stage, we've looked at how to start up a team where

looked at how to start up a team where looked at how to start up a team where we have to specifically say we want a we have to specifically say we want a we have to specifically say we want a team of agents. We can define a team of agents. We can define a

team of agents. We can define a different model that we want. We also different model that we want. We also different model that we want. We also looked at different management. So looked at different management. So looked at different management. So instead of just looking at all the

instead of just looking at all the instead of just looking at all the agents basically in that same room, we agents basically in that same room, we agents basically in that same room, we split them up into separate rooms. we're split them up into separate rooms. we're

split them up into separate rooms. we're able to see what they're working on. able to see what they're working on. able to see what they're working on. We're able to communicate with them We're able to communicate with them We're able to communicate with them directly as well. And then finally,

directly as well. And then finally, directly as well. And then finally, looking at these shutdown principles looking at these shutdown principles looking at these shutdown principles around cleaning up certain agents if we around cleaning up certain agents if we

around cleaning up certain agents if we don't want them to keep working, but don't want them to keep working, but don't want them to keep working, but then also shutting down the team then also shutting down the team then also shutting down the team gracefully and clearing up all the

gracefully and clearing up all the gracefully and clearing up all the resources. So now, interestingly, the resources. So now, interestingly, the resources. So now, interestingly, the final thing that I want to go across is final thing that I want to go across is

final thing that I want to go across is just looking at skills and how can you just looking at skills and how can you just looking at skills and how can you use skills to improve how you run teams.

use skills to improve how you run teams. use skills to improve how you run teams. So, as you guys know, a skill is just a So, as you guys know, a skill is just a So, as you guys know, a skill is just a way that you complete a repeatable way that you complete a repeatable

way that you complete a repeatable process. And for my own workflow with process. And for my own workflow with process. And for my own workflow with agents, I'm actually finding that I'm agents, I'm actually finding that I'm agents, I'm actually finding that I'm getting them to complete the exact same

getting them to complete the exact same getting them to complete the exact same thing just on different topics. So, for thing just on different topics. So, for thing just on different topics. So, for example, I've got a very specific way example, I've got a very specific way

example, I've got a very specific way that I like to do research. And instead that I like to do research. And instead that I like to do research. And instead of me just prompting up every single of me just prompting up every single of me just prompting up every single time the entire research process, I can

time the entire research process, I can time the entire research process, I can just turn this into a skill. And the just turn this into a skill. And the just turn this into a skill. And the best way that I found to create skills best way that I found to create skills

best way that I found to create skills is not to just write it from scratch and is not to just write it from scratch and is not to just write it from scratch and upload it and kind of just go with it upload it and kind of just go with it upload it and kind of just go with it blindly. It's to actually complete the

blindly. It's to actually complete the blindly. It's to actually complete the skill as a process first using Claude skill as a process first using Claude skill as a process first using Claude Code and then get Claude Code to create Code and then get Claude Code to create

Code and then get Claude Code to create that skill for you. So in this example, that skill for you. So in this example, that skill for you. So in this example, we had a very basic process. I literally we had a very basic process. I literally we had a very basic process. I literally just said, "Create a research team." I

just said, "Create a research team." I just said, "Create a research team." I didn't even read the results, but didn't even read the results, but didn't even read the results, but typically what you would do is you would typically what you would do is you would

[20:13]

typically what you would do is you would go back and forth and say, "I'll go back and forth and say, "I'll go back and forth and say, "I'll actually research this part of the actually research this part of the actually research this part of the thing, or can you now convert the output

thing, or can you now convert the output thing, or can you now convert the output into a PDF, or can you send me an into a PDF, or can you send me an into a PDF, or can you send me an email?" Once you run through that entire email?" Once you run through that entire

email?" Once you run through that entire process, you can just create a prompt process, you can just create a prompt process, you can just create a prompt like this that says, "Turn whatever we like this that says, "Turn whatever we like this that says, "Turn whatever we just did into a skill." And you can also

just did into a skill." And you can also just did into a skill." And you can also define that you want to have different define that you want to have different define that you want to have different variables in that skill. For example, variables in that skill. For example,

variables in that skill. For example, for our research skill, we want to have for our research skill, we want to have for our research skill, we want to have a different topic and maybe a different a different topic and maybe a different a different topic and maybe a different model that we use depending on the

model that we use depending on the model that we use depending on the research that we're doing. So, you can research that we're doing. So, you can research that we're doing. So, you can just go away and hit enter. And now, just go away and hit enter. And now,

just go away and hit enter. And now, Claude's going to take this specific Claude's going to take this specific Claude's going to take this specific process and then store that skill in our process and then store that skill in our process and then store that skill in our repository. So now another hack when

repository. So now another hack when repository. So now another hack when you're doing skills is that every time you're doing skills is that every time you're doing skills is that every time you actually run the skill, if there is you actually run the skill, if there is

you actually run the skill, if there is an update to the process that you want an update to the process that you want an update to the process that you want to make, you can just go back into to make, you can just go back into to make, you can just go back into Claude and just reprompt and say, "Hey,

Claude and just reprompt and say, "Hey, Claude and just reprompt and say, "Hey, this new adjustment to the process, how this new adjustment to the process, how this new adjustment to the process, how we're using fewer agents, more agents, we're using fewer agents, more agents,

we're using fewer agents, more agents, or instead of sending emails, now we're or instead of sending emails, now we're or instead of sending emails, now we're doing Slack, can you please go back and doing Slack, can you please go back and doing Slack, can you please go back and update the skill and it can just keep it

update the skill and it can just keep it update the skill and it can just keep it up to date for you." So now looks like up to date for you." So now looks like up to date for you." So now looks like Claude has created that skill for us, Claude has created that skill for us,

Claude has created that skill for us, added it to our directory, and now we added it to our directory, and now we added it to our directory, and now we can just do forward slash and hit can just do forward slash and hit can just do forward slash and hit research to use that skill. We're using

research to use that skill. We're using research to use that skill. We're using argument for the topic and then model argument for the topic and then model argument for the topic and then model for the agent model. And then we got a for the agent model. And then we got a

for the agent model. And then we got a very easy explanation of how to use that very easy explanation of how to use that very easy explanation of how to use that skill. So we can either just use skill. So we can either just use skill. So we can either just use forward/ressearch why is bitcoin

forward/ressearch why is bitcoin forward/ressearch why is bitcoin dropping to run with the sonnet agents dropping to run with the sonnet agents dropping to run with the sonnet agents or to override the model you can say why or to override the model you can say why

or to override the model you can say why is bitcoin dropping using haik coup. And is bitcoin dropping using haik coup. And is bitcoin dropping using haik coup. And now in order for us to use that skill we now in order for us to use that skill we now in order for us to use that skill we cannot do it in the exact same session.

cannot do it in the exact same session. cannot do it in the exact same session. That's why we don't see it coming up That's why we don't see it coming up That's why we don't see it coming up over here. So we just start a brand new over here. So we just start a brand new

over here. So we just start a brand new claude session. Let's hit enter forward claude session. Let's hit enter forward claude session. Let's hit enter forward slash research. And here is that skill.

slash research. And here is that skill. slash research. And here is that skill. And let's just test it out. So why is And let's just test it out. So why is And let's just test it out. So why is Bitcoin dropping? Hit enter. And because Bitcoin dropping? Hit enter. And because

Bitcoin dropping? Hit enter. And because I didn't actually launch this in T-Max, I didn't actually launch this in T-Max, I didn't actually launch this in T-Max, we're not going to see the split panel we're not going to see the split panel we're not going to see the split panel for all the agents, but we do have the

for all the agents, but we do have the for all the agents, but we do have the skill being used. So, launch a multi- skill being used. So, launch a multi- skill being used. So, launch a multi- aent research team to investigate why aent research team to investigate why

aent research team to investigate why Bitcoin is dropping. So, just like Bitcoin is dropping. So, just like Bitcoin is dropping. So, just like before, we had the evidence gatherer, we before, we had the evidence gatherer, we before, we had the evidence gatherer, we had the bull case, bare case, and now

had the bull case, bare case, and now had the bull case, bare case, and now two opposing different agents that we two opposing different agents that we two opposing different agents that we can use. All right, guys. Thank you very can use. All right, guys. Thank you very

can use. All right, guys. Thank you very much for watching. I hope you can now go much for watching. I hope you can now go much for watching. I hope you can now go away and use agent teams even better.

away and use agent teams even better. away and use agent teams even better. See you in the next one.

