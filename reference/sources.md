# Source entry points

Start each search with the dated listings below, then use WebSearch to go wider. Search pages on arXiv, the IACR, ACM, SSRN and SOUPS are blocked by robots.txt, and blocked pages can't be used as sources. Don't burn fetches on them.

Status: **ok** = the listing loaded with visible dates when tested on 2026-10-12 · **used** = individual pages loaded in past runs, but the listing page hasn't been checked · **partial** = loads but has a known catch · **blocked** = refused, don't use · **untested** = expected to work, not yet checked. When a run finds that a status has changed, the Source Audit should say so, and the next pipeline edit updates this file.

## Academic & cryptography

| Source | URL | Status | Notes |
|---|---|---|---|
| IACR ePrint, last 7 days | `https://eprint.iacr.org/days/7` | ok | Lists papers **updated** in the last 7 days. Open each paper page and use its "Received" date for the window. A revised old paper doesn't qualify. |
| arXiv cs.CR recent | `https://arxiv.org/list/cs.CR/recent?skip=0&show=2000` | ok | One page per weekday. Each abs page shows the v1 submission date. |
| arXiv cs.HC recent | `https://arxiv.org/list/cs.HC/recent?skip=0&show=2000` | ok | For wallet UX and usable security. |
| arXiv cs.DC recent | `https://arxiv.org/list/cs.DC/recent?skip=0&show=2000` | untested | Distributed key generation, consensus-adjacent custody. |
| arXiv search / API / RSS | `arxiv.org/search`, `export.arxiv.org/api`, `rss.arxiv.org` | blocked | The RSS feed is also empty on weekends. |
| IACR search | `eprint.iacr.org/search` | blocked | |
| ACM DL, SSRN, SOUPS program pages | | blocked | Find usable-security papers through arXiv cs.HC instead. |

## Standards

| Source | URL | Status | Notes |
|---|---|---|---|
| W3C technical reports | `https://www.w3.org/TR/` | used | Each spec shows its date and maturity level (WD, CR, REC). |
| NIST CSRC publications | `https://csrc.nist.gov/publications` | used | |
| EIP / ERC pull requests | `https://github.com/ethereum/EIPs/pulls`, `https://github.com/ethereum/ERCs/pulls` | partial | Individual PR pages load. The list views are sometimes refused. `eips.ethereum.org/all` shows no dates. |
| Ethereum Magicians | | blocked | |
| BIS, FSB, FATF publication lists | `https://www.bis.org/publ/work.htm`, `https://www.fsb.org/publications/`, `https://www.fatf-gafi.org/en/publications.html` | partial | BIS has returned 404s in past runs. |

## Regulatory

| Source | URL | Status | Notes |
|---|---|---|---|
| Federal Register API (all US agencies) | `https://www.federalregister.gov/api/v1/documents.json?conditions[term]=crypto+custody&order=newest&per_page=20` | ok | Best single US source: SEC, CFTC, FinCEN, OCC, Treasury, IRS. Gives the document type (proposed rule, rule, notice) and publication date. Change the term: `self-hosted wallet`, `digital asset`, `crypto asset`. |
| SEC press releases RSS | `https://www.sec.gov/news/pressreleases.rss` | ok | |
| CFTC press releases | `https://www.cftc.gov/PressRoom/PressReleases` | used | |
| FinCEN news | `https://www.fincen.gov/news-room` | used | |
| ESMA news | `https://www.esma.europa.eu/press-news/esma-news` | used | |
| congress.gov | | blocked | |

## Institutional research

| Source | URL | Status | Notes |
|---|---|---|---|
| Galaxy Research | `https://www.galaxy.com/insights/research/` | used | |
| Chainalysis blog | `https://www.chainalysis.com/blog/` | used | |
| a16z crypto | `https://a16zcrypto.com/posts/` | untested | |
| Messari | | blocked | Returned 403 in past runs. |

## Security, vendors and protocol teams

| Source | URL | Status | Notes |
|---|---|---|---|
| Bitcoin Optech | `https://bitcoinops.org/feed.xml` | ok | One newsletter can produce several items. Cite the newsletter, and split it only when the items are unrelated. |
| Ethereum Foundation blog | `https://blog.ethereum.org/` | used | |
| Ledger blog | `https://www.ledger.com/blog` | ok | Dates are shown. Also look for Ledger Donjon security posts. |
| Coinkite (COLDCARD) blog | `https://blog.coinkite.com/` | used | |
| Safe blog | `https://safe.global/blog` | used | |
| MetaMask news | `https://metamask.io/news` | used | |
| GitHub release pages | `https://github.com/<org>/<repo>/releases` | ok | `.atom` feeds are blocked, but the HTML release pages load with notes. A release with no notes on the page can't be used. |
| Trezor blog | `https://blog.trezor.io/` | partial | Loads without post listings. Use WebSearch for recent Trezor posts and fetch each one. |
| Trail of Bits, OpenZeppelin, Zellic, Halborn blogs | | untested | Halborn posts have had no visible publish date. Those can't be used. |
| NVD / CVE | | blocked | |

### Wallet release pages to check every week (wallet-ux)

`MetaMask/metamask-extension` · `MetaMask/metamask-mobile` · `safe-global/safe-wallet-monorepo` · `RabbyHub/Rabby` · `rainbow-me/rainbow` · `LedgerHQ/ledger-live` · `trezor/trezor-suite` · `coinbase/coinbase-wallet-sdk`

## Journalism: tier 7, fallback only

Allowed outlets, and only these:
- **The Block Research.** Research reports only. Regular `theblock.co` news and ecosystem articles don't qualify.
- **Bitcoin Magazine.** Analysis and technical pieces only (e.g. `/technical/`). News items don't qualify.
- **Bitcoin Foundation research.**
- **Unchained** (`unchainedcrypto.com`).

Not allowed, as killed in past runs: CoinDesk, Cointelegraph, Decrypt, CryptoSlate, CryptoTicker, The Block news, Help Net Security, crypto-reporter.com, cryptoast.fr, and any press-release relay.

For incidents and product changes, look for the affected organisation's own statement (vendor blog, security advisory, status page) **before** journalism. It's a stronger source and is tagged [Vendor security report] or [Protocol blog].
