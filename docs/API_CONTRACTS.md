# API contracts — NP-ARCH-001 initial increment

FastAPI runtime OpenAPI 3.1 is exported as packages/api-contracts/openapi.json. Review contract changes and run python scripts/export_openapi.py --write only intentionally; default command checks exact canonical bytes. Backend tests verify runtime equality and unique operation IDs. No undocumented endpoint may be presented as implemented.

| Operation | Method/path | Response | Authentication | Data access |
|---|---|---|---|---|
| live_api_v1_health_live_get | GET /api/v1/health/live | 200 {"status":"alive"} | none | none |
| ready_api_v1_health_ready_get | GET /api/v1/health/ready | 503 {"status":"not_ready"} | none | none |

Readiness remains intentionally fail-closed until real dependency probes exist. No credentials or internal exception details in health responses. These are operational endpoints, not product features.

Future domain contracts must specify request/response schemas, authorization and ownership, errors, idempotency for mutations, pagination bounds, locale and time semantics, dependency availability and negative tests before implementation. Breaking contract changes require explicit review and versioning. Planned endpoints are not included in the runtime snapshot until implemented. Authentication and database adapters are provider-neutral; no direct client database credentials.
