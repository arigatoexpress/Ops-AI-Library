# AGENTS.md — Maintainer Charter

For humans and AI assistants editing this repository.

## Product mandate

This repo is a **prompt + soul + playbook library** for FedEx Operations Managers.  
It is **not** an app monorepo. Do not re-center the README on dashboards, CLIs, or research spikes.

## Do

- Write for busy non-technical managers first.  
- Keep prompts scrubbed and anti-hallucination.  
- Keep souls with Always / Never / refusal lines.  
- Update `prompts/CATALOG.md` when adding prompts.  
- Keep SharePoint/Power Automate content as **plans** until access is real.  
- Prefer small PRs: one prompt pack, one soul, or one playbook section.

## Do not

- Commit secrets or real operational data.  
- Claim official FedEx policy or production status.  
- Add root Node/Python apps “for demos” without moving the product mandate.  
- Enable auto-send / unsupervised actions in playbooks.  
- Expand the appendix into the headline.

## Verification before handoff

- Links in README still resolve.  
- New prompt listed in CATALOG.  
- New soul linked from `souls/README.md` and `gemini-agents/README.md`.  
- Demos still use synthetic data only.  
- Language still says AI drafts / human decides.

## Related

- Style and contrib: [CONTRIBUTING.md](CONTRIBUTING.md)  
- Safety: [governance/safe-use-rules.md](governance/safe-use-rules.md)  
- Legacy footnote: [appendix/prior-example-projects.md](appendix/prior-example-projects.md)
