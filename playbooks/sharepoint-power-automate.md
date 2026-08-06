# Playbook: SharePoint + Power Automate (Prepare Before Access)

**Status:** Design-ready. **We do not have full access yet.**  
**Goal:** Day one after access is configuration — not brainstorming.

---

## Why SharePoint is the front door

Managers will not live in GitHub.  
They will open a SharePoint page, pick a prompt or agent card, and work.

| Surface | Role |
| --- | --- |
| **This GitHub repo** | Source of truth for prompts, souls, playbooks |
| **SharePoint** | Manager-facing library, search, ownership, feedback |
| **Power Automate** | Future workflows that *orchestrate* drafts + approvals (not unsupervised AI) |
| **Gemini Enterprise** | Where agents actually reason (web UI today) |
| **Microsoft 365 / Copilot** (if licensed) | Secondary drafting surface using the same prompts |

---

## Phase 0 — Before access (do now)

- [x] Prompt library written in GitHub  
- [x] Soul.md files written  
- [x] Safe use rules written  
- [ ] Nominate **Site Owner** + **Content Owner** + **Tech Owner**  
- [ ] Confirm tenant: which M365 group / security groups can view  
- [ ] Confirm whether Copilot Studio / Power Automate premium features will be available  
- [ ] Align with InfoSec / AI governance on data classes allowed in SharePoint vs Gemini  

**Deliverable of Phase 0:** this playbook + content ready to paste.

---

## Phase 1 — SharePoint site skeleton (week of access)

### Recommended site name

**Ops AI Library** (or region-specific: `Ops AI Library — [Region]`)

### Information architecture

```text
Home
├── Start here (3 steps + safe use summary)
├── Prompt Library
│   ├── Daily operations
│   ├── Safety
│   ├── Meetings
│   ├── Data & reporting
│   ├── Peak & surge
│   ├── Linehaul
│   ├── Customer & contractor
│   └── Governance
├── Agent Gallery
│   ├── Gemini agent cards (link + soul attachment)
│   └── How to request a new agent
├── Workflows (Power Automate)
│   ├── Draft / Pilot / Approved status tags
│   └── Runbooks per flow
├── Data Cards
│   └── What data, which tool, who may use
├── Training
│   └── 15-minute manager onboarding
└── Feedback
    └── Form: helped / failed / idea
```

### Libraries (document libraries)

| Library | Contents | Versioning |
| --- | --- | --- |
| `Prompts` | One page or file per prompt (export from repo) | On |
| `Souls` | soul.md copies for agents | On |
| `Data Cards` | Classification one-pagers | On |
| `Playbooks` | This file + GCP + Gemini day-one | On |
| `Evidence` | Screenshots of successful tests (no sensitive data) | On |

### Content types / metadata (minimum)

- Category  
- Audience (role)  
- Data class allowed  
- Status: Draft / Pilot / Approved  
- Owner  
- Last reviewed date  
- Gemini agent name (if linked)

### Home page modules

1. **Hero:** “AI drafts. You decide.” + link to Safe Use.  
2. **Do this today:** 3 featured prompts.  
3. **Agents:** cards for Shift Brief Coach, Safety Huddle, Metrics Explainer.  
4. **What’s new:** monthly update list.  
5. **Report a problem** button.

---

## Phase 2 — Sync model (GitHub → SharePoint)

Until automation exists:

| Cadence | Action |
| --- | --- |
| Weekly | Content owner copies changed prompts/souls from GitHub to SharePoint |
| On release | Bump “Last reviewed” metadata |
| Monthly | Archive outdated prompts (don’t delete history) |

**Later automation (when Power Automate access exists):**

- Flow: “When file committed / when manual button pressed → create SharePoint page from markdown”  
- Or: store canonical files in SharePoint and mirror to GitHub for engineering — pick **one** source of truth (recommend GitHub for version control, SharePoint as published view)

---

## Phase 3 — Power Automate agentic workflows (design only until access)

### Design principles

1. **Human approval before anything leaves the system** (email, Teams post, ticket).  
2. **No confidential data** in flows until classification + tool approval.  
3. **Gemini / Copilot for drafting; Power Automate for routing and logging.**  
4. **Every flow has an owner, a rollback, and a kill switch.**  
5. Start with **notification + approval**, not auto-send.

### First three workflows to build when access lands

#### Workflow A — “Prompt of the week” publisher

| Item | Spec |
| --- | --- |
| Trigger | Manual or weekly schedule |
| Steps | Pick approved prompt from SharePoint library → post to Teams channel → log views |
| AI? | Optional: generate a 1-sentence “why try this” from public description only |
| Human gate | Content owner approves post body |
| Success metric | Clicks / feedback form responses |

#### Workflow B — “Idea intake → triage packet”

| Item | Spec |
| --- | --- |
| Trigger | SharePoint form or Teams message to a channel |
| Steps | Create list item → call Gemini/Copilot with **Governance Gatekeeper** soul on scrubbed fields → write triage packet to SharePoint → assign reviewer |
| AI? | Yes — draft only |
| Human gate | Governance reviewer accepts/rejects before any broader share |
| Success metric | Time from idea to first review decision |

#### Workflow C — “Shift brief assist (manager-initiated)”

| Item | Spec |
| --- | --- |
| Trigger | Manager clicks “Draft brief” button / Adaptive Card |
| Steps | Manager pastes **scrubbed** notes → Gemini with Shift Brief Coach soul → return draft to manager only → manager copies to email/Teams manually |
| AI? | Yes — draft only |
| Human gate | Manager always edits; **no auto-post** in v1 |
| Success metric | Self-reported time saved; quality feedback |

### Explicit non-goals for v1

- Auto-emailing customers  
- Auto-creating production tickets with AI-written content unreviewed  
- Reading production mailboxes for package data  
- Writing to operational systems of record  

---

## Phase 4 — Microsoft-licensed agent stack (when available)

Possible components (availability varies by tenant):

| Component | Use |
| --- | --- |
| SharePoint | Content + permissions |
| Power Automate | Orchestration + approvals |
| Copilot Studio | Packaged agents with enterprise controls (if licensed) |
| Teams | Delivery surface for managers |
| Dataverse / Lists | Intake logs, feedback, audit |
| Purview labels | Classification on libraries |

**Decision rule:** Prefer the tool IT already supports. Do not invent a parallel shadow stack.

---

## Access checklist (hand to IT / platform)

When requesting access, ask for:

1. SharePoint site creation rights (or a provisioned site).  
2. Owners group + members group for Ops AI Library.  
3. Power Automate environment (default + DLP policy clarity).  
4. Permission to call Gemini Enterprise / Copilot from flows **if** that integration is approved.  
5. Logging / retention expectations.  
6. Whether external sharing is blocked (should be: **internal only**).

---

## 30-day post-access plan

| Week | Outcome |
| --- | --- |
| 1 | Site live, IA complete, Safe Use page published |
| 2 | All core prompts published with metadata |
| 3 | Three Gemini agent cards + souls linked |
| 4 | Workflow A live (publisher); B & C in pilot design review |

---

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Managers paste sensitive data into forms | Big red Safe Use banner; form field hints; DLP where available |
| Drift between GitHub and SharePoint | Single content owner; weekly sync; last-reviewed dates |
| Shadow IT automations | Only Approved-tagged flows; kill switch; environment DLP |
| Overpromising “agentic” | Agency ladder: draft → recommend → prepare → act-with-approval |

---

## Definition of done (SharePoint launch)

- [ ] Non-technical manager can find a prompt in under 60 seconds  
- [ ] Safe use rules linked from every major page  
- [ ] At least 3 agents documented with soul + example  
- [ ] Feedback form works  
- [ ] Owners named on the home page  
- [ ] No production auto-send flows enabled
