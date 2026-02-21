#!/usr/bin/env python3

with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])


def num_trees(dr, dc):
    r = c = 0
    total = 0
    while r < nrows:
        total += grid[r][c % ncols] == "#"
        r, c = r + dr, c + dc
    return total


print(
    num_trees(1, 1)
    * num_trees(1, 3)
    * num_trees(1, 5)
    * num_trees(1, 7)
    * num_trees(2, 1)
)  # 2122848000
