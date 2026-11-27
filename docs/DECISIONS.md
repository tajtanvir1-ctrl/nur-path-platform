# Decision log

- NP-ADR-001: Preserve main; use existing feature branch and remote SHA checks.
- NP-ADR-002: Keep Flutter/FastAPI/PostgreSQL baseline; modular monolith, provider-neutral AI. No new paid dependencies.
- NP-ADR-003: Readiness returns 503 until real dependency probes; liveness alone never implies production readiness.
- NP-ADR-004: Founder permits controlled FreeLLMAPI evaluation; production activation still gated by privacy, reliability, provider terms and religious accuracy.
- NP-ADR-005: Dependency pins record installed direct versions only, not a verified transitive lock.

- NP-ADR-006: Expand all six launch groups and Year-1 tasks in a single acyclic dependency registry; use automated negative tests for registry integrity. Year-1 implementation requires separate phase decision.
- NP-ADR-007: Founder authorizes phase-wise routine development without repetitive approvals. Hourly scheduled execution is enabled; no assurance of future connector/runtime success. No production release or self-approval.

- NP-ADR-006: Sequential continuation is the default; scheduled attempts are a fallback, not uninterrupted compute. No arbitrary approval pauses. Planner identifies candidates, not authentic approvals. Year-1 remains separately gated.

- NP-ADR-007: Core governance is verified only within its scoped acceptance. Domain documentation matures at mapped gates; no waiver of release criteria. CLAUDE.md retired, AGENTS.md canonical.
- NP-ADR-008: Observed Linux/Python 3.13 dependency closure and official Flutter 3.50.0 commit ab2912035e160d9cad6306df307576da6128ebdb selected for candidate CI verification, not yet validated as clean environment. CI uses read-only permissions and pinned official actions. Draft PR #1 is verification only, no merge.

- NP-ADR-009: Neon Free PostgreSQL for isolated development, Supabase Pro remains intended production target. Retain portable PostgreSQL migrations, provider-neutral auth/storage, least-privilege roles and verified TLS. No Firestore rewrite. See DEVELOPMENT_DATABASE.md.
- NP-ADR-010: CI remediation pins Ubuntu 24.04 for Python 3.13.5 and uses Flutter 3.50.0 tagged checkout with exact SHA and version assertion. Actual runner result required.

- NP-ADR-011: Pin Flutter 3.44.0 (559ffa3f75e7402d65a8def9c28389a9b2e6fe42) for existing Material API compatibility rather than suppress analyzer deprecations or introduce an unreviewed package. SDK warmed before machine version check. Generate Android/iOS scaffold in disposable CI stage; provisional namespace com.solvegrid is development-only. Review artifact before integrating. Do not cancel active verification merely to publish continuity documents.

- NP-ADR-012: Native staging reproduces the original package analyzer configuration rather than inheriting unrelated generated template lints. Check lock equality before artifact publication. No suppressed analyzer diagnostics, new dependencies or production identifiers.

- NP-ADR-013: Accept scoped CORE-002 using the verified pinned SDK native regeneration path and exact lockfile. Native source integration and compilation remain later requirements; debug signing and provisional identifiers are not release-ready.
- NP-ADR-014: FastAPI runtime OpenAPI snapshot is checked in CI and explicit regeneration requires --write; no silent contract drift. Integration registry distinguishes tested endpoints from planned app/database connectivity.

- NP-ADR-015: Keep modular FastAPI monolith, provider-independent verified issuer/subject identity mapping, app-owned UUID and portable PostgreSQL migrations. Initial schema default-deny RLS; no app grants until verified auth/role policy. Use PostgreSQL 17 disposable CI for first migration, no cloud writes until actual review. PostgreSQL 18 Neon and future Supabase target compatibility require separate verification.

- NP-ADR-016: External PostgreSQL runtime configuration accepts only dedicated nurpath_app role, separately configured target host/database, explicit port 5432 and exact verify-full/system CA parameters. Reject override parameters and redact errors. This preflight is not a TLS or authorization proof; verify actual driver and role privileges before connecting the app.

- NP-ADR-017: Founder prioritizes skipped/pending verification over next feature work. Apply reviewed additive Alembic SQL to authorized Neon development child only after actual PostgreSQL CI success. Provision read-only role for probe, no write policies or auth activation. Client TLS validation must use libpq client ssl_in_use with verify-full/system CA, not server-side proxy flag. Network DNS blocker must remain explicit; keep readiness fail-closed and no next task until current scope resolved.
