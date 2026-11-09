import unittest
from funding_release_gate import check_release

def entry(scope='BD-R3-THREAT', funder='bluedot', hours='12', amount='900'):
    return {'scope_id':scope,'funder':funder,'hours':hours,'amount_usd':amount}

class ReleaseGateTests(unittest.TestCase):
    def test_one(self): self.assertTrue(check_release([entry()])['ok'])
    def test_cross_funder_duplicate(self): self.assertFalse(check_release([entry(),entry(funder='ea')])['ok'])
    def test_case_whitespace_duplicate(self): self.assertFalse(check_release([entry(),entry(scope=' bd-r3-threat ',funder='ea')])['ok'])
    def test_distinct_scope(self): self.assertTrue(check_release([entry(),entry(scope='EA-R3-DEPLOY',funder='ea')])['ok'])
    def test_empty_fails_closed(self): self.assertFalse(check_release([])['ok'])
    def test_missing_scope(self): self.assertFalse(check_release([entry(scope='')])['ok'])
    def test_negative_hours(self): self.assertFalse(check_release([entry(hours='-1')])['ok'])
    def test_nonfinite(self): self.assertFalse(check_release([entry(amount='Infinity')])['ok'])
    def test_unknown_funder(self): self.assertFalse(check_release([entry(funder='unknown')])['ok'])
    def test_invalid_record(self): self.assertFalse(check_release([None])['ok'])

if __name__ == '__main__': unittest.main()
