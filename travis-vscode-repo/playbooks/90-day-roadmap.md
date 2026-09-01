# 90-Day Roadmap

Living plan for the Ops AI Library mandate.

## North star

> Non-technical Operations Managers use AI **weekly** for briefs, safety huddles, and metric conversations — safely — with a clear path to SharePoint delivery and measured pilots.

## Days 1–30 — Foundation

| Outcome | Owner type | Evidence |
| --- | --- | --- |
| Repo live with prompts + souls + playbooks | Program | This repository |
| 3 Gemini agents in web UI | Builder | Agents + test pack results |
| Safe use rules socialized | Program | Meeting + Teams post |
| Pilot manager list (5–10) | Ops lead | Named list |
| Feedback form defined | Program | Form link |

## Days 31–60 — Delivery surface

| Outcome | Owner type | Evidence |
| --- | --- | --- |
| SharePoint site skeleton (when access) | Content + IT | Site URL |
| Prompts published with metadata | Content | Library complete |
| Agent Gallery pages | Content | 3 agent cards |
| Power Automate Workflow A design approved | Tech | Design doc sign-off |
| GCP sandbox day-one complete | Data eng | Project hygiene checklist |

## Days 61–90 — Prove value

| Outcome | Owner type | Evidence |
| --- | --- | --- |
| Measured pilot story (time saved / quality) | Program | One-pager with numbers |
| Eval harness v1 on synthetic briefs | Data eng | Pass rate report |
| Workflow B (idea intake) in controlled pilot **if** access | Tech | Flow + human gate |
| Expand to Meeting Scribe + Process Coach | Builder | Agents live |
| Kill or keep decisions documented | Program | Stopped work list |

## Success metrics (program)

| Metric | Target by day 90 |
| --- | --- |
| Active pilot managers using prompts/agents weekly | ≥ 8 |
| Self-reported minutes saved per use | ≥ 10 |
| Incidents of sensitive data paste (known) | 0 critical; process for near-misses |
| Prompts with owner + last reviewed date | 100% of published |
| Autonomous production sends | **0** (by design) |

## Explicit kills (tech debt we are not carrying)

- Treating old dashboards as the product  
- Spec-kit / multi-app monorepo complexity as the front door  
- Research spikes without a manager-facing output  
- “Agentic” marketing without human approval gates  

## Review cadence

- Weekly: 15-minute builder standup (what shipped)  
- Monthly: leadership story (what managers used)  
- Quarterly: prune prompts/agents that nobody uses  
