---
source_id: "327"
title: "we're so back"
creator: "The PrimeTime"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=5DP0az1q_8M"
date: "2026-03-19"
duration: "10:49"
type: "video"
tags: ["agentic-coding", "vibe-coding", "ai-hype", "prompt-engineering", "validation"]
curriculum_modules: ["01-foundations", "02-prompting-and-workflows", "04-agentic-patterns"]
---

# 327: we're so back

> **Creator**: The PrimeTime | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 10:49

# we're so back — AI Debugging a 6-Month Bug (Mitchell Hashimoto / Ghostty)

## Summary

Prime reacts to Mitchell Hashimoto's post about OpenAI Codex (o3 at "extra high" reasoning) solving a persistent GTK4 screen-flicker bug in Ghostty that had stumped Mitchell and his team for over six months. The AI's decisive move was going beyond the project's own source code to read GTK4's C source directly — something lower reasoning settings and competing models (including Opus 4.6) failed to do. The root cause turned out to be unnecessary destruction and recreation of leaf-node surfaces on every split, which the AI identified and patched in roughly 50–60 lines of changes costing $4 over 14 minutes.

Prime's take is more nuanced than a simple "it's over" reading. He emphasizes that Mitchell still performed a thorough code review, asked probing follow-up questions, required additional changes to failure modes, and did manual cleanup — none of which is trivial. The AI handled the hardest part (forensic research across foreign codebases) while the human handled taste, correctness judgment, and code quality. This division of labor is what Prime finds genuinely encouraging rather than threatening.

The broader reflection is that the highest-leverage AI use case isn't "vibe coding" your whole app but rather delegating the specific class of problem that is deeply unfun and time-consuming: tracing undocumented behavior through layers of foreign source code. Prime draws a parallel to his own Honey investigation, where AI dramatically accelerated reading minified JavaScript. He concludes that AI is stripping away the least pleasurable parts of engineering — not the problem-solving itself.

## Key Concepts

### Reasoning Depth as a Critical Differentiator
The bug was only solved at "extra high" reasoning effort with Codex o3. Lower reasoning settings on the same model failed, as did other frontier models. The key behavior that made the difference was the AI's decision to leave the project's own code and go read GTK4's upstream C source — a research step that requires broad contextual judgment, not just code generation. This suggests that for hard debugging tasks, reasoning budget matters enormously and cheap inference is the wrong tool.

### AI-Assisted Forensic Debugging
The video illustrates a specific and high-value use pattern: using AI to trace root causes through large, unfamiliar, or poorly documented codebases. This is distinct from "write me a feature." The prompt was intentionally vague ("use GitHub to look up this issue and determine a fix"), and the AI performed multi-step investigative work — reviewing commits, narrowing to suspect operations, then cross-referencing upstream library source. This is closer to agentic research than code generation.

### The 80/20 Review Obligation
Prime identifies a failure mode he calls the "vibe coder" pattern: accepting AI-generated code without rigorous review because it seems to work and tests pass. Mitchell's workflow is held up as the counter-example — he reviewed the fix in detail, questioned specific implementation decisions, demanded changes to error-handling paths, and did manual cleanup. Notably, the AI also introduced two new simple bugs in the process. The human review layer is what converts AI output into production-quality code.

### Segmenting Work by Human vs. AI Comparative Advantage
A reframe Prime offers: rather than choosing between "write everything by hand" or "full Daario-take-the-wheel AI," the most effective posture is identifying which tasks have unfavorable time-to-insight ratios for humans (deep source archaeology, reading minified code, correlating commits across repos) and delegating those specifically. The human retains ownership of taste, architecture opinions, and final judgment.

### The Hype Cycle Framing
Prime opens by naming the recurring "it's over / we're so back" cycle in AI discourse and uses this example to complicate both poles. Even a genuine "it's over" moment (AI solving a 6-month bug in 14 minutes) is also a "we're so back" moment for skilled engineers who know how to direct and review AI work. The outcome reinforces the value of engineering judgment rather than replacing it.

## Practical Takeaways

- **Use high reasoning budgets for hard bugs.** Don't default to cheap/fast inference when the problem involves cross-codebase root-cause analysis. The qualitative jump at "extra high" was the difference between success and failure here.
- **Write vague, intent-driven prompts for investigative tasks.** Mitchell's prompt didn't prescribe a solution path; it gave the AI latitude to go wherever the evidence led, including upstream library source. Over-specifying the search space would have prevented the breakthrough.
- **Never skip the code review, even after a win.** AI fixed one hard bug and introduced two simple ones in the same change. Treat AI output as a strong junior PR: impressive research, requires careful review before merge.
- **Identify your "source archaeology" tasks and delegate them first.** These are the tasks with a bad human experience-to-insight ratio — reading unfamiliar C libraries, grepping minified JS, bisecting undocumented behavior. AI's ROI is highest here.
- **Ask "why" after the fix.** Mitchell's follow-up prompt ("explain in detail what you fixed") produced a clear explanation of the leaf-node surface reuse mechanism. Extracting this understanding preserves institutional knowledge and catches reasoning errors before they ship.

## Notable Quotes

> "The best thing that Codex did was eventually start reading the GTK4 source code. That's where I ended up seeing my GitHub issue, and I knew the answer was somewhere in there, but I didn't have the time or the motivation to do it myself. The other models never went there."
— Mitchell Hashimoto (quoted by Prime)

> "These are the things that make me so excited about AI because this is truly stripping away the things in programming that I find to be the least pleasurable parts of it. It's no longer problem solving — you're just actually just trying to swim through a river... just so fine-grain going into something just to find the one hidden answer."
— Prime

> "I don't often use it this way enough, which is like, okay, here's something that I know can take a lot of time. It's going to take a lot of research. You go get me 80% of the way there. I will do the other 20%."
— Prime
