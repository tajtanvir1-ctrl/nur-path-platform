"""Provider-independent identity foundation; no public access or RLS policies."""
from alembic import op
import sqlalchemy as sa

revision = '0001_identity_foundation'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SCHEMA nurpath')
    op.execute('REVOKE ALL ON SCHEMA nurpath FROM PUBLIC')
    op.create_table(
        'principals',
        sa.Column('id', sa.Uuid(), primary_key=True),
        sa.Column('state', sa.String(16), nullable=False, server_default='active'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("state IN ('active', 'disabled')", name='ck_principal_state'),
        schema='nurpath',
    )
    op.create_table(
        'external_identities',
        sa.Column('issuer', sa.String(512), primary_key=True),
        sa.Column('subject', sa.String(255), primary_key=True),
        sa.Column('principal_id', sa.Uuid(), sa.ForeignKey('nurpath.principals.id'), nullable=False),
        sa.CheckConstraint("length(btrim(issuer)) > 0 AND length(btrim(subject)) > 0", name='ck_identity_nonempty'),
        schema='nurpath',
    )
    op.create_index('ix_identity_principal', 'external_identities', ['principal_id'], schema='nurpath')
    op.create_table(
        'preferences',
        sa.Column('principal_id', sa.Uuid(), sa.ForeignKey('nurpath.principals.id'), primary_key=True),
        sa.Column('locale', sa.String(2), nullable=False, server_default='bn'),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("locale IN ('bn', 'en', 'ar', 'ur')", name='ck_preference_locale'),
        schema='nurpath',
    )
    for table in ('principals', 'external_identities', 'preferences'):
        op.execute(f'REVOKE ALL ON TABLE nurpath.{table} FROM PUBLIC')
        op.execute(f'ALTER TABLE nurpath.{table} ENABLE ROW LEVEL SECURITY')
        op.execute(f'ALTER TABLE nurpath.{table} FORCE ROW LEVEL SECURITY')


def downgrade():
    raise RuntimeError('Destructive downgrade disabled; use reviewed recovery plan')
