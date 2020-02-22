from math import hypot
from option12.task3.geometry.point import Point


class Vector2(object):

    def __init__(self, x, y):
        if x == y == 0:
            raise ValueError('Zero vector')
        self.__x = x
        self.__y = y

    def __mul__(self, other):
        return self.dot(other)

    def __add__(self, other):
        return Vector2(self.__x + other.get_x(), self.__y + other.get_y())

    def __sub__(self, other):
        return Vector2(self.__x - other.get_x(), self.__y - other.get_y())

    def __iadd__(self, other):
        self.__x += other.get_x()
        self.__y += other.get_y()
        return self

    def __isub__(self, other):
        self.__x -= other.get_x()
        self.__y -= other.get_y()
        return self

    def __neg__(self):
        return Vector2(-self.__x, -self.__y)

    def __len__(self):
        return self.__abs__()

    def __abs__(self):
        return hypot(self.__x, self.__y)

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

    def __repr__(self):
        return 'Vector2({0}, {1})'.format(self.__x, self.__y)

    def __str__(self):
        return '{{0}, {1}}'.format(self.__x, self.__y)

    def dot(self, other):
        return other.get_x() * self.__x + other.get_y() * self.__y

    def get_x(self): return self.__x

    def get_y(self): return self.__y

    def get_coords(self):
        return self.__x, self.__y

    @staticmethod
    def to_vector(from_: Point, to_: Point):
        return Vector2(to_.dx(from_), to_.dy(from_))
