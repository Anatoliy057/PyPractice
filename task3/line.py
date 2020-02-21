from task3.point import Point
from task3.vector2 import Vector2


class Line(object):

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.v = Vector2(p1, p2)

    def __str__(self):
        return '{0}: {1}; {2}'.format(type(self), self.p1, self.p2)

    def __inter__(self, l):
        if self.get_vector().dot(l.get_vector()) == 0:
            return None

        arg = l.main_arg()

        a, c = self.get_ac(arg)
        b, d = l.get_ac(arg)

        x = (d - c) / (a - b)
        y = a * x + c
        return Point(x, y)

    def get_point1(self):
        return self.p1

    def get_point2(self):
        return self.p2

    def get_points(self):
        return self.p1, self.p2

    def get_vector(self) -> Vector2:
        return self.v

    def on_line(self, p: Point) -> bool:
        return self.distance(p) == 0

    def distance(self, p: Point) -> float:
        p1, p2 = self.get_points()
        dy = p2.delta_y(p1)
        dx = p2.delta_x(p1)
        return dy * (p.get_x() - p1.get_x()) - dx * (p.get_y() - p1.get_y())

    def intersection(self, l):
        p = self.__inter__(l)
        if p is not None and self.__check_p__(p) and l.__check_p__(p):
            return p
        else:
            return None

    def __check_p__(self, p: Point):
        return True

    def get_ac(self, arg: int):
        p1, p2 = self.get_points()
        if arg == 0:
            a = p2.delta_x(p1) / p2.delta_y(p1)
            c = -a * p1.get_y() + p1.get_x()
        else:
            a = p2.delta_y(p1) / p2.delta_x(p1)
            c = -a * p1.get_x() + p1.get_y()
        return a, c

    def main_arg(self) -> int:
        i = 0
        while i < self.v.size():
            if self.v.at(i):
                return i
            i += 1
        return -1


class RayLine(Line):

    def on_line(self, p: Point) -> bool:
        return self.distance(p) == 0 & self.__check_p__(p)

    def __check_p__(self, p: Point) -> bool:
        v = Vector2(self.p1, p)
        n = self.v
        return v.get_x() * n.get_x() >= 0 and v.get_y() * n.get_y() >= 0


class SectionLine(RayLine):

    def __len__(self):
        return self.v.__len__()

    def __check_p__(self, p: Point) -> bool:
        p1, p2 = self.get_points()

        if p1.get_x() != p2.get_x():
            a, c = p1.get_x(), p2.get_x()
            b = p.get_x()
        else:
            a, c = p1.get_y(), p2.get_y()
            b = p.get_y()
        if a > c:
            a, c = c, a
        return a <= b <= c
