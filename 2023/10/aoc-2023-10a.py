#!/usr/bin/env python3

R, L, D, U = 1, -1, 2, -2
DIR = {R: (0, 1), L: (0, -1), D: (1, 0), U: (-1, 0)}
DIRV = "=>v^<"
DIRS = [(d, dr, dc) for d, (dr, dc) in DIR.items()]
NEXT_DIR = {
    "-": {L: L, R: R},
    "|": {U: U, D: D},
    "J": {D: L, R: U},
    "F": {L: D, U: R},
    "L": {D: R, L: U},
    "7": {U: L, R: D},
}
SHOW_MAZE = True


def find(target):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return r, c
    raise ValueError("failed to find target")


with open("input.txt") as f:
    maze = [list(line.strip()) for line in f]
    nrows, ncols = len(maze), len(maze[0])

start = find("S")

vmaze = [["."] * ncols for _ in range(nrows)]
(r, c), steps, dir = start, 0, 0

for d, dr, dc in DIRS:
    n = maze[r + dr][c + dc]
    if (
        (d == U and n in "|7F")
        or (d == D and n in "|LJ")
        or (d == R and n in "-7J")
        or (d == L and n in "-FL")
    ):
        dir = d
        break


while True:
    vmaze[r][c] = DIRV[dir]
    steps += 1
    dr, dc = DIR[dir]
    r, c = r + dr, c + dc
    if (r, c) == start:
        break
    dir = NEXT_DIR[maze[r][c]][dir]

if SHOW_MAZE:
    for row in vmaze:
        print(" ".join(row))

print(steps // 2)  # 6757
