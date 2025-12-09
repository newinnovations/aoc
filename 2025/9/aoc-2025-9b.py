#!/usr/bin/env python3

from itertools import combinations

from shapely import LineString, Polygon, prepare

red_tiles = list()
with open("input.txt") as f:
    for line in f:
        red_tiles.append(tuple(map(int, line.strip().split(","))))

polygon = Polygon(red_tiles)
prepare(polygon)

max_area = 0
for p1, p2 in combinations(red_tiles, 2):
    x1, y1 = p1
    x2, y2 = p2
    area = (1 + abs(x2 - x1)) * (1 + abs(y2 - y1))
    if area > max_area:
        if x1 == x2 or y1 == y2:
            area_rect = LineString([p1, p2])
        else:
            area_rect = Polygon([p1, (x1, y2), p2, (x2, y1)])
        if polygon.covers(area_rect):
            max_area = area
print(max_area)  # 1540060480
