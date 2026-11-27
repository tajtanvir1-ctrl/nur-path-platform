import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.database_config import validate_runtime_database_url

HOST = 'ep-example-pooler.example.invalid'
URL = f'postgresql+psycopg://nurpath_app:fixture-only@{HOST}:5432/neondb?sslmode=verify-full&sslrootcert=system'


def validate(url=URL, host=HOST, database='neondb'):
    return validate_runtime_database_url(url, expected_host=host, expected_database=database)


def test_verified_tls_and_dedicated_role():
    url = validate()
    assert url.username == 'nurpath_app'
    assert url.host == HOST
    assert url.query['sslmode'] == 'verify-full'
    assert url.query['sslrootcert'] == 'system'
    assert 'fixture-only' not in str(url)


@pytest.mark.parametrize('replacement', ['require', 'prefer', 'disable', 'verify-ca'])
def test_reject_weak_tls(replacement):
    with pytest.raises(ValueError, match='runtime database configuration rejected'):
        validate(URL.replace('verify-full', replacement))


@pytest.mark.parametrize('url', [
    URL.replace('nurpath_app:', 'nurpath_owner:'),
    URL.replace(HOST, 'other.example.invalid'),
    URL.replace(':5432/', ':5433/'),
    URL.replace('/neondb?', '/otherdb?'),
    URL.replace('postgresql+psycopg', 'postgresql'),
    URL.replace(':fixture-only@', '@'),
    URL.replace('&sslrootcert=system', ''),
    URL.replace('sslrootcert=system', 'sslrootcert=/tmp/untrusted.crt'),
    URL + '&sslmode=disable',
    URL + '&host=other.example.invalid',
    URL + '&options=-c%20role%3Dnurpath_owner',
    'not-a-url-fixture-only',
])
def test_reject_untrusted_settings_without_secret_echo(url):
    with pytest.raises(ValueError) as exc:
        validate(url)
    assert str(exc.value) == 'runtime database configuration rejected'
    assert 'fixture-only' not in str(exc.value)


def test_reject_missing_target_configuration():
    with pytest.raises(ValueError):
        validate(host='')
    with pytest.raises(ValueError):
        validate(database='')
