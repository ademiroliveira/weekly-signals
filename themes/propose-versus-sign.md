---
theme: Who may propose, and who may sign?
status: emerging
first_seen: 2026-09-28
last_seen: 2026-11-23
weeks: 2
---
**Thesis so far:** Team custody products are pulling apart three layers that used to blur together (logging in, proposing a transaction, signing it), and the products that say plainly which layer grants custody give users fewer ways to mistake access for authority.

## Evidence
- 2026-09-28 · 🟠 · Safe{Wallet} web-v1.101.0 adds proposer-role education before delegation. https://github.com/safe-global/safe-wallet-monorepo/releases/tag/web-v1.101.0
- 2026-11-23 · 🔴 · Safe Pro Workspace: "No Workspace role grants signing or execution authority over a Safe." https://safe.global/blog/authentication-is-not-authorization-how-safe-pro-separates-access-from-signing
- 2026-11-23 · 🔴 · Safe's new queue service rejects unsigned proposals and drops a removed owner's pending signatures and delegations. https://safe.global/blog/new-queue-service-multichain-by-default

## Counter-evidence
- Safe says wallet sign-in to the Workspace "doesn't have 2FA yet", so the access layer is still weaker than the signing layer it sits on.
- All evidence so far comes from one product family.

## Open question
Does another multisig or team-custody product adopt the same separation, and does any of them show it in the signing interface rather than in a blog post?
