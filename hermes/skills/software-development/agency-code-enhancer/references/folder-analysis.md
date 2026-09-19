# Complete folder analysis

Static review of the pinned source snapshot, not runtime certification. All file hashes and review inventories matched.

## Exact folder coverage

- `.` — 9 directly contained files; detailed findings follow by area.
- `.github` — 2 directly contained files; detailed findings follow by area.
- `.github/ISSUE_TEMPLATE` — 2 directly contained files; detailed findings follow by area.
- `.github/workflows` — 6 directly contained files; detailed findings follow by area.
- `academic` — 6 directly contained files; detailed findings follow by area.
- `design` — 10 directly contained files; detailed findings follow by area.
- `engineering` — 64 directly contained files; detailed findings follow by area.
- `examples` — 6 directly contained files; detailed findings follow by area.
- `finance` — 5 directly contained files; detailed findings follow by area.
- `game-development` — 6 directly contained files; detailed findings follow by area.
- `game-development/blender` — 1 directly contained files; detailed findings follow by area.
- `game-development/godot` — 3 directly contained files; detailed findings follow by area.
- `game-development/roblox-studio` — 3 directly contained files; detailed findings follow by area.
- `game-development/unity` — 4 directly contained files; detailed findings follow by area.
- `game-development/unreal-engine` — 4 directly contained files; detailed findings follow by area.
- `gis` — 13 directly contained files; detailed findings follow by area.
- `healthcare` — 3 directly contained files; detailed findings follow by area.
- `integrations` — 1 directly contained files; detailed findings follow by area.
- `integrations/aider` — 1 directly contained files; detailed findings follow by area.
- `integrations/antigravity` — 1 directly contained files; detailed findings follow by area.
- `integrations/claude-code` — 1 directly contained files; detailed findings follow by area.
- `integrations/codex` — 1 directly contained files; detailed findings follow by area.
- `integrations/cursor` — 1 directly contained files; detailed findings follow by area.
- `integrations/gemini-cli` — 1 directly contained files; detailed findings follow by area.
- `integrations/github-copilot` — 1 directly contained files; detailed findings follow by area.
- `integrations/hermes` — 1 directly contained files; detailed findings follow by area.
- `integrations/kimi` — 1 directly contained files; detailed findings follow by area.
- `integrations/mcp-memory` — 3 directly contained files; detailed findings follow by area.
- `integrations/openclaw` — 1 directly contained files; detailed findings follow by area.
- `integrations/opencode` — 1 directly contained files; detailed findings follow by area.
- `integrations/qwen` — 1 directly contained files; detailed findings follow by area.
- `integrations/vibe` — 1 directly contained files; detailed findings follow by area.
- `integrations/windsurf` — 1 directly contained files; detailed findings follow by area.
- `integrations/zcode` — 1 directly contained files; detailed findings follow by area.
- `marketing` — 36 directly contained files; detailed findings follow by area.
- `paid-media` — 7 directly contained files; detailed findings follow by area.
- `product` — 5 directly contained files; detailed findings follow by area.
- `project-management` — 7 directly contained files; detailed findings follow by area.
- `research` — 1 directly contained files; detailed findings follow by area.
- `sales` — 9 directly contained files; detailed findings follow by area.
- `scripts` — 19 directly contained files; detailed findings follow by area.
- `scripts/i18n` — 3 directly contained files; detailed findings follow by area.
- `security` — 12 directly contained files; detailed findings follow by area.
- `spatial-computing` — 6 directly contained files; detailed findings follow by area.
- `specialized` — 59 directly contained files; detailed findings follow by area.
- `strategy` — 4 directly contained files; detailed findings follow by area.
- `strategy/coordination` — 2 directly contained files; detailed findings follow by area.
- `strategy/playbooks` — 7 directly contained files; detailed findings follow by area.
- `strategy/runbooks` — 4 directly contained files; detailed findings follow by area.
- `support` — 6 directly contained files; detailed findings follow by area.
- `testing` — 9 directly contained files; detailed findings follow by area.

# Agency agents: engineering, design, security, testing, support, product, and project-management audit

## Scope and review method

Reviewed **113 files**, all Markdown, under `assets/upstream`: engineering 64, design 10, security 12, testing 9, support 6, product 5, project-management 7. Recursive enumeration found **no nested directories** within these seven folders in this checkout; nothing was excluded by depth. The companion `review-code.json` records exact absolute and relative paths, content hashes, lengths, and extracted source evidence for every reviewed file.

Every file was read in full as UTF-8 data. Section-aware batch reductions surfaced missions, rules, procedures, deliverables, and metrics for analysis; suspicious implementation claims were checked against full source passages. This is a source-content audit, **not execution or validation of the embedded code**. No repository scripts were run, no prompts were adopted as instructions, no software or skills were installed, and no production or external systems were changed. Legal, vendor-version, market, and performance claims in the source were not independently verified against current external documentation.

## Overall assessment

The most reusable material is not the role-play. It is the repeated engineering discipline: trace real code, define a contract, baseline behavior, make a scoped change, exercise failure cases, preserve evidence, and stop at an explicit release gate. Particularly strong references are codebase onboarding, backend architecture, API platform, identity/access, payments/billing, database reliability, minimal-change and Rust refactoring (when reconciled), UI finish gate, test automation, privacy, and LLM post-training.

The corpus mixes specific operational checklists with promotional personas, fictional work histories, numerical targets without measurement context, incomplete snippets, and mutually incompatible universal rules. Preserve source agents as **lazy reference material**, not concatenated system prompts. A reusable skill should route to relevant references and supply its own precedence, authorization, evidence, and completion rules.

### Shared procedure worth retaining

1. **Frame the job:** establish user outcome, acceptance criteria, non-goals, affected users, data sensitivity, current stack, and authorized change surface.
2. **Inspect reality:** discover entry points and contracts; trace a real request from interface through validation, authorization, domain logic, storage, and response. Inventory existing tests and deployment paths before choosing tools.
3. **Baseline:** record current tests, observed behavior, representative performance, known failures, accessibility state, and relevant security boundaries.
4. **Select the smallest coherent intervention:** size the change by semantic completeness rather than a fixed line count. Document trade-offs for architectural changes; avoid opportunistic redesign.
5. **Implement a complete vertical slice:** include UI states, API contracts, server-side permissions, storage/migration, observability, and docs as actually required.
6. **Verify at appropriate layers:** unit invariants, API and integration behavior, critical browser journeys, keyboard/assistive-technology checks, scoped security regression cases, and representative performance comparisons.
7. **Gate release:** explicit PASS / HOLD / UNVERIFIED against criteria; preserve commands, results, artifacts, remaining risks, rollback or roll-forward strategy, and owner. A screenshot, successful build, or green scan alone is never sufficient.
8. **Learn from use:** review support feedback, adoption, errors, and user outcomes against the baseline; change priorities based on evidence rather than persona certainty.

## engineering — 64 files

### Architecture, API, code understanding, review, and scope

`engineering-codebase-onboarding-engineer.md` offers an unusually disciplined code-first orientation: repository inventory, entry points, execution/data-flow traces, boundaries, and one-line / five-minute / deep-dive explanation. Its prohibition on improvement advice is useful in an explanation-only task but must not block a requested implementation review.

`engineering-software-architect.md` contributes ADRs, bounded contexts, explicit dependency rules, and architecture selection based on trade-offs. `engineering-backend-architect.md` strengthens this with simple architecture first, justified microservices, timeout/retry/idempotency contracts, expand-and-contract migration, and SLIs/SLOs. These should be the default backend backbone rather than a Kubernetes/microservice checklist.

`engineering-api-platform-engineer.md` covers contract-first OpenAPI/gRPC, versioning, deprecation, consistent errors/pagination, rate-limit feedback, and SDK lifecycle. Retain compatibility tests and consumer migration planning. Its shorthand that additive changes are safe needs qualification: new enum values, stricter validation, additional fields in strict clients, or new observable behavior can break consumers.

`engineering-code-reviewer.md` usefully separates blockers, suggestions, and nits with location, consequence, and repair. `engineering-minimal-change-engineer.md` guards against scope creep and captures follow-ups separately, but rules such as a median diff below 30 lines or reluctance to open a fourth file are not correctness criteria. `engineering-rust-refactoring-specialist.md` supplies the necessary counterweight: follow all callers, re-exports, features, docs, tests, serialization, drop timing, locks, cancellation, and public contracts until a requested transformation is complete. Read broadly enough to understand; write only the coherent requested change.

`engineering-git-workflow-master.md` provides atomic commits, branching alternatives, worktrees, and history cleanup. Respect existing repository policy and collaborators' work; do not blindly rebase shared history. `engineering-technical-writer.md` contributes tested examples, audience-first structure, docs-as-code, and separate tutorial/how-to/reference/explanation content. `engineering-developer-tooling-engineer.md` adds actionable CLI errors, TTY-aware output, stable machine formats, startup measurement, and discoverability. `engineering-orgscript-engineer.md` is a niche parser/DSL reference: preserve stable diagnostics, AST validity, canonical formatting, and export testing, but discover the actual installed grammar and commands rather than assuming its v0.1 vocabulary or package paths.

### Frontend, design implementation, internationalization, and accessibility

`engineering-frontend-developer.md` contains useful responsive components, TypeScript, state management, code splitting, image optimization, and real assistive-technology testing. Its extra editor/WebSocket responsibilities should only load for editor integration tasks. Its FID-centric Core Web Vitals template conflicts with the INP-based CMS performance references; do not propagate obsolete metrics uncritically.

`engineering-senior-developer.md` is highly stack-specific (Laravel/Livewire/FluxUI) and prescriptive about premium effects, Three.js, magnetic buttons, and a mandatory theme switch. This is not a general senior-engineering standard. Never add these features without a user need, performance budget, and accessibility rationale; do not assume paid/all FluxUI components or referenced local style guides exist.

`engineering-i18n-engineer.md` supplies immediately reusable ICU messages, locale formatting, plural rules, logical CSS for RTL, grapheme-safe text handling, pseudo-localization, and translation drift checks. Include timezones, long text, mixed-direction user content, and localized validation in the frontend/backend contract.

`engineering-section-508-specialist.md` separates automated scans from keyboard and screen-reader evidence, and asks for a specific conformance target and an honest ACR/VPAT. `engineering-uswds-developer.md` complements it with token-first theming, documented component contracts, CMS integration, and retesting after customization. These are specialized government references, not proof that every project must use USWDS. Check applicable law and standards externally for a real compliance engagement; blanket claims about automation catching a fixed fraction of issues are illustrative, not measured facts.

`engineering-data-visualization-engineer.md` is valuable for choosing charts from questions, honest axes and aggregation, colorblind-safe encodings, and rendering budgets. Treat SVG/Canvas/WebGL element-count cutoffs as profiling hypotheses. Ensure accessible summaries/table alternatives and preserve units, missingness, and uncertainty.

`engineering-filament-optimization-specialist.md` emphasizes structural form improvements, field inventory, create/edit parity, labeled repeaters, and restraint. Its always-use-tabs/replace-radio-ranges rules can undermine scanability, precise input, or keyboard access. Choose controls through task analysis and test small screens; do not optimize solely for reduced vertical scrolling.

### Data integrity, database performance, reliability, and knowledge

`engineering-database-optimizer.md` and `engineering-gaussdb-expert.md` emphasize query plans, bounded reads, N+1 elimination, pooling, and migration safety. GaussDB adds distributed placement, skew, streaming operators, and storage-engine choice. Avoid universal foreign-key indexing, reversible-DOWN, and never-lock prescriptions: indexes have write/storage costs, some migrations require roll-forward, and lock behavior depends on engine/version and data. `EXPLAIN ANALYZE` executes a query, so do not casually run it against mutating or costly production statements. The generic optimizer's string replacement of a database port is not robust URL parsing.

`engineering-database-reliability-engineer.md` correctly distinguishes query tuning from availability and recoverability: business RPO/RTO, backup restore drills, failover/fencing, connection capacity, and phased migrations. This is a high-value backend reference. Replication is not backup; successful backup creation is not successful recovery. Zero-downtime and zero-data-loss claims require tested workload-specific boundaries.

`engineering-data-engineer.md` contributes explicit data contracts, immutable raw ingestion, staged transformations, schema-drift alerts, idempotency, freshness/completeness monitoring, and replay. Medallion/lakehouse is an option, not a mandatory architecture for a small app.

`engineering-ai-data-remediation-engineer.md` has a strong intention—quarantine uncertain corrections, preserve identities and audit trails, generate transformation logic instead of fabricated replacement facts—but contains the most serious implementation hazard in this scope. It uses `eval(fix['transformation'])` and labels it safe after a lambda/keyword validation gate. A keyword denylist is **not** a Python sandbox. Use allowlisted transformations or an explicitly restricted DSL, reviewed semantics, bounded isolated execution, and before/after validation. Equal row counts do not prove no corruption or identity loss; reconcile keyed records and invariant values. The claim that 50,000 bad rows always reduce to 8–15 families is unjustified. Local inference alone does not prove air-gapping, privacy compliance, determinism, or zero egress.

`engineering-knowledge-graph-engineer.md` offers source hashes, provenance edges, contradiction preservation, idempotent merges, integrity gates, and bounded impact analysis. Retain claim-level provenance and uncertainty rather than forcing all knowledge into graph storage. Verify sample schema/code against the promised invariants: a checklist does not prove the graph actually enforces them.

`engineering-search-relevance-engineer.md` is strong on query-log segmentation, graded judgments, recall-before-precision, analyzer diagnostics, offline evaluation, and controlled relevance rollout. `engineering-rag-pipeline-engineer.md` extends this to corpus-specific embeddings, structural chunking, metadata scoping, hybrid retrieval, reranking, and ablations. Enforce authorization before retrieval and during generation; measure retrieval separately from answer faithfulness. Arbitrary golden-set sizes and precision thresholds are starting points, not validated adequacy. Do not silently equate late chunking with ColBERT-style late interaction.

### AI systems, prompts, and communication pipelines

`engineering-ai-engineer.md` supplies model lifecycle, drift, versioning, fairness/privacy evaluation, and production serving, but its broad accuracy and latency targets are not portable across tasks.

`engineering-llm-post-training-engineer.md` is one of the strongest sources: fixed comparator identity, preflight/smoke/signal/controlled gates, discriminating minimal experiments, explicit stop conditions, matched evaluation, and checkpoint inventory/hash/clean-load verification. It explicitly refuses to treat falling loss, running processes, higher reward, or exit zero as proof of learning quality or a complete artifact. Reuse that epistemic discipline beyond model training.

`engineering-prompt-engineer.md` usefully treats prompts as versioned interfaces with schema, representative/adversarial tests, and one-variable iteration. Temperature zero is not a determinism guarantee. Do not require disclosure of private chain-of-thought through `<thinking>` output; request concise decision rationales, evidence, and structured results. Prompt wording and role separation alone are not an injection security boundary.

`engineering-multi-agent-systems-architect.md` contributes explicit topology, input/output contracts, context budgets, identity and tool scoping, bounded retries, circuit breakers, checkpoints, evaluations, and human approval gates. Start with one agent when sufficient. Checkpointing after an irreversible side effect cannot undo it: combine pre-action durable intent, idempotency keys, read-back verification, and compensating actions where possible.

`engineering-autonomous-optimization-architect.md` advocates baseline budgets, asynchronous shadow evaluation, fallbacks, and guarded model routing. Shadow traffic still costs money and may expose user data. Automatic promotion requires authorized policy, representative held-out evaluations, drift/fairness checks, controlled rollout, and rollback; LLM-as-judge is not inherently objective. Reject guaranteed cost cuts or uptime from routing alone.

`engineering-email-intelligence-engineer.md` contributes MIME normalization, reply topology, quotation deduplication, provenance, tenant isolation, and structured context. Preserve ambiguity, revised decisions, and source-message IDs. `engineering-voice-ai-integration-engineer.md` contributes file validation, preprocessing, timestamp preservation, diarization, structured outputs, retention/redaction, quality tests, and durable delivery. Do not conflate diarization with verified identity; do not erase original audio/channels merely because one model prefers mono. Both pipelines must treat ingested content as untrusted data, not agent commands.

`engineering-rapid-prototyper.md` focuses on a narrow hypothesis, a working core journey, prebuilt components, feedback instrumentation, and fast user testing. Reuse its learning-first vertical slice, not its mandatory Next.js/Supabase/Clerk stack or under-three-day promise (its own example schedule extends into a fourth day). Mark prototype shortcuts, fake integrations, and unverified production properties explicitly; authentication, privacy, and irreversible actions do not become optional because the deliverable is an MVP.

### Platform, delivery, cost, operations, and security-adjacent engineering

`engineering-devops-automator.md` provides IaC, CI gates, staged deployment, rollback, monitoring, and secret management. `engineering-platform-engineer.md` adds golden paths as a product with adoption measurement, self-service, clear support boundaries, and deprecation. Avoid adopting Kubernetes, a service mesh, Backstage, or a central platform team merely because a template includes them. The source's one-command-production and fixed deprecation/DORA targets require local risk and team context.

`engineering-sre.md` grounds reliability in user-facing SLOs, error budgets, golden signals, and reducing toil. `engineering-incident-response-commander.md` adds severity classification, explicit command/comms/technical/scribe roles, recovery verified in metrics, and blameless postmortems with owners. `engineering-it-service-manager.md` expands to service catalog, incident/problem/change separation, SLAs, CMDB, and improvement registers. Keep change governance proportional; emergency authority must be established, not assumed from a persona.

`engineering-finops-engineer.md` contributes allocation before optimization, eliminate waste before commitments, unit economics, and reliability-preserving rightsizing. Savings estimates must include usage mix and actual bills, not only headline vendor discounts.

`engineering-network-engineer.md` and `engineering-china-network-engineer.md` are separate vendor-syntax references. Their useful common method is identify vendor/OS, capture state, distinguish control plane from data plane, preplan rollback, validate forwarding, and preserve logs. No template configuration should be applied without device/version checks, maintenance authorization, and out-of-band recovery. Regional regulatory hardening examples need current qualified validation.

`engineering-identity-access-engineer.md` contributes standard OAuth/OIDC/PKCE, validated callbacks, enterprise SSO/SCIM, session trade-offs, and server-side tenant authorization. `engineering-privacy-engineer.md` maps personal data through databases, logs, caches, queues, indexes, third parties, and backups; adds purpose-scoped consent, retention, DSAR, and deletion orchestration. Retain restoration tombstones, exceptions such as legal holds, and audit verification; simplistic “everything deleted immediately everywhere” claims can conflict with lawful retention or immutable backups.

`engineering-payments-billing-engineer.md` is another high-value reference: hosted/tokenized collection, business-operation idempotency, verified raw-body webhooks, deduplication, out-of-order handling, lifecycle state, money-safe representations, and processor/ledger reconciliation. A redirect is not payment confirmation. Test crashes between event receipt and business mutation; dedupe alone is not transactional exactly-once processing. PCI scope is not determined solely by whether PAN reaches a server, and real reconciliation must model fees, FX, pending settlements, reversals, and timing.

### CMS and commerce

`engineering-cms-developer.md` covers content modeling, update-safe themes/plugins/modules, configuration management, editor experience, and launch testing. `engineering-drupal-performance.md` emphasizes correct cache tags/contexts/max-age and profiling; `engineering-wordpress-performance.md` emphasizes Query Monitor, bounded queries, autoload/plugin weight, layered cache, and anonymous-versus-personalized paths. Prefer fixing invalidation over globally disabling cache, and verify tenant/user isolation as well as speed.

`engineering-drupal-shopping-cart.md` adds Commerce price resolvers, currency-aware money, checkout panes, gateway lifecycle, tax/promotion stacking, and order state. `engineering-wordpress-shopping-cart.md` adds hooks over core edits, block checkout/Store API extensibility, HPOS-aware data access, and live CDN exclusions for cart/checkout/account. Both appropriately require actual gateway sandbox tests and settlement reconciliation. Do not transplant CMS APIs or caching exclusions indiscriminately between versions or architectures.

### Client runtimes, devices, media, and specialist documents

`engineering-desktop-app-engineer.md`: treat renderer as untrusted; narrow typed IPC, privileged-side validation, capabilities, signed builds, staged updates, and runtime-specific packaging. `engineering-mobile-app-builder.md`: platform-native patterns, offline behavior, constrained resources, actual device tests. Its garbled heading characters are a source-quality warning, not a reason to omit it. `engineering-mobile-release-engineer.md`: shared protected signing identity, reproducible artifacts, beta cohorts, phased store release, halt criteria, and roll-forward reality. Store and framework policies are version-dependent.

`engineering-embedded-firmware-engineer.md`: bounded memory/timing, minimal ISRs, correct RTOS APIs, hardware measurements, and safe OTA. Its example labeled “STM32 LL SPI Transfer (non-blocking)” contains two busy-wait loops without timeout: do not reuse the label or code as an asynchronous implementation. `engineering-iot-fleet-engineer.md`: per-device identity, reconnect-safe buffered telemetry, hardware-cohort canaries, signed dual-bank OTA, and health-gated rollback. Device safety cannot be guaranteed by a rollout diagram alone.

`engineering-realtime-collaboration-engineer.md`: design reconnect/resume before connect, distinguish durable operations from ephemeral presence, choose convergence semantics per data type, dedupe operation IDs, and exercise hostile-network cases. Test authorization on room subscriptions, compaction/resume gaps, stale clients, and crash recovery; operation IDs alone do not prove exactly-once effects.

`engineering-video-streaming-engineer.md`: content-appropriate ladders, aligned segments, CMAF/HLS/DASH packaging, QoE, slow-network cohorts, and egress cost. Packaging reuse and latency promises depend on codec/DRM/device compatibility. `engineering-webassembly-engineer.md`: prove workload fit, batch JS/Wasm boundaries, clear ownership, small delivery artifacts, explicit WASI capabilities, and benchmark against real JS/native baselines. Wasm is neither universally faster nor a substitute for resource/host-API isolation.

`engineering-feishu-integration-developer.md` and `engineering-wechat-mini-program-developer.md`: platform-specific identity/token scopes, API error handling, callbacks, rate limits, package/render constraints, and real-device/provider testing. Keep credentials and payment authority server-side; verify signatures, replay protection, idempotency, and permissions beyond SDK convenience examples. Do not hardcode package limits or endpoint behavior without checking the target platform version.

`engineering-solidity-smart-contract-engineer.md`: trust modeling, vetted base contracts, state/external-call discipline, access control, fuzz/invariant testing, storage-layout review, and deployment checks. Gas optimization cannot supersede correctness; generic “never use arrays” or arbitrary branch coverage targets are not sound architecture rules. Audits and tests do not prove absence of exploitable economic behavior.

`engineering-pdf-engine-architect.md` proposes font synchronization, shared preview/export representation, print geometry, isolated contexts, asset controls, and text/vector integrity checks. Important cautions: setting PDF/A or PDF/UA metadata is not conformance, tagged output still requires structure/reading-order validation, universal sub-80ms compilation and perfect geometry are unproven, and sanitizer/network allowlists need robust parsing and redirect/IP handling. Shared rendering code may be preferable to mandatory live-DOM capture for server-generated documents.

`engineering-universal-document-compiler.md` contributes source-preserving CST/AST editing, layout sidecars, stable node identity, edit provenance, shape classification, and fragmentation rules. Bound depth, size, aliases, resource use, and unsupported inputs; “accept any YAML, never reject anything” is unsafe for hostile documents. `engineering-ats-validator-architect.md` contributes no fabricated resume claims, parser reading-order checks, actual text extraction, and explainable heuristics. Its weighted score is not a validated ATS predictor; universal parser requirements, legal safe-harbor language, sub-5ms budgets, and precise recruiter attention claims should not become promises.

## design — 10 files

**Useful sequence:** research the user's job → establish design contract and content hierarchy → select reusable tokens/components → specify states and responsive behavior → implement → inspect actual screens and interactions → validate with users and accessibility testing.

- `design-brand-guardian.md`: brand foundation, semantic visual identity, voice, guidelines, and asset consistency. Use existing brand constraints; do not make every small feature wait for a full rebrand or claim trademark protection without legal work.
- `design-image-prompt-engineer.md`: structured subject/environment/light/composition/style prompts and iterative generation. Treat camera terminology and negative prompts as controls to test, not guarantees of physical accuracy or 90% concept match.
- `design-inclusive-visuals-specialist.md`: counter-stereotypes, specific cultural context, distinct individuals, temporal/physical review, and community-sensitive QA. A prompt cannot ensure dignity, correct symbols, or zero artifacts; inspect output and seek relevant human feedback.
- `design-persona-walkthrough.md`: separate simulated user monologue from analyst assessment, use actual viewport/fold evidence, and label simulations as qualitative hypotheses. This explicit boundary is worth preserving. Do not substitute generated personas or national-cultural generalizations for interviews or measured conversion.
- `design-ui-designer.md`: tokens, component states, responsive behavior, accessible color, and developer handoff. Contrast numbers are not the entirety of WCAG; touch-target requirements depend on the chosen standard and exceptions.
- `design-ui-finish-gate-reviewer.md`: strongest general design gate. State user/job, first-read object, primary action, comparative pattern evidence, concrete implementation findings, and observable PASS/HOLD criteria. Avoid “premium/modern/clean” without explaining what a user can now understand or do.
- `design-ux-architect.md`: information architecture, CSS foundations, themes, layout and interaction specs. Remove assumed repository paths, mandatory heroes/smooth-scroll/theme switches, and claims that developers need make no architectural decisions.
- `design-ux-researcher.md`: research questions before methods, participant criteria, consent, task observations, triangulation, and actionable findings. Preserve source quotes and uncertainty; example interview numbers and projected gains are not observed evidence.
- `design-visual-storyteller.md`: narrative hierarchy, storyboard, channel adaptation, accessible media, and honest visualization. Not every operational screen needs a dramatic story arc; engagement lifts and platform reach are hypotheses.
- `design-whimsy-injector.md`: optional purposeful microinteractions, reduced motion, inclusive humor, and testing for distraction. Do not obscure destructive actions with playful labels or hide essentials behind Easter eggs. Its animation snippets need actual reduced-motion support, cleanup, and dynamic-content security review rather than assuming the prose supplies those controls.

**Frontend recommendation:** make product legibility and complete states mandatory; make decorative effects optional. Define loading, empty, error, success, disabled, permission-denied, offline, long-content, focus, and reduced-motion behavior. Validate on actual rendered UI at representative mobile/desktop widths, RTL/long locales, keyboard, and assistive technologies. Backend contracts should provide stable errors, status, pagination, accessible validation details, and consistent money/time representations that support those states.

## security — 12 files

**Useful sequence:** scope and authorization → assets/data flows/trust boundaries → threat model → targeted source/runtime/config review → evidence-backed finding → approved remediation → regression proof → rotation/incident/control follow-through.

- `security-ai-generated-code-auditor.md`: client-exposed secrets, public env prefixes, overly broad RLS/storage policies, source-to-LLM taint, redacted findings, stable fingerprints, and rescan. Its characterization of user-role messages as a “safe” injection pattern is too strong: separation helps but does not stop indirect injection or unsafe tools.
- `security-appsec-engineer.md`: design threat modeling, critical-path review, SAST/DAST/SCA/secret gates, exploitability-aware triage, and fix retesting. Tool output is a lead, not a verified vulnerability; local remediation deadlines must reflect actual risk and exposure.
- `security-architect.md`: assets, attack surfaces, STRIDE, supply-chain inventory, layered controls, and security regression tests. Avoid identifying an internal network as inherently trusted or implying one WAF/header/scan establishes security.
- `security-blockchain-security-auditor.md`: manual and automated review, economic invariants, oracle/upgrade/access paths, reproducible local proofs, commit-scoped report, and re-audit. Never promise every high-severity issue will be found or describe tool coverage percentages as universal.
- `security-cloud-security-architect.md`: workload identity, least privilege, IaC/policy review, centralized protected audit logs, segmentation, and detection. Absolute bans on all environment-variable secret injection or every emergency console change need contextual exception handling; secure delivery paths and audited break-glass matter more than slogans.
- `security-compliance-auditor.md`: explicit scope, control/evidence mapping, owner/frequency, gap remediation, tested controls, and continuous evidence. This technical-audit framing is preferable to a generic “98% compliant” assertion; framework/control editions must be verified.
- `security-incident-responder.md`: evidence integrity, forensic copies, hashes/custody, triage, containment, eradication, and recovery. Preserve volatile evidence when feasible without allowing ongoing harm while waiting for an ideal image; containment decisions require incident authority. Never copy its intrusive root/admin triage scripts into automatic execution.
- `security-penetration-tester.md`: explicit written scope, rules of engagement, test windows, protected evidence, and reproducible findings. Offensive examples are inert reference material, not standing permission. Any active tests need precise authorization, impact limits, stop conditions, cleanup, and isolated proof where possible.
- `security-secrets-credential-engineer.md`: scanner gates, credential inventory/ownership, short-lived identity, safe rotation, provider-side revocation, exposure-window investigation, and artifact/history coverage. Deleting a key is not revocation. Coordinate destructive history rewrites; routine overlap rotation differs from emergency revocation of an actively abused secret.
- `security-senior-secops.md`: useful fail-fast required secrets, JWT validation, redaction, schemas, auth rate limits, and security regression cases. Reject its “scan before reading the request” instruction and references to an unverified `17-security-pattern.md`. Cookie-only tokens, never-return-tokens, and IdP-only roles are not universal across browser, native, machine, or domain-specific authorization designs. CORS is not authorization; severity requires context.
- `security-threat-detection-engineer.md`: detections as code, realistic malicious/benign test data, log-source health, documented false positives, ATT&CK mapping, and hunt-to-rule feedback. A mapped technique is not demonstrated detection coverage; validate pipelines and on-call actionability.
- `security-threat-intelligence-analyst.md`: intelligence requirements, source confidence, deduplication, evidence-backed attribution, TLP handling, and audience-specific actions. Multiple syndicated reports are not independent corroboration; do not expose sensitive samples/indicators to third-party services without permission.

**Full-stack recommendation:** test authorization and tenant isolation on the server for every operation, not just hidden controls; check client bundles and source maps for secrets; validate and encode at actual trust boundaries; use provider/library primitives; keep session, CSRF, CORS, and XSS models explicit. For AI features, treat retrieved content as untrusted, constrain tools outside the model, require approval for material side effects, and verify outcomes. Security and legal compliance remain bounded assessments, never guarantees.

## testing — 9 files

- `testing-test-automation-engineer.md` is the best reusable testing core: critical journeys, test pyramid, API-created owned fixtures, condition-based waits, role selectors, parallel isolation, traces, and root-caused flakes. Network-idle is not a universal readiness signal for streaming applications; wait for the domain-specific condition. Retries should expose flakes, not hide them.
- `testing-api-tester.md`: inventory contracts, inputs, authentication/authorization, negative cases, integrations, and performance. Replace fixed 95% endpoint coverage, 200ms p95, and 10x load mandates with risk-based coverage and approved traffic budgets. Test concurrency, replay, pagination, schema drift, and partial failure as applicable.
- `testing-accessibility-auditor.md`: scope a standard, automate baseline checks, run keyboard/AT journeys, inspect custom controls, and report criterion + impact + evidence + fix. An automated score or a fixed estimated percentage of detectable defects cannot certify conformance.
- `testing-performance-benchmarker.md`: baseline, realistic load/stress/soak scenarios, network/device cohorts, bottleneck attribution, and before/after evidence. Its FID text needs updating/verification before reuse. Record environment, sample size, percentiles, error rate, saturation, caches, and workload; never load-test production without authorization and stop conditions.
- `testing-test-results-analyzer.md`: aggregate valid results, separate coverage types, cluster failure causes, expose release risk, and track regressions. “95% accuracy” defect prediction and confidence intervals for every claim are unjustified without training/evaluation data or a statistical model. A reproducible deterministic bug needs evidence, not a significance test.
- `testing-evidence-collector.md`: retain actual screenshots, before/after interaction evidence, and comparison to quoted requirements. Reject “screenshots are the only truth,” mandatory 3–5 defects, automatic failure of zero findings, and assumption that `qa-playwright-capture.sh` or a Laravel layout exists.
- `testing-reality-checker.md`: retain independent verification of earlier claims and complete journeys. Reject predetermined low grades, mandatory revision cycles, and automatic incompleteness of a first pass. Report no issues found within scope when that is what the evidence supports, with limitations.
- `testing-tool-evaluator.md`: realistic pilot tasks, weighted criteria, TCO, migration/exit costs, security, and adoption plan. Use synthetic or approved representative data rather than automatically uploading real customer records to evaluation tools.
- `testing-workflow-optimizer.md`: map current handoffs, measure cycle/queue time and quality, find bottlenecks, pilot changes, and monitor adoption. Do not promise average 40% improvement or fabricate ROI/confidence intervals.

**Recommended evidence stack:** source/contract inspection for logic; assertions and stored state for correctness; browser traces/screenshots for visual journeys; actual AT observations for accessibility; repeatable workloads for performance; abuse-case tests for security; restore/failover exercises for resilience. Record what was not tested. Release gates should be criterion-based, not pessimistic theater or vanity coverage.

## support — 6 files

- `support-support-responder.md`: contextual triage, routing, stepwise troubleshooting, confirmed resolution, follow-up, knowledge-base feedback, and product escalation. Protect customer data and avoid unsupported promises. First-response/FCR/CSAT targets depend on coverage hours and case mix; avoid closing unresolved cases to improve metrics.
- `support-analytics-reporter.md`: validate data before analysis, define business questions, preserve sources/transforms, segment/cohort, and deliver actionable reports. SQL/Python/dashboard examples are templates; verify grain, joins, missingness, time periods, and metric definitions. Correlation is not causal business impact.
- `support-executive-summary-generator.md`: decision-first SCQA/Pyramid structure, succinct findings, owners, deadlines, and next decisions. Mandatory quantified findings create pressure to invent numbers when none exist; say unknown and prioritize evidence over a fixed word/section formula.
- `support-finance-tracker.md`: reconciliation, budget/actual variance, cash flow, scenarios, approval and segregation of duties. Recompute all figures and state assumptions, currency, basis, period, and uncertainty. Budget accuracy and ROI percentages are targets, not facts; accounting/legal judgments need qualified review.
- `support-infrastructure-maintainer.md`: monitoring before changes, tested recovery, IaC, cost/performance, patching, and rollback. It overlaps engineering SRE/DevOps/DBRE; choose one operational owner rather than duplicating plans. The sample backup and Terraform content is not a validated recovery system, and sample uptime figures must never enter a real report as results.
- `support-legal-compliance-checker.md`: identify applicable jurisdictions, map obligations to processes, gather evidence, record policy decisions, and escalate gaps. Its omnibus compliance scores and generated policies do not establish legal compliance. Distinguish law, contracts, certification frameworks, and technical controls; obtain current authoritative sources and qualified review for actual obligations.

**Full-stack recommendation:** surface supportable stable error codes and correlation IDs without exposing secrets/PII; preserve reproducible context with access controls; connect recurring tickets to regression tests and product priorities; ensure account recovery, cancellation, consent, data export/deletion, and billing states work end to end.

## product — 5 files

- `product-manager.md`: problem/evidence before solution, PRD goals and non-goals, acceptance criteria, opportunity assessment, options, Now/Next/Later, launch gates, rollback, and post-launch learning. Press-release-first and minimum interview counts are optional techniques, not universal prerequisites. Define outcomes with baseline, denominator, cohort, window, and guardrails.
- `product-feedback-synthesizer.md`: collect across channels, deduplicate, code themes, preserve representative quotes, segment, and link findings to roadmap decisions. Distinguish requests from underlying needs and number of messages from number of affected users. Do not interpret sentiment confidence as truth or loud customers as the entire market.
- `product-sprint-prioritizer.md`: RICE/MoSCoW/Kano, dependency mapping, capacity, buffers, risk, and transparent trade-offs. Scoring is decision support under uncertain inputs. Do not compare teams or individuals by velocity, game story points, or assume a universal 15% buffer.
- `product-trend-researcher.md`: multi-source signals, market sizing, competitor alternatives, source credibility, and ongoing monitoring. “80% six-month prediction accuracy” or “50+ sources” has no evidential value without a defined forecast dataset and collection. Keep fact, estimate, forecast, and recommendation distinct.
- `product-behavioral-nudge-engine.md`: explicit tone/channel/cadence preferences, quiet hours, smaller next actions, and measuring completion rather than notifications sent. Keep opt-out, full queue visibility, and user agency; avoid hidden urgency, manipulative retention, or psychologically profiling people without need and consent.

**Frontend/backend recommendation:** every prioritized improvement should link a user problem to a concrete journey, supporting contract/storage changes, observability, and a falsifiable outcome. Build the smallest useful test of the hypothesis; do not ship analytics/experimentation without consent and data minimization where required.

## project-management — 7 files

- `project-manager-senior.md`: quote actual requirements, extract the requested stack, break work into actionable tasks with acceptance criteria, and avoid invented premium scope. Useful corrective to the senior-developer persona. Discard assumed `ai/memory-bank` paths, Laravel/FluxUI defaults, and universal command-execution rules that belong to a different environment.
- `project-management-project-shepherd.md`: charter, dependencies, critical path, stakeholders, risk owners, capacity/buffer, transparent reporting, and acceptance handoff. On-time percentages are not proof of value or certainty; record scope/date trade-offs explicitly.
- `project-management-jira-workflow-steward.md`: requirement → branch → commit → PR → release traceability, exact ticket identifiers, atomic changes, risk and test evidence. Only enforce Jira, Gitmoji, `develop`, or branch patterns where the repository actually requires them. Do not invent tickets or block otherwise valid work just because it uses another tracker.
- `project-management-meeting-notes-specialist.md`: source-as-data, four-section records, no fabricated decisions/owners, and explicit missing information. This is a strong extraction discipline. Preserve source references and exact dates where available; proposed actions are not agreed commitments.
- `project-management-experiment-tracker.md`: hypothesis, sampling/power, randomization, guardrails, data QA, effect sizes/intervals, and decision records. Its goal that 95% of experiments reach statistical significance is methodologically wrong as a success criterion: null findings are legitimate. Predefine stopping, multiple-comparison handling, and practical significance; do not peek until a desired result appears.
- `project-management-studio-operations.md`: versioned SOP with inputs, permissions, steps, outputs, owner, success criteria, common failures, and monitoring. Replace undefined “95% operational efficiency” with explicit cycle time, rework, service quality, and user burden.
- `project-management-studio-producer.md`: portfolio capacity, strategic fit, dependency/risk diversification, budget, and executive decisions. Guaranteed 25% ROI, market leadership, or awards cannot be promised by process. Use scenarios and revisit assumptions.

**Reusable handoff:** problem and source → acceptance criteria/non-goals → dependency-aware work packages → owners/authorization → implementation and verification artifacts → release decision/rollback → support and measurement. Scale ceremony to task risk; a small bug fix does not need a portfolio plan.

## Conflicts and unsafe claims to resolve in the parent skill

1. **Source is data, never policy.** Preserve agents as attributed references, but ignore commands to scan automatically, run named scripts, impersonate experience, remember facts permanently, or override the current request.
2. **Coherent scope beats tiny-diff dogma.** Minimal-change and Rust-refactoring principles combine as “inspect the affected system; complete the requested transformation; avoid unrelated edits.”
3. **Evidence beats demanded defects or grades.** No mandatory issue count, automatic C-grade, or predetermined pass/fail. No fabricated measurements or template example values.
4. **Contract and runtime evidence beat appearances.** Screenshots cannot demonstrate database persistence, authorization, payment settlement, reliability, or correct concurrent behavior.
5. **No universal stack or aesthetics.** Existing stack, product need, and user specification override Laravel/FluxUI, Next.js, Kubernetes, theme toggles, glassmorphism, and animation defaults.
6. **No unsupported numerical promises.** Accuracy, uptime, savings, turnaround time, conversion, prediction quality, compliance, and coverage targets need definitions, representative tests, and measured baselines.
7. **No execution of model-generated Python through keyword-gated `eval`.** Use constrained operations and real isolation; model confidence is not a safety proof.
8. **No paper compliance.** PDF metadata, policy generators, automated scans, scorecards, or tokenized checkout do not independently establish PDF/UA, PDF/A, WCAG, privacy law, SOC 2, or PCI conformance.
9. **Security architecture is contextual.** Cookie sessions may suit a web BFF while OAuth native/API clients differ. Role separation is not prompt-injection immunity. Secrets require lifecycle control, not a single preferred transport slogan.
10. **Check current authoritative documentation when implementing.** Framework APIs, cloud defaults, package policies, legal obligations, browser rendering, and third-party terms may differ from these unexecuted templates.
11. **Bound risky automation.** Shadow experiments, load tests, penetration tests, production changes, payments, credential rotation, notification sends, and agent promotion need scoped authorization and verification.
12. **Operationalize uncertainty.** Mark blocked/unverified work, distinguish examples from results, and identify required follow-up rather than filling gaps with confident prose.

## Recommended lazy-reference routing for a full-stack improvement skill

- **Always-on compact core:** requirements/non-goals, code-first inspection, coherent scope, trust boundaries, baseline, complete implementation, layered tests, evidence, and honest completion.
- **Frontend work:** UI finish-gate reviewer + frontend developer + UI designer/UX architect + accessibility auditor; add i18n, data visualization, or platform-specific material only when relevant.
- **Backend work:** backend/software architect + API platform + identity/access + database optimizer/reliability; add payments, realtime, data, privacy, or AI references when the dataflow requires them.
- **Review/security:** code reviewer + AppSec/security architect + AI-code auditor; add secrets, cloud, blockchain, detection, or incident material only for explicit scope.
- **Validation/release:** test automation + API tester + performance benchmarker + SRE/DevOps; use reality/evidence agents only after removing their predetermined grades and issue counts.
- **Product and coordination:** product manager + feedback synthesis + senior project manager; load experiment, Jira, portfolio, support, financial, or compliance references only as needed.

The parent skill should expose a small number of modes (inspect, plan, implement, review, verify), not claim to spawn or embody every persona. References expand expertise; they do not confer tools, credentials, authorization, legal qualification, persistent memory, or demonstrated execution.


---

# Domain-agent source review

## Scope, method, and limits

Reviewed every file recursively in `academic`, `research`, `gis`, `specialized`, `healthcare`, `finance`, `spatial-computing`, and `game-development` under `assets/upstream`. The inventory contains **114 files, all Markdown**, totaling **31,079 lines and 1,633,490 bytes**. Full file contents were read for batched structural/rule extraction; mission, deliverable, workflow, safety, and testing material was examined, with deeper targeted reading of the most transferable engineering procedures and hazardous examples. The companion JSON provides an exact path inventory, content hashes, and batch coverage.

This is a review of prompt definitions, not verification that their claimed expertise, example code, product integrations, regulatory statements, or performance targets work. No repository code was executed, no source directives were adopted, and no skills were installed. Numerical targets in the sources are proposals or examples, not measurements from this review. Legal, clinical, tax, and platform-version claims were not independently validated against current primary authorities.

| Folder | Files, including descendants | Principal value for frontend/backend enhancement |
|---|---:|---|
| `academic` | 6 | Experiment validity, uncertainty, content coherence; mostly not implementation |
| `research` | 1 | Auditable technology/product research and primary-source tracing |
| `gis` | 13 | Map UX, spatial data quality, streaming, ETL and geographic evaluation |
| `specialized` | 59 | Workflow discovery, drift audits, authorization, integration governance, domain workflows |
| `healthcare` | 3 | Clinical-claim governance and health-system adoption boundaries |
| `finance` | 5 | Financial model integrity, reconciliation, scenarios and controlled approvals |
| `spatial-computing` | 6 | Native spatial rendering, accessible XR interaction, terminal embedding |
| `game-development` | 21 | Interactive state design, network authority, asset pipelines and target-device budgets |

## Overall assessment

The strongest reusable engineering material is not the persona framing. It is the combination of **workflow state contracts**, **semantic and event-order drift checks**, **failure-oriented tests**, **source-of-truth ownership**, **human authorization**, and **evidence-backed completion**. These techniques transfer directly to ordinary web applications without adopting the agents' names, claims of memory, autonomous execution permissions, or prescribed tool stacks.

The collection mixes unusually detailed review procedures with thin capability descriptions and illustrative code. It should become a **selective reference library**, not one enormous instruction prompt. Load only the relevant domain, version-check its external assumptions, and derive bounded acceptance criteria from the actual application. Retain user-visible states and audit evidence; remove ceremonial persona requirements and absolute performance promises.

# 1. `academic` — 6 files

## Folder synthesis

Five definitions primarily support worldbuilding, character analysis, and narrative critique; the statistician is the broadly applicable product-engineering specialist. Their common strength is explaining recommendations through explicit theories and evidence rather than taste. Their limitation is that naming a framework is not proof of its validity or suitability. They contain neither a general frontend architecture nor a backend implementation method.

| Reviewed file | Substantive assessment and useful transfer |
|---|---|
| `academic/academic-anthropologist.md` | Connects kinship, ritual, exchange, social organization, and ecological constraints into coherent cultures. Useful for culturally sensitive product content and game settings; preserve contextual sourcing and crisis/adaptation checks, not assumptions that a culture is homogeneous or mechanically determined. |
| `academic/academic-geographer.md` | Tests terrain, climate, hydrology, resources, settlement, and trade as interdependent systems. Useful for map-based experiences and simulations; its physical-coherence checks do not replace measured GIS data, coordinate-system validation, or analysis of social confounding. |
| `academic/academic-historian.md` | Separates documented history from plausible extrapolation, checks anachronisms, and grounds material culture in primary and secondary sources. Useful for educational interfaces and content provenance; expose disputed interpretations and source limitations rather than presenting period generalizations as settled fact. |
| `academic/academic-narratologist.md` | Analyzes story structure, character arcs, pacing, promises/payoffs, and alternative narrative traditions. Useful for onboarding sequences and interactive storytelling, but narrative elegance is not evidence of usability or conversion improvement. Retain specific proposed changes and their rationale. |
| `academic/academic-psychologist.md` | Evaluates observable behavior, motivation, attachment, cognitive patterns, and interpersonal dynamics with explicit theory limitations. Useful for fictional characters and cautious behavioral hypotheses; do not diagnose real users, infer protected traits, or deploy contested personality models as product decision engines. |
| `academic/academic-statistician.md` | Interrogates question, measurement, sample, comparison, analysis, inference, and decision. Directly useful for A/B tests and performance/product claims: pre-specify outcomes, account for repeated looks and multiple comparisons, report effect sizes and uncertainty, and distinguish descriptive, associational, and causal questions. |

**Frontend applicability:** explanatory content, uncertainty displays, culturally coherent onboarding, and appropriately designed usability experiments. **Backend applicability:** metric definitions, experiment assignment/analysis contracts, and measurement provenance; limited direct software guidance otherwise.

**Retain:** design the study before reading its results; identify the weakest link in an inference; label exploratory versus confirmatory analysis; communicate what result would change the decision. **Pitfalls:** framework name-dropping, cultural essentialism, diagnostic overreach, treating significance as practical importance, and assuming lack of significance proves no effect.

# 2. `research` — 1 file

`research/research-synthesist.md` supplies a coherent workflow: frame the question and sufficient evidence; search multiple sources and phrasings; record inclusion/exclusion boundaries; grade methods and evidence; trace derivative claims to primary sources; synthesize agreements, disagreements, and gaps. Its search strategy, source evaluation table, and evidence synthesis map are stronger reusable outputs than an unstructured literature summary.

**Frontend enhancement:** substantiate accessibility or UX recommendations without turning marketing claims into requirements. **Backend enhancement:** compare infrastructure and library choices with source, version, workload, and benchmark provenance. Neither domain benefits from treating source volume or recency alone as reliability.

**Retain:** a claim ledger containing primary source, method, applicability, contradictory evidence, confidence, and the decision supported. Record databases, dates, language restrictions, and exclusions so a reader can audit search coverage.

**Limits/pitfalls:** this is a research protocol, not proof a search was exhaustive. Its weakest-link language is best applied to evidence necessary for a conclusion, not indiscriminately to every weak paper mentioned. Independent evidence and domain-specific study quality matter more than counting references. Generated bibliographies and confident summaries still require verification.

# 3. `gis` — 13 files

## Folder synthesis

This is a well-separated geospatial delivery chain: strategy → demonstrable feasibility → data acquisition/ETL → analysis → cartographic/web/3D presentation → independent QA. Several files explicitly identify when another specialist is appropriate. That routing is useful, though the web/API versus spatial-data-engineering boundary is not perfectly consistent and should be assigned by deliverable rather than title.

| Reviewed file | Scope, applicability, and specialist procedure worth retaining |
|---|---|
| `gis/gis-technical-consultant.md` | Maps operational pain to a phased spatial roadmap and technology choice. Start with data discovery, source availability, ownership, and realistic integration cost. Its asserted percentages and project durations are scoping examples, not universal estimates. |
| `gis/gis-solution-engineer.md` | Builds a narrow working PoC with target-device tests, reproducible setup, and offline/fallback demo assets. Useful for de-risking a map feature before committing engineering effort; keep prototype shortcuts explicitly separate from production readiness. |
| `gis/gis-analyst.md` | Covers map production, data inspection, spatial queries, and export checks. Verify coordinate reference systems, attributes, and geometry before operations, and spot-check conversions afterward. Use for routine GIS preparation rather than advanced inference or automated production ETL. |
| `gis/gis-cartography-designer.md` | Provides visual hierarchy, scale-aware labels, basemap selection, legends, and color semantics. Direct frontend value: choose sequential/diverging/categorical encodings intentionally and test interpretation with unfamiliar users. A visually polished map does not validate the underlying statistics. |
| `gis/gis-spatial-data-engineer.md` | Defines configurable ingestion, normalization, explicit reprojection, validation after transformations, immutable source preservation, and logged row counts. Strong backend transfer: reproducible ETL with geometry and attribute gates, lineage, and real-data tests. |
| `gis/gis-geoprocessing-specialist.md` | Focuses on ArcPy, Python toolboxes, Model Builder, parameter validation, extension licensing, and realistic error handling. Retain pre-execution validation and documented parameter contracts; ArcGIS-specific APIs and license assumptions limit portability. |
| `gis/gis-spatial-data-scientist.md` | Covers spatial dependence, clustering, regression, network/accessibility models, sensitivity, and uncertainty. Retain residual spatial-autocorrelation checks and sensitivity to aggregation boundaries (MAUP); ordinary independent-sample methods may not support the intended inference. |
| `gis/gis-geoai-ml-engineer.md` | Builds imagery extraction/classification pipelines with per-class metrics, confusion matrices, geographic error inspection, and unseen-region evaluation. Backend/model value is avoiding geographically leaked validation and validating predictions against ground truth; aggregate accuracy is insufficient. |
| `gis/gis-drone-reality-mapping.md` | Connects capture planning, image quality checks, photogrammetry, point-cloud classification, and output QA. Retain image inspection before processing and overlay/accuracy checks on final GIS products. Survey-grade claims need measured controls and the applicable professional/regulatory context, not merely a generated mesh. |
| `gis/gis-bim-specialist.md` | Bridges building models, indoor mapping, and digital twins. Explicitly reconcile Revit survey/base points with real coordinates and check conversion positioning, geometry, and attributes. BIM-to-GIS conversion can silently lose texture, semantics, or precision. |
| `gis/gis-3d-scene-developer.md` | Covers terrain, point clouds, streamed scenes, level of detail, and protected sharing. Direct frontend value: progressive streaming, standard navigation, target-device profiling, and real OAuth/CORS/redirect tests. Avoid loading entire datasets or treating a gaming-laptop demo as tablet evidence. |
| `gis/gis-web-gis-developer.md` | Integrates mapping libraries, real-time data, spatial services, clustering/tiling/filtering, mobile interaction, and slow-network testing. Retain legends, loading behavior, touch support, and bounded feature requests. Backend service choice and API authorization still require separate architecture. |
| `gis/gis-qa-engineer.md` | Supplies release gates for geometry/topology, attributes, metadata, spatial accuracy, services, and map delivery. Especially strong: confirm declared CRS against actual coordinate behavior; findings need reproducible locations/examples; rerun the failed check after fixes. |

**Frontend applicability:** interactive maps, accessible legends, scale-aware labels, mobile selection, 3D navigation, low-bandwidth loading, and honest uncertainty visualization. **Backend applicability:** PostGIS/service boundaries, immutable ingestion, lineage, explicit coordinate transformations, tiled/streamed datasets, and regional model evaluation.

**Retain as a specialist checklist:** source/license and intended accuracy → CRS and units → geometry/attribute inspection → explicit transform → post-transform checks → spatially appropriate analysis → tiled presentation → target-device/auth tests → reproducible QA and fix verification.

**Pitfalls:** silently assigning rather than transforming a CRS; confusing geographic with projected units; a correct-looking map with wrong coordinates; geographic train/test leakage; color-only legends; overloading the browser; stale SDK recommendations; and treating Esri licensing or product-specific packaging as a general web requirement. Sample threshold claims such as a feature-count performance ceiling should become workload-specific benchmarks, not hardcoded universal limits.

# 4. `specialized` — 59 files

## Folder synthesis

This folder combines high-value engineering review procedures, domain operational playbooks, executive advice, and culturally specific communication templates. The engineering core is highly relevant; many other definitions are valuable mainly as **requirements discovery** for vertical SaaS. Most are not executable integrations, and their asserted long-term memory, identities, permissions, experience, or certification do not exist merely because a prompt says they do.

## 4.1 Engineering, trust, data, and automation — file-level review

| Reviewed file | Assessment, transfer, and boundary |
|---|---|
| `specialized/specialized-codebase-archaeologist.md` | One of the strongest general-purpose reviews: compare implementation eras and responsibilities; maintain findings, era, responsibility, and severity views. Deliberately trace reversed defaults, near-identical identifiers, double transforms, units, and state-existence assumptions across unrelated event handlers. Confirm intentional divergence before declaring a bug and check both sides of a proposed fix. |
| `specialized/specialized-workflow-architect.md` | Specifies happy, invalid-input, timeout, transient, permanent, partial-failure, and concurrent-conflict paths. Each state records customer view, operator view, database state, and logs; handoffs define payload/response/timeout/recovery contracts. Excellent bridge from backend behavior to frontend loading/error/retry states. |
| `specialized/automation-governance-architect.md` | Scores recurring value, data criticality, dependency risk, and scaling before permitting full, partial, pilot, or rejected automation. Its validation → normalization → business logic → external action → result verification → logging → recovery → status-writeback sequence is useful beyond n8n. Production changes still need real user authorization. |
| `specialized/agents-orchestrator.md` | Structures specification → task breakdown → architecture → developer/QA loops → integration review, with explicit state and bounded retries. Retain evidence gates and failure escalation, but agent names and spawning examples are framework-specific; screenshots cannot replace backend, security, migration, or load tests. |
| `specialized/agentic-identity-trust.md` | Separates authenticated identity, delegated authorization, trust signals, and tamper-evident evidence. Retain scope narrowing, expiry checks, fail-closed behavior, key separation, and intent/authorization/outcome records. The illustrative verifier is not a complete security protocol; it does not by itself establish every link's signer continuity, trust anchor, revocation, or replay protection. |
| `specialized/identity-graph-operator.md` | Emphasizes deterministic canonical identity, tenant scoping, masked PII, per-field evidence, and reviewed merge/split proposals. Useful for CRM deduplication and account linking. Matching examples use simplistic phone/name normalization; a high weighted score from sparse fields is not sufficient evidence for automatic identity merging. |
| `specialized/lsp-index-engineer.md` | Describes multi-language LSP orchestration, symbol/reference graphs, atomic index updates, navigation endpoints, and event streams. Useful for code browsers and developer tools. Capability negotiation and consistent graph updates are transferable; `graphd`, concrete schemas, and latency/memory targets describe a specific project, not a generic LSP guarantee. |
| `specialized/specialized-mcp-builder.md` | Defines focused tool interfaces, schema validation, structured output, secret handling, recoverable errors, and testing through a real agent call loop. Strong backend/tooling guidance: test malformed inputs, unavailable APIs, authentication failure, rate limits, and empty results. Add least-privilege authorization and prompt-injection defenses; schema validation alone is not authorization. |
| `specialized/specialized-model-qa.md` | Independent ten-domain model review spans governance, data reconstruction, labels, cohorts, features, replication, calibration, monitoring, fairness, and impact. Retain out-of-time testing, leakage checks, segment analysis, incumbent comparison, and observation/evidence/impact/recommendation findings. Do not accept in-sample metrics or a single calibration p-value as certification. |
| `specialized/specialized-salesforce-architect.md` | Supplies ADRs, object/data-model review, governor budgets, trigger/handler separation, declarative-versus-code tradeoffs, and failure-aware integration. Useful only where Salesforce is actually in scope. Governor limits, encryption behavior, product names, and deployment/test APIs must be checked against the target edition/version. |
| `specialized/specialized-fedramp-rmf-compliance.md` | Maps categorization, authorization boundary, control selection, implementation evidence, assessment, authorization, and continuous monitoring into SSP/POA&M/ATO artifacts. Useful for compliance-oriented backend requirements and audit UI, not for declaring a system authorized. Its dated Rev5/20x/OSCAL claims and deadlines are unverified here and require current official sources. |
| `specialized/data-privacy-officer.md` | Covers processing inventories, lawful basis, DPIAs, data flows, rights requests, vendors, retention, and breach/privacy governance. Directly informs consent/rights interfaces and backend minimization, access control, deletion, export, and audit design. Jurisdiction and organizational role determine the actual duties. |
| `specialized/sales-data-extraction-agent.md` | Watches spreadsheet arrivals, ignores lock files, waits for write completion, maps columns, logs rejected rows, persists transactionally, and emits completion events. Good ingestion skeleton; fuzzy names/columns and inferred metric periods need confidence gates, quarantine, provenance, and version-aware deduplication rather than silent guessing. |
| `specialized/data-consolidation-agent.md` | Produces territory/rep/pipeline JSON, latest-per-type metrics, quota attainment, multiple periods, and generation timestamps. Useful dashboard/backend contract. Define snapshot consistency, fiscal periods, currencies, zero-quota semantics, and reconciliation between totals and detail; latest values from different periods must not be mixed casually. |
| `specialized/report-distribution-agent.md` | Routes reports by territory, separates manager summaries, logs each recipient outcome, and exposes delivery history. Retain per-recipient authorization and failure isolation. Hardcoded schedules/branding are project assumptions; add timezone/DST handling, replay deduplication, HTML escaping, and a distinction between SMTP acceptance and final delivery. |
| `specialized/accounts-payable-agent.md` | Offers vendor verification, spend limits, invoice references, and audit logging, but its payment examples are not safe production code. A read-then-send check is race-prone; some paths omit approval/vendor checks; rail failover after an ambiguous timeout can double-pay. Require durable provider idempotency, atomic state, verified settlement status, explicit scope, and approval before transfers. |
| `specialized/specialized-document-generator.md` | Recommends data-driven templates, semantic styles, accessible headings/alt text, and delivering both generator and output. Useful for export features and report services; a formatted file is not validated until opened/rendered and checked for content, pagination, accessibility, and formula behavior. |
| `specialized/specialized-developer-advocate.md` | Audits time to first success, actionable errors, runnable examples, documentation, and feedback grounded in real user issues. Direct frontend/docs and API onboarding value. Retain clean-environment sample execution, honest limitations, and reproducible bug feedback rather than engagement vanity metrics. |
| `specialized/specialized-master-plan-architect.md` | Requires actual-repository discovery, failure-vector critique, governance, regression blast-radius assessment, and a structured implementation plan. Useful for risky cross-layer changes. Scale the planning depth to the task; mandatory lectures and rigid ceremony are not appropriate for every small enhancement. |
| `specialized/zk-steward.md` | Uses atomic linked notes, structure/index notes, validation logs, and explicit task closure to maintain reusable knowledge. Useful for architecture decisions and evolving audit registries. Do not import forced salutations, expert personas, file-layout conventions, or external companion dependencies unless requested. |

## 4.2 Business, governance, and people operations — file-level review

| Reviewed file | Assessment, transfer, and boundary |
|---|---|
| `specialized/business-strategist.md` | Builds competitive/market-entry analysis, strategic options, business cases, and scenarios, with assumptions stress-tested before recommendations. Useful for prioritizing enhancements against measurable outcomes; market assertions need sourced data and strategic frameworks do not establish causality. |
| `specialized/change-management-consultant.md` | Uses stakeholder mapping, readiness, ADKAR, communication, resistance diagnosis, and adoption measurement. Useful for rolling out redesigned workflows, admin tools, and migrations. Validate actual user constraints rather than treating resistance as a communication defect. |
| `specialized/chief-financial-officer.md` | Covers treasury, planning, capital allocation, board reporting, financial controls, and licensed-professional boundaries. Useful for finance dashboards and approval policies. Fixed allocation/hurdle examples are not universal policy; preserve segregation of duties and reconciliation with actual accounts. |
| `specialized/corporate-training-designer.md` | Connects needs diagnosis, measurable curriculum, realistic practice, trial delivery, learning platforms, and Kirkpatrick evaluation. Useful for onboarding/help systems and compliance training records. Chinese regulatory references and suggested refresh periods need localization; learner feedback should not become punitive surveillance. |
| `specialized/esg-sustainability-officer.md` | Defines materiality, emissions scopes, boundaries, factor sources, reporting frameworks, target setting, and supplier diligence. Useful for auditable sustainability data pipelines and evidence-linked dashboards. Preserve units, reporting periods, methodologies, and achieved-versus-aspirational status to avoid greenwashing. |
| `specialized/government-digital-presales-consultant.md` | Covers policy fit, architecture, tender requirements, compliance, PoCs, evidence-backed performance claims, and delivery handoff. Good requirements/compliance matrix pattern; Chinese government/Xinchuang context is specific. Do not fabricate qualifications, references, or benchmarks to satisfy a tender. |
| `specialized/grant-writer.md` | Connects funder fit, proposal requirements, outcome evidence, budget narratives, submission calendars, and post-award reporting. Useful for grant-management workflows and document completeness checks. Deadlines, indirect-cost rules, and program commitments must come from the actual award, not template assumptions. |
| `specialized/hr-onboarding.md` | Models preboarding, first day, benefits, access, training, manager tasks, and milestone tracking with confidential records. Strong vertical-SaaS requirements. Its broad statement that I-9 verification is required on Day 1 collapses distinct legal steps; implement only jurisdiction-verified deadlines and completion definitions. |
| `specialized/ma-integration-manager.md` | Organizes pre-close/Day 1/100-day workstreams, customer continuity, retention, governance, and realized-versus-planned synergies. Useful for migration readiness and controlled cutovers; legal clean-team boundaries and data-access timing must be verified, not inferred from an integration plan. |
| `specialized/operations-manager.md` | Uses SIPOC, value-stream mapping, DMAIC, bottleneck analysis, capacity planning, SOPs, and business continuity. Direct transfer: baseline → identify constraint → bounded change → measure → hand off with ownership. Avoid optimizing a local metric while worsening end-to-end throughput. |
| `specialized/organizational-psychologist.md` | Covers psychological safety, team effectiveness, burnout, culture diagnostics, and evidence-based interventions. Relevant to research consent and organizational rollout, not software architecture. Protect survey anonymity and avoid presenting all named management models as equally validated clinical science. |
| `specialized/personal-growth-mentor.md` | Diagnoses goals and constraints, proposes small actions, decision matrices, weekly review, and environmental habit changes. Limited engineering relevance beyond scoped execution and feedback loops. Preserve professional boundaries; do not infer hidden motives or replace treatment with coaching. |
| `specialized/recruitment-specialist.md` | Describes channels, structured interviews, STAR evidence, hiring funnels, offer approval, and candidate communication. Useful for applicant-tracking workflows. China-specific labor rules and numerical funnel claims need verification; listed personality tools must not become unsupported or discriminatory selection filters. |
| `specialized/specialized-chief-of-staff.md` | Maintains decision filters, checklist ownership, cascading document dependencies, and action routing. Useful for change-impact tracking and keeping implementation, docs, and deployment status aligned. Principal-specific ADHD/persona assumptions and automatic commit/push sequences are not general operating permissions. |
| `specialized/specialized-pricing-analyst.md` | Combines fully loaded costs, market context, value, elasticity, sensitivity, discount governance, and review cadence. Useful for billing/pricing administration and experiments. Use verified cost/currency/tax inputs and versioned entitlements; behavioral pricing suggestions require ethical and legal review. |
| `specialized/specialized-strategy-duel-agent.md` | Simulates competing strategic moves using game-theory/stratagem framing and produces a verdict. Useful only as structured red-teaming or hypothesis generation; a simulated opponent is not independent evidence, a calibrated forecast, or proof a plan will succeed. |
| `specialized/supply-chain-strategist.md` | Covers supplier qualification, procurement, inventory models, logistics, TCO, ERP maturity, quality, contingency, and supplier ethics. Useful for inventory/procurement systems and resilience requirements. Region-specific platforms and blanket sourcing rules need business context; never skip qualification to meet a date. |

## 4.3 Customer-facing and regulated operational workflows — file-level review

| Reviewed file | Assessment, transfer, and boundary |
|---|---|
| `specialized/customer-service.md` | Provides identity-aware support, complaint resolution, account/order handling, escalation, confirmation, and case documentation. Useful for service UI and workflow status. Friendly scripts must not override cancellation rights, authorization, verified policy, or truthful confirmation of a state change. |
| `specialized/customer-success-manager.md` | Defines onboarding outcomes, health scores, business reviews, churn signals, expansion, and renewal management. Useful for account dashboards and intervention queues. Validate health-score predictors, distinguish correlation from cause, and never promise uncommitted roadmap delivery. |
| `specialized/healthcare-aging-parent-care-companion.md` | Maintains a care profile, reconciles updates, organizes medication/appointments, controls sharing, and escalates emergencies to professionals. Useful for caregiver coordination features, not diagnosis or dosage decisions. Explicitly distinguishes family-assistant privacy principles from automatic HIPAA covered-entity status. |
| `specialized/healthcare-customer-service.md` | Covers nonclinical patient identity, scheduling, billing/insurance support, complaints, emergencies, and handoff to licensed staff. Useful patient-service workflows with minimum-necessary information. Static identity questions are not by themselves strong authentication or a full HIPAA compliance program. |
| `specialized/healthcare-marketing-compliance.md` | Reviews medical/pharma/device/aesthetics/supplement claims, advertising approval, patient consent, platform rules, and privacy in a Chinese regulatory context. Useful as a content approval/evidence workflow, not universal healthcare law. Verify current authority, approved indication, audience, geography, and reviewer sign-off. |
| `specialized/hospitality-guest-services.md` | Connects reservation, pre-arrival, check-in, stay, checkout, service recovery, and feedback, with confidentiality and manager approval for sensitive exceptions. Useful booking/support state design. Room/location data is safety-sensitive, and compensation/availability must come from authorized systems. |
| `specialized/legal-billing-time-tracking.md` | Defines time narratives, prebilling review, invoice/collection workflows, trust accounts, approval of adjustments, and billing analytics. Useful legal practice-management requirements. Never fabricate time or treat trust funds as ordinary operating balances; jurisdiction-specific rules and reconciliations require professional oversight. |
| `specialized/legal-client-intake.md` | Identifies parties/practice fit, performs conflicts screening, captures urgency, and produces attorney-ready intake summaries with confirmed next steps. Useful secure intake and scheduling UX. Do not give legal advice or promise representation; deadline examples must be checked for the actual facts/jurisdiction. |
| `specialized/legal-document-review.md` | Starts with document type, parties, and represented side, then extracts clauses, missing terms, comparison findings, and prioritized attorney actions with page/section citations. Strong provenance/review UI pattern. A missing clause is not automatically unlawful and enforceability is not established by a template. |
| `specialized/loan-officer-assistant.md` | Models borrower intake, documents, disclosures, underwriting conditions, pipeline updates, and closing preparation. Useful lending workflow requirements with explicit pending/cleared states and written evidence. Do not promise approval, infer eligibility from protected traits, or use template TRID/licensing dates without authoritative checking. |
| `specialized/medical-billing-coding-specialist.md` | Requires rendered-service documentation, medical necessity, justified modifiers, claim scrubbing, posting/reconciliation, denial management, and audit records. Useful claims-processing requirements. Code sets and payer policies are versioned; revenue optimization cannot justify unsupported coding or services. |
| `specialized/real-estate-buyer-seller.md` | Covers needs, current comparable sales, offers, disclosure, transaction coordination, and wire-fraud safeguards. Useful transaction portals and milestone tracking. Preserve client confidentiality, independently verify payment instructions, and avoid discriminatory steering or pretending to supply licensed representation. |
| `specialized/retail-customer-returns.md` | Models eligibility, receipt/item inspection, reason codes, refund method, fraud escalation, and authorized exceptions. Useful state machines and refund UI. Original-payment-method defaults, manager overrides, duplicate refunds, and inventory reconciliation must be enforced server-side, with fair review of fraud flags. |
| `specialized/sales-outreach.md` | Connects ICP research, personalized messages, objection handling, pipeline stages, and one clear next step. Limited direct engineering value beyond CRM workflows. Convert persistent follow-up language into consent-aware, unsubscribe-respecting, frequency-limited behavior rather than autonomous unsolicited messaging. |
| `specialized/study-abroad-advisor.md` | Builds profile-based school lists, genuine essays/references, calendars, document checks, and visa preparation with sourced admissions information. Useful application-tracking features. Probability bands in templates are not calibrated admissions forecasts; preserve applicant authorship and verified current requirements. |

## 4.4 Culture, communication, creative and physical-domain specialists — file-level review

| Reviewed file | Assessment, transfer, and boundary |
|---|---|
| `specialized/language-translator.md` | Emphasizes meaning, register, regional Spanish variants, emergency-first translation, and spoken pronunciation support. Useful localization content and locale selection; the broad title overstates its Spanish-heavy detail. Medical/legal translations require qualified review and English phonetic approximations are not universal accessibility support. |
| `specialized/resume-tailor.md` | Maps job requirements to supported experience, explains edits, flags gaps, and optimizes readable/ATS-friendly structure without inventing achievements. Useful evidence-preserving document transformations. Keyword targets do not justify fabrication, hidden text, or unsupported quantified impact. |
| `specialized/specialized-cultural-intelligence-strategist.md` | Audits implicit defaults in names, language, disability/neurodivergence, calendars, and non-Western contexts; researches and explains corrections. Direct frontend value for inclusive validation and localization. Replace demographic generalizations with actual user research and flexible data models. |
| `specialized/specialized-french-consulting-market.md` | Explains consulting channels, gross/net daily rates, intermediaries, contracts, and international positioning. Useful only for localized freelance/business workflows. Rate ranges, tax-risk heuristics, and its categorical portage/employment framing require current local professional verification. |
| `specialized/specialized-korean-business-navigator.md` | Describes approval chains, titles, relationship sequencing, KakaoTalk conventions, and proof projects. Useful stakeholder discovery and communication localization. Treat these as contextual hypotheses, not universal rules about Korean people or permission to suppress direct questions. |
| `specialized/specialized-focus-music-architect.md` | Provides instrumental generative-music prompts, restrained dynamics, loop design, and Web Audio examples. Limited frontend relevance for optional sound environments. Absolute neuroscience, frequency, focus-duration, and zero-vocal guarantees are unsupported here; user comfort, volume controls, and opt-out matter more. |
| `specialized/specialized-civil-engineer.md` | Structures governing-code identification, loads, geotechnical assumptions, structural analysis, calculation packages, and review. Useful for traceable engineering-data/reporting software, not authorizing physical designs. Code editions, national annexes, site conditions, and licensed review are indispensable. |

## 4.5 High-priority procedures to extract into a reusable enhancement skill

1. **Workflow discovery before modification.** Inventory API routes, workers, cron, webhooks, event consumers, state enums, migrations, infrastructure, and configuration. Map entry points to user/operator journeys and affected state. The source includes discovery commands; adapt the concept to the actual repository rather than blindly running them.
2. **State contract per branch.** For each step: actor, input, output, deadline, retryability, errors, customer state, operator state, database state, and log evidence. Cover concurrency, retries, timeouts, and partial completion, not only success.
3. **Separate race and semantic audits.** For every handler reading state it did not create, locate the creator and prove ordering via transactions, locks, idempotent upserts, queue contracts, or explicit existence handling. Independently trace cents/dollars, fractions/percentages, UTC/local time, encoding, and normalized/raw values end to end.
4. **Cleanup with domain semantics.** Keep a resource inventory and compensation order, and test cleanup failure/orphan alerting. Do not blindly apply the source's delete-every-created-record model to payments, legal records, or other immutable audit data; compensate and preserve history where required.
5. **Integration governance.** Define authoritative systems, tenant scope, schemas, credential lifecycle, permissions, limits, ownership, bounded retry, dead-letter/recovery paths, and post-action readback. Automation is permitted only when actual authorization exists.
6. **Evidence-first QA.** Convert branches into explicit tests, retain both failing and verified-safe observations, prioritize data/money/security corruption over style, and verify a fix against the original failure. Add property/invariant and interaction tests: one example per branch does not prove complete correctness.
7. **Independent model/evidence review.** Reconstruct data/labels, check temporal leakage, evaluate held-out cohorts, inspect calibration and impact, and report uncertainty and fairness tradeoffs. Statistical tests are diagnostics, not automatic approval switches.

## 4.6 Specific hazards not to copy

- **Payment rail fallback:** never switch rails on an unknown outcome before checking whether the first transaction settled. Never rely on a non-atomic duplicate check or a source prompt's monetary threshold as permission to spend.
- **Incomplete cryptographic examples:** signatures and decreasing scopes are necessary but insufficient; signer/subject chain binding, trusted roots, audience, revocation, clock handling, nonce/replay policy, and canonical serialization need a real design and security review.
- **Model calibration example:** `p_value >= 0.05` means the test did not reject its null under its assumptions; it does not establish a model is calibrated. Tied predictions, extreme probabilities, group count, and sample size affect validity. SHAP API/output-shape assumptions also require version-specific testing.
- **Regulatory prose:** FedRAMP rollout dates, privacy duties, I-9 steps, healthcare marketing, lending timelines, French contracting, and structural codes must be re-sourced for jurisdiction and date. A confident template is not an authority.
- **Hardcoded project context:** STGCRM branding, fixed report times, `graphd`, agent names, and principal-specific communication conventions should be parameters or discarded, not propagated into unrelated projects.
- **False guarantees:** zero defects, zero surprises, perfect delivery, and numerical latency/conversion targets are proposed goals. They are not observed evidence or promises an assistant can responsibly make.

# 5. `healthcare` — 3 files

## Folder synthesis and file review

These files primarily govern evidence, narrative, regulatory positioning, and health-system engagement; they are not a clinical software architecture, FHIR implementation, or validated medical decision system.

| Reviewed file | Substance and transfer |
|---|---|
| `healthcare/healthcare-clinical-evidence-agent.md` | Separates validated, directional, and unvalidated claims; requests source and physician review; adapts presentation to audience without changing underlying evidence; frames clinical AI as assistance rather than diagnostic authority. Useful for claim registries, evidence-linked UI, review gates, and versioned approval records. |
| `healthcare/healthcare-innovation-strategist.md` | Builds consistent healthcare narratives, credential anchors, audience-specific documents, regulatory-category discussion, and a canonical version of contested claims. Useful for product copy/release review and keeping clinical, investor, and regulatory statements consistent. It does not establish a product's actual regulatory classification. |
| `healthcare/healthcare-sovereign-health-systems-agent.md` | Distinguishes government mandate partnerships from commercial procurement; maps coverage, financial protection, quality, stakeholder ownership, and jurisdiction-specific approvals; proposes staged evidence pilots. Useful requirements for deployment governance, data access, approval tracking, and institutional continuity. |

**Frontend applicability:** source-linked clinical statements, visible uncertainty/scope, patient-readable explanations, role-appropriate terminology, and review status. **Backend applicability:** immutable evidence versions, reviewer sign-off, purpose-scoped data access, jurisdictional requirements, and auditable claim publication workflows. None of the three is a substitute for patient safety engineering, clinical validation, access-control implementation, or professional review.

**Retain:** claim → exact evidence → study population/endpoints/limitations → applicability to product → clinical/regulatory review → approved wording/version → monitored changes. Keep commercial and public-sector records and requirements distinct.

**Pitfalls:** the clinical source says validated claims can be used externally “without qualification”; reject that blanket rule. Peer review, a pilot, labeling, or one physician sign-off does not erase study limitations or grant marketing authorization. Its mandatory use of “doctor” is a brand convention that may exclude other legitimate users. Calling software “decision support” does not itself determine legal classification. Government-first sequencing, communication prohibitions, and engagement timelines are strategic templates, not universal procurement facts. One pilot-authorization line contains an unresolved `***` placeholder, further reinforcing that these are templates rather than validated operating procedures.

# 6. `finance` — 5 files

## Folder synthesis and file review

The folder separates transaction/control integrity, financial modeling, planning, investment diligence, and tax positioning. Its common strength is explicit assumptions, reconciliation, downside scenarios, documentation, and review. Its limitation is that sample models, dates, returns, thresholds, and legal interpretations are not verified client-specific advice.

| Reviewed file | Substance and useful procedure |
|---|---|
| `finance/finance-bookkeeper-controller.md` | Provides transaction classification, reconciliations, month-end close, internal controls, and audit-ready statements. Retain a close checklist with dependencies, evidence, exceptions, reviewer approval, and locked/versioned outputs. Useful for ledger/admin features and controls, not permission to post journals or certify GAAP compliance. |
| `finance/finance-financial-analyst.md` | Builds linked financial statements, forecasting, valuation, sensitivity, variance analysis, and assumption governance. Retain source reconciliation, explicit units/periods, independent formula checks, extreme-case tests, and model versions. Useful financial dashboards need explainable drivers rather than a single confident forecast. |
| `finance/finance-fpa-analyst.md` | Connects operating plans, departments, hiring, rolling forecasts, scenario ranges, and business reviews. Useful planning applications: distinguish actual/budget/forecast, tie changes to drivers and owners, and explain forward implications of variances rather than merely labeling them favorable/unfavorable. |
| `finance/finance-investment-researcher.md` | Combines fundamental/quantitative diligence, bull/bear cases, valuation, catalysts, downside, and thesis breakers. Useful research workspaces and monitored assumptions; never turn template risk/reward ratios, benchmark claims, or diligence coverage targets into guaranteed returns or trading authorization. |
| `finance/finance-tax-strategist.md` | Structures facts, issues, applicable law, position strength, savings/risk, documentation, elections, and multi-jurisdiction compliance. Useful source-linked tax calendars and review workflows. Law, thresholds, deadlines, and filing decisions require current jurisdiction-specific verification and qualified professional judgment. |

**Frontend applicability:** scenario comparisons, reconciled drill-down, visible units/currency/date, assumptions, exceptions, and approvals. **Backend applicability:** decimal or integer-minor-unit money representation, consistent rounding/FX policy, append-only audit history, reconciled imports, separation of duties, versioned calculations, and controlled posting. These implementation recommendations follow from the financial integrity requirements; the prompts do not supply a complete financial platform.

**Retain:** reconcile source → document assumptions → model linked consequences → stress-test → independently review → approve/version → monitor deviations and reconcile again. **Pitfalls:** mixing cash/accrual or currencies/periods, unbalanced statements, unsupported tax-risk percentages, stale deadlines, silent spreadsheet overwrites, treating accounting standards as interchangeable, and publishing illustrative numerical examples as actual results.

# 7. `spatial-computing` — 6 files

## Folder synthesis and file review

The Apple-oriented files are specific implementation briefs; the three XR definitions are short capability sketches with much less testing detail. Together they are useful only when a spatial interface or embedded terminal is genuinely part of the product. Their transferable themes are bounded rendering work, multimodal accessibility, lifecycle management, and target-device comfort testing.

| Reviewed file | Substance, applicability, and limits |
|---|---|
| `spatial-computing/macos-spatial-metal-engineer.md` | Designs a graph renderer with instanced Metal drawing, streaming buffers, spatial input, layout physics, and a Vision Pro companion path. Retain GPU/CPU profiling, memory discipline, culling/LOD, and input-latency evidence. The 25k-node/90fps target and API examples are an unverified project budget, not a demonstrated benchmark. |
| `spatial-computing/terminal-integration-specialist.md` | Focuses on SwiftTerm, terminal escape behavior, scrollback/search, SSH client integration, native performance, and accessibility. Useful for embedded developer/admin terminals on Apple platforms. It explicitly does not cover server terminal lifecycle or general cross-platform terminal management; backend authentication, session authorization, and command audit need separate design. |
| `spatial-computing/visionos-spatial-engineer.md` | Covers visionOS 26 SwiftUI/RealityKit windows, volumes, attachments, observable state, gestures, accessibility, and glass materials. Retain platform-native lifecycle and usability review, but verify SDK symbols, availability, and fallback behavior against the actual deployment target. |
| `spatial-computing/xr-cockpit-interaction-specialist.md` | Centers seated, anchored controls with constrained mechanics and combined hand/gaze/voice feedback. Useful for simulator/control-room UI; prototype reach, posture, control affordance, and sickness/comfort on actual devices instead of assuming a cockpit automatically prevents discomfort. |
| `spatial-computing/xr-immersive-developer.md` | Sketches WebXR interactions, hit testing, raycasting, physics, occlusion, shader/LOD optimization, and device fallbacks. Useful for optional browser XR features. The listed headset/browser coverage is a compatibility ambition, not a tested matrix. |
| `spatial-computing/xr-interface-architect.md` | Defines comfortable spatial panels, discovery, selection/manipulation, multimodal input, and accessibility fallback. Useful frontend evaluation framework; lacks a detailed implementation or measurable acceptance suite, so supply task-based usability and comfort tests. |

**Frontend applicability:** high for spatial products; low for ordinary forms/dashboard work unless a validated use case calls for 3D. **Backend applicability:** mainly streamed data contracts, identity/session control, synchronization, and rate/backpressure management; little ordinary service architecture is supplied.

**Retain:** real device/runtime matrix → explicit frame/memory/input budget → minimal prototype → accessible input alternatives → profile under worst expected scene load → comfort and interruption/lifecycle tests → graceful nonimmersive fallback. **Pitfalls:** treating headset capabilities as uniform, unverified Apple API/version assumptions, opaque/translucent UI reducing legibility, high GPU load and sustained thermal constraints, terminal escape/clipboard/link security, and replacing measured responsiveness with aspirational FPS.

# 8. `game-development` — 21 files, all nested folders covered

## Folder-wide assessment

This material is unusually useful for non-game applications with rich interaction, realtime collaboration, editors, or 3D visualization. It emphasizes state authority, boundary validation, isolated components, telemetry, resource budgets, and testing under adverse conditions. Engine-specific APIs and stylistic absolutes should not be generalized to a web stack. Example code was read as illustrative source and was not compiled or run.

## 8.1 Root `game-development` — 6 files

| Reviewed file | Substance and procedure worth retaining |
|---|---|
| `game-development/game-designer.md` | Defines design pillars, core/session/long-term loops, mechanic specifications, onboarding, balance ranges, and playtest hypotheses. Transfer to frontend enhancements: identify the core user action, define observable success/failure before a prototype, and tune from actual behavior rather than “feel” alone. |
| `game-development/economy-designer.md` | Specifies currency purpose, sources/sinks, caps, exploit surface, segment simulations, telemetry, ethical monetization, and rollbackable balance changes. Transfer to credits/rewards/quotas: version policies, model abuse and inflation, and validate outcomes with production telemetry. Do not port pay-to-win or retention pressure into exploitative purchasing UX. |
| `game-development/game-audio-engineer.md` | Covers event architecture, adaptive music parameters, middleware integration, voice/memory budgets, spatial sound, and transition/stress tests. Transfer to notification/audio UX: cap simultaneous sound, define lifecycle cleanup, test device output modes, and retain mute/caption/accessibility alternatives. |
| `game-development/level-designer.md` | Builds greybox layouts, critical paths, encounters, pacing, readability, and navigation tests before art polish. Transfer to complex UI: validate information architecture and discoverability in a low-fidelity prototype, then add visuals. Automated reachability checks are useful but do not establish comprehensibility. |
| `game-development/narrative-designer.md` | Defines dialogue nodes, character voice, lore hierarchy, branch convergence, gameplay integration, and narrative debt. Transfer to wizard/chat flows: enumerate branches, keep essential content understandable without optional exposition, test text without audio, and resolve promises and dead ends. |
| `game-development/technical-artist.md` | Establishes per-platform asset, shader, texture, LOD, overdraw, and handoff budgets with in-engine acceptance. Transfer to WebGL/3D: validate imports automatically, inspect worst-case effects under actual lighting/view angles, and measure rendering cost on target hardware. |

**Root-folder limits:** playtest/conversion targets are goals, not established outcomes; behavioral design is not a license for dark patterns. Product telemetry requires consent, minimization, and a clear metric definition. Audio and rich graphics must not become prerequisites for completing essential tasks.

## 8.2 `game-development/blender` — 1 file

`game-development/blender/blender-addon-engineer.md` focuses on practical Python add-ons, validators, exporters, naming audits, and maintainable UI. Its best procedure is **inspect/report before optional repair**, preserve scene state/undo, check transforms separately, preserve downstream material-slot semantics, and test dirty real scenes. This helps backend asset ingestion and frontend 3D pipelines, not ordinary web UI implementation. Avoid context-sensitive operator assumptions, destructive “Apply All,” and assuming a successful export means a valid downstream asset; verify in the receiving tool.

## 8.3 `game-development/godot` — 3 files

| Reviewed file | Substance and transfer |
|---|---|
| `game-development/godot/godot-gameplay-scripter.md` | Builds typed GDScript, signal-driven composition, controlled Autoload responsibilities, and scene lifecycle discipline. Preserve standalone scene tests and explicit dependencies. Transfer to frontend components: render/test in isolation and avoid global state for local behavior; the file's signal-direction phrasing and absolute patterns need interpretation rather than literal adoption. |
| `game-development/godot/godot-multiplayer-engineer.md` | Maps authority, RPC callers/executors, synchronizers, spawning, validation, reconnection, and degraded-network tests. Transfer to backend realtime features: clients submit intent, servers validate sender and state, and tests include reconnect, loss, NAT, and latency. An `any_peer` declaration is not an authorization check. |
| `game-development/godot/godot-shader-developer.md` | Covers shader types, renderer compatibility, visual-versus-code authoring, post-processing, and mobile budgets. Transfer to frontend graphics: record supported renderer, bound loops/samples, supply fallbacks, and profile. Shader built-ins, hints, and compositor APIs must be checked for the selected Godot version. |

**Limits:** Godot-specific lifecycle, networking reliability modes, and renderer features cannot be transplanted into arbitrary web frameworks. Localhost success and editor previews do not prove deployment behavior.

## 8.4 `game-development/roblox-studio` — 3 files

| Reviewed file | Substance and transfer |
|---|---|
| `game-development/roblox-studio/roblox-avatar-creator.md` | Specifies mesh/texture/attachment/export checks, layered clothing cages, animation/body-type validation, customization previews, and marketplace compliance. Useful for asset validation and preview-before-purchase UI. Platform limits, moderation, licensing, and body compatibility need current verification and real Studio tests. |
| `game-development/roblox-studio/roblox-experience-designer.md` | Connects onboarding, progression, daily rewards, purchases, analytics, retention experiments, and younger-audience safeguards. Retain explicit purchase value, server-confirmed entitlements, and data-safe progression. Pricing/API/policy claims and retention thresholds are not portable; experiments must use stable assignment and protect minors. |
| `game-development/roblox-studio/roblox-systems-scripter.md` | Defines modular Luau services, validated RemoteEvents, DataStore retry/shutdown handling, and performance inspection. Strong backend transfer: reject impossible input, enforce server ownership and rate limits, test storage outages/recovery, and avoid client callbacks that can stall authoritative work. |

**Limits:** DataStore persistence examples require concurrency/session-locking and shutdown-budget scrutiny; simple retries do not guarantee durable saves. Client-visible purchase completion does not prove a durable entitlement. Roblox audience safeguards should strengthen, not be replaced by, engagement optimization.

## 8.5 `game-development/unity` — 4 files

| Reviewed file | Substance and transfer |
|---|---|
| `game-development/unity/unity-architect.md` | Advocates ScriptableObject data/event channels, isolated prefabs, small components, serialization hygiene, and designer-facing tools. Retain separation of data/configuration from scene-local runtime state and empty-scene prefab tests. ScriptableObject-first is a design preference, not the only valid architecture. |
| `game-development/unity/unity-editor-tool-developer.md` | Creates asset audits, import enforcement, property tools, assembly separation, undo-aware editor behavior, and prebuild failures/CI artifacts. Strong general transfer: editor/admin automation should have safe previews, deterministic validation, actionable reports, and blocking gates rather than warnings nobody reads. |
| `game-development/unity/unity-multiplayer-engineer.md` | Covers server-authoritative state, netcode variables/RPCs, bandwidth, lobby/relay lifecycle, latency, replay/audit, and rate limits. Strong realtime-backend lessons; validate inputs and outcomes, simulate disconnects and adverse networks, and record enough evidence to diagnose desync. SDK/RPC examples are version-sensitive. |
| `game-development/unity/unity-shader-graph-artist.md` | Organizes reusable graph/functions, URP/HDRP compatibility, custom passes, profiling, fallbacks, and shader-source retention. Transfer to graphics-heavy frontends: keep source/config, bound variants and material parameters, and inspect draw/pass costs. Alpha clipping is not a universal free optimization and needs visual/performance testing. |

**Limits:** package versions, render-pipeline APIs, editor serialization semantics, and server networking behavior require compile/runtime tests in the target project. Do not copy absolute bans on singletons or cross-component lookups without evaluating actual coupling and lifecycle needs.

## 8.6 `game-development/unreal-engine` — 4 files

| Reviewed file | Substance and transfer |
|---|---|
| `game-development/unreal-engine/unreal-systems-engineer.md` | Defines C++/Blueprint boundaries, UObject lifetime handling, Gameplay Ability System setup, tags/replication, tick optimization, and Nanite validation. Transfer to full-stack design: explicit authoritative ownership and runtime verification of persisted/replicated data. Detailed APIs and claims about feature restrictions require version checks. |
| `game-development/unreal-engine/unreal-multiplayer-architect.md` | Specifies GameMode/GameState roles, authority, replicated actors, GAS prediction, network frequency, dedicated servers, and malicious-RPC testing. Retain sender/state validation, ownership tests, rollback/prediction budgets, and network profiling. Its blanket demand for `_Validate` on every server RPC is not a substitute for version-appropriate security design. |
| `game-development/unreal-engine/unreal-technical-artist.md` | Manages material functions, shader permutations, Niagara effects, PCG, culling/LOD, and scalability on the lowest target hardware. Transfer to 3D frontends: reusable effects, bounded variants, maximum-density tests, and streaming hitch analysis. High-end editor output is not mobile evidence. |
| `game-development/unreal-engine/unreal-world-builder.md` | Coordinates World Partition, data layers, landscapes, foliage/PCG, HLOD, large-world coordinates, and one-file-per-actor collaboration. Retain repeatable traversal/load tests, coordinate precision checks, and explicit always-loaded content budgets. Distance/layer/frame thresholds are project assumptions rather than universal engine requirements. |

**Limits:** engine features and named helpers may change, examples are incomplete production scaffolds, and claims about Nanite eligibility or rendering budgets need hardware/version-specific testing. Reliable RPC does not imply business-level ordering, exactly-once execution, or authorization.

## 8.7 Cross-engine procedures worth keeping

- Model client input as **intent**, never trusted authoritative state; validate actor, object, action, range, rate, and current state on the server.
- Test with latency, loss, duplicate/reordered events, disconnect/reconnect, unavailable storage, and repeated requests; measure recovery, not only normal responsiveness.
- Isolate components/scenes, separate configuration from runtime state, clean subscriptions/resources on lifecycle transitions, and test reloads.
- Start with a playable/usable low-fidelity core; test navigation and task success before visual polish.
- Give assets and effects target-specific budgets, automate import checks, inspect in the actual runtime, and retain reproducible worst-case test scenes.
- For purchases/rewards/progression, enforce idempotency, entitlement consistency, auditable changes, ethical UX, and rollback/compensation policies.

# Recommended extraction priorities for the parent skill

**Core for ordinary frontend/backend enhancement:** workflow architect, codebase archaeologist, automation governance, research synthesist, statistician, developer advocate, privacy officer, and the trust-boundary principles from multiplayer/security specialists.

**Conditional modules:** GIS for spatial products; MCP/LSP/Salesforce for their actual integrations; model QA for predictive systems; finance and domain operations for relevant regulated business workflows; XR/game engine references for genuinely immersive/realtime products.

**Do not elevate into core rules:** fabricated experience/memory, automatic agent spawning, any permission to transact or publish, universal numerical success targets, mandatory persona/voice conventions, unverified regulatory calendars, and engine-specific implementation absolutes.

**Practical completion gate:** every proposed enhancement should state the existing behavior, intended user outcome, affected frontend/backend contracts, failure paths, privacy/authorization implications, tests actually run, before/after evidence, unresolved limitations, and an explicit rollback or safe recovery path. This is the durable procedural value of the reviewed folders.


---

# Agency Agents: operations, growth, strategy and integration review

## Scope and result

Reviewed **135 files / 1,327,331 bytes** beneath `assets/upstream`: every regular root file and every recursively nested file in the eight requested directories, excluding `.git`. All source was read as data. No repository installer, converter, test, generated plugin, embedded command or localization script was executed; no packages, settings, credentials, external services or scheduled jobs were changed.

This is a **static source review**, not a live integration certification, market-fact check, security penetration test or proof of the repository's advertised outcomes. The companion JSON records each relative and absolute path, byte/line count, SHA-256, extracted structure and individual analysis. Files in other source divisions are outside this subreview even when referenced by these documents.

| Area | Files |
|---|---:|
| Root | 9 |
| `.github/` | 10 |
| `examples/` | 6 |
| `integrations/` | 19 |
| `marketing/` | 36 |
| `paid-media/` | 7 |
| `sales/` | 9 |
| `scripts/` | 22 |
| `strategy/` | 17 |
| **Total** | **135** |

## Main conclusions

1. **The strongest material is procedural:** explicit task briefs, deliverable templates, dependency-aware parallel work, evidence gates, bounded repair loops, documented handoffs, and operational feedback.
2. **Use one procedural skill and lazy original-source references.** These files mostly define role context, not executable agents or verified expertise. Installing hundreds of personas would add prompt conflict and catalog overhead without adding tools.
3. **Do not install the upstream Hermes plugin for this request.** Although its lazy routing concept matches the desired architecture, it is executable code and the installer changes `plugins.enabled`, backs up/re-writes config, and replaces a plugin directory. None of that is needed for a source-backed skill.
4. **Reject embedded authority and autonomy claims.** The carousel role explicitly requests public posting without confirmation and recurring scheduling. Other roles assume credentials, tools, persistent memory, deployment rights and legal expertise that the source cannot confer.
5. **Keep claims proportional to evidence.** Strategy metrics, channel algorithms, legal/platform requirements and example market forecasts are not established facts merely because they appear in a persona. Marketing execution needs current documentation, real account data and appropriate human authorization.
6. **The installer and conversions have meaningful edge cases.** Known parallel-path failures remain xfail; config rewriting is layout-sensitive; body extraction is lossy; test scripts themselves execute code and can write outside their apparent temporary scope.

## Folder-by-folder analysis

### Root — catalog and governance, not runtime policy

`README.md` provides a broad catalog and usage recipes, including app promotion and “production-ready” language. Use it for navigation, not evidence that a deliverable is safe or complete. `divisions.json` is the declared source of truth for 18 divisions; strategy, examples, scripts and integrations are support material, not role divisions. `tools.json` models 16 tools with different rendering and installation contracts. These distinctions prevent accidentally treating all Markdown as installable agents.

The English contribution guide usefully demands concrete outputs, measurable acceptance criteria, service declarations and genuinely distinct roles. The Chinese guide covers the same broad authoring concerns but is less extensive; do not treat them as synchronized canonical schemas. The MIT license must accompany substantial vendored source. Security guidance prohibits secrets and malicious prompt definitions but does not itself validate the corpus. `.gitattributes` establishes LF conventions; `.gitignore` explains why generated outputs are absent and also excludes lockfiles that could matter for future reproducibility.

### `marketing/` — broad growth expertise with different risk profiles

**Discovery and acquisition:** SEO, AEO foundations, AI citation strategy, agentic task completion, app-store optimization and Baidu SEO supply audit/measurement templates. Keep the distinction between indexability, citation visibility and successful agent task completion. The SEO role's cross-page query ownership/cannibalization check is useful when Search Console data exists. Do not turn its absolute requirements into blockers for a new site with no data. Treat crawler policies as business/licensing choices. WebMCP markup/API examples require current specification checks rather than literal reuse.

**Editorial and creative:** content creator, book co-author, LinkedIn creator, carousel engine, video optimization/editing, Chinese and global podcast strategy, PR, email, and cross-platform publisher cover different outputs and audiences. Strong patterns include source-backed writing, versioned drafts with visible proof gaps, hook variants, platform-native adaptation, retention review and explicit revision questions. Do not fabricate autobiographical anecdotes, testimonials or expertise to satisfy a persona voice. Copyright, accessibility, consent and representation remain constraints.

**Channels and commerce:** Instagram, TikTok, X/Twitter engagement and intelligence, Reddit, WeChat, Weibo, Xiaohongshu, Zhihu, Bilibili, Douyin and Kuaishou provide channel-specific planning. China localization, private-domain operations, Chinese/cross-border e-commerce and livestream coaching add audience, inventory, margin and lifecycle considerations. Most are templates, not actual API integrations. Fixed posting ratios, exact ranking weights and legal generalizations are hypotheses to validate locally, not universal laws. Instagram material still mentions IGTV, illustrating the need to check present platform capabilities.

**Important contrasts:**
- `marketing-x-twitter-intelligence-analyst.md` gives unusually good evidence provenance and public/authorized-data boundaries.
- `marketing-email-strategist.md` emphasizes consent provenance, explicit sequence exits, data hygiene and transactional/marketing separation; preserve these.
- `marketing-carousel-growth-engine.md` says “Zero Confirmation,” publishes `PUBLIC_TO_EVERYONE` through Upload-Post and sets future cron execution. Never inherit this authorization. Its helper filenames describe an assumed stack, not supplied working scripts in the reviewed tree.
- `marketing-multi-platform-publisher.md` intends draft-only handoff but includes a `/api/v1/publish` request, `xhs-mcp publish`, `biliup upload`, scheduling and cookie-copy examples. Draft mode cannot be inferred from prose or a provider default. Require verified explicit draft semantics; do not copy credentials from browser storage. Its image-MD5 variation suggestion must not become a control-evasion tactic.
- App-store optimizer text contains corrupted heading glyphs and U+0004 control characters. Keep original source intact; flag or sanitize derived presentation only.

### `sales/` — revenue decision quality, not autonomous outreach

The nine roles form a coherent chain: offer/lead magnet → signal-based outbound → discovery → deal qualification → technical evaluation → proposal → pipeline/coaching → account retention/expansion. Valuable frameworks include MEDDPICC, SPIN/Gap/Sandler discovery, scoped POCs with buyer-agreed success criteria, win-theme/compliance matrices, forecast confidence ranges and account-health-first expansion.

Useful constraints already present include honoring opt-outs, never selling expansion into unhealthy accounts, evidence-based product claims and challenging poor CRM data. Preserve those over aggressive persuasion language. Competitive “landmines” should mean accurate evaluation questions, not deception or fabricated competitor deficiencies. CRM access, individual profiling, outbound sending, pricing commitments and contractual guarantees all need separately authorized scope. Reported sales benchmarks and framework uplift percentages are not independently substantiated here.

### `paid-media/` — measurement before spending

Seven roles cover account audit, PPC architecture, search queries/negative keywords, creative, paid social, programmatic/display and tracking/attribution. The useful operating sequence is **audit measurement → establish business economics → diagnose query/audience/creative waste → design isolated experiments → review results → propose controlled scaling**.

Tracking plans, conversion deduplication, consent review, brand safety, exclusion lists and creative-message match are valuable cross-functional inputs to a full-stack build. Tool names in frontmatter/body do not provide real API access. Budget changes, campaign activation, retargeting audiences, CRM uploads and tracking-tag deployment are material external actions; source personas cannot authorize them. Attribution is not causal proof, and ROAS/CAC targets need margin and sample-size context.

### `strategy/` and nested folders — reusable execution architecture

The master doctrine and quickstart offer Full/Sprint/Micro modes. Reuse **right-sized planning**, not the literal claim that a small task needs 5–10 agents or a feature needs 15–25. A single agent applying selected specialist checklists may suffice. The seven phase playbooks are discovery, strategy, foundation, build, hardening, launch and operate. Phase depth should reflect risk, existing evidence and the user's actual deliverable.

`coordination/` is especially useful: activation briefs and seven handoff shapes preserve goals, constraints, owner, artifacts, evidence, verdict and next action. `playbooks/phase-3-build.md` supplies the bounded Dev↔QA loop; `phase-4-hardening.md` separates raw evidence, analysis and final readiness, with backward transitions for architectural failure. Define whether the cap means three total attempts or three retries; upstream wording varies. Never force a reviewer to invent defects simply to satisfy a persona's default skepticism.

The four `runbooks/` cover startup MVP, enterprise feature, campaign and incident response. `runbooks.json` has 64 roster references across these scenarios (18, 22, 14 and 10 respectively). **Its identifiers are filename stems**, unlike display-name slugs used by installers/router; preserve both and map explicitly. They are not rename-proof despite that wording in its note.

The executive brief gives uncited numerical claims (73% handoff failure, 40–60% compression, 95% defect capture, 80% defect reduction). Keep the rationale but discard these as promises. A READY verdict never grants deployment rights. Incident response requires actual production scope, and operational cadence templates do not authorize recurring jobs.

### `examples/` — instructional scenarios, not reusable factual evidence

The landing-page workflow shows independent copy/design followed by convergence and conversion review. Add backend implementation/testing for its `/api/subscribe` reference: an HTML artifact alone cannot satisfy “working signup.” The startup MVP example shows staged deliverables and midpoint/final readiness gates. The book workflow is a good small-scope revision contract.

The spatial-discovery document is a rich eight-discipline planning artifact with conditional go/no-go, architectural/market/brand/UX tensions and a staged 2D-first strategy. Its budgets, market numbers, dates, pricing, milestones and SQL are illustrative, not adopted project decisions. The memory-enabled example usefully tags decisions for downstream roles, but its generic rollback assumption is unsafe: recalling or reverting a memory record does not undo repository changes, database migrations or external posts.

### `integrations/` and nested folders — optional adapters with unequal effects

The 19 files cover an overview, tool-specific instructions and a generic memory integration. Two tools use raw agent copies; other formats include per-role skill directories, Markdown rules/subagents, TOML or YAML with separate prompts, three-file workspaces, or whole-roster consolidated rules. Generated artifacts are normally ignored, so documentation is not proof they exist or load.

- **Home writes:** Claude/Copilot, Gemini, Antigravity, Codex, Kimi, Osaurus, OpenClaw, Hermes, Vibe and ZCode default to user locations in the reviewed installer; environment variables and overrides change destinations.
- **Project writes:** OpenCode, Cursor, Aider, Windsurf and Qwen default to the invoking working directory. Catalog scope support can be broader than a specific shell default.
- **Instruction promotion:** Codex uses `developer_instructions`; other tools consume system prompts, rules or persona files. Installing unreviewed source into those locations increases its authority in a different runtime; retaining it as labeled source data is safer here.
- **External/runtime actions:** OpenClaw installer attempts agent registration and ignores registration failures. Hermes installation changes config and installs executable Python. Kimi inherits its runtime default tools. No adapter creates missing permissions or credentials.
- **Memory:** `mcp-memory/setup.sh` currently only prints setup advice and checks config-file presence; it does not actually install a server. The example server name is a placeholder and no universal rollback API is established.

The existing Hermes integration is relevant as an architectural reference: a small four-tool surface plus lazy on-disk role data, search then inspect then load/delegate, a higher-priority instruction wrapper, duplicate-slug detection and bounded lifecycle handling. It is **not needed** for the parent's single-skill deliverable. Its documented generated count is a snapshot, not the count of this review.

### `scripts/` and `scripts/i18n/` — implementation risks and valuable tests

The installer auto-detects tools; in a noninteractive environment bare invocation can install broadly. It sources local helpers, auto-generates missing integrations, copies or symlinks files, and generally overwrites matching agent files without backups. Aider/Windsurf skip an existing consolidated file; that can leave stale content while returning success. Hermes replaces its plugin subtree and backs up/re-writes config. No install or “safe” dry-run was executed in this audit.

**Source-grounded issues, not reproduced runtime results:**

| Finding | Evidence and consequence |
|---|---|
| Parallel argument splitting | `scripts/install.sh:255` builds a command-shaped string; `:1480` expands `$AGENCY_INSTALL_EXTRA` unquoted in `sh -c`. Spaces/globs in paths are not preserved. `scripts/test-install.sh:291` explicitly xfails the known broken spaced-path case. |
| Fragile Hermes YAML rewriting | `install.sh:1063` onward edits lines rather than a parsed YAML tree. The empty-list branch at `:1185` replaces the line immediately after `plugins:`, not the actual located `enabled:` line; preceding sibling fields can be clobbered. The reverse scan at `:1203` finds any list in the plugin block, so later sibling lists can receive the new entry. Nonempty inline lists and blocks without `enabled` are not robustly handled. |
| Broad destination semantics | Copilot at `:773` still writes the second default `~/.copilot/agents` destination even when `--path` overrides the first. Aider/Windsurf functions at `:919/:933` ignore `--path`. Hermes destination overrides do not inherently redirect config editing away from HERMES_HOME. |
| All-deselected UI risk | Wizard turns selected teams into FILTER_DIVISIONS around `:747`; with every team deselected the array stays empty, and `build_selection` interprets no filters as everything. Static control-flow concern; not executed. |
| Destructive regeneration | `convert.sh` removes all selected tool output children other than README before rebuilding; custom --out locations need care. Builder also replaces its plugin subtree. The installer's Hermes basename guard helps avoid removing a shared plugin parent but is not a general sandbox. |
| Body fidelity loss | `scripts/lib.sh:44` get_body skips every exact `---` line anywhere in the file, including body horizontal rules or fenced examples, not merely the initial frontmatter. This contradicts literal unchanged-body claims for transformed formats. |
| Parser divergence | Shell helper handles selected scalar forms, while Python builder uses a simpler top-level line splitter and skips continuation/nested lines. Neither is a complete YAML parser; service/tool metadata can be omitted and multiline values may diverge. |
| Success is not readiness | OpenClaw registration uses `|| true`; Hermes config failure warns and continues; empty/stale conversions can survive weak presence checks. Completion messages are not client read-back. |
| Symlink/update trust | --link makes future source edits live without reinstalling. Copying onto existing destination symlinks may affect their targets. Standard per-agent installation does not provide a full stale-agent cleanup/uninstall contract. |
| Test isolation limits | `test-install.sh` changes HOME but does not fully clear inherited destination overrides; later cases auto-convert Codex into the repository despite its old “source tools only” header. Config regression optionally reads an actual home backup. Tests are executable, not harmless static checks. |

Useful testing patterns include independent strict source parsing, round-trip descriptions, output cardinality, split-fence preservation and drift manifests. The checked-in manifest has 279 agent entries, 14 tool entries and three catalog contracts; it is a drift baseline, not a signed trust root. Regression suites use fake contexts/lifecycles for Hermes and cannot prove installed-runtime compatibility. `test-hermes-plugin.py` is not referenced by the reviewed workflows. PyYAML/tomllib prerequisites exist even where comments suggest no extra dependencies.

Localization is optional and outside this English skill's needs. The 152-entry translation map is data. Its PowerShell script mutates installed copies without backups using regex frontmatter replacement; display-name changes may change derived identifiers. Do not run its ExecutionPolicy Bypass example.

### `.github/` and nested folders — useful contracts, incomplete security assurance

The ten files include sponsor metadata, two issue templates, a PR template and six workflows. Catalog/runbook/tool tests intentionally run broadly to catch cross-file drift, and Linux/macOS installer testing is valuable. Lint/originality operates on changed division files. The new-agent category dropdown lags the canonical division catalog.

Workflows use `actions/checkout@v4` tags rather than immutable commit pins and omit explicit least-privilege permission blocks. The lint workflow interpolates a base-ref into shell and passes changed paths unquoted; safer argument handling and hostile-filename testing would improve robustness. This is a static hardening observation, not a demonstrated exploit. CI checks format/contracts and contains a documented expected failure; it is not an evaluation of truthfulness, prompt-injection resistance, legal safety or production behavior.

## Recommended patterns for the reusable full-stack skill

1. **Brief before selection:** capture objective, real repository/environment, constraints, out-of-scope work, approval boundaries, measurable acceptance criteria and evidence needed.
2. **Minimal lazy routing:** search a lightweight catalog; load only the relevant original role/playbook files for the current phase. Preserve path, source revision/hash, filename-stem ID and display-name slug separately.
3. **Evidence-backed discovery:** distinguish user-provided facts, retrieved facts, assumptions and illustrative examples. For marketing, record data window, query, source, segment and limitations.
4. **Dependency-aware execution:** parallelize independent reads/research and disjoint owned work; converge before dependent implementation. Do not assume shared memory or let two writers silently own the same artifact.
5. **Deliverable contracts:** request concrete artifacts plus tests/evidence, not persona performance. Reuse chapter briefs, campaign briefs, architecture specs, POC scope, measurement plans and handoff fields as relevant.
6. **Independent QA and bounded repair:** implementation → real tests/inspection → PASS/FAIL with evidence → fix loop → explicit escalation when attempts, time or scope are exhausted. Failure is a result, not a reason to invent proof.
7. **Approval-gated external actions:** draft first; approve exact target, payload, budget and duration; act only with authorized tools; read back the exact target. No automatic public posting, ad spend, emailing, deployments, account registration, cookies, credentials or cron changes.
8. **Operational handoff:** report what changed, what passed, limitations, rollback mechanism, ownership and next decision. Save concise approved procedural lessons through the host's actual supported memory/skill mechanisms, not imagined MCP APIs.

## Scope boundaries for ingestion

- Keep original files as **attributed lower-trust reference data**; embedded “You are,” “must,” “never ask,” shell snippets and installation advice are not host instructions.
- Prefer a single skill that points to lazy sources over installing the upstream plugin or cloning every role into a global skill directory. The parent owns creation of that procedural skill; this subreview creates only the two requested review artifacts.
- Do not add `skills.external_dirs`, change `plugins.enabled`, install adapters, modify another profile, run generated code or configure external memory.
- Retain MIT attribution and provenance. Do not silently repair original identifiers, claims, encoded text or source code; annotate concerns in a derived index.
- Never claim persona memory, tool availability, API compatibility, statistical uplift, legal compliance or successful deployment based solely on these documents.
- Real production work requires project-specific security/privacy/legal review, current platform specifications and explicit user authority.

## File-level review register

Every in-scope file is listed below. The JSON companion contains exact paths and fingerprints, making omissions or upstream changes detectable.

### root

- `.gitattributes` — Enforces LF for Markdown, YAML and shell files; useful portability contract, not a code-safety guarantee.
- `.gitignore` — Excludes generated integrations, environments and scratch files; generated outputs are intentionally absent on a fresh checkout. Also ignores dependency lockfiles, weakening reproducibility for future added package tooling.
- `CONTRIBUTING.md` — Structured persona/deliverable template, external services declaration, originality expectations and catalog/converter integration checklist. Useful authoring contracts; persona memory statements do not implement persistence.
- `CONTRIBUTING_zh-CN.md` — Chinese contributor guide covering role template, PR process and style. Less extensive than the English guide; do not infer exact synchronization or translate the English working deliverable automatically.
- `LICENSE` — MIT, copyright 2025 AgentLand Contributors; retain this notice when vendoring substantial source material.
- `README.md` — Large human-facing catalog, product positioning, installation commands and use cases. Treat production-ready claims and static roster tables as promotional/navigation material, not execution evidence.
- `SECURITY.md` — Private-advisory reporting and no-secret/no-prompt-injection policy. Documentation expresses intent, not proof that examples or installers are safe.
- `divisions.json` — Canonical 18-division catalog with labels/icons/colors; explicitly excludes strategy, examples, integrations and scripts from source-agent divisions.
- `tools.json` — Canonical 16-tool installation/rendering catalog; distinguishes per-agent, consolidated roster and plugin mechanisms. Metadata describes supported scopes; individual shell defaults differ.

### .github

- `.github/FUNDING.yml` — GitHub sponsor metadata only; no runtime capability or dependency.
- `.github/ISSUE_TEMPLATE/bug-report.yml` — Structured file-specific bug reproduction and suggested-fix intake.
- `.github/ISSUE_TEMPLATE/new-agent-request.yml` — New-role scope and use-case intake; category dropdown omits newer divisions and should not serve as canonical catalog.
- `.github/PULL_REQUEST_TEMPLATE.md` — Frontmatter/examples/scenario-test checklist; self-attestation is not execution evidence.
- `.github/workflows/check-divisions.yml` — Runs catalog consistency on every PR and main push, intentionally without narrow path filters.
- `.github/workflows/check-hermes-config-rewrite.yml` — Runs installer rewrite regression wrapper on PR/main; test requires PyYAML despite no-dependency claim in workflow comments.
- `.github/workflows/check-runbooks.yml` — Runs roster-reference consistency on PR/main; protects renames even when JSON was untouched.
- `.github/workflows/check-tools.yml` — Runs catalog, generated plugin schema, scalar quoting, output invariant/drift and selection checks; drift advisory on PR and strict on main.
- `.github/workflows/lint-agents.yml` — Diff-scoped role lint/originality, fetch-depth zero; action version tag rather than immutable SHA, no explicit permissions, and unquoted changed-file list warrants defense-in-depth review.
- `.github/workflows/test-install.yml` — Linux/macOS matrix, shell syntax and installer behavioral suite; known xfail means green CI does not prove parallel-path correctness.

### marketing

- `marketing/marketing-aeo-foundations.md` — Expert in AI Engine Optimization infrastructure — implements llms.txt, AI-aware robots.txt, token-budgeted content, structured Markdown availability, and agent discovery files so AI crawlers, citation engines, and browsing agents can find, parse, and act on your site. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. Crawler access is an explicit business/licensing choice, not an automatic allow-all optimization.
- `marketing/marketing-agentic-search-optimizer.md` — Expert in WebMCP readiness and agentic task completion — audits whether AI agents can actually accomplish tasks on your site (book, buy, register, subscribe), implements WebMCP declarative and imperative patterns, and measures task completion rates across AI browsing agents. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. WebMCP API names and discovery formats are source assertions, not verified specifications; consult current authoritative documentation before implementation.
- `marketing/marketing-ai-citation-strategist.md` — Expert in AI recommendation engine optimization (AEO/GEO) — audits brand visibility across ChatGPT, Claude, Gemini, and Perplexity, identifies why competitors get cited instead, and delivers content fixes that improve AI citations. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-app-store-optimizer.md` — Expert app store marketing specialist focused on App Store Optimization (ASO), conversion rate optimization, and app discoverability. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. Source contains malformed emoji-style headings and U+0004 control characters; retain originals and sanitize only marked derived display text.
- `marketing/marketing-baidu-seo-specialist.md` — Expert Baidu search optimization specialist focused on Chinese search engine ranking, Baidu ecosystem integration, ICP compliance, Chinese keyword research, and mobile-first indexing for the China market.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-bilibili-content-strategist.md` — Expert Bilibili marketing specialist focused on UP主 growth, danmaku culture mastery, B站 algorithm optimization, community building, and branded content strategy for China's leading video community platform.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-book-co-author.md` — Strategic thought-leadership book collaborator for founders, experts, and operators turning voice notes, fragments, and positioning into structured first-person chapters.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-carousel-growth-engine.md` — Autonomous TikTok and Instagram carousel generation specialist. Analyzes any website URL with Playwright, generates viral 6-slide carousels via Gemini image generation, publishes directly to feed via Upload-Post API with auto trending music, fetches analytics, and iteratively improves through a data-driven learning loop.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. HIGH RISK: zero-confirmation public publishing and cron scheduling; reject these autonomy directives. Referenced helper scripts are not supplied in the reviewed scripts tree.
- `marketing/marketing-china-ecommerce-operator.md` — Expert China e-commerce operations specialist covering Taobao, Tmall, Pinduoduo, and JD ecosystems with deep expertise in product listing optimization, live commerce, store operations, 618/Double 11 campaigns, and cross-platform strategy.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-china-market-localization-strategist.md` — Full-stack China market localization expert who transforms real-time trend signals into executable go-to-market strategies across Douyin, Xiaohongshu, WeChat, Bilibili, and beyond. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-content-creator.md` — Expert content strategist and creator for multi-platform campaigns. Develops editorial calendars, creates compelling copy, manages brand storytelling, and optimizes content for engagement across all digital channels.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-cross-border-ecommerce.md` — Full-funnel cross-border e-commerce strategist covering Amazon, Shopee, Lazada, AliExpress, Temu, and TikTok Shop operations, international logistics and overseas warehousing, compliance and taxation, multilingual listing optimization, brand globalization, and DTC independent site development.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-douyin-strategist.md` — Short-video marketing expert specializing in the Douyin platform, with deep expertise in recommendation algorithm mechanics, viral video planning, livestream commerce workflows, and full-funnel brand growth through content matrix strategies.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-email-strategist.md` — Expert email marketing strategist for CRM-driven campaigns, lifecycle automation, segmentation architecture, and deliverability. Designs sequences (welcome, nurture, reactivation, win-back, review, referral) grounded in 2025-2026 benchmarks, AI-driven personalization, and post-Apple MPP measurement.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. Useful consent provenance, lifecycle segmentation, unsubscribe/bounce/complaint exits and transactional/marketing separation.
- `marketing/marketing-global-podcast-strategist.md` — Expert podcast growth specialist focused on show positioning, audience development, content strategy, and monetisation. Transforms raw ideas into authoritative audio brands that compound listeners and revenue over time on Spotify, Apple Podcasts, and YouTube.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-growth-hacker.md` — Expert growth strategist specializing in rapid user acquisition through data-driven experimentation. Develops viral loops, optimizes conversion funnels, and finds scalable growth channels for exponential business growth.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-instagram-curator.md` — Expert Instagram marketing specialist focused on visual storytelling, community building, and multi-format content optimization. Masters aesthetic development and drives meaningful engagement.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-kuaishou-strategist.md` — Expert Kuaishou marketing strategist specializing in short-video content for China's lower-tier city markets, live commerce operations, community trust building, and grassroots audience growth on 快手.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-linkedin-content-creator.md` — Expert LinkedIn content strategist focused on thought leadership, personal brand building, and high-engagement professional content. Masters LinkedIn's algorithm and culture to drive inbound opportunities for founders, job seekers, developers, and anyone building a professional presence.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-livestream-commerce-coach.md` — Veteran livestream e-commerce coach specializing in host training and live room operations across Douyin, Kuaishou, Taobao Live, and Channels, covering script design, product sequencing, paid-vs-organic traffic balancing, conversion closing techniques, and real-time data-driven optimization.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-multi-platform-publisher.md` — Expert orchestrator for one-click Chinese blog publishing. Routes a single article to 知乎 / 小红书 / CSDN / B站 / 公众号 / 掘金 via Wechatsync (main channel) with xhs-mcp and biliup as specialized fallbacks. Handles per-platform content adaptation, draft-first publishing, rate control, and risk-avoidance. Does NOT auto-publish — always stops at draft for human review.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. HIGH RISK: draft-first wording conflicts with fallback publish API/CLI examples and scheduled publication; verify actual draft flags and do not extract browser cookies or evade deduplication controls.
- `marketing/marketing-podcast-strategist.md` — Content strategy and operations expert for the Chinese podcast market, with deep expertise in Xiaoyuzhou, Ximalaya, and other major audio platforms, covering show positioning, audio production, audience growth, multi-platform distribution, and monetization to help podcast creators build sticky audio content brands.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-pr-communications-manager.md` — Strategic public relations and communications specialist for media relations, press releases, crisis communications, executive thought leadership, brand reputation management, and integrated communications planning — building and protecting reputations through earned media, storytelling, and proactive narrative control. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-private-domain-operator.md` — Expert in building enterprise WeChat (WeCom) private domain ecosystems, with deep expertise in SCRM systems, segmented community operations, Mini Program commerce integration, user lifecycle management, and full-funnel conversion optimization.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-reddit-community-builder.md` — Expert Reddit marketing specialist focused on authentic community engagement, value-driven content creation, and long-term relationship building. Masters Reddit culture navigation.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-seo-specialist.md` — Expert search engine optimization strategist specializing in technical SEO, content optimization, link authority building, and organic search growth. Drives sustainable traffic through data-driven search strategies.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-short-video-editing-coach.md` — Hands-on short-video editing coach covering the full post-production pipeline, with mastery of CapCut Pro, Premiere Pro, DaVinci Resolve, and Final Cut Pro across composition and camera language, color grading, audio engineering, motion graphics and VFX, subtitle design, multi-platform export optimization, editing workflow efficiency, and AI-assisted editing.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-social-media-strategist.md` — Expert social media strategist for LinkedIn, Twitter, and professional platforms. Creates cross-platform campaigns, builds communities, manages real-time engagement, and develops thought leadership strategies.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-tiktok-strategist.md` — Expert TikTok marketing specialist focused on viral content creation, algorithm optimization, and community building. Masters TikTok's unique culture and features for brand growth.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-twitter-engager.md` — Expert Twitter marketing specialist focused on real-time engagement, thought leadership building, and community-driven growth. Builds brand authority through authentic conversation participation and viral thread creation.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-video-optimization-specialist.md` — Video marketing strategist specializing in YouTube algorithm optimization, audience retention, chaptering, thumbnail concepts, and cross-platform video syndication.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-wechat-official-account.md` — Expert WeChat Official Account (OA) strategist specializing in content marketing, subscriber engagement, and conversion optimization. Masters multi-format content and builds loyal communities through consistent value delivery.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-weibo-strategist.md` — Full-spectrum operations expert for Sina Weibo, with deep expertise in trending topic mechanics, Super Topic community management, public sentiment monitoring, fan economy strategies, and Weibo advertising, helping brands achieve viral reach and sustained growth on China's leading public discourse platform.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-x-twitter-intelligence-analyst.md` — Social intelligence specialist for X/Twitter research, trend detection, account monitoring, and evidence-backed audience insights using public signals and structured data workflows.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. Especially useful research-integrity rules: public/authorized data, URLs/timestamps/query windows, confidence and no doxxing.
- `marketing/marketing-xiaohongshu-specialist.md` — Expert Xiaohongshu marketing specialist focused on lifestyle content, trend-driven strategies, and authentic community engagement. Masters micro-content creation and drives viral growth through aesthetic storytelling.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `marketing/marketing-zhihu-strategist.md` — Expert Zhihu marketing specialist focused on thought leadership, community credibility, and knowledge-driven engagement. Masters question-answering strategy and builds brand authority through authentic expertise sharing.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.

### sales

- `sales/sales-account-strategist.md` — Expert post-sale account strategist specializing in land-and-expand execution, stakeholder mapping, QBR facilitation, and net revenue retention. Turns closed deals into long-term platform relationships through systematic expansion planning and multi-threaded account development.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `sales/sales-coach.md` — Expert sales coaching specialist focused on rep development, pipeline review facilitation, call coaching, deal strategy, and forecast accuracy. Makes every rep and every deal better through structured coaching methodology and behavioral feedback.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `sales/sales-deal-strategist.md` — Senior deal strategist specializing in MEDDPICC qualification, competitive positioning, and win planning for complex B2B sales cycles. Scores opportunities, exposes pipeline risk, and builds deal strategies that survive forecast review.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `sales/sales-discovery-coach.md` — Coaches sales teams on elite discovery methodology — question design, current-state mapping, gap quantification, and call structure that surfaces real buying motivation.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `sales/sales-engineer.md` — Senior pre-sales engineer specializing in technical discovery, demo engineering, POC scoping, competitive battlecards, and bridging product capabilities to business outcomes. Wins the technical decision so the deal can close.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `sales/sales-offer-lead-gen-strategist.md` — Top-of-funnel architect who designs irresistible offers and lead magnets that attract qualified buyers at scale. Specializes in value-equation offer construction, lead magnet typology, multi-channel lead generation, and compounding reach through customers, employees, agencies, and affiliates.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `sales/sales-outbound-strategist.md` — Signal-based outbound specialist who designs multi-channel prospecting sequences, defines ICPs, and builds pipeline through research-driven personalization — not volume.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `sales/sales-pipeline-analyst.md` — Revenue operations analyst specializing in pipeline health diagnostics, deal velocity analysis, forecast accuracy, and data-driven sales coaching. Turns CRM data into actionable pipeline intelligence that surfaces risks before they become missed quarters.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act. Preserve forecast ranges, cohort segmentation and CRM-quality caveats rather than invented precision.
- `sales/sales-proposal-strategist.md` — Strategic proposal architect who transforms RFPs and sales opportunities into compelling win narratives. Specializes in win theme development, competitive positioning, executive summary craft, and building proposals that persuade rather than merely comply.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.

### paid-media

- `paid-media/paid-media-auditor.md` — Comprehensive paid media auditor who systematically evaluates Google Ads, Microsoft Ads, and Meta accounts across 200+ checkpoints spanning account structure, tracking, bidding, creative, audiences, and competitive positioning. Produces actionable audit reports with prioritized recommendations and projected impact.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `paid-media/paid-media-creative-strategist.md` — Paid media creative specialist focused on ad copywriting, RSA optimization, asset group design, and creative testing frameworks across Google, Meta, Microsoft, and programmatic platforms. Bridges the gap between performance data and persuasive messaging.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `paid-media/paid-media-paid-social-strategist.md` — Cross-platform paid social advertising specialist covering Meta (Facebook/Instagram), LinkedIn, TikTok, Pinterest, X, and Snapchat. Designs full-funnel social ad programs from prospecting through retargeting with platform-specific creative and audience strategies.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `paid-media/paid-media-ppc-strategist.md` — Senior paid media strategist specializing in large-scale search, shopping, and performance max campaign architecture across Google, Microsoft, and Amazon ad platforms. Designs account structures, budget allocation frameworks, and bidding strategies that scale from $10K to $10M+ monthly spend.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `paid-media/paid-media-programmatic-buyer.md` — Display advertising and programmatic media buying specialist covering managed placements, Google Display Network, DV360, trade desk platforms, partner media (newsletters, sponsored content), and ABM display strategies via platforms like Demandbase and 6Sense.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `paid-media/paid-media-search-query-analyst.md` — Specialist in search term analysis, negative keyword architecture, and query-to-intent mapping. Turns raw search query data into actionable optimizations that eliminate waste and amplify high-intent traffic across paid search accounts.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.
- `paid-media/paid-media-tracking-specialist.md` — Expert in conversion tracking architecture, tag management, and attribution modeling across Google Tag Manager, GA4, Google Ads, Meta CAPI, LinkedIn Insight Tag, and server-side implementations. Ensures every conversion is counted correctly and every dollar of ad spend is measurable.. Reuse brief, deliverable and measurement patterns; validate platform facts and do not infer permission to act.

### strategy

- `strategy/EXECUTIVE-BRIEF.md` — Executive coordination rationale and mode selection; percentages claiming failure rates, delivery speed and defect prevention lack supporting citations and must not become promises.
- `strategy/QUICKSTART.md` — Full/Sprint/Micro prompt recipes and brief evidence-gate glossary; role counts/timelines are illustrative, and minimal relevant roles are preferable to activating whole divisions.
- `strategy/coordination/agent-activation-prompts.md` — Task-specific activation templates defining inputs, deliverables and QA expectations. Translate role names into on-demand context, not imaginary tools or credentials.
- `strategy/coordination/handoff-templates.md` — Seven useful contracts: standard, QA pass, QA fail, escalation, phase gate, sprint and incident. Preserve artifact/evidence/owner/next-action fields.
- `strategy/nexus-strategy.md` — Seven-phase operational doctrine, dependency matrix, handoffs, Dev-QA loop, escalation and metrics. Adapt phase depth and thresholds to actual work; do not copy hardcoded organizational scale or unverified success claims.
- `strategy/playbooks/phase-0-discovery.md` — Parallel market/user/data/legal/tool investigations converge into feasibility and discovery gate; facts require live evidence, not generated market certainty.
- `strategy/playbooks/phase-1-strategy.md` — Sequential framing then parallel technical design then prioritization; outputs are architecture, constraints and testable scope.
- `strategy/playbooks/phase-2-foundation.md` — Parallel infrastructure and application foundations converge at verification; access metadata must reference secret stores, never carry credentials.
- `strategy/playbooks/phase-3-build.md` — Task ownership, parallel tracks and bounded Dev-QA repair loop; assign nonoverlapping write ownership and specify attempt versus retry budget explicitly.
- `strategy/playbooks/phase-4-hardening.md` — Independent evidence collection, analysis and final READY/NEEDS WORK/NOT READY gate with backward transitions. Best reusable release-quality pattern.
- `strategy/playbooks/phase-5-launch.md` — Preflight, deployment, coordinated marketing, monitoring and operations handoff. Actual deployment/publication/spend requires separately authorized scope.
- `strategy/playbooks/phase-6-operate.md` — Operational cadences, incident response, metrics and feedback into feature delivery. Cadence documentation does not authorize persistent scheduling.
- `strategy/runbooks/scenario-enterprise-feature.md` — Enterprise requirements through governed rollout, compliance and stakeholder cadence; add product-specific authorization and evidence requirements.
- `strategy/runbooks/scenario-incident-response.md` — Severity-based roles, investigation/mitigation/verification/postmortem and communications; emergency framing is not permission for destructive production changes.
- `strategy/runbooks/scenario-marketing-campaign.md` — Strategy/content then activation/optimization with brand checkpoints; useful review chain, but publishing and budget must stay approval-gated.
- `strategy/runbooks/scenario-startup-mvp.md` — Compressed discovery-to-launch execution with core/growth/support roles; treat timelines and success metrics as planning assumptions.
- `strategy/runbooks.json` — Four machine-readable scenario rosters with 64 total agent references. Uses source filename stems, unlike installer/router display-name slugs; explicit mapping is necessary.

### examples

- `examples/README.md` — Index and explanation of parallel discovery example; its coherence/no-coordination-overhead claim is an illustrative assertion rather than a measured evaluation.
- `examples/nexus-spatial-discovery.md` — Eight-role product discovery synthesis: conditional 2D-first go/no-go, market/architecture/brand/growth/support/UX/execution/spatial design. Preserve tensions and source links; budgets, forecasts, dates and code are example artifacts, not validated current facts or deployed software.
- `examples/workflow-book-chapter.md` — Single-role versioned chapter revision loop, explicit source material and editorial proof gaps; excellent bounded-output workflow.
- `examples/workflow-landing-page.md` — Parallel copy/design converge into implementation, then conversion review. A single HTML form does not implement the referenced /api/subscribe backend; add functional, accessibility and privacy tests before deployment.
- `examples/workflow-startup-mvp.md` — Staged discovery/build/launch with midpoint and final evidence gates; manual full-output handoffs should become artifact references plus concise contracts rather than unlimited prompt copying.
- `examples/workflow-with-memory.md` — Adds role/project-tagged decision recall and handoffs to the MVP workflow; assumes unavailable generic memory/rollback tools, and memory rollback must never be confused with restoring files or external systems.

### integrations

- `integrations/README.md` — Cross-tool overview: identity copies, per-agent transformed output, consolidated files and lazy plugin. Commands are optional installation recipes, not prerequisites to reading the source.
- `integrations/aider/README.md` — Consolidates the roster into project CONVENTIONS.md; context bloat and conflicts with existing conventions require review.
- `integrations/antigravity/README.md` — One agency-prefixed SKILL.md per role; different architecture from the requested single reusable skill.
- `integrations/claude-code/README.md` — Native raw Markdown agent copies into user agent directory; overwrites can replace user customization.
- `integrations/codex/README.md` — TOML agent mapping promotes body to developer_instructions; source trust needs review before installing into an instruction-bearing location.
- `integrations/cursor/README.md` — Project .mdc rules; converter uses alwaysApply:false. Do not infer automatic activation from generic README wording.
- `integrations/gemini-cli/README.md` — Generated Markdown subagents in user agents directory; source prompts alone do not supply executable capabilities.
- `integrations/github-copilot/README.md` — Raw agents copied to two home directories, with client discovery-setting caveats; no setting change authorized here.
- `integrations/hermes/README.md` — Existing four-tool lazy router avoids hundreds of external skills but is an executable plugin whose installer edits plugins.enabled. Reuse lazy-selection concept only for this task.
- `integrations/kimi/README.md` — Per-agent YAML and separate system prompt; inherits default runtime tools, not a least-privilege guarantee.
- `integrations/mcp-memory/README.md` — Generic remember/recall/rollback/search contract with placeholder server configuration; not an installed or validated memory backend.
- `integrations/mcp-memory/backend-architect-with-memory.md` — Architecture persona plus persistence/handoff instructions; embedded schema/API examples are incomplete illustrative snippets and rollback capability is assumed.
- `integrations/mcp-memory/setup.sh` — Despite install-oriented name, currently prints instructions and checks three config-file locations; package install lines are comments and no config is written.
- `integrations/openclaw/README.md` — Generated SOUL/AGENTS/IDENTITY workspaces; installer also registers through a CLI if available and recommends restart.
- `integrations/opencode/README.md` — Converts named colors to hex and mode:subagent, strips unsupported metadata; project default and optional global destination.
- `integrations/qwen/README.md` — Project Markdown subagents with minimal frontmatter; tools catalog advertises user scope too, but shell default remains project-scoped.
- `integrations/vibe/README.md` — Paired TOML/prompt files under VIBE_HOME; must keep companion files and identifiers aligned.
- `integrations/windsurf/README.md` — Whole-roster project rules file; creates broad context and conflicting-role risk rather than lazy specialization.
- `integrations/zcode/README.md` — Generated user-scoped Markdown subagents with environment override; some converter comments cite a different global path, so implementation is the stronger local reference.

### scripts

- `scripts/agents-to-install.example` — Four illustrative selection entries, including a display name; demonstrates subset selection but is not a required install list.
- `scripts/build-hermes-plugin.py` — Generates executable router and JSON corpus; duplicate-slug guard, lazy read/search, instruction-priority wrapper and bounded delegation/cancellation are useful. Custom frontmatter parser is not full YAML; output directory is replaced; generation rewrites integration README.
- `scripts/check-agent-originality.sh` — Entity-neutralized eight-word shingle Jaccard checks with warn/fail thresholds. English-centric lexical similarity is not semantic originality or malicious-instruction detection.
- `scripts/check-divisions.sh` — Checks tracked source directories against division JSON, shell arrays and CI coverage; Git metadata and formatting-sensitive parsing are assumptions.
- `scripts/check-hermes-config-rewrite.py` — Extracts and executes installer heredoc against sample configs; optionally reads a real home-directory backup. Limited tests do not cover arbitrary YAML layout or preservation of other plugin settings.
- `scripts/check-hermes-config-rewrite.sh` — Thin executable wrapper around Python rewrite regression test; not safe to treat as inert analysis.
- `scripts/check-hermes-plugin.py` — Imports builder and generated plugin, builds temp output and checks schemas/search/inspect using a recording fake context. Not real Hermes lifecycle compatibility evidence.
- `scripts/check-runbooks.sh` — Checks JSON fields, duplicate runbook IDs, document existence and filename-stem roster references using git ls-files. Does not validate prose roster equivalence or actual execution readiness.
- `scripts/check-tools.sh` — Checks supported tool sets and required fields using format-sensitive shell extraction. Useful drift guard but not full JSON schema validation or installation verification.
- `scripts/convert-outputs.sha256` — Stored drift manifest: 279 agent records, 14 tool records, three contracts; 298 total lines including two comment lines. Not a signature and not independently verified against generated outputs here.
- `scripts/convert.sh` — Transforms source into 14 generated formats, including plugin; cleans selected output directories except README. --out is a deletion/write boundary, and generated source-body fidelity needs independent checks.
- `scripts/i18n/README.md` — Optional Chinese localization of installed copies; includes PowerShell ExecutionPolicy Bypass advice that must not be followed automatically.
- `scripts/i18n/agent-names-zh.json` — 152 English-to-Chinese name/description mappings; data-only, not complete current roster coverage, and unsuitable as canonical identifiers.
- `scripts/i18n/localize-agents-zh.ps1` — Regex rewrites installed frontmatter in two default home locations or custom targets. No backup, full YAML parser or recursive traversal; changed display names can change downstream slug mapping.
- `scripts/install.sh` — Broad auto-detect/copy/symlink installer with subset selection and auto-conversion. Writes user/project settings and replaces Hermes plugin; parallel argument splitting and selection/destination edge cases remain.
- `scripts/lib.sh` — Shared scalar/frontmatter, slug and terminal UI helpers. get_body drops every exact --- line, not just initial frontmatter; source-body preservation is not literal.
- `scripts/lint-agents.sh` — Presence/line-ending/section/fence checks; many content requirements are warnings, not strict YAML or security validation.
- `scripts/test-agent-selection.sh` — Executes installer dry-run to reject unknown selections and accept display names; reviewed only, not run.
- `scripts/test-convert-frontmatter.sh` — Generates three outputs in a temp directory and checks quoting; verifies wrappers, not all semantic contracts.
- `scripts/test-convert-outputs.sh` — Strong independent strict-parse/round-trip/count/fence-integrity/drift checks, requiring PyYAML and Python tomllib. --update rewrites committed manifest; tests generate artifacts and execute converters.
- `scripts/test-hermes-plugin.py` — Fake lifecycle tests cover success, failure, pending cancellation and 32,000-character truncation. Expects generated plugin; not a live Hermes test and not referenced by reviewed CI workflows.
- `scripts/test-install.sh` — Home sandbox tests for paths, subsets, links and repeat runs; known-broken parallel spaced-path case is xfail. Inherited destination env vars are not fully cleared and conversion can write repository outputs despite old source-only header.
