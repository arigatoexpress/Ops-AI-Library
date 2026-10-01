# 02 — Power Automate Flow D: Late-Arrival Triage (Draft + Approval)

**Name:** `OpsAI-D-LateArrivalTriage-v1`  
**Goal:** Manager-triggered late-arrival triage that stages a Gemini draft and waits for human approval before any share. Never auto-sends. Never auto-posts to a channel.

**Agency level:** draft + human approval. This is a build spec, not a live flow.

---

## Shared standards (same as Flows A/B/C)

| Standard | Requirement |
| --- | --- |
| Environment | Company-managed Power Platform env only |
| DLP | Confirm connectors allowed (SharePoint, Teams, Outlook, Gemini/Copilot if approved) |
| Secrets | No API keys in plain compose actions |
| Logging | Run history retained per tenant policy; log metadata only, not note contents |
| Kill switch | Environment variable `OPS_AI_FLOWS_ENABLED=false` stops triggers |
| Data | Scrubbed / non-sensitive fields only in v1 |
| Naming | `OpsAI-D-LateArrivalTriage-v1` |
| Owner | Named human + backup |

---

## Flow steps

| Step | Action | Notes |
| --- | --- | --- |
| 1 | Trigger: Manual button / Adaptive Card "Draft late-arrival triage" | Manager only |
| 2 | Input: ScrubbedNotes (multiline) + OperationType (station/sort hub/P&D/linehaul) + Period | Helper text: no PII, no tracking numbers |
| 3 | Keyword/regex scan for long numeric IDs and email-like patterns | If hit → return "Scrub first" message; do not call AI |
| 4 | Compose the Gemini prompt from the starter-kit agent instruction + inputs | Use the 01-gemini-enterprise-pack.md block |
| 5 | Call approved AI connector (Gemini Enterprise) | Branch: if connector unavailable → create task "Human triage needed" |
| 6 | Return draft **only to the runner** (chat/email to self) | No channel post, no customer contact |
| 7 | **Start and wait for an approval** (content owner) | If rejected → log and end |
| 8 | On approve: optionally post scrubbed summary to Teams channel | Still labeled DRAFT |
| 9 | Log metadata only (user, timestamp, length, outcome) | Never log note contents in v1 |

---

## Acceptance tests (run before Pilot tag)

| Test | Expected |
| --- | --- |
| Keyword scan blocks obvious tracking-like strings | No AI call made |
| Rejected approval does not post | No Teams message |
| Kill switch stops trigger | Flow does not run |
| Output returns only to initiator until approved | No channel post in v1 |
| Every number in draft traces to input | Quality gate passes |

---

## Build order

1. Confirm DLP and connector availability with IT/governance.
2. Build Flow D in a dev environment first.
3. Run acceptance tests with synthetic notes.
4. Pilot with one manager, one operation type, 30 days.
5. Feed results back to this repo as a dated note.
