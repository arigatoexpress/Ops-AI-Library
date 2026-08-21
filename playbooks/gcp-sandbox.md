# Playbook: GCP Sandbox (Data Engineering Path)

**Status:** Plan ready for sandbox access.  
**Owner profile:** GCP data engineer supporting the Ops AI Library (not replacing manager prompts).

---

## Purpose of the sandbox

A **safe place to build and measure** data + AI experiments that may later inform:

- Better metric explanations for managers  
- Synthetic datasets for training  
- Evaluation harnesses for prompts/agents  
- Future Vertex AI / Gemini API prototypes  

It is **not** a production FedEx data platform and **not** a place for real package/customer data until classification + approval say so.

---

## Guardrails (non-negotiable)

1. **Public or synthetic data only** until written approval for other classes.  
2. **No secrets** in Git; use Secret Manager / env in sandbox only.  
3. **No production network write-backs.**  
4. Every experiment has: owner, hypothesis, success metric, kill date.  
5. Outputs that managers will see must pass the same **human-in-the-loop** bar as prompts.

---

## Day-one setup checklist

When sandbox access lands:

- [ ] Confirm project ID, billing account, region  
- [ ] Enable APIs only as needed (start small: BigQuery, Cloud Storage, Vertex AI if approved, Logging)  
- [ ] Create least-privilege SA for experiments  
- [ ] Create GCS buckets: `raw-synthetic/`, `curated/`, `exports/`  
- [ ] Create BigQuery dataset: `ops_ai_sandbox`  
- [ ] Set budget alert  
- [ ] Document who has Owner / Editor / Viewer  
- [ ] Clone this repo locally for content; do **not** dump internal data into the public GitHub repo  

---

## First three sandbox projects (ordered)

### 1) Synthetic ops metrics generator

| Field | Spec |
| --- | --- |
| Goal | Produce realistic **fake** weekly KPI series for demos and agent testing |
| Inputs | Parameterized volumes, labor hours, weather flags (synthetic) |
| Outputs | CSV/Parquet in GCS + BigQuery table |
| Why | Managers and Gemini agents need safe example data |
| Success | 12+ months synthetic history; documented field dictionary |

### 2) Prompt / agent eval harness

| Field | Spec |
| --- | --- |
| Goal | Score agent drafts for structure + hallucination risk on fixed fixtures |
| Inputs | Scrubbed fixtures + expected sections (from souls) |
| Outputs | Pass/fail report; no production traffic |
| Why | Improve souls with evidence, not vibes |
| Success | Regression suite for Shift Brief + Metrics Explainer |

### 3) Metric narrative helper (API optional)

| Field | Spec |
| --- | --- |
| Goal | Given **approved aggregate** metrics JSON, produce a structured narrative draft |
| Inputs | Aggregates only (same shape as Metrics Explainer expects) |
| Outputs | JSON: takeaways / hypotheses / verification questions |
| Why | Future SharePoint or Gemini tool integration |
| Success | Beats “blank page” in blind manager preference test on synthetic cases |

---

## What not to build in sandbox first

- Full station digital twin  
- Real-time package tracking pipelines  
- Anything requiring Foundry/internal systems without approval  
- Multi-agent autonomous ops control  

---

## Handoff to managers

Sandbox work becomes valuable when it produces:

1. Better prompts (checked into GitHub)  
2. Better souls (checked into GitHub)  
3. SharePoint data cards (“what this metric means”)  
4. Demo fixtures for training  

If managers cannot use the output without engineering help, it is not done.

---

## Security review packet (keep ready)

For each new dataset or API:

- Data classification  
- Source  
- Retention  
- Access list  
- Network exposure  
- Logging  
- Rollback plan  

Use [../governance/project-review-checklist.md](../governance/project-review-checklist.md).

---

## 60-day target

| Week | Outcome |
| --- | --- |
| 1–2 | Project hygiene + synthetic generator v1 |
| 3–4 | Eval harness on Shift Brief Coach |
| 5–6 | Metrics narrative helper on synthetic aggregates |
| 7–8 | Write-up: what earned a pilot vs what was deleted |
