import unittest
import quadratic_equation_jparve.quadratic_solver.main as solver


class TestQuadraticSolver(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(solver.find_roots(1, 1, -2), (1.0, -2.0))

    def test_one_result(self):
        self.assertEqual(solver.find_roots(1, 0, 0), 0.0)

    def test_no_result(self):
        self.assertIsNone(solver.find_roots(1, 0, 1))
