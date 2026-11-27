# Project status — checkpoint V0.4

NP-CORE-001 IN_PROGRESS. Source baseline ff1c9080c312f560dc130633088ab7ccd4e4b889. Product feature progress 0/16 verified V1, all 24 registered. Foundation: backend health spike, registry validation and dependency-ready planner. Current local run: 16 governance/planner unittest cases and 4 backend pytest cases passed. Six tested source/test blobs compared with remote. Planner only provides candidates; human review validates approval authenticity. No full runtime, native Flutter, PostgreSQL, CI, live providers or independent review. Remaining: finish canonical governance, detailed acceptance, architecture and environment. Do not claim launch-ready. Main is not changed by this increment.

V0.5 supersedes V0.4: NP-CORE-001 scoped VERIFIED; NP-CORE-002 IN_PROGRESS. 27 local test cases passed, 21 installed versions matched, Uvicorn loopback 200/503 confirmed. Flutter source generated, two widget tests NOT_RUN; CI configuration committed, run result unverified. Draft PR #1 not merged. Main not changed. All 24 features backlog; gates unchanged.

V0.9 supersedes earlier status: CORE-001 and CORE-002 scoped VERIFIED. ARCH-001 IN_PROGRESS. Run 25 native staging and backend CI successful, artifact and exact lock verified. Versioned OpenAPI and local backend six tests pass. Native APK/iOS build, auth/DB integration, domain functions, all 16 launch features and independent review remain unverified.

V0.10: CORE-001/002 and ARCH-001 scoped VERIFIED. DB-001 IN_PROGRESS. Run 44 PASS, initial database migration source committed and 3 local migration tests pass, 1 actual PostgreSQL test skipped. CI Run 64 pending; Neon application schema not applied. Product feature verification remains 0/16.
