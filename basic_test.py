import unittest
import calculator

class Testing(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_sum_failed(self):
        self.assertEqual(calculator.add(1, 2), 4)

    def test_sum_float_failed(self):
        self.assertEqual(calculator.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()