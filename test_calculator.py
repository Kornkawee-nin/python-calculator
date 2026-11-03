import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        

    # Add the following test methods to the TestCalculator class:

    def test_add2(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(4, 5), 9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(4, 5), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 13), 26)
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(8, -4), -2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(11, 2), 1)
        self.assertEqual(self.calc.modulo(10, 4), 2)

if __name__ == '__main__':
    unittest.main()