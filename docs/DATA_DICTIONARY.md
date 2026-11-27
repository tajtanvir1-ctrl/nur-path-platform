# Data dictionary — initial migration

| Table / field | Type | Rule |
|---|---|---|
| principals.id | UUID | App-owned primary key, supplied by server |
| principals.state | varchar(16) | active/disabled; default active |
| principals.created_at | timestamptz | Non-null, database now() |
| external_identities.issuer | varchar(512) | Verified token issuer; part of composite PK, nonblank |
| external_identities.subject | varchar(255) | Verified subject; part of composite PK, nonblank |
| external_identities.principal_id | UUID | FK to principal; indexed, non-null |
| preferences.principal_id | UUID | PK/FK to principal |
| preferences.locale | varchar(2) | bn/en/ar/ur; default bn |
| preferences.updated_at | timestamptz | Non-null; default now(); future service updates explicitly |

Identity and preferences are private. No cross-account access by default. No provider tokens, passwords or credentials in this schema. Future feature tables are added incrementally; not modeled or tested here.
