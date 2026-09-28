# Weekly Signals

This repo holds AO's weekly **Self-Custody & Sovereignty Signal Report** and turns its history into articles about UX and product design.

AO is Director of Product Experience Design at a large financial services firm and leads self-custody wallet design (Porto), agentic wallet UX and emerging Web3 product strategy.

It has two layers:

1. **Signals.** Every Monday, 8 research agents and 2 verification agents produce a report, which is saved to `signals/YYYY-MM-DD.md` (never overwritten) and mirrored to the live artifact.
2. **Writing.** `/connect`, `/angle` and `/draft` read across all past reports to find themes and write articles.

## Repo map

| Path | What |
|---|---|
| `signals/YYYY-MM-DD.md` | One report per week, named by run date. Append-only. |
| `themes/*.md` | Running threads that recur across weeks, maintained by `/connect` |
| `articles/ideas.md` | Article angle backlog from `/angle` |
| `articles/drafts/`, `articles/published/` | Drafts in progress and final versions |
| `reference/report-style.md` | Visual spec for the HTML artifact |
| `.claude/agents/` | The 8 domain researchers and the verifier |
| `.claude/commands/` | `/weekly-report`, `/connect`, `/angle`, `/draft` |

---

## Hard constraints: apply before including ANY signal

1. **Recency gate.** Only include items published in the past 7 days (cutoff = today minus 7 days). If no publication date is visible, exclude it. If the date is outside the window, exclude it. Never backfill with older material. **Never estimate, extrapolate or infer a publication date.** Sequential IDs (IACR ePrint numbers, arXiv IDs, PR numbers) are not evidence of a date. If a source is rate-limited or blocked by robots.txt, exclude the item (don't estimate it, and don't include it with a caveat) and note the blocked source in the Source Audit.
2. **No new signals = say so.** If a domain yields nothing in the window, write "No new signals this week." Never pad.
3. **A signal strength rating is required:** 🟡 Weak (niche/early, single source, preprint) | 🟠 Emerging (2+ independent sources, or funded/institutional backing) | 🔴 Strong (peer-reviewed, regulatory/legal, mainstream adoption, or multiple strong independent sources).
4. **A source type tag is required**, copied verbatim from this list: [IACR paper] [arXiv paper] [Usable security paper] [EIP] [W3C spec] [NIST pub] [BIS paper] [FSB report] [FATF guidance] [Regulatory filing] [Institutional report] [Audit] [Vendor security report] [GitHub release] [Protocol blog] [Verified journalism]. An invented or hybrid tag means the item is excluded.
5. **No social media** as a primary source (X/Twitter, Reddit, Farcaster, Nostr, LinkedIn). Developer mailing lists (bitcoin-dev, ethereum-magicians) are allowed.
6. **Verify URLs.** Only include URLs that were actually fetched and confirmed to exist. Never guess a URL.
7. **Relevance filter.** Does this change WHO holds the keys or HOW sovereignty is exercised? If not, exclude it. (The wallet UX agent uses its own experience filter instead.)

## Source hierarchy: search in this order for each domain

1. **Academic & cryptography**: IACR ePrint (`https://eprint.iacr.org/search?q=TOPIC`), arXiv cs.CR / cs.DC (`https://arxiv.org/search/?searchtype=all&query=TOPIC`), SSRN, IEEE Xplore, ACM, NBER, MIT DCI (`https://dci.mit.edu`), Stanford CBR (`https://cbr.stanford.edu`)
2. **Standards & protocol specs**: EIPs (`https://eips.ethereum.org`), W3C (`https://www.w3.org/TR/`), NIST (`https://csrc.nist.gov/publications`), BIS (`https://www.bis.org/publ/work.htm`), FSB (`https://www.fsb.org/publications/`), FATF (`https://www.fatf-gafi.org/en/publications.html`)
3. **Regulatory**: SEC (`https://www.sec.gov/news/`), ESMA, FinCEN, IRS, national treasury and central bank publications, congress.gov
4. **Institutional & industry research**: a16z crypto (`https://a16zcrypto.com/posts/`), Messari (`https://messari.io/research`), Galaxy Research (`https://www.galaxy.com/insights/research/`), Chainalysis (`https://www.chainalysis.com/blog/`), Delphi Digital, Coinbase Institutional, World Economic Forum
5. **Security & audit firms**: Trail of Bits (`https://blog.trailofbits.com/`), OpenZeppelin (`https://blog.openzeppelin.com/`), Zellic (`https://www.zellic.io/blog/`), Halborn (`https://halborn.com/blog/`); vendor threat-research units (HP Wolf, Mandiant, Kaspersky) are tagged [Vendor security report]
6. **Protocol teams & GitHub**: `https://github.com/ethereum/EIPs/pulls?q=is:merged`, official repos for Safe, MetaMask, Argent, Phantom, Ledger, Coinbase Wallet (releases pages), Bitcoin Optech (`https://bitcoinops.org/en/newsletters/`), bitcoin-dev mailing list
7. **Quality journalism** (fallback only, if tiers 1–6 yield fewer than 2 items for a domain, and you must say so): The Block Research, Bitcoin Magazine (analysis pieces only), Bitcoin Foundation research, Unchained. No other outlet qualifies: not CryptoSlate, CryptoTicker, Cointelegraph, Decrypt or CoinDesk. The publication date must be explicit and inside the window.

## Signal strength during synthesis

- 🔴 **Strong**: peer-reviewed paper, enacted regulation, funded product with multiple confirming sources, or a coordinated institutional move
- 🟠 **Emerging**: 2+ independent verified sources, or a single institutional/audit source with clear momentum
- 🟡 **Weak**: single source, early preprint, grant-stage project, or early regulatory proposal

---

## Writing layer

### Why the archive matters
One week is news. A pattern across weeks is a thesis. Articles should be built from **recurrence and tension across reports**, not from a single item.

### AO's article voice
- A design leader writing for designers and product people, not for cryptographers. Explain the mechanism in one sentence, then move on to what it means for the person using the product.
- Take a position. Every piece has a thesis you could disagree with.
- Get to the interface: what the user sees, understands, decides or delegates. A signal only matters for the article when it changes the experience.
- Use concrete references (a named release, paper or spec from the archive) rather than generic claims. Every factual claim links to its source URL in `signals/`.
- Show taste: restraint, precision, no hype. Include the strongest counterargument.
- Short paragraphs. No listicle filler. No emoji in articles.

### Rules for writing
- Cite only what exists in `signals/`. Never add facts from outside the archive without flagging them as `[needs source]`.
- Keep the report's signal strength honest in prose: a 🟡 preprint is "early research suggests", not "research proves".
- Porto-specific implications are internal. Don't put Porto or employer details into public drafts unless AO asks.
