#!/usr/bin/env python3

from collections import defaultdict

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
seq = ["N", "S", "W", "E"]


def occupied(r, c):
    return (r, c) in elves


def propose(r, c):
    free = True
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if (dr, dc) != (0, 0) and occupied(r + dr, c + dc):
                free = False
                break
    if free:
        return None

    for s in seq:
        if s == "N":
            for d in [-1, 0, 1]:
                if occupied(r - 1, c + d):
                    break
            else:
                return (r - 1, c)

        if s == "S":
            for d in [-1, 0, 1]:
                if occupied(r + 1, c + d):
                    break
            else:
                return (r + 1, c)

        if s == "W":
            for d in [-1, 0, 1]:
                if occupied(r + d, c - 1):
                    break
            else:
                return (r, c - 1)

        if s == "E":
            for d in [-1, 0, 1]:
                if occupied(r + d, c + 1):
                    break
            else:
                return (r, c + 1)
    return None


# def print_grid():
#     for r in range(nrows):
#         for c in range(ncols):
#             print("#" if occupied(r, c) else ".", end=" ")
#         print()
#     print()


with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

elves = set(
    [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]
)

for round in range(10):
    proposals = defaultdict(list)
    for r, c in elves:
        p = propose(r, c)
        if p:
            proposals[p].append((r, c))

    for dest, sources in proposals.items():
        if len(sources) == 1:
            elves.remove(sources[0])
            elves.add(dest)

    seq = seq[1:] + [seq[0]]

rmin, rmax, cmin, cmax = float("inf"), -float("inf"), float("inf"), -float("inf")
for r, c in elves:
    rmin = min(rmin, r)
    rmax = max(rmax, r)
    cmin = min(cmin, c)
    cmax = max(cmax, c)
rect_size = (rmax - rmin + 1) * (cmax - cmin + 1)
print(rect_size - len(elves))  # 4025
