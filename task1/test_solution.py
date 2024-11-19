# test_solution.py

import unittest
from solution import strict, sum_two

class TestStrictDecorator(unittest.TestCase):
    def test_correct_types(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_incorrect_types(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

if __name__ == "__main__":
    unittest.main()
