#!/usr/bin/env python3


def test_horizontal(grid):
    for r in range(1, len(grid)):
        for i in range(min(r, len(grid) - r)):
            if grid[r - 1 - i] != grid[r + i]:
                break
        else:
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

print(sum(test(grid) for grid in grids))  # 27505
