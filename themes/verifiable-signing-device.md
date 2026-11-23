---
theme: What can a user verify about the device that signs for them?
status: emerging
first_seen: 2026-10-12
last_seen: 2026-11-23
weeks: 4
---
**Thesis so far:** Trust in a signing device has rested on the vendor's supply chain and firmware, and the archive now shows protocol-level proposals that would let the host check the device's behaviour, moving part of that trust into something software can test.

## Evidence
- 2026-10-12 · 🟠 · Ledger reseller supply-chain attack surfaces device provenance as a custody precondition. https://unchainedcrypto.com/ledger-users-reportedly-drained-of-over-86-million-across-several-blockchains/
- 2026-10-19 · 🟠 · Update: Ledger responds to a hardware implant attack on devices returned through resellers. https://www.ledger.com/blog-response-hardware-implant-attack
- 2026-11-16 · 🟡 · Draft anti-exfil signing BIPs would have the host contribute to the nonce so a compromised device cannot leak its seed (Optech #431). https://bitcoinops.org/en/newsletters/2026/11/13/
- 2026-11-16 · 🟡 · arXiv paper questions the assumption behind RFC 6979 deterministic nonces; 28 of 31 audited secp256k1 implementations sign without added entropy. https://arxiv.org/abs/2611.18449
- 2026-11-23 · 🟠 · Independent Keylabs review confirms COLDCARD's fix for seed generation that used MicroPython's Yasmarang software generator instead of the hardware RNG; seeds already generated on affected firmware are not repaired. https://coldcard.com/security/status

## Counter-evidence
- The anti-exfil cryptography "had not received any audit", per Optech #431.
- The Keylabs report lists Coinkite as its client and is hosted only by Coinkite, so the review that restores trust is itself commissioned by the vendor.

## Open question
Will a hardware signer and a coordinator ship anti-exfil together, and how would the user see that the check ran? Will any signer let users check the entropy behind a seed it already generated?
