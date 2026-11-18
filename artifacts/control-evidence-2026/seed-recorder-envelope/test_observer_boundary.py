import unittest
from observer_boundary import run_trial

class BoundaryTests(unittest.TestCase):
    def test_authorized_write(self):
        self.assertEqual(run_trial(), 'VERIFIED')

    def test_substituted_file(self):
        self.assertEqual(run_trial(tamper=True), 'REJECT')

    def test_missing_execution(self):
        self.assertEqual(run_trial(omit=True), 'UNKNOWN')

if __name__ == '__main__':
    unittest.main()
