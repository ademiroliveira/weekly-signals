# Article ideas

Maintained by `/angle`. Newest first.

## 2026-09-28 — seeded from the first archived week

### Comprehension before configuration: how delegation should feel
- **Thesis:** Delegating custody (to a co-signer, a proposer or an agent) should always be explained before it's configured. Otherwise the form itself becomes the explanation, and users learn scope by filling in fields.
- **Why now:** Safe shipped two separate comprehension gates at delegation points in a single release.
- **Evidence:** 2026-09-28 · Safe{Wallet} web-v1.101.0 · https://github.com/safe-global/safe-wallet-monorepo/releases/tag/web-v1.101.0 (needs 2+ more signals)
- **The design move:** explanation-first, configuration-second, at every point where trust is delegated.
- **Counterpoint:** added friction; expert users skip the explanation anyway.
- **Fit:** Refined (craft) · LinkedIn
- **Readiness:** needs 2–3 more weeks of signal

### Your spending limit is a UX promise the cryptography doesn't keep
- **Thesis:** When an agent wallet shows a spending limit, the interface is promising something that app-layer policy can't guarantee. Designers need to know which layer enforces what they display.
- **Why now:** BTS (IACR 2026/2176) formally proves app-layer budget checks can be bypassed; agent payments are growing fast.
- **Evidence:** 2026-09-28 · Budgeted Threshold Signatures · https://eprint.iacr.org/2026/2176 ; 2026-09-28 · Safe spending limits pre-flow (UX side)
- **The design move:** show enforcement level honestly in the UI ("enforced by your keys" vs "enforced by the app").
- **Counterpoint:** users don't care about layers; they care whether it works. Too much detail creates anxiety.
- **Fit:** Refined · talk
- **Readiness:** close; one more agentic UX signal would make it ready
