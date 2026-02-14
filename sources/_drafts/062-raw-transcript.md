# Raw Transcript: Every Level of Claude Code Explained in 39 Minutes

[0:00]

I've spent over 150 hours now in Cyclude I've spent over 150 hours now in Cyclude Code, not just building with it, but Code, not just building with it, but Code, not just building with it, but studying every single major resource on studying every single major resource on

studying every single major resource on it. I've broken down the creator Boris it. I've broken down the creator Boris it. I've broken down the creator Boris Churnney's post, tested real workflows Churnney's post, tested real workflows Churnney's post, tested real workflows from top builders, and watched every

from top builders, and watched every from top builders, and watched every single masterclaw tutorial that I could single masterclaw tutorial that I could single masterclaw tutorial that I could find. And here's what most people miss.

find. And here's what most people miss. find. And here's what most people miss. Even if you think you're using Claw Code Even if you think you're using Claw Code Even if you think you're using Claw Code well today, you're probably stuck at well today, you're probably stuck at

well today, you're probably stuck at level two or level three. This video level two or level three. This video level two or level three. This video shows you what's beyond that. I'll walk shows you what's beyond that. I'll walk shows you what's beyond that. I'll walk you through all seven levels of claw

you through all seven levels of claw you through all seven levels of claw code from beginner workflows to fully code from beginner workflows to fully code from beginner workflows to fully autonomous systems so you can skip the autonomous systems so you can skip the

autonomous systems so you can skip the trial and error and start using it to trial and error and start using it to trial and error and start using it to its full potential today. And by the its full potential today. And by the its full potential today. And by the way, if you're looking for a full Claude

way, if you're looking for a full Claude way, if you're looking for a full Claude Code course that takes you from zero to Code course that takes you from zero to Code course that takes you from zero to expert, then check out the link in the expert, then check out the link in the

expert, then check out the link in the description below. Now, let's dive into description below. Now, let's dive into description below. Now, let's dive into level one. Let's quickly make sure it's level one. Let's quickly make sure it's level one. Let's quickly make sure it's set up in our environment. So, we're

set up in our environment. So, we're set up in our environment. So, we're going to come into a fresh instance of going to come into a fresh instance of going to come into a fresh instance of VS Code, open a folder, and open a new VS Code, open a folder, and open a new

VS Code, open a folder, and open a new terminal. I'm just going to open the the terminal. I'm just going to open the the terminal. I'm just going to open the the readme here and we're going to run this readme here and we're going to run this readme here and we're going to run this native installer that doesn't require

native installer that doesn't require native installer that doesn't require Node.js. We're going to run that inside Node.js. We're going to run that inside Node.js. We're going to run that inside our terminal and that's going to make our terminal and that's going to make

our terminal and that's going to make sure that Claude code is installed for sure that Claude code is installed for sure that Claude code is installed for us. And we're going to start running it us. And we're going to start running it us. And we're going to start running it just by running Claude with the basic

just by running Claude with the basic just by running Claude with the basic permissions. And once Claude opens, it's permissions. And once Claude opens, it's permissions. And once Claude opens, it's going to look a little bit like this.

going to look a little bit like this. going to look a little bit like this. Now, level one is actually prompting but Now, level one is actually prompting but Now, level one is actually prompting but with intent. So most people just type with intent. So most people just type

with intent. So most people just type and hope at the start. But the and hope at the start. But the and hope at the start. But the difference between somebody who's a difference between somebody who's a difference between somebody who's a beginner with Claude code and someone

beginner with Claude code and someone beginner with Claude code and someone who's going to get real results is one who's going to get real results is one who's going to get real results is one single habit and that is planning before single habit and that is planning before

single habit and that is planning before building. So plan mode, which you can building. So plan mode, which you can building. So plan mode, which you can turn on by hitting shift and tab and turn on by hitting shift and tab and turn on by hitting shift and tab and cycle between the modes. You can see

cycle between the modes. You can see cycle between the modes. You can see down here we've got accept edits, which down here we've got accept edits, which down here we've got accept edits, which is the default [music] mode, and plan is the default [music] mode, and plan

is the default [music] mode, and plan mode is a readonly mode. It's designed mode is a readonly mode. It's designed mode is a readonly mode. It's designed to research your codebase and propose a to research your codebase and propose a to research your codebase and propose a plan before you touch anything. So

plan before you touch anything. So plan before you touch anything. So whether you've got an existing codebase, whether you've got an existing codebase, whether you've got an existing codebase, it will go through and read those files it will go through and read those files

it will go through and read those files or if we're starting from scratch and or if we're starting from scratch and or if we're starting from scratch and we're giving it some context brief, it's we're giving it some context brief, it's we're giving it some context brief, it's really critical that we start with

really critical that we start with really critical that we start with planning mode. And Boris Churnney, the planning mode. And Boris Churnney, the planning mode. And Boris Churnney, the creator of Claude Code, has strong creator of Claude Code, has strong

creator of Claude Code, has strong opinions about using planning code. If opinions about using planning code. If opinions about using planning code. If my goal is to write a pull request, I my goal is to write a pull request, I my goal is to write a pull request, I will use plan mode. And I'll go back and

will use plan mode. And I'll go back and will use plan mode. And I'll go back and forth with Claude until I like its plan. forth with Claude until I like its plan.

forth with Claude until I like its plan. So, he does not take any execution So, he does not take any execution So, he does not take any execution actions until a plan is made. From actions until a plan is made. From actions until a plan is made. From there, I switch into auto accept edits

[2:00]

there, I switch into auto accept edits there, I switch into auto accept edits mode. And Claude can usually oneshot it. mode. And Claude can usually oneshot it.

mode. And Claude can usually oneshot it. So, it saves us going back and forth. So, it saves us going back and forth. So, it saves us going back and forth. And actually, we only need to oneshot And actually, we only need to oneshot And actually, we only need to oneshot prompt for the execution once we've got

prompt for the execution once we've got prompt for the execution once we've got a clear plan. And the reason this mode a clear plan. And the reason this mode a clear plan. And the reason this mode is so powerful is because it leverages is so powerful is because it leverages

is so powerful is because it leverages an in-built ask user questions tool an in-built ask user questions tool an in-built ask user questions tool inside Claude code. Claude will inside Claude code. Claude will inside Claude code. Claude will literally come back to us with a series

literally come back to us with a series literally come back to us with a series of questions to understand the of questions to understand the of questions to understand the underlying detail and the assumptions underlying detail and the assumptions

underlying detail and the assumptions that we're making in our plan. that we're making in our plan. that we're making in our plan. Therefore, building out a really Therefore, building out a really Therefore, building out a really comprehensive set of context that it can

comprehensive set of context that it can comprehensive set of context that it can use in the execution phase. So, we're use in the execution phase. So, we're use in the execution phase. So, we're going to look at an example today of a going to look at an example today of a

going to look at an example today of a content creation system and how we can content creation system and how we can content creation system and how we can use Claude Code to actually build us out use Claude Code to actually build us out use Claude Code to actually build us out a system that creates all of our content

a system that creates all of our content a system that creates all of our content for us. So, if I put in something vague for us. So, if I put in something vague for us. So, if I put in something vague during plan mode like help me build out during plan mode like help me build out

during plan mode like help me build out a social media content creation system, a social media content creation system, a social media content creation system, we know that that's not going to execute we know that that's not going to execute we know that that's not going to execute very well or it will veer off course and

very well or it will veer off course and very well or it will veer off course and not meet our assumptions because we're not meet our assumptions because we're not meet our assumptions because we're not actually specifying that. So, by not actually specifying that. So, by

not actually specifying that. So, by doing this in plan mode, we can force doing this in plan mode, we can force doing this in plan mode, we can force Claude to give come back with the ask Claude to give come back with the ask Claude to give come back with the ask user questions tool, ask us a bunch of

user questions tool, ask us a bunch of user questions tool, ask us a bunch of questions and build out a plan MD file questions and build out a plan MD file questions and build out a plan MD file which then when it executes on, it will which then when it executes on, it will

which then when it executes on, it will understand in detail exactly what we understand in detail exactly what we understand in detail exactly what we want to do. And then we can see down want to do. And then we can see down want to do. And then we can see down here which social media platforms do you

here which social media platforms do you here which social media platforms do you want to create content for? We click want to create content for? We click want to create content for? We click that, it will come up with the next set that, it will come up with the next set

that, it will come up with the next set of questions in the calendar. Then about of questions in the calendar. Then about of questions in the calendar. Then about the automation, the brand voice and then the automation, the brand voice and then the automation, the brand voice and then we submit and it will create a plan for

we submit and it will create a plan for we submit and it will create a plan for us and ask us any additional questions us and ask us any additional questions us and ask us any additional questions or ask us for any additional assumptions or ask us for any additional assumptions

or ask us for any additional assumptions before we start executing a thing. So before we start executing a thing. So before we start executing a thing. So level one users make sure that they're level one users make sure that they're level one users make sure that they're planning before they execute. So now

planning before they execute. So now planning before they execute. So now that you've got a plan, you need to make that you've got a plan, you need to make that you've got a plan, you need to make sure that Claude code isn't going to put sure that Claude code isn't going to put

sure that Claude code isn't going to put out generic slop within that plan and out generic slop within that plan and out generic slop within that plan and it's going to work in a way that it's going to work in a way that it's going to work in a way that actually saves you time and not cost you

actually saves you time and not cost you actually saves you time and not cost you more time in the end. And that brings us more time in the end. And that brings us more time in the end. And that brings us to the claude.mmd file and the to the claude.mmd file and the

to the claude.mmd file and the importance of having one for your importance of having one for your importance of having one for your [music] team. So Claude, like a [music] team. So Claude, like a [music] team. So Claude, like a coworker, needs to actually understand

coworker, needs to actually understand coworker, needs to actually understand your rules and the way you want to work your rules and the way you want to work your rules and the way you want to work with it. We use claude.md to show that.

with it. We use claude.md to show that. with it. We use claude.md to show that. It's a file that tells Claude how you It's a file that tells Claude how you It's a file that tells Claude how you work. And you can think of it like work. And you can think of it like

work. And you can think of it like literally onboarding a new team member. literally onboarding a new team member. literally onboarding a new team member. You write down your text stack, your You write down your text stack, your You write down your text stack, your preferences, the mistakes you don't want

preferences, the mistakes you don't want preferences, the mistakes you don't want repeated, and Claude reads the file repeated, and Claude reads the file repeated, and Claude reads the file every time you start a session. And this every time you start a session. And this

every time you start a session. And this is how Boris himself uses it. So their is how Boris himself uses it. So their is how Boris himself uses it. So their team shares a single claude.mmd file.

[4:03]

team shares a single claude.mmd file. team shares a single claude.mmd file. They keep it version controlled on Git They keep it version controlled on Git They keep it version controlled on Git and the whole team contributes lines to and the whole team contributes lines to

and the whole team contributes lines to that file or edits lines to that file. that file or edits lines to that file. that file or edits lines to that file. Don't necessarily add more lines to that Don't necessarily add more lines to that Don't necessarily add more lines to that file every single week and they'll even

file every single week and they'll even file every single week and they'll even go to the point where they'll tag it on go to the point where they'll tag it on go to the point where they'll tag it on GitHub and it will make the changes GitHub and it will make the changes

GitHub and it will make the changes automatically to tell it what mistakes automatically to tell it what mistakes automatically to tell it what mistakes it shouldn't make again. And there's it shouldn't make again. And there's it shouldn't make again. And there's lots of opinions on how you should write

lots of opinions on how you should write lots of opinions on how you should write your Claude.md file and what should be your Claude.md file and what should be your Claude.md file and what should be included. But the golden rule here is included. But the golden rule here is

included. But the golden rule here is keep it short, keep it specific, and keep it short, keep it specific, and keep it short, keep it specific, and only include what Claude can't figure only include what Claude can't figure only include what Claude can't figure out for itself. So, we've got a very

out for itself. So, we've got a very out for itself. So, we've got a very simple framework that you can follow to simple framework that you can follow to simple framework that you can follow to set up your claude. ND file for any set up your claude. ND file for any

set up your claude. ND file for any project, and we're going to talk about project, and we're going to talk about project, and we're going to talk about how we do that for building a social how we do that for building a social how we do that for building a social media content machine that sounds

media content machine that sounds media content machine that sounds exactly like your brand voice. Now, exactly like your brand voice. Now, exactly like your brand voice. Now, question one, what is this? Should just question one, what is this? Should just

question one, what is this? Should just be a single line to tell Claude exactly be a single line to tell Claude exactly be a single line to tell Claude exactly what it's doing. It's not your brand what it's doing. It's not your brand what it's doing. It's not your brand manifesto for this social media content

manifesto for this social media content manifesto for this social media content machine. This project generates daily machine. This project generates daily machine. This project generates daily social media content across various social media content across various

social media content across various different platforms in a brand voice, different platforms in a brand voice, different platforms in a brand voice, pulling topics from a content calendar pulling topics from a content calendar pulling topics from a content calendar in Air Table. That's it. Claude is then

in Air Table. That's it. Claude is then in Air Table. That's it. Claude is then able to understand exactly what its able to understand exactly what its able to understand exactly what its purpose is before we tell it how you're purpose is before we tell it how you're

purpose is before we tell it how you're going to run things which brings us on going to run things which brings us on going to run things which brings us on to the second bit and these should be to the second bit and these should be to the second bit and these should be the exact steps. So the content calendar

the exact steps. So the content calendar the exact steps. So the content calendar lives in notion that should actually be lives in notion that should actually be lives in notion that should actually be air table. We're going to pull topics air table. We're going to pull topics

air table. We're going to pull topics from the ready to write view. It's going from the ready to write view. It's going from the ready to write view. It's going to put generated posts into a new folder to put generated posts into a new folder to put generated posts into a new folder inside this explorer and we're going to

inside this explorer and we're going to inside this explorer and we're going to store any image assets in a separate store any image assets in a separate store any image assets in a separate folder. Now once it knows how, i.e. the folder. Now once it knows how, i.e. the

folder. Now once it knows how, i.e. the instructions it's going to follow. We're instructions it's going to follow. We're instructions it's going to follow. We're going to add things about brand voice, going to add things about brand voice, going to add things about brand voice, your rules, your non-negotiables. So,

your rules, your non-negotiables. So, your rules, your non-negotiables. So, what patterns do I follow? And you can what patterns do I follow? And you can what patterns do I follow? And you can use emphasis on words like important use emphasis on words like important

use emphasis on words like important where you need to make sure that where you need to make sure that where you need to make sure that actually it's really important that actually it's really important that actually it's really important that Claude follows those instructions. And

Claude follows those instructions. And Claude follows those instructions. And we've got some example brand voice stuff we've got some example brand voice stuff we've got some example brand voice stuff in here like write like you're talking in here like write like you're talking

in here like write like you're talking to one person over coffee, not to one person over coffee, not to one person over coffee, not presenting to a boardroom. But actually, presenting to a boardroom. But actually, presenting to a boardroom. But actually, the better thing to do here is not to

the better thing to do here is not to the better thing to do here is not to write this directly in here. It's to write this directly in here. It's to write this directly in here. It's to separate a brand voice document and then separate a brand voice document and then

separate a brand voice document and then reference it later on. And this brings reference it later on. And this brings reference it later on. And this brings us to the point don't dump trick which us to the point don't dump trick which us to the point don't dump trick which is actually keep claude.md super lean.

is actually keep claude.md super lean. is actually keep claude.md super lean. Tell claude where to find the details. Tell claude where to find the details.

Tell claude where to find the details. So if you're saying follow these brand So if you're saying follow these brand So if you're saying follow these brand voice guidelines, you would say for full voice guidelines, you would say for full voice guidelines, you would say for full brand voice guides with examples, see

[6:07]

brand voice guides with examples, see brand voice guides with examples, see this folder/docs/brandoice. this folder/docs/brandoice.

this folder/docs/brandoice. MD. And this might be things about brand MD. And this might be things about brand MD. And this might be things about brand voice and what patterns do I follow voice and what patterns do I follow voice and what patterns do I follow might be things about platform

might be things about platform might be things about platform formatting like keep it under 200 formatting like keep it under 200 formatting like keep it under 200 characters. It might be content rules.

characters. It might be content rules. characters. It might be content rules. So every post must teach something or So every post must teach something or So every post must teach something or share a real experience and be very very share a real experience and be very very

share a real experience and be very very practical. But again, these rules can practical. But again, these rules can practical. But again, these rules can live separately in separate folders and live separately in separate folders and live separately in separate folders and the claw.md file needs to just reference

the claw.md file needs to just reference the claw.md file needs to just reference where it understands and reads those where it understands and reads those where it understands and reads those rules from. Question four is where we rules from. Question four is where we

rules from. Question four is where we add the things about mistakes. So what add the things about mistakes. So what add the things about mistakes. So what are the things that's going to trip are the things that's going to trip are the things that's going to trip Claude up because it's not

Claude up because it's not Claude up because it's not counterintuitive? Like for example, our counterintuitive? Like for example, our counterintuitive? Like for example, our air table or notion might have a status air table or notion might have a status

air table or notion might have a status and post status column. Which one should and post status column. Which one should and post status column. Which one should it use? So these are the things that it use? So these are the things that it use? So these are the things that you'd put as your edge cases for an

you'd put as your edge cases for an you'd put as your edge cases for an employee that you're training on this. employee that you're training on this.

employee that you're training on this. And then the final part of the framework And then the final part of the framework And then the final part of the framework is how do we work? So every file is is how do we work? So every file is is how do we work? So every file is going to be named in this convention.

going to be named in this convention. going to be named in this convention. We're never going to publish or schedule We're never going to publish or schedule We're never going to publish or schedule anything when repurposing. We're going anything when repurposing. We're going

anything when repurposing. We're going to change the angle, not just shorten. to change the angle, not just shorten. to change the angle, not just shorten. So it's additional information that So it's additional information that So it's additional information that feeds into the instructions to make sure

feeds into the instructions to make sure feeds into the instructions to make sure that it delivers the outcome that you that it delivers the outcome that you that it delivers the outcome that you expect. So this is your guide and your expect. So this is your guide and your

expect. So this is your guide and your your set of rules. And down here we've your set of rules. And down here we've your set of rules. And down here we've got a copy paste template which you can got a copy paste template which you can got a copy paste template which you can grab that goes over all of these with an

grab that goes over all of these with an grab that goes over all of these with an example and create your very own claw.md example and create your very own claw.md example and create your very own claw.md file. And we would click on the tab over file. And we would click on the tab over

file. And we would click on the tab over here and actually introduce our own here and actually introduce our own here and actually introduce our own claw.md file. For now, we're going to claw.md file. For now, we're going to claw.md file. For now, we're going to keep it super simple and just give it

keep it super simple and just give it keep it super simple and just give it the project instructions. This project the project instructions. This project the project instructions. This project generates daily social media content generates daily social media content

generates daily social media content across LinkedIn X and Instagram in my across LinkedIn X and Instagram in my across LinkedIn X and Instagram in my brand voice pulling topics from a brand voice pulling topics from a brand voice pulling topics from a content calendar in Air Table. It's

content calendar in Air Table. It's content calendar in Air Table. It's important to add things like mistakes in important to add things like mistakes in important to add things like mistakes in here and how to reload that into your here and how to reload that into your

here and how to reload that into your context. So, we're going to say write a context. So, we're going to say write a context. So, we're going to say write a LinkedIn post about Google anti-gravity LinkedIn post about Google anti-gravity LinkedIn post about Google anti-gravity versus claude code for business use

versus claude code for business use versus claude code for business use cases. And this is the equivalent of not cases. And this is the equivalent of not cases. And this is the equivalent of not telling a new employee how we want the telling a new employee how we want the

telling a new employee how we want the outputs and just giving it this very outputs and just giving it this very outputs and just giving it this very generic project instruction. But as we generic project instruction. But as we generic project instruction. But as we understand how they work and how they

understand how they work and how they understand how they work and how they perform, we add in rules that help perform, we add in rules that help perform, we add in rules that help clarify the direction that we're looking clarify the direction that we're looking

clarify the direction that we're looking in as well. And it's come back with an in as well. And it's come back with an in as well. And it's come back with an okay LinkedIn post. It's had a first okay LinkedIn post. It's had a first okay LinkedIn post. It's had a first stab at it. This is the equivalent of

stab at it. This is the equivalent of stab at it. This is the equivalent of putting something into chatbt and just putting something into chatbt and just putting something into chatbt and just hoping for the best without telling it hoping for the best without telling it

hoping for the best without telling it anything about brand voice, how you want anything about brand voice, how you want anything about brand voice, how you want the outputs, etc. So, we're just going the outputs, etc. So, we're just going the outputs, etc. So, we're just going to add some simple rules. Never use m

[8:09]

to add some simple rules. Never use m to add some simple rules. Never use m dashes because we know that signifies dashes because we know that signifies dashes because we know that signifies that it's written uh by AI. Instead, use that it's written uh by AI. Instead, use

that it's written uh by AI. Instead, use regular dashes. always replace the word regular dashes. always replace the word regular dashes. always replace the word anti-gravity with AG. Maybe we've got a anti-gravity with AG. Maybe we've got a anti-gravity with AG. Maybe we've got a specific rule in our company that we

specific rule in our company that we specific rule in our company that we always write AG instead of anti-gravity. always write AG instead of anti-gravity.

always write AG instead of anti-gravity. And I also felt that it was a very very And I also felt that it was a very very And I also felt that it was a very very technical output here. It talks about technical output here. It talks about technical output here. It talks about existing stacks. Claude code is a CLI

existing stacks. Claude code is a CLI existing stacks. Claude code is a CLI tool, command line interface tool, the tool, command line interface tool, the tool, command line interface tool, the full IDE, whereas actually I want to full IDE, whereas actually I want to

full IDE, whereas actually I want to talk in business terms, never use talk in business terms, never use talk in business terms, never use technical jargon. So what we need to do technical jargon. So what we need to do technical jargon. So what we need to do then is effectively add that to our

then is effectively add that to our then is effectively add that to our project rules inside the claw. MD file. project rules inside the claw. MD file.

project rules inside the claw. MD file. You can format these however you want. You can format these however you want. You can format these however you want. And we need to restart for these to take And we need to restart for these to take And we need to restart for these to take effect. So we're going to hit clear or

effect. So we're going to hit clear or effect. So we're going to hit clear or /cle command. It's going to basically /cle command. It's going to basically /cle command. It's going to basically effectively restart then. So we're going effectively restart then. So we're going

effectively restart then. So we're going to reask it again. Write a LinkedIn post to reask it again. Write a LinkedIn post to reask it again. Write a LinkedIn post about anti-gravity versus claw code. And about anti-gravity versus claw code. And about anti-gravity versus claw code. And now it's going to have these rules

now it's going to have these rules now it's going to have these rules embedded into it. So hopefully it embedded into it. So hopefully it embedded into it. So hopefully it changes things like anti-gravity to ag.

changes things like anti-gravity to ag. changes things like anti-gravity to ag. It talks about only business value and It talks about only business value and It talks about only business value and not such technical jargon and has no m not such technical jargon and has no m

not such technical jargon and has no m dashes inside. And we see it's been dashes inside. And we see it's been dashes inside. And we see it's been reloaded. Ag versus claw code. It's got reloaded. Ag versus claw code. It's got reloaded. Ag versus claw code. It's got no m dashes inside. It talks about time

no m dashes inside. It talks about time no m dashes inside. It talks about time to value, quality control, and to value, quality control, and to value, quality control, and scalability instead of previously scalability instead of previously

scalability instead of previously talking about very technical content. talking about very technical content. talking about very technical content. So, it's understood and ingested the So, it's understood and ingested the So, it's understood and ingested the rules that we've applied via reading

rules that we've applied via reading rules that we've applied via reading that claude.md file. Now, a bit of a that claude.md file. Now, a bit of a that claude.md file. Now, a bit of a sense check you can do is can I read sense check you can do is can I read

sense check you can do is can I read this claw.md in 60 seconds? Am I under this claw.md in 60 seconds? Am I under this claw.md in 60 seconds? Am I under 30 instructions? So, 20 to 30 is kind of 30 instructions? So, 20 to 30 is kind of 30 instructions? So, 20 to 30 is kind of the maximum. And again, you can

the maximum. And again, you can the maximum. And again, you can reference other files and folders where reference other files and folders where reference other files and folders where it can find things. Did I include it can find things. Did I include

it can find things. Did I include specific examples, not vague rules? specific examples, not vague rules? specific examples, not vague rules? Again, those can be elsewhere. And would Again, those can be elsewhere. And would Again, those can be elsewhere. And would a freelancer, a human freelancer taking

a freelancer, a human freelancer taking a freelancer, a human freelancer taking over my content, find this useful? If over my content, find this useful? If over my content, find this useful? If you're already inside a project and you you're already inside a project and you

you're already inside a project and you want to set up this claude.md file, then want to set up this claude.md file, then want to set up this claude.md file, then you can run /init and it will actually you can run /init and it will actually you can run /init and it will actually go through your project repository and

go through your project repository and go through your project repository and create a claude.md file for you that you create a claude.md file for you that you create a claude.md file for you that you can go back and rectify and remove lines can go back and rectify and remove lines

can go back and rectify and remove lines from. But if you're starting from fresh, from. But if you're starting from fresh, from. But if you're starting from fresh, just copy the template and fill in the just copy the template and fill in the just copy the template and fill in the blanks as you build. Like Boris, fix

blanks as you build. Like Boris, fix blanks as you build. Like Boris, fix mistakes in real time and when something mistakes in real time and when something mistakes in real time and when something goes wrong midsession, you can just tell goes wrong midsession, you can just tell

goes wrong midsession, you can just tell it add this rule to my clawude. MD file it add this rule to my clawude. MD file it add this rule to my clawude. MD file and it will do it for you or you can add and it will do it for you or you can add and it will do it for you or you can add it directly into the lines. So at level

[10:11]

it directly into the lines. So at level it directly into the lines. So at level two, Claude is now following your two, Claude is now following your two, Claude is now following your personalization and your rules. And personalization and your rules. And

personalization and your rules. And Claude may be following your rules, but Claude may be following your rules, but Claude may be following your rules, but we're still having to start fresh every we're still having to start fresh every we're still having to start fresh every single time. We're typing the same

single time. We're typing the same single time. We're typing the same things over and over, like create me a things over and over, like create me a things over and over, like create me a LinkedIn post to get it to perform our LinkedIn post to get it to perform our

LinkedIn post to get it to perform our actions in the way we want. So level actions in the way we want. So level actions in the way we want. So level three is all about slash commands and three is all about slash commands and three is all about slash commands and skills. Now, you can just think of slash

skills. Now, you can just think of slash skills. Now, you can just think of slash commands as saved prompts that you can commands as saved prompts that you can commands as saved prompts that you can reuse with one keystroke. So tasks that reuse with one keystroke. So tasks that

reuse with one keystroke. So tasks that you're doing again and again that you you're doing again and again that you you're doing again and again that you can manually trigger at specific can manually trigger at specific can manually trigger at specific moments. So for example, we might say,

moments. So for example, we might say, moments. So for example, we might say, "Write me three LinkedIn posts about "Write me three LinkedIn posts about "Write me three LinkedIn posts about this topic." And all we'd have to do is this topic." And all we'd have to do is

this topic." And all we'd have to do is type in /in post and actually inside the type in /in post and actually inside the type in /in post and actually inside the command, the prompt says, "Write me command, the prompt says, "Write me command, the prompt says, "Write me three LinkedIn posts about this topic."

three LinkedIn posts about this topic." three LinkedIn posts about this topic." And then we actually pass in dynamically And then we actually pass in dynamically And then we actually pass in dynamically the topic name when we're prompting it the topic name when we're prompting it

the topic name when we're prompting it or commanding it. So the way that we do or commanding it. So the way that we do or commanding it. So the way that we do this is actually just creating a new this is actually just creating a new this is actually just creating a new folder inside our explorer called

folder inside our explorer called folder inside our explorer called Claude. And we'll keep using this folder Claude. And we'll keep using this folder Claude. And we'll keep using this folder /command. So it's a subfolder /command. So it's a subfolder

/command. So it's a subfolder inside.claude. And then inside that we inside.claude. And then inside that we inside.claude. And then inside that we would actually create a new command would actually create a new command would actually create a new command folder. Let's call it LinkedIn-post.md.

folder. Let's call it LinkedIn-post.md. folder. Let's call it LinkedIn-post.md. So it's a markdown file. Again, it's a So it's a markdown file. Again, it's a So it's a markdown file. Again, it's a folder inside of that command subfolder.

folder inside of that command subfolder. folder inside of that command subfolder. And we've got an example command here And we've got an example command here And we've got an example command here for our social media system. Write three for our social media system. Write three

for our social media system. Write three LinkedIn post variations about and then LinkedIn post variations about and then LinkedIn post variations about and then we've got this dollar arguments which is we've got this dollar arguments which is we've got this dollar arguments which is where we're going to pass in our dynamic

where we're going to pass in our dynamic where we're going to pass in our dynamic values which we'll show you in a second. values which we'll show you in a second.

values which we'll show you in a second. And then we've got some rules. So pull And then we've got some rules. So pull And then we've got some rules. So pull my brand voice from my brand voice from my brand voice from /doccks/brandvoice.nd.

/doccks/brandvoice.nd. /doccks/brandvoice.nd. Right now, we don't actually have that Right now, we don't actually have that Right now, we don't actually have that file, but we'll set that up next. Start file, but we'll set that up next. Start

file, but we'll set that up next. Start with a hook, then have a line break, with a hook, then have a line break, with a hook, then have a line break, then the body. So, this is specific then the body. So, this is specific then the body. So, this is specific context for this specific command. So,

context for this specific command. So, context for this specific command. So, think of this as a prompt for this think of this as a prompt for this think of this as a prompt for this command. End each post with a question command. End each post with a question

command. End each post with a question or CTA. Keep each post under 200 words, or CTA. Keep each post under 200 words, or CTA. Keep each post under 200 words, no hashtags, and then save the drafts to no hashtags, and then save the drafts to no hashtags, and then save the drafts to a /output/drafts folder. And right now,

a /output/drafts folder. And right now, a /output/drafts folder. And right now, that's not created, so it will that's not created, so it will that's not created, so it will automatically create that for us. Now, automatically create that for us. Now,

automatically create that for us. Now, if we just clear our memory here, this if we just clear our memory here, this if we just clear our memory here, this resets the claw code instance. and I resets the claw code instance. and I resets the claw code instance. and I start typing in the name of the command

start typing in the name of the command start typing in the name of the command LinkedIn- post. And for some reason, it LinkedIn- post. And for some reason, it LinkedIn- post. And for some reason, it doesn't show. So, what we need to do is doesn't show. So, what we need to do is

doesn't show. So, what we need to do is actually hit Ctrl + C. Close the session actually hit Ctrl + C. Close the session actually hit Ctrl + C. Close the session with Claude and reopen it with Claude.

[12:11]

with Claude and reopen it with Claude. with Claude and reopen it with Claude. And now, it should recognize when it's And now, it should recognize when it's And now, it should recognize when it's restarting that we have this restarting that we have this

restarting that we have this Claude/comands folder with this new Claude/comands folder with this new Claude/comands folder with this new command thing. And as soon as we hit command thing. And as soon as we hit command thing. And as soon as we hit slash, you can see that we've got our

slash, you can see that we've got our slash, you can see that we've got our new command linked in post in there. So, new command linked in post in there. So, new command linked in post in there. So, we're going to use the command linked we're going to use the command linked

we're going to use the command linked anti-gravity versus claude code. And anti-gravity versus claude code. And anti-gravity versus claude code. And it's going to understand now and pass it's going to understand now and pass it's going to understand now and pass that link anti-gravity versus claw code

that link anti-gravity versus claw code that link anti-gravity versus claw code as this argument. So it's going to say as this argument. So it's going to say as this argument. So it's going to say write three LinkedIn post variations write three LinkedIn post variations

write three LinkedIn post variations about this and follow these rules. So about this and follow these rules. So about this and follow these rules. So instead of typing this command every instead of typing this command every instead of typing this command every single time that I want to create a

single time that I want to create a single time that I want to create a post, I'm just going to use the slash post, I'm just going to use the slash post, I'm just going to use the slash command, pass my arguments, and now it's command, pass my arguments, and now it's

command, pass my arguments, and now it's going to add them to a draft folder. going to add them to a draft folder. going to add them to a draft folder. It's outputting our different variations It's outputting our different variations It's outputting our different variations in here, but we told it we also want it

in here, but we told it we also want it in here, but we told it we also want it to output them as documents in an to output them as documents in an to output them as documents in an outputs folder so that we have them outputs folder so that we have them

outputs folder so that we have them stored. So it's created this output stored. So it's created this output stored. So it's created this output folder. We've got the drafts and we can folder. We've got the drafts and we can folder. We've got the drafts and we can click in the specific file. Open that up

click in the specific file. Open that up click in the specific file. Open that up and we've got the variations here. I've and we've got the variations here. I've and we've got the variations here. I've been using both ag and claw code and you been using both ag and claw code and you

been using both ag and claw code and you can see it's now reading from our can see it's now reading from our can see it's now reading from our claw.md document which said actually claw.md document which said actually claw.md document which said actually replace it with ag. Don't use technical

replace it with ag. Don't use technical replace it with ag. Don't use technical jargon but also it's followed the slash jargon but also it's followed the slash jargon but also it's followed the slash command perfectly to create three command perfectly to create three

command perfectly to create three variations of LinkedIn post and then variations of LinkedIn post and then variations of LinkedIn post and then given us a summary down here of the given us a summary down here of the given us a summary down here of the hooks, the angles and the CTAs. Now, we

hooks, the angles and the CTAs. Now, we hooks, the angles and the CTAs. Now, we gave an example of writing three gave an example of writing three gave an example of writing three LinkedIn posts, but you can literally LinkedIn posts, but you can literally

LinkedIn posts, but you can literally turn any task that you do on a daily, turn any task that you do on a daily, turn any task that you do on a daily, weekly, monthly basis into one of these weekly, monthly basis into one of these weekly, monthly basis into one of these slash commands. The importance here is

slash commands. The importance here is slash commands. The importance here is you want to manually invoke or trigger you want to manually invoke or trigger you want to manually invoke or trigger it at certain moments. So, it could be it at certain moments. So, it could be

it at certain moments. So, it could be generate all posts for this week based generate all posts for this week based generate all posts for this week based on my notion calendar. This is where on my notion calendar. This is where on my notion calendar. This is where skills come in. And skills are slightly

skills come in. And skills are slightly skills come in. And skills are slightly different, but still represented as different, but still represented as different, but still represented as these slash commands down here. You can these slash commands down here. You can

these slash commands down here. You can think of skills as an upgraded version think of skills as an upgraded version think of skills as an upgraded version of slash commands. They're effectively of slash commands. They're effectively of slash commands. They're effectively background knowledge that's loaded in

background knowledge that's loaded in background knowledge that's loaded in automatically only when it's relevant. automatically only when it's relevant.

automatically only when it's relevant. So you don't need to trigger these, So you don't need to trigger these, So you don't need to trigger these, although you can tell Claude to use that although you can tell Claude to use that although you can tell Claude to use that specific skill. Claude just knows from

specific skill. Claude just knows from specific skill. Claude just knows from their project description and their their project description and their their project description and their skill description when it needs to use skill description when it needs to use

skill description when it needs to use that skill specifically. And unlike that skill specifically. And unlike that skill specifically. And unlike commands, which are fairly basic, one commands, which are fairly basic, one commands, which are fairly basic, one single file like LinkedIn postd skills

single file like LinkedIn postd skills single file like LinkedIn postd skills can include a whole folder of supporting can include a whole folder of supporting can include a whole folder of supporting files. So it can have for example for files. So it can have for example for

files. So it can have for example for our content creation, example posts, our content creation, example posts, our content creation, example posts, style guides, brand voice, reference style guides, brand voice, reference style guides, brand voice, reference docs. So it gives a richer set of

[14:14]

docs. So it gives a richer set of docs. So it gives a richer set of context for which claude code can context for which claude code can context for which claude code can actually work from. So skills are actually work from. So skills are

actually work from. So skills are effectively repeatable actions with effectively repeatable actions with effectively repeatable actions with context. And guess what? You don't need context. And guess what? You don't need context. And guess what? You don't need to create all the skills yourself. You

to create all the skills yourself. You to create all the skills yourself. You can actually get those skills from can actually get those skills from can actually get those skills from anywhere. And they're again going to sit anywhere. And they're again going to sit

anywhere. And they're again going to sit inside this. Claude folder. So if I inside this. Claude folder. So if I inside this. Claude folder. So if I click on the claude folder, create a new click on the claude folder, create a new click on the claude folder, create a new folder called skills. They're going to

folder called skills. They're going to folder called skills. They're going to sit under there with their skill.md file sit under there with their skill.md file sit under there with their skill.md file for specific skills. So you might have a for specific skills. So you might have a

for specific skills. So you might have a brand voice folder and inside that we'd brand voice folder and inside that we'd brand voice folder and inside that we'd have a skill.m MD file with supporting have a skill.m MD file with supporting have a skill.m MD file with supporting files inside that brand voice as well.

files inside that brand voice as well. files inside that brand voice as well. And we're going to look for a humanizer And we're going to look for a humanizer And we're going to look for a humanizer skill on skills MP that takes our skill on skills MP that takes our

skill on skills MP that takes our writing and creates more humanlike and writing and creates more humanlike and writing and creates more humanlike and less AI slop-like written context. So we less AI slop-like written context. So we less AI slop-like written context. So we can go down and browse agent skills

can go down and browse agent skills can go down and browse agent skills here, but it's easiest to browse by here, but it's easiest to browse by here, but it's easiest to browse by category. We're going to go to content category. We're going to go to content

category. We're going to go to content and media because we're creating social and media because we're creating social and media because we're creating social media content. And we will see very media content. And we will see very media content. And we will see very quickly we've got things like the

quickly we've got things like the quickly we've got things like the ability to actually create images using ability to actually create images using ability to actually create images using Nano Banana Pro, content creation, Nano Banana Pro, content creation,

Nano Banana Pro, content creation, technical writers, but what we're going technical writers, but what we're going technical writers, but what we're going to type in is human. And hopefully to type in is human. And hopefully to type in is human. And hopefully there's a humanizer we can grab from

there's a humanizer we can grab from there's a humanizer we can grab from here. We'll click inside that. And this here. We'll click inside that. And this here. We'll click inside that. And this one removes signs of AI generated one removes signs of AI generated

one removes signs of AI generated writing from text. Use it when editing writing from text. Use it when editing writing from text. Use it when editing or reviewing text to make it sound more or reviewing text to make it sound more or reviewing text to make it sound more natural and human written. This sounds

natural and human written. This sounds natural and human written. This sounds exactly what we're looking for. We're exactly what we're looking for. We're exactly what we're looking for. We're going to open up the GitHub repository going to open up the GitHub repository

going to open up the GitHub repository by clicking that button. And what we're by clicking that button. And what we're by clicking that button. And what we're going to do is grab this line here going to do is grab this line here going to do is grab this line here because we've already got our skills

because we've already got our skills because we've already got our skills folder and we're going to get clone into folder and we're going to get clone into folder and we're going to get clone into our own skills here. Now, you have a our own skills here. Now, you have a

our own skills here. Now, you have a choice. You can get clone it into your choice. You can get clone it into your choice. You can get clone it into your global directory using this uh squiggly global directory using this uh squiggly global directory using this uh squiggly line and slash. Or if I just want to

line and slash. Or if I just want to line and slash. Or if I just want to actually see the skill inside this actually see the skill inside this actually see the skill inside this directory, I'm going to install it directory, I'm going to install it

directory, I'm going to install it without the squig squiggly line and without the squig squiggly line and without the squig squiggly line and slash. And it's now going to clone that slash. And it's now going to clone that slash. And it's now going to clone that repo and add it inside our skills

repo and add it inside our skills repo and add it inside our skills folder. And we'll be able to see exactly folder. And we'll be able to see exactly folder. And we'll be able to see exactly what files make up that humanizer skill.

what files make up that humanizer skill. what files make up that humanizer skill. And if we go in the skill.md, this is And if we go in the skill.md, this is And if we go in the skill.md, this is effectively the context for this skill effectively the context for this skill

effectively the context for this skill that when claw code is understanding how that when claw code is understanding how that when claw code is understanding how to write a post, it's going to always to write a post, it's going to always to write a post, it's going to always look, okay, I'm going to create this in

look, okay, I'm going to create this in look, okay, I'm going to create this in a human-like way. And then it will a human-like way. And then it will a human-like way. And then it will absorb and read all the context only absorb and read all the context only

absorb and read all the context only when relevant of this skill.mmd. So it's when relevant of this skill.mmd. So it's when relevant of this skill.mmd. So it's a way to segregate and isolate that a way to segregate and isolate that a way to segregate and isolate that context without bloating our main

[16:14]

context without bloating our main context without bloating our main claude.md file in case the task is not claude.md file in case the task is not claude.md file in case the task is not related to actually humanizing text for related to actually humanizing text for

related to actually humanizing text for example. And it talks about personality example. And it talks about personality example. And it talks about personality and soul, how to add voice, how to add and soul, how to add voice, how to add and soul, how to add voice, how to add opinions, and gives clear examples in

opinions, and gives clear examples in opinions, and gives clear examples in this very comprehensive file that we this very comprehensive file that we this very comprehensive file that we didn't need to create for ourselves to didn't need to create for ourselves to

didn't need to create for ourselves to create humanlike writing very quickly. create humanlike writing very quickly. create humanlike writing very quickly. So, here's the key thing with a skill.

So, here's the key thing with a skill. So, here's the key thing with a skill. You effectively need a really, really You effectively need a really, really You effectively need a really, really precise description for Claude to precise description for Claude to

precise description for Claude to understand exactly when to use that understand exactly when to use that understand exactly when to use that skill. So, here we've got remove signs skill. So, here we've got remove signs skill. So, here we've got remove signs of AI generated writing from text. Use

of AI generated writing from text. Use of AI generated writing from text. Use when editing or reviewing text to make when editing or reviewing text to make when editing or reviewing text to make it sound more natural and human written.

it sound more natural and human written. it sound more natural and human written. So Claude will understand when we ask So Claude will understand when we ask So Claude will understand when we ask for a humanlike article to actually then for a humanlike article to actually then

for a humanlike article to actually then use this skill in its process and we use this skill in its process and we use this skill in its process and we don't need to say /humanizer but we can don't need to say /humanizer but we can don't need to say /humanizer but we can do if we wanted to so we can invoke it

do if we wanted to so we can invoke it do if we wanted to so we can invoke it manually but also automatically it will manually but also automatically it will manually but also automatically it will look to do that but the way we ensure look to do that but the way we ensure

look to do that but the way we ensure that in the claw.md file instead every that in the claw.md file instead every that in the claw.md file instead every time you write some content make sure time you write some content make sure time you write some content make sure you use the humanizer skill in

you use the humanizer skill in you use the humanizer skill in /kills/humanizer /kills/humanizer /kills/humanizer so now it will understand because we've so now it will understand because we've

so now it will understand because we've added it both globally and for this added it both globally and for this added it both globally and for this specific command and that it's going to specific command and that it's going to specific command and that it's going to use that skill when it tries to make

use that skill when it tries to make use that skill when it tries to make humanlike writing. Now, you could go and humanlike writing. Now, you could go and humanlike writing. Now, you could go and export entire libraries of content and export entire libraries of content and

export entire libraries of content and media and have, you know, 14,000 skills media and have, you know, 14,000 skills media and have, you know, 14,000 skills within your directory, but I prefer to within your directory, but I prefer to within your directory, but I prefer to control exactly what skills I'm getting

control exactly what skills I'm getting control exactly what skills I'm getting and actually just pull in the specific and actually just pull in the specific and actually just pull in the specific skills that I'm looking for so I know skills that I'm looking for so I know

skills that I'm looking for so I know when I'm invoking certain things and not when I'm invoking certain things and not when I'm invoking certain things and not blending things too much. So, you could blending things too much. So, you could blending things too much. So, you could do things like front-end design, SEO

do things like front-end design, SEO do things like front-end design, SEO review, email drafter, absolutely review, email drafter, absolutely review, email drafter, absolutely anything people have turned into a skill anything people have turned into a skill

anything people have turned into a skill and you can go through and edit those and you can go through and edit those and you can go through and edit those skills to your requirements, too. So, skills to your requirements, too. So, skills to your requirements, too. So, we're going to run our command again.

we're going to run our command again. we're going to run our command again. LinkedIn post anti-gravity versus claw LinkedIn post anti-gravity versus claw LinkedIn post anti-gravity versus claw code and we should have more naturally code and we should have more naturally

code and we should have more naturally written content and we've not had to do written content and we've not had to do written content and we've not had to do a huge amount of work. We've just a huge amount of work. We've just a huge amount of work. We've just installed the skill and already we

installed the skill and already we installed the skill and already we should be getting some really good should be getting some really good should be getting some really good outputs from this. I stopped using AG outputs from this. I stopped using AG

outputs from this. I stopped using AG last month. AG builds things fast. You last month. AG builds things fast. You last month. AG builds things fast. You describe what you want. It writes code.

describe what you want. It writes code. describe what you want. It writes code. You ship. The problem is what happens 6 You ship. The problem is what happens 6 You ship. The problem is what happens 6 weeks later when something breaks and weeks later when something breaks and

weeks later when something breaks and nobody on your team understands how it nobody on your team understands how it nobody on your team understands how it works. So, this is a lot clearer, a lot works. So, this is a lot clearer, a lot works. So, this is a lot clearer, a lot less AI slot-like. So, it's gone

less AI slot-like. So, it's gone less AI slot-like. So, it's gone through, written the posts, humanized through, written the posts, humanized through, written the posts, humanized them, and then actually even given us a them, and then actually even given us a

[18:16]

them, and then actually even given us a summary of the things that it's changed summary of the things that it's changed summary of the things that it's changed to make it sound more human. So, for to make it sound more human. So, for to make it sound more human. So, for example, these tools aren't competitors.

example, these tools aren't competitors. example, these tools aren't competitors. They're different answers to different They're different answers to different They're different answers to different questions. It's it's actually changed it questions. It's it's actually changed it

questions. It's it's actually changed it to the real question is, do you want to to the real question is, do you want to to the real question is, do you want to outsource your thinking or augment it?

outsource your thinking or augment it? outsource your thinking or augment it? So, we've got slash commands, which you So, we've got slash commands, which you So, we've got slash commands, which you want to manually invoke for certain want to manually invoke for certain

want to manually invoke for certain tasks. We've got skills, which are tasks. We've got skills, which are tasks. We've got skills, which are automatically invoked based on their automatically invoked based on their automatically invoked based on their description and can have a huge amount

description and can have a huge amount description and can have a huge amount of context in them. That brings us to of context in them. That brings us to of context in them. That brings us to the final part of level three, which are the final part of level three, which are

the final part of level three, which are hooks. Now, hooks don't require a brain. hooks. Now, hooks don't require a brain. hooks. Now, hooks don't require a brain. They don't require any LLM tokens They don't require any LLM tokens They don't require any LLM tokens specifically. They're just automatic

specifically. They're just automatic specifically. They're just automatic triggers, anything that you can do triggers, anything that you can do triggers, anything that you can do mechanically that fire off when Claude mechanically that fire off when Claude

mechanically that fire off when Claude code does something. And to use it, code does something. And to use it, code does something. And to use it, we're going to need to create a claude/ we're going to need to create a claude/ we're going to need to create a claude/ settings JSON inside our project file.

settings JSON inside our project file. settings JSON inside our project file. So, we're going to create a new file, So, we're going to create a new file, So, we're going to create a new file, and it's going to sit within our claude and it's going to sit within our claude

and it's going to sit within our claude file. And in our example for content file. And in our example for content file. And in our example for content creation, we might have a list of band creation, we might have a list of band creation, we might have a list of band words that we're going to check every

words that we're going to check every words that we're going to check every single content post for. and it's going single content post for. and it's going single content post for. and it's going to do that automatically. So, it doesn't to do that automatically. So, it doesn't

to do that automatically. So, it doesn't require any thinking at all. It's just require any thinking at all. It's just require any thinking at all. It's just check this text against these words.

check this text against these words. check this text against these words. It's very programmatic and it's going to It's very programmatic and it's going to It's very programmatic and it's going to do that every single time invoked after do that every single time invoked after

do that every single time invoked after we've created a LinkedIn post, for we've created a LinkedIn post, for we've created a LinkedIn post, for example. And therefore, we're not example. And therefore, we're not example. And therefore, we're not relying on the LLM to actually think

relying on the LLM to actually think relying on the LLM to actually think through this step. It's just through this step. It's just through this step. It's just automatically done the things that we automatically done the things that we

automatically done the things that we know should be true, like we're going to know should be true, like we're going to know should be true, like we're going to check for ban words. We're going to check for ban words. We're going to check for ban words. We're going to check for word count and flag if it's

check for word count and flag if it's check for word count and flag if it's over our limit. We're going to auto over our limit. We're going to auto over our limit. We're going to auto format into a certain specific format.

format into a certain specific format. format into a certain specific format. Those things don't require thinking Those things don't require thinking Those things don't require thinking power. So we turn them into hooks. And power. So we turn them into hooks. And

power. So we turn them into hooks. And the way that we do that is just copy the way that we do that is just copy the way that we do that is just copy this into our settings.json. We have this into our settings.json. We have this into our settings.json. We have this hooks outer object. It has a few

this hooks outer object. It has a few this hooks outer object. It has a few commands, but to be honest, I never commands, but to be honest, I never commands, but to be honest, I never write these myself. I always get Claude write these myself. I always get Claude

write these myself. I always get Claude to write the JSON object for me to say to write the JSON object for me to say to write the JSON object for me to say run this hook after this happens. And it run this hook after this happens. And it run this hook after this happens. And it will automatically do that. It can even

will automatically do that. It can even will automatically do that. It can even add it to your settings.json file. And add it to your settings.json file. And add it to your settings.json file. And now whenever we write a post, this is now whenever we write a post, this is

now whenever we write a post, this is going to run and make sure that no band going to run and make sure that no band going to run and make sure that no band words that no band words are in our uh words that no band words are in our uh words that no band words are in our uh output variations here. And I can just

output variations here. And I can just output variations here. And I can just say run the hook for band words on the say run the hook for band words on the say run the hook for band words on the output drafts to do it retrospectively.

output drafts to do it retrospectively. output drafts to do it retrospectively. But from now on, if we've got this in But from now on, if we've got this in But from now on, if we've got this in our settings.json and we've restarted our settings.json and we've restarted

our settings.json and we've restarted our instance, it will automatically run our instance, it will automatically run our instance, it will automatically run it on everything. And it will just it on everything. And it will just it on everything. And it will just appear like this. No band words found in

[20:20]

appear like this. No band words found in appear like this. No band words found in the output draft. So it gives us peace the output draft. So it gives us peace the output draft. So it gives us peace of mind that it's actually running that of mind that it's actually running that

of mind that it's actually running that hook. So the simple way to remember hook. So the simple way to remember hook. So the simple way to remember these three things are skills is how these three things are skills is how these three things are skills is how Claude thinks. So it's going to load the

Claude thinks. So it's going to load the Claude thinks. So it's going to load the skill with its context into its brain skill with its context into its brain skill with its context into its brain while working depending on the while working depending on the

while working depending on the description of the skill. So hooks are description of the skill. So hooks are description of the skill. So hooks are what happens automatically after claud what happens automatically after claud what happens automatically after claud code actually acts. And then commands

code actually acts. And then commands code actually acts. And then commands are just stuff that we want to trigger are just stuff that we want to trigger are just stuff that we want to trigger manually with a prompt that's fed into manually with a prompt that's fed into

manually with a prompt that's fed into the context when it runs. Now for every the context when it runs. Now for every the context when it runs. Now for every piece of content we write, it's only piece of content we write, it's only piece of content we write, it's only right that we should have a brand voice

right that we should have a brand voice right that we should have a brand voice skill in there. So I've gone ahead and skill in there. So I've gone ahead and skill in there. So I've gone ahead and created a brand voice skill with our created a brand voice skill with our

created a brand voice skill with our band words and phrases. It talks about band words and phrases. It talks about band words and phrases. It talks about how I sound, words I never use, platform how I sound, words I never use, platform how I sound, words I never use, platform specific rules, and then we've also fed

specific rules, and then we've also fed specific rules, and then we've also fed it a series of examples like best it a series of examples like best it a series of examples like best LinkedIn posts, best expost, etc. in LinkedIn posts, best expost, etc. in

LinkedIn posts, best expost, etc. in this examples file. Okay, so we're this examples file. Okay, so we're this examples file. Okay, so we're getting faster at performing actions by getting faster at performing actions by getting faster at performing actions by leveraging our own slash commands, other

leveraging our own slash commands, other leveraging our own slash commands, other people's skills, and running repeatable people's skills, and running repeatable people's skills, and running repeatable tests as hooks at the end of actions.

tests as hooks at the end of actions. tests as hooks at the end of actions. Now, up until this point, we're still Now, up until this point, we're still Now, up until this point, we're still doing everything inside of Clawude Code.

doing everything inside of Clawude Code. doing everything inside of Clawude Code. So, we're not actually taking actions So, we're not actually taking actions So, we're not actually taking actions using our day-to-day apps like Air Table using our day-to-day apps like Air Table

using our day-to-day apps like Air Table or Notion. So level four is about or Notion. So level four is about or Notion. So level four is about connecting to everything using MCP connecting to everything using MCP connecting to everything using MCP servers. So an MCP server is a model

servers. So an MCP server is a model servers. So an MCP server is a model context protocol server which is context protocol server which is context protocol server which is effectively just a bridge between claude effectively just a bridge between claude

effectively just a bridge between claude code and an external app. So instead of code and an external app. So instead of code and an external app. So instead of copying data out of air table and then copying data out of air table and then copying data out of air table and then pasting it into claude say we have our

pasting it into claude say we have our pasting it into claude say we have our content ideas stored in air table. We content ideas stored in air table. We content ideas stored in air table. We just get Claude to actually connect to just get Claude to actually connect to

just get Claude to actually connect to our app automatically via the MCP server our app automatically via the MCP server our app automatically via the MCP server read our content calendar and then read our content calendar and then read our content calendar and then create posts based on our ideas in our

create posts based on our ideas in our create posts based on our ideas in our content calendar. Let's bring it to life content calendar. Let's bring it to life content calendar. Let's bring it to life by showing you how to set this up with by showing you how to set this up with

by showing you how to set this up with air tableable. And we have this MCP air tableable. And we have this MCP air tableable. And we have this MCP command inside here. And you don't even command inside here. And you don't even command inside here. And you don't even need to do this anymore. You can just

need to do this anymore. You can just need to do this anymore. You can just ask your code to set up the Air Table ask your code to set up the Air Table ask your code to set up the Air Table MCP for you. But I'm going to show you MCP for you. But I'm going to show you

MCP for you. But I'm going to show you how to actually do this for a specific how to actually do this for a specific how to actually do this for a specific MCP server. And we can have a ton of MCP MCP server. And we can have a ton of MCP MCP server. And we can have a ton of MCP servers available again to connect to

servers available again to connect to servers available again to connect to all of your different apps at a repo all of your different apps at a repo all of your different apps at a repo like the one here, which is just a list like the one here, which is just a list

like the one here, which is just a list of literally thousands of services that of literally thousands of services that of literally thousands of services that we can automatically connect to. So we we can automatically connect to. So we we can automatically connect to. So we just add it to the project route. We can

just add it to the project route. We can just add it to the project route. We can literally create a new file MCP.json literally create a new file MCP.json literally create a new file MCP.json and we can paste that code in and it's and we can paste that code in and it's

[22:24]

and we can paste that code in and it's basically saying pick up these MCP basically saying pick up these MCP basically saying pick up these MCP servers and then we need to actually servers and then we need to actually servers and then we need to actually insert our air table API key for

insert our air table API key for insert our air table API key for example. But if you didn't want to do example. But if you didn't want to do example. But if you didn't want to do that, we could actually remove this and that, we could actually remove this and

that, we could actually remove this and just use the command /mcp which is built just use the command /mcp which is built just use the command /mcp which is built in add air table and it will start in add air table and it will start in add air table and it will start setting up this mcp.json file for us.

setting up this mcp.json file for us. setting up this mcp.json file for us. And then taking for example our air And then taking for example our air And then taking for example our air tableable personal access token which tableable personal access token which

tableable personal access token which for air tableable we can get from for air tableable we can get from for air tableable we can get from airtable.com/create/token/new give it a name clawed code and we're give it a name clawed code and we're going to give it the scopes of reading

going to give it the scopes of reading going to give it the scopes of reading records writing records and access to records writing records and access to records writing records and access to actually the bases the air table bases actually the bases the air table bases

actually the bases the air table bases too. So we need to actually give it too. So we need to actually give it too. So we need to actually give it access to a given base and we've got one access to a given base and we've got one access to a given base and we've got one where we have our LinkedIn carousel

where we have our LinkedIn carousel where we have our LinkedIn carousel ideas. So we're going to create a token ideas. So we're going to create a token ideas. So we're going to create a token for that. We're going to copy that token for that. We're going to copy that token

for that. We're going to copy that token and we're going to bring it back and and we're going to bring it back and and we're going to bring it back and effectively feed that into either the effectively feed that into either the effectively feed that into either the MCP.json file or just give it to Claude

MCP.json file or just give it to Claude MCP.json file or just give it to Claude to add that for us. So, it's created the to add that for us. So, it's created the to add that for us. So, it's created the MCP.json format for us. We're going to MCP.json format for us. We're going to

MCP.json format for us. We're going to paste in our access token and it says paste in our access token and it says paste in our access token and it says restart Claude code to confirm the restart Claude code to confirm the restart Claude code to confirm the setup. So, we're going to crl C to shut

setup. So, we're going to crl C to shut setup. So, we're going to crl C to shut down the claw code instance. We're going down the claw code instance. We're going down the claw code instance. We're going to hit claude again and we're going to to hit claude again and we're going to

to hit claude again and we're going to just test that we actually have that just test that we actually have that just test that we actually have that connection set up for our Air Table. So, connection set up for our Air Table. So, connection set up for our Air Table. So, we're just going to hit what Air Table

we're just going to hit what Air Table we're just going to hit what Air Table bases do I have? And it should bases do I have? And it should bases do I have? And it should understand that it needs to use the Air understand that it needs to use the Air

understand that it needs to use the Air Table MCP to actually make that request. Table MCP to actually make that request. Table MCP to actually make that request. And it's going to return a list of bases And it's going to return a list of bases And it's going to return a list of bases that it has access to, which should just

that it has access to, which should just that it has access to, which should just be that single uh LinkedIn carousels be that single uh LinkedIn carousels be that single uh LinkedIn carousels base. Would you like me to explore the base. Would you like me to explore the

base. Would you like me to explore the tables within this base? Yes, show me tables within this base? Yes, show me tables within this base? Yes, show me the tables. So, we're already reading the tables. So, we're already reading the tables. So, we're already reading access from our tables, but we can also

access from our tables, but we can also access from our tables, but we can also take actions with those tables. And if take actions with those tables. And if take actions with those tables. And if we open up the table, we've got a bunch we open up the table, we've got a bunch

we open up the table, we've got a bunch of content ideas from mid Jan. And you of content ideas from mid Jan. And you of content ideas from mid Jan. And you can see it's pulled out all the can see it's pulled out all the can see it's pulled out all the different tables and the key fields

different tables and the key fields different tables and the key fields inside those tables as well. This looks inside those tables as well. This looks inside those tables as well. This looks like a content pipeline for LinkedIn like a content pipeline for LinkedIn

like a content pipeline for LinkedIn carousels. Ideas flow into draft posts carousels. Ideas flow into draft posts carousels. Ideas flow into draft posts with a brand voice and design templates with a brand voice and design templates with a brand voice and design templates applied along the way. So it's nailed it

applied along the way. So it's nailed it applied along the way. So it's nailed it from just that MCP understanding of the from just that MCP understanding of the from just that MCP understanding of the fields and the descriptions. It fields and the descriptions. It

fields and the descriptions. It understands exactly the content it's understands exactly the content it's understands exactly the content it's looking at. So this is where things get looking at. So this is where things get looking at. So this is where things get really powerful because if we wanted to

really powerful because if we wanted to really powerful because if we wanted to combine our content creation system with combine our content creation system with combine our content creation system with a content pipeline that we're storing in a content pipeline that we're storing in

[24:28]

a content pipeline that we're storing in air table for example we could say pull air table for example we could say pull air table for example we could say pull all ideas from after Jan the 20th which all ideas from after Jan the 20th which all ideas from after Jan the 20th which was actually just one idea it should be

was actually just one idea it should be was actually just one idea it should be able to pull that specific record from able to pull that specific record from able to pull that specific record from the air table which is a transcript of a the air table which is a transcript of a

the air table which is a transcript of a video that I created and what we're video that I created and what we're video that I created and what we're going to do is actually push that into going to do is actually push that into going to do is actually push that into our slash command to create a post or

our slash command to create a post or our slash command to create a post or variations of post for us. So, we're variations of post for us. So, we're variations of post for us. So, we're going to say take this idea and we're going to say take this idea and we're

going to say take this idea and we're going to use our slash command / going to use our slash command / going to use our slash command / LinkedIn post. And what it's going to do LinkedIn post. And what it's going to do LinkedIn post. And what it's going to do is then take the idea, take the

is then take the idea, take the is then take the idea, take the transcript of that idea and turn it into transcript of that idea and turn it into transcript of that idea and turn it into three variations of LinkedIn post. And three variations of LinkedIn post. And

three variations of LinkedIn post. And we can then demonstrate that we can add we can then demonstrate that we can add we can then demonstrate that we can add it back into our field inside Air Table.

it back into our field inside Air Table. it back into our field inside Air Table. So, if we're managing our content So, if we're managing our content So, if we're managing our content pipeline in Air Table, we can still pipeline in Air Table, we can still

pipeline in Air Table, we can still actually interact and do things with actually interact and do things with actually interact and do things with clawed code, but actually then put those clawed code, but actually then put those clawed code, but actually then put those inputs or the outputs back into our

inputs or the outputs back into our inputs or the outputs back into our table where we work every day. And table where we work every day. And table where we work every day. And that's the power of connecting to the that's the power of connecting to the

that's the power of connecting to the data through an MCP server. So it says data through an MCP server. So it says data through an MCP server. So it says it's done the three variations, added it's done the three variations, added it's done the three variations, added them to here. So update the record table

them to here. So update the record table them to here. So update the record table with just idea three in the system with just idea three in the system with just idea three in the system message uh column. Everyone's talking message uh column. Everyone's talking

message uh column. Everyone's talking about AI coding tools. Most of the demos about AI coding tools. Most of the demos about AI coding tools. Most of the demos are underwhelming. Um so now we are are underwhelming. Um so now we are are underwhelming. Um so now we are giving it permission to actually go

giving it permission to actually go giving it permission to actually go through and add that directly into our through and add that directly into our through and add that directly into our data where we work every day. So we have data where we work every day. So we have

data where we work every day. So we have our content pipeline being updated by our content pipeline being updated by our content pipeline being updated by our claude code instance and it's saying our claude code instance and it's saying our claude code instance and it's saying it's now updated the record. We can go

it's now updated the record. We can go it's now updated the record. We can go along and we can see that it's just along and we can see that it's just along and we can see that it's just added to the system message. Everyone's added to the system message. Everyone's

added to the system message. Everyone's talking about AI coding tools. Most of talking about AI coding tools. Most of talking about AI coding tools. Most of the demos are underwhelming. So, it can the demos are underwhelming. So, it can the demos are underwhelming. So, it can work exactly where we're working and

work exactly where we're working and work exactly where we're working and it's updated that row perfectly. So, at it's updated that row perfectly. So, at it's updated that row perfectly. So, at level four, then we're taking actions level four, then we're taking actions

level four, then we're taking actions directly in our apps, reading the data, directly in our apps, reading the data, directly in our apps, reading the data, adding things back to the data, adding things back to the data, adding things back to the data, updating. It's gone through a full plan

updating. It's gone through a full plan updating. It's gone through a full plan and execute loop. So far, we're no and execute loop. So far, we're no and execute loop. So far, we're no longer needing to do manual updates in longer needing to do manual updates in

longer needing to do manual updates in our apps directly, and it's using the our apps directly, and it's using the our apps directly, and it's using the skills that we've given it as well. But skills that we've given it as well. But skills that we've given it as well. But so far, we're still having to contribute

so far, we're still having to contribute so far, we're still having to contribute the majority of the thinking time to the majority of the thinking time to the majority of the thinking time to this and planning efforts for Claude.

this and planning efforts for Claude. this and planning efforts for Claude. But why not leverage a framework like But why not leverage a framework like But why not leverage a framework like GSD to plan in high detail and then move GSD to plan in high detail and then move

GSD to plan in high detail and then move us to a supervisor role instead of us to a supervisor role instead of us to a supervisor role instead of somebody who's executing these things on somebody who's executing these things on somebody who's executing these things on a day-to-day? So GST is all about

[26:30]

a day-to-day? So GST is all about a day-to-day? So GST is all about removing us from the thinking home removing us from the thinking home removing us from the thinking home overhead. And it's a framework that overhead. And it's a framework that

overhead. And it's a framework that takes skills one step further. And what takes skills one step further. And what takes skills one step further. And what this framework is designed to do is this framework is designed to do is this framework is designed to do is break down huge projects into individual

break down huge projects into individual break down huge projects into individual phases and execute a loop of let's plan phases and execute a loop of let's plan phases and execute a loop of let's plan the phase first, let's execute the phase the phase first, let's execute the phase

the phase first, let's execute the phase second, and let's verify using user second, and let's verify using user second, and let's verify using user acceptance testing methods that the acceptance testing methods that the acceptance testing methods that the phase has been completed successfully.

phase has been completed successfully. phase has been completed successfully. So this is great for where you've not So this is great for where you've not So this is great for where you've not got a really defined scope and you have got a really defined scope and you have

got a really defined scope and you have a larger project that you want to a larger project that you want to a larger project that you want to effectively build out in great detail so effectively build out in great detail so effectively build out in great detail so that it can be run on your behalf. And

that it can be run on your behalf. And that it can be run on your behalf. And when we start planning the project, it's when we start planning the project, it's when we start planning the project, it's going to leverage that ask user going to leverage that ask user

going to leverage that ask user questions to actually come through and questions to actually come through and questions to actually come through and get a full understanding of all of the get a full understanding of all of the get a full understanding of all of the project scope, all the dependencies, all

project scope, all the dependencies, all project scope, all the dependencies, all of our assumptions, and exactly how we of our assumptions, and exactly how we of our assumptions, and exactly how we want to build it out. And it's like want to build it out. And it's like

want to build it out. And it's like planning on steroids. It's going to planning on steroids. It's going to planning on steroids. It's going to break down individual to-dos inside break down individual to-dos inside break down individual to-dos inside individual phases that are going to be

individual phases that are going to be individual phases that are going to be marked as completed as it goes through marked as completed as it goes through marked as completed as it goes through and executes on that brief. And the and executes on that brief. And the

and executes on that brief. And the reason that power users use a framework reason that power users use a framework reason that power users use a framework like this is because a huge problem with like this is because a huge problem with like this is because a huge problem with Claude during long sessions is that we

Claude during long sessions is that we Claude during long sessions is that we actually fill up the context window. So actually fill up the context window. So actually fill up the context window. So you can see down here with this bar, you can see down here with this bar,

you can see down here with this bar, we're at 50% of the maximum context we're at 50% of the maximum context we're at 50% of the maximum context window that Claude code can take. As window that Claude code can take. As window that Claude code can take. As soon as we get towards 95%, Claude is

soon as we get towards 95%, Claude is soon as we get towards 95%, Claude is going to automatically compress all that going to automatically compress all that going to automatically compress all that context into summaries and we're not context into summaries and we're not

context into summaries and we're not going to be able to find it. This is going to be able to find it. This is going to be able to find it. This is something known as context rot, which is something known as context rot, which is something known as context rot, which is basically as we increase the number of

basically as we increase the number of basically as we increase the number of input tokens, our reliability on the input tokens, our reliability on the input tokens, our reliability on the output gets less to the point where if output gets less to the point where if

output gets less to the point where if we're actually putting in 10,000 tokens we're actually putting in 10,000 tokens we're actually putting in 10,000 tokens or around 7,500 words, we lose 50% of or around 7,500 words, we lose 50% of or around 7,500 words, we lose 50% of the context. Now, a framework like GSD

the context. Now, a framework like GSD the context. Now, a framework like GSD helps tackle this because it actually helps tackle this because it actually helps tackle this because it actually keeps context in individual files. So we keeps context in individual files. So we

keeps context in individual files. So we have overall project documents that are have overall project documents that are have overall project documents that are spun up like road map requirements and spun up like road map requirements and spun up like road map requirements and state, but we also have context that's

state, but we also have context that's state, but we also have context that's kept in specific phase level documents kept in specific phase level documents kept in specific phase level documents with to-do level tasks. And you can see with to-do level tasks. And you can see

with to-do level tasks. And you can see this demonstrated in a previous video this demonstrated in a previous video this demonstrated in a previous video that I did that I'll link above where I that I did that I'll link above where I that I did that I'll link above where I built out an entire SAS application. So

built out an entire SAS application. So built out an entire SAS application. So a large project using the GSD framework. a large project using the GSD framework.

a large project using the GSD framework. So it takes planning to the next level. So it takes planning to the next level. So it takes planning to the next level. We have a dot planning folder with the We have a dot planning folder with the We have a dot planning folder with the project road map which is going to tell

[28:31]

project road map which is going to tell project road map which is going to tell you exactly what the phases are about. you exactly what the phases are about.

you exactly what the phases are about. We have foundation and authentication. We have foundation and authentication. We have foundation and authentication. We have data management. We have the AI We have data management. We have the AI We have data management. We have the AI generation pipeline and things like

generation pipeline and things like generation pipeline and things like payments. We have the state which is a payments. We have the state which is a payments. We have the state which is a document which tells us actually which document which tells us actually which

document which tells us actually which plans have been executed and which need plans have been executed and which need plans have been executed and which need to be done. So it's a memory of what to be done. So it's a memory of what to be done. So it's a memory of what progress we've made against the given

progress we've made against the given progress we've made against the given plan. And then we've got various other plan. And then we've got various other plan. And then we've got various other highle documents which feed in context highle documents which feed in context

highle documents which feed in context at the relevant points and solve that at the relevant points and solve that at the relevant points and solve that context for problem. Not to mention each context for problem. Not to mention each context for problem. Not to mention each phase is individually broken down into a

phase is individually broken down into a phase is individually broken down into a series of waves and tasks. So inside, series of waves and tasks. So inside, series of waves and tasks. So inside, for example, phase 5, Stripe billing, we for example, phase 5, Stripe billing, we

for example, phase 5, Stripe billing, we have a plan of what we're going to do have a plan of what we're going to do have a plan of what we're going to do for the first part of Stripe billing. We for the first part of Stripe billing. We for the first part of Stripe billing. We have a summary of what's been executed

have a summary of what's been executed have a summary of what's been executed when we run the execute command. And when we run the execute command. And when we run the execute command. And then we also have a user acceptance then we also have a user acceptance

then we also have a user acceptance testing file that runs through and testing file that runs through and testing file that runs through and automatically tells us what to test automatically tells us what to test automatically tells us what to test based on our Stripe billing requirements

based on our Stripe billing requirements based on our Stripe billing requirements in the first place. So at level five, in the first place. So at level five, in the first place. So at level five, we've taken planning to the next level we've taken planning to the next level

we've taken planning to the next level by using the GSD framework, but we're by using the GSD framework, but we're by using the GSD framework, but we're still just supervising one agent whilst still just supervising one agent whilst still just supervising one agent whilst we get on with other tasks in the

we get on with other tasks in the we get on with other tasks in the background. So why not instead run a background. So why not instead run a background. So why not instead run a team of agents that can verify each team of agents that can verify each

team of agents that can verify each other's work? And that brings us to other's work? And that brings us to other's work? And that brings us to level six where instead of one claude level six where instead of one claude level six where instead of one claude doing everything, researching, writing,

doing everything, researching, writing, doing everything, researching, writing, reviewing, you just split the jobs into reviewing, you just split the jobs into reviewing, you just split the jobs into separate sub aents. And ultimately, we separate sub aents. And ultimately, we

separate sub aents. And ultimately, we do this to increase our leverage. And do this to increase our leverage. And do this to increase our leverage. And it's summarized really well inside this it's summarized really well inside this it's summarized really well inside this Reddit thread by Sax Appeal and Kite. So

Reddit thread by Sax Appeal and Kite. So Reddit thread by Sax Appeal and Kite. So sub agents are specialized personas that sub agents are specialized personas that sub agents are specialized personas that you may want to offload specific types you may want to offload specific types

you may want to offload specific types of work to. And basically each agent has of work to. And basically each agent has of work to. And basically each agent has a fresh context that is then able to be a fresh context that is then able to be a fresh context that is then able to be pulled into your main context window

pulled into your main context window pulled into your main context window that's fed by your claw.md. So use sub that's fed by your claw.md. So use sub that's fed by your claw.md. So use sub aents to keep your context clean, i.e.

aents to keep your context clean, i.e. aents to keep your context clean, i.e. stop that context rot. But also it's stop that context rot. But also it's stop that context rot. But also it's about context isolation. The sub aent about context isolation. The sub aent

about context isolation. The sub aent therefore is not going to bloat your therefore is not going to bloat your therefore is not going to bloat your main agents context. So it makes your main agents context. So it makes your main agents context. So it makes your responses much faster if you're

responses much faster if you're responses much faster if you're executing it as a sub agent and also executing it as a sub agent and also executing it as a sub agent and also cheaper because you're using fewer cheaper because you're using fewer

cheaper because you're using fewer tokens because you've given it less tokens because you've given it less tokens because you've given it less context or isolated context. And you do context or isolated context. And you do context or isolated context. And you do this particularly when you're working on

this particularly when you're working on this particularly when you're working on a problem that requires a lot of a problem that requires a lot of a problem that requires a lot of expertise. So break down a bigger expertise. So break down a bigger

expertise. So break down a bigger project into its components and let project into its components and let project into its components and let agents work on it in either sequence or agents work on it in either sequence or agents work on it in either sequence or parallel. So for our content creation

[30:35]

parallel. So for our content creation parallel. So for our content creation system, this might be represented like a system, this might be represented like a system, this might be represented like a content research team. So we might have content research team. So we might have

content research team. So we might have a researcher sub agent one which is a researcher sub agent one which is a researcher sub agent one which is in-depth research with access to in-depth research with access to in-depth research with access to additional tools that the main cloud

additional tools that the main cloud additional tools that the main cloud code instant doesn't have access to. We code instant doesn't have access to. We code instant doesn't have access to. We then have our main instance which is then have our main instance which is

then have our main instance which is here which we've been using so far which here which we've been using so far which here which we've been using so far which is our content writer. And then we might is our content writer. And then we might is our content writer. And then we might also have a reviewer, a second sub agent

also have a reviewer, a second sub agent also have a reviewer, a second sub agent that can only suggest edits to things that can only suggest edits to things that can only suggest edits to things we've already written but not make we've already written but not make

we've already written but not make edits. Now there are two main reasons edits. Now there are two main reasons edits. Now there are two main reasons that you might run a team. The first is that you might run a team. The first is that you might run a team. The first is to improve our output quality. So if you

to improve our output quality. So if you to improve our output quality. So if you think of a specialist versus generalist, think of a specialist versus generalist, think of a specialist versus generalist, we might have one claude delegating to we might have one claude delegating to

we might have one claude delegating to specialists like a researcher within the specialists like a researcher within the specialists like a researcher within the same session. And the main claude agent same session. And the main claude agent same session. And the main claude agent that we've been using might call the

that we've been using might call the that we've been using might call the researcher sub agent, receive the researcher sub agent, receive the researcher sub agent, receive the research brief back, and then use that research brief back, and then use that

research brief back, and then use that research to write because the main research to write because the main research to write because the main instance is the writer. And this would instance is the writer. And this would instance is the writer. And this would all happen in one terminal window. Or if

all happen in one terminal window. Or if all happen in one terminal window. Or if our main goal is actually to get things our main goal is actually to get things our main goal is actually to get things done faster and work on multiple done faster and work on multiple

done faster and work on multiple non-dependent tasks at once, then we non-dependent tasks at once, then we non-dependent tasks at once, then we might have parallel terminals opening up might have parallel terminals opening up might have parallel terminals opening up new terminal windows where we might for

new terminal windows where we might for new terminal windows where we might for example have tab one working on writing example have tab one working on writing example have tab one working on writing LinkedIn posts, tab two working on LinkedIn posts, tab two working on

LinkedIn posts, tab two working on writing Instagram posts and tab three writing Instagram posts and tab three writing Instagram posts and tab three doing something else as well. So those doing something else as well. So those doing something else as well. So those two never interact, but the value we're

two never interact, but the value we're two never interact, but the value we're getting from those sub aents in parallel getting from those sub aents in parallel getting from those sub aents in parallel is the speed, not that they're able to is the speed, not that they're able to

is the speed, not that they're able to collaborate and specialize on certain collaborate and specialize on certain collaborate and specialize on certain things. And the master of this is Boris things. And the master of this is Boris things. And the master of this is Boris himself who runs five claudes in

himself who runs five claudes in himself who runs five claudes in parallel in his terminal. You can see parallel in his terminal. You can see parallel in his terminal. You can see the tabs where he switches between the the tabs where he switches between the

the tabs where he switches between the different chords and gets system different chords and gets system different chords and gets system notifications when it needs his input.

notifications when it needs his input. notifications when it needs his input. But he also runs 5 to 10 claudes on But he also runs 5 to 10 claudes on But he also runs 5 to 10 claudes on [music] claude.ai/code [music] claude.ai/code

[music] claude.ai/code as well in parallel with the local. So as well in parallel with the local. So as well in parallel with the local. So he's getting a lot done by running sub he's getting a lot done by running sub he's getting a lot done by running sub aents. But he goes on to mention that he

aents. But he goes on to mention that he aents. But he goes on to mention that he uses actually few sub aents regularly. uses actually few sub aents regularly.

uses actually few sub aents regularly. Just stuff that automates some of the Just stuff that automates some of the Just stuff that automates some of the most common workflows that he goes most common workflows that he goes most common workflows that he goes through. So let's set up our agent team

through. So let's set up our agent team through. So let's set up our agent team here to demonstrate. So again, it's here to demonstrate. So again, it's here to demonstrate. So again, it's going to sit under Claude. Instead of going to sit under Claude. Instead of

going to sit under Claude. Instead of the commands and skills, we're going to the commands and skills, we're going to the commands and skills, we're going to create an agents folder. And inside that create an agents folder. And inside that create an agents folder. And inside that folder, we're creating a content

folder, we're creating a content folder, we're creating a content researcher MD file, which is basically researcher MD file, which is basically researcher MD file, which is basically going to be our agent with a prompt going to be our agent with a prompt

going to be our agent with a prompt that's basically a research specialist that's basically a research specialist that's basically a research specialist for a social media content team. Now, for a social media content team. Now, for a social media content team. Now, this is just a fairly basic agent and

[32:37]

this is just a fairly basic agent and this is just a fairly basic agent and actually could be run as a skill or a actually could be run as a skill or a actually could be run as a skill or a command, but it just demonstrates how command, but it just demonstrates how

command, but it just demonstrates how you would actually use this. And agents you would actually use this. And agents you would actually use this. And agents would often have a lot more context would often have a lot more context would often have a lot more context because they're doing a very specialized

because they're doing a very specialized because they're doing a very specialized task. So, we're going to copy paste that task. So, we're going to copy paste that task. So, we're going to copy paste that in there. We've got the description.

in there. We've got the description. in there. We've got the description. We've got the allowed tools that it's We've got the allowed tools that it's We've got the allowed tools that it's allowed to use. And it's going basically allowed to use. And it's going basically

allowed to use. And it's going basically going out to find interesting angles on going out to find interesting angles on going out to find interesting angles on a given topic. So, it's content a given topic. So, it's content a given topic. So, it's content researching for us. We're then going to

researching for us. We're then going to researching for us. We're then going to set up our content reviewer. Again, we set up our content reviewer. Again, we set up our content reviewer. Again, we don't have a specific folder for this, don't have a specific folder for this,

don't have a specific folder for this, but we're going to set up just as a MD but we're going to set up just as a MD but we're going to set up just as a MD file. And this is all about after it's file. And this is all about after it's file. And this is all about after it's been created, review the drafted social

been created, review the drafted social been created, review the drafted social media post against the brand voice media post against the brand voice media post against the brand voice guidelines and platform rules. So we can guidelines and platform rules. So we can

guidelines and platform rules. So we can demonstrate now with a single task how demonstrate now with a single task how demonstrate now with a single task how you can get them to work together in one you can get them to work together in one you can get them to work together in one terminal and then the second task will

terminal and then the second task will terminal and then the second task will be working two terminals in parallel. So be working two terminals in parallel. So be working two terminals in parallel. So we're going to pull an idea from the air we're going to pull an idea from the air

we're going to pull an idea from the air table content calendar. We're going to table content calendar. We're going to table content calendar. We're going to use the content researcher sub agent to use the content researcher sub agent to use the content researcher sub agent to research angles and then use that

research angles and then use that research angles and then use that research to and then invoke the command research to and then invoke the command research to and then invoke the command LinkedIn post on that topic. So you can LinkedIn post on that topic. So you can

LinkedIn post on that topic. So you can see how we're building every time on see how we're building every time on see how we're building every time on that. And then we're going to use the that. And then we're going to use the that. And then we're going to use the content reviewer to review the [music]

content reviewer to review the [music] content reviewer to review the [music] drafts. And if I wanted multiple ideas drafts. And if I wanted multiple ideas drafts. And if I wanted multiple ideas to be processed at once, I could open up to be processed at once, I could open up

to be processed at once, I could open up a new terminal whilst that runs in the a new terminal whilst that runs in the a new terminal whilst that runs in the background. We'd open up a new clawed background. We'd open up a new clawed background. We'd open up a new clawed instance, we can demonstrate the speed

instance, we can demonstrate the speed instance, we can demonstrate the speed of doing multiple in parallel now. So of doing multiple in parallel now. So of doing multiple in parallel now. So we've now got two terminals actually we've now got two terminals actually

we've now got two terminals actually open and we're executing on both of open and we're executing on both of open and we're executing on both of those terminals. So we need to give this those terminals. So we need to give this those terminals. So we need to give this the go ahead on permissions here. And

the go ahead on permissions here. And the go ahead on permissions here. And the first one is launching the content the first one is launching the content the first one is launching the content researcher. The second one is starting researcher. The second one is starting

researcher. The second one is starting to actually access the air table data as to actually access the air table data as to actually access the air table data as well. So we could launch multiple well. So we could launch multiple well. So we could launch multiple terminals and have them side by side in

terminals and have them side by side in terminals and have them side by side in this view here to both get higher this view here to both get higher this view here to both get higher quality outputs but also run them quality outputs but also run them

quality outputs but also run them faster. So if we need multiple of the faster. So if we need multiple of the faster. So if we need multiple of the same things doing at once, we can run same things doing at once, we can run same things doing at once, we can run multiple shells, multiple commands at

multiple shells, multiple commands at multiple shells, multiple commands at once. And I can even open up multiple once. And I can even open up multiple once. And I can even open up multiple more instances if I have the capacity more instances if I have the capacity

more instances if I have the capacity myself to actually supervise these. Now myself to actually supervise these. Now myself to actually supervise these. Now if you only have to approve a few if you only have to approve a few if you only have to approve a few things, this is okay. But as soon as you

things, this is okay. But as soon as you things, this is okay. But as soon as you start approving absolutely every action start approving absolutely every action start approving absolutely every action you take, then you're going to want to you take, then you're going to want to

you take, then you're going to want to use what's called Claude dangerously use what's called Claude dangerously use what's called Claude dangerously skip permissions, which as it sounds skip permissions, which as it sounds skip permissions, which as it sounds basically says, I'm not going to ask for

basically says, I'm not going to ask for basically says, I'm not going to ask for any permission to access any file that any permission to access any file that any permission to access any file that you're giving me access to. I'm just you're giving me access to. I'm just

[34:37]

you're giving me access to. I'm just going to go ahead and do it. So if we going to go ahead and do it. So if we going to go ahead and do it. So if we start Claude with this d-dangerously start Claude with this d-dangerously start Claude with this d-dangerously skip permissions, it's going to start

skip permissions, it's going to start skip permissions, it's going to start and tell us, do you trust everything in and tell us, do you trust everything in and tell us, do you trust everything in this folder? Am I able to actually go this folder? Am I able to actually go

this folder? Am I able to actually go ahead and skip permissions? So we're ahead and skip permissions? So we're ahead and skip permissions? So we're accepting liability for any actions it's accepting liability for any actions it's accepting liability for any actions it's going to take. And you can see we've got

going to take. And you can see we've got going to take. And you can see we've got this bypass permissions on here as well. this bypass permissions on here as well.

this bypass permissions on here as well. And we could again feed this new And we could again feed this new And we could again feed this new instance the same task and it will run instance the same task and it will run instance the same task and it will run in parallel to everything we're doing so

in parallel to everything we're doing so in parallel to everything we're doing so far. So we've got four three or four far. So we've got four three or four far. So we've got four three or four windows running in parallel, same sub windows running in parallel, same sub

windows running in parallel, same sub aent doing the same thing, pulling a aent doing the same thing, pulling a aent doing the same thing, pulling a content idea and actually creating new content idea and actually creating new content idea and actually creating new content drafts for us. And now we're

content drafts for us. And now we're content drafts for us. And now we're really starting to get leverage because really starting to get leverage because really starting to get leverage because we have some drafts. We have some we have some drafts. We have some

we have some drafts. We have some reviews coming in now as well. So we reviews coming in now as well. So we reviews coming in now as well. So we have, for example, this uh LinkedIn post have, for example, this uh LinkedIn post have, for example, this uh LinkedIn post about hiring somebody for traits instead

about hiring somebody for traits instead about hiring somebody for traits instead of a degree. We have one about of a degree. We have one about of a degree. We have one about Stanford's free AI courses and it's gone Stanford's free AI courses and it's gone

Stanford's free AI courses and it's gone out and done the research on those out and done the research on those out and done the research on those actual courses as well. Whilst we've actual courses as well. Whilst we've actual courses as well. Whilst we've also got a third terminal running on the

also got a third terminal running on the also got a third terminal running on the same task where it's pulled a topic from same task where it's pulled a topic from same task where it's pulled a topic from the air table and is scheduling our the air table and is scheduling our

the air table and is scheduling our weekly content. So this ran for 4 weekly content. So this ran for 4 weekly content. So this ran for 4 minutes, this is running for 5 minutes minutes, this is running for 5 minutes minutes, this is running for 5 minutes and the previous one ran for 5 minutes

and the previous one ran for 5 minutes and the previous one ran for 5 minutes as well. So we can condense our as well. So we can condense our as well. So we can condense our potential 15minute endto-end process potential 15minute endto-end process

potential 15minute endto-end process into 5 minutes and start reviewing those into 5 minutes and start reviewing those into 5 minutes and start reviewing those uh outputs as they come in rather than uh outputs as they come in rather than uh outputs as they come in rather than waiting 15 minutes for them all to

waiting 15 minutes for them all to waiting 15 minutes for them all to complete. we're able to run them in complete. we're able to run them in complete. we're able to run them in parallel like that. So, now that we've parallel like that. So, now that we've

parallel like that. So, now that we've got a team set up and we've got guard got a team set up and we've got guard got a team set up and we've got guard rails in place, why not just get it to rails in place, why not just get it to rails in place, why not just get it to run the whole show and we're going to

run the whole show and we're going to run the whole show and we're going to talk about level seven now, which is talk about level seven now, which is talk about level seven now, which is what people are doing with fully what people are doing with fully

what people are doing with fully autonomous pipelines. So, for our autonomous pipelines. So, for our autonomous pipelines. So, for our content creation system, this is where content creation system, this is where content creation system, this is where you set it up, you walk away, and you

you set it up, you walk away, and you you set it up, you walk away, and you come back to a week's worth of content come back to a week's worth of content come back to a week's worth of content already drafted, reviewed, and ready for already drafted, reviewed, and ready for

already drafted, reviewed, and ready for your approval. So, everything we've seen your approval. So, everything we've seen your approval. So, everything we've seen so far is implemented in what's called a so far is implemented in what's called a so far is implemented in what's called a Ralph loop, which is literally just

Ralph loop, which is literally just Ralph loop, which is literally just three files. It's a bash script that three files. It's a bash script that three files. It's a bash script that tells it do not stop working until tells it do not stop working until

tells it do not stop working until you've met this condition. And the you've met this condition. And the you've met this condition. And the condition can either be the max number condition can either be the max number condition can either be the max number of iterations to stop us spending too

of iterations to stop us spending too of iterations to stop us spending too many tokens or a done completion state. many tokens or a done completion state.

many tokens or a done completion state. So we tell it exactly what done means in So we tell it exactly what done means in So we tell it exactly what done means in our prd.json file, which is just our our prd.json file, which is just our our prd.json file, which is just our product requirements document file. And

product requirements document file. And product requirements document file. And it continues to push that context back it continues to push that context back it continues to push that context back into a fresh context window for Claude.

[36:41]

into a fresh context window for Claude. into a fresh context window for Claude. Every time it thinks it's done a task, Every time it thinks it's done a task, Every time it thinks it's done a task, it will say, have you completed or have it will say, have you completed or have

it will say, have you completed or have you met the conditions of completion? If you met the conditions of completion? If you met the conditions of completion? If not, go again. And to use it, we're not, go again. And to use it, we're not, go again. And to use it, we're literally going to install the plugin by

literally going to install the plugin by literally going to install the plugin by using the command /plugin install raw. using the command /plugin install raw.

using the command /plugin install raw. But the only thing that we need to But the only thing that we need to But the only thing that we need to create and make sure that we create here create and make sure that we create here create and make sure that we create here is a prd.json file. So for our weekly

is a prd.json file. So for our weekly is a prd.json file. So for our weekly content, this would literally look like content, this would literally look like content, this would literally look like user stories. So it's a description of user stories. So it's a description of

user stories. So it's a description of exactly the task that they need to do exactly the task that they need to do exactly the task that they need to do and tells the acceptance criteria for and tells the acceptance criteria for and tells the acceptance criteria for which it should assess against. So it

which it should assess against. So it which it should assess against. So it will create its own verification test will create its own verification test will create its own verification test when it runs the rail loop to say have I when it runs the rail loop to say have I

when it runs the rail loop to say have I met this acceptance criteria for this met this acceptance criteria for this met this acceptance criteria for this user story. If I have then update that user story. If I have then update that user story. If I have then update that to done or completed and then go through

to done or completed and then go through to done or completed and then go through feed it into a new context window to feed it into a new context window to feed it into a new context window to stop the context rock problem with the stop the context rock problem with the

stop the context rock problem with the second task that we're going to run and second task that we're going to run and second task that we're going to run and it will see that the status of the first it will see that the status of the first it will see that the status of the first one is now done. So, it's updating those

one is now done. So, it's updating those one is now done. So, it's updating those statuses, but feeding back in the statuses, but feeding back in the statuses, but feeding back in the original task, and it will move on to original task, and it will move on to

original task, and it will move on to post two, post three, post five, post two, post three, post five, post two, post three, post five, whatever, until it meets that acceptance whatever, until it meets that acceptance whatever, until it meets that acceptance criteria. So, we're just going to set up

criteria. So, we're just going to set up criteria. So, we're just going to set up a new file, PRD.json, and we're going to a new file, PRD.json, and we're going to a new file, PRD.json, and we're going to feed these content ideas into our PR feed these content ideas into our PR

feed these content ideas into our PR document. And this is a task that's well document. And this is a task that's well document. And this is a task that's well scoped, so it will find it hard to scoped, so it will find it hard to scoped, so it will find it hard to actually go off the rails and do

actually go off the rails and do actually go off the rails and do something different. And all we need to something different. And all we need to something different. And all we need to do to run this is actually just run the do to run this is actually just run the

do to run this is actually just run the Ralph loop command. So, we hit / Ralph Ralph loop command. So, we hit / Ralph Ralph loop command. So, we hit / Ralph loop. And I always recommend actually loop. And I always recommend actually loop. And I always recommend actually running this with max iterations because

running this with max iterations because running this with max iterations because if you don't, it could potentially run if you don't, it could potentially run if you don't, it could potentially run on larger projects indefinitely and cost on larger projects indefinitely and cost

on larger projects indefinitely and cost you a lot of money in spent tokens. So you a lot of money in spent tokens. So you a lot of money in spent tokens. So always try to run it with max iterations always try to run it with max iterations always try to run it with max iterations as well as a completion promise as a

as well as a completion promise as a as well as a completion promise as a safeguard, too. So Ralph is very much an safeguard, too. So Ralph is very much an safeguard, too. So Ralph is very much an executor. It works brilliantly when all executor. It works brilliantly when all

executor. It works brilliantly when all of your tasks are really well defined, of your tasks are really well defined, of your tasks are really well defined, clear description, a clear acceptance clear description, a clear acceptance clear description, a clear acceptance criteria, and a clear completion status.

criteria, and a clear completion status. criteria, and a clear completion status. And the content batching process that And the content batching process that And the content batching process that we've done is a perfect example of this.

we've done is a perfect example of this. we've done is a perfect example of this. Like write a LinkedIn post under 200 Like write a LinkedIn post under 200 Like write a LinkedIn post under 200 words with no band words in it and write words with no band words in it and write

words with no band words in it and write six of them and the these are the six of them and the these are the six of them and the these are the topics. So there's literally nothing it topics. So there's literally nothing it topics. So there's literally nothing it needs to figure out. It just needs to do

needs to figure out. It just needs to do needs to figure out. It just needs to do the work. So compared to Ralph GSD the work. So compared to Ralph GSD the work. So compared to Ralph GSD framework which we saw earlier is a framework which we saw earlier is a

[38:42]

framework which we saw earlier is a planner and an executor. So when you planner and an executor. So when you planner and an executor. So when you need a larger project to be broken down need a larger project to be broken down need a larger project to be broken down into a really comprehensive plan, we use

into a really comprehensive plan, we use into a really comprehensive plan, we use something like GSD because it helps us something like GSD because it helps us something like GSD because it helps us with the scoping it out. So it might be with the scoping it out. So it might be

with the scoping it out. So it might be for example, I need a content strategy for example, I need a content strategy for example, I need a content strategy for Q2 rather than write these specific for Q2 rather than write these specific for Q2 rather than write these specific posts because we need to do the planning

posts because we need to do the planning posts because we need to do the planning first. And if you know all of this, you first. And if you know all of this, you first. And if you know all of this, you can build out fully autonomous pipelines can build out fully autonomous pipelines

can build out fully autonomous pipelines for any business task that you want to for any business task that you want to for any business task that you want to do inside Claude Code and have it do inside Claude Code and have it do inside Claude Code and have it interact with any of your day-to-day

interact with any of your day-to-day interact with any of your day-to-day apps. So there you have it. These are apps. So there you have it. These are apps. So there you have it. These are the top ways to get the most leverage the top ways to get the most leverage

the top ways to get the most leverage from Claude Code. If you want to see a from Claude Code. If you want to see a from Claude Code. If you want to see a full project build using the GSD full project build using the GSD full project build using the GSD framework that I showed earlier that

framework that I showed earlier that framework that I showed earlier that uses all of the elements we've talked uses all of the elements we've talked uses all of the elements we've talked about today, then check out the next

