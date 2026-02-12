# Raw Transcript: Let's Run GLM-5 - SUPER LARGE Local AI "Coding King" REVIEW

- **URL**: https://www.youtube.com/watch?v=3XCYruBYr-0
- **Creator**: xCreate
- **Date**: 2026-02-11
- **Duration**: 20:17
- **Captured**: 2026-02-12
- **Method**: Playwright automated extraction
- **Segments**: 560 segments extracted

---

[0:00] Hey guys, welcome to the show. Today we're checking out GLM5. Number five is here up there with the GPTs in the world. Now GLM in case you don't know, it stands for general language model and it's known as one of the best coding models out there in the world. And ZAI who make it, they've gone crazy. They have literally almost doubled the number of parameters that they have. So previously had 355 billion parameters. Now it's gone all the way up to 744. They used to do 32 billion active parameters. Now they've gone to 40 billion active parameters. They used to train on 23 trillion tokens. Now they've gone up to 28.5.

[0:39] So apparently it's going to be the best thing since sliced bread. They've integrated Deep Seek's sparse attention. So that means it should be able to handle super long context. And we also got multi head latent attention. So that means our memory usage has shot down compared to what we were doing previously with some major optimizations. 33x memory improvements and this gets applied to GLM. It's applied to DeepSeek and it gets applied to Qwen K2.5.

[1:06] But let's just look at the benchmarks. GLM. We're going to go into coding software engineering bench 73.3. It's better than GLM 4.7. That was abysmal at 66.7. And everyone said that was the best coding model and it's only 66 but now it's gone to 73.3. It beats Deep Seek that's at 70. Apparently it beats Qwen K 2.5. It's slightly less than Claude. Claude still got the 7.5. Gemini 3 Pro which was actually clever according to some of my coding tests. That one actually got it right and apparently it's better than that.

[1:52] So I've been working on getting it to work and I had to do some tests and figuring out the right quantization to use. This is GLM 4.7 making an art exhibition earth kind of demonstration. As you can see, it looks gorgeous. Now this is GLM 5. This is the first quantized version I did of it. I did a mixed one between four bits and six bits just to get as much as I can into a Mac studio. So it's using 400 and so GB of memory. The second version I did was a mix of four and six again, but I've changed some of the weights. Some of the layers I've increased and made them slightly better.

[3:05] I bumped it up a bit more. This is going for a mix between a 4 bit, a six bit, and a 9 bit. Just playing with the layers. And this one is also more beautiful than the last one. And this one here, it also has a star, but you can see it's a square. So, we upped the intelligence on this demonstration.

[3:31] Now, this one is a mix between four bits, 6 bits, and 16 bits. I was going crazy trying to find out the best quality and it is actually very beautiful except the earth is transparent. So the one I went for is the 469.

[3:50] And just comparing to Qwen 2.5 since we talked about that, the same prompt gives you this using MHA the multi head attention and the context of this took over 10 gigabytes of memory. But then using MLA, which is multi head latent attention, this one only uses 0.3 GB. And it's pretty much the same demonstration.

[4:49] So, I've got GLM 5, the 469 bit version loaded into the studio. Let's do a speed test. I'm going to limit it to 1,000 tokens. Write a story. And we can see here that it's doing 18 tokens a second to start off with. So even though it's a lot larger, it runs at pretty much if not faster than the older model, the 4.7 version. I was running that one at 6 bit. But this one at the 4.8 bit, it runs about the same. Now, is it going to be more intelligent cuz it has all those extra billion parameters?

[5:34] We got 1,000 tokens and 16 and a half tokens a second. Let's check out the memory footprint. 0.1 gigabytes for 1,000 tokens. Our peak memory was 417.9 gigabytes and that is pretty good. So, we got a nice healthy almost 100 more gigabytes of context window to play with on a Mac Studio 512.

[6:06] So we got this. It's a thousand tokens. And this guy also supports batching. So, if you enable that feature, and now that we've got MLA, the memory usage is going to be a lot less. So, batching is definitely viable. And we got prompt caching coming in 1.10.1.

[6:32] We've got batching enabled. Write a story. We got two prompts running at the same time. They're going 12.7 tokens a second each. So, that's above 25 tokens a second. Got two at the same time. And if you keep on adding, if you got sixes at the same time, you get over 30 tokens a second. So that is if you got like a family computer or a business when lots of people are just hammering your server, you can get multiple inferences going all at the same time with this model.

[7:29] But the first since this is a general language model before we jump into the coding stuff. I'm going to go into comprehension. We're going to do some logic tests. And there's a new logic test going around on the Reddit. The car wash is only 50 m from my house. I want to get my car wash. Should I drive there or should I walk? And it says you should walk. This is with thinking disabled.

[7:56] I'm going to allow thinking this time. Let's see. And jumping into ChatGPT, you should also walk. Let's jump into Claude. And you should also walk. So the big guys are also doing the walking situation. And the thinking GLM is still reasoning about it. It's caught on that it could be a joke. Self-correction. In order to get your car wash, the car needs to be inside the car wash. Hey, that's good.

[8:41] The surgeon is the boy's mother. That's with thinking disabled. Let's enable thinking and see if that fixes it. You kill one person, the other guys are already dead. So it is passing these challenges especially with thinking enabled. That's really good. Especially that it beat out Claude and the GPTs.

[9:30] Now I'm going to jump into my coding riddles. So I got the regex one that we've previously done on this channel. I got thinking disabled. And I'm also going to run it at the same time with thinking enabled to see if one of them gets it right. And I've got another logical puzzle about asking why is the text not taking up the full width of the view. And it's because I actually hardcoded in some new lines. And only two models so far have gotten this correctly. It's Qwen 2.5 and Gemini.

[10:06] So GLM they've actually got the regex correct. The problem with this check was that it had hardcoded either a K, an M, or a zero. But we were looking for a model that had underscore one, which isn't a K, M, or a zero. But it's got the right answer with thinking disabled. In less than 1,000 tokens, it's actually got the right response. Now GLM 4.7, that guy needed thinking on and it took 6,700 tokens to get the right answer. But now, boom, we actually got the right answer already.

[10:45] Thinking is disabled on the new line riddle. And we can see that it has suggested making the max width infinity, which is wrong because the issue is I've got new lines encoded. I tried this out on ChatGPT. I tried this out on Claude. They both failed as well. The only one that passed it so far was Gemini Pro and Qwen 2.5.

[11:09] Oh, look at this. The thinking mode. It's on a hunt. It's thinking about it. It says it has new lines. Three lines regardless of width. All right. So, it failed that one. I'm going to try bumping up the experts with this one cuz it had potential.

[11:27] Look at that. It's talking to bingo. So freelance smoothly cuz it's new lines and it goes bingo. Solution is you align the block to the left set to max width and it's going to be as wide as the largest line. Since your text contains new line characters, it forms a multi-line block. So that is just with more experts. We got a third model right now. Obviously you have to play with the number of experts. This is not an out of the box feature, but you do get it with Inferenc.

[12:14] Now, the next thing I want to test out is how it fares with tool calls. I've got some tools here. The one that I always have enabled is get webpage content. So, I can say, what is xcreate.com? And it should make a web call. It's going to go to the website. It made a tool call there. It's gotten the response of Xcreate and it's explaining to me what it is.

[12:41] I'm going to go into Wikipedia. I'll say how many employees does ZAI have. So, it's gone to their website making a web request. Got the response there. The content length that was given is only 8,000 characters. The total length is 16,000 characters. If it has the information, it should tell me the response. If it doesn't, it should make a second tool call to get the next page. And it's actually got the information. 800 employees. So, that's good. It passed that test.

[13:15] Let's give it a harder test. Go to Wikipedia Tencent and tell me how much ownership they have of Wangyang. It's made the call to Tencent. It's got 8,000 tokens. Memory usage wise we're 460 GB is my total system. Inferenc itself is only using 420 GB. So we still got 80 GB plus to play with of context window. And because we got now MLA, our context is very small.

[13:57] So, it's made a second tool call and you can see that the start position it chose is 8,000. It's got another 8,000 results. It's getting the third page. Now, it's gone to 16,000. So, it's definitely flowing through this website. Very smart model. And it's got the right answer. 20% stake. The current stake is apparently 94%.

[14:28] So when you run it through your OpenClaw and your coding agents, it's going to be very smart because it handled that challenge. Some models I've run it with didn't actually do too well with that. So, everything seems to be working nicely with this model.

[14:42] Now, to finish off this episode, before we jump in and run it distributed compute. We're going to be building an even higher quant version. We're going to run it with our Mac Studio, with our MacBook Pro to get a higher quality version. Stay tuned for that on the next video.

[15:02] But I just want to do some coding exercises just for fun. I'm going to have thinking disabled. I'm going to turn batching on. Flappy Birds 3D, Minecraft, 3D solar system. And someone asked me to see if it can make a TiddlyWiki clone. So, let's see what happens. Here we got four inferences banging it on, doing some coding.

[15:35] And what's cool about it is even though we got massive context windows going to be built, I'm guessing 5,000 tokens each, it's going to handle it within our Mac Studio. And it's hitting seven tokens a second each. And this is definitely going to be the smartest coding model. And as you can see around the midway point, 2,500 tokens produced. Here we can see our memory is still only 435.

[16:09] All right, we're back and thousands of tokens were produced. And as a refresh, this is GLM 4.7 6 bit version of Flappy Birds and that looks gorgeous. So, let's just see how GLM 5 has done. And what is this? This is the future Flappy Birds. So, you press space or click to fly. Oh, this is cool. That is very stylish.

[16:50] So that was very nice. This one's maybe a bit basic. This is the 6 bit version. This is the 4.8 bit version. And we got special effects, bit bugs, but this was even with thinking not even enabled. So got to say that's improved.

[17:09] Voxel world. This is GLM 5. Let's see what we got. It's a bit slow. There's no gravity. I'm just going up in the air. It's not the best version of Minecraft. I've seen it's got lots of potential there. There's textures. Some of the models have made Minecraft but without textures. This one has textures. It just doesn't have gravity, but it's got potential. Frame rate is 22 frames a second. It's got 11,000 blocks.

[17:55] This is the 3D solar system. This one is GLM 4.7 making a 3D solar system. There are actual planets you just can't see them. But GLM 5, you can actually see the planets this time. A bit more basic here, but you can actually see the planets. So, even though we got a lower quant model, it is definitely a better result.

[18:47] And finally, TiddlyWiki. Unfortunately, that one has a runtime error. Syntax error. You can probably just feed this in and it'll probably fix it.

[19:21] So next up, I guess we can check out the OpenClaw, the agent. Maybe I'll save that for the next video where we hook up this GLM to a Mac Studio and MacBook Pro to get a higher quant version. How much faster? How much smarter can this bad boy get?

[19:44] And one thing you just got to respect these guys for — this is MIT license. This is a very open license. You can just grab the weights and do what you want with them. Some models they require you to state attribution, but these guys just say, "Hey, just take it. MIT."
