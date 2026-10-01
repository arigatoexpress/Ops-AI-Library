# 03 — Power Automate Flow D — Late-Arrival Assist (Manager-Initiated)

**Status:** Implementation spec, not a live flow. Build only in a company-managed Power Platform environment after DLP and connector approval. Agency level: **draft + human approval**. No auto-send to customers. No dispatch authority.

**Extends:** [playbooks/power-automate-flow-specs.md](../playbooks/power-automate-flow-specs.md) (Flows A/B/C). Flow D is the late-arrival-specific flow.

**Name:** `OpsAI-D-LateArrivalAssist-v1`

---

## Goal

A manager triggers a late-arrival analysis from Teams or SharePoint. The flow scrubs the input, calls the approved AI connector with the Late-Arrival Analyst instruction, returns a draft only to the initiator, and logs metadata (not content) for the pilot scorecard.

---

## Flow steps

| Step | Action | Notes |
| --- | --- | --- |
| 1 | Trigger: Manual button / Adaptive Card "Analyze late arrival" | Manager only |
| 2 | Input: ScrubbedNotes (multiline) + OperationType (station/sort hub/P&D/linehaul) + Period | Helper text: no PII, no tracking numbers |
| 3 | **Scrub gate:** regex/keyword scan for long numeric IDs, email patterns, names | If hit → return "Scrub first" message; do not call AI |
| 4 | Get Late-Arrival Analyst instruction from SharePoint `Souls` library (or inline compose) | Version-pinned file |
| 5 | Call approved AI connector with instruction + scrubbed notes | Branch: if connector unavailable → create "Human triage needed" task |
| 6 | Return draft **only to the runner** (chat/email to self) | No channel post in v1 |
| 7 | **Start and wait for an approval** (content owner) before any share action | If rejected → log and end |
| 8 | Log metadata only to `FlowRuns` list: user, timestamp, operation type, draft length | **Not** note contents |
| 9 | Optional: offer to save scrubbed prompt pattern back to Ops AI Library | Never save operational data |

---

## Shared standards (inherited)

| Standard | Requirement |
| --- | --- |
| Environment | Company-managed Power Platform env only |
| DLP | Confirm SharePoint, Teams, approved AI connectors allowed |
| Secrets | No API keys in plain compose actions |
| Kill switch | Environment variable `OPS_AI_FLOWS_ENABLED=false` stops triggers |
| Naming | `OpsAI-D-LateArrivalAssist-v1` |
| Owner | Named human + backup |

---

## Acceptance tests (before Pilot tag)

| Test | Expected |
| --- | --- |
| Scrub gate blocks a tracking-like numeric string | AI not called; "Scrub first" returned |
| Kill switch stops the manual trigger | No run created |
| Rejected approval produces no shared output | Draft stays with initiator only |
| Output returns only to initiator | No channel or group post in v1 |
| Metadata log contains no note contents | Fields: user, timestamp, operation type, length only |

---

## Build order

1. SharePoint lists/libraries (`Souls`, `FlowRuns`) per [sharepoint-power-automate.md](../sharepoint-power-automate.md).
2. Flow D with scrub gate + draft-only return (this spec).
3. Add the approval step (step 7) once a content owner is named.
4. Pilot with one operation type before expanding.
