import unittest
from main import square_numbers

class TestMain(unittest.TestCase):
    def test_square_numbers(self):
        self.assertEqual(square_numbers([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
        self.assertEqual(square_numbers([0, -1, -2, -3]), [0, 1, 4, 9])

if __name__ == '__main__':
    unittest.main()
