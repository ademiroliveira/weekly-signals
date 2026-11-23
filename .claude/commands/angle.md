---
description: Propose article angles from the themes and signals archive. Adds them to articles/ideas.md.
argument-hint: "[optional: a theme slug or topic to focus on]"
---

Read `themes/`, the relevant `signals/` files and `articles/ideas.md` (don't repeat existing ideas). If $ARGUMENTS is given, focus on it.

Propose **3 angles**, each written for designers and product people, not cryptographers. For each:

```markdown
### <Working title — a claim, not a topic>
- **Theme:** `themes/<slug>.md` (or `none yet`)
- **Thesis:** one arguable sentence.
- **Why now:** what in the archive makes this timely.
- **Evidence:** 3+ signals from `signals/` (date · title · url). At least one must be a UX/interaction signal.
- **The design move:** the pattern, principle or decision a reader could apply on Monday.
- **Counterpoint:** the strongest objection, taken from the archive where possible.
- **Format:** essay | pattern breakdown | teardown | provocation · ~words
- **Fit:** Refined (taste/craft angle) | LinkedIn | talk
- **Readiness:** ready | needs 2–3 more weeks of signal
```

Rank them by readiness and strength of evidence. Append them to `articles/ideas.md` under today's date.

## Weekly mode

Used by step 9 of `/weekly-report`. It keeps `articles/ideas.md` current without flooding it.

1. **Update before adding.** For each existing idea, check whether this week's report or theme updates add evidence for it. If they do, add the new signals to its **Evidence** line (date · title · url), add a `**Theme:**` line if it's missing, and update **Readiness**. An idea is `ready` once it has 3+ cited signals from 2+ reports, including at least one UX/interaction signal. Edit the idea where it is, and add `(updated YYYY-MM-DD)` after its title.
2. **Add at most one new angle**, and only for a theme with `status: active`, or one seen in 3+ weeks, that no existing idea already covers. Use the format above, under a `## YYYY-MM-DD — weekly` heading.
3. **Change nothing else.** Don't reorder, rewrite or delete ideas, and don't draft.
4. Report back: ideas updated, any new angle, and any idea that became `ready`.
