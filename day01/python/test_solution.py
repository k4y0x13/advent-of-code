import unittest
from solution import solve_part1, solve_part2

class TestDay1(unittest.TestCase):
    def test_part1_example(self):
        test_input = """((()))"""

        self.assertEqual(solve_part1(test_input), 0)

    def test_part2_example(self):
        test_input = """())"""

        self.assertEqual(solve_part2(test_input), 3)

if __name__== "__main__":
    unittest.main()
