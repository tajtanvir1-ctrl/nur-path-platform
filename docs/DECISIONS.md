# Decision log

- NP-ADR-001: Preserve main; use existing feature branch and remote SHA checks.
- NP-ADR-002: Keep Flutter/FastAPI/PostgreSQL baseline; modular monolith, provider-neutral AI. No new paid dependencies.
- NP-ADR-003: Readiness returns 503 until real dependency probes; liveness alone never implies production readiness.
- NP-ADR-004: Founder permits controlled FreeLLMAPI evaluation; production activation still gated by privacy, reliability, provider terms and religious accuracy.
- NP-ADR-005: Dependency pins record installed direct versions only, not a verified transitive lock.

- NP-ADR-006: Expand all six launch groups and Year-1 tasks in a single acyclic dependency registry; use automated negative tests for registry integrity. Year-1 implementation requires separate phase decision.
- NP-ADR-007: Founder authorizes phase-wise routine development without repetitive approvals. Hourly scheduled execution is enabled; no assurance of future connector/runtime success. No production release or self-approval.

- NP-ADR-006: Sequential continuation is the default; scheduled attempts are a fallback, not uninterrupted compute. No arbitrary approval pauses. Planner identifies candidates, not authentic approvals. Year-1 remains separately gated.
