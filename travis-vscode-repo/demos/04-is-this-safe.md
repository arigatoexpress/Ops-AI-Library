# Demo 04 — Is This Safe? (2 minutes)

## Setup

Open **Governance Gatekeeper**, *or* use “Is This Safe To Try?” from `prompts/governance-safe-use.md`.

## Paste this (synthetic idea)

```text
I want to use AI for this task. Tell me if it is safe as described.

Task:
Automatically draft a customer delay email from our live tracking system and send it without a manager reading it.

Tool I plan to use:
Public consumer chatbot on a phone

Data I would provide:
Real tracking numbers, customer names, and addresses

Return:
- Green / Yellow / Red rating
- Why
- Safer alternative if Red or Yellow
- Minimum human review step
- What approval I should seek before piloting
```

## What you should see

- **Red** (or strong Yellow at best — should be Red)  
- Safer alternative: scrubbed internal draft → human send from approved channel  
- Clear “do not paste PII into public tools”  

## Contrast (optional second paste) — should be Green/Yellow

```text
Task: Turn my own scrubbed shift notes into a handoff checklist.
Tool: Gemini Enterprise
Data: Placeholders only — no tracking numbers or names
```

## Facilitator ask

> “Where is the human gate in the safer version?”
