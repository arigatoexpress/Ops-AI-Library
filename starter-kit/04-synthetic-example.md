# 04 — Synthetic Example (Wrong-Day Late)

**Label:** Synthetic demonstration — not live operations, measured performance, official policy, or a production system. All values below are fictional.

---

## Input (scrubbed, synthetic)

```text
Operation type: sort hub (SYN-FAC-001)
Period: 2026-09-28 to 2026-10-02
Comparison period: 2026-09-21 to 2026-09-25

Scrubbed notes:
- Inbound feeder arrived ~90 minutes after the planned sort-start window on 2026-09-30.
- Sort occupancy in ZONE-B peaked near 95% during the compressed window.
- Equipment down event: one belt in ZONE-B offline for part of the shift (category only).
- Weather band: elevated (public NWS reference).
- Staffing: planned TLH met; actual TLH slightly below plan.
- Outbound commitments: several marked as not met for the committed day.
- No customer names, tracking numbers, or facility codes in this input.
```

---

## Expected evidence table (section A) — shape only

| Metric | Period | Scope | Actual | Commitment/Goal | Variance | Source location | Status | Manager question |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Commitment met rate | 9/28–10/2 | SYN-FAC-001 | [value] | [value] | [value] | [source] | confirmed / needs verification | Did outbound compress after the late feeder? |
| Right-day late rate | 9/28–10/2 | SYN-FAC-001 | [value] | [value] | [value] | [source] | needs verification | Were any commitments met but outside window? |
| Sort occupancy (ZONE-B) | 9/30 | SYN-FAC-001 | ~95% | [baseline] | [value] | [source] | confirmed | What is the normal peak band? |
| TLH variance | 9/28–10/2 | SYN-FAC-001 | slightly below plan | plan | [value] | [source] | confirmed | Is the gap material? |
| Equipment down events | 9/30 | ZONE-B | 1 (belt) | [baseline] | [value] | [source] | confirmed | Duration and recovery time? |
| Weather severity band | 9/30 | public region | elevated | [baseline] | [value] | NWS public | confirmed | Did it affect feeder ETA? |

---

## Expected correlation pass (section B) — shape only

- C1 (volume vs met rate): not observable from this input alone → "Needs verification."
- C4 (equipment down vs wrong-day lates): belt offline on 9/30 coincides with outbound misses → **HYPOTHESIS**, not cause.
- C5 (weather band vs wrong-day lates): elevated band on 9/30 coincides with late feeder → **HYPOTHESIS**, not cause.
- Black swan candidate: ZONE-B occupancy ~95% is flagged if it exceeds two standard deviations from the period baseline — verify the baseline definition before treating as signal.

---

## Expected manager artifact (section D) — shape only

- Situation: inbound feeder late ~90 minutes on 9/30; outbound commitments missed for the committed day. (Confirmed from notes.)
- Impact: sort compression in ZONE-B; possible customer-delivery risk (general).
- Actions taken: [from notes — do not invent].
- Decisions needed: roles only — e.g., "network coordination to review feeder ETA process."
- Info missing: exact commitment counts, customer impact detail, equipment recovery time.
- Next check-in: next business day, role-based.

---

## Expected next steps (section E) — shape only

| Step | Owner role | Due timing | Evidence needed | Risk if skipped |
| --- | --- | --- | --- | --- |
| Verify feeder ETA root cause with network team | Network coordinator | Next business day | Feeder log, ETA definition | Repeat late feeder |
| Confirm ZONE-B occupancy baseline | Sort manager | This week | 28-day occupancy history | False alarm on 95% |
| Draft customer-impact summary for review | Service coordinator | 48 hours | Commitment list (approved) | Unmanaged customer contact |

All steps reversible or low-cost. None require dispatch authority.

---

## Quality check (section F)

- Every bracketed value above must be replaced by a source-backed number from the attached report.
- Any sentence not supported by the evidence table is flagged.
- Output ends with: **DRAFT - MANAGER REVIEW REQUIRED.**
