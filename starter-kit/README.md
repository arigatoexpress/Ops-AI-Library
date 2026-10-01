# Gemini Enterprise Starter Kit — Wrong-Day / Right-Day Lates

**Purpose:** One drop-in packet for Gemini Enterprise (Outlook + Teams connected) that a manager can paste and run on the sanctioned wrong-day/right-day lates use case.

**Public repo, synthetic-only.** No proprietary FedEx data, no real tracking numbers, no PII. Everything here is a template, a methodology, or a synthetic example.

**Companion artifacts:**
- [P45–P48 prompts](../prompts/late-arrival-and-service-recovery.md)
- [Baseline framework](../docs/wrong-day-lates-baseline.md)
- [Gemini Enterprise late-arrival config](../docs/gemini-enterprise-late-arrival-config.md)
- [Power Automate flow specs](../playbooks/power-automate-flow-specs.md) (Flow D extends these)

---

## What's in the kit

| File | What it does |
| --- | --- |
| [01-drop-in-packet.md](01-drop-in-packet.md) | The single paste-into-Gemini block: system instruction + evidence-table workflow + output format. Start here. |
| [02-correlation-matrix.md](02-correlation-matrix.md) | Candidate metric pairs and black-swan signals to investigate — labeled as hypotheses, never as proven causes. |
| [03-power-automate-flow-d.md](03-power-automate-flow-d.md) | Flow D spec: manager-triggered late-arrival assist with scrub gate, approval, and draft-only output. |
| [04-synthetic-example.md](04-synthetic-example.md) | One fully worked synthetic example (wrong-day late) showing expected evidence table + brief shape. |
| [05-measurement-plan.md](05-measurement-plan.md) | Before/after timing trials and the pilot scorecard fields specific to this use case. |

## How to use on the job

1. Open Gemini Enterprise in the approved environment.
2. Paste the block from `01-drop-in-packet.md` as the agent instruction (or attach it as a file).
3. Attach your approved, scrubbed source report for the period in question.
4. Run. Review every number against the source before sharing.
5. If a Power Automate flow is approved, use Flow D instead of manual paste — it adds the scrub gate and approval step automatically.

## What this kit is NOT

- Not a live integration with FedEx operational systems.
- Not a dispatch, reroute, or customer-contact tool.
- Not measured ROI until the timing trials in `05-measurement-plan.md` are recorded.
- Not permission to paste confidential data into public or unapproved tools.

## Design principles (same as the library)

1. **Modular** — one file, one job; compose, don't fork.
2. **Evidence before prose** — every output starts with a claim/source table.
3. **Draft before action** — default agency is draft or recommend.
4. **Synthetic in public** — real operational data never enters this repo.
5. **Preserve existing work** — P01–P48, Travis Long's concepts, governance docs, and SharePoint templates are untouched.
