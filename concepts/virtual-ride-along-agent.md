# Virtual Ride-Along Agent

**Status:** Concept / calibration proposal

**Author:** Travis Long

**Date:** 2026-08-26

**Version:** 0.9.1

## Problem

Independent Service Providers experience route constraints daily, but a human description alone may not provide the consistent, objective evidence needed for a Unique Characteristics review. The proposed Virtual Ride-Along Agent (VRAA) would turn approved handheld telemetry and driver-entered context into a human-reviewed evidence package.

It does **not** determine contract terms, blame a driver, or prove a causal claim by itself.

## Proposed workflow

1. An approved handheld collects only enabled sensor features and timestamps.
2. The device derives short-lived features such as vertical-vibration RMS, speed, altitude change, stop-to-scan delay, and optional driver annotations.
3. A validator checks calibration, device placement, GPS quality, duration, and missing data.
4. Candidate segments are compared with an approved route baseline.
5. The system prepares a dossier with evidence, uncertainty, and missing verification steps.
6. The authorized station or FLME reviewer accepts, edits, rejects, or requests a physical ride-along.

## Evidence channels

| Channel | Proposed feature | What it may support | Required control |
| --- | --- | --- | --- |
| IMU / accelerometer | Vertical acceleration, RMS vibration, event duration | Candidate degraded segment | Device-mount calibration, vehicle baseline, false-positive testing |
| GPS / altitude | Speed, position quality, grade estimate, switchback density | Route geometry and sustained speed variance | Map matching, GPS-quality threshold, no employee productivity use |
| Temporal events | Vehicle stop to delivery-event interval | Candidate infrastructure delay | Approved event definitions and aggregation |
| Voice annotation | Driver-triggered short note | Context for later verification | Opt-in, hands-free policy, transcription review, short retention |
| Microphone-derived event | On-device, non-recording acoustic feature | Potential call-box or gate wait context | Disabled by default; privacy/legal approval and proof raw audio is discarded |

## Proposed haptic thresholds - not validated

The source proposal offers starting thresholds, not production rules:

| Profile | Proposed vertical acceleration | Proposed interpretation |
| --- | --- | --- |
| Smooth / paved | less than +/-0.15 g | Baseline candidate |
| Moderately degraded | +/-0.2 g to +/-0.4 g | Possible speed reduction |
| Severely degraded | +/-0.5 g to +/-1.0 g | Candidate UC segment |
| Sustained degradation | RMS above 0.25 g for more than 30 seconds | Candidate sustained degraded segment |

Before use, calibrate by device model, mount position, vehicle class, tire/suspension condition, load, road type, and speed. Thresholds must be evaluated against labeled physical ride-alongs. They must not be used as a safety instruction or contractual determination.

## Speed-to-vibration hypothesis

The useful signal is not vibration alone. The hypothesis is that **sustained vibration remaining high while a vehicle safely decelerates** may distinguish a constrained road from ordinary speed-related vibration. Validation should compare:

- vibration against speed within the same vehicle/device configuration;
- the candidate segment against matched paved and rough-road controls;
- repeated traversals across weather and load conditions; and
- model output against an independent human road assessment.

## Routing baseline

Use the current Google Maps Platform **Routes API** for `ComputeRoutes` or `ComputeRouteMatrix` rather than designing a new integration around the legacy Directions and Distance Matrix APIs. The Roads API may provide posted speed-limit context, but Google states that speed-limit data may be inaccurate, incomplete, estimated, outdated, or not real time. Map data is supporting context, not proof of driver behavior.

References:

- https://developers.google.com/maps/documentation/routes/compute-route-over
- https://developers.google.com/maps/documentation/routes/compute-route-matrix-over
- https://developers.google.com/maps/documentation/roads/speed-limits

## Dossier output

The proposed one-page dossier should include:

- segment map with generalized or access-controlled location display;
- collection window and device/calibration version;
- observed speed, vibration, grade, and delay summaries;
- baseline source and version;
- confidence, missing data, and alternative explanations;
- driver annotation clearly labeled as reported context;
- review disposition and reviewer role.

The language model may draft narrative only from the validated evidence object. All figures should be rendered deterministically.

## Non-negotiable controls

- Explicit purpose limitation: UC evidence, not covert productivity monitoring.
- Privacy, labor, legal, security, records, device, and FLME-owner review before real collection.
- No cabin monitoring or always-on raw audio/video storage.
- Opt-in and notice requirements determined before pilot.
- Encryption, access logging, retention limits, and deletion verification.
- Separation between driver annotation, measured fact, derived inference, and reviewer decision.

## Smallest safe validation

Run a synthetic pipeline first, then a consented closed-course test using known road surfaces and a small set of approved devices/vehicles. Success is not a high trigger rate; it is repeatable separation of labeled conditions with an acceptable false-positive rate and a dossier reviewers can audit.
