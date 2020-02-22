from task3.geometry.line import RayLine
from task3.geometry.point import Point
from task3.geometry.triangle import Triangle


p = Point(0, 0)
axis = [
    RayLine(p, Point(1, 0)),
    RayLine(p, Point(0, 1)),
    RayLine(p, Point(-1, 0)),
    RayLine(p, Point(0, -1)),
]

t = Triangle(Point(1, 2), Point(3, -2), Point(0, 0))
lines = t.get_lines()
count = 0
for ax in axis:
    for l in lines:
        if ax.intersection(l):
            count += 1

print(count)