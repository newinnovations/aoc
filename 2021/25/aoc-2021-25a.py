#!/usr/bin/env python3


def move_one_dir(d, dr, dc):
    to_move = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if d == ch:
                nr, nc = (r + dr) % nrows, (c + dc) % ncols
                if grid[nr][nc] == ".":
                    to_move.append((r, c))

    for r, c in to_move:
        nr, nc = (r + dr) % nrows, (c + dc) % ncols
        grid[r][c] = "."
        grid[nr][nc] = d
    return len(to_move)


def do_step():
    return move_one_dir(">", 0, 1) + move_one_dir("v", 1, 0)


total = 0
with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

steps = 1
while steps:
    total += 1
    steps = do_step()


for row in grid:
    print(" ".join(row))

print()
print(total)  # 384
