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
