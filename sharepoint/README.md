# SharePoint Content Model

SharePoint is how managers will use this library day to day.  
GitHub remains the engineering/content source of truth until automation exists.

## Paste-ready assets

| Asset | Use |
| --- | --- |
| [home-page-paste.md](home-page-paste.md) | Home page web part copy |
| [prompt-card-template.md](prompt-card-template.md) | Duplicate per published prompt |
| [../docs/manager-wallet-card.md](../docs/manager-wallet-card.md) | Printable / PDF attachment |
| [../demos/](../demos/README.md) | Training page with synthetic demos |

## Page map

Full IA: [playbooks/sharepoint-power-automate.md](../playbooks/sharepoint-power-automate.md)

```text
Home → Start here + Safe use
Prompt Library → cards from template + CATALOG IDs
Agent Gallery → 3 agents first
Workflows → Draft/Pilot/Approved only
Data Cards → classification one-pagers
Training → demos + wallet card
Feedback → form
```

## Content block: Prompt card

See [prompt-card-template.md](prompt-card-template.md). Minimum metadata:

- Category · Audience · Data class · Status · Owner · Last reviewed · Related agent  

## Content block: Agent card

| Field | Example |
| --- | --- |
| Agent name | Shift Brief Coach |
| One-liner | Turns scrubbed notes into shift briefs |
| Open agent | Link (Gemini Enterprise) |
| Soul version | v1.0 date |
| Example inputs | Link to `demos/01-shift-brief.md` |
| Feedback | Form link |

## Publishing checklist

- [ ] Text is non-technical  
- [ ] No real sensitive examples  
- [ ] Status tag set (Draft / Pilot / Approved)  
- [ ] Owner + review date set  
- [ ] Safe use linked  
- [ ] Catalog ID shown (P01…)  

## When access is missing

Continue improving content in GitHub.  
Do not block prompt quality work on SharePoint provisioning.
