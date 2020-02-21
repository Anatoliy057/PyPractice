from task3.triangle import Triangle
from task3.point import Point
from task3.line import RayLine

triangle = Triangle(Point(1, 2), Point(3, -2), Point(-2, -1))
o = Point(0, 0)
axis = [
    RayLine(o, Point(0, 1)),
    RayLine(o, Point(1, 0)),
    RayLine(o, Point(-1, 0)),
    RayLine(o, Point(0, -1))
]
lines = triangle.get_lines()
count = 0

for l in lines:
    for ax in axis:
        if l.intersection(ax) is not None:
            print(ax)
            print(l)
            count += 1

if count != 4:
    print("No")
else:
    print("Yes")

