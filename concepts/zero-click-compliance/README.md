# Zero-Click Compliance Agent

**Status:** Synthetic proof of concept / architecture review

**Author:** Travis Long

**Date:** 2026-08-21

**Version:** 1.1.0

## Problem

Managers may need to find approaching compliance deadlines, identify the approved response, and prepare consistent reminders across separate systems. The proposed agent reduces this manual assembly while preserving the manager as the final reviewer.

"Zero-click" describes the target reduction in repetitive handling after an authorized user initiates the workflow. It does not mean bypassing authentication, approval, or review.

## Target workflow

1. The manager asks an approved enterprise agent to audit authorized compliance items.
2. A narrowly scoped connector retrieves only records the manager is permitted to view.
3. Deterministic logic validates dates, status, recipient mapping, and urgency.
4. Agent Search retrieves the relevant approved policy passage with access controls and citations.
5. The system combines the record and policy into a draft action package.
6. Drafts are staged for manager review; nothing is sent automatically.
7. The manager edits, rejects, or approves through the official channel.

## Architecture direction

| Component | Preferred production path | Prototype boundary |
| --- | --- | --- |
| Identity | Contextual enterprise identity and least-privilege service accounts | No credentials stored |
| Compliance source | Approved API or governed export | Synthetic CSV only |
| Browser automation | Controlled fallback after portal-owner approval | Not included in public demo |
| Policy retrieval | Access-controlled Gemini Enterprise / Agent Search data store | No internal policy documents committed |
| Rules | Deterministic date/status/recipient validation | Standard-library Python |
| Drafting | Approved Microsoft 365 integration with Drafts-only permission where possible | Local Outlook draft option, explicit flag, Windows only |
| Audit | Source version, policy citation, rule version, draft hash, reviewer outcome | Local console output |

Google's current documentation calls the search/data-store layer **Agent Search**; earlier names include Vertex AI Search, AI Applications, and Agent Builder. Architecture documents should name the capability and record the deployed product/version rather than assuming one console label.

References:

- https://docs.cloud.google.com/generative-ai-app-builder/docs
- https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es
- https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control

## Prototype

The [prototype](prototype/README.md) is intentionally synthetic and offline by default. It demonstrates the data contract, urgency rules, deterministic message rendering, and optional Drafts-only handoff. It does not log into Workday, reuse browser sessions, read real employee records, or send email.

## Data contract

| Field | Type | Rule |
| --- | --- | --- |
| `employee_display_name` | string | Synthetic placeholder in the public demo |
| `compliance_item` | string | Approved course/control label |
| `days_until_due` | integer | Validated, bounded integer |
| `reviewer_email` | string | `.invalid` address in the public demo |
| `source_as_of` | ISO date | Required for real integrations |
| `source_record_id` | string | Internal-only pseudonymous identifier where approved |

## Security and governance gates

- HR, privacy, labor, legal, records, security, source-system owner, and communications-owner approval.
- No discipline, scheduling, access removal, or employment decision from model output.
- Recipient resolution and authorization checked before a draft is created.
- Policy citations must come from the user-authorized data store and be rechecked after policy updates.
- No master password, token reuse, or session-file commit.
- Draft-only by default; sending requires a separate approved workflow and explicit user confirmation.
- Synthetic fixtures for public tests; real records stay in the approved enterprise boundary.

## Evaluation

Measure precision/recall of due-item detection, date and recipient accuracy, policy citation accuracy, drafts requiring material edits, time to complete the review, false escalations, and user-reported failure cases. Do not claim "80% automated" or "little to no latency" until measured under the approved pilot.
