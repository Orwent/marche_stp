# test_app.py
import unittest
from app import addition, soustraction

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)
        self.assertEqual(soustraction(-1, -1), 0)
        self.assertEqual(soustraction(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
