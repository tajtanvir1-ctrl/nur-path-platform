"""Select dependency-ready work; never infer an independent approval."""
import json
from pathlib import Path

from validate_governance import validate

ELIGIBLE = {'BACKLOG', 'READY', 'IN_PROGRESS', 'REMEDIATION_REQUIRED'}
DONE = {'VERIFIED', 'APPROVED'}


def next_tasks(features, tasks, gates):
    validate(features, tasks)
    by_id = {task['id']: task for task in tasks}
    gate_ids = {f'CTO-GATE-{i:02d}' for i in range(1, 7)}
    gate_by_id = {gate['id']: gate for gate in gates}
    if len(gates) != 6 or set(gate_by_id) != gate_ids:
        raise ValueError('invalid gate registry')

    def satisfied(task_id):
        task = by_id[task_id]
        if task_id in gate_ids:
            # No gate can become satisfied just by changing its task status.
            # An approval record must be checked separately by the operator.
            return (task['status'] == 'APPROVED'
                    and gate_by_id[task_id]['status'] == 'APPROVED'
                    and bool(gate_by_id[task_id].get('approval_ref'))
                    and all(satisfied(dep) for dep in task['depends_on']))
        return task['status'] == 'VERIFIED' and all(
            satisfied(dep) for dep in task['depends_on'])

    # Gates are never implementation tasks; year-1 requires a separate decision.
    return [task['id'] for task in tasks
            if task['id'] not in gate_ids
            and task.get('group') in {'A', 'B', 'C', 'D', 'E', 'F'}
            and task['status'] in ELIGIBLE
            and all(satisfied(dep) for dep in task['depends_on'])]


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1] / 'docs'
    def read(name, key):
        return json.loads((root / name).read_text(encoding='utf-8'))[key]
    print(json.dumps(next_tasks(read('feature-registry.json', 'features'),
                               read('task-registry.json', 'tasks'),
                               read('quality-gates.json', 'gates'))))
