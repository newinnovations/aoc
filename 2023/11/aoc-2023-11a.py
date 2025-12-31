#!/usr/bin/env python3

from itertools import combinations

with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

for _ in range(2):
    grid = [r for row in grid for r in ([row, row] if "#" not in row else [row])]
    grid = list(zip(*grid))

pos = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]

total = 0
for (ar, ac), (br, bc) in combinations(pos, 2):
    dist = abs(br - ar) + abs(bc - ac)
    total += dist
print(total)  # 9724940
