from task3.line import SectionLine


class Triangle(object):

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_points(self):
        return self.p1, self.p2, self.p3

    def get_lines(self):
        return SectionLine(self.p1, self.p2), SectionLine(self.p2, self.p3), SectionLine(self.p3, self.p1)
