import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_environment import parse_lock, check_versions


class EnvironmentTests(unittest.TestCase):
    def test_parse_exact_pins(self):
        self.assertEqual(parse_lock('# comment\nfastapi==0.128.2\n\n'), {'fastapi': '0.128.2'})

    def test_reject_unpinned(self):
        for line in ('fastapi>=1', 'fastapi', 'fastapi==1.*', '-r another.txt', 'fastapi @ https://example.invalid'):
            with self.subTest(line=line), self.assertRaises(ValueError):
                parse_lock(line)

    def test_reject_duplicate_names(self):
        with self.assertRaises(ValueError):
            parse_lock('typing_extensions==1.0\ntyping-extensions==1.0')

    def test_reject_empty(self):
        with self.assertRaises(ValueError):
            parse_lock('# nothing')

    def test_version_matches(self):
        self.assertEqual(check_versions({'a': '1.0'}, lambda name: '1.0'), [])

    def test_version_mismatch(self):
        self.assertEqual(check_versions({'a': '1.0'}, lambda name: '2.0'), ['a: expected 1.0, found 2.0'])

    def test_missing_version(self):
        from importlib.metadata import PackageNotFoundError
        def missing(name):
            raise PackageNotFoundError(name)
        self.assertEqual(check_versions({'a': '1.0'}, missing), ['a: not installed'])


if __name__ == '__main__':
    unittest.main()
