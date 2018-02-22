import unittest
import rpn
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_min(self):
        result = rpn.calculate("13 1 -")
        self.assertEqual(12, result)
    def test_mul(self):
        result = rpn.calculate("5 4 *")
        self.assertEqual(20, result)
    def test_div(self):
        result = rpn.calculate("20 4 /")
        self.assertEqual(5, result)
    def test_carat(self):
        result = rpn.calculate("4 3 ^")
        self.assertEqual(64, result)
