import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from next_task import next_tasks


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.features = [{'id': f'NP-F{i:02d}',
                          'phase': 'V1' if i <= 16 else 'YEAR1'}
                         for i in range(1, 25)]
        self.tasks = [dict(id='core', status='IN_PROGRESS', group='A',
                           features=[f['id'] for f in self.features], depends_on=[]),
                      dict(id='reader', status='BACKLOG', group='B', features=[],
                           depends_on=['CTO-GATE-01']),
                      dict(id='later', status='BACKLOG', group='YEAR1', features=[],
                           depends_on=[])]
        self.gates = []
        for i in range(1, 7):
            gate = f'CTO-GATE-{i:02d}'
            self.tasks.append(dict(id=gate, status='BLOCKED', group='A',
                                   features=[], depends_on=['core']))
            self.gates.append(dict(id=gate, status='BLOCKED'))

    def run_planner(self):
        return next_tasks(self.features, self.tasks, self.gates)

    def test_only_ready_core(self):
        self.assertEqual(self.run_planner(), ['core'])

    def test_verified_core_does_not_unlock_gate(self):
        self.tasks[0]['status'] = 'VERIFIED'
        self.assertEqual(self.run_planner(), [])

    def test_task_approval_alone_is_insufficient(self):
        self.tasks[0]['status'] = 'VERIFIED'
        self.tasks[3]['status'] = 'APPROVED'
        self.assertEqual(self.run_planner(), [])

    def test_gate_approval_needs_reference(self):
        self.tasks[0]['status'] = 'VERIFIED'
        self.tasks[3]['status'] = 'APPROVED'
        self.gates[0]['status'] = 'APPROVED'
        self.assertEqual(self.run_planner(), [])

    def test_gate_requires_prerequisite_even_with_reference(self):
        self.tasks[3]['status'] = 'APPROVED'
        self.gates[0].update(status='APPROVED', approval_ref='synthetic-review')
        self.assertEqual(self.run_planner(), ['core'])

    def test_approved_gate_enables_reader_but_not_year_one(self):
        self.tasks[0]['status'] = 'VERIFIED'
        self.tasks[3]['status'] = 'APPROVED'
        self.gates[0].update(status='APPROVED', approval_ref='synthetic-review')
        self.assertEqual(self.run_planner(), ['reader'])

    def test_missing_gate_rejected(self):
        self.gates.pop()
        with self.assertRaises(ValueError):
            self.run_planner()

    def test_cycle_rejected(self):
        self.tasks[0]['depends_on'] = ['reader']
        with self.assertRaises(ValueError):
            self.run_planner()


if __name__ == '__main__':
    unittest.main()
