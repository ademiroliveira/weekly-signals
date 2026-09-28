---
description: Draft an article from an angle in articles/ideas.md, in AO's voice, citing only the signals archive.
argument-hint: "<angle title or number from articles/ideas.md>"
---

Draft the article for: $ARGUMENTS

1. Load the angle from `articles/ideas.md`, its theme file and every signal it cites.
2. Follow the **Writing layer** section of `CLAUDE.md` (voice, rules, no Porto or employer details in public drafts).
3. Structure:
   - **Opening:** a concrete moment in the interface (a screen, a decision, a prompt), not a trend statement.
   - **The shift:** what changed underneath, explained in plain language, with its source.
   - **Why it's a design problem:** what users now have to understand, decide or delegate.
   - **The move:** the pattern or principle, with a real example from the archive.
   - **Counterpoint:** taken seriously.
   - **Close:** the question practitioners should carry forward.
4. Link every factual claim inline to its source URL. Mark anything not in the archive `[needs source]`.
5. Keep the report's confidence levels: a 🟡 preprint is "early research", not a fact.

Save to `articles/drafts/<YYYY-MM-DD>-<slug>.md` with frontmatter (`title`, `thesis`, `theme`, `signals: [ids]`, `status: draft`). Then list the 3 weakest points of the draft for AO to review.
