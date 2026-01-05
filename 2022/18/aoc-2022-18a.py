#!/usr/bin/env python3

CORNERS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

droplets = set()
with open(0) as f:
    for line in f:
        x, y, z = map(int, line.strip().split(","))
        droplets.add((x, y, z))

corners = list()
for x, y, z in droplets:
    for dx, dy, dz in CORNERS:
        c = (x + dx, y + dy, z + dz)
        if c not in droplets:
            corners.append(c)

print(len(corners))  # 4548
