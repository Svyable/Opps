import unittest
from ec_rank_probe import integral_points, nonsingular, naive_height, search, build_report

class SearchTests(unittest.TestCase):
    def test_singularity_filter(self):
        self.assertFalse(nonsingular(0,0))
        self.assertTrue(nonsingular(-1,1))
    def test_exact_integer_points(self):
        for x,y in integral_points(-1,1,-8,8):
            self.assertEqual(y*y,x*x*x-x+1)
    def test_only_one_sign_per_x(self):
        pts=integral_points(-1,1,-8,8)
        self.assertEqual(len(pts),len({x for x,y in pts}))
        self.assertTrue(all(y>=0 for x,y in pts))
    def test_deterministic(self):
        self.assertEqual(build_report(4,7,6,2,4),build_report(4,7,6,2,4))
    def test_sorted_by_count(self):
        d=search(4,7,6,2,10)
        self.assertTrue(all(d[i]['point_count']>=d[i+1]['point_count'] for i in range(len(d)-1)))
    def test_nonsingular_candidates(self):
        self.assertTrue(all(nonsingular(*c['a_invariants'][-2:]) for c in search(5,8,7,2,10)))
    def test_report_is_not_claimed_certified(self):
        d=build_report(4,7,6,2,4)
        self.assertIn('NOT a certified rank',d['purpose'])
        self.assertTrue('canonical height-pairing independence' in d['official_verification_required'])
    def test_invalid_bounds(self):
        with self.assertRaises(ValueError): search(0,1,1,1,1)
    def test_finite_height(self):
        self.assertGreaterEqual(naive_height(-1,1),0)

if __name__=='__main__': unittest.main()
