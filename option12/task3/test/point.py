import unittest
from option12.task3.geometry.point import Point


class MyTestCase(unittest.TestCase):

    def test_add(self):
        p1 = Point(1, 3)
        p2 = Point(-2, 5)
        self.assertEqual(Point(-1, 8), p1 + p2)

    def test_sub(self):
        p1 = Point(1, 3)
        p2 = Point(-2, 5)
        self.assertEqual(Point(3, -2), p1 - p2)

    def test_iadd(self):
        p1 = Point(1, 3)
        p2 = Point(-2, 5)
        p1 += p2
        self.assertEqual(Point(-1, 8), p1)

    def test_isub(self):
        p1 = Point(1, 3)
        p2 = Point(-2, 5)
        p1 -= p2
        self.assertEqual(Point(3, -2), p1)


if __name__ == '__main__':
    unittest.main()
