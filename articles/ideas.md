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

## 2026-11-23

### Logging in is not holding the keys
- **Theme:** `themes/propose-versus-sign.md`
- **Thesis:** As custody products add logins, workspaces, proposer roles and agents, the most important sentence in the interface is the one that says which of them can actually move money.
- **Why now:** Safe Pro now writes that separation into the product, and an agent wallet has shipped where the agent prepares and the user approves elsewhere.
- **Evidence:** 2026-09-28 · 🟠 · Safe{Wallet} web-v1.101.0: Proposer Role Education and Spending Limits Pre-Flow · https://github.com/safe-global/safe-wallet-monorepo/releases/tag/web-v1.101.0 ; 2026-11-02 · 🔴 · Update: MetaMask Agent Wallet Goes Live as a Grok Bot Plugin, with Guard Mode Limits and Out-of-Band Approval · https://metamask.com/news/metamask-agent-wallet-grok-bot ; 2026-11-23 · 🔴 · Safe Pro Makes the Workspace the Account, but "No Workspace Role Grants Signing or Execution Authority" · https://safe.global/blog/authentication-is-not-authorization-how-safe-pro-separates-access-from-signing ; 2026-11-23 · 🔴 · Safe's New Queue Service Drops a Removed Owner's Pending Signatures and Delegations and Rejects Unsigned Proposals · https://safe.global/blog/new-queue-service-multichain-by-default
- **The design move:** name three layers (access, propose, sign) and say on each screen which one the user is in. The login screen says what logging in can't do, Review says who prepared the transaction, and removing a signer visibly removes their pending approvals.
- **Counterpoint:** Safe says its wallet sign-in "doesn't have 2FA yet", so the access layer is still the weak one, and naming it doesn't fix that. Three of the four signals come from one product family.
- **Format:** essay · ~1,200 words
- **Fit:** Refined · LinkedIn
- **Readiness:** ready (4 signals from 3 reports, 3 of them UX)

### A protection you can't see the edge of is a promise you can't check
- **Theme:** none yet. This is a companion to "Your spending limit is a UX promise the cryptography doesn't keep": that idea asks which layer enforces a limit, and this one asks whether the user can see where any protection stops.
- **Thesis:** Wallets keep shipping protections whose boundary is invisible (switched off together, scoped to some actions, or authored by someone else), and users extend trust past the edge because nothing marks it.
- **Why now:** five UX signals in seven weeks, from three vendors, each about where a protection starts, stops or comes from.
- **Evidence:** 2026-10-05 · 🟠 · MetaMask Basic Functionality Toggle: Binary Security/Privacy Gate at Onboarding · https://metamask.io/news/product-spotlight-privacy-preserving-features-in-metamask ; 2026-10-05 · 🟠 · MetaMask Agent Wallet Guard Mode: Selective Evaluation Perimeter Excludes Off-Chain Protocol Actions · https://metamask.io/news/trade-prediction-markets-metamask-agent-wallet ; 2026-10-19 · 🟡 · Ledger Atom Preview: Secure Mode Takes Over the Screen for Approvals, with a Secure Bar · https://www.ledger.com/blog-ledger-atom-security-architecture ; 2026-10-26 · 🔴 · Safenet Launches: Four Security Firms Assess Safe Pro Transactions Before Execution, Replacing the Interface Warning · https://safe.global/blog/safenet-launches ; 2026-11-02 · 🔴 · Update: MetaMask Agent Wallet Goes Live as a Grok Bot Plugin, with Guard Mode Limits and Out-of-Band Approval · https://metamask.com/news/metamask-agent-wallet-grok-bot
- **The design move:** every protection shows three things: what it covers, what it doesn't, and who stands behind the verdict. A check that didn't run looks different from a check that passed, and no switch turns off several protections without naming them.
- **Counterpoint:** the Basic Functionality switch exists for a real reason, because users trade checks for less data sharing, and listing every boundary adds noise to a screen people already skim. The Atom evidence is a preview with too little flow detail to judge.
- **Format:** pattern breakdown · ~1,000 words
- **Fit:** Refined · talk
- **Readiness:** ready (5 signals from 4 reports, all UX). The catch-up items queued for 2026-11-30 (a "Simulation Unavailable" notice, Safenet checks shown as unreadable) would strengthen it if they verify.

### "Buy direct" is not a security model
- **Theme:** `themes/verifiable-signing-device.md`
- **Thesis:** Hardware wallet trust has been handed to the shopper as an instruction to buy from the right place, and the archive shows it moving into checks that software can run, which means the interface now has to show that those checks ran.
- **Why now:** two reseller attacks, a firmware RNG flaw whose fix can't repair existing seeds, and draft BIPs that let the host test the device, all inside seven weeks.
- **Evidence:** 2026-10-12 · 🔴 · Ledger Supply Chain Attack Surfaces Device Provenance as an Unscaffolded Custody Precondition · https://unchainedcrypto.com/ledger-users-reportedly-drained-of-over-86-million-across-several-blockchains/ ; 2026-10-19 · 🟠 · Update: Ledger Responds to Hardware Implant Attack on Devices Returned Through Resellers · https://www.ledger.com/blog-response-hardware-implant-attack ; 2026-11-16 · 🟡 · Draft BIPs Propose a Standard Anti-Exfil Signing Protocol So a Compromised Signing Device Cannot Leak Its Seed Through Nonces (Optech #431) · https://bitcoinops.org/en/newsletters/2026/11/13/ ; 2026-11-16 · 🟡 · Deterministic ECDSA on secp256k1: the RFC 6979 Assumption, a Counterexample, and the State of Deployed Implementations · https://arxiv.org/abs/2611.18449 ; 2026-11-23 · 🟠 · Independent Keylabs Review Confirms COLDCARD's July 2026 RNG Fix in Shipped Firmware; the Fix Does Not Repair Seeds Already Generated on Affected Firmware · https://coldcard.com/security/status
- **The design move:** treat device trust as a state the wallet shows, next to backup status, with the date of the last check. Design the "this seed can't be trusted" path (new seed, move everything) before an incident needs it.
- **Counterpoint:** the checks themselves are thin. Ledger's Genuine Check can't detect hardware changes to the case, the anti-exfil cryptography "had not received any audit", and the COLDCARD review was commissioned by the vendor. A green check could overstate what was verified.
- **Format:** essay · ~1,200 words
- **Fit:** Refined · talk
- **Readiness:** ready (5 signals from 4 reports, 1 UX). Device-setup checks queued for catch-up (Ledger Live, Trezor Suite) would add the shipped-UX side.
