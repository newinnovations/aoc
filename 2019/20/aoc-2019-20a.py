#!/usr/bin/env python3

from collections import defaultdict, deque

with open(0) as f:
    grid = [list(line.rstrip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

for row in grid:
    print("".join(row))

tag_points = defaultdict(list)

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == ".":
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if "A" <= grid[r + dr][c + dc] <= "Z":
                    tag = frozenset(
                        [grid[r + dr][c + dc], grid[r + 2 * dr][c + 2 * dc]]
                    )
                    nb = (r - dr, c - dc)
                    tag_points[tag].append(((r, c), nb))

nb_map = dict()
for points in tag_points.values():
    if len(points) == 2:
        (a1, a2), (b1, b2) = points
        nb_map[a1] = b2
        nb_map[b1] = a2

start = tag_points[frozenset(["A"])][0][0]
finish = tag_points[frozenset(["Z"])][0][0]

q = deque([(start, 0)])
seen = set()

while True:

    pos, step = q.popleft()

    if pos == finish:
        print(step)  # 552
        break

    r, c = pos

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        npos = (r + dr, c + dc)
        if npos in nb_map:
            npos = nb_map[npos]
            nstep = 3
        else:
            nstep = 1
        if grid[npos[0]][npos[1]] == "." and npos not in seen:
            q.append((npos, step + nstep))
            seen.add(npos)
