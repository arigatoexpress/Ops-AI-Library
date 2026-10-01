# Wrong-Day & Right-Day Lates — Baseline Framework

**Date:** 2026-10-01  
**Audience:** AI Efficiency Group meeting  
**Repo:** [arigatoexpress/Ops-AI-Library](https://github.com/arigatoexpress/Ops-AI-Library)  
**Status:** Public, synthetic-only foundation. No proprietary FedEx data. Ready to adapt on the job.

---

## 1. The problem in one paragraph

Wrong-day lates and right-day lates are the sanctioned AI Efficiency project. The friction is not a lack of data — it is that the data lives in dense operational reports, and turning it into a defensible manager conversation takes time and risks unsupported claims. Gemini Enterprise with Outlook and Teams access is now the approved surface. The gap was a shared, modular, human-readable baseline that any manager can configure without rebuilding from scratch.

## 2. Design principles (non-negotiable)

1. **Modular, not opinionated.** One prompt = one job. Compose them; do not fork them.
2. **Synthetic-only in public.** No real tracking numbers, names, addresses, or facility identifiers ever enter this repo or a public prompt.
3. **Evidence before prose.** Every output starts with a claim/source table; "Needs verification" is a first-class status.
4. **Draft before action.** Default agency is draft or recommend. No dispatch, reroute, or customer contact authority.
5. **Adaptable to facts on the ground.** Placeholders are generic: station, sort hub, P&D, linehaul — the same prompt works everywhere.
6. **Preserve existing work.** Travis Long's concepts (Zero-Click, ACT, EAVA, VRAA, Smith Agent) and all 45 existing prompts are untouched. This baseline extends; it does not replace.

## 3. The four prompts (P45–P48)

| ID | Name | Job | File |
| --- | --- | --- | --- |
| P45 | Wrong-Day Late Framing | Frame a wrong-day late for internal coordination | [prompts/late-arrival-and-service-recovery.md](../prompts/late-arrival-and-service-recovery.md) |
| P46 | Right-Day Late Framing | Frame a right-day late (on-time-but-late-in-window) | same |
| P47 | Service Recovery Plan Draft | Draft 2–3 advisory recovery options | same |
| P48 | Late-Arrival After-Action | After-action review, facts vs hypotheses separated | same |

**Typical cycle:** P45 or P46 → P47 → P48. Each step is independently reviewable.

## 4. Gemini Enterprise configuration (copy-ready)

Use this as the agent instruction block in Gemini Enterprise. It is environment-agnostic — paste it, attach your approved source, and it works.

```text
Act as an evidence-disciplined FedEx operations analyst supporting a manager
review of a late-arrival event (wrong-day or right-day).

Use only the approved files and facts provided in this chat. Do not upload
operational data to any unapproved tool.

Decision to support:
[What decision should this briefing enable?]

Scope:
- Operation type: [station / sort hub / P&D / linehaul]
- Reporting period: [exact period]
- Metrics in scope: [list — e.g., commitment met/missed, volume, staffing]

Source rules:
1. Treat the attached report as the source of record.
2. Do not invent, interpolate, or carry values across periods.
3. Do not infer root cause from a variance or correlation.
4. If a value or definition is missing, write "Needs verification."
5. Keep confidential identifiers out. Use approved aggregates and role labels only.

Work in this order:

A. Evidence table
Return columns:
Metric | Period | Scope | Actual | Commitment/Goal | Variance | Source location | Status (confirmed / needs verification) | Manager question

B. Interpretation boundaries
- Confirmed facts
- Possible explanations to investigate (labeled hypotheses)
- Data-quality or definition questions
- Items that must not be concluded from this source

C. Manager artifact
- Executive summary: maximum 5 bullets
- What improved / what needs attention
- 3 prioritized follow-up questions
- Action table: Question/Action | Owner role | Due timing | Evidence needed

D. Quality check
- List every number used and its source location.
- Identify any sentence not directly supported by the evidence table.
- Label the output "DRAFT - MANAGER REVIEW REQUIRED."

Write in plain operational language. Be concise, neutral, non-punitive.
```

## 5. How this maps to what the group already has

| Existing asset | How the baseline uses it |
| --- | --- |
| P32 Feeder/Linehaul Delay Framing | Complementary — P32 frames the delay type; P45/P46 frame the service consequence |
| P01 Daily Manager Brief | The late-arrival cycle feeds into P01 as a priority item |
| P04 After-Action Review | P48 is the specialized version with late-specific columns |
| Smith Agent (Travis Long) | ARR gate + Analyst/Planner/Operator/Auditor loop is the orchestration pattern for any promoted pilot |
| Synthetic-data standard | P45–P48 demos must use synthetic data per that standard |
| SharePoint page template | Upload the late-arrival prompts to the team page alongside P01–P44 |

## 6. What this baseline is NOT

- Not official FedEx policy or a production system.
- Not a claim that any integration is live.
- Not measured ROI — time and quality measures are still to be captured.
- Not permission to paste real operational data into public or unapproved systems.

## 7. Suggested next steps for the group

1. Run one timed before/after trial on a representative late-arrival report (measure median minutes to verified brief).
2. Pick one operation type (station vs sort hub) for the first shadow evaluation.
3. Name owners: business, data, security, governance, evaluation.
4. Decide agency level: explain, recommend, or stage-a-draft.
5. Feed results back into this repo as a dated receipt — what was tried, what was measured, what changed.

## 8. Receipt

- **What ran:** baseline framework authored from public library contents + owner direction (2026-10-01).
- **Inputs:** Ops-AI-Library tree (README, 45-prompt catalog, concepts, governance, SharePoint register, prior meeting briefs); owner approval for full autonomy on this lane.
- **Outputs:** this file + prompts/late-arrival-and-service-recovery.md (P45–P48); catalog updated to 49 prompts.
- **Preserved:** all existing prompts, concepts, Travis Long attributions, governance docs, and SharePoint templates untouched.
- **Not done:** no real FedEx data used; no deploys; no customer contact; no dispatch authority granted.
