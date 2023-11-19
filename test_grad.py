import unittest
from number import Number


class TestNumber(unittest.TestCase):
    def test_grad_add(self):
        a = Number(5)
        b = Number(10)
        c = a + b
        c.backward()
        self.assertEqual(c.grad, 1)
        self.assertEqual(a.grad, 1)
        self.assertEqual(b.grad, 1)
        a.grad = 0
        b.grad = 0
        c.grad = 0
        d = a + 2
        d.backward()
        self.assertEqual(d.grad, 1)
        self.assertEqual(a.grad, 1)
        a.grad = 0
        d.grad = 0  
        e = 2 + a
        e.backward()
        self.assertEqual(e.grad, 1)
        self.assertEqual(a.grad, 1)
        a.grad = 0
        e.grad = 0
        g = 10 + a + 2 + b + 3
        g.backward()
        self.assertEqual(g.grad, 1)
        self.assertEqual(a.grad, 1)
        self.assertEqual(b.grad, 1)
        a.grad = 0
        b.grad = 0
        g.grad = 0
        with self.assertRaises(TypeError):
            f = a + "2"
            print(f.value)

    def test_grad_mul(self):
        a = Number(5)
        b = Number(10)
        c = a * b
        c.backward()
        self.assertEqual(c.grad, 1)
        self.assertEqual(a.grad, 10)
        self.assertEqual(b.grad, 5)
        a.grad = 0
        b.grad = 0
        c.grad = 0
        d = a * 2
        d.backward()
        self.assertEqual(d.grad, 1)
        self.assertEqual(a.grad, 2)
        a.grad = 0
        d.grad = 0
        e = 2 * a
        e.backward()
        self.assertEqual(e.grad, 1)
        self.assertEqual(a.grad, 2)
        a.grad = 0
        e.grad = 0
        g = 10 * a * 2 * b * 3
        g.backward()
        self.assertEqual(g.grad, 1)
        self.assertEqual(a.grad, 600)
        self.assertEqual(b.grad, 300)
        a.grad = 0
        b.grad = 0
        g.grad = 0
        with self.assertRaises(TypeError):
            f = a * "2"
            print(f.value)
        
if __name__ == "__main__":
    unittest.main()