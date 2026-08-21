# Power Automate — Flow Specs (Build When Access Lands)

These are **implementation specs**, not live flows.  
Every flow stays at agency level: **draft + human approval**. No auto-send to customers.

---

## Shared standards (all flows)

| Standard | Requirement |
| --- | --- |
| Environment | Company-managed Power Platform env only |
| DLP | Confirm connectors allowed (SharePoint, Teams, Gemini/Copilot if approved) |
| Secrets | No API keys in plain compose actions |
| Logging | Run history retained per tenant policy |
| Kill switch | Environment variable `OPS_AI_FLOWS_ENABLED=false` stops triggers |
| Data | Scrubbed / non-sensitive fields only in v1 |
| Naming | `OpsAI-[A\|B\|C]-[Name]-v1` |
| Owner | Named human + backup |

---

## Flow A — Prompt of the Week Publisher

**Name:** `OpsAI-A-PromptOfWeek-v1`  
**Goal:** Post one approved prompt to a Teams channel weekly.

| Step | Action | Notes |
| --- | --- | --- |
| 1 | Trigger: Recurrence (Monday 08:00 local) **or** Manual | Prefer manual for first month |
| 2 | Get item from SharePoint list `PromptQueue` where Status=Ready | List columns: Title, PromptId, Blurb, PromptUrl, Status |
| 3 | Compose Teams message from template | Include Safe Use one-liner |
| 4 | **Start and wait for an approval** (content owner) | If rejected → set Status=Rejected; end |
| 5 | Post message in Teams | Channel: Ops AI Library |
| 6 | Update list item Status=Published + PublishedDate | |
| 7 | Optional: log row to `FlowRuns` list | |

**Success metrics:** posts sent, reactions, feedback form responses.  
**Failure mode:** approval timeout → no post.

**Teams message template:**

```text
📌 Prompt of the week: {{Title}} ({{PromptId}})
{{Blurb}}
Open: {{PromptUrl}}
Rule: AI drafts. You decide. No tracking #s / customer names / employee records.
```

---

## Flow B — Idea Intake → Triage Packet

**Name:** `OpsAI-B-IdeaIntake-v1`  
**Goal:** Capture AI ideas and produce a governance draft for a human reviewer.

| Step | Action | Notes |
| --- | --- | --- |
| 1 | Trigger: When SharePoint form / list item created on `IdeaIntake` | Fields: Idea, Roles, DataCategories (not values), Tool, Submitter |
| 2 | Validate required fields | If missing → comment + stop |
| 3 | Compose Gemini/Copilot prompt using **Governance Gatekeeper** soul text (stored in SharePoint `Souls` library) + form fields | **No raw sensitive data fields on form** |
| 4 | Call approved AI connector **if licensed & allowed**; else create task “Human triage needed” | Branch on connector availability |
| 5 | Write triage packet to `TriagePackets` library | Rating, risks, smallest test, approvals needed |
| 6 | Create approval for governance reviewer | |
| 7 | On approve: set Idea Status=PilotCandidate; on reject: Status=Parked | |
| 8 | Notify submitter of outcome (Teams/email) | |

**Form field rules:** free-text “paste data samples” field is **forbidden**.

**Success metrics:** time-to-first-review, % Red correctly caught in sampling.

---

## Flow C — Shift Brief Assist (Manager-initiated)

**Name:** `OpsAI-C-ShiftBriefAssist-v1`  
**Goal:** Manager-triggered draft; **never auto-posts**.

| Step | Action | Notes |
| --- | --- | --- |
| 1 | Trigger: Manual button / Adaptive Card “Draft shift brief” | Manager only |
| 2 | Input: ScrubbedNotes (multiline) + Shift + StationPlaceholder | Helper text: no PII |
| 3 | Simple regex/keyword scan for patterns like long numeric IDs | If hit → return “Scrub first” message; do not call AI |
| 4 | Call AI with Shift Brief Coach soul + notes | Draft only |
| 5 | Return draft **only to the runner** (chat/email to self) | No channel post in v1 |
| 6 | Log metadata only (user, timestamp, length) — **not** note contents if policy forbids | Prefer no content logging in v1 |

**Success metrics:** self-reported minutes saved; optional thumbs up/down.  
**Non-goal:** sending the brief to a team channel automatically.

---

## Acceptance tests (run before “Pilot” tag)

| Flow | Test |
| --- | --- |
| A | Rejected approval does not post |
| A | Kill switch stops schedule |
| B | Idea with “tracking numbers” in text is not auto-approved |
| B | Reviewer can park idea |
| C | Keyword scan blocks obvious tracking-like strings |
| C | Output returns only to initiator |

---

## Build order after access

1. SharePoint lists/libraries from [sharepoint-power-automate.md](sharepoint-power-automate.md)  
2. Flow A (lowest risk)  
3. Flow C (high manager value, still draft-only)  
4. Flow B (needs governance reviewer capacity)  
