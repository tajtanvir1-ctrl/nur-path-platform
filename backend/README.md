# Backend foundation spike

Python 3.13.5 was used for the initial local test. Install the listed direct dependencies in a disposable virtual environment (fresh dependency resolution has not yet been verified). From backend/: PYTHONPATH=. python -m pytest -q tests/test_health.py. For local smoke use python -m uvicorn app.main:app --host 127.0.0.1.

GET /api/v1/health/live -> 200 {"status":"alive"}.
GET /api/v1/health/ready -> 503 {"status":"not_ready"} until real dependency probes are implemented.

This is an in-process ASGI testable foundation spike, not an application feature, deployable production service, or DB integration. No secrets, credentials, user data, paid providers or external integrations. No native mobile code in this checkpoint.
