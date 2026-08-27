# Product Portfolio Boundaries

This repository is the **FedEx operations AI adoption, manager enablement, and governed concept-incubation layer**. It is intentionally not the production monorepo for every prototype.

## Source of truth by product

| Product | Canonical source | Runtime boundary | Purpose |
| --- | --- | --- | --- |
| Ops AI Library | `arigatoexpress/Ops-AI-Library` | Static GitHub / SharePoint / Teams content; no always-on application runtime required | Prompts, manager guidance, souls, governance, training, and sandbox playbooks |
| Operational AI concept portfolio | `concepts/` in `arigatoexpress/Ops-AI-Library` | Documentation plus narrowly scoped synthetic evidence artifacts only | Architecture proposals, validation gates, data contracts, and meeting-ready concept review |
| RECON | Standalone deployable application sourced from the former Logistics Intelligence prototype until its dedicated repository is promoted | Dedicated Cloud Run service in the approved FedEx prototype/sandbox GCP project | Public/synthetic station-risk decision support and human-reviewed manager briefs |
| Delivery Markets Lab | `arigatoexpress/fedex-delivery-markets` | Dedicated Cloud Run service and isolated configuration | Paper-only, synthetic-data governance/research prototype; no live trading and no real tracking data |
| Sapphire Nexus | `arigatoexpress/sapphire-nexus` | Separate Sapphire GCP project/service | General AI/quant/research intelligence kernel; not a FedEx product and not a host for RECON or Delivery Markets |

## Non-negotiable separation

1. **No shared production secrets.** Each deployed service owns its own runtime identity, environment variables, and Secret Manager bindings.
2. **No shared mutable data stores by default.** Cross-product communication should use explicit public/read-only contracts or approved APIs, never incidental database coupling.
3. **No FedEx internal data in public prototypes.** RECON and Delivery Markets remain public/synthetic until written approval changes that boundary.
4. **Sapphire stays company-neutral.** FedEx-specific UI, data, market logic, and branding do not live in Sapphire Nexus.
5. **Ops AI Library stays manager-first.** Application source belongs in the application repository, not in this library.
6. **Concept evidence stays bounded.** A small synthetic proof of concept may live beside its concept when it proves a contract or guardrail; durable services, real integrations, production dependencies, and operational data move to a product-specific repository and approved runtime.

## GCP naming and ownership convention

Use a distinct Cloud Run service per product and make the repository name discoverable in service labels/metadata.

Recommended logical layout (project IDs are intentionally not specified here):

```text
FedEx prototype / sandbox GCP project
├── recon-dashboard              # RECON only
└── fedex-delivery-markets       # paper-only Delivery Markets only

Sapphire GCP project
└── sapphire-nexus               # Sapphire only
```

Do not deploy a FedEx prototype into the Sapphire service or route FedEx product paths through Sapphire as a convenience proxy.

## Promotion rule for RECON

The legacy `AI-Efficiency` repository is no longer the program front door. The RECON application may reuse the tested Logistics Intelligence source as its seed, but before the next durable production promotion it should have:

- a standalone canonical repository or clearly isolated source root;
- its own CI and Cloud Run deployment identity;
- public/synthetic data labels on every demo path;
- Gemini/Vertex configuration server-side only;
- a deterministic fallback so the demo remains usable when model access is unavailable;
- no dependency on the Ops AI Library runtime, because the library has no application runtime mandate.

## Portfolio navigation rule

The Ops AI Library may **link to** RECON and Delivery Markets as optional demos. It should not absorb their source trees or imply that either prototype is required for manager adoption.
