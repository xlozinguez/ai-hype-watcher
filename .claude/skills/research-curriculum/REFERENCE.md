# Research Curriculum — Reference Material

## Concept Classification Thresholds

| Classification | Strength Score | Meaning | Review Priority |
|---------------|---------------|---------|-----------------|
| evergreen | >= 5.0 | Well-supported, multi-creator, enduring | Low (spot-check) |
| established | 2.0 - 5.0 | Solid support, may benefit from refresh | Medium |
| emerging | 1.0 - 2.0 | Few sources, watch for reinforcement | High |
| stale | < 1.0 | Low support + old sources | Critical |

## Strength Formula

```
strength = support_count * decay_factor * diversity_bonus
```

- **support_count**: Distinct sources matching concept keywords within the module
- **decay_factor**: 1.0 (< 3mo), 0.85 (3-6mo), 0.7 (6-12mo), 0.5 (12+mo)
- **diversity_bonus**: 1.0 + 0.1*(unique_creators - 1), capped at 1.5

## Eval Criteria (Binary Yes/No)

For each concept being validated:

1. **Citation accuracy**: Are all `[#NNN]` references valid source IDs that exist in `sources/`?
2. **Claim fidelity**: Does the curriculum text accurately represent what the cited source says?
3. **Currency**: Has the concept been superseded or significantly evolved since the latest supporting source?
4. **Contradiction-free**: Does any source in the module directly contradict this concept?
5. **External consistency**: Do authoritative external sources confirm the concept's current framing?
6. **Completeness**: Are important related sources missing from the concept's citations?

## Module Scope Boundaries

| Module | Scope | NOT in scope |
|--------|-------|-------------|
| 01 Foundations | AI landscape, capability levels, hype vs reality, model releases | Tool-specific workflows |
| 02 Prompting | Prompt engineering, context engineering, spec-first, workflows | Agent orchestration |
| 03 Claude Code | Setup, CLAUDE.md, skills, context discipline, computer use | Multi-agent coordination |
| 04 Agentic | Agent patterns, builder/validator, hooks, evals, memory | Team-level orchestration |
| 05 Teams | Multi-agent, team composition, coordination, observability | Individual agent design |
| 06 Strategy | Economics, infrastructure, security, adoption, career, bubble | Technical implementation |

## External Validation Sources (Trusted)

When searching externally, prioritize:
- **Official docs**: docs.anthropic.com, platform.openai.com, docs.github.com
- **Respected practitioners**: simonwillison.net, martinfowler.com, karpathy.ai
- **Industry analysis**: SemiAnalysis, Stratechery, a16z research
- **Academic**: arxiv.org (for foundational claims)

Avoid: social media hot takes, SEO content farms, "top 10" listicles

## Research Report Location

Reports go to `research/YYYY-MM-DD-module-NN-section.md`

Example: `research/2026-04-05-module-04-core-concepts.md`
