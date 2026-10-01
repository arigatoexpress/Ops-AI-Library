# CI hardening — 2026-10-01

## What changed

`scripts/check-docs.mjs` now enforces:

1. **Exact prompt count** — `prompts.json` must contain exactly 49 prompts (was `>= 40`, which could not catch a stale committed index).
2. **Required prompt IDs** — P00, P01, P08, P20, P44, P45, P46, P47, P48 must all be present.
3. **Secret-filename scan** — fails the build if any file matching `secrets.toml`, `.env`, `*.pem`, `*.key`, or `credentials.*` appears anywhere in the tree.

## Why

- The docs check previously allowed a stale index to pass, which is how the red streak (missing P45–P48) was masked.
- The public tree contained `travis-vscode-repo/.streamlit/secrets.toml` (0-byte placeholder) and `travis-vscode-repo/data/*.xlsx` files. The filename scan now blocks any future secret-like file from landing on main.

## Still open (owner decisions)

- Whether `travis-vscode-repo/` belongs in this public repo at all. It holds station-coded roster and hire spreadsheets (NRXX, P895–P960) that may be real operational data, not synthetic. If real, it should be removed or moved to a private repo. If synthetic, it should be labeled as such per `demos/synthetic-data-standard.md`.
- Branch protection on `main` (requires a write; not done from this PR).

## Receipt

- Branch: `ci/harden-docs-check`
- Files: `scripts/check-docs.mjs`, `docs/ci-hardening-2026-10-01.md`
- No merges, deploys, or spend from this change.
