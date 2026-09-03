# Operational AI Concept Portfolio

This directory converts early ideas into reviewable product proposals. A concept can be valuable without being production-ready; the status labels keep that distinction visible.

## Status model

| Status | Evidence required | Allowed claim |
| --- | --- | --- |
| Concept | Problem, users, proposed inputs/outputs, risks | "Proposed" |
| Synthetic proof of concept | Reproducible synthetic demo and basic tests | "Demonstrated on synthetic data" |
| Validation candidate | Named owner, approved data path, evaluation plan, governance intake | "Ready for controlled validation" |
| Pilot | Written approval, limited users/site, monitoring, rollback, measured baseline | "Pilot in progress" |
| Production | Supported runtime, security review, operations owner, SLOs, incident plan | "Production" |

No file in this directory is production approval.

## Concepts

| Concept | Author | Version / date | Status | Decision it supports |
| --- | --- | --- | --- | --- |
| [Zero-Click Compliance Agent](zero-click-compliance/README.md) | Travis Long | 1.1.0 / 2026-08-21 | Synthetic proof of concept | Which compliance items need review, what approved policy says, and which drafts should be prepared |
| [Virtual Ride-Along Agent](virtual-ride-along-agent.md) | Travis Long | 0.9.1 / 2026-08-26 | Concept | Whether a route segment merits a human-reviewed Unique Characteristics evidence package |
| [EAVA](eava.md) | Travis Long | 2026-08 | Concept | Where flow, density, orientation, or jam risk warrants attention |
| [ACT](act.md) | Travis Long | 2026-08 | Concept | Which reversible intervention should a supervisor consider next |
| [Smith Agent](smith-agent.md) | Travis Long | 1.0 / source received 2026-09-03 | Concept | Whether a recurring workflow has adequate evidence, steps, controls, and proof to advance |

## Shared system view

Read [Integrated Operations Architecture](integrated-operations-architecture.md) for the combined perception, reasoning, action, evidence, and governance model. Use [Smith Agent](smith-agent.md) as the shared orchestration and audit pattern across eligible workflows.

## Required intake for a new concept

Every concept must state:

1. Problem and user.
2. Decision being supported.
3. Minimum necessary inputs and prohibited data.
4. Output and human reviewer.
5. Failure modes and stop conditions.
6. Baseline, success metric, and evaluation window.
7. Security, privacy, safety, labor, legal, and records-review needs.
8. Pilot boundary, rollback, and owner.

## Promotion gate

Before a concept moves beyond synthetic demonstration, complete the [project review checklist](../governance/project-review-checklist.md). For physical operations systems, add a hazard analysis and fail-safe review. For employee-related systems, require HR, privacy, labor, legal, data-owner, and records-retention review before using real records.
