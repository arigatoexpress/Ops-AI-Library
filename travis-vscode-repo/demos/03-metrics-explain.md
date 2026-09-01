# Demo 03 — Metrics Explainer (2 minutes)

## Setup

Open **Metrics Explainer**, *or* Metrics Interpretation from `prompts/data-and-reporting.md`.

## Paste this (synthetic)

```text
Help interpret these metrics.

Metrics:
- On-time departure rate: 94.2% (prior week 95.1%; target 96%)
- Misload rate: 0.8% (prior week 0.6%; target ≤0.5%)
- Overtime hours (index): 112 vs baseline 100
- Safety observations completed: 18 (prior week 22)

Context:
Night sort, Station A, week ending last Saturday. Synthetic training numbers only.

Return:
- What looks normal
- What looks unusual
- Possible explanations (labeled as hypotheses)
- Follow-up data needed
- Actions that are safe now (information-gathering only)
- Actions that should wait for confirmation

Do not invent missing values. Mark gaps "Needs verification."
```

## What you should see

- Misload and on-time called out as watch items  
- Hypotheses labeled **hypotheses**, not “the cause is…”  
- Information-gathering steps first  
- No invented root cause or staffing orders  

## Facilitator ask

> “What would you verify in the source system before changing the plan?”
