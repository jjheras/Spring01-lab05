import unittest
from suma import suma

class TestSumar(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3,2), 5)
        self.assertEqual(suma(-1,1), 0)
        self.assertEqual(suma(-1,-1), -2)
        
if __name__ == "__main__":
    unittest.main()