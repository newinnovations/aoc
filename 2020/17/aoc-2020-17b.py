#!/usr/bin/env python3

from collections import defaultdict


def neighbors(point):
    x, y, z, w = point
    res = set()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    n = (x + dx, y + dy, z + dz, w + dw)
                    if n != point:
                        res.add(n)
    return res


total = 0
with open(0) as f:
    grid = [list(line.strip()) for line in f]

space = set()
for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        if ch == "#":
            space.add((x, y, 0, 0))

# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
for _ in range(6):
    to_delete = set()
    inactives = defaultdict(int)
    for p in space:
        active_nbs = 0
        for nb in neighbors(p):
            if nb in space:
                active_nbs += 1
            else:
                inactives[nb] += 1

        if active_nbs < 2 or active_nbs > 3:
            to_delete.add(p)

    for p in to_delete:
        space.remove(p)

    for p, count in inactives.items():
        if count == 3:
            space.add(p)

print(len(space))  # 1972
