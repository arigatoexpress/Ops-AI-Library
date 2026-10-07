# Portfolio Synthesis — 2026-10-07

**Audience:** the owner (Ari Spector, GitHub: [arigatoexpress](https://github.com/arigatoexpress)) and future maintainers.
**Lens:** everything should be **portable, composable, extensible, and secure, with no vendor lock-in**.
**Companion document:** [../NAMING.md](../NAMING.md) — the naming canon this synthesis references.

## Evidence standard and method

- Every claim below cites a repository file or a public URL. Where a document and reality disagreed, the discrepancy is flagged instead of resolved by guessing.
- Sources read: all 47 repositories visible under `arigatoexpress` via `gh repo list arigatoexpress --limit 200` (2026-10-07); every non-fork README; deep docs in the active repositories (architecture, security, launch-readiness, boundary, and cutover documents); closed-PR lists on the active repositories; and this repository's full docs set.
- Live-state checks run 2026-10-07: `www.texashomeoutlet.com` returns HTTP 200; `sapphirealpha.xyz` returns HTTP 200; `tho.sapphirealpha.xyz` returns HTTP 200; `wegoforward.app` resolves and serves the WeGoForward site (HTTP 200).
- Nothing here invents revenue, customers, or results. Where a repo publishes prices or test counts, they are cited as *published claims*, not verified outcomes.
- No repository ADR directories exist anywhere in the portfolio (checked `Project-Go-Forward` and `AI-Efficiency` trees); decision history lives in READMEs, readiness ledgers, registers, and PR trails instead.

---

## 1. Inventory

Status meanings: **active** = committed within roughly the last month or carrying a live workload; **parked** = not archived but no recent commits; **archived** = GitHub-archived (read-only).

### Active / parked (8)

| Repo | Purpose | Status | Main stack |
| --- | --- | --- | --- |
| [Ops-AI-Library](https://github.com/arigatoexpress/Ops-AI-Library) (this repo) | Manager enablement + governed concept incubator for FedEx operations managers: 49 prompts, agent "souls", governance, concept portfolio | Active | Markdown/HTML, Node CI scripts, small Python prototype |
| [AI-Efficiency](https://github.com/arigatoexpress/AI-Efficiency) | Legacy "FedEx AI Efficiency Hub": 52 prompts, offline KPI tools, Logistics Intelligence dashboard (RECON seed), ADK agent kit | Active (legacy hub; front-door role retired per `appendix/prior-example-projects.md`) | TypeScript/React/Express, Python, Node CLIs |
| [Project-Go-Forward](https://github.com/arigatoexpress/Project-Go-Forward) | Texas Home Outlet storefront + back office (CRM, regulatory document engine, "Tex" AI consultant, Ad Studio) | Active, live production at [texashomeoutlet.com](https://www.texashomeoutlet.com) | FastAPI + React 19 + Firestore + Gemini on Vertex AI, single Cloud Run service |
| [wegoforward](https://github.com/arigatoexpress/wegoforward) | WeGoForward business site: five offer pages + a workshop exercise | Active, live at [wegoforward.app](https://wegoforward.app) (repo description still says "not registered" — stale) | Static HTML/CSS + one Node test exercise; served via Cloudflare |
| [fedex-delivery-markets](https://github.com/arigatoexpress/fedex-delivery-markets) | Delivery Markets Lab: paper-only, synthetic-data delivery-time prediction-market demo | Active prototype (paper-only) | TypeScript/React 19/Hono + Solidity contracts |
| [aegis](https://github.com/arigatoexpress/aegis) | Stdlib-only, model- and deployment-agnostic agent-safety firewall | Parked as a finished library (last push 2026-07-16); prime reuse candidate | Python stdlib only |
| [home-access-kit](https://github.com/arigatoexpress/home-access-kit) | Tailscale home-gateway / Wake-on-LAN scripts | Parked (2026-07-03) | Bash + Make |
| [gunnison-fishing-guide](https://github.com/arigatoexpress/gunnison-fishing-guide) | Gunnison–Crested Butte fishing PWA with live USGS flows | Parked (2026-07-03) | Static HTML/JS, Leaflet, USGS API |

### Archived (39)

| Repo | Purpose | Main stack |
| --- | --- | --- |
| [Sapphire](https://github.com/arigatoexpress/Sapphire) | "Self-sovereign capital intelligence OS" monorepo (7,997+ tests claimed in README badge) | Python, FastAPI, Redis, Ollama, DuckDB, Solidity, Tailscale, GCP |
| [sapphire-nexus](https://github.com/arigatoexpress/sapphire-nexus) | Local-first intelligence kernel: typed API contracts, evidence ledger, model-gateway contracts | TypeScript/Hono, Vitest |
| [sapphire-alpha-dashboard](https://github.com/arigatoexpress/sapphire-alpha-dashboard) | Public "Evidence/Decision Observatory" at [sapphirealpha.xyz](https://sapphirealpha.xyz) with HMAC-signed telemetry ingest and a strict privacy boundary | FastAPI + Next.js static export + React/Vite SPA, Firestore |
| [sapphire-sentinel](https://github.com/arigatoexpress/sapphire-sentinel) | Policy/privacy/payment-safety firewall for RWA agents (x402 gates, Robinhood Chain testnet) | Python/Flask, web3.py, Solidity |
| [0guard](https://github.com/arigatoexpress/0guard) | Pre-wallet agent firewall for 0G (exploit signatures, reputation, receipts) | Python/Flask, web3.py, Solidity |
| [megaeth-agent-guard](https://github.com/arigatoexpress/megaeth-agent-guard) | Read-only scout + intent firewall for MegaETH | Python/Flask, web3.py |
| [libcircuit](https://github.com/arigatoexpress/libcircuit) | Composable, deployment-agnostic circuit breaker + kill-switch library | Python stdlib |
| [libsim](https://github.com/arigatoexpress/libsim) | Composable, deterministic distributed-systems/swarm simulator (design phase; evals-first) | Python stdlib |
| [sovereign-terminal](https://github.com/arigatoexpress/sovereign-terminal) | Mac-side CLI for the local agentic stack (`sov`, `ai`) | Python/shell |
| [sovereign-windows-worker](https://github.com/arigatoexpress/sovereign-windows-worker) | Windows worker companion (no README) | — |
| [org-platform](https://github.com/arigatoexpress/org-platform) | OSINT fan-in, event normalization, crypto scoring, local dashboard for Sapphire OS | Python/DuckDB + TypeScript dashboard |
| [adk-workspace](https://github.com/arigatoexpress/adk-workspace) | Google ADK config agents + frontend + deploy scripts (mock data) | Python, Google ADK, React |
| [agent-runtime-control-plane](https://github.com/arigatoexpress/agent-runtime-control-plane) | Dry-run inventory/control-plane scanners for local runtime surfaces | Node.js ES modules |
| [agent-opportunity-exchange](https://github.com/arigatoexpress/agent-opportunity-exchange) | "AOE": x402-ready marketplace for rights-cleared intelligence products | TypeScript/Hono, x402 SDK, Viem |
| [market-atlas-ai](https://github.com/arigatoexpress/market-atlas-ai) | Consolidated trading lab; absorbed `tradingview-mcp` and `tradingview-autonomous-manager` as `packages/` subtrees | Python/DuckDB/Pandas |
| [tradingview-mcp](https://github.com/arigatoexpress/tradingview-mcp) | MCP server bridging Claude Code to TradingView via session cookies + Playwright | TypeScript, MCP SDK |
| [tradingview-mcp-upstream](https://github.com/arigatoexpress/tradingview-mcp-upstream) | Fork of the upstream TradingView CDP bridge | TypeScript (fork) |
| [tradingview-autonomous-manager](https://github.com/arigatoexpress/tradingview-autonomous-manager) | TradingView Desktop automation + signal forwarding to Sapphire | Python/FastAPI/Playwright |
| [ArigatoALMM](https://github.com/arigatoexpress/ArigatoALMM) | "Full Sail DEX" CLAMM/ALMM design blueprint (Move-like pseudocode; third-party brand + BSL license text) | Sui Move (blueprint only) |
| [sui-dashboard-app](https://github.com/arigatoexpress/sui-dashboard-app) | Blockchain metrics API scaffold (README only; backend never committed) | TypeScript/Express (planned) |
| [full-sail-volume-calculator-2.0](https://github.com/arigatoexpress/full-sail-volume-calculator-2.0) | Sui DeFi volume prediction dashboard | Python/Streamlit/Prophet |
| [tdr-analytics-hub](https://github.com/arigatoexpress/tdr-analytics-hub) | DeFi valuation dashboard + scraped-research archive | Python stdlib server + vanilla JS |
| [regional-intel-workbench](https://github.com/arigatoexpress/regional-intel-workbench) | Public-source regional intelligence console with provenance (Austin, Houston, Gunnison) | Python/FastAPI, Leaflet, Chart.js |
| [cyber-threat-bot](https://github.com/arigatoexpress/cyber-threat-bot) | CISA KEV/NVD/MITRE + EPSS ranked threat queue; README badge still advertises a live Cloud Run URL | Python stdlib HTTP server, Docker |
| [wildfire-watch](https://github.com/arigatoexpress/wildfire-watch) | County-scale wildfire drone-fleet simulation (pre-flight; zero flight hours) | Python sim/ML, Flask |
| [AI-Benchmark](https://github.com/arigatoexpress/AI-Benchmark) | Local LLM benchmarking scripts; absorbed `kadima-bench` as `vendor/kadima-bench` | Python, Ollama, Matplotlib |
| [kadima-bench](https://github.com/arigatoexpress/kadima-bench) | Packaged local-LLM benchmarking framework (folded into AI-Benchmark) | Python, Ollama |
| [Asterism](https://github.com/arigatoexpress/Asterism) | "Codex Projects" workspace hosting a local-first creative-OS single-page app | Static HTML/JS |
| [SitarHero](https://github.com/arigatoexpress/SitarHero) | Sitar/raga learning demo app | React 18 + Vite |
| [DesktopOrganizer](https://github.com/arigatoexpress/DesktopOrganizer) | Local-LLM file organizer with dry-run and undo | Python + Ollama |
| [blackjackal](https://github.com/arigatoexpress/blackjackal) | Safe Chrome-extension dev workspace (metadata-only sync) | Bash/Make |
| [rari-portfolio](https://github.com/arigatoexpress/rari-portfolio) | Static portfolio site ("rari's walrus site") | Static HTML |
| [arigatoexpress](https://github.com/arigatoexpress/arigatoexpress) | GitHub profile config/README | Markdown |
| [eliza](https://github.com/arigatoexpress/eliza), [openclaw](https://github.com/arigatoexpress/openclaw), [claw-code](https://github.com/arigatoexpress/claw-code), [hermes-agent](https://github.com/arigatoexpress/hermes-agent), [NemoClaw](https://github.com/arigatoexpress/NemoClaw), [sui](https://github.com/arigatoexpress/sui) | Third-party forks (agent frameworks, Sui platform) | various (forks) |

### Referenced but no longer resolvable

The profile README (`arigatoexpress/arigatoexpress`) lists **Kronos**, **crypto-tax-tracker**, **rtk**, and **home-lead-pipeline-rari-edition**; all four return "Could not resolve to a Repository" as of 2026-10-07 (deleted or renamed). The profile README is stale.

---

## 2. Reusable pieces worth extracting into shared, composable modules

The portfolio already contains the raw material for a small, portable module set. The extraction rule already written in [AI-Efficiency `docs/building-blocks.md`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/building-blocks.md) is the right governance: *copy a block when one real call-site exists; extract to a shared module only when two or more real call-sites exist.* The table below marks which blocks already meet that bar.

| # | Module (proposed name) | What it does | Best current source | Proposed interface | Two+ call-sites? |
| --- | --- | --- | --- | --- | --- |
| 1 | **aegis** (agent-safety firewall) | Wraps any agent action in composable `Check`s; returns a deterministic `Decision` plus tamper-evident receipt hash; fail-closed defaults | [aegis](https://github.com/arigatoexpress/aegis) (`src/aegis/`: `check.py`, `checks/`, `adapters/`); chain-specific variants in [0guard](https://github.com/arigatoexpress/0guard), [megaeth-agent-guard](https://github.com/arigatoexpress/megaeth-agent-guard), [sapphire-sentinel](https://github.com/arigatoexpress/sapphire-sentinel) | `Guard(Policy([...checks])).check(AgentAction) -> Decision`; custom checks subclass `Check.evaluate(action, ctx)` | Yes — 4 repos implement the same pattern |
| 2 | **libcircuit** (breaker / kill-switch) | Circuit breaker and threshold kill-switch with pluggable state store and notifier | [libcircuit](https://github.com/arigatoexpress/libcircuit) | `CircuitBreaker(name, failure_threshold, recovery_seconds).call(fn)`; `KillSwitch(name, threshold, mode).update(value)` | Conceptually — trading stacks + any paid API client |
| 3 | **reviewed-draft** (AI with a deterministic floor) | Deterministic fallback first, model second, `source: model\|fallback` label always; "needs human verification" footer | [AI-Efficiency `app/lib/drafts.ts`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/building-blocks.md) (block 2); PGF's fallback posture in its [README](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/README.md) trust section | `draft(request) -> { text, source, labels[], reviewFooter }` | Yes — AI-Efficiency + PGF |
| 4 | **model-auth-switch** | One function resolving model-client config from env: Vertex ADC ↔ AI Studio key ↔ null (run fallback) | [AI-Efficiency `app/lib/gemini-config.ts`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/building-blocks.md) (block 3); PGF env table in [`docs/ARCHITECTURE.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md) §4 | `resolveModelAuth(env) -> ClientOptions \| null` | Yes — AI-Efficiency + PGF |
| 5 | **prompt-pack** (machine-readable prompt library) | Versioned JSON prompt schema + markdown↔JSON build script + offline explorer with sensitivity scan | This repo (`prompts/prompts.json`, `scripts/build-prompt-index.mjs`, `prompts/explorer.html`) and [AI-Efficiency `prompts/`](https://github.com/arigatoexpress/AI-Efficiency/tree/main/prompts) | `{ id, title, category, placeholders[], body, safetyRule }`; `buildIndex(mdDir) -> prompts.json` | Yes — two libraries (52 vs 49 prompts) already drift |
| 6 | **lead-capture / CRM tools** | Lead intake, status transitions, appointments, nurture drafts | [PGF `tools/crm_tools.py`, `tools/contact_capture.py`, `tools/lead_nurture.py`](https://github.com/arigatoexpress/Project-Go-Forward/tree/main/tools) | `captureLead(LeadIn) -> Lead`; `transitionLead(id, status) -> Lead`; storage behind a repository interface | One real (PGF); WGF "Follow-up" tier is the second |
| 7 | **document-engine** (registry-driven PDF fill) | Fills regulatory PDF templates (XFA/AcroForm) from deal data using a field registry | [PGF `tools/document_engine*.py` + `config/field_map.json` + `tho_documents/`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md) §5 | `fillDocument(templateId, data) -> DocumentRef`; field names only via registry | One real (PGF) — extract only when a second client needs packets |
| 8 | **pii-guard / field-crypto** | Strips PII before logs/LLM prompts; field-level symmetric encryption at rest | [PGF `tools/pii_guard.py`, `tools/input_sanitizer.py`, `tools/field_crypto.py`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) §3 | `scrub(text) -> text`; `encryptField(name, value)` / `decryptField(...)` | Yes — PGF + every future client app |
| 9 | **auth-kit** (PIN + passkey + email-code sessions) | Staff auth: WebAuthn passkeys, email-code sign-in, PIN break-glass, HMAC session tokens, CSRF double-submit | [PGF `auth/`](https://github.com/arigatoexpress/Project-Go-Forward/tree/main/auth) + [SECURITY.md §1](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) | `issueSession(identity) -> token`; `verifySession(token)`; `registerPasskey()` / `assertPasskey()`; step-up API | One real (PGF); WGF answer-appliance is the second |
| 10 | **public-data adapters** | Dependency-free fetchers (Open-Meteo, NWS, USGS) with per-source degradation and source labels | [AI-Efficiency `live-signals.ts`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/building-blocks.md) (block 1); [gunnison-fishing-guide](https://github.com/arigatoexpress/gunnison-fishing-guide) USGS cards | `fetchSignals(source, location, fetchImpl) -> LabeledValues` | Yes — AI-Efficiency + fishing guide |
| 11 | **deterministic metrics layer** | Targets/MoM/YoY compare, risk-lineage state machine, lagged associations, drift baseline, canonical JSON brief | [AI-Efficiency `priority-metrics-intelligence/src/`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/building-blocks.md) (block 5) | Pure functions: arrays in → plain objects out; no I/O | One real; Ops-AI-Library wrong-day-lates work is the second |
| 12 | **offline-app guarantee** | Single-file HTML apps with `connect-src 'none'` CSP so loaded data cannot leave the machine; CI fails if the header goes missing | [AI-Efficiency Signal Lab / TLH-SPH Explorer + `scripts/check-docs.mjs`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/building-blocks.md) (block 7) | Pattern + CI check, not a library | Yes — two apps + CI |
| 13 | **ci-templates** | Docs-integrity check, prompt-index sync, JSON validation, pinned actions, minimal permissions, WIF keyless Cloud Run deploy | This repo (`scripts/check-docs.mjs`, `.github/workflows/ci.yml`); [PGF `.github/workflows/deploy.yml`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md) §4; [fedex-delivery-markets hardening note](https://github.com/arigatoexpress/fedex-delivery-markets) | Template repo with cookiecutter-style variables | Yes — 3+ repos converge on the same workflow |
| 14 | **evidence/receipt ledger** | Hash-addressed, append-only decision/evidence receipts with a verifier | [aegis](https://github.com/arigatoexpress/aegis) receipt hash; [sapphire-nexus `GET /v1/evidence-ledger`](https://github.com/arigatoexpress/sapphire-nexus); PGF [`audit_log.py`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) §8; WGF "one-page receipt" promise ([workshop.html](https://github.com/arigatoexpress/wegoforward/blob/main/workshop.html)) | `append(event) -> hash`; `verify(chain) -> bool`; JSONL storage | Yes — 4 independent implementations |
| 15 | **research-packet** (sourced briefs) | Public-source collection with per-signal provenance (name, URL, fetch date, source health) | [cyber-threat-bot](https://github.com/arigatoexpress/cyber-threat-bot), [regional-intel-workbench](https://github.com/arigatoexpress/regional-intel-workbench), [agent-opportunity-exchange](https://github.com/arigatoexpress/agent-opportunity-exchange) source-rights envelope | `collect(question, sources) -> [{ claim, sourceUrl, fetchedAt, counterclaim }]` | Yes — 3 repos + the WGF "sourced brief" offer |
| 16 | **x402 payment gate** | HTTP 402 payment-required flow with quote binding and nonce-replay protection (testnet/simulated only) | [sapphire-sentinel](https://github.com/arigatoexpress/sapphire-sentinel) (`/api/x402/*`), [agent-opportunity-exchange](https://github.com/arigatoexpress/agent-opportunity-exchange) x402 middleware | Middleware: `requirePayment(route, quote) -> 402 \| pass` | Yes — 2 repos + WGF x402 offer page |
| 17 | **telemetry projector** (privacy boundary) | Aggregate → allowlist → validate → HMAC-sign → bounded history; missing sources render "not observed", never invented zeros | [sapphire-alpha-dashboard](https://github.com/arigatoexpress/sapphire-alpha-dashboard) (`telemetry/`, privacy boundary section) | `project(rawSnapshot) -> PublicProjection` | One real; any future public status page is the second |
| 18 | **read-only agent template** | Agent whose tool surface *is* the safety model: read-only tools, data-safety gate, offline harness proving no network/send surface | [AI-Efficiency `starter-projects/adk-shift-brief-agent/`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/building-blocks.md) (block 6) | Copy-the-project template + `run_checks.py` harness | One real; every future client agent is the second |
| 19 | **simulation kernel** | Deterministic, seeded world/agent stepping with pluggable channels and protocols | [libsim](https://github.com/arigatoexpress/libsim) (design phase), [wildfire-watch `sim/`](https://github.com/arigatoexpress/wildfire-watch) | `Stepper(world, channel, seed).run(ticks) -> trace` | One real (wildfire-watch); libsim is the spec |
| 20 | **home-access-kit** (remote-ops runbook) | Always-on subnet router + watchdog + WoL for owner's own ops | [home-access-kit](https://github.com/arigatoexpress/home-access-kit) | `config.sh.example` → sourced config; `setup`, `wake`, `watchdog`, `verify` scripts | Internal only — keep as runbook, not a product |

**Modules 1, 5, 13, and 14 are the highest-leverage extractions**: each already has multiple convergent implementations, each is vendor-neutral by design, and each directly supports the WeGoForward offers (see §5).

---

## 3. Lock-in risks and portable alternatives

| Project | Lock-in observed (citation) | Risk | Portable alternative |
| --- | --- | --- | --- |
| Project-Go-Forward | **Firestore** as primary store ([`docs/ARCHITECTURE.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md) §2–3); JSON files already exist as fallback | Proprietary API; client data hard to migrate; single-cloud failure domain | Formalize the existing fallback into a repository interface (`database/models.py` already defines Pydantic models); add SQLite/Postgres adapter. Firestore becomes one adapter, not the schema owner |
| Project-Go-Forward | **Gemini via Google ADK + Vertex AI** ([ARCHITECTURE.md](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md) §2) | Agent orchestration and model tied to one vendor | The repo's own enterprise plan already schedules a "platform library (Track B `ari-llm`)" provider abstraction ([`docs/GCP_ENTERPRISE_PLAN.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/GCP_ENTERPRISE_PLAN.md) §3). Build it as an OpenAI-compatible/Ollama-capable gateway so any model serves Tex |
| Project-Go-Forward | **Cloud Run + Secret Manager + GCS + Cloud DNS** ([ARCHITECTURE.md](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md) §3–4) | Deploy, secrets, storage, DNS all single-cloud | The app is already one container — keep it OCI-portable (any Docker host: Fly.io, ECS, a VPS + Caddy); abstract secrets behind env vars (already true); use S3-compatible storage (MinIO/R2) behind an `image_storage`-style interface; DNS is portable by nature |
| Project-Go-Forward | **Resend** (email) and **DocuSeal** (e-sign) ([README architecture](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/README.md)) | Third-party SaaS in the deal-critical path | DocuSeal is open-source and self-hostable — the repo's own [`deploy-docuseal.yml`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/LAUNCH_READINESS.md) (item 6) self-hosts it on Cloud Run/Cloud SQL; keep that shape. Put email behind one `sendMail()` seam so SMTP/any provider works |
| Project-Go-Forward | **Matterport** 3D iframes in CSP ([SECURITY.md §4](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md)) | Third-party embed in the storefront | Treat as optional enhancement; ensure catalog works without it (photos/floorplans already first-class per README) |
| AI-Efficiency | Gemini SDK (`@google/genai`) and planned Vertex/Agent Engine path ([`docs/technology/google-cloud-adk-integration.md`](https://github.com/arigatoexpress/AI-Efficiency/blob/main/docs/technology/google-cloud-adk-integration.md), referenced from its README) | Model + agent runtime single-vendor | Its own `gemini-config.ts` env switch (block 4 above) is the right seam; extend it to an OpenAI-compatible endpoint. The offline tools and prompt library are already fully portable |
| AI-Efficiency | Cloud Run hosting (both published URLs returned 404 on 2026-09-09 per its [README](https://github.com/arigatoexpress/AI-Efficiency)) | Demo availability depends on one cloud | The local demo (`npm run demo`, port 3900) already works anywhere; container is portable |
| fedex-delivery-markets | Cloud Run deploy target; EVM testnets; optional Hedera anchoring ([`docs/SECURITY_AND_COMPLIANCE.md`](https://github.com/arigatoexpress/fedex-delivery-markets/blob/main/docs/SECURITY_AND_COMPLIANCE.md)) | Moderate: contracts are EVM-standard; anchoring is optional | Already isolated by its [PRODUCT_BOUNDARY](https://github.com/arigatoexpress/fedex-delivery-markets/blob/main/docs/PRODUCT_BOUNDARY.md); `infra/` carries Docker Compose + Render scaffolds — keep multi-target |
| aegis / libcircuit / libsim | None — stdlib-only by design ([aegis README](https://github.com/arigatoexpress/aegis), [libcircuit README](https://github.com/arigatoexpress/libcircuit)) | — | These are the portability gold standard; new modules should follow their shape |
| home-access-kit | **Tailscale** coordination server + tailnet dependency ([README](https://github.com/arigatoexpress/home-access-kit)) | Personal remote access depends on one SaaS | Headscale (self-hosted coordination server) or plain WireGuard; the scripts' shape (config + setup + watchdog) survives the swap |
| wegoforward | None in code — static site, "no forms, no scripts, no analytics" (live site footer); currently served via Cloudflare (response headers, 2026-10-07) | Low | Any static host works; keep it that way |
| gunnison-fishing-guide | Leaflet + public map tiles + USGS API ([README](https://github.com/arigatoexpress/gunnison-fishing-guide)) | Low: third-party tiles | Swap tile provider or self-host tiles; USGS is a public API |
| Sapphire (archived) | GCP (BQ/GCS), Tailscale, Robinhood Agentic MCP, Ollama mesh ([README](https://github.com/arigatoexpress/Sapphire)) | High coupling — one reason a restart should reuse modules, not the monolith | If revived, revive as composition of aegis + libcircuit + receipt-ledger + model-gateway, not as the monorepo |
| tradingview-mcp family (archived) | TradingView session cookies + undocumented internal APIs ([tradingview-mcp-upstream README](https://github.com/arigatoexpress/tradingview-mcp-upstream)) | Extreme single-vendor brittleness; credential handling risk | Keep archived; if chart tooling is needed, use documented APIs only |
| cyber-threat-bot (archived) | Cloud Run deploy ([README](https://github.com/arigatoexpress/cyber-threat-bot)) | Low — runtime is stdlib `http.server` | Runs in any container; already portable |

---

## 4. Security gaps visible from code or docs

Severity: **high** = live data or credentials at risk now; **medium** = documented weakness with a known fix; **low** = hygiene.

| # | Gap | Evidence | Suggested fix | Severity |
| --- | --- | --- | --- | --- |
| 1 | PGF: `N8N_API_TOKEN` and `THO_API_KEY` are plaintext env vars, self-flagged as "exposed in prior tooling output" | [PGF `docs/SECURITY.md` §2](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) | Rotate both, move to Secret Manager, bind via `secretKeyRef` (exact commands already in that doc) | **High** (until rotated) |
| 2 | PGF: Firestore `(default)` has delete protection **disabled** while holding live customer/deal data | [PGF `docs/SECURITY.md` §7.1](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md), [ARCHITECTURE.md §3](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md) | One `gcloud firestore databases update --delete-protection` command (in doc) | **High** (blast radius) |
| 3 | PGF: no scheduled Firestore backup confirmed; GCS bucket versioning unconfirmed | [PGF `docs/SECURITY.md` §7](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md); [LAUNCH_READINESS.md item 8](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/LAUNCH_READINESS.md) | Run the documented "Ops bootstrap" workflow; do the manual restore drill | Medium |
| 4 | PGF: shared-PIN admin model with stateless, non-revocable JWT sessions (30-day sliding TTL) | [PGF `docs/SECURITY.md` §1](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) | The repo's own plan: per-person Google identities via IAP/SSO ([`docs/GCP_ENTERPRISE_PLAN.md` §1](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/GCP_ENTERPRISE_PLAN.md)); recent PRs [#369](https://github.com/arigatoexpress/Project-Go-Forward/pull/369)/[#370](https://github.com/arigatoexpress/Project-Go-Forward/pull/370) moved sign-in to email-link + PIN backup — continue that direction | Medium |
| 5 | PGF: launch ledger's GO decision was **NO** on 2026-07-25 with operator actions open (partner API key, PIN strength verification, DocuSeal e-sign server never deployed, monitoring/bootstrap, staging E2E + load test) — yet the site is live | [PGF `LAUNCH_READINESS.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/LAUNCH_READINESS.md), [`docs/CUTOVER_GUIDE.md`](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/CUTOVER_GUIDE.md) (live since 2026-06-14) | Reconcile the ledger with reality: either close the items with evidence or restate current status. Do not advertise e-sign until the DocuSeal deploy exists | Medium |
| 6 | PGF: in-memory per-IP rate limiting resets on instance recycle and does not coordinate across instances | [PGF `docs/SECURITY.md` §5](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) | Acceptable at current scale; note as a known limit if traffic grows | Low |
| 7 | PGF: a personal Gmail address appears in a `gcloud` label example | [PGF `docs/SECURITY.md` §7.3](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) | Replace with a role/group address in docs (value not reproduced here deliberately) | Low |
| 8 | home-access-kit: README publishes real home-network topology — tailnet name, node names, a Tailscale IP, the LAN subnet, an internal IP, and a local username | [home-access-kit README](https://github.com/arigatoexpress/home-access-kit) (values deliberately not reproduced here) | Move topology into the gitignored `config.sh` the repo already uses; keep the README on placeholders | Medium |
| 9 | home-access-kit: setup instructs disabling Tailscale key expiry for the gateway | [home-access-kit README](https://github.com/arigatoexpress/home-access-kit) ("Do this when you're next physically at home", step 4) | Documented trade-off; add a re-auth reminder cadence instead of never-expire | Low |
| 10 | cyber-threat-bot: archived repo still advertises a live Cloud Run URL badge | [cyber-threat-bot README](https://github.com/arigatoexpress/cyber-threat-bot) | Verify the service is decommissioned or intentionally running; an unmaintained public endpoint is an attack surface | Medium |
| 11 | tradingview-mcp (archived): authentication via copied session cookies in `.env` | [tradingview-mcp README](https://github.com/arigatoexpress/tradingview-mcp) | Keep archived; never revive the cookie pattern | Low (while archived) |
| 12 | This repo: `travis-vscode-repo/` previously carried secret-like filenames and real-looking contacts; removed and CI-gated | [PR #10](https://github.com/arigatoexpress/Ops-AI-Library/pull/10), `CHANGELOG.md` v2.1 note, `scripts/check-docs.mjs` secret-filename scan | Done — keep the CI gate; do not re-add contributor subtrees with live-system material | Closed |

**Positive patterns worth keeping and spreading:** WIF keyless deploys with no service-account keys (PGF [ARCHITECTURE.md §4](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/ARCHITECTURE.md)); PII scrubbing before logs/LLM plus field-level encryption and a structured, PII-free audit trail (PGF [SECURITY.md §3, §8](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md)); fail-closed checks with per-check enforcement knobs ([aegis](https://github.com/arigatoexpress/aegis)); `connect-src 'none'` offline apps enforced by CI (AI-Efficiency block 7); branch protection verified by an actual rejected push (PGF [LAUNCH_READINESS.md item 1](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/LAUNCH_READINESS.md)); wegoforward.app shipping with no forms, scripts, or analytics.

---

## 5. Project proposals under the new approach

Effort is sized **S / M / L** by technical scope, not calendar time: **S** = one new small package, mostly glue code, one CI workflow; **M** = extraction from one existing repo plus a new test harness and docs; **L** = extraction from the live PGF monolith with parity evidence against its 655-test suite (count per its [README badge](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/README.md)) plus portability adapters.

### P1 — `storefront-kit`: the portable small-business storefront (L)

- **Goal:** extract PGF's reusable core — lead capture, CRM, booking, document engine, reviewed-draft chat — into a self-hostable starter any small business can run with `docker compose up`.
- **Serves:** WeGoForward small-business clients; Texas Home Outlet remains the reference deployment.
- **Reuses:** PGF `auth/`, `tools/crm_tools.py`, `tools/document_engine*.py`, `tools/pii_guard.py`, `prompts/` (Tex's plain-English instructions); modules 3, 6, 7, 8, 9 from §2.
- **Portability stance:** SQLite/Postgres default (Firestore as an adapter), OpenAI-compatible model gateway, S3-compatible storage, SMTP email seam.
- **First milestone:** demo storefront with synthetic inventory; lead captured into SQLite; one document template filled; chat in deterministic-fallback mode only.
- **Effort:** L. Depends on roadmap items R4–R6 (storage interface + model gateway first).

### P2 — aegis adoption + contrib packs (S–M)

- **Goal:** make [aegis](https://github.com/arigatoexpress/aegis) the portfolio's single guardrail library; port the chain-specific checks from 0guard / megaeth-agent-guard / sapphire-sentinel into optional contrib packs; wire it in front of Tex's tool calls in PGF.
- **Serves:** internal (every agent we run) and large-business clients (agent governance story).
- **Reuses:** aegis core; the three archived guards' check logic; PGF tool surface.
- **First milestone:** aegis release with a PGF adapter guarding one Tex tool (e.g. lead creation), writing receipt hashes to a JSONL sink.
- **Effort:** S–M.

### P3 — `prompt-pack`: one prompt library, packaged (S)

- **Goal:** merge the two drifting libraries (AI-Efficiency 52 prompts, Ops-AI-Library 49) into one versioned, model-agnostic package with the existing build script and explorer; both repos consume it.
- **Serves:** internal (both FedEx-lane repos) and small-business clients (the WGF "Answer" offer needs approved-question packs — same schema).
- **Reuses:** `scripts/build-prompt-index.mjs`, `prompts/explorer.html` sensitivity scan, both libraries' content.
- **First milestone:** single JSON schema + dedup report + both repos building from the package in CI.
- **Effort:** S.

### P4 — `answer-appliance`: the website-answers product (S–M)

- **Goal:** productize the published WGF "Answer / Follow-up" tiers ([wegoforward `answers.html`](https://github.com/arigatoexpress/wegoforward/blob/main/answers.html) lists approved prices: $495 setup / $99 monthly and $995 / $249; "Book and text" explicitly not for sale) as a self-hostable, no-tracking Q&A widget: approved-answer store, deterministic retrieval, unknown questions handed to a person, drafts never auto-sent.
- **Serves:** small-business clients.
- **Reuses:** prompt-pack (P3), aegis (P2), reviewed-draft module, auth-kit for the admin side.
- **First milestone:** single-file demo answering ~15 approved questions from a JSON pack with "unknown → person" behavior and a receipt per answer.
- **Effort:** S–M. This is the smallest offer already published with prices, so it is the fastest path from portfolio to a repeatable product.

### P5 — `sourced-brief` service (M)

- **Goal:** productize the published WGF "sourced brief, or twenty cases" offer ([wegoforward `sourced-brief.html`](https://github.com/arigatoexpress/wegoforward/blob/main/sourced-brief.html)): one page of what sources said, URL, fetch date, counterclaim, and what would prove it wrong — "no source means the page says unknown and it is not billed."
- **Serves:** founders and small/large business clients.
- **Reuses:** cyber-threat-bot's parallel fetch/score shape, regional-intel-workbench's provenance model, AOE's source-rights envelope (module 15).
- **First milestone:** CLI that answers one question from three public sources with full provenance and an explicit "unknown" path.
- **Effort:** M.

### P6 — `portable-deploy` template pack (S)

- **Goal:** one template repo carrying the portfolio's hardened CI: docs-integrity checks, JSON validation, pinned actions with minimal permissions, secret-filename scan, plus a two-target deploy (WIF→Cloud Run *and* plain OCI→non-GCP host) so no project is born locked-in.
- **Serves:** internal first; every client project after.
- **Reuses:** this repo's `scripts/check-docs.mjs` + `.github/workflows/ci.yml`, PGF's `deploy.yml`, fedex-delivery-markets' hardening (pinned actions, minimal permissions per its README hardening note).
- **First milestone:** template repo boots a "hello" service to both targets with green CI.
- **Effort:** S.

### P7 — `ops-metrics` pack (M)

- **Goal:** package the deterministic numbers layer (priority-metrics modules, Signal Lab SPC rules, TLH/SPH decomposition) as one offline, no-network CSV-in/brief-out tool with the `connect-src 'none'` guarantee.
- **Serves:** large-business operations teams; the FedEx lane (Ops-AI-Library wrong-day-lates work is a natural consumer).
- **Reuses:** AI-Efficiency modules 11–12; this repo's P45–P48 framing (`prompts/late-arrival-and-service-recovery.md`).
- **First milestone:** one HTML/CLI tool ingesting a synthetic weekly CSV, emitting SPC flags + lever decomposition + a labeled draft brief.
- **Effort:** M.

### P8 — `receipt-ledger` (S)

- **Goal:** one tiny append-only, hash-chained receipt format with Python + TypeScript reference implementations and a verifier CLI — the shared "receipt" for aegis decisions, PGF audit events, WGF leave-behinds, and the bot fleet's receipts rule (`docs/master-plan-grok-bot-first.md` §3: "No receipt = UNKNOWN, never success").
- **Serves:** internal; large-business clients as an audit feature.
- **Reuses:** aegis receipt hash, sapphire-nexus evidence-ledger shape, PGF `audit_log.py` field discipline.
- **First milestone:** spec + two implementations + `verify` CLI passing a cross-language golden test.
- **Effort:** S.

---

## 6. Ranked refactor roadmap

Ranking criteria: (1) live-data risk first, (2) public-disclosure risk, (3) confusion removal, (4) unlocks the proposals in dependency order.

| Rank | Action | Why here | Depends on |
| --- | --- | --- | --- |
| R1 | Close PGF's self-documented secret/backup gaps: rotate `THO_API_KEY` + `N8N_API_TOKEN` into Secret Manager; enable Firestore delete protection; run the ops-bootstrap workflow (backups, alerts); confirm GCS versioning | Live client data; the exact commands are already written in [PGF SECURITY.md §2/§7](https://github.com/arigatoexpress/Project-Go-Forward/blob/main/docs/SECURITY.md) — execution, not design | — |
| R2 | Scrub home-access-kit's public topology into its gitignored `config.sh` pattern (§4 #8) | Personal network exposure in a public repo | — |
| R3 | Reconcile PGF's launch ledger with the live site (§4 #5): close or restate the five open items; do not advertise e-sign until DocuSeal is deployed | Public claims must match verified state — the portfolio's own evidence standard | R1 |
| R4 | Formalize PGF storage behind a repository interface (Firestore adapter + SQLite/Postgres adapter), growing from the existing JSON fallback | The single highest-leverage portability change; prerequisite for P1 | R1 |
| R5 | Build the neutral model gateway (the planned "Track B `ari-llm`" — rename per [NAMING.md](../NAMING.md)) as an OpenAI-compatible seam; point Tex and AI-Efficiency's `gemini-config.ts` pattern at it | Removes the deepest vendor lock-in (model + agent framework) | R4 |
| R6 | Extract `storefront-kit` (P1) from PGF once R4–R5 land | Turns the one paying-client build into the repeatable small-business product | R4, R5 |
| R7 | Adopt aegis in PGF (P2) and publish the receipt-ledger spec (P8) | Security + audit story for every client conversation; small and independent | — (can run parallel to R4) |
| R8 | Dedup the prompt libraries into `prompt-pack` (P3) | Two libraries (52 vs 49 prompts) will keep drifting; cheap to fix now | — |
| R9 | Build `answer-appliance` (P4) on P2+P3 | Smallest published, priced offer; validates the composable stack end-to-end | R7, R8 |
| R10 | Refresh stale public identity surfaces: profile README (four dead repo links), wegoforward repo description (domain is live), PGF README badge (legacy origin) | Cheap confusion removal; see [NAMING.md](../NAMING.md) discrepancy list | — |
| R11 | Decide RECON's fate per `docs/product-portfolio-boundaries.md`: promote to its own repo with CI + deploy identity, or mark the AI-Efficiency copy historical | Boundary doc already prescribes the promotion bar; today it is in limbo | — |
| R12 | Package `ops-metrics` (P7) and `sourced-brief` (P5) | Both are M-size extractions from archived/parked repos; do them only when a client or the FedEx lane pulls | R8 |
| R13 | Leave the archived fleet archived; verify the cyber-threat-bot Cloud Run service is decommissioned (§4 #10); delete nothing without owner review | Archived repos cost nothing; live unmaintained endpoints do | — |

---

## Appendix — evidence map

- This repo: `README.md`, `AGENTS.md`, `CHANGELOG.md`, `docs/product-portfolio-boundaries.md`, `docs/master-plan-grok-bot-first.md`, `docs/sharepoint-contribution-register-2026-10-01.md`, `appendix/prior-example-projects.md`, `concepts/README.md`, `scripts/check-docs.mjs`, `.github/workflows/ci.yml`, `prompts/prompts.json` (49 prompts).
- Project-Go-Forward: `README.md`, `AGENTS.md`, `LAUNCH_READINESS.md`, `docs/ARCHITECTURE.md`, `docs/SECURITY.md`, `docs/GCP_ENTERPRISE_PLAN.md`, `docs/DNS_CUTOVER_RUNBOOK.md`, `docs/CUTOVER_GUIDE.md`, full file tree, closed PR list through [#370](https://github.com/arigatoexpress/Project-Go-Forward/pull/370).
- AI-Efficiency: `README.md`, `docs/building-blocks.md`, closed PR list through [#107](https://github.com/arigatoexpress/AI-Efficiency/pull/107).
- wegoforward: all six pages (`index.html`, `answers.html`, `one-workflow.html`, `sourced-brief.html`, `workshop.html`, `x402.html`) plus live-site check.
- fedex-delivery-markets: `README.md`, `AGENTS.md`, `docs/PRODUCT_BOUNDARY.md`, `docs/SECURITY_AND_COMPLIANCE.md`.
- aegis, home-access-kit, gunnison-fishing-guide: full READMEs; aegis file tree.
- All 39 archived repos: READMEs (or repo descriptions where no README exists, e.g. `sovereign-windows-worker`).
- Live checks 2026-10-07: `www.texashomeoutlet.com` 200; `sapphirealpha.xyz` 200; `tho.sapphirealpha.xyz` 200; `wegoforward.app` 200 (Cloudflare-fronted).
