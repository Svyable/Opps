"""Exact planning-math checks; not experiment or model-performance tests."""
import unittest
from exact_power import exact_one_sided_p, unconditional_power, planning_table


class ExactPowerTests(unittest.TestCase):
    def test_no_discordance(self):
        self.assertEqual(exact_one_sided_p(0, 0), 1.0)

    def test_five_and_six_all_beneficial(self):
        self.assertEqual(exact_one_sided_p(5, 0), 0.03125)
        self.assertEqual(exact_one_sided_p(6, 0), 0.015625)

    def test_harm_not_significant(self):
        self.assertEqual(exact_one_sided_p(0, 5), 1.0)

    def test_invalid_counts(self):
        for x, y in ((-1, 0), (1.0, 0), (True, 0)):
            with self.assertRaises(ValueError):
                exact_one_sided_p(x, y)

    def test_power_under_null_below_alpha(self):
        self.assertLessEqual(unconditional_power(20, .2, .2), .025)

    def test_power_increases_with_n_for_grid_case(self):
        a = unconditional_power(20, .3, .1)
        b = unconditional_power(40, .3, .1)
        self.assertLess(a, b)
        self.assertAlmostEqual(a, .1736397148439823)

    def test_invalid_probability(self):
        for n, b, h, alpha in ((0, .2, .1, .025), (20, .8, .3, .025),
                                (20, -.1, .2, .025), (20, .2, .1, 1),
                                (20, float('nan'), .1, .025)):
            with self.assertRaises(ValueError):
                unconditional_power(n, b, h, alpha)

    def test_grid(self):
        rows = planning_table()
        self.assertEqual(len(rows), 9)
        self.assertEqual(rows[0]["pairs"], 20)
        self.assertEqual(rows[0]["power_at_alpha_0_025"], .1736)


if __name__ == "__main__":
    unittest.main()
