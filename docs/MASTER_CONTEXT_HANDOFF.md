# Nur Path — Master context handoff V0.2

2026-11-27 | NP-CORE-001 IN_PROGRESS | starting checkpoint 80ada5344829f719c93964c0a2ffe5bde850163b | branch feat/NP-CORE-001-foundation.

Current source checkpoint: e477688d89ffbf7869e2d7b28d6db189026ff538. First executable slice: FastAPI /api/v1/health/live and /ready (503 fail-closed until real probes). In-process TDD: four red, then four green; compileall pass. Source and test Git blobs match remote. Direct dependency pins are observed local versions, not a transitive lock. Read docs/evidence-index.json for actual test scope. Immutable handoff: docs/handoffs/2026-11-27-NP-CORE-001-V0.2.md. Prior V0.1 is preserved in Git history.

Product and architecture drafts, V1 acceptance criteria, roadmap, memory, tasks, decisions, changelog, evidence index and draft CTO queue are present. All 24 feature entries remain backlog. NP-CORE-001 is not complete; next finish detailed specifications, Year-1 criteria, full task dependency registry and required documentation, then NP-CORE-002. No native Flutter SDK, PostgreSQL integration, CI, live providers, deployment or independent approval verified. FreeLLMAPI controlled evaluation authorized, not activated. No third-party installer executed. Main preserved; legacy Antigravity workflow security review pending. Derive current exact branch SHA from remote; this document cannot contain its own commit hash.

Read AGENTS.md, RESOURCE_ADOPTION.md, TASKS.md, task-registry.json and evidence-index.json before resuming.
