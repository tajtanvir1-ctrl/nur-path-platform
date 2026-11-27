"""Explicit one-off secure read-only probe. Inject environment via a trusted secret store."""
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))
from app.database_probe import probe_runtime_database


def main():
    if os.environ.get('NP_DB_ALLOW_LIVE_READ_PROBE') != '1':
        print('Live development database probe not authorized', file=sys.stderr)
        return 1
    try:
        probe_runtime_database(os.environ['NP_DB_RUNTIME_URL'],
            expected_host=os.environ['NP_DB_EXPECTED_HOST'],
            expected_database=os.environ['NP_DB_EXPECTED_DATABASE'])
    except Exception:
        print('Live development database probe failed', file=sys.stderr)
        return 1
    print('PASS: verified client TLS and read-only database role scope')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
