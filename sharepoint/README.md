# SharePoint Content Model

SharePoint (or a Teams tab pointing at SharePoint) is how managers use this library day to day.  
GitHub remains the source of truth for builders.

## Start here (blank site / non-technical team)

| Asset | Use |
| --- | --- |
| **[ops-ai-library-page-template.html](ops-ai-library-page-template.html)** | **Best option:** upload + Teams Website tab. Ready-made manager page with Copy buttons. |
| [sharepoint-native-page-recipe.md](sharepoint-native-page-recipe.md) | Rebuild as a native SharePoint page / save as template |
| [home-page-paste.md](home-page-paste.md) | Section copy if building web parts by hand |
| [prompt-card-template.md](prompt-card-template.md) | Expand beyond the first 6 prompts later |
| [../docs/manager-wallet-card.md](../docs/manager-wallet-card.md) | Printable rules |
| [../docs/print-pack-first-week.md](../docs/print-pack-first-week.md) | Six starter prompts as paper/PDF |

## 10-minute setup

1. Download `ops-ai-library-page-template.html` from this folder (or repo ZIP).  
2. SharePoint → document library → **Upload**.  
3. Teams channel → **+** tab → **Website** → paste the file link.  
4. Name the tab **Ops AI Library**.  
5. Post the welcome message in the channel.

## Page map (if you grow beyond one page)

```text
Home / template page   ← managers live here
├── Start here
├── Prompt Library     ← expand after week 1
├── Agent Gallery
├── Safe use
├── Training
└── Feedback
```

## Publishing checklist

- [ ] Non-technical language  
- [ ] No real sensitive examples  
- [ ] Safe use visible without hunting  
- [ ] First-week prompts available without GitHub  
- [ ] Owner + last reviewed date  

## When Power Automate access arrives

Use [../playbooks/sharepoint-power-automate.md](../playbooks/sharepoint-power-automate.md) — do not block the simple page on automation.
