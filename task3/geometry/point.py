class Point(object):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        return Point(self.__x + other.get_x(), self.__y + other.get_y())

    def __sub__(self, other):
        return Point(self.__x - other.get_x(), self.__y - other.get_y())

    def __iadd__(self, other):
        self.__x += other.get_x()
        self.__y += other.get_y()
        return self

    def __isub__(self, other):
        self.__x -= other.get_x()
        self.__y -= other.get_y()
        return self

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

    def __str__(self):
        return '[{0}, {1}]'.format(self.__x, self.__y)

    def __repr__(self):
        return 'Point: [{0}, {1}]'.format(self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_coords(self):
        return self.__x, self.__y

    def dx(self, p):
        return self.__x - p.get_x()

    def dy(self, p):
        return self.__y - p.get_y()
