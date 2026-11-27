import json
from pathlib import Path

from app.main import app


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / 'packages' / 'api-contracts' / 'openapi.json'


def test_openapi_snapshot_matches_runtime():
    expected = json.loads(CONTRACT.read_text(encoding='utf-8'))
    assert expected == app.openapi()


def test_health_operation_ids_are_unique():
    operations = [operation['operationId'] for path in app.openapi()['paths'].values()
                  for operation in path.values()]
    assert len(operations) == len(set(operations))
