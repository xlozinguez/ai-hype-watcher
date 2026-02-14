# Raw Transcript: The Cursor Situation

- **URL**: https://www.youtube.com/watch?v=yzqNWVvd2BM
- **Duration**: 18:46
- **Captured**: 2026-02-13
- **Method**: yt-dlp VTT extraction

---

[00:27]

So last month, Curser released a blog post that has been a bit controversial. They did an experiment where they used their agents and applied them to build complex tasks but by just prompting it once. So they tried stuff like building a full spreadsheet software from scratch and a full browser from scratch. You know that a web browser is one of the most complex pieces of software we have, right? A web browser needs to have a bunch of stuff. It needs to have like a

[00:54]

JavaScript engine, needs to be able to render HTML. needs to have like a network stack, a security stack. There's a whole lot of stuff there. So when cursor comes and says, well, we were able to deploy a bunch of agents and without any prompting or human involvement, the agents were able to build a full browser from scratch. Well, I was curious, so I checked it out. And what I found is that this is a perfect example of the kind of nonsensical BS

[01:21]

hype that happens in the industry today. So did cursor actually build a browser from scratch? Let let me show you what they've done. So the blog post is titled scaling longunning autonomous coding. We've been experimenting with running coding agents autonomously for weeks. Our goal is to understand how far we can push the frontier of agentic coding for projects that typically take human teams months to complete. I want to add something here which as a context for

[01:49]

this, right? Why why is cursor doing this? Cursor is an IDE after all, right? Why are they looking at agents where you don't have to use an ID? Seems like a conflict of interest, right? So, what I've noticed is that cursor has been steadily pushing agents. Okay, you might have noticed this. If you look at a recent installation of cursor, you install cursor from like from the scratch. You open it up, the first thing you see is that agentic panel. They

[02:16]

don't even show the file browser bar. Okay, you don't even see like why do you want to see files? See our agents. So, it starts out with agents and there's been this constant push to focus more on agents. And I think this is in line with that. So, it's not really them saying don't use cursor, use agents instead. It's basically saying you want to use agents, cursor is the right tool for that. I think that's the pitch. Okay, so keep that in mind. Now they talk about a

[02:43]

bunch of stuff about how they did the architecture and we'll come to that in a bit. But basically here is the key to test the system. We pointed it at an ambitious goal building a web browser from the scratch. The agent ran for close to a week writing over 1 million lines of code across 1,000 files. You can explore the source code on GitHub. Yes, we're going to explore it. But wait a minute, they've given this uploaded this uh what is this? A video? A gif?

[03:11]

It's loading some page. Okay, it's loading a medium page uh on medium.com. And this is an Apple developer page. So they have something here. It says while it might seem like a simple screenshot, building a browser from scratch is extremely difficult. Okay, so they've built a browser and they have done this with hundreds of workers running concurrently and pushing to the same branch with minimal conflicts. Seems impressive, right? Seems amazing if they

[03:38]

could do this. They have a bunch of other uh experiments as well. So they've done this solid to React migration in the cursor codebase. So they were using the solid framework, they switched to React framework. If you're not sure, basically there are two UI frameworks, right? They move from one UI framework to another. This one's actually a little more promising and I'll come to that in a bit. But we they have a few more. Okay, they've done Java LSP, right?

[04:05]

Language server protocols language server for IDE. They've done Windows 7 emulator and Excel. So they've created all these things from the scratch, which seems amazing. It's like can agents really do all this? Okay, so the blog post says they ran about 2,000 agents concurrently at its peak and they made thousands of commits per hour and they used trillions of tokens. That's their word. Trillions plural. So big claims, lots of numbers and the repo is public

[04:32]

which means that anyone can go and verify. So people went and checked and guess what? The damn thing doesn't compile. What did you expect? Really, what did you expect? Okay, let's take a look at this. So, this is the repo. I'm going to show show you the repo that they have. This one's called uh fast render. Okay, this is the repo created by entirely by AI. A browser rendering engine in Rust. It parses HTML, CSS, computes, all that

[05:00]

stuff. Wait a minute, where is AI? Oh, here it is. Developed as a part of research into collaborative parallel AI coding agents. This is the repo. You can check it out. It has nice AI generated documentation with like charts and all that stuff. Amazing, right? Except that it just doesn't compile. Apart from that one tiny bit of detail, everything else in this repo is awesome. If you go to the releases tab, well, there are no releases, I guess.

[05:27]

Yeah, there are no releases. There are a bunch of issues. If you go to the issues, a bunch of people are not able to compile the thing. Full of complaints about that. And that's excluding the closed issues about not being able to compile. And there's nothing that you can actually download and run as a uh as a packaged thing, right? It's just there as an experiment, as a proof of concept. So the CI/CD pipeline, the automated checks that run after every time a code

[05:54]

is merged, right? So there was this guy Jason Gorman from codemanship who analyzed the CI/CD for this project and he found an 88% failure rate. 88% failure rate. That means that out of every 10 times the automated build ran it failed almost nine times right and the agents are still merging code while CI was failing. And basically the check is saying hey this is broken but code gets merged anyway. This was the issue that was created I think about a day

[06:22]

after they made this announcement. Someone went ahead and tried to compile it and they said, "Well, the build is actually failing with 32 errors. There are no releases, no tags, no stable branch. What do we do with this thing?" Right? And um let me zoom this up. And there are a bunch of people who asked, well, is there a CI run that actually worked? It doesn't seem to be. Someone else also tried to do a run for it. They were not able to. Large parts of the

[06:49]

codebase has code that is completely out of place. bunch of stuff that's being linked to under one title but actually links to something completely different. CICD seems to not have been successful once yet PRs are merged. The blog post mentions something like it might look like just a screenshot but blah blah blah is the screenshot the thing we're supposed to be impressed by because for all intents and matters this project does not contain a functioning web

[07:16]

browser by any measurements and I'm not sure how anyone could have successfully ran this at least with the code as is right now. There was one other issue that someone had opened saying that they manually managed to get that to work and they tried to use it as a browser and the search box didn't work. The browser didn't respond to clicks and then the page just hangs. It says page unresponsive. So basically basic interaction doesn't work even when you

[07:44]

put in the effort and clear the build. Okay. So this browser that they announced as built from scratch in a week, maybe it's likely that a fully clean build never existed. Not that it's buggy, it's never fully compiled as a whole. Now let's take a look at the other claim which is built from scratch. Okay, it's not working at its current state. But can it just you know just maybe a little nudge and then it starts working? Well, okay, for that let's look

[08:11]

at the other part. What will we have if we do fix the builds, right? Is it a browser built from the scratch? So it turns out the project uses HTML 5 and CSS parser. So these are two libraries from Mosilla's servo engine and they're used for HTML parsing and CSS parsing. Okay. So basically what the agent has done is it's taken a library from another open-source browser just plugged it in. These are not utility libraries, right? HTML parsing is a fundamental

[08:38]

feature of a browser. So if you're saying you're building it from the scratch, you can't go about using a library. You got to build a new library. CSS parsing is a fundamental feature of of a browser. layouts, graphics, text rendering. This is basically what a browser is. So if you're outsourcing that what do you have in your browser and what these guys have done is the agents really it's basically taken existing mature open source projects and

[09:05]

it's got that in right so there's this guy called Gregory Terzian who maintains I hope I'm pronouncing the name right he maintains the sero browser engine right he's been working on server since 2016 okay he looked at this code and he basically said uh the actual code is worse I can only describe it as a tangle of spaghetti, a uniquely bad design that could never support anything resembling a realworld web engine. Right? This is a guy who does the work professionally,

[09:33]

saying that the code is structurally broken. It's not just incomplete, it is broken. The libraries that I talked about, right? Servo and Ladybird, they are open source and they each are about a million lines of code, right? They have been built for over years. I think some of them are for even decades. Fast render has three million lines of code and it actually does less. Okay, three times the code and a fraction of the capability. In software, there's a term

[10:00]

for it. When you have more code but it's less functional, you know what they call it? They call it bloat is what it is. So Wilson, who's the cursor engineer who created this project, kind of pushed back on social media, right? He responded on hacker news and he said, "Well, yeah, the JSVM, uh, the DOM, the like the pain systems, they're all being part of the project. They're not being wired from dependency." He was honest about what's not there yet. He was

[10:27]

basically saying, well, it is like a research project, but the discrepancy is in what they're saying here versus what the tweet claimed. I'm going to show you the tweet here. So this is the CEO saying we built a browser and it ran for a week and it's kind of works has issues but then we were astonished is what he says right and all I can think of is this comment here investors can't read code and don't even know what GitHub is the computer programmed itself so line

[10:55]

go up so basically the point is that this is we are not the target audience this is meant for someone else and the blog post has done its job in generating the hype which is a very fair assessment. And now finally if you think all this is surprising I'm going to give you the biggest shocker of all which is about the cost. The blog post says that they deployed trillions of tokens okay trillions of tokens. If you look at the calculation all right GPT 5.2 into

[11:22]

Cordex, which is the model that they claimed they used. It costs $14 per million output tokens. Okay, this is a standard OpenAI price. Maybe they might get a discount, but let's keep it at $14 per million output tokens. Okay, so if you do a calculation, 1 trillion tokens divided by 1 million gives you 1 million batches, right? So 1 million * 14, you get $14 million. That's the simple version. It's I'd say it's the conservative version because basically

[11:49]

what you're saying is if the agents just generated 1 trillion tokens as output without anything else without iterating or without like going the wrong place correcting and all that generates 1 trillion tokens you basically spend $14 million. But if you look at reality not all tokens are output right? If you look at agentic systems they use a lot of input tokens as well. They basically load the context. They read the codebase. They do some planning. And

[12:17]

input tokens are a little bit cheaper, but they're not free. Usually, if you realistically, if you look at a 7030 input output split, you say trillions, what are we looking at? Two trillion. And if you look at the calculation, you're basically getting to around with 7030, you're basically looking at around $10.8 million total. If they used 3 trillions, you're basically getting closer to around $16 million. So the realistic range is somewhere between 8

[12:44]

million to 16 million. Okay, that's about $2 million a day for a week for code that does not compile. Someone on social media commented, "Maybe next time just donate the money to a browser team." Hard to argue with that. So all of the stuff, the compile errors, the from scratch claim being bad and then even the cost has been covered well in social media. A lot of people have been talking about it, but I think there is a detail in this blog post which matters a

[13:11]

little more than the headline stuff. And that is something that I think people haven't been picking up on. The blog actually describes how their agent architecture evolved. Early on, they had this integrator role, the agent whose job is to do quality control. It reviewed code from worker agents and checked for consistency, made sure things fit together. Basically, what like a senior engineer or a staff engineer does in a coding review.

[13:38]

Basically what they said was, okay, we have an integrator agent whose job is to do quality control, but it was actually slowing down. This this is literally what the blog says. They say that removing the integrator simplified the system and eliminated bottlenecks. Workers just handled the conflicts on their own. Think about that for a minute. The quality control agent was slowing things down. And yes, quality control does slow things down. That's

[14:06]

the point. That's what it does. You check for quality before they ship. And if the quality is bad, it does slow down. It does take time. And instead of figuring out how to do quality checks at speed, they just stop doing them. So no wonder you have this result, right? And then they pointed the throughput numbers and said, see, look at how much we can produce. You can always produce more. Okay? If you stop checking whether what you're producing is correct or not,

[14:33]

whether it works or not, sure, you can produce more. And that's basically what happened here. It's the same pattern that you see in human software teams by the way, right? When a team starts optimizing for velocity, you basically have managers counting lines of code per sprint. How many commits do you have per day? How many story points did you get done? You can always hit bigger numbers by cutting out the quality, right? Cut out the code reviews. Just do rubber

[15:00]

stamped code reviews, skip the tests, ship faster, you have metrics which now look amazing, and the software gets worse. So this literally what's happened over here, right? They have 30,000 commits, 3 million lines of code, and 88% of those fail CI metrics are amazing. The software doesn't compile. Now, here's the thing that bothers me. Like I use cursor and clot code. It does certain things well if you use it right. Right. not just give an agent a vague

[15:28]

prompt and say go ahead and do it. But if you have the agency and you're basically controlling it, right? You're kind of treating it as a buddy paired programmer and then working on it actually does a really good job. The fact that hundreds of agents can actually work on shared codebase at all is fascinating. Cursor's own blog post has better demonstration built inside. We looked at a couple of other examples, right? They moved from solid to React.

[15:55]

They did it in 3 weeks and the CI was green for that. at the end that actually worked and it is a bounded problem in that case right so they can actually test it and verify it it's easier to examine and iterate so there is a clear input a clear output and I think for those agents are really good at right they can find out if what they're doing is right or not but a browser it's not as easy it's open-ended and it is ambiguous and it requires some

[16:22]

architectural judgment about trade-offs which I don't think the agents are good at yet the thing that really bugs me about this whole situation. It isn't about code quality, right? Bad experimental code exists. Sure, people write bad code too. The problem, the thing that really bugs me is the framing. Okay, cursor is no longer some random startup. They're one of the biggest names in AI assisted development today. There are millions of developers

[16:49]

who actually use that tool. So when a company with that kind of credibility says we built a browser from scratch in a week and the code doesn't compile and the from scratch claim fails and the whole thing costs like $16 million in API tokens. What it does is it damages trust not just in cursor but in the whole space right I mean I'm someone who genuinely thinks that these tools are good. I know some of you might oppose that, but the real capabilities of what

[17:17]

AI does today is already impressive enough compared to where we started. It's impressive enough that we don't need this exaggeration. Cursor could have basically hyped their own solid to React migration. That's a good example of agents actually doing useful work. Why did they not lead with that? Well, we are in this environment where every AI company feels like they have to top the last announcement. When everyone is amplifying their announcements, people

[17:44]

who are rational and people who are realistic, their story gets buried, right? The most inflated version of the story is the one that goes viral. And I keep coming back to this question. If a company like Cursor overstates the results like this, how do we evaluate smaller like less established AI companies? What's our baseline for trust? Because right now it feels like the whole industry is asking us to just kind of take their word for it. And

[18:11]

especially because AI tools are nondeterministic. You can't just take and replicate the experience just the same way. You could literally do exactly what someone claimed they did and get different results. So you kind of have to trust. And that trust is getting harder to do. So I'm curious to see how you process the news. When you see an AI news, do you think it's just hype and look at it with skepticism or do you think companies like cursor should be

[18:39]

held to a higher standard? I struggled with this myself. So, for example, for creating the thumbnail to this video, I was debating, okay, should I put $14 million or $12 million? Let me do the math. Well, if they did two trillion in I was doing the calculation to put the damn thing on the thumbnail because I didn't want to lie. And here we have these large companies who are not technically lying, but they're deceiving in bad faith. So, I don't know.

[18:46]

Shouldn't they be held accountable to a higher standard? Let me know what you think.

