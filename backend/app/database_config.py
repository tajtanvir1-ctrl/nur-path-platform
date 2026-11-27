"""Validate a configured external PostgreSQL runtime target before connecting.

This is a configuration boundary, not a connection or authorization check.
Never log the supplied URL or exception from parsing it.
"""
import re

from sqlalchemy.engine import URL, make_url

RUNTIME_ROLE = 'nurpath_app'
REQUIRED_QUERY = {'sslmode': 'verify-full', 'sslrootcert': 'system'}
HOSTNAME = re.compile(r'(?=.{1,253}$)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\Z')
DATABASE = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]{0,62}\Z')


def validate_runtime_database_url(raw: str, *, expected_host: str,
                                  expected_database: str) -> URL:
    """Return a password-redacting SQLAlchemy URL or a generic rejection.

    The expected host/database must be independently supplied from the approved
    deployment configuration, not derived from the untrusted connection URL.
    Dedicated role privileges and actual TLS must still be checked at runtime.
    """
    try:
        if (not isinstance(raw, str) or not raw or any(c.isspace() for c in raw)
                or not isinstance(expected_host, str) or not HOSTNAME.fullmatch(expected_host)
                or not isinstance(expected_database, str) or not DATABASE.fullmatch(expected_database)):
            raise ValueError
        url = make_url(raw)
        if (url.drivername != 'postgresql+psycopg'
                or url.username != RUNTIME_ROLE or not url.password
                or url.host != expected_host or url.port != 5432
                or url.database != expected_database
                or dict(url.query) != REQUIRED_QUERY):
            raise ValueError
    except Exception:
        raise ValueError('runtime database configuration rejected') from None
    return url
