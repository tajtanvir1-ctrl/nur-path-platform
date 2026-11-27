# Risk register — baseline V0.1

| ID | Risk | Priority | Mitigation | Status |
|---|---|---|---|---|
| R01 | Unlicensed or inaccurate Quran/Hadith | Critical | Edition rights, checksums, qualified reviewer | Open |
| R02 | AI fabricates religious rulings | Critical | Verified retrieval, citation and abstention gates; independent locked holdout | Open |
| R03 | Unauthorized private recording or consultation access | High | Object-level access, redaction, signed URLs and negative tests | Open |
| R04 | Free provider reliability and privacy | High | Isolated evaluation, provider-neutral routing, no live traffic | Open |
| R05 | Legacy agent bridge and public session files | High | Do not execute; review credential lifecycle separately | Open |
| R06 | Native/DB environment unavailable | High | Verified CI runner and device/DB evidence before gate | Open |
| R07 | Unsaved or concurrent changes | High | Exact branch SHA, bounded commits, remote readback | Mitigated in scoped runs |
| R08 | Financial duplicate event | High | Integer ledger, idempotent transactions, sandbox verification | Open |
| R09 | Child/community abuse | High | Consent, moderation, reporting and access tests | Open |
| R10 | No independent gate approval | High | External reviewer bound to SHA | Open |
