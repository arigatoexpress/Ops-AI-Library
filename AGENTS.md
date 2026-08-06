# AGENTS.md — Maintainer Charter

For humans and AI assistants editing this repository.

## Product mandate

This repo is a **prompt + soul + playbook library** for FedEx Operations Managers.  
Front door for managers: **`prompts/explorer.html`**, not the GitHub file tree.  
It is **not** an app monorepo. Do not re-center the README on dashboards, CLIs, or research spikes.

## Do

- Write for busy non-technical managers first.  
- Keep prompts scrubbed and anti-hallucination.  
- Keep souls with Always / Never / refusal lines.  
- Update `prompts/CATALOG.md` when adding prompts.  
- Run `node scripts/build-prompt-index.mjs` after prompt markdown changes.  
- Keep SharePoint/Power Automate content as **plans** until access is real.  
- Prefer small PRs: one prompt pack, one soul, or one playbook section.

## Do not

- Commit secrets or real operational data.  
- Claim official FedEx policy or production status.  
- Add root Node/Python apps “for demos” without moving the product mandate.  
- Enable auto-send / unsupervised actions in playbooks.  
- Expand the appendix into the headline.

## Verification before handoff

- `node scripts/build-prompt-index.mjs` succeeds.  
- Explorer opens and lists ~45 prompts.  
- Links in README still resolve.  
- New prompt listed in CATALOG with ID.  
- New soul linked from `souls/README.md` and `gemini-agents/README.md`.  
- Demos still use synthetic data only.  
- Language still says AI drafts / human decides.

## Related

- [CONTRIBUTING.md](CONTRIBUTING.md)  
- [governance/safe-use-rules.md](governance/safe-use-rules.md)  
- [appendix/prior-example-projects.md](appendix/prior-example-projects.md)
