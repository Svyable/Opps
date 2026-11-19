"""Negative control: a signed file-state observation is not proof of execution."""
import hashlib
import hmac
import multiprocessing as mp
from pathlib import Path
import secrets
import tempfile
import unittest

from observer_boundary import canonical, observer


class PreexistingFileNegativeControl(unittest.TestCase):
    def test_preexisting_matching_bytes_are_signed_without_executor(self):
        payload = b'authorized harmless write'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'action.txt'
            path.write_bytes(payload)  # Existing state, not an action by executor.
            key = secrets.token_bytes(32)
            parent, child = mp.Pipe(duplex=False)
            proc = mp.Process(target=observer, args=(str(path), 'run-new', 'write-1', key, child))
            proc.start()
            child.close()
            self.assertTrue(parent.poll(5), 'observer did not return evidence')
            report, tag = parent.recv()
            proc.join(5)
            self.assertEqual(proc.exitcode, 0)
            self.assertTrue(hmac.compare_digest(hmac.new(key, canonical(report), hashlib.sha256).hexdigest(), tag))
            self.assertTrue(report['observed'])
            self.assertEqual(report['sha256'], hashlib.sha256(payload).hexdigest())
            # The observation passes the prototype's receipt checks despite no executor running.
            # This is a successful *vulnerability demonstration*, not an acceptable verifier outcome.


if __name__ == '__main__':
    unittest.main()
