"""Read-only live driver probe for the approved development runtime role.

Not wired to application readiness until real target validation succeeds.
The caller injects secrets privately; neither the URL nor exceptions are logged.
"""
from sqlalchemy import create_engine, pool, text

from app.database_config import validate_runtime_database_url


CHECK_SQL = text("""
SELECT current_database() AS database_name, current_user AS role_name,
       NOT EXISTS (
           SELECT 1 FROM pg_roles r WHERE pg_has_role(current_user, r.oid, 'MEMBER')
             AND (r.rolsuper OR r.rolbypassrls OR r.rolcreaterole OR r.rolcreatedb OR r.rolreplication)
       ) AS no_privileged_memberships,
       NOT has_schema_privilege(current_user, 'nurpath', 'CREATE') AS no_schema_create,
       (SELECT count(*) FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
        WHERE n.nspname='nurpath' AND c.relname IN ('principals','external_identities','preferences')
          AND c.relkind='r' AND c.relrowsecurity AND c.relforcerowsecurity
          AND c.relowner <> (SELECT oid FROM pg_roles WHERE rolname=current_user)
          AND has_table_privilege(current_user,c.oid,'SELECT')
          AND NOT (has_table_privilege(current_user,c.oid,'INSERT')
                OR has_table_privilege(current_user,c.oid,'UPDATE')
                OR has_table_privilege(current_user,c.oid,'DELETE')
                OR has_table_privilege(current_user,c.oid,'TRUNCATE'))) = 3 AS initial_role_scope_ok
""")


def probe_runtime_database(raw: str, *, expected_host: str, expected_database: str,
                           engine_factory=create_engine) -> None:
    """Raise a generic error unless client TLS and read-only role scope pass."""
    url = validate_runtime_database_url(raw, expected_host=expected_host,
                                        expected_database=expected_database)
    engine = None
    try:
        engine = engine_factory(url, poolclass=pool.NullPool, hide_parameters=True,
                                connect_args={'connect_timeout': 5, 'application_name': 'nurpath_dev_probe'})
        with engine.connect() as connection:
            # Client libpq flag verifies the actual client-to-proxy hop;
            # pg_stat_ssl on the server is not equivalent for proxied databases.
            if connection.connection.driver_connection.pgconn.ssl_in_use is not True:
                raise RuntimeError('client TLS not active')
            connection.execute(text('SET TRANSACTION READ ONLY'))
            row = connection.execute(CHECK_SQL).mappings().one()
            if (row['database_name'] != expected_database or row['role_name'] != 'nurpath_app'
                    or any(row[k] is not True for k in ('no_privileged_memberships',
                        'no_schema_create', 'initial_role_scope_ok'))):
                raise RuntimeError('unexpected role scope')
            connection.rollback()
    except Exception:
        raise RuntimeError('runtime database probe failed') from None
    finally:
        if engine is not None:
            engine.dispose()
