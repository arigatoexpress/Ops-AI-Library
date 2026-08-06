# Playbook: SharePoint + Power Automate (Prepare Before Access)

**Status:** Design-ready. **We do not have full access yet.**  
**Goal:** Day one after access is configuration — not brainstorming.

**Related:** [Power Automate flow specs A/B/C](power-automate-flow-specs.md) · [SharePoint paste pack](../sharepoint/README.md)

---

## Why SharePoint is the front door

Managers will not live in GitHub.  
They will open a SharePoint page, pick a prompt or agent card, and work.

| Surface | Role |
| --- | --- |
| **This GitHub repo** | Source of truth for prompts, souls, playbooks, demos |
| **SharePoint** | Manager-facing library, search, ownership, feedback |
| **Power Automate** | Orchestrates drafts + approvals (not unsupervised AI) |
| **Gemini Enterprise** | Where agents reason (web UI today) |
| **Microsoft 365 / Copilot** (if licensed) | Secondary drafting surface using the same prompts |

---

## Phase 0 — Before access (do now)

- [x] Prompt library + catalog in GitHub  
- [x] Soul.md files written  
- [x] Safe use rules written  
- [x] SharePoint home-page paste + card template  
- [x] Power Automate flow specs A/B/C  
- [x] Synthetic demos for training  
- [ ] Nominate **Site Owner** + **Content Owner** + **Tech Owner**  
- [ ] Confirm tenant groups who can view  
- [ ] Confirm Power Automate / Copilot Studio availability + DLP  
- [ ] Align InfoSec / AI governance on data classes  

**Deliverable of Phase 0:** content ready to paste (this repo).

---

## Phase 1 — SharePoint site skeleton (week of access)

### Recommended site name

**Ops AI Library** (or `Ops AI Library — [Region]`)

### Information architecture

```text
Home                    ← paste sharepoint/home-page-paste.md
├── Start here
├── Prompt Library      ← cards from prompt-card-template.md + CATALOG IDs
├── Agent Gallery
├── Workflows           ← Draft / Pilot / Approved only
├── Data Cards
├── Training            ← demos/ + wallet card
└── Feedback
```

### Libraries

| Library | Contents | Versioning |
| --- | --- | --- |
| `Prompts` | One card per prompt | On |
| `Souls` | soul.md copies | On |
| `Data Cards` | Classification one-pagers | On |
| `Playbooks` | Access playbooks | On |
| `Evidence` | Screenshots of tests (no sensitive data) | On |

### Metadata (minimum)

Category · Audience · Data class · Status · Owner · Last reviewed · Gemini agent · Catalog ID (P01…)

---

## Phase 2 — Sync model (GitHub → SharePoint)

| Cadence | Action |
| --- | --- |
| Weekly | Content owner publishes changed prompts/souls |
| On release | Bump last-reviewed metadata |
| Monthly | Archive unused prompts (keep history) |

Later: automate publish with Flow A pattern — still keep **one** source of truth (recommend GitHub for version control, SharePoint as published view).

---

## Phase 3 — Power Automate (design → build)

Full step tables: **[power-automate-flow-specs.md](power-automate-flow-specs.md)**

| Flow | Name | Risk |
| --- | --- | --- |
| A | Prompt of the week publisher | Low |
| B | Idea intake → triage packet | Medium |
| C | Shift brief assist (manager-only draft) | Medium |

### Design principles

1. Human approval before anything leaves the system  
2. No confidential data until classification + tool approval  
3. Gemini/Copilot for drafting; Power Automate for routing/logging  
4. Owner, rollback, kill switch on every flow  
5. Start with notification + approval — never auto-send to customers  

### Explicit non-goals for v1

- Auto-emailing customers  
- Unreviewed production tickets  
- Reading production mailboxes for package data  
- Writing to operational systems of record  

---

## Access checklist (hand to IT)

1. SharePoint site (or creation rights)  
2. Owners + members groups  
3. Power Automate environment + DLP clarity  
4. Permission to call Gemini/Copilot from flows **if** approved  
5. Logging / retention expectations  
6. External sharing blocked (internal only)  

---

## 30-day post-access plan

| Week | Outcome |
| --- | --- |
| 1 | Site live; Safe Use + home page published |
| 2 | Core prompts published with metadata + catalog IDs |
| 3 | Three Gemini agent cards linked |
| 4 | Flow A live; B & C in pilot design review |

---

## Definition of done (SharePoint launch)

- [ ] Manager finds a prompt in under 60 seconds  
- [ ] Safe use linked from every major page  
- [ ] ≥3 agents documented with soul + demo link  
- [ ] Feedback form works  
- [ ] Owners named on home page  
- [ ] No production auto-send flows enabled  
