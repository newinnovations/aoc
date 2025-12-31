#!/usr/bin/env python3

from shapely import Polygon

R, L, D, U = 1, -1, 2, -2
DIR = {R: (0, 1), L: (0, -1), D: (1, 0), U: (-1, 0)}
DIRS = [(d, dr, dc) for d, (dr, dc) in DIR.items()]
NEXT_DIR = {
    "-": {L: L, R: R},
    "|": {U: U, D: D},
    "J": {D: L, R: U},
    "F": {L: D, U: R},
    "L": {D: R, L: U},
    "7": {U: L, R: D},
}


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

(r, c), dir = start, 0

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

corners = []

while True:
    dr, dc = DIR[dir]
    r, c = r + dr, c + dc
    m = maze[r][c]
    if m not in "-|":
        corners.append((r, c))
    if m == "S":
        break
    dir = NEXT_DIR[m][dir]

polygon = Polygon(corners)
buffered = polygon.buffer(-0.5, join_style="mitre")
print(buffered.area)  # 523.0
