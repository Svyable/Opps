import unittest
from funding_overlap_guard import validate

BASE = dict(task_id='T1',funder='TAIF',person='Person A',date='2026-11-10',start_minute='540',end_minute='600',hours='1',rate='100',deliverable_id='D1',evidence_link='internal',approval='approved')

class GuardTests(unittest.TestCase):
    def test_clean(self): self.assertEqual(validate([BASE]), [])
    def test_cross_funder_overlap(self):
        b=dict(BASE,funder='BlueDot',task_id='T2',start_minute='570',end_minute='630',deliverable_id='D2')
        self.assertTrue(any('overlapping' in x for x in validate([BASE,b])))
    def test_same_funder_overlap(self):
        self.assertTrue(validate([BASE,dict(BASE,task_id='T2',deliverable_id='D2')]))
    def test_double_deliverable(self):
        b=dict(BASE,funder='BlueDot',person='Person B',task_id='T2')
        self.assertTrue(any('multiple funders' in x for x in validate([BASE,b])))
    def test_missing_approval(self): self.assertTrue(validate([dict(BASE,approval='pending')]))
    def test_bad_hours(self): self.assertTrue(validate([dict(BASE,hours='2')]))
    def test_bad_date(self): self.assertTrue(validate([dict(BASE,date='2026-99-10')]))
    def test_nan(self): self.assertTrue(validate([dict(BASE,rate='NaN')]))
    def test_adjacent_valid(self):
        b=dict(BASE,task_id='T2',funder='BlueDot',start_minute='600',end_minute='660',deliverable_id='D2')
        self.assertEqual(validate([BASE,b]),[])
    def test_missing_fields(self): self.assertTrue(validate([dict(BASE,evidence_link='')]))

if __name__ == '__main__': unittest.main()
