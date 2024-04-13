import unittest
from calculos import suma,resta,multiplicacion,division

class TestSumar(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3,2), 5)
        self.assertEqual(suma(-1,1), 0)
        self.assertEqual(suma(-1,-1), -2)
        
class TestRestar(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(3,2), 1)
        self.assertEqual(resta(2,5), -3)
        self.assertEqual(resta(-1,1), -2)
        self.assertEqual(resta(1,1), 0)
        self.assertEqual(resta(-1,-1), 0)
        self.assertEqual(resta(1,-1), 2)

class TestMultipliar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicacion(3,2), 6)
        self.assertEqual(multiplicacion(5,0), 0)
        self.assertEqual(multiplicacion(6,-2), -12)
        self.assertEqual(multiplicacion(0,5), 0)

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(division(10,5), 2)
        self.assertEqual(division(6,-2), -3)
        self.assertEqual(division(0,2), 0)
        self.assertEqual(division(8,0), "Error, ZeroDivisionError")
        
if __name__ == "__main__":
    unittest.main()