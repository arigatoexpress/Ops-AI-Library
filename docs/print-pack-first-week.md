# First-Week Print Pack

Print or PDF this for managers who prefer paper.  
**Rule:** AI drafts. You decide. No tracking #s, customer names, employee records, or routes in unapproved tools.

---

## How to use each day

| Day | Prompt | Minutes |
| --- | --- | --- |
| Mon | P01 Daily Manager Brief | 5 |
| Tue | P02 Shift Handoff | 5 |
| Wed | P08 Safety Huddle | 3 |
| Thu | P15 Notes → Action Items | 5 |
| Fri | P20 Metrics Interpretation | 8 |
| Anytime | P44 Is This Safe To Try? | 5 |

Scrub notes first: `[Station A]` · `[Shift 2]` · `[Issue category]` · `[Volume range]`

---

## P01 — Daily Manager Brief

```text
Act as a FedEx FEC supervisor or manager preparing a concise daily brief for your station or hub.

Context (scrubbed — no real names, addresses, tracking numbers, or sensitive package counts):
[Paste non-sensitive shift notes, volume ranges, staffing notes, weather summary,
equipment notes, and known constraints.]

Create a daily brief with:
- Top 5 priorities for this shift
- Risks to watch (weather, road, equipment, staffing)
- Sort hub / P&D / linehaul coordination notes
- Decisions needed and who should make them (roles, not personal names)
- Owner and next step for each item

Rules:
- Do not invent facts.
- Put unclear items under "Needs verification."
- Keep it under 300 words.
- Include a safety reminder.
- Label the whole output as a draft for manager review.
```

---

## P02 — Shift Handoff

```text
Turn these non-sensitive notes into a shift handoff for the incoming supervisor or manager.

Outgoing shift: [Day/Evening/Night]
Incoming shift: [Day/Evening/Night]
Tone: direct, calm, and action-oriented

Notes (scrubbed):
[Paste notes. Remove all real names, addresses, tracking numbers, and package details.]

Return:
1. What changed since the last handoff
2. What is still open
3. High-risk items (safety, customer, linehaul)
4. Who owns each next step (roles, not names)
5. What to check first in the next shift
6. One safety reminder

Do not invent facts. Use "Needs verification" where details are missing.
```

---

## P08 — Pre-Shift Safety Huddle

```text
Act as a safety-focused FEC supervisor or manager preparing a 2-minute huddle brief.

Station: [Station name or code — if non-sensitive]
Shift: [Day/Evening/Night]
Season/Conditions: [e.g., winter ice, summer heat, rain]
Known equipment status: [e.g., all scanners functional, 2 dollies out for repair]

Return:
- 1 safety focus for this shift
- 1 quick check everyone should do before starting
- 1 reminder about PPE or equipment inspection
- 1 "see something, say something" prompt
- End with: "Safety Above All. Questions before we start?"

Keep it under 150 words. Direct, respectful language.
Do not include real employee names or past incident details.
```

---

## P15 — Meeting Notes To Action Items

```text
Convert these meeting notes into action items.

Notes (scrubbed):
[Paste non-sensitive notes.]

Return a table:
Owner (role) | Action | Due date | Dependency | Risk if missed

If owner or due date is missing, write "Needs assignment" or "Needs date."
Do not invent owners or deadlines.
```

---

## P20 — Metrics Interpretation

```text
Help interpret these metrics.

Metrics:
[Paste non-sensitive metric names and values.]

Context:
[Describe time period and operation in general terms.]

Return:
- What looks normal
- What looks unusual
- Possible explanations (labeled as hypotheses)
- Follow-up data needed
- Actions that are safe now (information-gathering only)
- Actions that should wait for confirmation

Do not invent missing values. Mark gaps "Needs verification."
```

---

## P44 — Is This Safe To Try?

```text
I want to use AI for this task. Tell me if it is safe as described.

Task:
[Describe task.]

Tool I plan to use:
[Gemini Enterprise / other approved tool / unknown]

Data I would provide:
[Categories only]

Return:
- Green / Yellow / Red rating
- Why
- Safer alternative if Red or Yellow
- Minimum human review step
- What approval I should seek before piloting
```

---

## End-of-week feedback (send to pilot owner)

- Minutes saved this week: ___  
- Best prompt: ___  
- Anything invented by AI: ___  
- Would use again: Y / N  

Full library: Prompt Explorer (`prompts/explorer.html`) or github.com/arigatoexpress/Ops-AI-Library
