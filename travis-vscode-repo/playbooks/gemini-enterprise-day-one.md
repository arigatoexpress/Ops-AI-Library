# Playbook: Gemini Enterprise Day-One

**Status:** Active — we have Gemini Enterprise and can build agents in the web UI.

---

## Goal

Ship a small set of **high-quality, guardrailed agents** managers can trust, instead of dozens of half-configured experiments.

---

## Day-one agent set (build these first)

| # | Agent name | Soul file | Primary prompts |
| --- | --- | --- | --- |
| 1 | Shift Brief Coach | [souls/shift-brief-coach.md](../souls/shift-brief-coach.md) | daily-operations |
| 2 | Safety Huddle Coach | [souls/safety-huddle-coach.md](../souls/safety-huddle-coach.md) | safety-and-compliance |
| 3 | Metrics Explainer | [souls/metrics-explainer.md](../souls/metrics-explainer.md) | data-and-reporting |

Optional second wave: Meeting Scribe, Process Coach, Governance Gatekeeper.

---

## Create an agent (web UI checklist)

Exact labels vary by Gemini Enterprise version; use this logical checklist:

1. **Create agent** with clear name (use table above).  
2. **Description:** one sentence managers understand.  
3. **Instructions:** paste entire soul.md.  
4. **Starter prompts:** add 2–3 from the matching prompt file.  
5. **Knowledge / files:** only non-sensitive templates (optional). Do not upload confidential ops exports.  
6. **Tools / actions:** leave **off** until governance approves any action-taking.  
7. **Access:** start with builders + pilot managers only.  
8. **Test** with synthetic scenarios (below).  
9. **Document** on SharePoint Agent Gallery (when site exists) and in this repo if behavior changes.

---

## Synthetic test pack (run before sharing)

### Shift Brief Coach

Paste:

```text
Station: [Station A]
Shift: Night
Notes: Typical midweek volume range. One belt delayed return from maintenance.
Weather: rain expected after 02:00. Staffing: full package handler plan; one supervisor floater available.
Open: feeder delayed ~30 minutes (estimate). Safety focus: wet floors at dock doors.
```

Expect: priorities, risks, Needs verification, safety line, no invented counts.

### Safety Huddle Coach

Paste seasonal condition only (heat / ice / rain). Expect ≤150 words + Safety Above All close.

### Metrics Explainer

Paste 4–6 **fake** KPI rows. Expect hypotheses labeled; no invented history.

---

## Naming and versioning

- Agent display name stable: `Shift Brief Coach`  
- Internal note: `v1.0 — soul date YYYY-MM-DD`  
- When soul changes, bump version and re-test the pack  

---

## Rollout stages

| Stage | Who | Exit criteria |
| --- | --- | --- |
| Private | Builders | Test pack passes |
| Pilot | 5–10 managers | Feedback form ≥5 responses; no safety incidents of data misuse |
| Team | Region ops managers | Documented in SharePoint; owner named |

---

## Feedback questions (send with pilot)

1. Did this save time? (minutes estimate)  
2. What did you have to fix in the draft?  
3. Did it invent anything?  
4. Would you use it again this week?  

---

## Anti-patterns

- Building 20 agents before 3 are good  
- Uploading real scorecards as “knowledge”  
- Enabling tools that send email “because we can”  
- No owner and no review date  

---

## Done looks like

A manager can open **Shift Brief Coach**, paste scrubbed notes, get a usable draft in one try, and knows the draft is not a decision.
