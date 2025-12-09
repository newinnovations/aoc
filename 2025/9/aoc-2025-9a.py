#!/usr/bin/env python3

from itertools import combinations

red_tiles = list()
with open("input.txt") as f:
    for line in f:
        red_tiles.append(tuple(map(int, line.strip().split(","))))

max_area = 0
for p1, p2 in combinations(red_tiles, 2):
    x1, y1 = p1
    x2, y2 = p2
    area = (1 + abs(x2 - x1)) * (1 + abs(y2 - y1))
    if area > max_area:
        max_area = area
print(max_area)  # 4782896435
