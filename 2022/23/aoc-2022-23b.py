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


with open(0) as f:
    grid = [list(line.strip()) for line in f]

elves = set(
    [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]
)

round = 1
while True:
    proposals = defaultdict(list)
    for r, c in elves:
        p = propose(r, c)
        if p:
            proposals[p].append((r, c))

    moved = False
    for dest, sources in proposals.items():
        if len(sources) == 1:
            elves.remove(sources[0])
            elves.add(dest)
            moved = True

    if not moved:
        break

    round += 1
    seq.append(seq.pop(0))

print(round)  # 935
