# Prompt Library

Copy-paste prompts for FedEx Operations Managers who are new to AI.

## Fastest path

**Open [explorer.html](explorer.html)** in your browser.

- Search / filter by category, first-week set, or Gemini agent  
- Fill `[brackets]` with helpers  
- **Sensitivity scan** warns on tracking/PII-like patterns  
- Copy into Gemini Enterprise  
- Nothing is uploaded by this page  

Also:

- [../index.html](../index.html) — offline hub  
- [CATALOG.md](CATALOG.md) — IDs P00–P44  
- [prompts.json](prompts.json) — machine index  
- [../docs/print-pack-first-week.md](../docs/print-pack-first-week.md) — paper version  
- [../demos/](../demos/README.md) — live demos  

## How to use (5 steps)

1. Open the Explorer **or** a category file below.  
2. Copy one prompt.  
3. Replace `[brackets]` with **non-sensitive** notes.  
4. Paste into Gemini (or your approved tool).  
5. Edit the answer before you share or act.

## Categories

| File | Use it for |
| --- | --- |
| [00-how-to-write-prompts.md](00-how-to-write-prompts.md) | Learn the simple formula |
| [daily-operations.md](daily-operations.md) | Shift briefs, handoffs, escalations |
| [safety-and-compliance.md](safety-and-compliance.md) | Huddles, near-miss structure |
| [meeting-and-communication.md](meeting-and-communication.md) | Agendas, action items, emails |
| [data-and-reporting.md](data-and-reporting.md) | Metrics in plain English |
| [process-improvement.md](process-improvement.md) | Root cause, pilots |
| [peak-season-and-surge.md](peak-season-and-surge.md) | Peak planning |
| [linehaul-and-routing.md](linehaul-and-routing.md) | Delay and coordination drafts |
| [customer-and-contractor.md](customer-and-contractor.md) | Scrubbed external-facing drafts |
| [governance-safe-use.md](governance-safe-use.md) | Is this idea safe? |

## First-week set

P01 · P02 · P08 · P15 · P20 · P44

## Rebuild (builders)

```bash
node scripts/build-prompt-index.mjs
node scripts/check-docs.mjs
```
