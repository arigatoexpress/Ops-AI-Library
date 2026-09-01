# Gemini Enterprise Agent Setup Checklist

Print or keep open while building agents in the web UI.

## Before you start

- [ ] You have Gemini Enterprise access  
- [ ] You will use **synthetic / scrubbed** test notes only  
- [ ] Soul files available from `souls/`  

## Build each agent

### 1) Shift Brief Coach

- [ ] Name: `Shift Brief Coach`  
- [ ] Description: `Drafts shift briefs and handoffs from scrubbed notes. Human review required.`  
- [ ] Instructions: paste full [souls/shift-brief-coach.md](../souls/shift-brief-coach.md)  
- [ ] Starters: P01, P02 from explorer  
- [ ] Tools/actions: **OFF**  
- [ ] Access: builders + pilot managers only  
- [ ] Test: [demos/01-shift-brief.md](../demos/01-shift-brief.md)  
- [ ] Version note: `v1.0 — YYYY-MM-DD`  

### 2) Safety Huddle Coach

- [ ] Name: `Safety Huddle Coach`  
- [ ] Description: `2-minute safety huddle scripts. No real incident details.`  
- [ ] Instructions: paste [souls/safety-huddle-coach.md](../souls/safety-huddle-coach.md)  
- [ ] Starters: P08, P11  
- [ ] Tools/actions: **OFF**  
- [ ] Test: [demos/02-safety-huddle.md](../demos/02-safety-huddle.md)  

### 3) Metrics Explainer

- [ ] Name: `Metrics Explainer`  
- [ ] Description: `Plain-English metric interpretation. No invented trends.`  
- [ ] Instructions: paste [souls/metrics-explainer.md](../souls/metrics-explainer.md)  
- [ ] Starters: P20, P23  
- [ ] Tools/actions: **OFF**  
- [ ] Test: [demos/03-metrics-explain.md](../demos/03-metrics-explain.md)  

## After build

- [ ] Sample outputs reviewed by a second person  
- [ ] Linked from SharePoint Agent Gallery (when site exists)  
- [ ] Feedback path shared with pilots  
- [ ] Review date set (+90 days)  

## Do not enable yet

- Email send  
- Ticket create  
- Production system write-back  
- Knowledge uploads of real scorecards with PII  
