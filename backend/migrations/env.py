"""Offline SQL or explicitly opted-in, disposable CI database only."""
import os
from alembic import context
from sqlalchemy import create_engine, pool, text
from sqlalchemy.engine import make_url


def run_migrations_offline():
    context.configure(dialect_name='postgresql', literal_binds=True,
                      version_table='nurpath_alembic_version')
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    if os.environ.get('NP_DB_ALLOW_CI_MIGRATIONS') != '1':
        raise RuntimeError('Online migrations require disposable CI opt-in')
    try:
        url = make_url(os.environ.get('NP_DB_MIGRATION_URL', ''))
    except Exception:
        raise RuntimeError('Invalid disposable CI database configuration') from None
    if (url.drivername != 'postgresql+psycopg' or url.host != '127.0.0.1'
            or url.port != 5432 or url.database != 'nurpath_ci'
            or url.username != 'nurpath_ci' or url.query):
        raise RuntimeError('Only the isolated loopback CI target is allowed')
    engine = create_engine(url, poolclass=pool.NullPool, hide_parameters=True)
    try:
        with engine.connect() as connection:
            identity = connection.execute(text('SELECT current_database(), current_user')).one()
            if tuple(identity) != ('nurpath_ci', 'nurpath_ci'):
                raise RuntimeError('Unexpected database identity')
            connection.rollback()
            context.configure(connection=connection,
                              version_table='nurpath_alembic_version')
            with context.begin_transaction():
                context.run_migrations()
    finally:
        engine.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
