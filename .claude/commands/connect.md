---
description: Read across all weekly reports and update the running themes — recurring patterns, rising signals, tensions.
argument-hint: "[optional: number of weeks to look back, default all]"
---

Read every file in `signals/` (or the last $ARGUMENTS weeks) and every file in `themes/`. `python3 scripts/signals.py prior` lists every covered item and which `ux_pattern` slugs appeared in which reports. Older free-text patterns are already mapped through `reference/ux-patterns.md`. Each report's **Patterns across weeks** section is a starting point, not a substitute for reading the items.

Notes on older reports:
- `section: weak` means the radar section.
- Some weeks repeat an item from the previous week. Count a story once, at its first appearance, plus any genuine Update.

## Find
1. **Recurring threads:** topics, mechanisms or `ux_pattern` slugs that show up in 2+ reports. Name each thread by the *design question* underneath it, not the technology (e.g. "Who explains the delegation?" rather than "session keys").
2. **Strengthening signals:** things that started 🟡 and later came back as 🟠 or 🔴, or moved from academic → standards → shipped product.
3. **Tensions:** two verified signals that pull in opposite directions (e.g. custody concentrating in ETFs while self-custody tooling gets easier).
4. **Gaps:** things the cryptography or regulation layer is changing where no UX signal has appeared yet. These are opportunities to write first.

## Update `themes/`
One file per thread: `themes/<slug>.md`

```markdown
---
theme: <design question>
status: emerging | active | cooling
first_seen: YYYY-MM-DD
last_seen: YYYY-MM-DD
weeks: <n>
---
**Thesis so far:** 1–2 sentences, stated as a position.

## Evidence
- YYYY-MM-DD · 🟠 · <title> — why it belongs here. <url>

## Counter-evidence
- …

## Open question
What would confirm or kill this thesis next?
```

Update existing theme files rather than duplicating them. Mark a theme `cooling` if it's been absent for 4+ weeks.

## Report back
A short summary: new themes, themes that strengthened, and the single thread most ready to become an article.
