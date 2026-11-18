import hashlib
import unittest
from recorder import sign, verify

KEY = b'local-demo-secret-not-for-deployment'
RUN = 'run-001'
ACTION = 'write-001'
DIGEST = hashlib.sha256(b'hello').hexdigest()
EVENT = dict(run_id=RUN, action_id=ACTION, path='sandbox/out.txt', sha256=DIGEST, observed=True)

class RecorderEnvelopeTests(unittest.TestCase):
    def check(self, event, tag=None, run=RUN, action=ACTION, digest=DIGEST):
        return verify(event, tag if tag is not None else sign(event, KEY), KEY, run, action, 'sandbox/out.txt', digest)
    def test_valid(self): self.assertEqual(self.check(EVENT), 'VERIFIED')
    def test_forged_label(self): self.assertEqual(self.check(EVENT, '0'*64), 'REJECT')
    def test_substituted_path(self):
        e = dict(EVENT, path='sandbox/evil.txt')
        self.assertEqual(self.check(e, sign(EVENT, KEY)), 'REJECT')
    def test_signed_substitution(self):
        e = dict(EVENT, path='sandbox/evil.txt')
        self.assertEqual(self.check(e), 'REJECT')
    def test_replay_other_run(self): self.assertEqual(self.check(EVENT, run='run-002'), 'REJECT')
    def test_digest_mismatch(self): self.assertEqual(self.check(EVENT, digest='f'*64), 'REJECT')
    def test_missing_event(self): self.assertEqual(self.check({}), 'UNKNOWN')
    def test_not_observed(self):
        e = dict(EVENT, observed=False)
        self.assertEqual(self.check(e), 'UNKNOWN')
    def test_extra_field(self): self.assertEqual(self.check(dict(EVENT, recorder='independent')), 'UNKNOWN')

if __name__ == '__main__': unittest.main()
