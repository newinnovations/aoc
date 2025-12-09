#!/usr/bin/env python3

from itertools import combinations

from shapely import LineString, Polygon

red_tiles = list()
with open("ref.txt") as f:
    for line in f:
        red_tiles.append(tuple(map(int, line.strip().split(","))))

polygon = Polygon(red_tiles)

for p1, p2 in combinations(red_tiles, 2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 or y1 == y2:
        area_rect = LineString([p1, p2])
    else:
        area_rect = Polygon([p1, (x1, y2), p2, (x2, y1)])
    if polygon.covers(area_rect):
        for y in range(9):
            for x in range(14):
                if (x, y) in red_tiles:
                    print("#", end=" ")
                elif (
                    x >= min(x1, x2)
                    and x <= max(x1, x2)
                    and y >= min(y1, y2)
                    and y <= max(y1, y2)
                ):
                    print("o", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
