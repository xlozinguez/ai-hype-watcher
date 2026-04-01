---
source_id: "432"
title: "One Prompt Change That Forces Claude to Be Honest"
creator: "Dylan Davis"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=v-3iRJ_lMLY"
date: "2026-03-28"
duration: "10:14"
type: "video"
tags: ["prompt-engineering", "validation", "meta-prompts"]
curriculum_modules: ["02-prompting-and-workflows"]
---

# 432: One Prompt Change That Forces Claude to Be Honest

> **Creator**: Dylan Davis | **Platform**: YouTube | **Date**: 2026-03-28 | **Duration**: 10:14

# One Prompt Change That Forces Claude to Be Honest

## Summary

Dylan Davis addresses a structural problem with increasingly capable AI models: as intelligence increases, models become *more* confident and *less* likely to admit uncertainty, creating what he calls an "honesty gap." This is compounded by automation bias on the user side—the more confident AI sounds, the less humans verify its outputs, allowing errors to compound silently. The video presents three prompt engineering rules specifically designed for information-extraction tasks (contracts, invoices, meeting notes, CRM data) that force the model to surface uncertainty rather than fill gaps with plausible-sounding guesses.

The three rules work as a layered defense system. Rule one grounds the AI to the source document and instructs it to leave fields blank—with a written explanation—whenever a value is ambiguous, missing, or unclear. Rule two shifts the incentive structure by explicitly telling the AI that a wrong answer is three times worse than a blank answer. Rule three adds a "source" column requiring the AI to label each extracted value as either "extracted" (verbatim from document) or "inferred" (derived from context), with an evidence note explaining the inference. Together, these rules reduce the reviewer's burden to spot-checking blanks and inferred values rather than validating every field.

The practical value here is that these prompts are short, composable, and transferable across platforms (Claude, ChatGPT, Gemini). They implement a lightweight version of grounding and auditability that is typically associated with more complex RAG or structured output pipelines, but using only natural-language prompt instructions accessible to non-developers.

## Key Concepts

### The Honesty Gap
As model generations advance, intelligence scales faster than honesty. More capable models are better at generating plausible-sounding answers, which means they are more likely to confabulate rather than admit ignorance. This phenomenon is documented in recent OpenAI research referenced in the video. The practical implication: the default behavior of a smarter model during extraction tasks is to infer and fill rather than flag gaps.

### Automation Bias Feedback Loop
The second problem is user-side: increased model confidence leads users to check outputs less rigorously, which allows compounding errors to go undetected. This creates a self-reinforcing loop where trust grows ahead of verified accuracy—a critical risk in high-stakes extraction workflows like contract review or compliance checking.

### Grounding via Prompt Instruction
"Grounding" here means constraining the AI to extract only values explicitly stated in the source document, not inferred from training data or contextual interpolation. The prompt technique is a direct instruction: *"Only extract values explicitly stated in this document."* This is a simpler, prompt-only analog to retrieval-grounding in RAG systems, and serves as the foundation for the other two rules.

### Incentive Re-weighting
AI models implicitly treat a wrong answer and a blank answer as equivalent—both are "filling the field." By explicitly stating that a wrong answer is 3× more costly than leaving a field blank, the prompt reframes the model's optimization target. The analogy to managing a new employee is useful: telling someone that wrong answers cost the team more than honest "I don't know" responses changes their default behavior.

### Extraction vs. Inference Labeling
Rather than trusting the model to always follow grounding instructions (especially on long, complex tasks), rule three adds a structural audit trail. Each extracted value is tagged as `extracted` or `inferred`, with an `evidence` column. This doesn't prevent inference—it makes inference visible and reviewable, so the human can quickly triage only the flagged fields.

## Practical Takeaways

- **Use blank-with-reason instead of confidence scores**: Asking for a confidence score still lets the model fabricate a plausible number. Forcing a blank field with a mandatory explanation is a harder constraint and produces more actionable output.
- **Add a single incentive line to extraction prompts**: `"A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank."` is low-cost to add and meaningfully shifts model behavior on ambiguous fields.
- **Always include a source column on extraction tasks**: Requiring the model to label each value as `extracted` or `inferred` creates a built-in audit trail that reduces full-output review to spot-checking inferred fields only.
- **Expect grounding instructions to degrade on long/complex tasks**: Models will drift toward inference even when instructed not to. The source column functions as a compensating safety net for this predictable failure mode.
- **Target the review workload, not perfect accuracy**: The goal of these rules isn't to eliminate AI errors—it's to concentrate them in clearly flagged locations (blanks + inferred) so human review time is minimized and focused.

## Notable Quotes

> "The smarter these models get, the more confidently they guess instead of admitting that they don't know."

> "We don't want to leave that up to AI. We want to remove that responsibility from them and have them just give us evidence."

> "Instead of looking at everything, I'm just looking at the inferred fields."
