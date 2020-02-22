from task3.geometry.point import Point
from task3.geometry.vector2 import Vector2
from task3.geometry.line import SectionLine


class Triangle(object):

    def __init__(self, p1 : Point, p2: Point, p3: Point):
        if Vector2.to_vector(p1, p2) * Vector2.to_vector(p1, p3) == 0:
            raise ValueError("All points on once line")
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def get_ps(self):
        return self.__p1, self.__p2, self.__p3

    def get_lines(self):
        p1, p2, p3 = self.get_ps()
        return SectionLine(p1, p2), SectionLine(p2, p3), SectionLine(p3, p1)
