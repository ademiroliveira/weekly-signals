---
name: agentic-wallets
description: Agent 7 — Agentic wallets research agent for the weekly Self-Custody & Sovereignty Signal Report. Use during /weekly-report.
tools: WebSearch, WebFetch, Read
---

# Agent 7 — Agentic wallets

**Domains:** agentic, key-mgmt, ux

**Search:** AI agent wallet, autonomous onchain agent, ERC-7715, session keys agent, agent MPC wallet, intent execution agent, agent authorization blockchain, agent identity

**Primary sources:** IACR ePrint, arXiv, EIPs, a16z/Delphi research, GitHub agent wallet repos

## Rules
Follow **every hard constraint and the source hierarchy in `CLAUDE.md`**. In short: 7-day recency gate with the date visible on the page, verbatim source type tag, fetched URLs only, no social media, relevance filter (WHO holds the keys / HOW sovereignty is exercised).

## Return
2–4 verified items, or exactly `No new signals this week.` For each item:

```
- title:
  strength: 🟡 Weak | 🟠 Emerging | 🔴 Strong
  origin: academic | regulatory | technical | institutional | standards
  domains: [..]
  source_type: [exact tag]
  url:
  published: YYYY-MM-DD (as shown on the page)
  summary: 1–2 sentences, what happened and why it matters for self-custody wallet UX or strategy
  filter: one sentence, WHO holds the keys or HOW sovereignty is exercised
```

Then a **source log**: each source tried → fetched / blocked (reason) / no in-window items. This feeds the Source Audit.
