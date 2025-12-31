#!/usr/bin/env python3


def roll_north(r, c):
    nr, result = r, None
    while True:
        nr = nr - 1
        if nr < 0 or grid[nr][c] != ".":
            return result
        result = nr


def tilt_north():
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "O":
                rt = roll_north(r, c)
                if rt is not None:
                    grid[r][c] = "."
                    grid[rt][c] = "O"


def show_grid():
    for row in grid:
        print(" ".join(row))


with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

tilt_north()
show_grid()

total = 0
for r, row in enumerate(grid):
    for _, ch in enumerate(row):
        if ch == "O":
            total += len(grid) - r
print(total)  # 109661
