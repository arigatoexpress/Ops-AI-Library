# How To Write A Good Prompt

You do not need to be technical. If you can explain a task to a sharp assistant, you can write a useful prompt.

## The formula

```text
Goal:
Context:
Source:
Rules:
Output:
```

| Part | Meaning |
| --- | --- |
| **Goal** | What you want done |
| **Context** | Who it is for and why it matters |
| **Source** | What information the AI should use (scrubbed) |
| **Rules** | What it must not do |
| **Output** | Format you want back |

## Weak vs strong

**Weak**

```text
Summarize this.
```

**Strong**

```text
Goal: Summarize these scrubbed shift notes.
Context: Incoming station supervisor needs the handoff in under 2 minutes.
Source: Use only the notes below.
Rules: Do not invent facts. Put missing details under "Needs verification."
Output: 5 bullets, then a table: Owner | Action | Due | Risk.

Notes:
[paste scrubbed notes]
```

## Six moves that always help

1. **Give a role** — `Act as a practical FEC supervisor or manager.`  
2. **Give a clear task** — `Turn these notes into a shift handoff.`  
3. **Name the audience** — `Write for a senior manager who needs the key points quickly.`  
4. **Set boundaries** — `Use only the notes provided. Do not add new facts.`  
5. **Force uncertainty** — `Create a section called "Needs verification."`  
6. **Specify format** — `Return a table with columns: Issue, Impact, Owner, Next Step.`

## Follow-ups (after the first answer)

```text
Make this shorter.
```

```text
List anything that sounds like an unsupported claim.
```

```text
Turn this into a checklist with checkboxes.
```

```text
Review your answer. Flag assumptions and items that need human verification.
```

## Manager template (blank)

```text
Act as a practical FEC supervisor or manager.

I need help with:
[task]

Audience:
[who will read this]

Source material (scrubbed — no real tracking, customer, or employee data):
[paste notes]

Rules:
- Use only the source material.
- Do not invent facts.
- Keep it concise.
- Flag uncertainty under "Needs verification."
- Do not include sensitive data in the answer.

Output format:
[bullets / table / email / checklist / one-page brief]
```

## Common mistakes

- Vague asks (“make this better”)  
- Pasting sensitive context “because it’s faster”  
- Forgetting the audience  
- Accepting the first answer without review  
- Letting AI make commitments you did not approve  
- Asking AI to **decide** instead of **prepare a decision**
