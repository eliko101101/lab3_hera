import unittest
from lab2 import Weight


class TestProgression(unittest.TestCase):
    test = Weight(4.75)
    def test_add__(self):
        self.assertEqual(self.test.__add__(2), 6.75)
        self.assertEqual(self.test.__add__(3.46), 8.21)
        self.assertTrue(self.test.__add__(487), isinstance(self.test.__add__(487), float))
        self.assertRaises(TypeError, self.test.__add__, "hello")

    def test_sub__(self):
        self.assertEqual(self.test.__sub__(8), -3.25)
        self.assertEqual(self.test.__sub__(2), 2.75)
      


    def test_mul__(self):
        self.assertEqual(self.test.__mul__(7), 35.25)
        self.assertEqual(self.test.__mul__(3), 14.25)




if __name__ == '__main__':
    unittest.main()
