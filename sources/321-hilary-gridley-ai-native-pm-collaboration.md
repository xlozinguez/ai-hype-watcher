---
source_id: "321"
title: "How AI-Native PMs Collaborate with Engineers"
creator: "Hilary Gridley & Anjali Ahuja"
platform: "Maven"
url: "https://maven.com/p/20edc1/how-ai-native-pms-collaborate-with-engineers"
date: "2026-03-19"
duration: "45:48"
type: "video"
tags: ["ai-sdlc", "enterprise-ai", "validation"]
curriculum_modules: ["06-strategy-and-economics"]
---

# 321: How AI-Native PMs Collaborate with Engineers

> **Creator**: Hilary Gridley & Anjali Ahuja | **Platform**: Maven | **Date**: 2026-03-19 | **Duration**: 45:48

## Summary

Hilary Gridley (former Head of Core Product and AI at WHOOP) interviews Anjali Ahuja (AI Product Leader at WHOOP) about how the PM-engineer relationship has fundamentally changed on AI-native teams. The central thesis is that the traditional product development flow — PM defines problem, writes spec, hands to engineering — is breaking down. On fast-moving AI teams, engineers prototype solutions before PMs can fully scope problems. The majority of shipped AI features at WHOOP now start with technical exploration rather than product requirements.

The conversation covers the full arc of how WHOOP rebuilt its AI product development process: replacing feature roadmaps with a durable AI strategy anchored by five pillars and clear KPIs, creating structured "lanes for hacking" so engineers experiment within strategic guardrails, establishing a 12,000-member AI beta group for rapid real-world feedback, and shifting from PRDs to A/B test roadmaps that systematically test 30+ variables per feature. A candid failure story — where Anjali blocked an AI strength trainer feature and lost team trust, only to gain it back through data-driven observability — illustrates why "let them cook" with real user data beats subjective PM gatekeeping.

Anjali also shares her daily AI toolkit (Cursor with Claude Code, MCP connections to Confluence and Snowflake, Replit for prototyping, custom GPTs for comms) and how design has adapted with compressed 1-2 week sprints post-incubation rather than multi-month upfront design phases.

## Key Concepts

### From Problem-First to Tech-Led Exploration

The traditional PM approach — start with problem hypotheses, validate through research, define requirements, hand off to engineering — took 2-3 months per feature. WHOOP flipped this: the majority of AI features now start with engineers discovering what's possible through prototyping, and PMs shape those explorations into shippable products. The PM role shifts from problem definition to recognizing which engineering experiments solve real user problems and packaging them for market. As Anjali frames it: she can't write requirements for capabilities she didn't know were possible.

### Durable AI Strategy Over Feature Roadmaps

Feature roadmaps became unsustainable — outdated within a month as AI capabilities shifted faster than planned features could ship. WHOOP replaced them with a six-to-twelve month strategic framework: five pillars defining what "winning with AI" looks like, each with clear KPIs. A cross-functional working group of eight (product, engineering, design, analytics, data science) spent six weeks crafting this strategy through a deliberately human process. Engineers now hack within these strategic lanes — picking pillars for monthly hack days and measuring against KPIs — rather than building aimlessly or following stale roadmaps.

### "Let Them Cook" — Trust Through Controlled Experimentation

Anjali's first principle: step in when product discipline adds value, not before. When an engineer built proactive health check-in notifications over winter break and the CPO felt "so seen" receiving one before a marathon, Anjali let the team incubate for a full month — 30 different prompt versions shipped to 30-50K members — before bringing structure. Her signal to engage: when user feedback shifts from delight to fatigue, and iterations plateau. The lesson was hard-won: blocking the AI strength trainer feature earlier had destroyed team trust, and an accidental silent ship later proved that real user data was a better arbiter of readiness than subjective PM judgment.

### A/B Test Roadmaps Replacing PRDs

Instead of writing traditional product requirement documents, Anjali now writes A/B test roadmaps: structured lists of 30+ testable variables per feature (frequency, tone, purpose, message length, check-in triggers). The team reviews results twice weekly, runs tests multiple times per week, and continuously updates the roadmap. This gives engineers clear iteration paths beyond "make it cooler" — each test maps to strategic KPIs, creating accountability without heavy process. WHOOP uses EPPO for rapid A/B test spin-up, tracking 5-8 KPIs per experiment.

### AI Beta Group as the Quality Gate

After the trust-destroying strength trainer episode, WHOOP established a 12,000-member AI beta group recruited from a demographically representative subset. Members explicitly opt in knowing features are not production-ready, and provide feedback through in-app thumbs up/down, direct chat comments with negative sentiment flagging, Typeform surveys, and member interviews. Live observability routes negative sentiment directly to PMs. This replaced subjective "is this good enough?" debates with data-driven shipping decisions: if a feature isn't hitting unacceptable scenarios (dangerous advice, data accuracy errors) and isn't declining KPIs, it ships.

### Defining "Good Enough" Through Unacceptables

Rather than defining what good looks like for each feature, Anjali defines what is unacceptable: dangerous health advice, data accuracy errors that destroy trust, privacy transparency failures. If experimentation shows no unacceptable scenarios and no KPI decline, the feature ships — even with zero positive KPI movement initially. The team ships silently, collects two months of real-world data, and iterates. This inverts the traditional quality gate from "prove it's good enough" to "prove it's not harmful."

### The AI PM's Daily Toolkit

Anjali's stack: Cursor with Claude Code connected via MCP to Confluence (for PRDs, A/B test plans, Jira tickets, comment responses) and Snowflake (for conversational analytics queries about user engagement, demographics, and drop-off). Replit for prototyping with pre-built WHOOP screen templates. Custom ChatGPT GPTs for editing messages, generating test plans, and writing marketing comms. She builds prototypes instead of writing one-pagers, finding that stakeholders react faster to interactive prototypes than documents.

## Practical Takeaways

- **Replace feature roadmaps with durable AI strategy**: Define 5-6 strategic pillars and KPIs that outlast individual features. Review and adjust every six months, not per-feature.
- **Create structured lanes for hacking**: Monthly hack days tied to strategic pillars give engineers freedom to experiment while ensuring alignment. Frame hacking around "which KPI does this move?" not "build something cool."
- **Let engineers incubate before adding PM structure**: Step in when you see user feedback shift from delight to fatigue, or when iterations plateau — not when you personally feel it's "not good enough."
- **Write A/B test roadmaps, not PRDs**: List every testable variable, prioritize by expected KPI impact, review results biweekly, and iterate the roadmap continuously.
- **Establish an AI beta group**: Recruit a demographically representative opt-in group. Ship early and imperfect to them. Use observability to flag negative sentiment automatically.
- **Define unacceptables, not perfection**: List the scenarios that are truly unacceptable (safety, accuracy, privacy). If experiments avoid those and don't decline KPIs, ship.
- **Use prototypes to drive alignment**: Build interactive prototypes in Replit or Claude Code instead of writing docs. Present 3-4 scenarios and let stakeholders react rather than discuss from a document.
- **Connect your PM tools via MCP**: Link Cursor/Claude Code to Confluence, Jira, and analytics (Snowflake) for real-time access to PRDs, tickets, and user data without context-switching.

## Notable Quotes

> "The majority of the features I ship these days start with technical exploration — what are engineers finding? What's even possible with the AI tools that we have today?" — Anjali Ahuja

> "I don't feel like I can go to engineers with a set of requirements anymore because I don't even know what is possible to be solved." — Anjali Ahuja

> "One of my first principles working with the engineering team is I like to come in when I feel like product discipline is going to add value. But if I see them cooking and I see them excited, I think the best way I can build trust is first let them cook." — Anjali Ahuja

> "Instead of writing a PRD, I actually wrote an A/B test roadmap. I laid out sort of 30 variables we could be testing." — Anjali Ahuja

> "We found that building out feature roadmaps was really becoming unsustainable. Our feature roadmaps would be outdated within a month because the tech would change so quickly." — Anjali Ahuja

> "I'd so much rather get the data directly from members as something is being iterated on than having one person be like, this isn't good enough." — Anjali Ahuja

## Related Sources

- [018: The New AI-Driven SDLC](018-circleci-ai-sdlc.md) — Complementary perspective on how AI reshapes the development lifecycle, with similar conclusions about the shift from implementation to judgment
- [320: ChatGPT Health Identified Respiratory Failure. Then It Said Wait.](320-nate-b-jones-chatgpt-health-agent-evals.md) — Related themes on AI health product evaluation and the importance of safety-first approaches in health AI

## Related Curriculum

- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — AI product strategy, organizational adoption patterns, and the evolving role of product management in AI-native teams
