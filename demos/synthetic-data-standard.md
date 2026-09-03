# Synthetic Data Standard for Operations Demos

Use this standard for demonstrations that combine operational telemetry, labor planning, compliance, route conditions, inspections, or reporting.

## Non-negotiable label

Every screen, export, chart tooltip, and generated narrative must state:

> **Synthetic demonstration — not live operations, measured performance, official policy, or a production system.**

## Three evidence classes

| Class | Meaning | Example |
| --- | --- | --- |
| Public reference | A cited schema, geography, weather field, or public taxonomy | NWS forecast period fields or a public road geometry |
| Modeled assumption | A transparent parameter chosen for the scenario | Sort wave starts at 05:30; jam-risk threshold is 0.72 |
| Synthetic event | A generated record that never happened | A fictional zone reaches 84% occupancy at 06:15 |

Never describe modeled assumptions or synthetic events as public facts.

## Required provenance fields

Every generated table must be able to expose:

```text
record_id, scenario_id, event_time, generated_at, generator_version,
seed, evidence_class, source_name, source_url, basis, synthetic,
confidence, pii_present
```

For a synthetic row, `synthetic=true` and `pii_present=false`.

## Public grounding candidates

| Domain | Approved demo use | Public source |
| --- | --- | --- |
| Weather | Field names, forecast/alert shapes, and scenario conditioning | [National Weather Service API](https://www.weather.gov/documentation/services-web-API) |
| Roads | Public geometry or road class; retain attribution and license | [OpenStreetMap](https://www.openstreetmap.org/copyright) |
| Freight geography | Generic freight corridors, modes, and public network context | [BTS geospatial data](https://geodata.bts.gov/) |
| Population context | County/place scale and density bands | [U.S. Census data](https://data.census.gov/) |
| Elevation | Terrain bands and route grade context | [USGS 3D Elevation Program](https://www.usgs.gov/3d-elevation-program) |
| Optional Google services | Route, elevation, or road metadata only when configured and licensed | [Maps Roads API](https://developers.google.com/maps/documentation/roads/overview) and [Elevation API](https://developers.google.com/maps/documentation/elevation/overview) |

Google Maps data is not open data. Do not cache, redistribute, or represent it as such; follow the applicable license and billing requirements.

## Safe identifiers

- Facilities: `SYN-FAC-001`, `SYN-FAC-002`.
- Work areas: `ZONE-A`, `ZONE-B`.
- Routes: `SYN-RT-0001`.
- People-like records: `SYN-WRK-0001`; no names are necessary.
- Email examples: reserved `.invalid` addresses only.
- Do not generate realistic tracking numbers, employee IDs, VINs, private URLs, or real facility codes.

## Recommended default dataset

| Table | Rows | Notes |
| --- | ---: | --- |
| `facilities` | 12 | Fictional archetypes and public-region context only |
| `sort_intervals` | 32,256 | 12 facilities × 28 days × 96 fifteen-minute intervals |
| `eava_events` | 20,000 | Metadata only; no images, audio, faces, or plates |
| `labor_plan_intervals` | 8,064 | Planned/actual synthetic labor at hourly grain |
| `route_segments` | 1,500 | Fictional route IDs with public-inspired terrain bands |
| `vraa_samples` | 18,000 | Synthetic speed, grade, and IMU samples |
| `compliance_items` | 2,000 | Fictional worker IDs and fictional training assignments |
| `inspection_items` | 1,200 | Generic checklist categories and statuses |
| `agent_runs` | 250 | Smith Agent trace and audit outcomes |
| `reporting_events` | 1,000 | Generic OTS-style reporting states, clearly labeled |

Generate rows at runtime from a seeded pseudorandom generator rather than embedding huge literals.

## Invariants

- Counts, durations, miles, and labor hours are nonnegative.
- Percentages remain between 0 and 100; risk scores between 0 and 1.
- Timestamps are valid ISO 8601 values and ordered within a trace.
- Total labor hours equal the sum of their component intervals within rounding tolerance.
- A completion date cannot precede an assignment date.
- An expiration state must agree with the expiration date and scenario clock.
- EAVA occupancy and flow influence jam risk but do not prove a cause.
- VRAA thresholds from the proposal are labeled **proposed and unvalidated**.
- A rejected audit cannot be displayed as approved because retries were exhausted.
- Draft actions never appear as sent, submitted, dispatched, or executed.

## Reproducibility and tests

- Default seed: `OPS-DEMO-20260903`.
- Show the seed and generator version in the UI.
- Provide **Regenerate**, **Reset**, and **Export synthetic JSON/CSV** controls.
- Add automated checks for all invariants and show their pass/fail status in a Data Lab panel.
- Keep a compact manifest of row counts, schema versions, source links, and generation time.
