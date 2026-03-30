---
source_id: "424"
title: "AI Software Engineers are Too Expensive"
creator: "Philip Bohun"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=CfpxWupvuOU"
date: "2026-03-25"
duration: "17:03"
type: "video"
tags: ["ai-economics", "ai-hype", "infrastructure", "ai-landscape"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 424: AI Software Engineers are Too Expensive

> **Creator**: Philip Bohun | **Platform**: YouTube | **Date**: 2026-03-25 | **Duration**: 17:03

# AI Software Engineers are Too Expensive

## Summary

Philip Bohun argues that current AI model pricing is deeply subsidized—potentially by 10-25x or more versus break-even costs—and that the economics of large frontier models are fundamentally unsustainable. He surveys the three main levers for improving AI capability (data, model size, and inference-time compute) and concludes that all three are hitting diminishing returns simultaneously: training data is largely exhausted (with model collapse from AI-generated content as an additional hazard), frontier models at 3-5 trillion parameters already require dozens of GPUs per user to serve, and extended "thinking" loops yield rapidly diminishing improvements while adding latency. The only credible path to a step-change, he argues, is an algorithmic breakthrough on the order of the transformer—which, by definition, cannot be planned or scheduled.

Given these constraints, Bohun predicts a significant pricing correction once subsidies roll back, estimating true-cost pricing at 30-40x current rates. He expects large frontier models to become economically unviable and anticipates a shift toward smaller, domain-focused models (in the 70B parameter range) that can actually turn a profit—though he notes that models at that scale can also be run locally, further threatening the commercial viability of cloud AI providers. For practitioners, his core recommendation is to use AI now while it remains cheap, but to treat it as a reference tool rather than an integral workflow dependency, and to actively protect your own skills from atrophy.

The video is skeptical of the "AI will replace software engineers" narrative, using Anthropic's demo of a C compiler (which produced slow code and lacked type checking) as evidence that even state-of-the-art frontier models fall far short of the zero-oversight standard that true replacement would require. Bohun frames the current moment as a window of subsidized experimentation that practitioners should exploit deliberately, while remaining structurally prepared for a much higher-cost environment within the next year or two.

## Key Concepts

### Massive Subsidies Distort the True Cost of AI

AI companies have publicly acknowledged charging far below cost. Anthropic's own framing of a $200 subscription delivering $5,000 in compute is cited as evidence. When measured against reported losses, Bohun estimates current pricing would need to increase 10-25x just to break even—and potentially 30-40x to also service accumulated debt, pay investors, cover taxes, and fund growth. This means the pricing signals practitioners use today to evaluate AI's ROI are systematically misleading.

### Diminishing Returns Across All Three Scaling Axes

The three traditional levers for improving model capability—training data volume, model parameter count, and inference-time compute (looping/thinking)—are each hitting diminishing returns. The internet's human-generated data corpus is largely consumed, with AI-generated content creating model collapse risk. Model scaling continues to yield improvements but at a declining rate, with costs growing faster than capability gains. Extended inference loops improve outputs initially but quickly plateau, adding latency with little marginal benefit. Without an algorithmic breakthrough, there is no obvious fourth lever.

### Model Collapse from AI-Generated Training Data

As AI-generated content saturates the web (articles, reviews, social media, code), models trained on scraped internet data increasingly ingest their own outputs. This feedback loop degrades model quality over successive training runs—a phenomenon known as model collapse. It represents a structural ceiling on the data-scaling approach and makes indiscriminate web crawling progressively less viable as a data sourcing strategy.

### The True Replacement Bar Is Zero Human Oversight

Bohun defines "replacing a software engineer" as producing code that requires no human review—covering design, engineering, testing, and QA entirely autonomously. By this standard, current frontier models (evidenced by the Anthropic C compiler demo, which produced slow, type-check-free code) are nowhere close. This framing is useful for calibrating where agentic coding tools actually sit on the capability curve versus where they would need to be to justify displacement claims.

### Small, Focused Models as the Economically Viable Tier

Models in the 70B parameter range, fine-tuned for specific domains, are likely to be the sweet spot where AI companies can actually charge profitable prices. However, this tier is also runnable locally, which undercuts the cloud providers' position. The implication is a potential bifurcation: large frontier models become unaffordable or disappear, while small local/specialized models commoditize. AI companies that built their business on frontier-model subscriptions face structural revenue risk from both directions.

## Practical Takeaways

- **Don't build critical workflow dependencies on AI at current prices.** When subsidies end and prices rise 30-40x, any workflow where AI is load-bearing becomes a liability. Use AI as an accelerant, not infrastructure.
- **Treat the current pricing window as a learning subsidy.** Use cheap AI access now to build skills, explore capabilities, and understand limitations—as you would exploit a temporary discount on professional education.
- **Protect your own skills from atrophy.** Studies already show measurable skill decay when developers offload cognitive work entirely to AI. Use AI as a reference book or Stack Overflow replacement, not as a ghostwriter.
- **Watch for price inflection signals.** Bohun estimates meaningful price increases will be visible within roughly a year (by early 2027). If your team or product roadmap depends on current AI pricing, build contingency plans now.
- **Be skeptical of "agent replaces engineer" claims.** The gap between current AI capability and zero-oversight autonomous coding remains enormous; the C compiler demo is a useful reality anchor when evaluating vendor claims.

## Notable Quotes

> "When they sell you a $200 subscription, they're giving you $5,000 in compute."

> "What would it mean to replace a software engineer? It means that you don't need a human being to ever look at the code... you could trust it. That's what it means to replace a software engineer. And the models with 3 to 5 trillion parameters are nowhere near that happening."

> "Don't make AI an integral part of your workflow, because as soon as the price goes up, you're going to be screwed over. Use it right now. It's subsidized. Use it for learning. Use it to increase your own skills."
