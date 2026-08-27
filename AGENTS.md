# AGENTS.md — Maintainer Charter

## Product mandate

Manager enablement + governed concept-incubation library for FedEx Operations Managers.

**Manager front doors:** `index.html` and `prompts/explorer.html`.

**Concept front door:** `concepts/README.md`.

Not a production app monorepo.

## Do

- Write for non-technical managers first.  
- Keep prompts scrubbed and anti-hallucination.  
- After prompt markdown changes:
  ```bash
  node scripts/build-prompt-index.mjs
  node scripts/check-docs.mjs
  ```
- Update `prompts/CATALOG.md` when adding prompts.  
- Keep SharePoint/PA as plans until access is real.
- Keep concepts labeled as concept, synthetic proof of concept, validation candidate, pilot, or production.
- Keep prototype fixtures synthetic and use reserved `.invalid` addresses.
- Run the Zero-Click unit tests when its prototype changes.

## Do not

- Commit secrets or real operational data.  
- Claim official FedEx policy or live production automation.  
- Re-center README on legacy apps.
- Present modeled targets, proposed thresholds, or synthetic results as measured outcomes.
- Add browser-session reuse, raw camera/voice data, or autonomous hardware control to a public demo.

## Verification

- `check-docs.mjs` passes  
- Explorer lists ~45 prompts and includes sensitivity scan  
- README relative links resolve  
- `python3 -m unittest discover -s concepts/zero-click-compliance/prototype/tests -v` passes
