#!/usr/bin/env python3

# Transpose
#   grid = list(map(list, zip(*grid)))
#
# Rotate clockwise
#   grid = list(map(list, zip(*grid[::-1])))
#
# Rotate counter-clockwise
#   grid = list(map(list, zip(*grid)))[::-1]


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


def cycle():
    global grid
    for _ in range(4):
        tilt_north()
        grid = list(map(list, zip(*grid[::-1])))


def score(g):
    nrows = len(g)
    total = 0
    for r, row in enumerate(g):
        for _, ch in enumerate(row):
            if ch == "O":
                total += nrows - r
    return total


def show_grid():
    for row in grid:
        print(" ".join(row))
    print()


with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

grids, num_cycles = [], 0
while True:
    cycle()
    num_cycles += 1
    tuple_grid = tuple(tuple(g) for g in grid)
    if tuple_grid in grids:
        break
    grids.append(tuple_grid)

start = 1 + grids.index(tuple_grid)  # cycle 1 at index 0
interval = num_cycles - start
# print(start, interval)

offset = (1000000000 - start) % interval
print(score(grids[start + offset - 1]))  # 90176
