#!/usr/bin/env python3

from itertools import combinations

"""Just for fun: solution without shapely (generated from shapely based solution)"""


def orientation(a, b, c):
    """Return cross product (b-a) x (c-a); sign indicates orientation."""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a, b, p):
    """Check if point p lies on segment ab (inclusive)."""
    if orientation(a, b, p) != 0:
        return False
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[
        1
    ] <= max(a[1], b[1])


def segments_proper_intersect(a, b, c, d):
    """
    Return True if segments ab and cd intersect in a proper crossing (not just touching
    at endpoints or overlapping collinearly). We allow touches/overlaps as 'covered'.
    """
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    # Proper intersection if orientations differ strictly
    if (o1 > 0 and o2 < 0 or o1 < 0 and o2 > 0) and (
        o3 > 0 and o4 < 0 or o3 < 0 and o4 > 0
    ):
        return True

    # Otherwise, handle collinear/endpoints -> not a proper crossing (allowed)
    return False


def point_in_polygon_inclusive(pt, poly, poly_edges=None):
    """
    Ray-casting point-in-polygon with boundary included: True if inside or on edge.
    poly: list of (x, y) vertices in order.
    """
    x, y = pt
    n = len(poly)

    # Boundary check first
    if poly_edges is None:
        poly_edges = [(poly[i], poly[(i + 1) % n]) for i in range(n)]
    for a, b in poly_edges:
        if on_segment(a, b, pt):
            return True

    # Ray cast to +infinity in x direction
    inside = False
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        # Check if edge straddles the horizontal line at y
        if (y1 > y) != (y2 > y):
            # Compute x coordinate of intersection of edge with line y = constant
            # Avoid division by zero because (y1 > y) != (y2 > y) implies y1 != y2
            x_at_y = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_at_y:
                inside = not inside

    return inside


def rect_edges_from_corners(corners):
    """Return the 4 edges of a rectangle from its corners in order."""
    # corners are expected in cyclic order; if not, sort into rectangle loop:
    # We expect corners: (x1,y1), (x1,y2), (x2,y2), (x2,y1)
    return [
        (corners[0], corners[1]),
        (corners[1], corners[2]),
        (corners[2], corners[3]),
        (corners[3], corners[0]),
    ]


def polygon_covers_rectangle(poly, corners, poly_edges):
    """
    Return True if the polygon covers (contains) the entire axis-aligned rectangle.
    Boundary inclusion: touching/overlapping edges/corners are considered covered.
    Conditions:
      1) All rectangle corners are inside or on polygon boundary.
      2) No proper intersection (crossing) between rectangle edges and polygon edges.
    """
    # 1) Every vertex must be inside or on boundary
    for c in corners:
        if not point_in_polygon_inclusive(c, poly, poly_edges):
            return False

    # 2) Rectangle edges must not have proper crossing with polygon edges
    rect_edges = rect_edges_from_corners(corners)
    for ra, rb in rect_edges:
        for pa, pb in poly_edges:
            if segments_proper_intersect(ra, rb, pa, pb):
                return False

    return True


def polygon_covers_segment(poly, a, b, poly_edges):
    """
    Return True if polygon covers (contains) the entire segment ab.
    Boundary inclusion is allowed. Conditions:
      1) Both endpoints inside or on boundary.
      2) No proper intersection (crossing) between segment and polygon edges.
    """
    if not point_in_polygon_inclusive(a, poly, poly_edges):
        return False
    if not point_in_polygon_inclusive(b, poly, poly_edges):
        return False

    for pa, pb in poly_edges:
        if segments_proper_intersect(a, b, pa, pb):
            return False
    return True


def pip_cached(pt):
    if pt not in pip_cache:
        pip_cache[pt] = point_in_polygon_inclusive(pt, polygon, poly_edges)
    return pip_cache[pt]


# Overwrite the inclusion functions to use cache for corners/endpoints
def polygon_covers_rectangle_cached(corners):
    for c in corners:
        if not pip_cached(c):
            return False
    rect_edges = rect_edges_from_corners(corners)
    for ra, rb in rect_edges:
        for pa, pb in poly_edges:
            if segments_proper_intersect(ra, rb, pa, pb):
                return False
    return True


def polygon_covers_segment_cached(a, b):
    if not pip_cached(a) or not pip_cached(b):
        return False
    for pa, pb in poly_edges:
        if segments_proper_intersect(a, b, pa, pb):
            return False
    return True


# Main logic
red_tiles = []
with open("input.txt") as f:
    for line in f:
        red_tiles.append(tuple(map(int, line.strip().split(","))))

# Interpret red_tiles as polygon vertices in order
polygon = red_tiles[:]  # list of (x, y)
n = len(polygon)
poly_edges = [(polygon[i], polygon[(i + 1) % n]) for i in range(n)]

# Cache for point-in-polygon checks (same points are reused a lot)
pip_cache = {}

# Compute maximum area
max_area = 0
for p1, p2 in combinations(red_tiles, 2):
    x1, y1 = p1
    x2, y2 = p2
    area = (1 + abs(x2 - x1)) * (1 + abs(y2 - y1))
    if area > max_area:
        if x1 == x2 or y1 == y2:
            # Degenerate rectangle: a horizontal or vertical line
            if polygon_covers_segment_cached(p1, p2):
                max_area = area
        else:
            corners = [p1, (x1, y2), p2, (x2, y1)]
            if polygon_covers_rectangle_cached(corners):
                max_area = area
print(max_area)  # 1540060480
