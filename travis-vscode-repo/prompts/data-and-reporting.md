# Data And Reporting Prompts

Use only non-sensitive extracts or synthetic examples unless your tool is approved for the data class.

## Report Summary

```text
Summarize this report for an FEC supervisor or manager.

Report text or non-sensitive extract:
[Paste text.]

Return:
- 5 key takeaways
- What changed from the prior period, if known
- Risks
- Recommended questions (not final decisions)
- Questions to ask the data owner

Do not invent trends that are not visible in the text.
```

## Metrics Interpretation

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

## Data Request Draft

```text
Draft a clear data request for an analyst or data partner.

Business question:
[What are we trying to answer?]

Decision it supports:
[What decision depends on this?]

Return:
- Requested fields (categories, not real values)
- Time period
- Filters
- Granularity
- Privacy / sensitivity concerns
- Why each field is needed
- Suggested summary output format
```

## Dashboard Feedback

```text
Review this dashboard description for manager usefulness.

Dashboard description:
[Paste description or field list.]

Return:
- What decisions it supports
- What is confusing
- Missing filters or context
- Metrics that need definitions
- Suggested layout improvements
- Risks of misinterpretation
```

## “Explain This Number” For A Non-Technical Audience

```text
Explain this metric in plain English for someone new to the report.

Metric name: [name]
Value: [value]
Period: [period]
Target or comparison (if any): [target]

Return:
- One-sentence definition
- Why operations cares
- What a good vs concerning movement looks like (general)
- Two questions a manager should ask before acting
- Reminder to verify against the source system

Do not invent history that was not provided.
```
