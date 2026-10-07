# NAMING.md — Portfolio Naming Canon

**Status:** single source of truth for project names across the arigatoexpress portfolio.
**Date:** 2026-10-07. **Owner:** Ari Spector ([arigatoexpress](https://github.com/arigatoexpress)).
**Companion:** [strategy/2026-10-07-portfolio-synthesis.md](strategy/2026-10-07-portfolio-synthesis.md).

## How to use this file

1. When you write a doc, issue, PR, or conversation, use the **canonical name** from the tables below — on first use in a document, add the repo in parentheses, e.g. "Texas Home Outlet storefront (repo: Project-Go-Forward)".
2. **Short codes** exist for tables, branch names, labels, and receipts. Use them only after the canonical name has appeared once.
3. **Aliases to retire** may still appear in old documents. Do not propagate them into new work.
4. Nothing in this file renames a GitHub repo or a Google Cloud project ID. Live deploys, Workload Identity Federation bindings, branch-protection rules, and DNS depend on those identifiers. Section 6 lists what is worth renaming *later* and why.

---

## 1. The two anchors — never conflate them

### Texas Home Outlet storefront (repo: Project-Go-Forward) — code `PGF`

- **What it is:** the client storefront and back office for **Texas Home Outlet (THO)**, a manufactured-home retailer — the repo's description: "An AI Powered Business System Designed to Replace Third Party Vendors and Allow Businesses to Truly Own Their Business Systems" ([repo](https://github.com/arigatoexpress/Project-Go-Forward)).
- **Live at:** [texashomeoutlet.com](https://www.texashomeoutlet.com) (verified HTTP 200 on 2026-10-07; cutover recorded in [`docs/CUTOVER_GUIDE.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/CUTOVER_GUIDE.md), 2026-06-14).
- **Runs on:** Google Cloud project **`tho-ai-agent`**, Cloud Run service **`project-go-forward`** (`us-central1`) ([`docs/ARCHITECTURE.md` §3](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md)).
- **Legacy origin:** `tho.sapphirealpha.xyz` — still serving, but the repo's own AGENTS.md calls it "a legacy origin" ([PGF `AGENTS.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/AGENTS.md), "Current status").
- **Always call it:** **"Texas Home Outlet storefront (repo: Project-Go-Forward)"** on first mention; **PGF** thereafter.
- **Never do:** rename the repo, rename the GCP project, or treat it as the owner's business brand. It is a *client* system.

### WeGoForward — code `WGF`

- **What it is:** the **owner's business brand** offering AI and automation services to small and large business clients. The site lists five offers: half-day agent-safety workshop, one-workflow-one-week, sourced brief / twenty cases, x402 demo, and website answers/follow-up ([wegoforward repo pages](https://github.com/arigatoexpress/wegoforward)).
- **Site:** [wegoforward.app](https://wegoforward.app) — **live as of 2026-10-07** (HTTP 200, Cloudflare-fronted, "no forms, no scripts, no analytics"). The repo description "wegoforward.app is not registered" is **stale** — see §5.
- **Repo:** [arigatoexpress/wegoforward](https://github.com/arigatoexpress/wegoforward) (static pages + a workshop exercise).
- **Google Cloud project:** a GCP project represents this business, but **its ID does not appear in any public repo doc** reviewed for this canon. Record it in the private project registry (§4) and keep it out of public docs.
- **Always call it:** **"WeGoForward (WGF)"**.
- **Never do:** put Texas Home Outlet content, FedEx content, or Sapphire trading content under the WGF brand. The WGF site itself already carries the rule: "WeGoForward. Not Texas Home Outlet." ([wegoforward `index.html`](https://github.com/arigatoexpress/wegoforward/blob/main/index.html)).

**The one-sentence rule:** *PGF is a client product the owner built; WGF is the owner's business that builds such products.*

---

## 2. Canonical names, codes, and aliases to retire

### Client and business surfaces

| Seen names | Canonical name | Code | Aliases to retire | Recommended action |
| --- | --- | --- | --- | --- |
| Project-Go-Forward, Project Go Forward, THO App, "the THO repo" | **Texas Home Outlet storefront (repo: Project-Go-Forward)** | `PGF` | "Project Go Forward" as a *product* name; "THO App" | Update PGF README badge (still says `tho.sapphirealpha.xyz`) to texashomeoutlet.com; keep repo + project IDs untouched |
| Texas Home Outlet, THO, `tho-*` (GCP project, bucket, CSS prefix) | **Texas Home Outlet (the client)** | `THO` | none | Keep. `tho-` prefix is reserved for THO client infrastructure |
| WeGoForward, wegoforward, "WeGoForward pages" | **WeGoForward** | `WGF` | none | Update the repo description — the domain is registered and live |
| Tex | **Tex (THO chat agent)** | `TEX` | none | Keep; Tex is a feature of PGF, not a standalone product |
| Ari, rari, arigatoexpress, aribs | **Ari Spector (GitHub: arigatoexpress)** | `ARI` | "rari" for new public work (legacy handle: `rari-portfolio`, deleted `home-lead-pipeline-rari-edition`) | Use the GitHub handle in docs; keep personal username out of public repos |

### FedEx-lane program

| Seen names | Canonical name | Code | Aliases to retire | Recommended action |
| --- | --- | --- | --- | --- |
| Ops-AI-Library, Ops AI Library | **Ops AI Library** (this repo) | `OAL` | none | Keep — manager front door per `AGENTS.md` |
| AI-Efficiency, "FedEx AI Efficiency Hub", AI Efficiency Group | **AI Efficiency Hub (legacy)** | `AEH` | "FedEx AI Efficiency Hub" as a program front door | Add a top-of-README banner pointing managers to OAL; keep the repo as app/block source (per `appendix/prior-example-projects.md`) |
| RECON, Logistics Intelligence System, fedex-logistics-intelligence-system, recon-dashboard | **RECON (station decision support)** | `RECON` | "Logistics Intelligence" as a product name | Decide promotion per `docs/product-portfolio-boundaries.md` ("Promotion rule for RECON"): standalone repo or historical |
| Delivery Markets, fedex-delivery-markets, Delivery Markets Lab | **Delivery Markets Lab (repo: fedex-delivery-markets)** | `DML` | the in-tree copy name at `AI-Efficiency/starter-projects/fedex-delivery-markets` | Keep the standalone repo canonical; the AEH copy is already labeled "Prototype reference" |

### The Sapphire family (archived R&D program)

| Seen names | Canonical name | Code | Aliases to retire | Recommended action |
| --- | --- | --- | --- | --- |
| Sapphire, Sapphire OS, "Autonomous Organization" | **Sapphire (archived R&D program)** | `SPH` | "Sapphire OS" for new work | Keep archived; revive only as composition of shared modules (see synthesis §5) |
| Sapphire Nexus, sapphire-nexus | **Sapphire Nexus (archived)** | `SPN` | — | Keep archived; its evidence-ledger and contract patterns feed module extractions |
| sapphire-alpha-dashboard, Sapphire Alpha Observatory, sapphirealpha.xyz | **Sapphire Alpha Observatory** | `SAO` | "Mission Control" (ambiguous) | Keep as the program's public evidence site while maintained; note it shares a domain with PGF's legacy origin — see §6 |
| Sapphire Sentinel, sapphire-sentinel | **Sapphire Sentinel (archived)** | `SPS` | — | Keep archived; guard checks port into aegis contrib |
| `sapphire-479610` (GCP project) | **Sapphire DNS host project** | — | — | Never rename (GCP project IDs are immutable; it hosts the `sapphirealpha.xyz` Cloud DNS zone and is load-bearing per [PGF ARCHITECTURE.md §3](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md)). Add the `do-not-delete` label its own SECURITY.md already prescribes |
| `sapphire-jwt-*` secret-derivation prefix in PGF | internal constant | — | — | Not user-visible; no action. Noted so nobody reads "sapphire" as a client-system dependency |

### The guard family — one canonical library

| Seen names | Canonical name | Code | Aliases to retire | Recommended action |
| --- | --- | --- | --- | --- |
| aegis | **aegis** | `AEG` | — | The one guardrail library for all new work |
| 0guard, megaeth-agent-guard, sapphire-sentinel (as guard products) | archived chain-specific guards | — | their names for any *new* guard work | Port their checks into aegis contrib packs; keep repos archived |

### Libraries and internal tooling

| Seen names | Canonical name | Code | Aliases to retire | Recommended action |
| --- | --- | --- | --- | --- |
| libcircuit | **libcircuit** | `LCT` | — | Keep name if unarchived for reuse |
| libsim | **libsim** | `LSM` | — | Keep; design-phase spec for any simulation work |
| sovereign-terminal, sovereign-windows-worker, "sovereign workspace", "Sovereign Local Builder" (retired bot) | **Sovereign local stack (archived)** | `SOV` | "sovereign" as a prefix for new work | Keep archived; the master plan's "Cloud Lab … owns the sovereign workspace" (`docs/master-plan-grok-bot-first.md` §2) should read "owner's local stack" |
| kadima-bench, Kadima Digital Laboratories, AI-Benchmark | **AI-Benchmark (archived bench suite)** | `AIB` | "Kadima" byline; `kadima-bench` as a standalone repo | kadima-bench already lives on as `vendor/kadima-bench` inside AI-Benchmark ([AI-Benchmark README](https://github.com/arigatoexpress/AI-Benchmark)); if benchmarking resumes, resume in AI-Benchmark |
| tradingview-mcp, tradingview-mcp-upstream, tradingview-autonomous-manager, `packages/tradingview-mcp` | **Market Atlas tradingview packages (archived)** | `TVM` | the three standalone repo names | Canonical copies already merged as subtrees in [market-atlas-ai](https://github.com/arigatoexpress/market-atlas-ai) `packages/`; keep all archived |
| market-atlas-ai | **Market Atlas (archived)** | `MAA` | — | Keep archived |
| full-sail-volume-calculator-2.0, ArigatoALMM ("Full Sail DEX") | archived Sui/DeFi experiments | — | "Full Sail" in any owned repo name — it is a third-party brand, and ArigatoALMM carries BSL-1.1 license text | Do not revive under third-party branding; keep archived |
| agent-opportunity-exchange, AOE | **Agent Opportunity Exchange (archived)** | `AOE` | — | Keep archived; see the bot-name collision in §3 |
| agent-runtime-control-plane | **Runtime Control Plane (archived)** | `RCP` | — | Keep archived |
| org-platform | **org-platform (archived)** | `ORG` | — | Keep archived |
| adk-workspace | **ADK Workspace (archived)** | `ADW` | — | Keep archived (code avoids collision with Google's "ADK" product) |
| cyber-threat-bot | **Cyber Threat Bot (archived)** | `CTB` | — | Verify its advertised Cloud Run URL is decommissioned (synthesis §4 #10) |
| regional-intel-workbench | **Regional Intel Workbench (archived)** | `RIW` | — | Keep archived; provenance pattern feeds the sourced-brief proposal |
| wildfire-watch | **Wildfire Watch (archived)** | `WFW` | — | Keep archived |
| home-access-kit | **Home Access Kit** | `HAK` | — | Keep name; scrub README topology (synthesis §4 #8) |
| gunnison-fishing-guide / "Gunnison-Crested Butte Fish Finder" | **Gunnison Valley Fish Finder (repo: gunnison-fishing-guide)** | `GFG` | — | Keep repo name; use the display name in prose |
| Asterism ("Codex Projects") | **Asterism (archived)** | `AST` | "Codex Projects" as a workspace title | Keep archived |
| blackjackal | **blackjackal (archived)** | `BJK` | — | Keep archived |
| DesktopOrganizer / "AI File Organizer" | **AI File Organizer (archived)** | `DTO` | — | Keep archived |
| SitarHero | **Sitar Hero (archived)** | `STH` | — | Keep archived |
| rari-portfolio | **rari-portfolio (archived)** | `RPF` | — | Keep archived |
| eliza, openclaw, claw-code, hermes-agent, NemoClaw, sui, tradingview-mcp-upstream | **third-party forks (archived)** | — | presenting any fork as an own product | Keep archived; no codes; no new work |

### Planned / proposed names

| Seen names | Canonical name | Code | Note |
| --- | --- | --- | --- |
| "ari-llm" (Track B platform library, [PGF `docs/GCP_ENTERPRISE_PLAN.md` §3](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/GCP_ENTERPRISE_PLAN.md)) | **model-gateway** (when built) | `MGT` | Avoid personal prefixes on shared modules; the portfolio rule is neutral, composable names like aegis/libcircuit |
| storefront-kit, prompt-pack, answer-appliance, sourced-brief, portable-deploy, ops-metrics, receipt-ledger | proposals in the [synthesis](strategy/2026-10-07-portfolio-synthesis.md) §5 | — | Names are provisional until their first repo exists; register them here when created |

---

## 3. Bot fleet names (from `docs/master-plan-grok-bot-first.md`)

Bots are internal tooling identities, not products. Canonical list as of 2026-10-01 (master plan §2), with two collisions fixed:

| Bot name in master plan | Canonical name | Note |
| --- | --- | --- |
| Steering Hub | **Steering Hub** | Keep — sole owner check-in point |
| Cloud Refactor Lead | **Cloud Refactor Lead** | Keep |
| Cloud Lab | **Cloud Lab** | Keep; "owns … the sovereign workspace" should read "owner's local stack" (see §2) |
| dr eggbot | **dr eggbot** | Keep — bot designer, specs only |
| FHE Sentinel Architect | **FHE Sentinel Architect** | Keep; do not shorten to "Sentinel" (collides with Sapphire Sentinel) |
| CI Regression Reviewer | **CI Regression Reviewer** | Keep |
| Projects Manager | **Projects Manager** | Keep |
| Research Synthesizer | **Research Synthesizer** | Keep |
| Thesis Red Team | **Thesis Red Team** | Keep |
| Founder Research | **Founder Research** | Keep |
| Agent Opportunity Exchange (bot) | **Marketplace Builder** | **Rename the bot's display name** — it collides with the archived repo `agent-opportunity-exchange` (`AOE`) and with AOE adapters referenced in sapphire-nexus |
| Archive Miner | **Archive Miner** | Keep |
| AI Automation Builder | **AI Automation Builder** | Keep; its "freelance revenue lane" work now rolls up under the WGF brand |
| SyncLink Catchup | **SyncLink Catchup** | Keep, but define "Astra thread" somewhere — no repo or doc reviewed explains what Astra is |
| Sovereign Local Builder, CI Failure Triage | retired | Deletion candidates per master plan §7 — owner action |
| WeGoForward Scout | **WeGoForward Scout (parked)** | Keep parked; prefix makes the brand ownership clear — correct pattern |

**Lane names** (master plan §4): "Freelance AI automation" → canonical **WGF services lane**; "RH-FHE Sentinel (lane F)" → **RH-FHE research lane** (`LNF`), gated per master plan §7; "Ops AI Library / AI Efficiency" → **FedEx enablement lane**; "Sapphire / other" → **Sapphire (parked) lane**.

---

## 4. Google Cloud project registry (public-safe)

GCP project IDs are immutable and several are load-bearing. Public docs should use **role names**; keep the full ID list in a private registry.

| Role name | Project ID | Public? | Rule |
| --- | --- | --- | --- |
| THO storefront production | `tho-ai-agent` | Yes (already in public docs) | Never rename; enable Firestore delete protection (synthesis §4 #2) |
| Sapphire DNS host | `sapphire-479610` | Yes (already in public docs) | Never rename; add `do-not-delete` label per [PGF SECURITY.md §7.3](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) |
| FedEx prototype / sandbox | *(intentionally not in public docs)* | No | Keep it that way — `docs/product-portfolio-boundaries.md` already withholds the ID |
| Sapphire services | *(not in public docs)* | No | Record privately |
| WeGoForward business | *(not found in any public doc)* | No | Record privately; confirm which project serves wegoforward.app, if any (the site is currently static and Cloudflare-fronted) |
| Legacy threat-bot host | project number `691674245427` appears in the archived repo's live-URL badge | Yes (via badge) | Verify decommission; then remove the badge reference |

---

## 5. Open discrepancies to fix (doc and display-name changes)

1. **wegoforward repo description** says "wegoforward.app is not registered" — the domain resolves and serves the site today (verified 2026-10-07). Update the description to "WeGoForward — the business site. wegoforward.app." (Owner action on that repo.)
2. **PGF README badge** advertises "live — tho.sapphirealpha.xyz" while PGF `AGENTS.md` says the canonical storefront is `www.texashomeoutlet.com` and the sapphirealpha URL is a legacy origin. Update the badge. (Owner action on that repo.)
3. **Profile README** ([arigatoexpress/arigatoexpress](https://github.com/arigatoexpress/arigatoexpress)) lists four repos that no longer resolve (Kronos, crypto-tax-tracker, rtk, home-lead-pipeline-rari-edition) and presents archived projects without status markers. Refresh or trim. (Owner action.)
4. **AI-Efficiency README** still reads as a program front door; the program front door is this repo (per `appendix/prior-example-projects.md`). Add a banner. (Owner action.)
5. **Prompt counts differ** (AEH: 52, OAL: 49) with overlapping content — resolve via the `prompt-pack` proposal (synthesis §5 P3).
6. **cyber-threat-bot badge** advertises a live Cloud Run URL on an archived repo — verify and either decommission or annotate (synthesis §4 #10).
7. **Master plan §2**: rename the "Agent Opportunity Exchange" bot to **Marketplace Builder** and reword "sovereign workspace" — both edits belong to `docs/master-plan-grok-bot-first.md` and are proposed here for the next master-plan revision.

## 6. Flagged for later renaming — not now

| Item | Why it is confusing | Why not now |
| --- | --- | --- |
| Repo `Project-Go-Forward` | The name says nothing about Texas Home Outlet; "PGF" reads like an internal codename (because it is one) | Live deploys, WIF bindings, branch protection, SEO-relevant links, and the Cloud Run service name all key off current identifiers. Revisit only if the repo ever stops serving production — and a GitHub rename's redirects make even that low-value |
| GCP project `sapphire-479610` | A numeric, non-descriptive ID hosts the DNS zone that a client site's legacy origin depends on | GCP project IDs are immutable. Mitigate with labels + this registry instead |
| GCP project `tho-ai-agent` | "ai-agent" undersells that it holds live customer data | Immutable; mitigate with labels + the private registry |
| `tho.sapphirealpha.xyz` legacy origin | A *client* storefront answering on the owner's R&D brand domain blurs the PGF/SPH boundary | It still serves and may hold indexed links; retire only after an SEO check against [`docs/SEO_MIGRATION.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SEO_MIGRATION.md), with a 301 to texashomeoutlet.com |
| Repo `Asterism` | Repo name says nothing about the "Codex Projects" workspace inside | Archived; renaming an archived repo adds churn with no reader benefit |
| Repo `ArigatoALMM` | Contains a third-party brand's blueprint ("Full Sail") under a personal-brand name | Archived; do not revive. If ALMM work ever resumes, it resumes under a neutral name with original code |
| Bot "Agent Opportunity Exchange" | Collides with the archived AOE repo | Not load-bearing — renamed in §3 above, effective on the next master-plan edit |

## 7. Standing rules

1. New projects get a **neutral, composable name** (aegis, libcircuit, libsim are the model), a two-to-four-letter code registered in this file, and no personal prefixes.
2. Client work is always named **"\<Client\> \<surface\> (repo: \<repo-name\>)"** so the client relationship is explicit — the PGF pattern.
3. Never name owned work after a third-party brand (the Full Sail lesson).
4. Never put a GCP project ID, tailnet name, internal IP, or personal email in a public doc unless it is already load-bearing and public — and even then, prefer role names.
5. When a name changes meaning (parked → active, concept → pilot), update this file in the same PR.
