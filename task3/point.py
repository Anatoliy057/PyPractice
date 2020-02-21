from task3.vector2 import Vector2


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point: x = {0}, y = {1}'.format(self.x, self.y)

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def delta_x(self, p):
        return self.x - p.get_x()

    def delta_y(self, p):
        return self.y - p.get_y()

    def to_vector(self) -> Vector2:
        return Vector2(self.x, self.y)
