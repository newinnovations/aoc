#!/usr/bin/env python3

DIR = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
DIRS = [(dr, dc) for _, (dr, dc) in DIR.items()]  # speedup


def update_blizzards():
    global grid, blizzards
    new_blizzards = []
    for r, c, dir in blizzards:
        dr, dc = DIR[dir]
        r, c = r + dr, c + dc
        if r < 1:
            r = nrows - 2
        elif r > nrows - 2:
            r = 1
        if c < 1:
            c = ncols - 2
        elif c > ncols - 2:
            c = 1
        new_blizzards.append((r, c, dir))
    blizzards = new_blizzards
    for r, row in enumerate(grid):
        for c, dir in enumerate(row):
            if dir in "<>^v":
                grid[r][c] = "."
    for r, c, dir in blizzards:
        grid[r][c] = dir


def bfs(sr, sc, er, ec):
    nq = set([(sr, sc)])
    step = 0
    while True:
        q = nq
        step += 1
        nq = set()
        update_blizzards()
        for r, c in q:
            if grid[r][c] == ".":
                nq.add((r, c))
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if (nr, nc) == (er, ec):
                    return step
                if nr < nrows and grid[nr][nc] == ".":
                    nq.add((nr, nc))


total = 0
with open(0) as f:
    grid = [list(line.strip()) for line in f]
    nrows, ncols = len(grid), len(grid[0])

blizzards = [
    (r, c, ch)
    for r, row in enumerate(grid)
    for c, ch in enumerate(row)
    if ch in DIR.keys()
]

print(
    bfs(0, 1, nrows - 1, ncols - 2)
    + bfs(nrows - 1, ncols - 2, 0, 1)
    + bfs(0, 1, nrows - 1, ncols - 2)
)  # 842
