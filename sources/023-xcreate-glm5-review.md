---
source_id: "023"
title: "Let's Run GLM-5 - SUPER LARGE Local AI \"Coding King\" REVIEW"
creator: "xCreate"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=3XCYruBYr-0"
date: "2026-02-12"
duration: "20:17"
type: "video"
tags: ["ai-landscape", "infrastructure"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 023: Let's Run GLM-5 - SUPER LARGE Local AI "Coding King" REVIEW

> **Creator**: xCreate | **Platform**: YouTube | **Date**: 2026-02-12 | **Duration**: 20:17

## Summary

xCreate reviews GLM-5, the latest 744B parameter open-source model from ZhipuAI, deployed on a Mac Studio with 512GB RAM. The model represents a significant evolution from GLM 4.7 (355B parameters), now featuring 40B active parameters trained on 28.5 trillion tokens. Through extensive hands-on testing of various quantization strategies (4-bit, 6-bit, 9-bit, and 16-bit mixes), the video demonstrates GLM-5's practical performance in coding challenges, logic tests, tool calling, and batch inference scenarios.

The review focuses on the engineering tradeoffs of running frontier-scale models locally, showcasing multi-head latent attention (MLA) for dramatic memory reduction (33x improvement over traditional multi-head attention), and exploring batching capabilities that enable multiple concurrent inferences on consumer hardware. The model scores 73.3 on SWE-bench, beating DeepSeek (70.0) and approaching Claude's 75.0, while maintaining an MIT license that allows unrestricted commercial use.

## Key Concepts

### Multi-Head Latent Attention (MLA) for Memory Efficiency
Multi-head latent attention represents a significant architectural improvement over traditional multi-head attention (MHA), reducing context memory usage by 33x ([0:39](https://www.youtube.com/watch?v=3XCYruBYr-0&t=39)). In a direct comparison, the same 3D demo prompt consumed over 10GB with MHA but only 0.3GB with MLA ([3:50](https://www.youtube.com/watch?v=3XCYruBYr-0&t=230)). This efficiency enables much larger context windows on fixed hardware and makes batching viable for local deployments.

### Quantization Strategy Exploration
The video documents a methodical exploration of quantization approaches to fit the 744B parameter model into 512GB RAM ([1:52](https://www.youtube.com/watch?v=3XCYruBYr-0&t=112)). Starting with a 4/6-bit mix using 400GB, xCreate progressively experimented with 4/6/9-bit and 4/6/16-bit combinations before settling on a "469" configuration ([3:31](https://www.youtube.com/watch?v=3XCYruBYr-0&t=211)) that balanced quality and memory footprint at approximately 418GB peak usage ([5:34](https://www.youtube.com/watch?v=3XCYruBYr-0&t=334)). This leaves nearly 100GB available for context window operations.

### Sparse Attention and Mixture-of-Experts Architecture
GLM-5 integrates DeepSeek's sparse attention mechanism for extended context handling ([0:39](https://www.youtube.com/watch?v=3XCYruBYr-0&t=39)) and uses a mixture-of-experts design with 40B active parameters out of 744B total. The video demonstrates that increasing the number of active experts can improve performance on difficult reasoning tasks ([11:27](https://www.youtube.com/watch?v=3XCYruBYr-0&t=687)), though this requires manual configuration rather than automatic scaling.

### Batching for Local Inference at Scale
With MLA reducing memory overhead, batching becomes practical for local deployments. The video shows 2 concurrent prompts running at 12.7 tokens/second each (25+ combined), with the potential to serve 6 simultaneous requests exceeding 30 tokens/second aggregate throughput ([6:32](https://www.youtube.com/watch?v=3XCYruBYr-0&t=392)). This positions local hardware as viable for family or small business multi-user scenarios.

## Practical Takeaways

- **Quantization Requires Experimentation**: Optimal performance came from a mixed 4/6/9-bit quantization scheme rather than uniform precision across all layers. Visual test outputs (3D demos) provided quick feedback on quality degradation.

- **MLA Dramatically Changes Memory Dynamics**: The 33x reduction in context memory means that batch inference and large context windows become feasible on consumer hardware, fundamentally changing what's possible with local AI deployment.

- **Expert Count is Tunable**: While thinking mode (extended reasoning) helps with complex problems, manually increasing the number of active experts can push the model to solve difficult riddles that it fails with default settings.

- **Performance at 16.5 tokens/second**: Despite being nearly double the parameters of GLM 4.7, the quantized GLM-5 runs at comparable or faster speeds (16-18 tokens/second) due to architectural improvements and optimized quantization.

- **Tool Calling Works Reliably**: GLM-5 demonstrated multi-step tool use, correctly chaining multiple API calls to traverse paginated Wikipedia content and extract specific information, a critical capability for agentic applications.

- **MIT License Removes Deployment Friction**: Unlike models requiring attribution or commercial licensing, GLM-5's MIT license allows unrestricted use, eliminating legal overhead for business deployment.

## Notable Quotes

> "They used to do 32 billion active parameters. Now they've gone to 40 billion active parameters. They used to train on 23 trillion tokens. Now they've gone up to 28.5." — xCreate ([0:00](https://www.youtube.com/watch?v=3XCYruBYr-0&t=0))

> "Using MHA the multi head attention and the context of this took over 10 gigabytes of memory. But then using MLA, which is multi head latent attention, this one only uses 0.3 GB." — xCreate ([3:50](https://www.youtube.com/watch?v=3XCYruBYr-0&t=230))

> "If you got sixes at the same time, you get over 30 tokens a second. So that is if you got like a family computer or a business when lots of people are just hammering your server, you can get multiple inferences going all at the same time with this model." — xCreate ([6:32](https://www.youtube.com/watch?v=3XCYruBYr-0&t=392))

> "And one thing you just got to respect these guys for — this is MIT license. This is a very open license. You can just grab the weights and do what you want with them. Some models they require you to state attribution, but these guys just say, 'Hey, just take it. MIT.'" — xCreate ([19:44](https://www.youtube.com/watch?v=3XCYruBYr-0&t=1184))

## Related Sources

- **003**: PrimeTime - Opus 4.6 and ChatGPT 5.3 (benchmark comparisons with frontier models)
- **019**: Matt Shumer - Something Big (context on frontier model development trends)

## Related Curriculum

- **01-foundations**: Model architectures (MLA vs MHA), quantization techniques, mixture-of-experts
- **06-strategy-and-economics**: Open-source licensing models, economics of local vs cloud inference, deployment tradeoffs
