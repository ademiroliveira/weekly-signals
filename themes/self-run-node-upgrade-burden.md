---
theme: Who carries the burden of keeping self-run custody safe?
status: active
first_seen: 2026-10-05
last_seen: 2026-11-09
weeks: 6
---
**Thesis so far:** Running your own Lightning node means the operator, not a vendor, has to notice and apply each security fix, and six reports across the archive carried a node or server release the operator had to apply, now spanning Eclair, Core Lightning, LND and BTCPay.

## Evidence
- 2026-10-05 · 🟠 · Eclair Lightning Node Dual DoS Disclosure (fixed in v0.14.0) — two denial-of-service bugs reported in Optech #425. https://bitcoinops.org/en/newsletters/2026/10/02/
- 2026-10-12 · 🟠 · Core Lightning 26.06.9 and LDK security releases (Optech #426). https://bitcoinops.org/en/newsletters/2026/10/09/
- 2026-10-19 · 🟠 · Eclair Fixes Two Memory-Exhaustion DoS Bugs in v0.14.1 (Optech #427) — the newsletter says users on older versions should upgrade. https://bitcoinops.org/en/newsletters/2026/10/16/
- 2026-10-26 · 🔴 · Eclair 0.14.4 and 0.14.5 Are Security Releases (Optech #428) — fund-theft flaws fixed, project strongly recommends upgrading. https://bitcoinops.org/en/newsletters/2026/10/23/
- 2026-11-02 · 🔴 · Eclair 0.14.6 security release and Bitcoin Core backport policy (Optech #429). https://bitcoinops.org/en/newsletters/2026/10/30/
- 2026-11-09 · 🟠 · Core Lightning 26.06.10 security release; LND MPTCP mitigation that leaves the fix to the host kernel; BTCPay Server 2.4.7 (Optech #430). https://bitcoinops.org/en/newsletters/2026/11/06/

## Counter-evidence
- Optech #427 says mobile wallets using an Eclair LSP, such as Phoenix, are unaffected, so the burden falls only on people who run the node themselves.

## Open question
Does any wallet or node product show the operator that a security release exists and what it protects? No UX signal in the archive covers this yet.
