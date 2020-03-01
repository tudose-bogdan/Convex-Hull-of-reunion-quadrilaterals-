from functools import reduce
import matplotlib.pyplot as plt

####
#d1 = [(1,1), (3,1), (4,2), (2,2)]
#d2 = [(5,4), (6,3), (7,3), (8,4), (7, 5), (6, 5)]
d1 = [(5, 0), (7, 0), (7, 3), (5, 3)]
d2 = [(-1, -2), (1, -2), (1, 1), (-1, 1)]
####

def convex_hull_graham(points): 
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l
#Acoperirea convexa a reuniunii

d1.extend(d2)

d3 = convex_hull_graham(d1)

d3.extend(convex_hull_graham(d2))

#print(convex_hull_graham(d3))

coord = convex_hull_graham(d3)


def arata(pct):
    coord.append(coord[0])
    xs, ys = zip(*coord)
    plt.figure()
    plt.plot(xs, ys)

arata(d1)
plt.show()
arata(d2)
arata(coord)


