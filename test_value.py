# wrote some test cases for number.py class

import unittest
from number import Number

class TestNumber(unittest.TestCase):
    def test_add(self):
        a = Number(5)
        b = Number(10)
        c = a + b
        self.assertEqual(c.value, 15)
        d = a + 2
        self.assertEqual(d.value, 7)
        e = 2 + a
        self.assertEqual(e.value, 7)
        g = 10 + a + 2 + b + 3
        self.assertEqual(g.value, 30)
        with self.assertRaises(TypeError):
            f = a + "2"
            print(f.value)

    def test_mul(self):
        a = Number(5)
        b = Number(10)
        c = a * b
        self.assertEqual(c.value, 50)
        d = a * 2
        self.assertEqual(d.value, 10)
        e = 2 * a
        self.assertEqual(e.value, 10)
        g = 10 * a * 2 * b * 3
        self.assertEqual(g.value, 3000)
        with self.assertRaises(TypeError):
            f = a * "2"
            print(f.value)

if __name__ == "__main__":
    unittest.main()