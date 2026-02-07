#!/usr/bin/env python3
import itertools


def inside(x, y):
    res = x >= 0 and y >= 0 and x < size and y < size and area[y][x] != "#"
    if res:
        area[y][x] = "#"
    return res


with open(0) as f:
    area = [list(line.strip()) for line in f]

ant, size = dict(), len(area)
for y in range(size):
    for x, v in enumerate(area[y]):
        if v != ".":
            if v not in ant.keys():
                ant[v] = list()
            ant[v].append((x, y))

total = 0
for f, pos in ant.items():
    for (x1, y1), (x2, y2) in itertools.combinations(pos, 2):
        p1 = (x1 - (x2 - x1), y1 - (y2 - y1))
        p2 = (x2 + (x2 - x1), y2 + (y2 - y1))
        total += inside(*p1)
        total += inside(*p2)
print(total)  # 369
