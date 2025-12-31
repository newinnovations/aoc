#!/usr/bin/env python3

from itertools import combinations

N = 1000000 - 1
with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

pos = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]

empty_row = [r for r, row in enumerate(grid) if not row.count("#")]
grid = list(zip(*grid))
empty_col = [r for r, row in enumerate(grid) if not row.count("#")]

for er in reversed(empty_row):
    pos = [(r + N, c) if r > er else (r, c) for r, c in pos]
for ec in reversed(empty_col):
    pos = [(r, c + N) if c > ec else (r, c) for r, c in pos]

total = 0
for (ar, ac), (br, bc) in combinations(pos, 2):
    dist = abs(br - ar) + abs(bc - ac)
    total += dist
print(total)  # 569052586852
