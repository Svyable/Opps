import unittest
from fractions import Fraction as F
from ec_rank_relation_audit import add,negate,on_curve,relation_audit


class ExactGroupLawTests(unittest.TestCase):
    def test_identity_and_inverse(self):
        p=(F(2),F(2))
        self.assertEqual(add(None,p,-28),p)
        self.assertEqual(add(p,negate(p),-28),None)

    def test_exact_double(self):
        self.assertEqual(add((F(2),F(2)),(F(2),F(2)),-28),(F(12),F(38)))

    def test_exact_relation(self):
        p=[(-6,2),(-2,10),(12,38)]
        r=relation_audit(-28,52,p)
        self.assertTrue(any(x['i']==0 and x['j']==1 and x['k']==2 and x['sign']==-1 for x in r))

    def test_offcurve_rejected(self):
        with self.assertRaisesRegex(ValueError,'off-curve'):
            relation_audit(-28,52,[(0,0)])

    def test_singular_rejected(self):
        with self.assertRaisesRegex(ValueError,'singular'):
            relation_audit(0,0,[])

    def test_repeated_rejected(self):
        with self.assertRaisesRegex(ValueError,'repeated'):
            relation_audit(-28,52,[(2,2),(2,2)])

    def test_signs(self):
        p=(F(4),F(2))
        self.assertTrue(on_curve(p,-28,52))
        self.assertTrue(on_curve(negate(p),-28,52))

    def test_zero_y_double(self):
        self.assertIsNone(add((F(0),F(0)),(F(0),F(0)),-1))


if __name__=='__main__':
    unittest.main()
