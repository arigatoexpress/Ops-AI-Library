# Gemini Enterprise Use Case - Interview Preparation

**Working story:** From operational reports to a verified manager brief and reusable AI workflow

**Interview audience:** Data & AI Enablement, Google technical validation, Citizen Learner CoP, and executive sponsors

**Status:** Draft for Ari, Edrie, and the AI Efficiency Group to personalize

## One-sentence story

We used Gemini Enterprise to turn approved operational reports and structured notes into a concise, source-grounded manager briefing workflow, then converted the technique into reusable prompts, agent instructions, and governance controls that other managers can follow.

## Introduction and the before state

### Role and team

Suggested answer:

> We work close to frontline operations and focus on turning recurring operational friction into safer, repeatable AI-assisted workflows. Our AI Efficiency Group combines process knowledge with citizen development: we identify the decision a manager needs to make, structure the evidence, create a reusable workflow, and keep the manager in control.

### Before Gemini

Suggested answer:

> A weekly performance review meant opening a dashboard or exported PDF, moving through a large multi-tab KPI workbook, finding the relevant measures, comparing actuals with goals and prior periods, writing a narrative, and checking that the summary did not imply a cause the data could not prove. The hard part was not copying a number; it was converting a dense report into a clear, defensible conversation while keeping source, metric definition, and uncertainty straight.

Manual steps to describe:

1. Open the approved report and select the correct period, organization, and facility level.
2. Locate the relevant productivity, service, safety, compliance, and people measures.
3. Reconcile actual, goal, variance, trend, and data freshness.
4. Identify questions without guessing at root cause.
5. Draft the manager brief and meeting agenda.
6. Recheck each claim against the source and remove sensitive details before reuse.

### Time and friction - measure before the interview

Do not estimate from memory. Run the same representative report three times under the old and new workflow.

| Measure | Before | With Gemini | Evidence |
| --- | ---: | ---: | --- |
| Median minutes to first complete draft | [measure] | [measure] | Screen recording or timer log |
| Median minutes to verified final brief | [measure] | [measure] | Timer log plus checklist |
| Claims requiring correction | [count] | [count] | Review worksheet |
| Required sections present | [count / total] | [count / total] | Output rubric |

Use the measured median, not the best run. Keep first-draft time separate from verified-final time.

## The solution and the aha moment

### Aha moment

Suggested answer:

> The aha moment was realizing Gemini did not need to be the system of record or calculate our official metrics. It was most useful as the translation and reasoning interface around approved source material. We kept calculations and authoritative values in the source, then made Gemini show its work: separate facts from interpretations, cite where each claim came from, flag missing context, and return the exact decision artifact a manager needs.

### Current workflow

1. Use an approved export or file in Gemini Enterprise; do not upload data to an unapproved tool.
2. State the decision, audience, period, metric definitions, and output format.
3. Require an evidence table before the narrative.
4. Require facts, hypotheses, and missing verification to be separate.
5. Review every number and claim against the source.
6. Save only the scrubbed, reusable prompt pattern and agent behavior - not the operational data - in the public library.

### Unique technique: evidence-first reverse engineering

The technique combines two moves:

1. **Reverse-engineer the manager artifact.** Start from the briefing or decision table the manager must leave with, not from a vague request to "analyze this file."
2. **Force an evidence pass before prose.** Gemini must build a claim/source/period/status table, identify missing context, and only then draft the executive summary.

This reduces fluent but unsupported narratives and makes review faster.

## Master prompt

Copy and adapt only inside an approved enterprise environment.

```text
Act as an evidence-disciplined operations performance analyst supporting a
manager review. Use only the approved files and facts provided in this chat.

Decision to support:
[What decision or discussion should this briefing enable?]

Audience:
[Roles, not personal names]

Scope:
- Organization level: [network / region / district / location]
- Reporting period: [exact period]
- Comparison period: [exact prior period, if available]
- Metrics in scope: [list]

Source rules:
1. Treat the attached dashboard/PDF/workbook as the source of record for this task.
2. Do not invent, interpolate, or carry values across periods or organization levels.
3. Do not infer a root cause from a variance or correlation.
4. If a value, definition, freshness date, or comparison is missing, write
   "Needs verification" and state exactly what is missing.
5. Keep confidential identifiers out of the response. Use approved aggregates
   and role labels only.

Work in this order:

A. Evidence table
Return columns:
Metric | Period | Scope | Actual | Goal/Benchmark | Variance | Source location |
Status (confirmed / needs verification) | Manager question

B. Interpretation boundaries
- Confirmed facts
- Possible explanations to investigate (clearly labeled hypotheses)
- Data-quality or definition questions
- Items that must not be concluded from this source

C. Manager brief
- Executive summary: maximum 5 bullets
- What improved
- What needs attention
- Cross-metric tensions or tradeoffs
- 3 prioritized follow-up questions
- Action table: Question/Action | Owner role | Due timing | Evidence needed

D. Quality check
- List every number used in the brief and its source location.
- Identify any sentence that is not directly supported by the evidence table.
- Label the output "DRAFT - MANAGER REVIEW REQUIRED."

Write in plain operational language. Be concise, neutral, and non-punitive.
```

## Business impact and after state

### Biggest benefit

Suggested answer:

> The biggest benefit is not only faster drafting. It closes a translation gap between a dense operational source and a consistent manager conversation. The workflow improves completeness, makes uncertainty visible, gives us a repeatable quality check, and lets more team members produce a strong first draft without pretending the model is the source of truth.

### What it enables

- More time for verification, coaching, and decisions instead of formatting.
- A consistent briefing structure across users and periods.
- Reusable prompts and agent instructions instead of one-off chats.
- Safer handoffs because the source and uncertainty are explicit.
- A path from prompt to governed agent without changing the human accountability model.

Avoid saying the workflow improved an operational KPI unless a controlled measurement shows that link. Report time, quality, adoption, and decision-cycle measures separately from facility performance.

## Three-step replicable takeaway

1. **Define the decision and the exact output.** Give Gemini a table, brief, checklist, or agenda to build.
2. **Ground it in approved sources and force an evidence table.** Facts first; prose second.
3. **Verify, edit, and save the pattern.** Check every claim, remove sensitive data, and reuse the prompt or agent instructions.

## Advice for a hesitant user

> Start with a task where you already know what a good answer looks like. Give Gemini approved source material, constrain the output, and ask it to show which source supports every claim. You are not giving up control; you are creating a faster first draft that is easier to inspect.

## Technical validation notes

Be precise with Google:

- The current workflow is Gemini Enterprise-assisted source synthesis and human review.
- The reusable assets are prompts, agent instructions, rubrics, and governance patterns.
- Deterministic metrics remain in source systems or validated code; Gemini explains them.
- A future RAG path may use access-controlled Agent Search data stores and narrowly scoped tools after approval.
- Do not claim live integrations, automated email sending, production camera inference, or autonomous operational control unless they are actually deployed and measured.

## Interview checklist

- [ ] Choose one exact representative report/workflow.
- [ ] Capture three before and three after timing trials.
- [ ] Bring one scrubbed before/after example.
- [ ] Confirm which data/file type was approved for Gemini Enterprise.
- [ ] Rehearse the master prompt in the approved environment.
- [ ] Decide which metrics can be shared externally and at what aggregation.
- [ ] Agree on Ari/Edrie speaking roles.
- [ ] Ask for review of the communications bundle before broad publication.
