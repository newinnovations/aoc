#!/usr/bin/env python3


def find(grid, type):
    n = 0
    while len(grid) > 1:
        row = next(zip(*grid))
        ones = sum(row)
        zeros = len(row) - ones
        if type == "o2":
            bit = int(ones >= zeros)
        else:  # co2
            bit = int(ones < zeros)
        n = n * 2 + bit
        grid = [row[1:] for row in grid if row[0] == bit]
    if grid:
        for bit in grid[0]:
            n = n * 2 + bit
    return n


with open(0) as f:
    grid = [list(map(int, line.strip())) for line in f]

print(find(grid, "o2") * find(grid, "co2"))  # 4790390
