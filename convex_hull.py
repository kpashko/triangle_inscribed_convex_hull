from functools import reduce
from ast import literal_eval
import matplotlib #.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import UI


def graham(points):
    def less_eq(a, b):
        return (a > b) - (a < b)

    def cross_product(p1, p2, p3):
        return less_eq((p1[0] - p2[0]) * (p3[1] - p2[1]) - (p3[0] - p2[0]) * (p1[1] - p2[1]), 0)

    def _keep_left(hull, p3):
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p3) != 1:  # 1 - поворот наліво
            hull.pop()
        if not len(hull) or hull[-1] != p3:
            hull.append(p3)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


def area(a, b, c):
    return abs((b[0]*a[1]-a[0]*b[1])+(c[0]*b[1]-b[0]*c[1])+(a[0]*c[1]-c[0]*a[1]))/2

input_data = UI.draw()
# x = [(1,3), (2,3), (0,3), (5,7)]
# inp = literal_eval(x)
c_hull = list(enumerate(graham(input_data)))
A, B, C = (0, 1, 2)
n = len(c_hull)
bA, bB, bC = (A, B, C)  # The "best" triple of points

while True:  # loop A

    while True:  # loop B
        while area(c_hull[A][1], c_hull[B][1], c_hull[C][1]) <= area(c_hull[A][1], c_hull[B][1], c_hull[(C+1)%n][1]): # loop C  %n - to stay in an array
            C = (C+1) % n

        if area(c_hull[A][1], c_hull[B][1], c_hull[C][1]) <= area(c_hull[A][1], c_hull[(B+1) % n][1], c_hull[C][1]):
            B = (B+1) % n
            continue
        else:
            break

    if area(c_hull[A][1], c_hull[B][1], c_hull[C][1]) > area(c_hull[bA][1], c_hull[bB][1], c_hull[bC][1]):
        bA = A
        bB = B
        bC = C

    A = (A+1) % n
    if A == B:
        B = (B+1) % n
    if B == C:
        C = (C+1) % n
    if A == 0:
        break

convex_hull = [y for (x, y) in c_hull]
convex_hull.append(convex_hull[0])
triangle = [c_hull[bA][1], c_hull[bB][1], c_hull[bC][1], c_hull[bA][1]]
px, py = zip(*input_data)
hx, hy = zip(*convex_hull)
tx, ty = zip(*triangle)

plt.plot(px, py, 'o')
plt.plot(hx, hy, 'r-')
plt.plot(tx, ty, 'g-')
plt.margins(x=0.5, y=0.5)
plt.show()
