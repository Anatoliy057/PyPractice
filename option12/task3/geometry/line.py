from option12.task3.geometry.point import Point
from option12.task3.geometry.vector2 import Vector2


class Line(object):

    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2
        self.__v = Vector2.to_vector(p1, p2)

        dp = p2 - p1
        if not dp.get_x():
            self.__fx = None
            self.__fy = lambda y: dp.get_x() / dp.get_y() * (y - p1.get_y()) + p1.get_x()
        elif not dp.get_y():
            self.__fy = None
            self.__fx = lambda x: dp.get_y() / dp.get_x() * (x - p1.get_x()) + p1.get_y()
        else:
            self.__fx = lambda x: dp.get_y() / dp.get_x() * (x - p1.get_x()) + p1.get_y()
            self.__fy = lambda y: dp.get_x() / dp.get_y() * (y - p1.get_y()) + p1.get_x()

    def __str__(self):
        return '{0} : {1}, v = {2}'.format(self.__p1, self.__p2, self.__v)

    def __repr__(self):
        return 'Line: [{0}, {1}], v = {2}'.format(self.__p1, self.__p2, self.__v)

    def __check__(self, p):
        return p is not None

    def __inter__(self, l):
        if self.get_v() * l.get_v() == 0:
            return None

        if self.is_axis():
            if self.is_defined_x():
                y = self.__fx(0)
                return Point(l.get_fy()(y), y)
            else:
                x = self.__fy(0)
                return Point(x, l.get_fx()(x))
        else:
            p1 = self.get_p1()
            p2 = l.get_p1()
            v1, v2 = self.get_v(), l.get_v()
            a1 = v1.get_y() / v1.get_x()
            a2 = v2.get_y() / v2.get_x()
            x = (a1 * p1.get_x() - a2 * p2.get_x() - p1.get_y() + p2.get_y()) / (a1 - a2)
            y = self.__fx(x)
            return Point(x, y)

    def get_fx(self):
        return self.__fx

    def get_fy(self):
        return self.__fy

    def is_axis(self):
        return self.__fx is None or self.__fy is None

    def is_defined_x(self) -> bool:
        return self.__fx is not None

    def is_defined_y(self) -> bool:
        return self.__fy is not None

    def get_p1(self):
        return self.__p1

    def get_p2(self):
        return self.__p2

    def get_ps(self):
        return self.__p1, self.__p2

    def get_v(self) -> Vector2:
        return self.__v

    def on_line(self, p: Point) -> bool:
        return self.__check__(p) and self.distance(p) == 0

    def distance(self, p: Point) -> float:
        p1, p2 = self.get_ps()
        dp0 = p2 - p1
        dp1 = p - p1
        return dp0.get_y() * dp1.get_x() - dp0.get_x() * dp0.get_y()

    def intersection(self, l):
        p = self.__inter__(l)
        if self.__check__(p) and l.__check__(p):
            return p
        else:
            return None


class RayLine(Line):

    def __check__(self, p):
        v = self.get_v()
        p1 = self.get_p1()
        if v.get_x() > 0:
            return p.get_x() > p1.get_x()
        elif v.get_x() < 0:
            return p.get_x() < p1.get_x()

        if v.get_y() > 0:
            return p.get_y() > p1.get_y()
        elif v.get_y() < 0:
            return p.get_y() < p1.get_y()


class SectionLine(Line):

    def __check__(self, p):
        v = self.get_v()
        p1, p2 = self.get_ps()
        if v.get_y() == 0:
            if v.get_x() > 0:
                return p1.get_x() <= p.get_x() <= p2.get_x()
            else:
                return p1.get_x() >= p.get_x() >= p2.get_x()
        else:
            if v.get_y() > 0:
                return p1.get_y() <= p.get_y() <= p2.get_y()
            else:
                return p1.get_y() >= p.get_y() >= p2.get_y()
