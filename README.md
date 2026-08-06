# Ops AI Library

**Copy-paste prompts, agent “souls,” and playbooks so FedEx Operations Managers can use AI safely — without needing to be technical.**

This is the clean home for our operations-led AI work.  
Not a software product. Not a production FedEx system.  
**A practical library for busy managers who want better briefs, clearer handoffs, safer experiments, and less time fighting blank screens.**

> **Who this is for:** Station / hub / P&D / linehaul managers and supervisors (FEC and similar roles), continuous-improvement leads, and anyone coaching ops teams on AI.  
> **Who this is *not* for (yet):** Production automation, real customer/package data, or anything that sends messages or changes systems without a human.

---

## Start here (3 minutes)

| If you want to… | Do this |
| --- | --- |
| **Use AI today on a real shift task** | Open [prompts/](prompts/README.md) → pick a category → copy → paste into **Gemini Enterprise** (or another approved tool) → review the draft |
| **Understand the rules in plain English** | Read [Safe use rules](governance/safe-use-rules.md) |
| **Build or tune a Gemini agent** | See [Gemini agents guide](gemini-agents/README.md) + [souls/](souls/README.md) |
| **Plan SharePoint + Power Automate (when access lands)** | Open the [SharePoint & Power Automate playbook](playbooks/sharepoint-power-automate.md) |
| **Plan GCP sandbox work (data / engineering)** | Open the [GCP sandbox plan](playbooks/gcp-sandbox.md) |
| **Prep for today’s leadership meeting** | Read the [Meeting one-pager](docs/meeting-one-pager.md) |

**The only rule that matters on day one:**  
AI drafts. **You** decide. Never paste real tracking numbers, customer names, employee records, routes, or credentials into an unapproved tool.

---

## What we are building (new mandate)

| We build | We do not build (here) |
| --- | --- |
| **Prompt libraries** managers can copy into Gemini | Another dashboard product that needs install/deploy |
| **Soul.md files** (agent personality + guardrails) for Gemini Enterprise agents | Unsupervised agents that act without human review |
| **Playbooks** for SharePoint, Power Automate, and MSFT-licensed workflows | Production Power Automate flows before we have access and approval |
| **Plans** for GCP sandbox + data engineering experiments | Claims that internal data is approved when it is not |
| **Governance checklists** non-technical people can follow | Policy that pretends to be official FedEx policy |

**Success looks like:**  
A manager who is new to AI can open one prompt, get a useful draft in under five minutes, and know exactly what not to paste.

---

## How the pieces fit together

```text
  MANAGER HAS A JOB TO DO
  (shift brief, handoff, safety huddle, metrics note, improvement idea)
                 │
                 ▼
     ┌───────────────────────┐
     │  PROMPT LIBRARY       │  ← copy-paste recipes (this repo)
     │  prompts/             │
     └───────────┬───────────┘
                 │
                 ▼
     ┌───────────────────────┐
     │  GEMINI ENTERPRISE    │  ← web UI agents we can build today
     │  + soul.md personas   │     (souls/ + gemini-agents/)
     └───────────┬───────────┘
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
  HUMAN REVIEW          LATER (when access + approval land)
  always required       • SharePoint library of prompts/souls/data cards
                        • Power Automate agentic workflows (MSFT stack)
                        • GCP sandbox for data engineering experiments
```

Everything in this repo is written so it can be **dropped into SharePoint** later without rewriting the content.

---

## Prompt library (use today)

Prompts are plain English. They work in **Gemini Enterprise**, Copilot, ChatGPT, or Claude — whatever your site has approved.

| Category | What managers use it for |
| --- | --- |
| [How to write a good prompt](prompts/00-how-to-write-prompts.md) | The only skill you need: goal, context, rules, output |
| [Daily operations](prompts/daily-operations.md) | Shift briefs, handoffs, escalations, after-action |
| [Safety & compliance](prompts/safety-and-compliance.md) | Huddles, near-miss drafts, seasonal alerts |
| [Meetings & communication](prompts/meeting-and-communication.md) | Agendas, action items, emails, exec updates |
| [Data & reporting](prompts/data-and-reporting.md) | Metric summaries, “what does this mean?”, data requests |
| [Process improvement](prompts/process-improvement.md) | Root cause, standard work, small pilots |
| [Peak season & surge](prompts/peak-season-and-surge.md) | Pre-peak plans, surge checklists, post-peak review |
| [Linehaul & routing](prompts/linehaul-and-routing.md) | Delay framing, yard notes, coordination drafts |
| [Customer & contractor](prompts/customer-and-contractor.md) | Service notes, ISP briefings (scrubbed) |
| [Governance-safe use](prompts/governance-safe-use.md) | “Is this idea safe?”, review prep, accuracy checks |

**How to use any prompt (5 steps):**

1. Open the category file.  
2. Copy the prompt.  
3. Replace `[brackets]` with **scrubbed** notes (no real sensitive data).  
4. Paste into Gemini Enterprise (or your approved tool).  
5. Review: fix facts, remove guesses, add owners — **then** share.

---

## Agent souls (`soul.md`)

A **soul** is a short file that tells an AI agent *who it is*, *what it may do*, and *what it must never do*.  
When you create a Gemini Enterprise agent in the web UI, paste the matching soul into the system / instructions field.

| Soul | Job |
| --- | --- |
| [Shift Brief Coach](souls/shift-brief-coach.md) | Turns scrubbed notes into pre-shift / handoff / closeout drafts |
| [Safety Huddle Coach](souls/safety-huddle-coach.md) | 2-minute huddle scripts and near-miss structure |
| [Metrics Explainer](souls/metrics-explainer.md) | Plain-English metric interpretation (no invented trends) |
| [Meeting Scribe](souls/meeting-scribe.md) | Agendas, action tables, exec updates |
| [Process Coach](souls/process-coach.md) | Improvement framing and pilot design |
| [Governance Gatekeeper](souls/governance-gatekeeper.md) | Use-case intake and “is this safe?” checks |

See [souls/README.md](souls/README.md) for how to attach souls in Gemini Enterprise.

---

## Playbooks (access landing soon)

We do **not** have full Microsoft Power Automate / production workflow access yet.  
We **do** have Gemini Enterprise (web UI) and are gaining a **GCP sandbox**.  
These playbooks make day one productive instead of chaotic.

| Playbook | Status | Purpose |
| --- | --- | --- |
| [Gemini Enterprise day-one](playbooks/gemini-enterprise-day-one.md) | **Active now** | First agents, naming, testing, rollout |
| [SharePoint + Power Automate](playbooks/sharepoint-power-automate.md) | **Prepared — waiting on access** | Site structure, libraries, agentic flow designs |
| [GCP sandbox](playbooks/gcp-sandbox.md) | **Prepared — sandbox landing** | Safe data experiments for the data-engineer path |
| [90-day roadmap](playbooks/90-day-roadmap.md) | Living plan | What we ship by month |

---

## SharePoint as the front door (design now, configure later)

When Microsoft access is fully available, managers should not need GitHub.  
They should open a **SharePoint page**, pick a prompt or agent card, and run.

Planned structure (full detail in [sharepoint/](sharepoint/README.md)):

```text
SharePoint site: Ops AI Library
├── Home — “Start here” + Safe use rules
├── Prompt Library — one card per prompt (copy button / Word / PDF)
├── Agent Gallery — Gemini agents + soul.md attachments
├── Workflows (future) — Power Automate recipes + status (Draft / Pilot / Approved)
├── Data Cards — what data is allowed, in what tool, by whom
└── Feedback — “this prompt helped / failed” form
```

This repo is the **source of truth** for content. SharePoint is the **delivery surface**.

---

## Safety (non-negotiable)

1. **Protect people, customers, and the company first.**  
2. AI is for **drafts and analysis support** — not unchecked decisions.  
3. **Never paste** confidential, regulated, customer, employee, package, route, security, or proprietary data into public or unapproved tools.  
4. A **human** owns every external message, operational decision, and escalation.  
5. Prefer **small pilots** with clear metrics over big vague automation.  
6. This repo is **not** official FedEx policy and is **not** a production system.

Full version: [governance/safe-use-rules.md](governance/safe-use-rules.md)

---

## Repository map

```text
prompts/           ← Copy-paste prompt library (start here)
souls/             ← Agent personas (soul.md) for Gemini Enterprise
gemini-agents/     ← How to build agents in the Gemini web UI
playbooks/         ← Day-one plans: Gemini, SharePoint/PA, GCP, roadmap
sharepoint/        ← Page layout and content-block design for the site
governance/        ← Safe use, review checklists, human-in-the-loop
docs/              ← Meeting one-pager and plain-English guides
appendix/          ← Prior example projects (legacy footnote only)
```

---

## Status

| Area | Status |
| --- | --- |
| Prompt library | **Active** — ready for managers today |
| Gemini Enterprise agents | **Active** — build in web UI using souls/ |
| SharePoint content model | **Designed** — implement when site permissions allow |
| Power Automate agentic workflows | **Playbook only** — no production flows until access + approval |
| GCP sandbox experiments | **Plan ready** — execute when sandbox lands |
| Old starter apps / dashboards | **Appendix only** — see below |

---

## Appendix — prior example projects (footnote)

Earlier exploration lived in a broader hub that mixed **apps, CLIs, research spikes, and prompts**.  
That mix created tech debt and mixed signals about what this team actually owns.

**New mandate is clear:** prompts, souls, governance, and access-ready playbooks for Operations Managers.

The older example projects (offline KPI tools, metrics CLIs, Cloud Run demos, ADK starter kits, research spikes) remain useful **as historical prototypes**, not as the front door.  
Short index: [appendix/prior-example-projects.md](appendix/prior-example-projects.md)  
Legacy repo: [arigatoexpress/AI-Efficiency](https://github.com/arigatoexpress/AI-Efficiency)

---

## Contributing

- Prefer **one prompt, one soul, or one playbook section** per change.  
- Write for a **busy non-technical manager** first.  
- Never commit secrets, real ops data, or customer/employee information.  
- Details: [CONTRIBUTING.md](CONTRIBUTING.md)

---

*Questions before or after the meeting? Start with the [meeting one-pager](docs/meeting-one-pager.md) or open a GitHub issue.*
