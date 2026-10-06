# CI hardening — prompt count and scan scope

## What the docs check enforces

`scripts/check-docs.mjs` fails unless all of the following are true:

1. **Exact prompt count** — `prompts/prompts.json` contains exactly 49 prompts. A minimum such as 40 or more let a stale index pass.
2. **Required prompt IDs** — P00, P01, P08, P20, P44, P45, P46, P47, and P48 are all present. The success line prints only when every one of those IDs is in the index.
3. **Secret-filename scan** — a name like `secrets.toml`, `.env`, `*.pem`, `*.key`, or `credentials.*` fails the check. The success line prints only when that walk is clean.

## Owner ruling — 2026-10-05

`travis-vscode-repo/` stays in this repository. The scan-scope exclusion for that prefix is approved. Do not delete, move, or rewrite anything under that folder.

The exclusion is the path prefix `travis-vscode-repo/` and nothing else. A near-miss folder such as `travis-vscode-repo-extra/` is still scanned. A self-test writes a temporary tree outside the repo, checks that rule, and deletes the temporary tree before the script exits.

## What this note does not change

This note does not close an older pull request, change branch protection, or remove files. SharePoint and Power Automate remain plans until access is real.
