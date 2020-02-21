import hashlib


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '[{0}, {1}]'.format(self.x, self.y)

    def __repr__(self):
        return 'Point: [{0}, {1}]'.format(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def dx(self, p):
        return self.x - p.get_x()

    def dy(self, p):
        return self.y - p.get_y()
