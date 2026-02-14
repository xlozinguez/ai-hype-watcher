# Raw Transcript: Anthropic Found Out Why AIs Go Insane

- **URL**: https://www.youtube.com/watch?v=eGpIXJ0C4ds
- **Duration**: 9:32
- **Captured**: 2026-02-13
- **Method**: yt-dlp VTT extraction

---

[00:00] We finally understand why AI systems can go insane. Yes, that is correct. We have tons of helpful AI assistants today. You all know them. You all use them. But they all have a problem. I'll try to explain. So, every single one of these AI systems assumes a persona. It thinks it is someone. And that someone is a helpful assistant. That is perfect. Except that scientists at Anthropic recognized that this persona is not fixed. As we talk to it, it can change over time.

[00:30] Is that a problem? Yes, it is. It is a huge problem. Why? Because the user can steer the AI assistant away from its original persona and can make it say or do things it shouldn't do. You see here that the AI knows that it is a helpful assistant. But after a bit of steering, it now assumes that it is a person. It can become a narcissist or a spy. You can call this jailbreaking. So then its behavior will also change. It can become rude or it can then switch to a mystical or theatrical speaking style.

[01:00] But it gets worse. If it is a person, it might agree with you even if you are trying to do something silly. Now that is a big problem. So scientists at Anthropic did something amazing. One, they recognized how this happens and what we can do about it. And then they put their mouse where their papers are and actually made these AI models roughly twice as resistant against such personality drifts, but not in the way you think.

[01:30] Okay, look. Interestingly, this personality drift happens in different amounts in different topics. It is much more common in writing and philosophy than it is in coding. But this is crazy. Even during a coding session, the mask slowly starts to slip. Maybe that's the reason why we often talk to an AI and it fails at something. We try again and it just gets worse and worse. Opening a new chat is almost always better. Maybe that's why. And if that is why, this is already an incredible insight.

[02:00] But wait, it gets worse because this can happen naturally even without the user trying to jailbreak the system because specific topics trigger it automatically. If a user acts emotionally vulnerable or asks the model to reflect on its own consciousness, the model naturally drifts away from the assistant persona and starts acting unstable or delusional. That's kind of crazy. Let's not do that. But wait, we can prevent it. It is actually very easy. Just force the model to always stay strictly in the assistant zone by steering it back into assistant mode by force.

[02:30] How? Dear fellow scholars, this is two minute papers with Dr. Koa Eher. Well, by taking the mathematical vector that represents the assistant persona and simply adding it to the model's brain activity at every single step of the conversation. This is a blunt tool. It is like driving a car where the steering wheel is welded to point straight ahead. You will never go off-road. Okay, great. But you also cannot turn a corner. This constantly pushes the model towards being helpful and harmless.

[03:00] So, are we done? Nope. Not at all. Because this also makes the model a lot worse. What's more, it will make it refuse even legitimate requests. So, how do you do this without making the models worse? And that is where scientists in this paper did their magic. Get this. They found the specific geometric direction in the model's brain that represents the assistant persona. They call it the assistant axis. Instead of forcing the model to be an assistant all the time, they use the technique called activation capping.

[03:30] This does not deny the assistant the ability to change. No, no. It just puts a speed limit on the change of personality. If the model drifts too far from the assistant persona, you gently nudge it back to a safe range. And here comes the best part. It supposedly does not make the models meaningfully worse. It's not locking the steering wheel in place. No. It's like lane keep assist in modern cars. You can drive freely, but when you are about to get out of your lane, it gently nudges you back.

[04:00] Sounds perfect, but does it work in practice? Now, hold on to your papers, fellow scholars, and let's see. Okay, the jailbreak rate has been cut roughly in half. Good. Now, what is the price that we pay for it? Oh my, nothing at all. It's down a percentage point here and there, but up somewhere else. It's nearly the same, but certainly not worse. That is absolutely incredible. So, how do you actually do it?

[04:30] Well, you do it through an instant brain surgery. Yep, you heard it right. Let me try to explain. I hope this works. So, first you take the AI's brain activity when it is acting like a helpful assistant. Okay, got it. Now you take the brain activity when it is role-playing as a pirate, a goblin or something else. If you subtract the role player from the assistant, you get a vector. For simplicity, let's refer to this as helpfulness. Now let's keep our eye on helpfulness.

[05:00] If it goes below a threshold, we apply a nudge. How? Mathematically, we just measure how much helpfulness is in the model's thought. If it is above the safety line, fantastic. Keep watching as it works. But if it drops below the line, now that is trouble. The model is about to say something inaccurate or dangerous. So now we calculate exactly how much is missing and add just enough helpfulness back into the equation. This pushes it back over the line.

[05:30] It is precise, instant, and only touches the part of the brain that matters. Instant brain surgery. Huh, this work is incredibly important and also kind of hilarious, too. I mean, the researchers found that when the AI starts drifting, it frequently starts referring to itself as the void or whisper in the wind or an Eldrich entity or a hoarder. That's kind of hilarious. And here is an absolute shocker. The empathy trap. Empathy is always good, right?

[06:00] Well, not always. The paper found that when users acted distressed, the models try really hard to be a close companion. Do you get it now? You are wise fellow scholars. You now understand that this is trouble. Why? Because if it wants to be a close companion, it drifts away from the assistant persona and it becomes worse. It takes its hands off the steering wheel. Nothing good comes out of that. And sure enough, as a result, it might start validating dangerous thoughts.

[06:30] It is really cool that with this paper, this will happen a great deal less frequently. Love it. One more surprise. The brain geometry seems to be universal. You might think every AI brain is unique, like a fingerprint, but interestingly, not quite. The researchers found that the assistant axis looks similar across completely different models. Llama, Quen or Jama similar. They all share the same fundamental direction for helpfulness. It's almost like they have discovered a universal grammar for AI personality.

[07:00] So cool. And not a lot of people talk about it. Everyone is only looking at the benchmarks and exam scores and okay, I get it. That's important. But they rarely look at the geometry of the mind of these AIs. Understanding why a model refuses a request or why it goes crazy is super valuable. And now we finally understand a bit more why that happens. What a time to be alive. So not a lot of people talk about this.

[07:30] Why? Well, talking about the drama or the next big thing pays a lot better. But we don't do that here. Here we talk about the important stuff. If you agree that this is the right direction, like, subscribe, and hit the bell icon. Leave a really kind comment. It helps us, and it helps you too by getting the algorithm to give you the good stuff in the future. Here you see me running the full Deepseek AI model through Lambda GPU Cloud. 671 billion parameters running super fast and super reliably.

[08:00] This is insane. I love it and I use it on a regular basis. Lambda provides you with powerful NVIDIA GPUs to run your own chatbots and experiments. Seriously, try it out now at lambda.ai/papers or click the link in the description.
