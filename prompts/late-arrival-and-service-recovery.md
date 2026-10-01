# Late Arrival & Service Recovery Prompts

**Status:** Draft templates for the AI Efficiency Group. Synthetic examples only — no real tracking numbers, customer names, addresses, or facility identifiers.

**Scope:** Wrong-day lates, right-day lates, and service-recovery framing. These prompts draft coordination language and recovery plans; they do not dispatch, reroute, or contact customers.

**How to use:** Paste scrubbed notes into Gemini Enterprise, review every claim against the source, and edit before sharing. Label output DRAFT — MANAGER REVIEW REQUIRED.

---

## P45 — Wrong-Day Late Framing

```text
Act as a FedEx operations supervisor framing a wrong-day late for internal coordination.

Context (scrubbed — no real tracking numbers, customer names, addresses, or facility identifiers):
[Paste non-sensitive notes: what was expected, what actually happened, general impact.]

Return:
- Situation in 2 sentences (confirmed facts only)
- Operational impact (sort / P&D / customer risk — general terms)
- Actions already taken
- Decisions needed (roles, not personal names)
- Information still missing
- Suggested next check-in time

Rules:
- Do not invent facts, causes, or root causes.
- Put unclear items under "Needs verification."
- Neutral tone. No blame.
- Label the whole output as a draft for manager review.
```

## P46 — Right-Day Late Framing

```text
Act as a FedEx operations supervisor framing a right-day late (on-time-but-late-in-window) for internal coordination.

Context (scrubbed):
[Paste non-sensitive notes: commitment window, actual arrival, general impact.]

Return:
- Situation in 2 sentences
- Whether the commitment was met or missed (confirmed only)
- Operational impact (general)
- Actions already taken
- Decisions needed (roles)
- Information still missing

Rules:
- Do not infer root cause from the variance.
- Do not invent facts.
- Label the whole output as a draft for manager review.
```

## P47 — Service Recovery Plan Draft

```text
Draft a service-recovery plan for a late or missed commitment.

Event (scrubbed, general terms):
[Describe the event without sensitive identifiers.]

Return:
- Customer impact (general — no names or tracking numbers)
- Recovery options (2-3, advisory only)
- Communication needed (who to notify, in role terms)
- Owner and next step for each option
- What must be verified before acting

Rules:
- Advisory only. No dispatch authority, no customer contact.
- Do not promise outcomes that are not confirmed.
- Label the whole output as a draft for manager review.
```

## P48 — Late-Arrival After-Action

```text
Create an after-action review for a late-arrival event.

Event:
[Describe in general terms.]

Notes (scrubbed):
[Paste notes.]

Return:
- What happened (confirmed facts only)
- What went well
- What slowed us down
- Root causes to investigate (labeled as hypotheses)
- Corrective actions with owners (roles)
- Follow-up date

Separate confirmed facts from theories. No real employee names or incident IDs.
```

---

## Design notes

- **Modular:** each prompt is one job. Combine P45/P46 with P47 for a full recovery cycle.
- **Adaptable:** placeholders are generic so the same prompt works at a station, sort hub, or P&D operation.
- **Grounded:** every prompt forces "Needs verification" instead of invented causes — matching the library's evidence-first standard.
- **Safe:** no real operational data ever enters the prompt. Synthetic examples only.
