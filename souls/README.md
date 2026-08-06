# Agent Souls (`soul.md`)

A **soul** is the personality + guardrails for an AI agent.  
Paste it into Gemini Enterprise when you create or edit an agent (system instructions / custom instructions).

## Why souls exist

| Without a soul | With a soul |
| --- | --- |
| Manager re-explains rules every chat | Rules live with the agent |
| Tone drifts | Consistent “ops coach” voice |
| Easy to invent facts | Hard-coded “do not invent” |
| Safety is optional | Safety is default |

## How to attach in Gemini Enterprise (web UI)

1. Open Gemini Enterprise → create or edit an agent.  
2. Open **Instructions / System instructions** (wording varies by UI version).  
3. Paste the full contents of a soul file.  
4. Optionally pin 1–2 example prompts from [../prompts/](../prompts/README.md).  
5. Test with **synthetic** notes only.  
6. Share with a small pilot group before broad rollout.

## Catalog

| File | Best for |
| --- | --- |
| [shift-brief-coach.md](shift-brief-coach.md) | Daily briefs, handoffs, closeouts |
| [safety-huddle-coach.md](safety-huddle-coach.md) | Pre-shift safety scripts |
| [metrics-explainer.md](metrics-explainer.md) | Plain-English metric interpretation |
| [meeting-scribe.md](meeting-scribe.md) | Agendas, action tables, exec updates |
| [process-coach.md](process-coach.md) | Improvement and pilot design |
| [governance-gatekeeper.md](governance-gatekeeper.md) | Use-case intake and safety checks |

## Soul format (standard)

Every soul includes:

1. **Identity** — who the agent is  
2. **Mission** — what success looks like  
3. **Always do**  
4. **Never do**  
5. **Output shape**  
6. **Escalation language** — when to refuse or ask for scrubbing  

When you create a new soul, copy an existing file and edit — do not invent a new structure.
