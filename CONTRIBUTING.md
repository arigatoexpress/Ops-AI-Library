# Contributing

## Concept contributions

New operational AI ideas belong under `concepts/` and must use the status model in `concepts/README.md`. State the supported decision, minimum necessary data, prohibited uses, human reviewer, failure modes, evaluation plan, approval needs, and smallest safe pilot.

Concepts may include a small synthetic proof-of-concept only when it demonstrates a contract or guardrail. Do not add production integrations, credentials, real employee/facility data, browser sessions, raw video/audio, or autonomous control logic.

Thank you for helping Operations Managers use AI safely.

## What to contribute

- New or improved **prompts** (update [prompts/CATALOG.md](prompts/CATALOG.md))  
- New or improved **souls**  
- Playbook updates (SharePoint, Power Automate, GCP, Gemini)  
- Synthetic **demos** and before/after examples  
- Plain-English governance clarity  

## What not to contribute

- Secrets, credentials, private URLs with tokens  
- Real customer, employee, package, or route data  
- Unreviewed production automations  
- Large app monorepos that re-center the product away from prompts  

## Style

- Write for a busy **non-technical manager** first.  
- Short sections, copyable examples, checklists.  
- Every AI output framed as a **draft for human review**.  
- Prefer one focused PR per change.  
- See [AGENTS.md](AGENTS.md).

## Prompt checklist

- [ ] Scrubbed placeholders only  
- [ ] “Do not invent facts” (or equivalent)  
- [ ] Output format specified  
- [ ] Needs verification / human review language  
- [ ] Listed in `prompts/CATALOG.md` with ID  
- [ ] Linked from `prompts/README.md` if new category  

## Soul checklist

- [ ] Identity, mission, always/never, output shape  
- [ ] Refusal line for sensitive data  
- [ ] Linked from `souls/README.md` and `gemini-agents/README.md`  

## Demo checklist

- [ ] Synthetic data only  
- [ ] Paste block works stand-alone  
- [ ] “What you should see” quality bar listed  

## Review

Use [governance/project-review-checklist.md](governance/project-review-checklist.md) for anything team-recommended.  
File ideas via GitHub issue templates (prompt / feedback / use case).
