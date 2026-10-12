# Researcher contract

Every research agent follows this file. Domain-specific search terms and sources are in each agent's own file. All rules come from `CLAUDE.md`.

## What you receive
- Today's date and the **report window** (start and end, inclusive).
- The **seen list**: URLs and titles already covered in earlier reports, from `python3 scripts/signals.py prior`.

## How to work
1. **Start with your entry points** in `reference/sources.md`, the dated listings that actually load. Skip anything marked *blocked*.
2. **Go wider with WebSearch**, using your search terms plus the month and year.
3. **Check each candidate:**
   - Fetch it.
   - Confirm the publication date is on the page and inside the window.
   - Check it against the seen list.
   - Pick the tag from the tag table in `CLAUDE.md`.
   - Set its stage and strength with the rubric.
   - Write the summary from the page only.
4. **Stay in your lane.** If you find something that belongs to another agent's domain, don't write it up. List it under **Hand-offs** with its URL, and synthesis will route it.
5. **Prefer first-party sources.** For an incident or product change, find the organisation's own statement before any coverage of it.
6. **Fewer, better items.** Return 0–4 items. `No new signals this week.` is a valid, complete answer.

## Self-check before you return
Drop any item that fails one of these. The verifier will kill it anyway, and every kill costs a fetch.
- [ ] Date visible on the page and inside the window
- [ ] URL is not in the seen list (or the item is a true Update with a new primary document)
- [ ] Tag copied verbatim from the tag table and fits the source type
- [ ] Journalism only from the four allowed outlets, and only after tiers 1–6 gave fewer than 2 items
- [ ] Every figure, name, version and date in the summary appears on the page
- [ ] No universal claims ("no wallet does X", "first ever") unless the source itself says so
- [ ] Strength follows the rubric for its stage and number of independent sources

## Return format

```
- title:
  stage: early | formal | in-force
  strength: 🟡 Weak | 🟠 Emerging | 🔴 Strong
  origin: academic | standards | regulatory | institutional | technical | journalism
  domains: [from the CLAUDE.md vocabulary]
  source_type: [exact tag]
  url:
  published: YYYY-MM-DD (as shown on the page)
  also: [other fetched URLs covering the same story]        # optional
  update_of: <id from the seen list>                         # only for an Update
  summary: 1–2 sentences, only what the source says
  filter: one sentence, WHO holds the keys or HOW sovereignty is exercised
```

Then:
- **Hand-offs:** URLs for other domains, one line each with the domain they belong to.
- **Source log:** one line per source tried: `source — ok / blocked (reason) / nothing in window — n candidates`. Note any source whose status differs from `reference/sources.md`.
