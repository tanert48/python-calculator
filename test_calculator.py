import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()


#add
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    # Add the following test methods to the TestCalculator class:
    def test_add_zero(self):
            self.assertEqual(self.calc.add(1, 0), 1)
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
#sub
    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)

    def test_sub_zero(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)  
#multi
    def test_mul(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def test_mul_negative(self):
        self.assertEqual(self.calc.multiply(-2, -2), 4)

    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(-5, 0), 0)
#div
    def test_div_zero(self):
        self.assertEqual(self.calc.divide(5, 0), "Eror")
    def test_div(self):
        self.assertEqual(self.calc.divide(0, 5), 0)
#mod
    def test_mod(self):
        self.assertEqual(self.calc.modulo(6, 5), 1)
    def test_mod_same(self):
        self.assertEqual(self.calc.modulo(6, 6), 0)
    

if __name__ == '__main__':
    unittest.main()