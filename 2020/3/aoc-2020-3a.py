#!/usr/bin/env python3

with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

r = c = 0
total = 0
while r < nrows:
    total += grid[r][c % ncols] == "#"
    r, c = r + 1, c + 3

print(total)  # 270
