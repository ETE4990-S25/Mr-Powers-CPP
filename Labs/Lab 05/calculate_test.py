import unittest
from calculate import Calculator

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.add(2,2))
    
    def test_add_method_raises_typeerror(self):
        self.assertRaises(TypeError,self.calc.add, {1}, 2) 

if __name__=='__main__':
    unittest.main()