import unittest

from scripts.validate_governance import validate


class GovernanceTests(unittest.TestCase):
    def setUp(self):
        self.features = [{'id': f'NP-F{i:02d}', 'phase': 'V1' if i <= 16 else 'YEAR1'} for i in range(1, 25)]
        self.tasks = [{'id': 'work', 'depends_on': [], 'features': [f['id'] for f in self.features]}]
        self.tasks += [{'id': f'CTO-GATE-{i:02d}', 'depends_on': ['work'], 'features': []} for i in range(1, 7)]

    def test_valid(self):
        self.assertEqual(validate(self.features, self.tasks), {'features': 24, 'tasks': 7, 'gates': 6})

    def test_duplicate(self):
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            validate(self.features, self.tasks + [self.tasks[0]])

    def test_cycle(self):
        self.tasks[0]['depends_on'] = ['CTO-GATE-01']
        with self.assertRaisesRegex(ValueError, 'cycle'):
            validate(self.features, self.tasks)

    def test_unknown_dependency(self):
        self.tasks[0]['depends_on'] = ['missing']
        with self.assertRaisesRegex(ValueError, 'unknown dependency'):
            validate(self.features, self.tasks)

    def test_missing_feature_coverage(self):
        self.tasks[0]['features'].pop()
        with self.assertRaisesRegex(ValueError, 'coverage'):
            validate(self.features, self.tasks)

    def test_wrong_v1(self):
        self.features[0]['phase'] = 'YEAR1'
        with self.assertRaisesRegex(ValueError, 'V1'):
            validate(self.features, self.tasks)

    def test_missing_gate(self):
        with self.assertRaisesRegex(ValueError, 'missing gate'):
            validate(self.features, self.tasks[:-1])

    def test_missing_feature(self):
        with self.assertRaisesRegex(ValueError, 'feature IDs'):
            validate(self.features[:-1], self.tasks)
