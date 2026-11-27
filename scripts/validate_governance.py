"""Validate project registry integrity without external dependencies."""
import json
from pathlib import Path


def validate(features, tasks):
    expected = {f'NP-F{i:02d}' for i in range(1, 25)}
    feature_ids = [f['id'] for f in features]
    if len(feature_ids) != 24 or set(feature_ids) != expected:
        raise ValueError('feature IDs must be exactly NP-F01 through NP-F24')
    if {f['id'] for f in features if f['phase'] == 'V1'} != {f'NP-F{i:02d}' for i in range(1, 17)}:
        raise ValueError('invalid V1 feature scope')
    by_id = {t['id']: t for t in tasks}
    if len(by_id) != len(tasks):
        raise ValueError('duplicate task ID')
    covered = {f for t in tasks for f in t['features']}
    if covered != expected:
        raise ValueError('invalid task feature coverage')
    if not {f'CTO-GATE-{i:02d}' for i in range(1, 7)} <= by_id.keys():
        raise ValueError('missing gate')
    visiting, done = set(), set()

    def visit(task_id):
        if task_id in visiting:
            raise ValueError('dependency cycle')
        if task_id not in by_id:
            raise ValueError('unknown dependency')
        if task_id in done:
            return
        visiting.add(task_id)
        for dep in by_id[task_id]['depends_on']:
            visit(dep)
        visiting.remove(task_id)
        done.add(task_id)

    for task_id in by_id:
        visit(task_id)
    return {'features': len(features), 'tasks': len(tasks), 'gates': 6}


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1] / 'docs'
    features = json.loads((root / 'feature-registry.json').read_text(encoding='utf-8'))['features']
    tasks = json.loads((root / 'task-registry.json').read_text(encoding='utf-8'))['tasks']
    print(json.dumps(validate(features, tasks)))
