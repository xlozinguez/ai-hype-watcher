---
source_id: "091"
title: "Claude Code built me a $273/Day online directory"
creator: "Greg Isenberg"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=I_wbc5ND79o"
date: "2026-02-16"
duration: "55:41"
type: "video"
tags: ["vibe-coding", "claude-code", "ai-economics"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 091: Claude Code built me a $273/Day online directory

> **Creator**: Greg Isenberg | **Platform**: YouTube | **Date**: 2026-02-16 | **Duration**: 55:41

## Summary

Greg Isenberg interviews Frey Chu, a directory builder who demonstrates a seven-step process for building profitable online directories using Claude Code and the open-source Crawl4AI web crawler. The episode opens with three case studies of successful directories — Parting.com (funeral homes, $1M+/year revenue), APlaceForMom.com (senior living, estimated $50M/year from lead generation), and GasBuddy.com (gas prices, 1.1M monthly organic visitors monetized via a Mastercard debit card partnership). These examples establish the thesis that niche directories with strong data moats can become significant businesses.

The core of the episode walks through Frey's process of building a luxury restroom trailer directory in 4 days for under $250 ($100 Claude Code Max subscription, $100 for data via OutScraper, $50 for Claude API credits). The workflow starts with scraping 71,000 rows from Google Maps, using Claude Code for initial data cleaning (71K down to 20K by removing junk data), then deploying Crawl4AI to visit all 20,000 websites and identify actual luxury restroom trailer businesses (20K down to 725). Subsequent passes enrich the data with trailer inventory, images (validated via Claude Vision at $30 for 700 listings), amenities/features, and service areas — each pass requiring edge case discovery and re-runs.

The broader argument is that directories are a "distribution-first" business model that teaches three high-leverage skills simultaneously: AI coding (Claude Code), SEO, and lead generation. Frey is candid about limitations — SEO takes 6+ months to produce results, and this is not a get-rich-quick play. The discussion addresses the LLM threat to directories, arguing that niche local directories survive because users in the decision-making phase (not discovery phase) need to compare options for high-consequence purchases where the risk of a bad choice is too high to trust a single LLM response.

## Key Concepts

### Data Enrichment as the Directory Moat

The central insight is that the competitive advantage in directories is not the website itself but the quality and depth of enriched data. Frey's process involves multiple sequential enrichment passes — business verification, inventory cataloging, image scraping and validation via Claude Vision, amenity/feature extraction, and service area mapping. Each pass requires prompt iteration and edge case handling (e.g., businesses in Florida showing service areas in Arizona, images returning logos instead of product photos). The total process saved an estimated 2,000+ hours of manual work. This pattern generalizes: the harder the data is to collect and clean, the stronger the moat.

### Claude Code as Non-Technical Builder's Tool

Frey explicitly identifies as non-technical with only 6 months of AI coding experience. His workflow is conversational — writing prompts in plain language, asking Claude Code for a "game plan" before burning tokens, and iterating based on results. He combines Claude Code (the "brain") with Crawl4AI (the "engine") for automated website analysis at scale. This demonstrates Claude Code's accessibility for business-oriented users who need to process data rather than build traditional software.

### The Price Transparency Opportunity

Across all three case study directories, the common thread is bringing price transparency to industries where pricing information is difficult to obtain — funeral homes, senior living, gas stations. Frey argues this pattern extends to numerous "boring but important" niches: ADA-accessible bathroom contractors, dementia-specific senior living, tap water quality. The combination of Crawl4AI for automated website scraping and Claude Code for data classification makes it newly feasible to build these hyper-niche directories that would have been prohibitively expensive to research manually.

### Directory Survival in the LLM Search Era

The discussion addresses the existential question of whether LLM-based search will kill directories. Frey's argument has two parts: (1) directories serve users in the decision-making phase, not the discovery phase — for high-consequence decisions (legal, health, finance, senior living), people will not trust a single LLM response and need to compare options; (2) local SEO has not fundamentally changed, and niche directories may actually benefit from AI search because LLMs will surface fewer results (3 links vs. Google's "1,000 little blue links"), making being the definitive niche source more valuable. Isenberg adds that horizontal directories get hurt while vertical niche directories become the referenced source.

## Practical Takeaways

- **Start with data, not design**: The directory's value comes from enriched, verified data. Frey's crappy WordPress directory with Lorem Ipsum on the homepage still generated leads including a $20,000+ order from the New Mexico State Fair
- **Use sequential enrichment passes**: Do not try to extract all data points in one crawl. Run separate passes for business verification, inventory, images, amenities, and service areas — each with its own prompt and edge case handling
- **Validate AI-scraped images with Claude Vision**: A $30 pass through the Claude API to visually verify scraped images eliminates logos, favicons, and low-quality results that text-based scraping misses
- **Target niches where price transparency is the moat**: Industries where pricing is opaque and consequences of bad choices are high (legal, health, events, specialized contractors) are natural directory opportunities
- **Expect 6+ months for SEO traction**: Directories are not quick-return businesses. Treat the first build as a learning playground for Claude Code and SEO skills, with revenue as a longer-term outcome

## Notable Quotes

> "I built this in 4 days. I probably saved over 2,000 hours in what would have been manual data cleaning, manual data enrichment." — Frey Chu

> "I built this thinking like no one could reasonably trust this directory... But to my surprise, I got leads coming in. I got a lead from the New Mexico State Fair. This is like $20,000 plus of porta potty/luxury restroom trailers that they wanted." — Frey Chu

> "If someone's browsing a directory in 2026, they're past the discovery phase... By the time someone's on a directory, they're in the decision-making phase." — Frey Chu

## Related Sources

- [075: Stop Shipping AI Slop](075-greg-isenberg-ai-slop-design.md) — Same creator's earlier episode on design quality in AI-built products, relevant to directory aesthetics
- [072: Build ANYTHING: Google Antigravity + Convex + Clerk](072-income-stream-surfers-antigravity-convex.md) — Another vibe-coding business-building approach for comparison
- [042: Vibe Coding is a Trap](042-devforge-vibe-coding-trap.md) — Counterpoint on the limitations of non-technical AI-assisted development
- [065: SaaS-pocalypse](065-griffonomics-saaspocalypse.md) — The broader economic context for AI-built micro-businesses competing with traditional SaaS

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Iterative prompt design for data enrichment, sequential pass methodology
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — AI-driven business economics, the data moat concept, and cost analysis of AI-built products
