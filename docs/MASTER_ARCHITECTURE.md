# Architecture baseline — V0.1

Flutter/Riverpod/GoRouter/Drift mobile client; FastAPI/Pydantic/SQLAlchemy/Alembic modular backend; PostgreSQL and Redis/worker when needed; Next.js admin and scholar portal. Backend owns authorization and canonical data. Client local DB owns pending offline state with durable idempotent outbox; explicit conflict policies. Private signed object access; no direct unrestricted database access. All financial amounts integer minor units with currency. UTC instants and named local timezones.

API namespace /api/v1; OpenAPI is HTTP contract authority. Current implemented boundary only live/ready health endpoints. Future domains split routers, service, repository, model and policy. Use least-privilege credentials, deterministic migrations, disposable DB for destructive tests. Gate before provider activation, live payment, production deployment and religious content release.

AI: approved corpus -> retrieval/rerank -> generation -> deterministic citation/claim checks -> response or abstention; provider-neutral interface. FreeLLMAPI approved for isolated evaluation, not yet integrated or activated. Separate Quran acoustic/forced alignment pipeline for Tajweed; generic STT is insufficient. Reviewed topic catalog for Journey. No real private queries sent to an unvalidated provider.

Design: five tabs Home, Quran, Worship, Nur AI, More; emerald #123D32, forest #397A62, gold #B89A5B, ivory #F7F5ED, sage #DEE4D8, ink #182820. Native accessibility, RTL, reduced motion and low-end Android requirements. No native build available in current environment.
