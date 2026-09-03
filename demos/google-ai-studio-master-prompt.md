# Google AI Studio One-Shot Master Prompt

Paste the entire prompt below into **Google AI Studio Build mode**. It is designed to create a polished, self-contained demonstration without private data or mandatory external services.

## Master prompt

```text
Build a complete, polished, presentation-ready web application named “Ops AI Control Tower — Synthetic Demonstration.” Generate the actual working application now. Do not return a plan, ask clarifying questions, leave TODOs, create dead buttons, or require a second prompt.

PRIMARY OUTCOME
Create one coherent demonstration of an operations AI portfolio. It must show how governed AI can combine public-reference context with deterministic synthetic operational data, route work through a Smith Agent orchestration loop, and prepare human-reviewed recommendations and drafts. This is a concept demonstration—not an official product, policy, production system, or statement of measured performance.

TECHNICAL BASELINE
- Build a responsive React + TypeScript single-page application using the environment’s supported toolchain.
- Use clean, modular components and strict TypeScript types.
- Use the current supported Google GenAI SDK and the Interactions API only if the environment already provides secure Gemini access. Never expose an API key in client code.
- The core demo must work with no network, no API key, and no backend through deterministic local generators and precomputed example narratives.
- If Gemini is available, add an optional “AI synthesis” toggle. Gemini may summarize the current synthetic evidence into a structured recommendation, but it may not send messages, control equipment, make employee decisions, or claim a tool was called when it was not.
- For AI output, require a JSON schema with: summary, confirmedFacts[], assumptions[], risks[], recommendations[], citations[], confidence, humanDecisionRequired, and prohibitedActions[]. Validate the response and fall back to the deterministic output if validation fails.
- Use a seeded pseudorandom generator. Default seed: OPS-DEMO-20260903. Provide Regenerate, Reset, Play Scenario, Pause, and Export controls.
- Avoid huge embedded data literals. Generate the requested data at runtime and memoize it.
- Use accessible semantic HTML, keyboard navigation, visible focus, WCAG-friendly contrast, reduced-motion support, and responsive layouts.

TRUST AND SAFETY REQUIREMENTS
Persist this banner on every screen:
“SYNTHETIC DEMONSTRATION — Not live operations, measured performance, official policy, or a production system. Human review required.”

Never generate or request:
- real employee/customer names, emails, IDs, addresses, tracking numbers, route manifests, VINs, facility codes, private links, credentials, biometrics, faces, license plates, raw audio, or raw video;
- FedEx logos, trade dress, or claims of endorsement;
- a claim that an email was sent, a ticket was submitted, a route was changed, equipment was controlled, or a policy decision was made.

Use neutral fictional identifiers: SYN-FAC-001, ZONE-A, SYN-RT-0001, SYN-WRK-0001, and example.invalid email addresses. Label every figure as one of PUBLIC REFERENCE, MODELED ASSUMPTION, or SYNTHETIC EVENT. Put the label in chart tooltips and detail drawers.

INFORMATION ARCHITECTURE
Create a left navigation rail and top command bar with these sections:
1. Executive Control Tower
2. Smith Agent
3. EAVA + ACT + ROM
4. Zero-Click Compliance
5. VRAA Route Evidence
6. Inspection Center
7. TLH Survey
8. OTS Reporting
9. Resource Registry
10. Data Lab & Governance

The first load must open on Executive Control Tower with a fully populated “Winter Mountain Morning” scenario. Include scenario presets: Normal Day, Winter Mountain Morning, Late Inbound + Compressed Sort, Staffing Variance, Sensor Degradation, and Compliance Deadline Wave.

VISUAL DESIGN
- Professional operations-command-center aesthetic: warm off-white canvas, dark navy surfaces, restrained violet accent, amber warning, green verified, red stop.
- Do not imitate a specific company brand.
- Use a dense but readable 12-column dashboard, crisp typography, small status chips, generous detail drawers, and meaningful whitespace.
- Include animated signal flow and event replay, but respect reduced-motion settings.
- Use charts appropriate to the data: sparklines, stacked area for flow, line/target bands for labor, heat map for occupancy, scatter plot for speed vs vibration, and a timeline for agent runs.
- Every chart needs a plain-language interpretation beneath it. Never rely on color alone.

GLOBAL DATA MODEL AND PROVENANCE
Every table must support these provenance fields even if they are hidden until a row is expanded:
record_id, scenario_id, event_time, generated_at, generator_version, seed, evidence_class, source_name, source_url, basis, synthetic, confidence, pii_present.

Set synthetic=true and pii_present=false for generated records. Add a “Why this number exists” drawer that traces a selected metric to its generator rule, scenario modifier, and public reference if any.

Generate these default volumes at runtime:
- 12 fictional facilities across mountain, metro, rural, and regional-hub archetypes;
- 32,256 sort-interval rows (12 facilities × 28 days × 96 fifteen-minute intervals);
- 20,000 EAVA metadata events;
- 8,064 labor-plan intervals;
- 1,500 route segments;
- 18,000 VRAA samples;
- 2,000 fictional compliance items;
- 1,200 inspection items;
- 250 Smith Agent runs;
- 1,000 reporting events.

Do not render all rows at once. Aggregate for charts, paginate/virtualize tables, and keep interaction fast.

SYNTHETIC GENERATION LOGIC
- Create daily and weekly seasonality plus scenario modifiers.
- Correlate late inbound arrival with sort compression; correlate occupancy, flow, sideways-item count, and bridging flags with jam risk; correlate weather/terrain with synthetic route travel-time variance; correlate labor variance with planned throughput—but never label correlation as causation.
- Add realistic missingness: 1–3% delayed readings, 0.5% sensor gaps, and a few deliberately inconsistent records for the Auditor/Data Lab to catch.
- Use deterministic distributions and document them in the Data Lab. Keep all counts nonnegative, percentages 0–100, risks 0–1, timestamps valid, and totals internally consistent.
- Define TLH as Total Labor Hours. Use PPLH for Packages per Labor Hour. Never use TLH for both concepts.

EXECUTIVE CONTROL TOWER
Show:
- a scenario clock, active seed, generator version, and trust banner;
- KPI cards for planned volume band, synthetic flow, Total Labor Hours, PPLH, departure-risk band, jam-risk zones, compliance items due, and data-quality score;
- a network flow timeline with inbound, unload, sort, dispatch, and route phases;
- a ranked “Decisions for human review” queue with evidence links, confidence, owner role, expiry time, reversibility, and an Approve for demo / Reject for demo interaction that only changes local demo state;
- a daily brief that separates Confirmed synthetic facts, Modeled assumptions, Recommendations, and Needs verification.

SMITH AGENT
Implement the four-worker loop:
- Analyst: establishes ground truth from selected synthetic evidence and lists anomalies.
- Planner: creates 2–4 ordered steps with dependencies and stop conditions.
- Operator: performs only local, simulated, allow-listed actions such as generate draft, open evidence, compare scenario, or create review item.
- Auditor: tests Goal, Proof, Steps, source coverage, schema, policy, and invariants.

Show a live trace with timestamps, inputs, outputs, tool receipts, retries, and audit reasons. Let the user select one run and force one failure (missing citation, impossible percentage, or prohibited action). The Auditor must reject it, send it back to the Analyst, and stop after the retry ceiling. Exhausted retries must display ESCALATED—not APPROVED.

Add an ARR + GPS intake form:
- ARR: Autonomous, Recurring, Reviewable, with rationale.
- GPS: Goal, Proof, Steps.
- Data, tools, agency level, stop conditions, reviewer, baseline, metric, and test window.
Calculate a transparent readiness score, but never imply formal approval.

EAVA + ACT + ROM
EAVA is metadata-only edge perception. Simulate MQTT-shaped records with timestamp, camera_id, zone_id, sensor_health, belt_speed_fpm, occupancy_percent, flow_rate_ppm, jam_risk_factor, sideways_item_count, bridging_detected, irregular_item_categories, and confidence. Do not create or display raw images/video.

ACT is advisory coordination. Combine EAVA, synthetic volume forecasts, labor plan, equipment state, and scenario timing into ranked reversible recommendations. Include evidence, expected direction of impact, confidence, tradeoffs, expiry, and human owner. Recommendations may include observe, reposition a role category, adjust release cadence, or request a supervisor check. Never automate labor decisions or equipment control.

ROM source details were not provided. Therefore implement ROM as an explicitly unresolved adapter contract labeled “ROM — definition/source pending.” Show expected input/output placeholders and a mock synthetic planning feed, but do not invent the acronym expansion, production logic, or claimed results.

ZERO-CLICK COMPLIANCE
Create a fictional compliance dashboard using SYN-WRK identifiers and fictional course categories. Include due-soon, overdue, complete, exception, and source-unavailable states. Add three fictional policy excerpts with obvious labels such as DEMO-POLICY-001 and citations that point to an in-app Demo Policy Library, not a real company policy.

The workflow must retrieve the fictional source, show the exact excerpt and version, identify the synthetic records in scope, and stage a manager-review draft. The only final buttons are “Save local demo draft” and “Discard local demo draft.” Never include Send, Submit, or autonomous notification behavior.

VRAA ROUTE EVIDENCE
Create a synthetic route view with a neutral, non-proprietary schematic map; if an open map library is already available, include required attribution. Do not require a live map service.

Plot synthetic samples for GPS speed, proposed ideal/posted-speed reference, elevation/grade band, Z-axis acceleration, rolling RMS, and event confidence. Implement these source-proposal thresholds and label every one “PROPOSED — UNVALIDATED”:
- smooth/paved: absolute Z acceleration below 0.15g;
- moderately degraded: 0.2g–0.4g;
- severe trigger: 0.5g–1.0g;
- sustained degraded segment: RMS above 0.25g for more than 30 seconds.

Show speed-to-vibration inverse relationship as supporting evidence, not proof. Generate a one-page preview dossier with synthetic route ID, source ledger, map/plot, thresholds, limitations, and human-review block. Do not include real routes, audio, people, addresses, or camera imagery.

INSPECTION CENTER
Build a generic digital checklist shell based only on these verified high-level categories: vehicle-management alignment; mechanical/fluids; chassis/brakes/suspension; tires; safety equipment; safety technology; branding; defect follow-up; documentation; sign-off.

Do not reproduce unavailable checklist wording. Display a source badge: “Four-page combined checklist linked; exact authorized field mapping pending.” Include Pass, Fail, Not observed, and Needs follow-up states; photo upload is disabled in the demo. A failed safety item must create a local review item and must not claim the vehicle was released or removed from service.

TLH SURVEY
Create a synthetic Ops Supervisor survey for Total Labor Hours planning. Clearly label the source survey as unavailable/title-only. Ask about planning effort, number of handoffs, data sources used, rework frequency, confidence band, major friction categories, and desired decision support. Avoid employee-performance questions and free-text PII. Show aggregate fictional responses and a methodology panel. Use PPLH for productivity, not TLH.

OTS REPORTING
Create a generic reporting workbench labeled “OTS-style reporting — field definitions pending source export.” Use synthetic timeliness/completeness/status records, source freshness, exception categories, draft narrative, and an evidence table. Do not invent what OTS expands to. Never claim the layout matches an official report.

RESOURCE REGISTRY
Show cards for the prompt library, agent souls, governance, Zero-Click, ACT, EAVA, VRAA, Smith Agent, checklist, TLH survey, OTS draft, Preload BI links, and the integrated architecture. Each card has owner/contributor, source date, status, classification, canonical link field, last verified, and action needed.

Private BI URLs must remain empty placeholders with the message: “Add only in an approved internal environment; never commit private BI links to public source control.”

DATA LAB & GOVERNANCE
Include:
- schema browser and row-count manifest;
- seed, generator version, scenario modifiers, and distribution explanations;
- source ledger with clickable public references;
- invariant test runner with pass/fail details;
- sensitivity scanner that flags names, emails outside .invalid, tracking-like long numbers, precise addresses, VIN-like strings, credentials, private URLs, and unsupported claims;
- audit export containing only synthetic data and local decisions;
- a promotion-gate checklist: owner, approved data path, evaluation, security/privacy/labor/legal/safety review as applicable, rollback, monitoring, records retention, and human decision point.

PUBLIC REFERENCE LEDGER
Link these sources in the app and explain exactly what each supports:
- National Weather Service API: https://www.weather.gov/documentation/services-web-API — forecast, alert, and observation field shapes; open U.S. government data.
- Bureau of Transportation Statistics geospatial portal: https://geodata.bts.gov/ — generic public freight/network context.
- U.S. Census data: https://data.census.gov/ — public population/place context.
- USGS 3D Elevation Program: https://www.usgs.gov/3d-elevation-program — public terrain/elevation context.
- OpenStreetMap copyright/license: https://www.openstreetmap.org/copyright — optional road geometry with required attribution.
- Google Maps Roads API: https://developers.google.com/maps/documentation/roads/overview — optional licensed snap-to-road/speed metadata; not open data and not required by the demo.
- Google Maps Elevation API: https://developers.google.com/maps/documentation/elevation/overview — optional licensed elevation service; not required by the demo.

Do not fetch these sources automatically on load. The bundled data is synthetic and merely shaped or conditioned using documented public concepts. Any live connector must be opt-in, clearly separated, and fail safely back to the bundled scenario.

INTERACTIONS THAT MUST WORK
- Navigation, scenario switching, play/pause, seed regeneration, date range, facility/zone filters, chart hover, table sort/filter/pagination, evidence drawers, Smith replay, forced audit failure, ARR/GPS scoring, local draft save/discard, checklist updates, invariant runner, sensitivity scan, and JSON/CSV export.
- Provide useful empty, loading, error, and source-unavailable states.
- All buttons must have real local behavior. Hide features you cannot implement instead of leaving dead controls.

ACCEPTANCE TESTS
Before finishing, verify in the generated app:
1. It loads with no network and no key.
2. The default scenario is populated and coherent.
3. Reusing the same seed creates identical data.
4. Every displayed record is synthetic and contains provenance.
5. No real-looking person, email, facility, tracking, VIN, route, or private URL exists.
6. TLH always means Total Labor Hours; PPLH is separate.
7. ROM and OTS expansions are not invented.
8. Proposed VRAA thresholds are visibly unvalidated.
9. EAVA contains metadata only.
10. Smith audit rejection loops correctly and retry exhaustion escalates.
11. Compliance drafts cannot be sent.
12. Charts, filters, drawers, exports, reset, and keyboard navigation work.
13. The Data Lab catches the deliberately inconsistent records.
14. The UI never labels synthetic or modeled results as measured outcomes.
15. The application is polished enough for a seven-minute leadership demonstration.

Create all code, data generators, types, components, tests supported by the environment, and concise in-app documentation now.
```

## Fast demo path

Use the seven-minute sequence in [the September 3 meeting brief](../docs/weekly-meeting-2026-09-03.md). The build remains useful if Gemini or every public source is unavailable because its primary path is deterministic and local.
