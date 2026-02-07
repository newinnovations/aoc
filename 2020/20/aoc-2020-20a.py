#!/usr/bin/env python3

from collections import defaultdict


def to_int(s):
    return int(s.replace(".", "0").replace("#", "1"), 2)


T = dict()
with open(0) as f:
    tiles = f.read().split("\n\n")
    for tile in tiles:
        tile = tile.splitlines()
        if not tile:
            break
        grid = tile[1:]
        edges = set()
        edges.add(to_int(grid[0]))
        edges.add(to_int(grid[0][::-1]))
        edges.add(to_int(grid[-1]))
        edges.add(to_int(grid[-1][::-1]))
        grid = list(zip(*grid))
        s = "".join(grid[0])
        edges.add(to_int(s))
        edges.add(to_int(s[::-1]))
        s = "".join(grid[-1])
        edges.add(to_int(s))
        edges.add(to_int(s[::-1]))
        T[int(tile[0][5:-1])] = edges


C = defaultdict(set)
for k1, v1 in T.items():
    for k2, v2 in T.items():
        if k1 != k2:
            if v1 & v2:
                C[k1].add(k2)

total = 1
for k in sorted(C.keys()):
    v = C[k]
    print(k, v)
    if len(v) == 2:
        total = total * k
print()

print(total)  # 107399567124539
