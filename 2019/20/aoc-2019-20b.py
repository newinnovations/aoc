#!/usr/bin/env python3

from collections import defaultdict, deque


def on_edge(pos):
    r, c = pos
    return r == edge_min_r or r == edge_max_r or c == edge_min_c or c == edge_max_c


with open(0) as f:
    grid = [list(line.rstrip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

for row in grid:
    print("".join(row))

tag_points = defaultdict(list)

edge_min_r = edge_min_c = 1000
edge_max_r = edge_max_c = 0

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
                    edge_min_r = min(edge_min_r, r)
                    edge_max_r = max(edge_max_r, r)
                    edge_min_c = min(edge_min_c, c)
                    edge_max_c = max(edge_max_c, c)


nb_map_outside = dict()
nb_map_inside = dict()
for points in tag_points.values():
    if len(points) == 2:
        (a1, a2), (b1, b2) = points

        assert on_edge(a1) != on_edge(b1)

        if on_edge(a1):
            nb_map_outside[a1] = b2
        else:
            nb_map_inside[a1] = b2

        if on_edge(b1):
            nb_map_outside[b1] = a2
        else:
            nb_map_inside[b1] = a2

start = tag_points[frozenset(["A"])][0][0]
finish = tag_points[frozenset(["Z"])][0][0]

q = deque([(start, 0, 0)])
seen = set()

while q:

    pos, level, step = q.popleft()

    if pos == finish and level == 0:
        print(step)  # 6492
        break

    # Limit level in case of insolvable maze
    if level > 30:
        continue

    r, c = pos

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        npos = (r + dr, c + dc)
        if npos == start:
            continue
        if level > 0 and npos == finish:
            continue
        if npos in nb_map_inside:
            npos = nb_map_inside[npos]
            nstep = 3
            nlevel = level + 1
        elif npos in nb_map_outside:
            npos = nb_map_outside[npos]
            nstep = 3
            nlevel = level - 1
        else:
            nstep = 1
            nlevel = level
        if nlevel >= 0 and grid[npos[0]][npos[1]] == "." and (npos, nlevel) not in seen:
            q.append((npos, nlevel, step + nstep))
            seen.add((npos, nlevel))
