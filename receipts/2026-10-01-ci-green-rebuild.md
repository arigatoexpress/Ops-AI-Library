# Receipt — 2026-10-01 CI green rebuild

## What failed
PR #8 check run 110504121535 (workflow run 36902285643) failed Docs integrity:
prompts.json count=45, missing P45-P48. The branch restored
scripts/build-prompt-index.mjs but did not commit the rebuilt index, and
ci.yml never ran the builder before check-docs.

## What this commit does
- ci.yml checks out the PR head, runs node scripts/build-prompt-index.mjs,
  and commits prompts.json + explorer.html when they drift.
- check-docs then runs against the rebuilt tree (expect count=49, P45-P48).
- Local verification before this push: builder emitted 49 prompts and
  check-docs PASSED with 0 warnings.

## Boundary
Public/synthetic only. No operational identifiers.
