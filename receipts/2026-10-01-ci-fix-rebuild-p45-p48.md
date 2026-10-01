# Receipt — 2026-10-01 CI fix: rebuild P45-P48 into prompts.json

## What ran
Diagnosed CI FAIL at HEAD c48b39e0 (run 36901309526, Docs integrity check):
ERROR: missing prompt id P45 / P46 / P47 / P48; prompts.json count=45.
Same error on runs 17-23; last green was 939d4bd.

Root cause: scripts/build-prompt-index.mjs files array omitted
prompts/late-arrival-and-service-recovery.md, so the v2.2 P45-P48 sections
never entered prompts.json or explorer.html DATA. check-docs.mjs did not
require the starter-kit path or check P45-P48, so CI stayed green through
the starter-kit merge (PR #6) and only failed after the check-docs patch.

## Fix (this branch)
- scripts/build-prompt-index.mjs: index late-arrival-and-service-recovery.md
  (files array, categoryNames, catalogTitles P45-P48, agentMap, FIRST-week
  set, tips)
- scripts/check-docs.mjs: require starter-kits/wrong-day-lates/README.md and
  verify P45-P48 in prompts.json
- Rebuild prompts.json + explorer.html DATA locally against the real repo:
  count=49, P45-P48 present, check-docs PASS
- Sensitive-data scan of starter-kits/: NONE

## PASS/FAIL/UNKNOWN
- build-prompt-index.mjs: PASS (locally)
- check-docs.mjs: PASS (locally)
- P45-P48 in rebuilt index: PASS
- Sensitive-data scan: PASS
- Remote CI on this fix: UNKNOWN until next run

## Not done
- Merge this branch to main (owner action)
- Remote CI verification
- SharePoint upload remains manual
