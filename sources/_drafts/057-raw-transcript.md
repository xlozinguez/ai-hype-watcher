# Raw Transcript: Securing AI Agents with Zero Trust

[0:00]

We've entered the age of agentic AI We've entered the age of agentic AI systems that don't just think, but they systems that don't just think, but they systems that don't just think, but they also act. Agents can talk to APIs. They also act. Agents can talk to APIs. They

also act. Agents can talk to APIs. They can call tools. They can buy things. can call tools. They can buy things. can call tools. They can buy things. They can move data. Even create sub They can move data. Even create sub They can move data. Even create sub agents. But every new capability adds a

agents. But every new capability adds a agents. But every new capability adds a new attack surface. Yet another way the new attack surface. Yet another way the new attack surface. Yet another way the bad guys can get into our systems. So bad guys can get into our systems. So

bad guys can get into our systems. So how do we protect this new ecosystem? We how do we protect this new ecosystem? We how do we protect this new ecosystem? We bring zero trust. Never trust. Always bring zero trust. Never trust. Always bring zero trust. Never trust. Always verify.

verify. verify. I know, I know you've heard about zero I know, I know you've heard about zero I know, I know you've heard about zero trust before. Isn't that just a trust before. Isn't that just a

trust before. Isn't that just a marketing slogan that all the vendors marketing slogan that all the vendors marketing slogan that all the vendors used and abused in order to get us to used and abused in order to get us to used and abused in order to get us to buy whatever they had on the truck?

buy whatever they had on the truck? buy whatever they had on the truck? Well, yes and no. Definitely the term Well, yes and no. Definitely the term Well, yes and no. Definitely the term got hijacked by overzealous sellers got hijacked by overzealous sellers

got hijacked by overzealous sellers trying to meet their quotas. But I'm a trying to meet their quotas. But I'm a trying to meet their quotas. But I'm a cyber security architect and I never got cyber security architect and I never got cyber security architect and I never got confused by all that noise because I

confused by all that noise because I confused by all that noise because I knew there were some solid, even knew there were some solid, even knew there were some solid, even game-changing security principles worth game-changing security principles worth

game-changing security principles worth holding on to. And now that we have AI holding on to. And now that we have AI holding on to. And now that we have AI agents popping up everywhere, the time agents popping up everywhere, the time agents popping up everywhere, the time is right to dust off the hype and

is right to dust off the hype and is right to dust off the hype and repurpose the good in zero trust in repurpose the good in zero trust in repurpose the good in zero trust in order to face the current security order to face the current security

order to face the current security challenge. Okay, let's take a quick challenge. Okay, let's take a quick challenge. Okay, let's take a quick review of what zero trust principles review of what zero trust principles review of what zero trust principles are. What distinguishes zero trust from

are. What distinguishes zero trust from are. What distinguishes zero trust from doing things in a nonzero trust way. doing things in a nonzero trust way.

doing things in a nonzero trust way. Well, one of the simple things that I Well, one of the simple things that I Well, one of the simple things that I mentioned previously is you verify and mentioned previously is you verify and mentioned previously is you verify and then you trust. So you only trust

then you trust. So you only trust then you trust. So you only trust something that has in fact been verified something that has in fact been verified something that has in fact been verified or trust follows verification is another or trust follows verification is another

or trust follows verification is another way to think of it. Another thing is we way to think of it. Another thing is we way to think of it. Another thing is we get rid of the just in case principle get rid of the just in case principle get rid of the just in case principle where we put things out in case we need

where we put things out in case we need where we put things out in case we need them and replace it with just in time. them and replace it with just in time.

them and replace it with just in time. So we give the access rights that are So we give the access rights that are So we give the access rights that are needed only when they're needed and not needed only when they're needed and not needed only when they're needed and not for longer than they're needed. That's a

for longer than they're needed. That's a for longer than they're needed. That's a preserving of the principle of lease preserving of the principle of lease preserving of the principle of lease privilege which says you have only the privilege which says you have only the

privilege which says you have only the access rights that you need for only as access rights that you need for only as access rights that you need for only as long as you need them and not longer.

long as you need them and not longer. long as you need them and not longer. Another thing is we move from Another thing is we move from Another thing is we move from perimeterbased controls where we're perimeterbased controls where we're

perimeterbased controls where we're trying to basically put the hard crunchy trying to basically put the hard crunchy trying to basically put the hard crunchy outside and leave the soft chewy center.

[2:01]

outside and leave the soft chewy center. outside and leave the soft chewy center. That's not very good. In fact, what we That's not very good. In fact, what we That's not very good. In fact, what we want to move to is a more pervasive set want to move to is a more pervasive set

want to move to is a more pervasive set of security controls. So the security of security controls. So the security of security controls. So the security controls are throughout the system not controls are throughout the system not controls are throughout the system not just around the outside. And then what I

just around the outside. And then what I just around the outside. And then what I think is the most important aspect and think is the most important aspect and think is the most important aspect and it often gets overlooked in zero trust it often gets overlooked in zero trust

it often gets overlooked in zero trust discussions is the idea of the discussions is the idea of the discussions is the idea of the assumption of breach. You assume the bad assumption of breach. You assume the bad assumption of breach. You assume the bad guy is already in your system already in

guy is already in your system already in guy is already in your system already in your network already in your database in your network already in your database in your network already in your database in your application already has elevated your application already has elevated

your application already has elevated privileges from stolen credentials. privileges from stolen credentials. privileges from stolen credentials. That's what we're going to operate from.

That's what we're going to operate from. That's what we're going to operate from. Now design your security. So it's Now design your security. So it's Now design your security. So it's assuming that you've been breached assuming that you've been breached

assuming that you've been breached already and it's a very different model, already and it's a very different model, already and it's a very different model, a very different paradigm and way of a very different paradigm and way of a very different paradigm and way of thinking about security. So let's take a

thinking about security. So let's take a thinking about security. So let's take a look and see what zero trust principles look and see what zero trust principles look and see what zero trust principles would look like if they were applied to would look like if they were applied to

would look like if they were applied to an agentic environment. First of all, an agentic environment. First of all, an agentic environment. First of all, let's look at a traditional environment.

let's look at a traditional environment. let's look at a traditional environment. How do we apply zero trust in this case? How do we apply zero trust in this case?

How do we apply zero trust in this case? Well, we've got users that have to be Well, we've got users that have to be Well, we've got users that have to be secured. They're part of the security secured. They're part of the security secured. They're part of the security equation. So I need to do identity and

equation. So I need to do identity and equation. So I need to do identity and access management. I need to make sure access management. I need to make sure access management. I need to make sure that the user has an account, that that the user has an account, that

that the user has an account, that they're logged in, that the person they're logged in, that the person they're logged in, that the person logged in is in fact the user they claim logged in is in fact the user they claim logged in is in fact the user they claim to be. So that's strong authentication,

to be. So that's strong authentication, to be. So that's strong authentication, access controls, so that they can only access controls, so that they can only access controls, so that they can only access the things that they're permitted access the things that they're permitted

access the things that they're permitted to see. The device that the user is to see. The device that the user is to see. The device that the user is using matters as well. It could be using matters as well. It could be using matters as well. It could be compromised. I need to make sure that it

compromised. I need to make sure that it compromised. I need to make sure that it is in fact pure, that it hasn't been is in fact pure, that it hasn't been is in fact pure, that it hasn't been jailbroken, that an attacker hasn't jailbroken, that an attacker hasn't

jailbroken, that an attacker hasn't taken control of the system because then taken control of the system because then taken control of the system because then it won't matter if I have the authentic it won't matter if I have the authentic it won't matter if I have the authentic user trying to do the right thing if the

user trying to do the right thing if the user trying to do the right thing if the device has already been compromised. I device has already been compromised. I device has already been compromised. I need to look at the data layer of all of need to look at the data layer of all of

need to look at the data layer of all of this. So, I need to make sure that the this. So, I need to make sure that the this. So, I need to make sure that the data that's sensitive has been encrypted data that's sensitive has been encrypted data that's sensitive has been encrypted so it can't be easily seen. I need to

so it can't be easily seen. I need to so it can't be easily seen. I need to make sure that it's not leaving my make sure that it's not leaving my make sure that it's not leaving my network if it's not supposed to. Things network if it's not supposed to. Things

network if it's not supposed to. Things like that. And then another big part and like that. And then another big part and like that. And then another big part and a lot of people start their zerorust a lot of people start their zerorust a lot of people start their zerorust discussions in this particular area and

discussions in this particular area and discussions in this particular area and it's the area of the network. So I'm it's the area of the network. So I'm it's the area of the network. So I'm going to make sure that my network is going to make sure that my network is

[4:03]

going to make sure that my network is well secured that if information is well secured that if information is well secured that if information is traversing a part and that information traversing a part and that information traversing a part and that information is sensitive then I want to have it

is sensitive then I want to have it is sensitive then I want to have it encrypted. I want to make sure that I do encrypted. I want to make sure that I do encrypted. I want to make sure that I do things like micro segmentation where I things like micro segmentation where I

things like micro segmentation where I group individual parts of the network group individual parts of the network group individual parts of the network together and give some level of together and give some level of together and give some level of isolation so that if this guy gets

isolation so that if this guy gets isolation so that if this guy gets infected, his infection doesn't easily infected, his infection doesn't easily infected, his infection doesn't easily spread to others. So those are some of spread to others. So those are some of

spread to others. So those are some of the things that we've done traditionally the things that we've done traditionally the things that we've done traditionally in zero trust and spreading this in zero trust and spreading this in zero trust and spreading this pervasively throughout the system. I've

pervasively throughout the system. I've pervasively throughout the system. I've got to do all of that as I move into the got to do all of that as I move into the got to do all of that as I move into the agentic world plus I have to do some agentic world plus I have to do some

agentic world plus I have to do some more. So as we start looking at agents, more. So as we start looking at agents, more. So as we start looking at agents, who are the actors? The actors are in who are the actors? The actors are in who are the actors? The actors are in fact software. So we've got an AI agent

fact software. So we've got an AI agent fact software. So we've got an AI agent here that is here that is here that is using a nonhuman identity. So here we using a nonhuman identity. So here we

using a nonhuman identity. So here we had users and we could associate them had users and we could associate them had users and we could associate them with the identity they were using. But with the identity they were using. But with the identity they were using. But an agent may in fact use lots of these

an agent may in fact use lots of these an agent may in fact use lots of these different NHIS, lots of different different NHIS, lots of different different NHIS, lots of different non-human identities. So here we have a non-human identities. So here we have a

non-human identities. So here we have a proliferation of these things growing. I proliferation of these things growing. I proliferation of these things growing. I need to make sure all of them have the need to make sure all of them have the need to make sure all of them have the same level of control and visibility

same level of control and visibility same level of control and visibility that we had for the human users. In that we had for the human users. In that we had for the human users. In fact, maybe even more because they're fact, maybe even more because they're

fact, maybe even more because they're operating autonomously and we need operating autonomously and we need operating autonomously and we need supervision of that. We need tools that supervision of that. We need tools that supervision of that. We need tools that we're going to be using to also be

we're going to be using to also be we're going to be using to also be secure. We need to make sure that the secure. We need to make sure that the secure. We need to make sure that the tools that we're leveraging are tools we tools that we're leveraging are tools we

tools that we're leveraging are tools we can trust. Again, we have data. In this can trust. Again, we have data. In this can trust. Again, we have data. In this case, data may be the thing that was the case, data may be the thing that was the case, data may be the thing that was the basis for the AI agent. We use data to

basis for the AI agent. We use data to basis for the AI agent. We use data to train the model. We need to also augment train the model. We need to also augment train the model. We need to also augment the model. We may use preference the model. We may use preference

the model. We may use preference information and other context information and other context information and other context information that we put into the model.

information that we put into the model. information that we put into the model. I need to make sure all of that stuff I need to make sure all of that stuff I need to make sure all of that stuff has been secured, that it hasn't been has been secured, that it hasn't been

has been secured, that it hasn't been tampered with. And then ultimately, I tampered with. And then ultimately, I tampered with. And then ultimately, I need to be able to look at the need to be able to look at the need to be able to look at the intentions of the agent and make sure

intentions of the agent and make sure intentions of the agent and make sure those intentions match what the original those intentions match what the original those intentions match what the original user's intentions were for this user's intentions were for this

user's intentions were for this particular system. Let's take a look at particular system. Let's take a look at particular system. Let's take a look at an agentic system and see where the an agentic system and see where the an agentic system and see where the threats might be. So here is how the

[6:07]

threats might be. So here is how the threats might be. So here is how the thing basically works. We have a sensing thing basically works. We have a sensing thing basically works. We have a sensing portion that is the thing that takes the portion that is the thing that takes the

portion that is the thing that takes the input. It might be visual, it might be input. It might be visual, it might be input. It might be visual, it might be textual, it could be a lot of different textual, it could be a lot of different textual, it could be a lot of different things but that feeds into the AI which

things but that feeds into the AI which things but that feeds into the AI which does the thinking and then in that does the thinking and then in that does the thinking and then in that thinking we will augment that with thinking we will augment that with

thinking we will augment that with policies, preferences and other things policies, preferences and other things policies, preferences and other things like that. So we'll have that like that. So we'll have that like that. So we'll have that information affecting the thought

information affecting the thought information affecting the thought process, the reasoning process that's process, the reasoning process that's process, the reasoning process that's happening and then ultimately it takes happening and then ultimately it takes

happening and then ultimately it takes those actions. So it could do an API those actions. So it could do an API those actions. So it could do an API call, it might uh write some data, move call, it might uh write some data, move call, it might uh write some data, move some data around, it might use a tool,

some data around, it might use a tool, some data around, it might use a tool, it might spawn other agents. And then it might spawn other agents. And then it might spawn other agents. And then all of this is going to be driven by all of this is going to be driven by

all of this is going to be driven by credentials. So we have individual credentials. So we have individual credentials. So we have individual capabilities that each one of these capabilities that each one of these capabilities that each one of these things ought to be able to have. So, if

things ought to be able to have. So, if things ought to be able to have. So, if I'm an attacker, I look at this thing I'm an attacker, I look at this thing I'm an attacker, I look at this thing and start to figure how might I break and start to figure how might I break

and start to figure how might I break this thing? Well, one thing I could do this thing? Well, one thing I could do this thing? Well, one thing I could do right here is a direct prompt injection.

right here is a direct prompt injection. right here is a direct prompt injection. I might send a prompt in that is going I might send a prompt in that is going I might send a prompt in that is going to break the context of this system and to break the context of this system and

to break the context of this system and have it start doing things that it's not have it start doing things that it's not have it start doing things that it's not supposed to do. So, that's one of the supposed to do. So, that's one of the supposed to do. So, that's one of the things I could think about. Another is I

things I could think about. Another is I things I could think about. Another is I could attack right here and I could do could attack right here and I could do could attack right here and I could do something to manipulate to to mess up something to manipulate to to mess up

something to manipulate to to mess up the policy the preference information to the policy the preference information to the policy the preference information to poison that information or even poison poison that information or even poison poison that information or even poison the model that was used to train this

the model that was used to train this the model that was used to train this thing. So that's another one to look at. thing. So that's another one to look at.

thing. So that's another one to look at. Another thing here is looking at all of Another thing here is looking at all of Another thing here is looking at all of these interfaces. What if I insert these interfaces. What if I insert these interfaces. What if I insert myself at any one of these? that would

myself at any one of these? that would myself at any one of these? that would be uh a place where I could do some be uh a place where I could do some be uh a place where I could do some damage if on this and this might be say damage if on this and this might be say

damage if on this and this might be say an MCP call something along those lines. an MCP call something along those lines. an MCP call something along those lines. Um and I would be able to insert and Um and I would be able to insert and Um and I would be able to insert and take control of that. I might also

take control of that. I might also take control of that. I might also attack individuals of these services, attack individuals of these services, attack individuals of these services, these APIs, the data source, the tools, these APIs, the data source, the tools,

these APIs, the data source, the tools, uh the agents. So all of those are an uh the agents. So all of those are an uh the agents. So all of those are an extension of the attack surface. And extension of the attack surface. And extension of the attack surface. And then right here they're credentials.

then right here they're credentials. then right here they're credentials. Maybe I want to go in and attack those. Maybe I want to go in and attack those.

Maybe I want to go in and attack those. Maybe I can copy those credentials. Maybe I can copy those credentials. Maybe I can copy those credentials. Maybe I can log into a system and create Maybe I can log into a system and create Maybe I can log into a system and create new accounts or increase my level of

[8:09]

new accounts or increase my level of new accounts or increase my level of privilege. So there's a lot of different privilege. So there's a lot of different privilege. So there's a lot of different moving parts in this system. An attacker moving parts in this system. An attacker

moving parts in this system. An attacker has a wealth of different places that has a wealth of different places that has a wealth of different places that they could in fact dive into and do a they could in fact dive into and do a they could in fact dive into and do a lot of damage. So now let's apply those

lot of damage. So now let's apply those lot of damage. So now let's apply those zero trust principles to this AI agentic zero trust principles to this AI agentic zero trust principles to this AI agentic environment and we'll see what we can do environment and we'll see what we can do

environment and we'll see what we can do to eliminate some or all of these to eliminate some or all of these to eliminate some or all of these threats. So first of all, we're going to threats. So first of all, we're going to threats. So first of all, we're going to start here with the credentials. And I

start here with the credentials. And I start here with the credentials. And I mentioned this before, we want unique mentioned this before, we want unique mentioned this before, we want unique credentials for every agent, for every credentials for every agent, for every

credentials for every agent, for every user, and every agent that those agents user, and every agent that those agents user, and every agent that those agents create as well. So, we need a place to create as well. So, we need a place to create as well. So, we need a place to store all of these nonhuman identities

store all of these nonhuman identities store all of these nonhuman identities and keep all of them access controlled. and keep all of them access controlled.

and keep all of them access controlled. Keep them so that they don't have more Keep them so that they don't have more Keep them so that they don't have more privilege than they're supposed to have.

privilege than they're supposed to have. privilege than they're supposed to have. We want it to be just in time, not just We want it to be just in time, not just We want it to be just in time, not just in case. In other words, we give the in case. In other words, we give the

in case. In other words, we give the privilege just when it's needed and then privilege just when it's needed and then privilege just when it's needed and then we take it away. We don't give it in we take it away. We don't give it in we take it away. We don't give it in advance and say, "Well, just in case you

advance and say, "Well, just in case you advance and say, "Well, just in case you might need this later." So, we're going might need this later." So, we're going might need this later." So, we're going to do that. We're going to make sure to do that. We're going to make sure

to do that. We're going to make sure that these systems also never include that these systems also never include that these systems also never include credentials buried into the system credentials buried into the system credentials buried into the system itself. And that's been a temptation of

itself. And that's been a temptation of itself. And that's been a temptation of programmers. They put a a password, they programmers. They put a a password, they programmers. They put a a password, they put an API key, and they bet it direct put an API key, and they bet it direct

put an API key, and they bet it direct embed it directly into their code. That embed it directly into their code. That embed it directly into their code. That is an absolute no no. What we want is an absolute no no. What we want is an absolute no no. What we want instead is to store all of these in a

instead is to store all of these in a instead is to store all of these in a vault where we have a dynamic system vault where we have a dynamic system vault where we have a dynamic system where I can go check credentials in and where I can go check credentials in and

where I can go check credentials in and out. I can get new credentials created out. I can get new credentials created out. I can get new credentials created over time. I can enforce just in time. I over time. I can enforce just in time. I over time. I can enforce just in time. I can enforce RO based access control. I

can enforce RO based access control. I can enforce RO based access control. I can do strong authentication. I can do can do strong authentication. I can do can do strong authentication. I can do all of those kinds of things that I'm all of those kinds of things that I'm

all of those kinds of things that I'm needing to do in these cases. So, we're needing to do in these cases. So, we're needing to do in these cases. So, we're going to uh cover all of those bases. No going to uh cover all of those bases. No going to uh cover all of those bases. No static credentials. everything is

static credentials. everything is static credentials. everything is dynamic instead. And then we're going to dynamic instead. And then we're going to dynamic instead. And then we're going to move over to the tools themselves. So I move over to the tools themselves. So I

move over to the tools themselves. So I need to make sure that these things have need to make sure that these things have need to make sure that these things have registered versions. So I'm going to registered versions. So I'm going to registered versions. So I'm going to have a tool registry where I have

have a tool registry where I have have a tool registry where I have verified these are secure APIs that we verified these are secure APIs that we verified these are secure APIs that we can afford to use. The others have not can afford to use. The others have not

[10:10]

can afford to use. The others have not been vetted. These are a set of secure been vetted. These are a set of secure been vetted. These are a set of secure databases and data sources that we can databases and data sources that we can databases and data sources that we can use. These are a set of tools that we

use. These are a set of tools that we use. These are a set of tools that we have vetted and we can trust. And all of have vetted and we can trust. And all of have vetted and we can trust. And all of these kinds of things, if we're going to these kinds of things, if we're going to

these kinds of things, if we're going to be using those, it's basically, think be using those, it's basically, think be using those, it's basically, think about if you're making a cake or a soup, about if you're making a cake or a soup, about if you're making a cake or a soup, you want to make sure that the

you want to make sure that the you want to make sure that the ingredients that go into it are pure. ingredients that go into it are pure.

ingredients that go into it are pure. So, we want to make sure that we're So, we want to make sure that we're So, we want to make sure that we're using the pure stuff to begin with.

using the pure stuff to begin with. using the pure stuff to begin with. Then, I need something that's going to Then, I need something that's going to Then, I need something that's going to give me some sort of inspection over the give me some sort of inspection over the

give me some sort of inspection over the whole thing. So something that's going whole thing. So something that's going whole thing. So something that's going to be able to look over it all, look to be able to look over it all, look to be able to look over it all, look here and see if there are improper

here and see if there are improper here and see if there are improper inputs going into any of these tools inputs going into any of these tools inputs going into any of these tools that are coming out of the agent. Also that are coming out of the agent. Also

that are coming out of the agent. Also be able to look and check for these be able to look and check for these be able to look and check for these prompt injections that may be coming prompt injections that may be coming prompt injections that may be coming into the system. We could use an AI

into the system. We could use an AI into the system. We could use an AI firewall or an AI gateway, whichever firewall or an AI gateway, whichever firewall or an AI gateway, whichever term you prefer, to do those sort of term you prefer, to do those sort of

term you prefer, to do those sort of checks and block. So it will look and checks and block. So it will look and checks and block. So it will look and see, is that something that should be see, is that something that should be see, is that something that should be allowed to go in? Do we have information

allowed to go in? Do we have information allowed to go in? Do we have information leaking out of systems that shouldn't leaking out of systems that shouldn't leaking out of systems that shouldn't be? Are we making improper calls? This be? Are we making improper calls? This

be? Are we making improper calls? This sort of thing. So, it's an enforcement sort of thing. So, it's an enforcement sort of thing. So, it's an enforcement layer here as well. And then ultimately, layer here as well. And then ultimately, layer here as well. And then ultimately, I need to be able to have traceability

I need to be able to have traceability I need to be able to have traceability of all of this. So, I need a system of all of this. So, I need a system of all of this. So, I need a system where I'm logging immutable logs. That where I'm logging immutable logs. That

where I'm logging immutable logs. That means that they can't be changed. I means that they can't be changed. I means that they can't be changed. I don't want a bad guy to come in here and don't want a bad guy to come in here and don't want a bad guy to come in here and change the information that's in my log.

change the information that's in my log. change the information that's in my log. I want to be able to prevent that. So, I want to be able to prevent that. So, I want to be able to prevent that. So, when actions are occurring in the when actions are occurring in the

when actions are occurring in the system, it needs to be able to be system, it needs to be able to be system, it needs to be able to be traceable. so we can go back later and traceable. so we can go back later and traceable. so we can go back later and understand why it did what it did. I

understand why it did what it did. I understand why it did what it did. I also want to scan the entire also want to scan the entire also want to scan the entire environment, be able to look across all environment, be able to look across all

environment, be able to look across all of these different things. And we've got of these different things. And we've got of these different things. And we've got different tools for different types of different tools for different types of different tools for different types of scanning. We've got network scanning

scanning. We've got network scanning scanning. We've got network scanning tools. We've got endpoint scanning tools. We've got endpoint scanning tools. We've got endpoint scanning tools. We've got tools now that can scan tools. We've got tools now that can scan

tools. We've got tools now that can scan AI models and look for vulnerabilities AI models and look for vulnerabilities AI models and look for vulnerabilities that may be latent and hiding inside of that may be latent and hiding inside of that may be latent and hiding inside of those. Ultimately, at the end of all

those. Ultimately, at the end of all those. Ultimately, at the end of all this, we need still a human in the loop. this, we need still a human in the loop.

this, we need still a human in the loop. We need an ability to be able to have a We need an ability to be able to have a We need an ability to be able to have a kill switch. If someone sees this thing kill switch. If someone sees this thing kill switch. If someone sees this thing is running out of control, what it's

[12:12]

is running out of control, what it's is running out of control, what it's doing is not right and we can go see doing is not right and we can go see doing is not right and we can go see what it's been doing, we want to put what it's been doing, we want to put

what it's been doing, we want to put throttles in place in some cases so that throttles in place in some cases so that throttles in place in some cases so that if maybe it's a buying application, it if maybe it's a buying application, it if maybe it's a buying application, it doesn't just suddenly decide, hey, I

doesn't just suddenly decide, hey, I doesn't just suddenly decide, hey, I like this. I'm going to buy a thousand like this. I'm going to buy a thousand like this. I'm going to buy a thousand of these in a minute. Maybe we don't of these in a minute. Maybe we don't

of these in a minute. Maybe we don't want it to do that. So, we throttle back want it to do that. So, we throttle back want it to do that. So, we throttle back its activity. We have canary deployments its activity. We have canary deployments its activity. We have canary deployments where we sort of drop the canary in the

where we sort of drop the canary in the where we sort of drop the canary in the coal mine to see what happens. So we're coal mine to see what happens. So we're coal mine to see what happens. So we're going to see if this system dropped into going to see if this system dropped into

going to see if this system dropped into an environment is going to operate an environment is going to operate an environment is going to operate properly or not. A lot of different properly or not. A lot of different properly or not. A lot of different things you can see here. The agent

things you can see here. The agent things you can see here. The agent systems are complex. The number of systems are complex. The number of systems are complex. The number of threats that we face are complex and threats that we face are complex and

threats that we face are complex and numerous. So our security defenses have numerous. So our security defenses have numerous. So our security defenses have to be up to the challenge. Agentic AI to be up to the challenge. Agentic AI to be up to the challenge. Agentic AI multiplies power

multiplies power multiplies power and risk. Zero trust gives us the and risk. Zero trust gives us the and risk. Zero trust gives us the framework to keep that power contained.

framework to keep that power contained. framework to keep that power contained. Every agent must prove who it is, Every agent must prove who it is, Every agent must prove who it is, justify what it wants, and earn trust justify what it wants, and earn trust

justify what it wants, and earn trust continuously. As we move forward with continuously. As we move forward with continuously. As we move forward with autonomous systems, zero trust autonomous systems, zero trust autonomous systems, zero trust principles deployed correctly serve as

principles deployed correctly serve as principles deployed correctly serve as guard rails that keep innovation in guard rails that keep innovation in guard rails that keep innovation in alignment with our intent instead of the alignment with our intent instead of the

alignment with our intent instead of the bad guys.

