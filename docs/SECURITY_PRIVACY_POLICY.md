# Security and privacy baseline V0.1

Public Git repository is Founder-approved; never place credentials, recordings, private conversations, real identities or production dumps in Git or test artifacts. Use synthetic fixtures. Secrets in approved secret stores only. Legacy Antigravity third-party bridge is not trusted for execution; separately review and revoke credentials if authorized.

Require server-side ownership and role checks per object; negative cross-account tests. Admin MFA, short-lived credentials, rotation, least privilege and audit events with redaction. Private audio/consultations use scoped signed URLs, consent, configurable retention and deletion. No private reflections or location to unapproved models. Minors need age-appropriate protection and applicable consent. Define retention and jurisdiction requirements before launch.

AI retrieval uses approved immutable corpus, untrusted text isolated from instructions, citation validation and abstention. FreeLLMAPI isolated synthetic evaluation is authorized; no live connection until provider terms, privacy, dependency review and benchmark gates pass. No quota circumvention. Payments use exact minor units, receipt validation, idempotent webhooks and sandbox until approval.

No independent penetration test or production security signoff yet. Record findings, severity, reproduction, remediation and retest evidence. Critical/high unresolved findings block relevant releases.
