# Linehaul And Routing Prompts

Draft coordination language only. Do not paste real manifests, trailer numbers tied to sensitive routes, GPS traces, or customer addresses.

## Feeder / Linehaul Delay Framing

```text
Help me frame a delay update for internal coordination.

Delay type: [weather / traffic / equipment / network / other]
General impact: [e.g., "inbound late; outbound may compress"]
What is already known (scrubbed):
[notes]

Return:
- Situation (2 sentences)
- Operational impact (sort / P&D / customer risk — general)
- Actions already taken
- Decisions needed (roles)
- Info still missing
- Suggested next check-in time (if known)

Neutral tone. No blame. Draft only.
```

## Yard / Dock Coordination Notes

```text
Turn these scrubbed notes into a yard/dock coordination brief.

Notes:
[Paste non-sensitive notes about congestion, door availability, trailer status in general terms.]

Return:
- Current state (bullets)
- Bottlenecks
- Prioritized actions (next 60–90 minutes)
- Who needs to know (roles)
- Safety watch-outs

Do not invent door counts or trailer IDs.
```

## Alternate Plan Discussion (Advisory)

```text
Help structure an alternate plan discussion. Advisory only — no dispatch authority.

Constraint:
[Describe constraint without sensitive identifiers.]

Options under consideration:
[List option A/B/C in general terms.]

Return a comparison table:
Option | Benefit | Risk | Dependencies | Verification needed

Remind: final plan must follow approved dispatch and network procedures.
```

## P&D Density / Coverage Conversation Starter

```text
Create talking points for a P&D density/coverage discussion using scrubbed context.

Context:
[General volume/shape notes — no addresses or stop lists]

Return:
- 5 discussion questions for the team
- 3 data points to pull from official systems before decisions
- Common misinterpretations to avoid
- Safety and customer-service considerations

Do not generate routes or stop sequences.
```
