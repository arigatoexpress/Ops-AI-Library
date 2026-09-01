# AGENTS.md — Maintainer Charter

## Product mandate

Prompt + soul + playbook library for FedEx Operations Managers.  
**Manager front doors:** `index.html` and `prompts/explorer.html`.  
Not an app monorepo.

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

## Do not

- Commit secrets or real operational data.  
- Claim official FedEx policy or live production automation.  
- Re-center README on legacy apps.

## Verification

- `check-docs.mjs` passes  
- Explorer lists ~45 prompts and includes sensitivity scan  
- README relative links resolve  
