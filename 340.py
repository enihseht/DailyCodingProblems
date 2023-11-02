"""
This problem was asked by Google.
Given a set of points (x, y) on a 2D cartesian plane,
find the two closest points. For example, given the points
[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
return [(-1, -1), (1, 1)].
"""

from itertools import combinations

set_of_points = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]


def distcal(point_1, point_2):
    # Distance Formula = √((x2 - x1)^2 + (y2 - y1)^2)
    x1, y1 = point_1
    x2, y2 = point_2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


points_closest = None
distance_minimum = float("inf")

for point in combinations(set_of_points, 2):
    distance = distcal(point[0], point[1])
    if distance < distance_minimum:
        distance_minimum = distance
        points_closest = point

print(f"The two closest points are: {points_closest}")
