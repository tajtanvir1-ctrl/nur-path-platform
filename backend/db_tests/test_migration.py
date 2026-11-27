"""Only run against the disposable CI target; no cloud database writes."""
import os
from pathlib import Path
from uuid import uuid4

import pytest
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url
from sqlalchemy.exc import DBAPIError, IntegrityError

ROOT = Path(__file__).resolve().parents[1]


def test_offline_sql(capsys):
    command.upgrade(Config(str(ROOT / 'alembic.ini')), 'head', sql=True)
    sql = capsys.readouterr().out
    assert 'CREATE SCHEMA nurpath' in sql
    for name in ('principals', 'external_identities', 'preferences'):
        assert f'CREATE TABLE nurpath.{name}' in sql
        assert f'ALTER TABLE nurpath.{name} ENABLE ROW LEVEL SECURITY' in sql
        assert f'ALTER TABLE nurpath.{name} FORCE ROW LEVEL SECURITY' in sql
    assert 'DROP TABLE' not in sql


def test_online_requires_opt_in(monkeypatch):
    monkeypatch.delenv('NP_DB_ALLOW_CI_MIGRATIONS', raising=False)
    with pytest.raises(RuntimeError, match='disposable CI opt-in'):
        command.upgrade(Config(str(ROOT / 'alembic.ini')), 'head')


def test_remote_target_rejected(monkeypatch):
    monkeypatch.setenv('NP_DB_ALLOW_CI_MIGRATIONS', '1')
    monkeypatch.setenv('NP_DB_MIGRATION_URL', 'postgresql+psycopg://nurpath_ci@example.invalid:5432/nurpath_ci')
    with pytest.raises(RuntimeError, match='isolated loopback'):
        command.upgrade(Config(str(ROOT / 'alembic.ini')), 'head')


def test_actual_postgres_schema_and_deny_by_default():
    if os.environ.get('NP_DB_ALLOW_CI_MIGRATIONS') != '1':
        pytest.skip('Disposable PostgreSQL CI not supplied')
    url = make_url(os.environ['NP_DB_MIGRATION_URL'])
    assert url.drivername == 'postgresql+psycopg'
    assert (url.host, url.port, url.database, url.username, dict(url.query)) == (
        '127.0.0.1', 5432, 'nurpath_ci', 'nurpath_ci', {})
    config = Config(str(ROOT / 'alembic.ini'))
    command.upgrade(config, 'head')
    command.upgrade(config, 'head')  # versioned re-run must be a no-op
    engine = create_engine(url, hide_parameters=True)
    try:
        with engine.connect() as connection:
            assert tuple(connection.execute(text('SELECT current_database(), current_user')).one()) == ('nurpath_ci', 'nurpath_ci')
            assert connection.execute(text('SELECT version_num FROM nurpath_alembic_version')).scalar_one() == '0001_identity_foundation'
            rows = connection.execute(text("SELECT c.relname, c.relrowsecurity, c.relforcerowsecurity FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='nurpath' AND c.relkind='r' ORDER BY c.relname")).all()
            assert [tuple(r) for r in rows] == [(n, True, True) for n in ('external_identities', 'preferences', 'principals')]
            uid = uuid4()
            connection.execute(text('INSERT INTO nurpath.principals(id) VALUES (:id)'), {'id': uid})
            connection.execute(text("INSERT INTO nurpath.external_identities VALUES ('https://issuer.invalid', 'fixture', :id)"), {'id': uid})
            with pytest.raises(IntegrityError), connection.begin_nested():
                connection.execute(text("INSERT INTO nurpath.external_identities VALUES ('https://issuer.invalid', 'fixture', :id)"), {'id': uid})
            with pytest.raises(IntegrityError), connection.begin_nested():
                connection.execute(text("INSERT INTO nurpath.preferences(principal_id, locale) VALUES (:id, 'xx')"), {'id': uid})
            with pytest.raises(IntegrityError), connection.begin_nested():
                connection.execute(text('INSERT INTO nurpath.preferences(principal_id) VALUES (:id)'), {'id': uuid4()})
            connection.execute(text('CREATE ROLE nurpath_ci_probe NOLOGIN NOSUPERUSER NOBYPASSRLS'))
            connection.execute(text('GRANT USAGE ON SCHEMA nurpath TO nurpath_ci_probe'))
            connection.execute(text('GRANT SELECT, INSERT ON nurpath.principals TO nurpath_ci_probe'))
            connection.execute(text('SET LOCAL ROLE nurpath_ci_probe'))
            assert connection.execute(text('SELECT count(*) FROM nurpath.principals')).scalar_one() == 0
            with pytest.raises(DBAPIError), connection.begin_nested():
                connection.execute(text('INSERT INTO nurpath.principals(id) VALUES (:id)'), {'id': uuid4()})
            connection.rollback()  # all synthetic data/role changes rolled back
    finally:
        engine.dispose()
