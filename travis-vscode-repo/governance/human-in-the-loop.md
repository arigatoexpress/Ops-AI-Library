# Human In The Loop

## Why this exists

AI is fast and confident. Operations is high-stakes.  
This page defines **where a person must stay in control**.

## Required human steps

| Step | Person does | AI may help |
| --- | --- | --- |
| Choose the task | Decide what needs doing | Suggest a prompt |
| Provide facts | Pull from approved systems | Structure notes the human pastes |
| Scrub data | Remove sensitive fields | Remind user of rules |
| Review draft | Accept / edit / reject | Self-critique on request |
| Decide | Staffing, safety, customer, legal | Options list only |
| Communicate | Send, post, escalate | Draft language only |
| Record | Log what was used and verified | Generate a checklist of what was checked |

## Agency ladder (keep us honest)

1. **Draft** — AI writes text. Human owns all use. ← *default for this library*  
2. **Recommend** — AI ranks options. Human chooses.  
3. **Prepare action** — AI fills a form or flow **draft**. Human submits.  
4. **Act with approval** — Automation runs after explicit human approval (future Power Automate).  
5. **Act autonomously** — **Out of scope** for this program until governance explicitly allows it.

We live in levels 1–2 today. Level 3–4 only after SharePoint/Power Automate access + approval. Level 5 is not on the roadmap.

## Red flags (stop and escalate)

- AI invents package counts, names, or SLAs.  
- AI encourages skipping safety or policy steps.  
- User wants to paste real tracking/customer data “just this once.”  
- Automation would message customers or contractors without review.  
- Output would be used in discipline, legal, or HR actions without proper channels.
