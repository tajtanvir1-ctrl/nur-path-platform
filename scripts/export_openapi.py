"""Export or verify the versioned FastAPI contract without network access."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend'))
from app.main import app  # noqa: E402

CONTRACT = ROOT / 'packages' / 'api-contracts' / 'openapi.json'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='explicitly update snapshot')
    args = parser.parse_args()
    expected = json.dumps(app.openapi(), indent=2, sort_keys=True) + '\n'
    if args.write:
        CONTRACT.parent.mkdir(parents=True, exist_ok=True)
        CONTRACT.write_text(expected, encoding='utf-8')
        print('OpenAPI snapshot written')
        return 0
    if not CONTRACT.is_file() or CONTRACT.read_text(encoding='utf-8') != expected:
        print('OpenAPI snapshot missing or stale; review and run --write', file=sys.stderr)
        return 1
    print('OpenAPI snapshot matches runtime')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
