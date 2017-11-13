import unittest

from quadratic_equation import get_roots


class QuadraticEquationTestCase(unittest.TestCase):
    def test_solves_real_roots(self):
        root1, root2 = get_roots(1, -2, 1)
        self.assertEqual(root1, 1)

    def test_first_root_less_than_second(self):
        root1, root2 = get_roots(1, 2, -3)
        self.assertEqual(root1, -3)
        self.assertEqual(root2, 1)

    def test_second_root_is_none_if_one_solution(self):
        root1, root2 = get_roots(1, -2, 1)
        self.assertIsNotNone(root1)
        self.assertIsNone(root2)

    def test_returns_none_for_complex_solution(self):
        root1, root2 = get_roots(1, 2, 3)
        self.assertIsNone(root1)
        self.assertIsNone(root2)


if __name__ == '__main__':
    unittest.main()
