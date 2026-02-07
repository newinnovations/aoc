#!/usr/bin/env python3
import itertools


def inside_unique(x, y):
    inside = x >= 0 and y >= 0 and x < size and y < size
    unique = inside and area[y][x] != "#"
    if unique:
        area[y][x] = "#"
    return inside, unique


with open(0) as freq:
    area = [list(line.strip()) for line in freq]

ant, size = dict(), len(area)
for y in range(size):
    for x, freq in enumerate(area[y]):
        if freq != ".":
            if freq not in ant.keys():
                ant[freq] = list()
            ant[freq].append((x, y))

total = 0
for freq, pos in ant.items():
    for (x1, y1), (x2, y2) in itertools.combinations(pos, 2):
        dx, dy = x2 - x1, y2 - y1
        x, y = x1, y1
        while True:
            i, u = inside_unique(x, y)
            if not i:
                break
            total += u
            x, y = x - dx, y - dy
        x, y = x2, y2
        while True:
            i, u = inside_unique(x, y)
            if not i:
                break
            total += u
            x, y = x + dx, y + dy
print(total)  # 1169
