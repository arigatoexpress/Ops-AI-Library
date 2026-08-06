# Gemini Agents

We build agents in the **Gemini Enterprise web UI** first.  
Code-first frameworks can wait until there is a clear need and approved platform path.

## Start here

1. Read [playbooks/gemini-enterprise-day-one.md](../playbooks/gemini-enterprise-day-one.md)  
2. Pick a soul from [souls/](../souls/README.md)  
3. Attach matching prompts from [prompts/](../prompts/README.md)  
4. Test with synthetic data only  
5. Pilot with a small manager group  

## Agent catalog (target)

| Agent | Soul | Status |
| --- | --- | --- |
| Shift Brief Coach | shift-brief-coach.md | Build first |
| Safety Huddle Coach | safety-huddle-coach.md | Build first |
| Metrics Explainer | metrics-explainer.md | Build first |
| Meeting Scribe | meeting-scribe.md | Second wave |
| Process Coach | process-coach.md | Second wave |
| Governance Gatekeeper | governance-gatekeeper.md | Second wave |

## Configuration template

Copy into the agent’s description field:

```text
Helps FedEx Operations Managers draft [briefs / safety huddles / metric notes]
from scrubbed notes. Always produces drafts for human review. Never uses
confidential package, customer, or employee data.
```

## Knowledge files

Allowed: blank templates, public training outlines, this library’s markdown.  
Not allowed: real scorecards with sensitive fields, route files, HR data, customer lists.

## Tools / actions

Keep **disabled** until a reviewed Power Automate or platform workflow exists with a human approval step.

## Related

- [SharePoint delivery](../sharepoint/README.md)  
- [Power Automate playbook](../playbooks/sharepoint-power-automate.md)  
- [Human in the loop](../governance/human-in-the-loop.md)
