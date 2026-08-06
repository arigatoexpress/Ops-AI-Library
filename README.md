# Ops AI Library

**AI drafts. You decide.**  
Copy-paste prompts and Gemini agent “souls” so FedEx Operations Managers can use AI safely — without being technical.

> Not a software product. Not official FedEx policy. Not for confidential package/customer/employee data in unapproved tools.

**[Open the hub](index.html)** · **[Prompt Explorer](prompts/explorer.html)** · [GitHub](https://github.com/arigatoexpress/Ops-AI-Library)

---

## Use it in 60 seconds

### Option A — Prompt Explorer (best for managers)

1. Open **[prompts/explorer.html](prompts/explorer.html)** (or [index.html](index.html) → Explorer)  
2. First-week set is pre-filtered — start with **P01 Daily Manager Brief**  
3. Optionally fill brackets · run **sensitivity scan** · **Copy prompt**  
4. Paste into **Gemini Enterprise** → **edit the draft** → share  

Explorer highlights:

- Search + category + agent filters  
- Placeholder fill helpers  
- Blocks copy when tracking/PII-like patterns appear  
- Insert synthetic sample notes for first-week prompts  
- Keyboard: `↑` `↓` navigate · `Ctrl/Cmd+Enter` copy  

### Option B — Print / paper

- [Manager wallet card](docs/manager-wallet-card.md)  
- [First-week print pack](docs/print-pack-first-week.md) (all 6 starter prompts)

### Option C — Meeting demo

[demos/01-shift-brief.md](demos/01-shift-brief.md) · offline sample: [sample-good-output-01](demos/sample-good-output-01.md)

**Also:** [Getting started](docs/getting-started-for-managers.md) · [FAQ](docs/faq.md) · [Meeting one-pager](docs/meeting-one-pager.md) · [15-min workshop](docs/workshop-15-min.md) · [Teams announcement](docs/teams-announcement.md)

---

## Start here

| If you want… | Go here |
| --- | --- |
| Browse & copy prompts | **[prompts/explorer.html](prompts/explorer.html)** |
| Offline hub homepage | [index.html](index.html) |
| Prompt list by ID | [prompts/CATALOG.md](prompts/CATALOG.md) |
| Good vs bad examples | [docs/examples-before-after.md](docs/examples-before-after.md) |
| Safe use + data cards | [governance/safe-use-rules.md](governance/safe-use-rules.md) · [data-cards](governance/data-cards.md) |
| Build Gemini agents | [gemini-agents/](gemini-agents/README.md) · [setup checklist](gemini-agents/agent-setup-checklist.md) |
| SharePoint paste pack | [sharepoint/home-page-paste.md](sharepoint/home-page-paste.md) |
| Power Automate designs | [playbooks/sharepoint-power-automate.md](playbooks/sharepoint-power-automate.md) · [flow specs](playbooks/power-automate-flow-specs.md) |
| GCP sandbox | [playbooks/gcp-sandbox.md](playbooks/gcp-sandbox.md) |
| Pilot metrics | [docs/pilot-scorecard.md](docs/pilot-scorecard.md) |

---

## Mandate

| We build | We do not build here |
| --- | --- |
| Prompt libraries + offline explorer | Dashboard monorepos as the product |
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
node scripts/build-prompt-index.mjs   # rebuild explorer + json after prompt edits
node scripts/check-docs.mjs           # integrity check
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

Day-one: [playbooks/gemini-enterprise-day-one.md](playbooks/gemini-enterprise-day-one.md) · Checklist: [agent-setup-checklist.md](gemini-agents/agent-setup-checklist.md)

---

## Playbooks (access-aware)

| Playbook | Status |
| --- | --- |
| [Gemini Enterprise day-one](playbooks/gemini-enterprise-day-one.md) | **Active now** |
| [SharePoint + Power Automate](playbooks/sharepoint-power-automate.md) | Prepared — waiting on access |
| [Power Automate flow specs A/B/C](playbooks/power-automate-flow-specs.md) | Build-ready specs |
| [GCP sandbox](playbooks/gcp-sandbox.md) | Prepared — sandbox landing |
| [90-day roadmap](playbooks/90-day-roadmap.md) | Living plan |

---

## Safety

1. Protect people, customers, and the company first.  
2. AI = drafts — not unchecked decisions.  
3. Never paste confidential / customer / employee / package / route / security data into unapproved tools.  
4. A human owns every external message and operational decision.  
5. Small pilots with metrics beat vague automation.  

[safe-use-rules](governance/safe-use-rules.md) · [data cards](governance/data-cards.md) · [human-in-the-loop](governance/human-in-the-loop.md)

---

## Repo map

```text
index.html             ← Offline hub homepage
prompts/explorer.html  ← Manager front door (search / scan / copy)
prompts/               ← Markdown source + CATALOG + prompts.json
demos/                 ← Meeting demos + sample good outputs
souls/                 ← Gemini agent personas
gemini-agents/         ← Build guides + setup checklist
playbooks/             ← Gemini, SharePoint/PA, GCP, roadmap
sharepoint/            ← Paste-ready site content
governance/            ← Safe use, data cards, checklists
docs/                  ← Wallet card, FAQ, workshop, print pack
scripts/               ← build-prompt-index + check-docs
appendix/              ← Legacy projects footnote
```

---

## Status

| Area | Status |
| --- | --- |
| Prompt Explorer v1.3 | Active |
| Hub + print pack + workshop | Active |
| Gemini souls + setup checklist | Build in web UI now |
| SharePoint / Power Automate | Specs + paste packs ready |
| GCP sandbox | Plan ready |
| Legacy apps | [Appendix](appendix/prior-example-projects.md) |

---

## Contributing

One prompt, one soul, or one playbook section per change.  
After prompt edits: `node scripts/build-prompt-index.mjs && node scripts/check-docs.mjs`  
[CONTRIBUTING.md](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md) · [CHANGELOG.md](CHANGELOG.md)
