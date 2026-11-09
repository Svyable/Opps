import unittest
from funding_overlap import validate

def item(funder='bluedot', date='2027-01-01', amount='75', hours='1'):
    return dict(package='recorder', date=date, contributor='researcher', deliverable='fixture', funder=funder, hours=hours, amount_usd=amount)

class TestFundingOverlap(unittest.TestCase):
    def test_one(self): self.assertTrue(validate({'allocations':[item()]})['ok'])
    def test_two_funders_same_work_rejected(self):
        d=validate({'allocations':[item(),item(funder='ea')]})
        self.assertFalse(d['ok']); self.assertIn('duplicate work identity',d['errors'][0])
    def test_same_funder_duplicate_rejected(self): self.assertFalse(validate({'allocations':[item(),item()]})['ok'])
    def test_distinct_future_work_allowed(self): self.assertTrue(validate({'allocations':[item(),item('ea','2027-01-02')]})['ok'])
    def test_nan_rejected(self): self.assertFalse(validate({'allocations':[item(amount='NaN')]})['ok'])
    def test_negative_hours_rejected(self): self.assertFalse(validate({'allocations':[item(hours='-1')]})['ok'])
    def test_missing_funder_rejected(self):
        a=item(); del a['funder']; self.assertFalse(validate({'allocations':[a]})['ok'])
    def test_empty_document_allowed(self): self.assertEqual(validate({'allocations':[]})['allocation_count'],0)
    def test_wrong_document_rejected(self):
        with self.assertRaises(ValueError): validate({})
    def test_amount_totals(self): self.assertEqual(validate({'allocations':[item(),item('ea','2027-01-02','200')]})['total_by_funder_usd'],{'bluedot':'75','ea':'200'})
if __name__=='__main__': unittest.main()
