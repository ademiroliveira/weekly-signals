---
theme: Who actually enforces the limit the interface shows?
status: emerging
first_seen: 2026-09-28
last_seen: 2026-09-28
weeks: 1
---
**Thesis so far:** A spending limit or guard in the UI is a promise, and the layer that enforces it decides whether the promise holds. Wallets currently present app-layer, contract-layer and key-layer limits the same way, and that sameness misleads users.

## Evidence
- 2026-09-28 · 🔴 (see caveat) · Budgeted Threshold Signatures. The paper proves that naive MPC-comparison budget checks can be bypassed, undetectably, by an honest-majority coalition of signers. It then gives a Schnorr construction that enforces per-epoch caps inside the signing session. https://eprint.iacr.org/2026/2176
- 2026-09-28 · 🟡 · Safe Contracts v1.5.0. The module guard now covers recovery modules, which closes a path where recovery could sidestep guard logic. This is a concrete case of a displayed control not covering every route to the keys. https://safe.global/blog/safe-contract-version-1-5-0
- 2026-09-28 · 🟠 · Safe{Wallet} spending limits pre-flow. The UX side: users are now told what a limit grants, but not which layer enforces it. https://github.com/safe-global/safe-wallet-monorepo/releases/tag/web-v1.101.0

## Counter-evidence
- Users care whether a limit works, not which layer enforces it. Showing the enforcement layer may add anxiety without adding understanding.
- BTS addresses threshold-signature setups specifically. The claim that it undermines contract-enforced limits (like Safe's) is our reading, carried over from the report's Porto lens. The paper does not make that claim `[needs source]`.

## Caveat on strength
The report rated BTS 🔴 Strong, but it is an IACR ePrint. "Approved" on ePrint means approved for posting, not peer review. Under the repo's rubric (preprint → 🟡) it should be treated as **early research** in prose until it is published at a venue.

## Open question
Will any wallet or agent framework label enforcement level in the UI (e.g. "enforced by your keys" vs "enforced by the app")? Will BTS, or a similar scheme, move from ePrint toward a spec or an implementation? Either would confirm the thesis. If the field converges on contract-layer limits as good enough and no key-layer scheme ships, the thesis should narrow.
