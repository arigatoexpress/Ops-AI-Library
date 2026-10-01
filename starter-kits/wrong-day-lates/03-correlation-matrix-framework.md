# 03 — Correlation Matrix Framework

**Purpose:** A repeatable method for finding which tracked metrics move together around late-arrival events, flagging outliers as hypotheses (never causes), and turning both into recommended next steps. This is analysis methodology — it does not fix anything by itself, and it does not claim that plugging AI in solves the operational problem.

---

## What this is for

Wrong-day and right-day lates have many tracked metrics behind them: volume, staffing, equipment status, weather, feeder arrival times, sort start times, P&D density, and more. The framework helps a manager see which pairs co-move, which single points are outliers, and what the smallest safe next check is for each.

## Step 1 — Define the metric set (approved sources only)

List the metrics you actually track, with definitions and owners. Example categories (adapt to your operation):

| Category | Example metrics | Source |
| --- | --- | --- |
| Volume | Packages processed, stops completed | Approved ops report |
| Staffing | Headcount by role, overtime hours | Approved staffing report |
| Equipment | Belt/chute uptime, trailer availability | Approved equipment log |
| Network | Feeder arrival variance, linehaul delays | Approved network report |
| Service | Commitment met/missed rate, right-day late count | Approved service report |

**Rule:** If a metric's definition or owner is unknown, it goes in "Needs verification" — it is not used in the matrix.

## Step 2 — Build the co-movement table

For each metric pair over the same period:

| Metric A | Metric B | Co-movement | Period | Status |
| --- | --- | --- | --- | --- |
| [e.g., feeder late arrivals] | [e.g., wrong-day lates] | move together / opposite / no clear link | [period] | confirmed / needs verification |

**Status meanings:**
- **Confirmed:** the co-movement is visible in the source data.
- **Needs verification:** the comparison is incomplete, definitions differ, or the window is too short.

## Step 3 — Flag outliers as hypotheses only

An outlier is a single data point that breaks the pattern. Flag it, label it a hypothesis, and never treat it as a cause. Example: "Feeder 3 arrived 40 minutes late on Tuesday while wrong-day lates spiked — hypothesis: feeder delay contributed; verify against the feeder log."

## Step 4 — Recommend next steps

For each confirmed co-movement and each flagged outlier, recommend the smallest reversible check:

| Finding | Recommended next step | Owner role | Evidence needed |
| --- | --- | --- | --- |
| [co-movement or outlier] | [one concrete check] | [role] | [what would confirm or deny] |

## Step 5 — What not to do

- Do not claim causation from correlation.
- Do not recommend operational changes (reroutes, staffing moves) from this framework alone.
- Do not paste real metric values into public prompts or this repo.
- Do not skip the "Needs verification" column.

## How Gemini uses this

Attach this file plus an approved metric export. The agent instruction block in 01-gemini-enterprise-pack.md includes a correlation-pass output template. The agent ranks pairs, flags outliers, and recommends next steps — all labeled as hypotheses pending verification.
