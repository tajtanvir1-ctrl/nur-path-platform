# Development environment — NP-CORE-002 partial

Observed Linux/Python 3.13.5. backend/requirements-linux-py313.lock records 21 exact installed dependency versions including transitive closure for the five direct dependencies. Not a hashed supply-chain lock or proof of a clean install. scripts/check_environment.py checks matching installed versions offline. Clean dependency resolution and artifact hashes remain pending because network is unavailable locally. Backend health contract is executable via in-process ASGI tests.

Commands from repository root:
- python scripts/check_environment.py
- python scripts/validate_governance.py
- python scripts/next_task.py
- python -m unittest discover -s tests -v
- cd backend && PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_health.py

Mobile package in apps/mobile; native SDK, platform projects, lockfile and builds pending. PostgreSQL runner and driver, Redis, Next.js portals, Docker and CI are not established. No live environment or credentials. The dependency planner must keep CORE-002 IN_PROGRESS until reproducible environment acceptance is met; safe independent preparatory work may continue. No claim of production readiness.
