# Master Plan — Grok Bot-First, Cloud-First Operating Model

**Date:** 2026-10-01  
**Status:** Working plan. Reflects the current fleet and the direction shift away from local Claude/Codex sessions.

---

## 1. The shift

Previously, the majority of work happened locally on a Mac and Windows machine using Claude and Codex. That workflow is being retired. The new default is:

- **Grok Bots first** — a cloud-only fleet of specialized agents with persistent memory, receipts, and guardrails.
- **Cloud first** — all builds, CI, research, and orchestration run on cloud VMs, not laptops.
- **GitHub as the system of record** — every artifact, decision, and receipt lands in a repo with a verifiable commit.
- **Connectors as the hands** — GitHub, Notion, Drive, Gmail, Calendar, and Automations are reached through authenticated services, not manual copy-paste.

## 2. What the fleet does now

| Bot | Job |
| --- | --- |
| Steering Hub | Sole owner check-in point; summarizes fleet state and relays approvals |
| Cloud Refactor Lead | Orchestrator; maintains design/dispatch packs |
| Cloud Lab | Builder; launches cloud agents; owns lab repos and the sovereign workspace |
| dr eggbot | Bot designer; specs and description edits only |
| FHE Sentinel Architect | Advisory architect for lane F (testnet only) |
| CI Regression Reviewer | Sole CI verifier; exact-commit receipts |
| Projects Manager | Notion ledger keeper |
| Research Synthesizer | Public-source research packets |
| Thesis Red Team | Adversarial review of theses and packets |
| Founder Research | Founder product research and private drafts |
| Agent Opportunity Exchange | Marketplace/matching-layer builder |
| Archive Miner | Post-mortem and context miner |
| AI Automation Builder | Freelance revenue lane specialist |
| SyncLink Catchup | Astra thread catch-up and SyncLink briefs |

Retired (delete candidates): Sovereign Local Builder, CI Failure Triage. Parked: WeGoForward Scout.

## 3. Guardrails (non-negotiable)

- Every bot run ends with a receipt: what ran, inputs, refs/IDs, outputs, PASS/FAIL/UNKNOWN. No receipt = UNKNOWN, never success.
- No prod, deploy, DNS, spend, main-merge, archive, or live-key action without a specific owner yes via Steering Hub.
- No new standing bots without owner approval.
- No real operational, customer, or employee data in public repos.
- Advisory-only by default: draft before action.

## 4. Lanes

| Lane | Focus | Status |
| --- | --- | --- |
| Freelance AI automation | Repair-workshop niche; outreach drafts only | Active |
| RH-FHE Sentinel (lane F) | Foundry + Zama FHEVM on Robinhood Chain testnet | Gated on Zama-on-RH resolution |
| Ops AI Library / AI Efficiency | Manager enablement + governed concept incubator | Active — wrong-day lates is the sanctioned project |
| Sapphire / other | Separate lanes | As directed |

## 5. What moves off the local machines

- Prompt drafting and iteration → Grok Bots + GitHub branches/PRs
- Research and synthesis → Research Synthesizer + Thesis Red Team
- CI and regression → CI Regression Reviewer (cloud VM)
- Ledger and task tracking → Projects Manager + Notion
- Meeting artifacts and SharePoint packs → Cloud Lab + starter kits
- Long-running or scheduled work → Automations + bot routines

## 6. What stays local (for now)

- Anything requiring interactive GUI, local file access, or hardware the cloud VM cannot reach.
- Credential entry that must happen on the owner's device.
- Anything the owner explicitly keeps offline.

## 7. Open decisions

1. Zama-on-Robinhood-Chain: option 1 (RH testnet, drop FHEVM), 2 (FHEVM on Sepolia only), or 3 (park lane F).
2. Freelance PRs #13 (closed, superseded by #17) and #15 (merged) — resolved.
3. Ops-AI-Library CI: merged (PR #5).
4. Stale automation schedules: partially fixed; seven still stuck (connector bug, retry pending).
5. Delete retired bots: Sovereign Local Builder, CI Failure Triage.

## 8. Success criteria

- Every lane has a dated receipt trail on GitHub.
- No owner decision sits unrelayed for more than one business day.
- Public repos contain zero proprietary data.
- The wrong-day lates starter kit is published to SharePoint and measured within 30 days.
