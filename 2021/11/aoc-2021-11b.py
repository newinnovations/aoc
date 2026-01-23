#!/usr/bin/env python3


def do_step():
    flashed = set()
    nflashed = set()
    for r in range(nrows):
        for c in range(ncols):
            grid[r][c] += 1
            if grid[r][c] > 9:
                nflashed.add((r, c))

    while nflashed:
        flashed.update(nflashed)
        lflashed = nflashed
        nflashed = set()
        for r, c in lflashed:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = (r + dr, c + dc)
                    if 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in flashed:
                        grid[nr][nc] += 1
                        if grid[nr][nc] > 9:
                            nflashed.add((nr, nc))

    for r, c in flashed:
        grid[r][c] = 0

    return len(flashed)


total = 0
with open(0) as f:
    grid = [list(map(int, line.strip())) for line in f]
    nrows, ncols = len(grid), len(grid[0])


while True:
    total += 1
    if do_step() == nrows * ncols:
        break

for row in grid:
    print(row)

print(total)  # 303
