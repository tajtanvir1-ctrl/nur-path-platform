# Decision log

- NP-ADR-001: Preserve main; use existing feature branch and remote SHA checks.
- NP-ADR-002: Keep Flutter/FastAPI/PostgreSQL baseline; modular monolith, provider-neutral AI. No new paid dependencies.
- NP-ADR-003: Readiness returns 503 until real dependency probes; liveness alone never implies production readiness.
- NP-ADR-004: Founder permits controlled FreeLLMAPI evaluation; production activation still gated by privacy, reliability, provider terms and religious accuracy.
- NP-ADR-005: Dependency pins record installed direct versions only, not a verified transitive lock.
