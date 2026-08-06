# Safe Use Rules (Plain English)

**Who this is for:** Anyone using prompts or Gemini agents from this library.  
**What this is:** Working team rules. Align with official company policy before treating as authoritative.

---

## Always allowed (with approved tools)

- Rewrite **your own** non-sensitive notes.  
- Draft agendas, checklists, training outlines.  
- Summarize **public** or already-approved training material.  
- Brainstorm process improvements.  
- Improve tone, clarity, and structure of drafts you already own.

---

## Needs review first

Ask before using AI with:

- Customer or package data  
- Employee data  
- Route, station, security, or facility-sensitive information  
- Financial, legal, HR, safety incident, or disciplinary topics  
- External customer or public communication  
- Automation connected to production systems  
- Anything that could move money, send production mail, or change operations without a human

---

## Never paste

- Secrets, passwords, tokens, API keys  
- Real tracking numbers  
- Customer names, addresses, phones, signatures, photos  
- Employee records or performance details  
- Unreleased strategy  
- Private system logs or security procedures  
- Route manifests or GPS traces

### Use placeholders instead

```text
[Station A]
[Shift 2]
[Customer group]
[Volume range — not exact counts if sensitive]
[Issue category]
[Role, not personal name]
```

---

## Human review standard

Before you share or act on AI output:

1. Check facts against the real source system.  
2. Verify names, dates, numbers, and commitments.  
3. Delete unsupported claims.  
4. Label uncertain items **Needs verification**.  
5. Confirm tone fits the audience.  
6. Confirm nothing sensitive leaked into the prompt or the answer.

---

## Manager rule

If the output could affect a person, customer, package, paycheck, safety event, legal position, or production system:

> **A human reviews it, and the right approval path is used.**

AI can prepare the draft. AI does not own the decision.

---

## Agent rule (Gemini / future automations)

Agents in this program:

- May **draft** and **structure**  
- May **ask clarifying questions**  
- May **flag missing data**  
- Must **not** send messages, create tickets, or change systems unless a separate approved workflow and human approval step exist  
- Must **refuse** requests that require forbidden data

See [souls/](../souls/README.md) for how this is encoded in each agent.
