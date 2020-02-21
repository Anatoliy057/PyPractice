from math import hypot
from task3.point import Point


class Vector2(object):

    def __init__(self, x, y):
        self.coords = (x, y)

    def __mul__(self, vector):
        return vector.get_x() * self.get_x() + vector.get_y() * self.get_y()

    def __add__(self, other):
        return Vector2(self.get_x() + other.get_x(), self.get_y() + other.get_y())

    def __sub__(self, other):
        return Vector2(self.get_x() - other.get_x(), self.get_y() - self.get_y())

    def __iadd__(self, other):
        i = 0
        while i < len(self.coords):
            self.coords[i] += other.at(i)
            i += 1

    def __isub__(self, other):
        i = 0
        while i < len(self.coords):
            self.coords[i] -= other.at(i)
            i += 1

    def __neg__(self):
        return Vector2(-self.get_x(), -self.get_y())

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return hypot(self.get_x(), self.get_y())

    def __iter__(self):
        return self.coords

    def __repr__(self):
        return 'Vector2({0}, {1})'.format(self.get_x(), self.get_y())

    def __str__(self):
        return '{{0}, {1}}'.format(self.get_x(), self.get_y())

    def __getitem__(self, key):
        return self.coords[key]

    def get_x(self): return self.coords[0]

    def get_y(self): return self.coords[1]

    @staticmethod
    def to_vector(p1: Point, p2: Point):
        return Vector2(p2.delta_x(p1), p2.delta_y(p1))
