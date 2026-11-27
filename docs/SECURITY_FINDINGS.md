# Findings register

NP-SEC-F001: HIGH potential supply-chain/credential exposure in legacy Antigravity workflow, based on earlier source review of external bridge and OAuth handling. OPEN; no compromise proven. Do not execute legacy workflow; owner review and authorization needed for disablement/credential revocation. Public repository visibility accepted, not credential exposure. Retest must inspect actual workflow revision and redacted authorization state.

NP-SEC-F002: MEDIUM approval integrity gap: scripts/next_task.py checks presence of approval_ref but does not authenticate its origin. OPEN; operator must independently validate reviewer identity and exact SHA, and implementation must not auto-promote. No production or external penetration tests run. This is not a zero-findings certificate.
