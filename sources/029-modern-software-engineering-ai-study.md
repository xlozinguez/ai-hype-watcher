---
source_id: "029"
title: "We Studied 150 Developers Using AI (Here's What's Actually Changed...)"
creator: "Modern Software Engineering (Dave Farley)"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=b9EbCb5A408"
date: "2026-01-27"
duration: "11:55"
type: "video"
tags: ["ai-hype", "ai-sdlc", "enterprise-ai", "vibe-coding"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 029: We Studied 150 Developers Using AI (Here's What's Actually Changed...)

> **Creator**: Modern Software Engineering (Dave Farley) | **Platform**: YouTube | **Date**: 2026-01-27 | **Duration**: 11:55

## Summary

Dave Farley presents findings from a pre-registered controlled experiment he co-authored, studying 151 participants (95% professional developers) to measure the downstream maintainability of AI-assisted code. Unlike most AI productivity studies that stop at "did the developer finish faster," this research specifically measured what happens when a different developer has to understand and modify the code later -- a much better proxy for real-world software costs given that maintenance represents 50-80% of total ownership cost.

The headline finding is nuanced: AI-assisted code was no harder and no easier to maintain than human-written code. There was no measurable difference in downstream maintenance cost, code quality, or test coverage between the two groups. AI users were roughly 30% faster during initial development (55% for habitual users), confirming the productivity claim, but critically this speed did not come at a hidden maintainability cost. A secondary finding showed that experienced developers who used AI habitually produced code with slightly improved maintainability, potentially because AI tends to generate "boring, idiomatic, unsurprising" code -- and boring code is good for maintenance.

Farley frames the results through his central thesis: AI acts as an amplifier of existing developer capability, not a replacement for engineering discipline. Skilled developers get better outcomes; unskilled developers dig deeper holes faster. The study also identifies two emerging risks -- code bloat from near-zero generation cost and cognitive debt from developers who stop thinking critically about their code -- neither of which appears in sprint-level metrics but could compound into serious long-term problems.

## Key Concepts

### Maintenance Cost Dominance

Farley opens by establishing the economic reality that most AI studies ignore: maintenance costs 3-4x more than initial development, representing 50-80% of total cost of ownership ([0:55](https://www.youtube.com/watch?v=b9EbCb5A408&t=55)). This makes "did the developer type faster?" a deeply insufficient metric. The real question is what happens after the AI has written the code -- when the next developer has to understand it, change it, and maintain it ([0:17](https://www.youtube.com/watch?v=b9EbCb5A408&t=17)). Most AI productivity claims focus on the cheapest phase of software development while ignoring the most expensive one.

### Two-Phase Experimental Design

The study used a rigorous two-phase methodology that separates AI-assisted creation from human maintenance ([3:07](https://www.youtube.com/watch?v=b9EbCb5A408&t=187)). In Phase 1, developers added a feature to buggy Java code -- some with AI assistants, some without. In Phase 2, a different set of developers received Phase 1 output and had to evolve it, with no knowledge of whether the code was AI-assisted and no AI tools allowed. This design isolates the maintainability signal from the productivity signal and measures what actually matters: how easy the code is for someone else to change ([3:32](https://www.youtube.com/watch?v=b9EbCb5A408&t=212)).

### AI as Capability Amplifier

The study's results align with the DORA research conclusion that AI coding assistants act as amplifiers rather than equalizers ([7:00](https://www.youtube.com/watch?v=b9EbCb5A408&t=420)). Developers already practicing good engineering -- small batches, continuous testing, modular design, rapid iteration -- get amplified benefits. Developers with poor practices produce poor results faster. Farley cites Jason Gorman's breakdown of what "doing the right things" means in an AI context: small batches, one problem at a time, continuous testing and refactoring, highly modular designs, and high-autonomy decision-making ([8:03](https://www.youtube.com/watch?v=b9EbCb5A408&t=483)). Junior developers cannot "vibe their way to good systems" ([7:08](https://www.youtube.com/watch?v=b9EbCb5A408&t=428)).

### Code Bloat and Cognitive Debt

The study authors flag two long-term risks that don't show up in sprint metrics ([9:22](https://www.youtube.com/watch?v=b9EbCb5A408&t=562)). Code bloat occurs when generation becomes nearly free, tempting developers to produce far more code than necessary -- and volume alone is a massive driver of complexity. Cognitive debt is the more insidious risk: when developers stop deeply thinking about the code they produce, understanding erodes, skills atrophy, and innovation slows ([9:46](https://www.youtube.com/watch?v=b9EbCb5A408&t=586)). These are exactly the kinds of costs that compound over years while remaining invisible to short-term productivity dashboards.

### Boring Code as a Feature

Experienced, habitual AI users produced code with a small but measurable improvement in downstream maintainability ([6:28](https://www.youtube.com/watch?v=b9EbCb5A408&t=388)). Farley hypothesizes this is because AI tends to generate "boring, idiomatic, unsurprising code" -- and in software maintenance, surprise is the enemy ([6:44](https://www.youtube.com/watch?v=b9EbCb5A408&t=404)). This is a notable counter to the fear that AI code is inherently worse; when guided by experienced hands, AI's tendency toward convention may actually be an advantage.

## Practical Takeaways

- **Measure what matters**: Stop evaluating AI tools purely on speed-to-completion. Maintenance cost is the dominant expense in software -- any honest productivity assessment must include downstream impact on changeability.
- **Developer skill outweighs tool choice**: The study shows that who uses the AI matters more than whether AI was used. Invest in engineering fundamentals (testing, modular design, refactoring discipline) before investing in AI tooling.
- **Treat AI speed gains as real but bounded**: A 30% speed improvement (55% for habitual users) is meaningful but far from the 10x claims circulating in the industry. Calibrate expectations accordingly.
- **Watch for code bloat**: When generation is cheap, actively resist the temptation to produce more code. Apply the same code review rigor to AI-generated code as to human-written code -- more code is more complexity.
- **Preserve deep thinking**: Deliberately maintain the habit of reasoning about code structure, design tradeoffs, and problem decomposition. These skills atrophy when fully offloaded to AI and are precisely the skills that differentiate good outcomes.
- **Embrace boring code**: AI's tendency toward idiomatic, unsurprising patterns is a feature for maintainability, not a bug. Resist the urge to make AI-generated code more "clever."

## Notable Quotes

> "What happens after the AI has written the code? What happens when the next developer has to understand it? When the code has to be changed? When it has to be maintained?" — Dave Farley ([0:17](https://www.youtube.com/watch?v=b9EbCb5A408&t=17))

> "Most AI studies stop at 'did the software developer finish faster? Did they type fewer characters?' That's not engineering. That's measuring typing speed." — Dave Farley ([1:50](https://www.youtube.com/watch?v=b9EbCb5A408&t=110))

> "Code written with AI assistance was no harder to change, no easier to change, no worse in quality and no better in quality." — Dave Farley ([5:25](https://www.youtube.com/watch?v=b9EbCb5A408&t=325))

> "AI tends to produce boring, idiomatic, unsurprising code. And boring code is good. Surprise is usually the enemy of maintainability." — Dave Farley ([6:44](https://www.youtube.com/watch?v=b9EbCb5A408&t=404))

> "Tools amplify capability. They don't replace it." — Dave Farley ([7:43](https://www.youtube.com/watch?v=b9EbCb5A408&t=463))

> "This compartmentalization through decomposition is the central fundamental aspect of building software. This is the real technical skill at the heart of what it is that we do." — Dave Farley ([10:51](https://www.youtube.com/watch?v=b9EbCb5A408&t=651))

## Related Sources

- [025: AI productivity bubble: 'There is a reckoning coming for employers'](025-natasha-bernal-ai-productivity-bubble.md) — Bernal explores the burnout side of AI productivity gains; Farley's study provides empirical grounding that speed gains are real but bounded, while both warn about hidden costs beneath surface-level productivity metrics
- [022: Developers are forced to use AI](022-traversy-media-forced-ai.md) — Traversy's "architect vs. builder" framing aligns with Farley's finding that developer skill matters more than tool usage; both emphasize that beginners cannot skip foundational engineering knowledge
- [005: Most People Aren't Ready for Vibe Coding](005-nate-b-jones-vibe-coding-readiness.md) — Nate's vibe coding readiness framework directly supports Farley's conclusion that AI amplifies existing capability rather than replacing it
- [007: Super Bowl Commercial Bubble Curse](007-internet-of-bugs-ai-bubble.md) — Internet of Bugs' hype cycle analysis provides context for the inflated productivity claims that Farley's controlled study pushes back against (30% vs. claimed 10x)
- [024: You are Not Ready: Agentic coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) — Van Eyck's practical agentic coding patterns represent the "doing the right things" that Farley argues AI amplifies

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — Farley's controlled study provides the strongest empirical evidence yet for calibrating AI productivity expectations: real gains exist but are far more modest than industry claims, and maintenance cost remains the dominant concern
- [Module 06: Strategy & Economics](../curriculum/06-strategy-and-economics/README.md) — The maintenance cost dominance argument (3-4x initial development) directly informs enterprise AI adoption strategy: organizations optimizing only for initial development speed are optimizing for the wrong phase
