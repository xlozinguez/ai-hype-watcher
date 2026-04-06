---
source_id: "501"
title: "Code that shouldnt have made it to production"
creator: "TheStandupPod"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=ILizAdc4mLY"
date: "2026-03-31"
duration: "10:10"
type: "video"
tags: ["ai-sdlc", "vibe-coding"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 501: Code that shouldnt have made it to production

> **Creator**: TheStandupPod | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 10:10

# Code That Shouldn't Have Made It to Production

## Summary

This episode of The Standup Pod features a candid, experience-driven conversation about the surprisingly permanent nature of production code. The hosts share war stories from companies like Netflix, Epic Games, and Rad Game Tools, illustrating a near-universal truth in software development: code that was written hastily, experimentally, or outright badly has an uncanny ability to survive indefinitely in production systems — long outlasting the intentions or warnings of the people who wrote it.

The conversation centers on a vivid confession from Casey about a self-built build utility called CDEP, created at Rad Game Tools when cross-platform build systems were immature. What started as a clever-sounding idea — inferring build dependencies by parsing source code comments and using string replacement — became a decades-long burden. Senior engineers invested thousands of hours building on top of this fundamentally broken foundation, resulting in tens of thousands of lines of unmaintainable, undebuggable build scripts that the company still runs on today.

The deeper pattern the hosts identify is that bad code doesn't just survive — it *compounds*. Other skilled engineers optimize around it, add layers on top of it, and encode institutional knowledge into it, making it progressively harder to replace. The CDEP story is a cautionary tale about technical debt not as a slow accumulation but as a sudden crystallization: one poor foundational decision that gets load-bearing before anyone realizes the danger.

## Key Concepts

### The Permanence of Shipped Code
Code has a near-zero chance of being removed once deployed to production, regardless of quality, documentation warnings, or original intent. The hosts describe finding unchanged code from the 1970s and 80s at Epic Games — some originally written by the CEO — still running in critical healthcare logistics systems. The realistic mental model for any shipped code is: assume it will run for decades.

### Load-Bearing Bugs and Accidental Contracts
When old or broken code survives long enough, its bugs become features that downstream systems depend on. The hosts describe stumbling into legacy codebases and immediately closing the file — not out of laziness, but because fixing a decades-old bug in a live system could silently break workflows that billions of dollars depend on. The correct response is often strategic avoidance.

### The "Seems Good at First" Failure Mode
The most dangerous bad code is code that appears to work well on initial use. CDEP built dependencies automatically by parsing includes and comments, which felt like a breakthrough on first use. This early success signal caused Casey to share it, Jeff Roberts to invest heavily in it, and the company to become structurally dependent on it — before anyone understood its fundamental limitations. A tool that fails immediately teaches you nothing; a tool that fails after years of investment is a catastrophe.

### A/B Testing as a Vector for Technical Debt
The hosts argue that A/B testing cultures systematically encourage cowboy coding: developers build deliberately rough implementations to test a hypothesis quickly, the test "wins," and the rough code gets promoted to production without ever being productionized. The incentive structure rewards shipping speed over code quality, and the follow-up cleanup almost never happens. This creates a pipeline of intentionally under-engineered code flowing into long-lived production systems.

### The 10x Engineer Inversion
The episode coins a sharp inversion of the "10x engineer" myth: the truest 10x engineer creates 10x more work for everyone else. Casey's CDEP didn't just fail to help — it actively made the outcome worse than if nothing had been built at all. Jeff Roberts would have built a proper, maintainable utility from scratch. Instead, he spent years optimizing on top of garbage, encoding irreplaceable institutional knowledge into an unreadable system. The lesson is that a mediocre solution is often worse than no solution, because it forecloses the better path.

## Practical Takeaways

- **Treat every line you ship as potentially permanent.** Write, document, and test code under the assumption it will outlive your tenure, your team, and possibly the technology stack around it — because statistically, it might.
- **Never build on a foundation you haven't stress-tested.** The CDEP story shows how early investment by capable engineers can lock in a bad foundation. Before allowing others to build on your work, validate the core abstraction — not just that it works on the happy path.
- **Recognize "load-bearing legacy" and leave it alone.** When you stumble into decades-old code in a production system, the correct default is to close the file. The cost of understanding the full dependency graph almost always exceeds the value of the fix, and the risk of silent breakage is real.
- **Build A/B test infrastructure with a productionization gate.** If your org runs A/B tests, establish a formal step that requires winning variants to be refactored to production standards before full rollout. The test-to-prod pipeline is a reliable debt injection point.
- **When evaluating your own tools or abstractions, ask: what does skilled engineering on top of this look like?** The danger isn't that bad tools stay small — it's that good engineers invest in them, making them indispensable. Audit your foundational work before others build on it.

## Notable Quotes

> "If you write something, there is a non-zero chance that it will be used for potentially decades. It does not matter if it is utter garbage. It does not matter if you tested it. It does not matter if you put a thing at the top that says 'do not use this, it will destroy the world.' People will just deploy stuff."

> "There's billions of dollars residing on that bug. You do not fix or touch this. You close your editor and walk away for a little bit if you accidentally end up in there."

> "The truest 10x engineer makes 10x more work for everybody else... just not having this tool would have been much better, because then Jeff would have made something much less crappy. I basically took all of this other work that was actually useful and I made it suck by having it start with something awful that it never got rid of."
