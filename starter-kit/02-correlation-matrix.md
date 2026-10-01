# 02 — Correlation Matrix & Black-Swan Signals

**Status:** Candidate pairs for investigation. Every row is a hypothesis template, not a proven relationship. Real correlations must be measured on approved internal data inside approved tools — never computed in this public repo.

**How to use:** When the evidence table (section A of the drop-in packet) is filled, scan this matrix for pairs that moved together. Record the observed pair in the correlation pass (section B). Do not conclude cause.

---

## Metric dictionary (names to align on)

| Metric | Definition used here | Notes |
| --- | --- | --- |
| Commitment met rate | % of commitments delivered on the committed day | Wrong-day = missed day |
| Right-day late rate | % delivered on committed day but outside the window | On-time-but-late-in-window |
| Volume | Packages or stops handled in period | Use ranges/categories if counts are sensitive |
| Total labor hours (TLH) | Sum of component labor intervals | Per the SharePoint register: TLH = Total Labor Hours; packages-per-labor-hour is a separate name |
| Sort interval occupancy | % of sort windows at/near capacity | Synthetic standard uses 15-min grain |
| Equipment down events | Count of equipment-down incidents | Categories only in public material |
| Weather severity band | Public NWS alert/forecast band | Public reference only |
| Staffing variance | Planned vs actual labor hours | Gaps, not individuals |

---

## Candidate correlation pairs

| ID | Pair | Direction to watch | Why it matters | Falsifier |
| --- | --- | --- | --- | --- |
| C1 | Volume ↑ vs commitment met rate ↓ | Inverse | Load pressure hypothesis | Met rate holds under higher volume |
| C2 | TLH variance ↑ vs right-day late rate ↑ | Same direction | Labor gap hypothesis | Lates hold when TLH variance is low |
| C3 | Sort occupancy ↑ vs right-day late rate ↑ | Same direction | Bottleneck hypothesis | Lates independent of occupancy |
| C4 | Equipment down events ↑ vs wrong-day lates ↑ | Same direction | Capacity shock hypothesis | Lates independent of down events |
| C5 | Weather severity band ↑ vs wrong-day lates ↑ | Same direction | External shock hypothesis | Lates independent of weather band |
| C6 | Staffing variance ↑ vs commitment met rate ↓ | Inverse | Coverage hypothesis | Met rate stable across staffing variance |
| C7 | Right-day late rate ↑ vs escalation volume ↑ | Same direction | Customer-risk hypothesis | Escalations flat despite right-day lates |

Each pair is a starting hypothesis. The packet's section B records which pairs actually moved in the period under review.

---

## Black-swan signal checklist

Flag any of these as a **BLACK SWAN CANDIDATE** in section B. A flag means "investigate before acting" — it does not mean "act."

1. Any metric moving more than **two standard deviations** from its period baseline.
2. A value **outside any range seen in the prior comparison period**.
3. A **reversal of a stable trend** (e.g., three periods of improving met rate followed by a sharp drop).
4. **Simultaneous movement** in three or more pairs from the matrix in the same period.
5. A metric that is **missing or undefined** in the source when peers expect it — a data-quality black swan.

For each flagged candidate, section B must state: what moved, by how much, and exactly what would need to be verified (source, definition, freshness) before treating it as signal rather than noise.

---

## What this matrix is not

- Not a statistical model. No coefficients, no p-values, no fitted parameters.
- Not a claim about FedEx's actual internal data.
- Not a substitute for the official metric definitions maintained by data owners.
- Not permission to paste real metric values into this public repository.
