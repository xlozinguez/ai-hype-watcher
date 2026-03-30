---
source_id: "413"
title: "AI isn't reading the code"
creator: "ThePrimeagenHighlights"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=iOAtFxP9Pg4"
date: "2026-03-29"
duration: "7:01"
type: "video"
tags: ["ai-hype", "context-engineering", "security", "vibe-coding"]
curriculum_modules: ["01-foundations", "02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 413: AI isn't reading the code

> **Creator**: ThePrimeagenHighlights | **Platform**: YouTube | **Date**: 2026-03-29 | **Duration**: 7:01

# AI isn't reading the code

## Summary

ThePrimeagen reacts with sardonic humor to two research findings making the rounds: one showing that frontier LLMs score 80–95% on standard coding benchmarks but collapse to 0–11% when given equivalent problems in esoteric languages like Brainfuck and Whitespace, and a second showing that superficial code changes—renaming a variable, adding a comment, inserting dead code—dramatically degrade LLM bug-detection accuracy. His core point is that both findings should be obvious to anyone who understands how LLMs work: they learn by pattern-matching on massive repetition, so they perform poorly on data they haven't seen and are confused by surface-level noise that doesn't affect program logic.

The second paper's findings are more practically relevant. Renaming a variable caused models to fail to find a previously identified bug 78% of the time. Adding unreachable dead code dropped bug detection accuracy to around 20%, with models treating dead code as live and flagging it as the bug source. There's also a strong positional bias: 56% of correctly found bugs were in the first quarter of a file, while only 6% were in the last quarter—suggesting models pay significantly less attention to code deeper in context.

Primeagen uses this as a practical nudge toward better agentic coding hygiene: keep files small, don't let AI agents grow files indefinitely, and recognize that the model's apparent "understanding" of code is more pattern-recognition than logical reasoning. The video is primarily commentary and reaction, light on solutions but useful as a grounding corrective to inflated expectations about LLM code comprehension.

---

## Key Concepts

### Benchmark Performance vs. Novel Problem Solving
LLMs achieve high scores on standard coding benchmarks (80–95%) because those benchmarks draw from the same distribution of code they trained on. When researchers reformulated equivalent problems in languages like Brainfuck or Whitespace that have minimal training data, scores dropped to 0–11%. This confirms that benchmark performance reflects memorization and pattern-matching, not generalizable reasoning ability.

### Surface-Level Code Changes Break Bug Detection
A renamed variable or an added comment—changes with zero semantic effect—caused models to miss a previously identified bug 78% of the time. This reveals that LLMs are sensitive to superficial token patterns rather than tracking the logical structure of code. The model "found" the bug before because the surrounding tokens matched a known pattern, not because it understood the bug's cause.

### Dead Code as a Confounding Signal
Adding code that never executes reduced bug-detection accuracy to ~20%. Models treated unreachable code as live and sometimes identified it as the bug source. This has a security-relevant implication Primeagen notes in passing: dead code could be used as a deliberate prompt injection or distraction vector against AI-assisted code review.

### Positional Attention Bias in Code Files
56% of bugs correctly identified by models were in the first quarter of the file; only 6% were in the last quarter. Models appear to attend more strongly to early context and degrade in attention as file length increases. This is a practical argument for keeping files short and placing the most logic-dense or bug-prone code early.

### Pattern Matching vs. Logical Execution Modeling
The throughline across both papers is that LLMs read code top-to-bottom as a token sequence, not as a logical execution graph. They cannot reliably distinguish code that runs from code that never runs, and they are misled by irrelevant surface changes. This is a fundamental limitation of current transformer-based approaches to code understanding.

---

## Practical Takeaways

- **Keep files small.** Positional bias means bugs in the bottom half of a file are significantly less likely to be found. Refactoring long files into smaller, focused modules improves AI-assisted review reliability.
- **Don't trust LLM bug-finding on refactored code without re-running the check.** A rename or comment change is enough to invalidate a prior finding—re-verify after any non-trivial edit.
- **Be skeptical of benchmark numbers as capability proxies.** 80–95% on standard benchmarks tells you the model has seen similar code before; it says little about reasoning on novel codebases.
- **Be aware of dead code as a noise vector.** Whether accidental or adversarial, unreachable code can misdirect AI code review. Prune dead code before asking an LLM to audit a file.
- **Limit autonomous agent file growth.** Primeagen's personal note about letting agents expand files unchecked maps directly to the positional bias finding—larger files mean less reliable attention on later content.

---

## Notable Quotes

> "LLMs who learn by seeing the same amount of data, but a cajillion amount of times when not seeing data a cajillion amount of times, in fact, did not memorize it as well as the language they saw millions upon millions of times."

> "Models are read top to bottom, not logically. 56% of correctly found bugs were in the first quarter of the file. Only 6% were in the last quarter."

> "You could probably add in little traps in your codebase with dead code and it would probably read it and you could probably do some good prompt injections in there."

---
