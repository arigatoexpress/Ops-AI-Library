# Ops AI Library

**AI drafts. You decide.**  
Copy-paste prompts and Gemini agent “souls” so FedEx Operations Managers can use AI safely — without being technical.

> Not a software product. Not official FedEx policy. Not for confidential package/customer/employee data in unapproved tools.

**[Open the hub](index.html)** · **[Prompt Explorer](prompts/explorer.html)** · **[SharePoint page template](sharepoint/ops-ai-library-page-template.html)** · [GitHub](https://github.com/arigatoexpress/Ops-AI-Library)

---

## Use it in 60 seconds

### Option A — SharePoint / Teams (best for your team site)

1. Upload **[sharepoint/ops-ai-library-page-template.html](sharepoint/ops-ai-library-page-template.html)** to a SharePoint library  
2. Teams channel → **+** → **Website** tab → paste the file link  
3. Managers open the tab → **Copy prompt** → paste into Gemini → edit  

Recipe: [sharepoint/sharepoint-native-page-recipe.md](sharepoint/sharepoint-native-page-recipe.md)

### Option B — Prompt Explorer

1. Open **[prompts/explorer.html](prompts/explorer.html)**  
2. Start with **P01 Daily Manager Brief**  
3. Copy → Gemini Enterprise → edit draft  

### Option C — Print / paper

- [Manager wallet card](docs/manager-wallet-card.md)  
- [First-week print pack](docs/print-pack-first-week.md)

**Also:** [Getting started](docs/getting-started-for-managers.md) · [FAQ](docs/faq.md) · [Meeting one-pager](docs/meeting-one-pager.md) · [Teams announcement](docs/teams-announcement.md)

---

## Start here

| If you want… | Go here |
| --- | --- |
| SharePoint / Teams page (upload & go) | **[sharepoint/ops-ai-library-page-template.html](sharepoint/ops-ai-library-page-template.html)** |
| Browse & copy prompts offline | [prompts/explorer.html](prompts/explorer.html) |
| Offline hub homepage | [index.html](index.html) |
| Prompt list by ID | [prompts/CATALOG.md](prompts/CATALOG.md) |
| Safe use + data cards | [governance/safe-use-rules.md](governance/safe-use-rules.md) · [data-cards](governance/data-cards.md) |
| Build Gemini agents | [gemini-agents/](gemini-agents/README.md) · [setup checklist](gemini-agents/agent-setup-checklist.md) |
| Power Automate designs | [playbooks/sharepoint-power-automate.md](playbooks/sharepoint-power-automate.md) |
| GCP sandbox | [playbooks/gcp-sandbox.md](playbooks/gcp-sandbox.md) |

---

## Mandate

| We build | We do not build here |
| --- | --- |
| Prompt libraries + offline explorer + SharePoint page | Dashboard monorepos as the product |
| Soul.md guardrails for Gemini | Unsupervised auto-send agents |
| SharePoint / Power Automate / GCP **playbooks** | Fake “workflows are live” claims |
| Demos, workshop, print packs | Official FedEx policy cosplay |

**Success:** a new manager gets a useful draft in under five minutes and knows what never to paste.

---

## Prompt library

| Category | Use for |
| --- | --- |
| [How to write prompts](prompts/00-how-to-write-prompts.md) | Simple formula |
| [Daily operations](prompts/daily-operations.md) | Briefs, handoffs, escalations |
| [Safety & compliance](prompts/safety-and-compliance.md) | Huddles, near-miss structure |
| [Meetings & communication](prompts/meeting-and-communication.md) | Agendas, actions, emails |
| [Data & reporting](prompts/data-and-reporting.md) | Metrics in plain English |
| [Process improvement](prompts/process-improvement.md) | Root cause, pilots |
| [Peak season & surge](prompts/peak-season-and-surge.md) | Peak planning |
| [Linehaul & routing](prompts/linehaul-and-routing.md) | Delay framing |
| [Customer & contractor](prompts/customer-and-contractor.md) | Scrubbed external drafts |
| [Governance-safe use](prompts/governance-safe-use.md) | “Is this safe?” |

**45 prompts** · [CATALOG](prompts/CATALOG.md) · [prompts.json](prompts/prompts.json)  
**First-week set:** P01 · P02 · P08 · P15 · P20 · P44  

```bash
node scripts/build-prompt-index.mjs
node scripts/check-docs.mjs
```

---

## Agent souls (Gemini Enterprise)

| Soul | Job |
| --- | --- |
| [Shift Brief Coach](souls/shift-brief-coach.md) | Briefs / handoffs / closeouts |
| [Safety Huddle Coach](souls/safety-huddle-coach.md) | 2-minute safety scripts |
| [Metrics Explainer](souls/metrics-explainer.md) | Numbers without invented causes |
| [Meeting Scribe](souls/meeting-scribe.md) | Agendas & action tables |
| [Process Coach](souls/process-coach.md) | Improvement + pilot design |
| [Governance Gatekeeper](souls/governance-gatekeeper.md) | Green / Yellow / Red checks |

---

## Safety

1. Protect people, customers, and the company first.  
2. AI = drafts — not unchecked decisions.  
3. Never paste confidential / customer / employee / package / route / security data into unapproved tools.  
4. A human owns every external message and operational decision.  
5. Small pilots with metrics beat vague automation.  

---

## Status

| Area | Status |
| --- | --- |
| SharePoint page template (HTML) | Active — upload to blank site |
| Prompt Explorer + first-week pack | Active |
| Gemini souls | Build in web UI now |
| Power Automate | Specs ready when access lands |
| Legacy apps | [Appendix](appendix/prior-example-projects.md) |

---

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md) · [CHANGELOG.md](CHANGELOG.md)
