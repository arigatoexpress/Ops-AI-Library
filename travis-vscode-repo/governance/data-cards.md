# Data Cards

One-page rules for “what data may go where.”  
Publish these on SharePoint as **Data Cards**. Confirm against official company policy before treating as authoritative.

---

## Card D1 — Public / training material

| Field | Value |
| --- | --- |
| Examples | Public web pages, public weather summaries, generic training outlines you already own |
| Allowed tools | Approved enterprise AI tools; sometimes public tools if policy allows |
| Not allowed | Treating public web as a substitute for internal systems of record |
| Human review | Still required for anything you send internally as guidance |
| Prompt tip | Ask for sources when researching public topics |

---

## Card D2 — Synthetic / demo data

| Field | Value |
| --- | --- |
| Examples | Fake stations, made-up KPIs, `[Station A]` scenarios in this repo’s demos |
| Allowed tools | Any approved tool used for training |
| Not allowed | Passing synthetic numbers off as real performance |
| Human review | Label demos as synthetic |
| Prompt tip | Start every demo paste with “synthetic training numbers only” |

---

## Card D3 — Internal non-sensitive operations notes

| Field | Value |
| --- | --- |
| Examples | Your own scrubbed shift notes, general equipment status, role-based open items |
| Allowed tools | **Approved enterprise tools only** (e.g., Gemini Enterprise) |
| Not allowed | Public consumer chatbots; personal accounts |
| Human review | Always before share/act |
| Prompt tip | Prefer ranges and categories over exact sensitive counts |

---

## Card D4 — Confidential / regulated / PII

| Field | Value |
| --- | --- |
| Examples | Tracking numbers, customer names/addresses/phones, employee records, route manifests, signatures, GPS traces, credentials, unreleased strategy |
| Allowed tools | **None in this library’s default workflows** until explicit approval for that data class and tool |
| Not allowed | Pasting into Gemini / Copilot / ChatGPT / this repo / SharePoint forms without approval |
| Human review | Use official systems and approved processes only |
| Prompt tip | Replace with placeholders; redesign the use case (Governance Gatekeeper) |

---

## Quick chooser

```text
Is it a real person, package, route, credential, or secret?
  YES → Card D4 (stop / redesign)
  NO  → Is it fake demo data?
          YES → Card D2
          NO  → Is it public?
                  YES → Card D1
                  NO  → Card D3 (enterprise tool + scrub + review)
```

## Related

- [safe-use-rules.md](safe-use-rules.md)  
- [human-in-the-loop.md](human-in-the-loop.md)  
- Prompts: [governance-safe-use.md](../prompts/governance-safe-use.md)  
