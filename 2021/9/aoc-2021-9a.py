#!/usr/bin/env python3

total = 0
with open(0) as f:
    grid = [list(map(int, line.strip())) for line in f]
    nrows, ncols = len(grid), len(grid[0])

for r in range(nrows):
    for c in range(ncols):
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if grid[nr][nc] <= grid[r][c]:
                    break
        else:
            total += 1 + grid[r][c]

print(total)  # 491
