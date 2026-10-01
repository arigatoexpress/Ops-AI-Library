# Wrong-Day & Right-Day Lates — Starter Kit v1.1

**Purpose:** A complete, drop-in packet for the sanctioned AI Efficiency Group project. Paste this into Gemini Enterprise (with Outlook/Teams connected) and you are on the case — no rebuilding, no proprietary data, no company-specific configuration required.

**Public repo, synthetic-only.** No real tracking numbers, customer names, addresses, employee records, route manifests, or facility identifiers ever enter these files. Real operational data stays in approved internal systems; this kit holds the methodology, prompts, flows, and measurement plan.

**Companion artifacts (already on main):**
- [P45–P48 prompts](../prompts/late-arrival-and-service-recovery.md)
- [Baseline framework + Gemini config](../docs/wrong-day-lates-baseline.md)
- [Standalone agent config block](../docs/gemini-enterprise-late-arrival-config.md)
- [Today's meeting brief](../docs/weekly-meeting-2026-10-01.md)
- [Power Automate specs A/B/C](../playbooks/power-automate-flow-specs.md)

---

## What's in this kit

| File | What it does |
| --- | --- |
| [01-gemini-enterprise-pack.md](01-gemini-enterprise-pack.md) | The full drop-in: agent instruction, evidence-table workflow, output templates, quality gate. Copy → paste → attach approved source → run. |
| [02-power-automate-flow-d.md](02-power-automate-flow-d.md) | Flow D: manager-triggered late-arrival triage that stages a draft and waits for human approval. Never auto-sends. |
| [03-correlation-matrix-framework.md](03-correlation-matrix-framework.md) | How to find metric correlations, flag black swans, and turn them into recommended next steps — without claiming causation. |
| [04-sharepoint-upload-guide.md](04-sharepoint-upload-guide.md) | Step-by-step to publish this kit on the team SharePoint page. |
| [05-measurement-plan.md](05-measurement-plan.md) | Timed before/after trials, pilot scorecard fields, kill/keep/change criteria. |

## Design principles (non-negotiable)

1. **Modular, not opinionated.** One prompt = one job. Compose; don't fork.
2. **Synthetic-only in public.** Real data never enters this repo.
3. **Evidence before prose.** Every output starts with a claim/source table; "Needs verification" is a first-class status.
4. **Draft before action.** Default agency is draft or recommend. No dispatch, reroute, or customer contact.
5. **Adaptable to facts on the ground.** Placeholders are generic: station, sort hub, P&D, linehaul.
6. **Preserve existing work.** Travis Long's concepts and all prior prompts are untouched.

## What this kit is NOT

- Not official FedEx policy or a production system.
- Not a claim that any integration is live.
- Not measured ROI until timed trials are recorded.
- Not permission to paste real operational data into public or unapproved systems.

## Quick start (5 minutes)

1. Open Gemini Enterprise.
2. Create a new agent; paste the instruction block from [01-gemini-enterprise-pack.md](01-gemini-enterprise-pack.md).
3. Attach one approved, scrubbed source (a late-arrival report export is fine if policy allows).
4. Run with a synthetic example first.
5. Review the draft, edit, and share only what you verified.
