import hashlib
import os
import sqlite3
import tempfile
import unittest
from recorder import sign
from replay_guard import initialize, verify_once

KEY = b'test-only-secret'
DIGEST = hashlib.sha256(b'hello').hexdigest()
EVENT = {'run_id':'r1','action_id':'a1','path':'sandbox/out.txt',
         'sha256':DIGEST,'observed':True}

class ReplayGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = os.path.join(self.temp.name, 'events.sqlite')
        self.conn = sqlite3.connect(self.db)
        initialize(self.conn)
    def tearDown(self):
        self.conn.close()
        self.temp.cleanup()
    def check(self, event=EVENT, tag=None, conn=None):
        return verify_once(conn or self.conn, event,
                           sign(event, KEY) if tag is None else tag,
                           KEY, event['run_id'], event['action_id'],
                           'sandbox/out.txt', DIGEST)
    def test_first_then_same_run_replay(self):
        self.assertEqual(self.check(), 'VERIFIED')
        self.assertEqual(self.check(), 'REJECT')
    def test_replay_after_reopen(self):
        self.assertEqual(self.check(), 'VERIFIED')
        self.conn.close()
        self.conn = sqlite3.connect(self.db)
        initialize(self.conn)
        self.assertEqual(self.check(), 'REJECT')
    def test_second_connection(self):
        with sqlite3.connect(self.db) as second:
            self.assertEqual(self.check(), 'VERIFIED')
            self.assertEqual(self.check(conn=second), 'REJECT')
    def test_invalid_does_not_consume(self):
        self.assertEqual(self.check(tag='0'*64), 'REJECT')
        self.assertEqual(self.check(), 'VERIFIED')
    def test_distinct_action_can_pass(self):
        self.assertEqual(self.check(), 'VERIFIED')
        other = dict(EVENT, action_id='a2')
        self.assertEqual(self.check(other), 'VERIFIED')
    def test_missing_schema_fails_closed(self):
        with sqlite3.connect(':memory:') as blank:
            with self.assertRaises(sqlite3.OperationalError):
                self.check(conn=blank)

if __name__ == '__main__': unittest.main()
