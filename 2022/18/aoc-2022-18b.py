#!/usr/bin/env python3

from collections import deque

CORNERS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

droplets = set()
mx = my = mz = float("inf")
Mx = My = Mz = -float("inf")
with open(0) as f:
    for line in f:
        x, y, z = map(int, line.strip().split(","))
        droplets.add((x, y, z))
        mx, Mx = min(x, mx), max(x, Mx)
        my, My = min(y, my), max(y, My)
        mz, Mz = min(z, mz), max(z, Mz)

mx, my, mz, Mx, My, Mz = mx - 1, my - 1, mz - 1, Mx + 1, My + 1, Mz + 1

q = deque([(mx, my, mz)])
air = set([(mx, my, mz)])
while q:
    x, y, z = q.popleft()
    for dx, dy, dz in CORNERS:
        c = (x + dx, y + dy, z + dz)
        if c in air:
            continue
        if (
            mx <= c[0] <= Mx
            and my <= c[1] <= My
            and mz <= c[2] <= Mz
            and c not in droplets
        ):
            air.add(c)
            q.append(c)

corners = list()
for x, y, z in droplets:
    for dx, dy, dz in CORNERS:
        c = (x + dx, y + dy, z + dz)
        if c in air:
            corners.append(c)
print(len(corners))  # 2588
