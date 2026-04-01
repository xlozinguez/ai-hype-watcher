---
source_id: "429"
title: "The End of JS"
creator: "The PrimeTime"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=ceH0IT-OBCw"
date: "2026-03-31"
duration: "9:38"
type: "video"
tags: ["ai-landscape", "ai-hype", "capability-overhang"]
curriculum_modules: ["01-foundations"]
---

# 429: The End of JS

> **Creator**: The PrimeTime | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 9:38

## Summary

Prime reviews Gary Bernhardt's legendary 2014 conference talk "The Birth and Death of JavaScript," which made 20-year predictions about web technology — predictions that are now arriving at their pivotal moment in 2026. The talk's central thesis was that asm.js (a typed subset of JavaScript designed to function as assembly for the web) would ultimately kill JavaScript by making it possible to compile any language down to something runnable in the browser, eliminating the need to write JavaScript directly.

Prime evaluates how well those predictions aged. The core technology prediction — asm.js enabling thick, large applications to port to browser-native execution — largely materialized through WebAssembly (Wasm), asm.js's direct successor. Wasm 3.0 now includes garbage collection, better exception handling, and JavaScript string built-ins, making it increasingly viable. Real-world adoption exists: Cloudflare Workers supports Rust, C++, Go, and Python via Wasm compilation; Figma is a notable example. The prediction is directionally correct, if not dramatically realized.

The wildcard Bernhardt couldn't have anticipated was AI. His timeline assumed developer frustration with JavaScript would drive mass migration to asm.js/Wasm, but AI-assisted code generation has instead allowed developers to tolerate JavaScript's pain points far longer — and produce far more JavaScript than ever before. The final "metal" prediction — a JavaScript VM embedded in the kernel, with Wasm as the universal execution format for all software — remains speculative but is no longer entirely dismissible given Wasm's growing footprint in edge computing and server-side runtimes.

## Key Concepts

### asm.js as Proto-WebAssembly
Asm.js was a strict, typed subset of JavaScript designed to be optimizable by JIT compilers into near-native machine code. Every operation required explicit type coercion (e.g., `x = +x` to enforce numeric type), allowing engines like Firefox's to recognize numeric operations and emit direct CPU instructions. It was the conceptual predecessor to WebAssembly, which formalized the same idea with a proper binary format and cross-browser standard.

### The "JavaScript Kills JavaScript" Thesis
Bernhardt's central prediction was that asm.js would render JavaScript itself obsolete — not by replacing it externally, but by making JavaScript a compilation *target* rather than a language developers write. Any C/C++ codebase could compile to asm.js and run in the browser at near-native speed, as demonstrated by the Unreal Engine 3 running in Firefox circa 2013. The irony is that JavaScript's survival mechanism becomes its own displacement.

### WebAssembly 3.0 and Edge Runtime Adoption
Wasm has matured significantly beyond its asm.js origins. Wasm 3.0 adds garbage collection, improved exception handling, JavaScript string built-ins, and deterministic profiling. Cloudflare Workers now allows deployment of Rust, C++, Go, and Python workloads compiled to Wasm, making polyglot server-edge development practical. This represents the first meaningful mainstream adoption of the "compile anything, run anywhere in the browser/edge" vision.

### AI as the Unforeseen Variable
Bernhardt's timeline assumed developer pain with JavaScript would accelerate migration to alternative-language-compiled-to-Wasm workflows. AI code generation disrupted this by dramatically reducing the friction of writing JavaScript — producing more of it than ever while simultaneously lowering the motivation to switch paradigms. AI didn't kill JavaScript; it arguably extended its dominance by making its worst parts more tolerable.

### The "Metal" Prediction: Wasm as Universal OS Primitive
Bernhardt's most ambitious (and still-speculative) prediction is "metal" — eliminating the ring 0/ring 3 OS boundary overhead by embedding a JavaScript/Wasm VM in the kernel itself, using VM isolation instead of process isolation. Every program would compile to Wasm. While not realized, the prediction rhymes with current trends: Wasm is appearing in serverless edge runtimes, IoT, and plugin sandboxing systems in ways that suggest a slow drift toward Wasm-as-universal-execution-layer.

## Practical Takeaways

- **Wasm is now worth re-evaluating for production use.** Wasm 3.0's additions (GC, exception handling, string built-ins) address the major friction points that made earlier versions frustrating. If you dismissed it previously, the calculus may have changed.
- **Cloudflare Workers + Wasm is a real polyglot edge stack.** Rust, C++, Go, and Python can all compile to Wasm and deploy as Workers today — this is no longer theoretical and is worth considering for performance-critical or language-diverse teams.
- **AI extended JavaScript's runway, but didn't change the architectural direction.** Wasm's long-term trajectory toward becoming a universal compilation target is intact; AI just slowed the timeline by making JavaScript more tolerable to write.
- **The "compile anything to the browser" vision is largely proven.** Figma's use of Wasm for performance-critical rendering, and game engines running in-browser, validate the core technical thesis even if the mass-migration narrative hasn't materialized.
- **Watch the Bernhardt talk.** "The Birth and Death of JavaScript" (Destroy All Software, 2014) is considered one of the best tech conference talks ever made and provides useful mental models for thinking about long-arc technology predictions.

## Notable Quotes

> "JavaScript will kill JavaScript via asm.js."
— Prime paraphrasing Gary Bernhardt's central thesis

> "AI didn't include this idea of generating code. So he thought people would just get so frustrated with JavaScript that everybody would just want to use asm.js. And he's not completely wrong."

> "Every program you compile, it's asm. Every dream you ever had, asm."
— Gary Bernhardt (as quoted/performed by Prime)
