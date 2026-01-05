#!/usr/bin/env python3
import re

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
R, D, L, U = 0, 1, 2, 3
DIR = {R: (0, 1), L: (0, -1), D: (1, 0), U: (-1, 0)}
DIRV = ">v<^"


def get_next(r, c, dir):
    dr, dc = DIR[dir]
    nr, nc = r + dr, c + dc
    if nc < rsize[r][0]:
        nc = rsize[r][1]
    if nc > rsize[r][1]:
        nc = rsize[r][0]
    if nr < csize[c][0]:
        nr = csize[c][1]
    if nr > csize[c][1]:
        nr = csize[c][0]
    return nr, nc


with open(0) as f:
    lines = [line.rstrip() for line in f]

grid = [list(line) for line in lines[:-2]]
w = max(len(r) for r in grid)
grid = [list(line) + [" "] * (w - len(line)) for line in lines[:-2]]

rsize, csize = [], []
for row in grid:
    row = "".join(row).rstrip()
    rsize.append((row.count(" "), len(row) - 1))
for row in zip(*grid):
    row = "".join(row).rstrip()
    csize.append((row.count(" "), len(row) - 1))

moves = re.findall(r"(\d+|[LR])", lines[-1])

vgrid = grid.copy()
r, c = 0, rsize[0][0]
dir = 0
for move in moves:
    if move in "LR":
        dir = (dir + (1 if move == "R" else -1)) % 4
    else:
        for _ in range(int(move)):
            vgrid[r][c] = DIRV[dir]
            nr, nc = get_next(r, c, dir)
            if grid[nr][nc] == "#":
                break
            r, c = nr, nc

# for row in vgrid:
#     print(" ".join(row))

print((r + 1) * 1000 + (c + 1) * 4 + dir)  # 117102
