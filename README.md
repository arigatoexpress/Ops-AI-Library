# Ops AI Library

**AI drafts. You decide.**  
Copy-paste prompts and Gemini agent “souls” so FedEx Operations Managers can use AI safely — without being technical.

> Not a software product. Not official FedEx policy. Not for confidential package/customer/employee data in unapproved tools.

---

## Use it in 60 seconds

### Option A — Prompt Explorer (best for managers)

1. Open **[prompts/explorer.html](prompts/explorer.html)** in any browser (works offline after download)  
2. Pick **P01 Daily Manager Brief** (or search)  
3. Edit the brackets → **Copy prompt** → paste into **Gemini Enterprise**  
4. **Edit** the AI draft → then share  

### Option B — Meeting demo pack

Open **[demos/01-shift-brief.md](demos/01-shift-brief.md)** (synthetic — safe to paste) and run it live.

Print the rules: **[Manager wallet card](docs/manager-wallet-card.md)**  
New manager path: **[Getting started](docs/getting-started-for-managers.md)** · **[FAQ](docs/faq.md)**  
Leadership meeting: **[Meeting one-pager](docs/meeting-one-pager.md)** · **[15-min workshop](docs/workshop-15-min.md)**  
Announce to the team: **[Teams / email paste](docs/teams-announcement.md)**

---

## Start here

| If you want… | Go here |
| --- | --- |
| Browse & copy prompts (offline UI) | **[prompts/explorer.html](prompts/explorer.html)** |
| Prompt list by ID | [prompts/CATALOG.md](prompts/CATALOG.md) |
| See good vs bad examples | [docs/examples-before-after.md](docs/examples-before-after.md) |
| Sample “good” brief output | [demos/sample-good-output-01.md](demos/sample-good-output-01.md) |
| Safe use rules | [governance/safe-use-rules.md](governance/safe-use-rules.md) |
| What data may go where | [governance/data-cards.md](governance/data-cards.md) |
| Build a Gemini agent | [gemini-agents/](gemini-agents/README.md) + [souls/](souls/README.md) |
| SharePoint page copy | [sharepoint/home-page-paste.md](sharepoint/home-page-paste.md) |
| Power Automate designs | [playbooks/sharepoint-power-automate.md](playbooks/sharepoint-power-automate.md) · [flow specs](playbooks/power-automate-flow-specs.md) |
| GCP sandbox plan | [playbooks/gcp-sandbox.md](playbooks/gcp-sandbox.md) |
| Measure a pilot | [docs/pilot-scorecard.md](docs/pilot-scorecard.md) |
| Plain-English terms | [docs/glossary.md](docs/glossary.md) |

---

## Mandate (what this repo is)

| We build | We do not build here |
| --- | --- |
| **Prompt libraries** managers can copy | Another install/deploy dashboard product |
| **Offline explorer** for non-GitHub users | Unsupervised agents that act without review |
| **Soul.md** guardrails for Gemini Enterprise | Fake claims that MSFT workflows are already live |
| **Playbooks** for SharePoint, Power Automate, GCP | Production automation |
| **Demos, workshop, announcements** | “Official FedEx policy” cosplay |

**Success:** a new manager gets a useful draft in under five minutes and knows what never to paste.

---

## Prompt library

| Category | Use for |
| --- | --- |
| [How to write prompts](prompts/00-how-to-write-prompts.md) | The simple formula |
| [Daily operations](prompts/daily-operations.md) | Briefs, handoffs, escalations, closeouts |
| [Safety & compliance](prompts/safety-and-compliance.md) | Huddles, near-miss structure, seasonal alerts |
| [Meetings & communication](prompts/meeting-and-communication.md) | Agendas, actions, emails, exec updates |
| [Data & reporting](prompts/data-and-reporting.md) | Metrics in plain English |
| [Process improvement](prompts/process-improvement.md) | Root cause, standard work, pilots |
| [Peak season & surge](prompts/peak-season-and-surge.md) | Pre-peak, surge, post-peak |
| [Linehaul & routing](prompts/linehaul-and-routing.md) | Delay framing, yard notes |
| [Customer & contractor](prompts/customer-and-contractor.md) | Scrubbed external-facing drafts |
| [Governance-safe use](prompts/governance-safe-use.md) | “Is this safe?”, review prep |

**45 prompts** in [CATALOG.md](prompts/CATALOG.md) · machine index [prompts.json](prompts/prompts.json)  
**First-week set:** P01 · P02 · P08 · P15 · P20 · P44  

After editing prompt markdown, rebuild explorer/json:

```bash
node scripts/build-prompt-index.mjs
```

---

## Agent souls (Gemini Enterprise)

| Soul | Job |
| --- | --- |
| [Shift Brief Coach](souls/shift-brief-coach.md) | Pre-shift / handoff / closeout drafts |
| [Safety Huddle Coach](souls/safety-huddle-coach.md) | 2-minute safety scripts |
| [Metrics Explainer](souls/metrics-explainer.md) | Numbers without invented causes |
| [Meeting Scribe](souls/meeting-scribe.md) | Agendas, action tables, exec updates |
| [Process Coach](souls/process-coach.md) | Improvement + pilot design |
| [Governance Gatekeeper](souls/governance-gatekeeper.md) | Green / Yellow / Red use-case checks |

Build order: [playbooks/gemini-enterprise-day-one.md](playbooks/gemini-enterprise-day-one.md)

---

## How the pieces fit

```text
Manager job → Explorer or prompt → Gemini agent (soul) → Human review → Share / act
                              │
                              └─ later: SharePoint front door
                                        Power Automate (approvals, not auto-send)
                                        GCP sandbox (synthetic / approved data)
```

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

## Safety (non-negotiable)

1. Protect people, customers, and the company first.  
2. AI = drafts and analysis support — not unchecked decisions.  
3. Never paste confidential / customer / employee / package / route / security data into unapproved tools.  
4. A human owns every external message and operational decision.  
5. Small pilots with metrics beat vague automation.  

Full: [safe-use-rules](governance/safe-use-rules.md) · [data cards](governance/data-cards.md) · [human-in-the-loop](governance/human-in-the-loop.md)

---

## Repo map

```text
prompts/explorer.html  ← Offline UI for managers (start here)
prompts/               ← Markdown source + CATALOG + prompts.json
demos/                 ← Live meeting demos + sample good output
souls/                 ← Agent personas for Gemini Enterprise
gemini-agents/         ← How to build agents in the web UI
playbooks/             ← Gemini, SharePoint/PA, GCP, roadmap
sharepoint/            ← Paste-ready page + card templates
governance/            ← Safe use, data cards, review checklists
docs/                  ← Wallet card, FAQ, workshop, announcements
scripts/               ← Rebuild explorer/json from markdown
appendix/              ← Prior example projects (footnote only)
```

---

## Status

| Area | Status |
| --- | --- |
| Prompt Explorer + catalog | Active |
| Demos + wallet card + workshop | Active |
| Gemini agents (souls) | Build in web UI now |
| SharePoint content model | Paste-ready |
| Power Automate | Specs only until access + approval |
| GCP sandbox | Plan ready |
| Old starter apps | [Appendix only](appendix/prior-example-projects.md) |

---

## Appendix — prior example projects

Earlier work mixed apps, CLIs, and research into one hub. Useful for learning; wrong front door for managers.  
[appendix/prior-example-projects.md](appendix/prior-example-projects.md) · legacy: [AI-Efficiency](https://github.com/arigatoexpress/AI-Efficiency)

---

## Contributing

Prefer one prompt, one soul, or one playbook section per change.  
Rebuild explorer after prompt edits: `node scripts/build-prompt-index.mjs`  
No secrets. No real ops data. [CONTRIBUTING.md](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md) · [CHANGELOG.md](CHANGELOG.md)
