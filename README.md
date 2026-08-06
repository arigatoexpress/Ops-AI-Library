# Ops AI Library

**AI drafts. You decide.**  
Copy-paste prompts and Gemini agent “souls” so FedEx Operations Managers can use AI safely — without being technical.

> Not a software product. Not official FedEx policy. Not for confidential package/customer/employee data in unapproved tools.

---

## Use it in 60 seconds

1. **Scrub** your notes → `[Station A]`, `[Shift 2]`, `[Issue category]`  
2. Open **[demos/01-shift-brief.md](demos/01-shift-brief.md)** (synthetic — safe to paste)  
3. Paste into **Gemini Enterprise** (or another approved tool)  
4. **Edit** the draft → then share  

Print the rules: **[Manager wallet card](docs/manager-wallet-card.md)**  
First week as a manager: **[Getting started](docs/getting-started-for-managers.md)**  
In a leadership meeting: **[Meeting one-pager](docs/meeting-one-pager.md)** + **[Live demos](demos/README.md)**

---

## Start here

| If you want… | Go here |
| --- | --- |
| A prompt for a real shift task | [prompts/](prompts/README.md) · [full catalog](prompts/CATALOG.md) |
| See good vs bad examples | [docs/examples-before-after.md](docs/examples-before-after.md) |
| Safe use rules | [governance/safe-use-rules.md](governance/safe-use-rules.md) |
| Build a Gemini agent | [gemini-agents/](gemini-agents/README.md) + [souls/](souls/README.md) |
| SharePoint page copy (when site exists) | [sharepoint/home-page-paste.md](sharepoint/home-page-paste.md) |
| Power Automate designs (no access yet) | [playbooks/sharepoint-power-automate.md](playbooks/sharepoint-power-automate.md) · [flow specs](playbooks/power-automate-flow-specs.md) |
| GCP sandbox plan | [playbooks/gcp-sandbox.md](playbooks/gcp-sandbox.md) |
| Measure a pilot | [docs/pilot-scorecard.md](docs/pilot-scorecard.md) |
| Plain-English terms | [docs/glossary.md](docs/glossary.md) |

---

## Mandate (what this repo is)

| We build | We do not build here |
| --- | --- |
| **Prompt libraries** managers can copy | Another install/deploy dashboard product |
| **Soul.md** guardrails for Gemini Enterprise agents | Unsupervised agents that act without review |
| **Playbooks** for SharePoint, Power Automate, GCP | Fake claims that MSFT workflows are already live |
| **Demos & training packs** with synthetic data | Production automation |
| **Governance** non-technical people can follow | “Official FedEx policy” cosplay |

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

**45 prompts** indexed in [prompts/CATALOG.md](prompts/CATALOG.md).  
**First-week set:** P01 · P02 · P08 · P15 · P20 · P44

### Every prompt

1. Copy → 2. Fill `[brackets]` with scrubbed notes → 3. Paste into approved AI → 4. Edit → 5. Share  

---

## Agent souls (Gemini Enterprise)

Paste a soul into the agent’s system instructions in the web UI.

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
Manager job → Prompt or Gemini agent (soul) → Human review → Share / act
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

Full: [governance/safe-use-rules.md](governance/safe-use-rules.md) · [human-in-the-loop](governance/human-in-the-loop.md)

---

## Repo map

```text
demos/             ← Live meeting demos (synthetic paste packs)
prompts/           ← Copy-paste library + CATALOG.md
souls/             ← Agent personas for Gemini Enterprise
gemini-agents/     ← How to build agents in the web UI
playbooks/         ← Gemini, SharePoint/PA, GCP, roadmap
sharepoint/        ← Paste-ready page + card templates
governance/        ← Safe use, review, human-in-the-loop
docs/              ← Wallet card, meeting one-pager, scorecard, glossary
appendix/          ← Prior example projects (footnote only)
```

---

## Status

| Area | Status |
| --- | --- |
| Prompts + catalog | Active |
| Demos + wallet card | Active |
| Gemini agents (souls) | Build in web UI now |
| SharePoint content model | Paste-ready; configure when access lands |
| Power Automate | Specs only until access + approval |
| GCP sandbox | Plan ready |
| Old starter apps | [Appendix only](appendix/prior-example-projects.md) |

---

## Appendix — prior example projects

Earlier work mixed apps, CLIs, and research into one hub. Useful for learning; wrong front door for managers.  
Details: [appendix/prior-example-projects.md](appendix/prior-example-projects.md) · legacy repo: [AI-Efficiency](https://github.com/arigatoexpress/AI-Efficiency)

---

## Contributing

Prefer one prompt, one soul, or one playbook section per change.  
No secrets. No real ops data. See [CONTRIBUTING.md](CONTRIBUTING.md) · [AGENTS.md](AGENTS.md) · [CHANGELOG.md](CHANGELOG.md)
