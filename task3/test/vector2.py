import unittest
from task3.geometry.vector2 import Vector2


class MyTestCase(unittest.TestCase):

    def test_add(self):
        p1 = Vector2(1, 3)
        p2 = Vector2(-2, 5)
        self.assertEqual(Vector2(-1, 8), p1 + p2)

    def test_sub(self):
        p1 = Vector2(1, 3)
        p2 = Vector2(-2, 5)
        self.assertEqual(Vector2(3, -2), p1 - p2)

    def test_iadd(self):
        p1 = Vector2(1, 3)
        p2 = Vector2(-2, 5)
        p1 += p2
        self.assertEqual(Vector2(-1, 8), p1)

    def test_isub(self):
        p1 = Vector2(1, 3)
        p2 = Vector2(-2, 5)
        p1 -= p2
        self.assertEqual(Vector2(3, -2), p1)

    def test_dot(self):
        p1 = Vector2(1, 3)
        p2 = Vector2(-2, 5)
        self.assertEqual(13, p1 * p2)

    def test_abs(self):
        p = Vector2(-4, 3)
        self.assertEqual(5, abs(p))


if __name__ == '__main__':
    unittest.main()
