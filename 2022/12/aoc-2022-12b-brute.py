#!/usr/bin/env python3

from collections import deque


def get_steps(start_r, start_c):
    steps = 0
    q = deque([(start_r, start_c, 0)])
    seen = set((start_r, start_c))
    while q:
        r, c, steps = q.popleft()
        if (r, c) == (end_r, end_c):
            return steps
        height = ord(maze[r][c])
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if (nr, nc) not in seen:
                    h = ord(maze[nr][nc])
                    if h - height < 2:
                        q.append((nr, nc, steps + 1))
                        seen.add((nr, nc))


def find(target):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return r, c
    raise ValueError("failed to find target")


with open(0) as f:
    maze = [list(line.strip()) for line in f]
    nrows, ncols = len(maze), len(maze[0])

start_r, start_c = find("S")
end_r, end_c = find("E")

maze[start_r][start_c] = "a"
maze[end_r][end_c] = "z"

min_steps = int(1e7)
for r in range(nrows):
    for c in range(ncols):
        if maze[r][c] == "a":
            steps = get_steps(r, c)
            if steps:
                min_steps = min(min_steps, steps)
print(min_steps)  # 363
