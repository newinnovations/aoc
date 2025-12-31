#!/usr/bin/env python3


def test_horizontal(grid):
    for r in range(1, len(grid)):
        num_diff = 0
        for i in range(min(r, len(grid) - r)):
            num_diff += sum(a != b for a, b in zip(grid[r - 1 - i], grid[r + i]))
        if num_diff == 1:
            return r
    return None


def test_vertical(grid):
    return test_horizontal(list(zip(*grid)))


def test(grid):
    if (pos := test_vertical(grid)) is not None:
        return pos
    if (pos := test_horizontal(grid)) is not None:
        return pos * 100
    raise ValueError("No mirror")


grids = []
with open("input.txt") as f:
    for grid in f.read().strip().split("\n\n"):
        grids.append([list(g) for g in grid.split("\n")])

print(sum(test(grid) for grid in grids))  # 22906
