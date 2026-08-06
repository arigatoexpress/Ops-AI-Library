# Demo 01 — Shift Brief (2 minutes)

## Setup

Open **Shift Brief Coach** in Gemini Enterprise, *or* paste the Daily Manager Brief prompt from `prompts/daily-operations.md`.

## Paste this (synthetic)

```text
Act as a FedEx FEC supervisor or manager preparing a concise daily brief for your station or hub.

Context (scrubbed — no real names, addresses, tracking numbers, or sensitive package counts):
Station: [Station A]
Shift: Night
Day type: Typical midweek
Volume: Slightly above typical for this night (range only — not exact counts)
Staffing: Package handler plan covered; one supervisor floater available
Equipment: One sort belt delayed return from maintenance; scanners OK
Weather: Rain expected after 02:00; dock doors may be wet
Network: Feeder arrival estimated ~30 minutes late (unverified — confirm in system)
Open items: Overflow lot in use; QA asked for extra attention on misloads after last night's near-miss theme (general — no incident IDs)
Safety focus requested: wet floors and three points of contact on equipment

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

## What you should see

- Priorities covering belt, feeder delay, wet dock, overflow, QA focus  
- Feeder timing under **Needs verification**  
- Safety reminder about wet floors  
- No fake package counts or employee names  

## Facilitator ask

> “What would you change before sending this to the next shift?”

Expected answers: confirm feeder ETA in the real system; name real owners; drop anything that does not match tonight.
