# Integration matrix — initial baseline

| Integration ID | Caller | API / service | Persistence | Evidence | Status |
|---|---|---|---|---|---|
| NP-INT-HEALTH-LIVE | HTTP probe | GET /api/v1/health/live | none | backend/tests/test_health.py; contract snapshot test | Locally verified |
| NP-INT-HEALTH-READY | HTTP probe | GET /api/v1/health/ready | none | health regression tests; expected 503 | Locally verified, intentionally not ready |
| NP-INT-DB | FastAPI repository | PostgreSQL via SQLAlchemy/Alembic | Neon development branch | connector SELECT 1 only | Planned app integration |
| NP-INT-MOBILE | Flutter | versioned FastAPI client | offline store planned | independent Flutter widget tests | No connected flow |

See integration-registry.json for machine-readable state. Extend feature-level mappings as routes/services/data and client tests become real; do not count planned rows as implemented. All product integrations remain pending.
