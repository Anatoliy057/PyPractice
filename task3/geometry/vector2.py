from math import hypot
from task3.geometry.point import Point


class Vector2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return self.dot(other)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __len__(self):
        return self.__abs__()

    def __abs__(self):
        return hypot(self.x, self.y)

    def __iter__(self):
        return (self.x, self.y).__iter__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Vector2({0}, {1})'.format(self.x, self.y)

    def __str__(self):
        return '{{0}, {1}}'.format(self.x, self.y)

    def dot(self, other):
        return other.x * self.x + other.y * self.y

    def get_x(self): return self.x

    def get_y(self): return self.y

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def to_vector(_from: Point, _to: Point):
        return Vector2(_to.dx(_from), _to.dy(_from))
