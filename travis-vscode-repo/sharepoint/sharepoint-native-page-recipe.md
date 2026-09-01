# Native SharePoint Page Recipe (Save as Template)

Use this if you want a **real SharePoint site page** (not only the HTML file).  
After you build it once: **Promote as news / Save as page template** (wording varies by tenant).

## Best fast path for non-technical teams

Upload and tab this file instead of rebuilding web parts:

**[ops-ai-library-page-template.html](ops-ai-library-page-template.html)**

1. Upload to a document library  
2. Teams channel → **+** tab → **Website** → paste file link  
3. Tab name: `Ops AI Library`  

That HTML page already has: hero, safe-use banner, 4 steps, six starter prompts with **Copy** buttons.

---

## If you want a native SharePoint page

### Create the page

1. SharePoint site → **New → Page**  
2. Template: **Blank**  
3. Title: `Ops AI Library`  
4. Keep layout simple: one column on mobile-friendly sections  

### Section map (top → bottom)

| # | Section | Web parts | Content |
| --- | --- | --- | --- |
| 1 | Hero | **Text** + **Button** (or Call to action) | Title `Ops AI Library` · subtitle `AI drafts. You decide.` · button “Start with a prompt” |
| 2 | Safety | **Callout** or highlighted **Text** | Do-not-paste list (tracking #s, names, employee data, routes, passwords) |
| 3 | How to use | **Text** or 4 **Quick links** | Scrub → Copy → Paste into Gemini → Edit |
| 4 | Starters | **Text** (or **Accordion** if available) | Full text of P01 P02 P08 P15 P20 P44 — from print pack |
| 5 | Agents | **Quick links** or cards | Shift Brief / Safety Huddle / Metrics Explainer (links when ready) |
| 6 | Feedback | **Text** or **Microsoft Forms** | Minutes saved / what you fixed / invented? |
| 7 | Footer | **Text** | Owner, “not official policy”, GitHub link |

### Exact hero copy

```text
Ops AI Library
AI drafts. You decide.
Copy-paste prompts for Operations Managers — safer briefs, clearer handoffs, less blank-page time.
```

### Exact safety callout

```text
SAFE USE
Do not paste tracking numbers, customer names, employee records, routes, GPS, signatures, or passwords into unapproved tools.
Every AI answer is a DRAFT. You edit it before you share or act.
```

### Starter prompt source

Copy full prompts from:

- [../docs/print-pack-first-week.md](../docs/print-pack-first-week.md)  
- or the HTML template file (already formatted)

### Publish + save as template

1. **Publish** the page  
2. Open page details / promote options  
3. **Save as template** / **Create page template** (if your tenant shows it)  
4. Name: `Ops AI Library — Manager Home`  
5. Next time: **New → Page → from template**

> Not every FedEx tenant exposes “Save as page template.” If missing, keep this published page and **Copy page** when you need another site.

### Add to Teams

1. Channel → **+** → **SharePoint** → pick this page  
   (or **Website** → page URL)  
2. Tab name: `Ops AI Library`  

---

## Permissions

- Team: **Read** (or Member)  
- You / content owner: **Edit**  
- Avoid “Everyone except external” if not intentional  

## Done checklist

- [ ] Page title Ops AI Library  
- [ ] Safety callout visible above the fold  
- [ ] Six starter prompts present  
- [ ] Gemini mentioned as the paste target  
- [ ] Teams tab added  
- [ ] Owner name in footer  
- [ ] No real sensitive examples  
