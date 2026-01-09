#!/usr/bin/env python3

from itertools import pairwise


def is_free(x, y):
    return not ((x, y) in sand or (x, y) in rocks)


rocks, sand, lowest = set(), set(), 0
with open(0) as f:
    for line in f:
        for (x1, y1), (x2, y2) in pairwise(
            [list(map(int, corner.split(","))) for corner in line.strip().split(" -> ")]
        ):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rocks.add((x, y))
            lowest = max(lowest, max(y1, y2))

contained = True
while contained:
    x, y = 500, 0
    while contained:
        if is_free(x, y + 1):
            y += 1
        elif is_free(x - 1, y + 1):
            x -= 1
            y += 1
        elif is_free(x + 1, y + 1):
            x += 1
            y += 1
        else:
            sand.add((x, y))
            break
        contained = y < lowest
print(len(sand))  # 737
