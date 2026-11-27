# Feature specification V0.2 — planned scope

All features BACKLOG. No content or provider approval implied. Each slice requires UI, domain service, authorization, persistence, integration tests and accessibility/localization evidence.

| ID | User journey | Data/API responsibility | Negative and boundary cases |
|---|---|---|---|
| NP-F01 | Browse verified scholars, ask privately by text/voice, track reply, dispute/refund | scholar credentials, consultation assignment, private messages, integer BDT ledger | unauthorized access, unavailable scholar, duplicate payment, 24h SLA failure |
| NP-F02 | Choose reviewed passage, listen, consent, record, receive calibrated feedback, repeat | private audio jobs, rule evaluation, confidence, deletion | unusable audio, unsupported rule, uncertain alignment, minors consent |
| NP-F03 | Browse halal listings/map, inspect evidence, save/report | merchant certification, expiry, mosque notices and educational resources | unverified/expired certificate, misleading claim, denied location |
| NP-F04 | Opt into reviewed topic journey, read daily bundle, reflect privately | approved thematic catalog, preferences, bookmarks, retention | crisis referral, no diagnosis/guarantees, opt-out and delete |
| NP-F05 | Read all 114 Surahs, navigate Juz/Ayah, search, compare attributed translation/Tafsir | immutable licensed edition, manifest, bookmarks and progress | invalid IDs, corrupt pack, missing translation, offline resume |
| NP-F06 | Choose licensed Qari, stream, repeat, download permitted audio | media rights, catalog, signed delivery and checksum | interrupted downloads, unavailable track, expired entitlement |
| NP-F07 | Select city or consent to location, see prayer times and Qibla, set reminders | calculation method, Hanafi/Shafi, timezone, manual adjustment | denied sensors, polar conditions, DST, timetable mismatch |
| NP-F08 | Browse reviewed Dua/Azkar/99 Names, counter, save and offline read | sourced text, pronunciation/audio rights, counters | unreviewed narration, missing content, counter persistence |
| NP-F09 | Ask Nur AI, inspect citations, feedback or scholar escalation | approved retrieval, claim validation, abstention, quotas | fabricated reference, prompt injection, private data leakage |
| NP-F10 | Private worship log, goals, optional city challenge | daily entries, idempotent sync, privacy | duplicate event, timezone change, opt-out, no piety ranking |
| NP-F11 | Daily reviewed Ayat, reminders and share/widget | versioned daily selection, platform widget state | midnight, denied notifications, offline, invalid share |
| NP-F12 | Swipe reviewed clips/cards, bookmark/share/report | references, licensed audio, moderation | removed media, missing rights, accessible playback |
| NP-F13 | Post, comment, report, block, appeal | community roles, moderation and audit trail | abuse, minor privacy, blocked user, removed content |
| NP-F14 | Download approved packs, read/log offline, reconnect and sync | SQLite transactions, checksums, outbox, server idempotency | replay, interruption, conflict, crash, account switch |
| NP-F15 | Switch BN/EN/AR/UR, persisted preference and RTL | UI catalog, reviewed translation metadata | missing string, mixed-direction text, font shaping |
| NP-F16 | Inspect plans, sandbox buy/restore/cancel, quota view | receipts, server entitlements, reconciliation, refunds | duplicate webhook, expired receipt, provider outage |
| NP-F17 | Enter assets/liabilities, review calculation and assumptions | reviewed zakat method, exact arithmetic | nisab source missing, currency conversion/date ambiguity |
| NP-F18 | View Islamic calendar and local observance | method and authority metadata | moon-sighting disagreement, regional adjustment |
| NP-F19 | Memorization plan, repeat and review progress | licensed audio, spaced practice, private records | offline restart, no false proficiency claims |
| NP-F20 | Guardian-managed child-safe learning | age-appropriate reviewed catalog, consent | no private public contact, parental data deletion |
| NP-F21 | Invite family, set permissions and leave | membership RBAC, invitation lifecycle | revoked invite, cross-family leakage |
| NP-F22 | Browse reviewed Hajj/Umrah guidance | versioned sources, offline checklists | outdated operational guidance, medical/emergency boundaries |
| NP-F23 | View authorized live stream | broadcast rights, availability, moderation | no rights, outage, timezone |
| NP-F24 | Browse verified merchants, checkout and dispute | catalog, order ledger, sandbox reconciliation | false halal claim, duplicate order/payment, refund |

Year-1 implementation requires a separate phase decision after V1. Acceptance targets are not measurements.
