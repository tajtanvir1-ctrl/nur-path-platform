"""Offline preflight for the observed Linux/Python 3.13 backend environment."""
import json
import re
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

PIN = re.compile(r'([A-Za-z0-9][A-Za-z0-9._-]*)==([0-9][A-Za-z0-9.+!-]*)')


def parse_lock(text):
    pins = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        match = PIN.fullmatch(line)
        if not match:
            raise ValueError('expected an exact package pin')
        name, value = match.groups()
        name = re.sub(r'[-_.]+', '-', name).lower()
        if name in pins:
            raise ValueError('duplicate package pin')
        pins[name] = value
    if not pins:
        raise ValueError('empty lock')
    return pins


def check_versions(pins, get_version=version):
    failures = []
    for name, expected in sorted(pins.items()):
        try:
            actual = get_version(name)
        except PackageNotFoundError:
            failures.append(f'{name}: not installed')
            continue
        if actual != expected:
            failures.append(f'{name}: expected {expected}, found {actual}')
    return failures


def main():
    if sys.platform != 'linux' or sys.version_info[:2] != (3, 13):
        print('This observed lock targets Linux / Python 3.13.', file=sys.stderr)
        return 2
    lock = Path(__file__).resolve().parents[1] / 'backend' / 'requirements-linux-py313.lock'
    try:
        pins = parse_lock(lock.read_text(encoding='utf-8'))
    except (OSError, ValueError) as error:
        print(f'Invalid lock: {error}', file=sys.stderr)
        return 2
    failures = check_versions(pins)
    print(json.dumps({'checked': len(pins), 'failures': failures}))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
