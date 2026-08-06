# SharePoint Content Model

SharePoint is how managers will use this library day to day.  
GitHub remains the engineering/content source of truth until automation exists.

## Page map

See the full IA in [playbooks/sharepoint-power-automate.md](../playbooks/sharepoint-power-automate.md).

## Content block: Prompt card

Each prompt published to SharePoint should include:

| Field | Example |
| --- | --- |
| Title | Daily Manager Brief |
| Category | Daily operations |
| Time to use | 3–5 minutes |
| You need | Scrubbed shift notes |
| You get | Priorities, risks, owners draft |
| Safe use | Link to rules |
| Copy box | Full prompt text |
| Related agent | Shift Brief Coach |
| Owner | Name/role |
| Last reviewed | Date |

## Content block: Agent card

| Field | Example |
| --- | --- |
| Agent name | Shift Brief Coach |
| One-liner | Turns scrubbed notes into shift briefs |
| Open agent | Link (Gemini Enterprise) |
| Soul version | v1.0 date |
| Example inputs | Link to synthetic samples |
| Feedback | Form link |

## Content block: Data card

| Field | Example |
| --- | --- |
| Data name | Weekly efficiency aggregates |
| Classification | Internal (example — confirm with policy) |
| Allowed tools | Approved enterprise AI only |
| Not allowed | Public ChatGPT, personal accounts |
| Contact | Data owner role |

## Publishing checklist

- [ ] Text is non-technical  
- [ ] No real sensitive examples  
- [ ] Status tag set (Draft / Pilot / Approved)  
- [ ] Owner + review date set  
- [ ] Safe use linked  

## When access is missing

Continue improving content in GitHub.  
Do not block prompt quality work on SharePoint provisioning.
