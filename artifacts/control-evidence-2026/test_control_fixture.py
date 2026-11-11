import unittest
from control_fixture import run_fixture


class FixtureTests(unittest.TestCase):
    def test_allow_and_deny(self):
        decisions = [x['decision'] for x in run_fixture([{'action':'read_public'}, {'action':'write_private'}])['trace']]
        self.assertEqual(decisions, ['allow', 'deny'])

    def test_case_sensitive_fail_closed(self):
        self.assertEqual(run_fixture([{'action':'READ_PUBLIC'}])['trace'][0]['decision'], 'deny')

    def test_reproducible_digest(self):
        a = [{'action':'read_public'}, {'action':'write_private'}]
        self.assertEqual(run_fixture(a), run_fixture(a))
        self.assertNotEqual(run_fixture(a)['sha256'], run_fixture(a[::-1])['sha256'])

    def test_malformed_rejected(self):
        for request in [{}, {'action':None}, 'read_public']:
            with self.subTest(request=request), self.assertRaises(ValueError):
                run_fixture([request])

    def test_no_side_effects(self):
        request = {'action':'write_private', 'payload':{'secret':'never logged'}}
        self.assertNotIn('never logged', str(run_fixture([request])))


if __name__ == '__main__':
    unittest.main()
