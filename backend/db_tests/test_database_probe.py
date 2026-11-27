from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.database_probe import probe_runtime_database

HOST = 'ep-example.example.invalid'
URL = f'postgresql+psycopg://nurpath_app:fixture-only@{HOST}:5432/neondb?sslmode=verify-full&sslrootcert=system'
ROW = {'database_name': 'neondb', 'role_name': 'nurpath_app', 'no_privileged_memberships': True,
       'no_schema_create': True, 'initial_role_scope_ok': True}


def setup_probe(*, tls=True, row=None):
    factory = MagicMock()
    engine = factory.return_value
    conn = engine.connect.return_value.__enter__.return_value
    conn.connection.driver_connection = SimpleNamespace(pgconn=SimpleNamespace(ssl_in_use=tls))
    conn.execute.return_value.mappings.return_value.one.return_value = dict(ROW if row is None else row)
    return factory, engine, conn


def run(factory, url=URL):
    probe_runtime_database(url, expected_host=HOST, expected_database='neondb', engine_factory=factory)


def test_probe_requires_client_tls_and_role_scope():
    factory, engine, conn = setup_probe()
    run(factory)
    assert str(conn.execute.call_args_list[0].args[0]) == 'SET TRANSACTION READ ONLY'
    assert factory.call_args.kwargs['hide_parameters'] is True
    conn.rollback.assert_called_once()
    engine.dispose.assert_called_once()


def test_probe_rejects_non_tls_before_sql():
    factory, engine, conn = setup_probe(tls=False)
    with pytest.raises(RuntimeError, match='runtime database probe failed'):
        run(factory)
    conn.execute.assert_not_called()
    engine.dispose.assert_called_once()


@pytest.mark.parametrize('key,value', [('role_name','neondb_owner'), ('database_name','wrong'),
    ('no_privileged_memberships',False), ('no_schema_create',False), ('initial_role_scope_ok',False)])
def test_probe_rejects_mismatches(key,value):
    factory, engine, conn = setup_probe(row={**ROW,key:value})
    with pytest.raises(RuntimeError, match='runtime database probe failed'):
        run(factory)
    engine.dispose.assert_called_once()


def test_probe_does_not_expose_connection_error():
    factory, engine, _ = setup_probe()
    engine.connect.side_effect = RuntimeError('fixture-only password')
    with pytest.raises(RuntimeError) as exc:
        run(factory)
    assert str(exc.value) == 'runtime database probe failed'
    engine.dispose.assert_called_once()


def test_bad_configuration_never_creates_engine():
    factory, _, _ = setup_probe()
    with pytest.raises(ValueError):
        run(factory, URL.replace('verify-full','disable'))
    factory.assert_not_called()
